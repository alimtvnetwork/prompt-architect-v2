import os
import sys
import argparse
import shutil
import subprocess
from pathlib import Path

# --- Core Utilities ---

def log(msg, verbose=False, is_verbose_msg=False):
    if not is_verbose_msg or (is_verbose_msg and verbose):
        print(msg)

def get_safe_path(path_str):
    """Safely handle Windows MAX_PATH limitations by using \\?\ prefix for absolute paths."""
    abs_path = os.path.abspath(path_str)
    if os.name == 'nt' and not abs_path.startswith('\\\\?\\'):
        return '\\\\?\\' + abs_path
    return abs_path

def safe_rename(old_path_str, new_path_str, dry_run=False, verbose=False):
    """Attempt `git mv` first to preserve history, fallback to `os.rename`."""
    if dry_run:
        log(f"[DRY-RUN] Would rename: {os.path.basename(old_path_str)} -> {os.path.basename(new_path_str)}")
        return

    try:
        subprocess.run(['git', 'mv', old_path_str, new_path_str], check=True, capture_output=True, text=True)
        log(f"[GIT MV] {os.path.basename(old_path_str)} -> {os.path.basename(new_path_str)}", verbose, True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            os.rename(get_safe_path(old_path_str), get_safe_path(new_path_str))
            log(f"[OS RENAME] {os.path.basename(old_path_str)} -> {os.path.basename(new_path_str)}", verbose, True)
        except Exception as e:
            print(f"[ERROR] Failed to rename {old_path_str}: {e}")

def should_ignore(name, path_str, except_patterns):
    """Check if a file or directory should be ignored."""
    if name in ['node_modules', '.git', '__pycache__', '.venv']:
        return True
    
    path_obj = Path(path_str)
    for pattern in except_patterns:
        pattern = pattern.strip()
        if not pattern:
            continue
        if path_obj.match(pattern) or name == pattern:
            return True
    return False

# --- Feature 1: Lowercase Renamer ---

def command_lowercase(args):
    target = args.target_directory
    except_patterns = args.except_list.split(',') if args.except_list else []
    dry_run = args.dry_run
    verbose = args.verbose
    
    log(f"Lowercasing files in {target}...", verbose)
    if dry_run: log("[DRY-RUN MODE ENABLED]")
    
    renames = []
    
    for root, dirs, files in os.walk(target):
        # Modify dirs in-place to prune ignored directories
        dirs[:] = [d for d in dirs if not should_ignore(d, os.path.join(root, d), except_patterns)]
        
        for file in files:
            if should_ignore(file, os.path.join(root, file), except_patterns):
                continue
                
            old_path = os.path.join(root, file)
            name, ext = os.path.splitext(file)
            
            # Enforce .md strictly, lowercase the rest
            new_ext = '.md' if ext.lower() == '.md' else ext.lower()
            new_name = name.lower() + new_ext
            
            if file != new_name:
                new_path = os.path.join(root, new_name)
                renames.append((old_path, new_path))
                
    for old_p, new_p in renames:
        safe_rename(old_p, new_p, dry_run, verbose)
        
    log(f"Processed {len(renames)} files for lowercasing.")

# --- Feature 2: Fix File Sequencing ---

def parse_sequence(filename):
    """Extracts numeric prefix and the rest of the filename (e.g. '01-notes.md' -> (1, '-notes.md'))"""
    import re
    match = re.match(r'^(\d+)(.*)$', filename)
    if match:
        return int(match.group(1)), match.group(2)
    return None, filename

def command_fix_seq(args):
    target = args.target_directory
    dry_run = args.dry_run
    verbose = args.verbose
    
    log(f"Fixing sequences in {target}...", verbose)
    if not os.path.isdir(target):
        print(f"Error: {target} is not a valid directory.")
        sys.exit(1)
        
    files = [f for f in os.listdir(target) if os.path.isfile(os.path.join(target, f))]
    
    # Parse pinned files
    pinned = {}
    if args.pin:
        pairs = args.pin.split(',')
        for pair in pairs:
            if '=' in pair:
                k, v = pair.split('=')
                try:
                    pinned[k.strip()] = int(v.strip())
                except ValueError:
                    pass
                    
    # Sort files based on strategy
    if args.order_by_time:
        files.sort(key=lambda x: os.path.getmtime(os.path.join(target, x)))
    elif args.order_by_az:
        files.sort(key=lambda x: parse_sequence(x)[1].lower())
    else:
        files.sort()
        
    used_seqs = set(pinned.values())
    
    if args.keep_old_order:
        for f in files:
            seq, _ = parse_sequence(f)
            if seq is not None and seq not in used_seqs:
                pass 
    
    current_seq = 1
    rename_count = 0
    for file in files:
        old_path = os.path.join(target, file)
        
        assigned_seq = None
        for k, v in pinned.items():
            if k in file:
                assigned_seq = v
                break
                
        if assigned_seq is None:
            while current_seq in used_seqs:
                current_seq += 1
            assigned_seq = current_seq
            current_seq += 1
            used_seqs.add(assigned_seq)
            
        _, remainder = parse_sequence(file)
        if remainder and not remainder.startswith('-') and not remainder.startswith('_') and not remainder.startswith('.'):
            remainder = '-' + remainder
            
        new_name = f"{assigned_seq:02d}{remainder}"
        
        if file != new_name:
            new_path = os.path.join(target, new_name)
            safe_rename(old_path, new_path, dry_run, verbose)
            rename_count += 1
            
    log(f"Re-sequenced {rename_count} files.")

# --- Feature 3: Fix Encoding ---

def command_fix_encoding(args):
    target = args.target_directory
    dry_run = args.dry_run
    verbose = args.verbose
    
    log(f"Fixing encoding in {target}...")
    if dry_run: log("[DRY-RUN MODE ENABLED]")
    
    fixed_count = 0
    for root, dirs, files in os.walk(target):
        if 'node_modules' in root or '.git' in root or '__pycache__' in root:
            continue
            
        for file in files:
            if file.endswith(('.md', '.txt', '.py', '.json', '.go', '.yaml', '.yml', '.sh', '.ps1')):
                path = os.path.join(root, file)
                try:
                    with open(get_safe_path(path), 'rb') as f:
                        raw = f.read()
                        
                    changed = False
                    
                    if raw.startswith(b'\xff\xfe') or raw.startswith(b'\xfe\xff'):
                        raw = raw.decode('utf-16').encode('utf-8')
                        changed = True
                    
                    if raw.startswith(b'\xef\xbb\xbf'):
                        raw = raw[3:]
                        changed = True
                        
                    if b'\r\n' in raw:
                        raw = raw.replace(b'\r\n', b'\n')
                        changed = True
                        
                    if changed:
                        if dry_run:
                            log(f"[DRY-RUN] Would fix encoding for: {path}")
                        else:
                            with open(get_safe_path(path), 'wb') as f:
                                f.write(raw)
                            log(f"[FIXED] {path}", verbose, True)
                        fixed_count += 1
                except Exception as e:
                    print(f"[ERROR] Failed {path}: {e}")
                    
    log(f"Total files fixed: {fixed_count}")

# --- CLI Setup ---

def main():
    parser = argparse.ArgumentParser(description="AI File Manipulator CLI - Mass rename, sequence, and encode.")
    
    # Global flags
    parser.add_argument('--dry-run', action='store_true', help="Preview changes without modifying files")
    parser.add_argument('--verbose', action='store_true', help="Enable detailed logging output")
    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Lowercase
    parser_lower = subparsers.add_parser('lowercase', help="Convert files to lowercase recursively.")
    parser_lower.add_argument('target_directory', type=str, help="Target directory to process")
    parser_lower.add_argument('--except', dest="except_list", type=str, help="Comma separated list of patterns to ignore")
    
    # Sequence
    parser_seq = subparsers.add_parser('fix-seq-files', help="Re-sequence numbered files in a directory.")
    parser_seq.add_argument('target_directory', type=str, help="Target directory")
    parser_seq.add_argument('--order-by-time', action='store_true', help="Order by modification time")
    parser_seq.add_argument('--order-by-az', action='store_true', help="Order alphabetically")
    parser_seq.add_argument('--keep-old-order', action='store_true', help="Preserve existing sequences where possible")
    parser_seq.add_argument('--pin', type=str, help="Comma separated key=seq mappings (e.g. readme=00,intro=01)")
    
    # Encoding
    parser_enc = subparsers.add_parser('fix-encoding', help="Aggressively strip BOMs and convert CRLF to LF.")
    parser_enc.add_argument('target_directory', type=str, help="Target directory")
    
    args = parser.parse_args()
    
    if args.command == 'lowercase':
        command_lowercase(args)
    elif args.command == 'fix-seq-files':
        command_fix_seq(args)
    elif args.command == 'fix-encoding':
        command_fix_encoding(args)

if __name__ == "__main__":
    main()
