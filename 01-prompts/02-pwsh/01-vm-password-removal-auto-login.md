# VM Password Removal and Auto Login Scripts

## Prompt

Hi there. Can you please write, root of the repo as a PowerShell script? So create a folder called PowerShell. And currently, I'm stuck with my Windows Server, which is under my VM. I forgot the user password. Or let's say I'm logged into my user. And I wanted to change the password to empty or remove the password. Write a script for an AI so that it can understand and follow through. See that, and also wherever the policies needs to change in order to make that password set as an empty password or a single character. So the thing is that I wanted to log into the VM very quickly, so I wanted to have like one character password or no password at all, auto login in my VM. So once I logged in inside the VM, I wanted to run that script so that it removes the password. So it should have a function. So create the function. Based on the function, I pass the username of the Windows server username, and then it removes the password and changes the policies and everything else. Same thing I wanted to do for the shell script, for Linux or Ubuntu. So we should do it for Windows Server, Windows 10, Windows 11 as well. Do you understand me? If you understood, let me know, and then write the scripts, each script. PowerShell scripts write on 01 PowerShell folder as a 01, 02 sequence of the script name, and also for Ubuntu, keep that under the Ubuntu folder, 02 Ubuntu folder. Keep it modular and write it as a function so that anyone can call it, and also write the description of it in the root readme file. Root readme file needs to be lowercase in the repo. Do you understand? Can you please follow through?

## Action Items — Must Follow (Non-Negotiable)

- [ ] Create a PowerShell scripts folder at the repo root.
- [ ] Inside it, use `01-powershell/` for PowerShell scripts and `02-ubuntu/` for shell scripts.
- [ ] Name every script with a two-digit sequence prefix: `01-<slug>.ps1`, `02-<slug>.ps1`, `01-<slug>.sh`.
- [ ] Write each script modularly, exposing a callable function (not top-level procedural code).
- [ ] The function takes the target username as a parameter.- [ ] The function must remove the user's password (set it to empty) or set a single-character password.
- [ ] Change every policy required to allow an empty/short password (minimum password length, complexity, "Limit local account use of blank passwords to console logon only").
- [ ] Configure auto login so the VM signs in without prompting.
- [ ] Support Windows Server, Windows 10 and Windows 11.
- [ ] Provide the Ubuntu/Linux equivalent as a shell script under `02-ubuntu/`, same modular function style
