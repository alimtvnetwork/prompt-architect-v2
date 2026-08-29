# Instruction (must follow): Coding Guideline Execution — React & Frontend Architecture

Trigger Keywords & Aliases: `cg-react`, `cg-execute react`, `audit react`, `fix frontend guidelines`, `enforce react standards`

```text
N = 100
```

N = total self-loop steps budget for scanning, spec planning, and autonomously resolving all React and frontend guideline violations.

- [ ] /goal First `N/2` steps (Phase 1) are dedicated to scanning the codebase for frontend and React architecture violations, writing the master audit spec into `.lovable/plans/pending/XX-react-frontend-audit.md`, decomposing into subtasks in `.lovable/plans/subtasks/XX-react-frontend/`, and verifying/creating the dedicated frontend linter in `linter-scripts/`.
- [ ] /goal Second `N/2` steps (Phase 2) are dedicated to executing each subtask sequentially, decomposing monolithic components ($\le$ 100 lines), eliminating redundant `useEffect` calls, converting custom hook tuple returns to named objects, running the frontend linter, and verifying all local CI gates exit with code 0.
- [ ] /learn Ingest `.lovable/coding-guidelines/coding-guidelines.md`, `.lovable/strictly-avoid.md`, and `.lovable/memory/issues/` before modifying code.

```text
PHASE_1_STEPS = N / 2   (Steps 1 .. N/2)
PHASE_2_STEPS = N / 2   (Steps N/2+1 .. N)
```

N, PHASE_1_STEPS, and PHASE_2_STEPS are read-only after initialization.

---

## Phase 0: Antigravity Skill Bootstrap (Memory Optimization)

Before execution, check if `.agents/skills/coding-guidelines/skill.md` exists. If missing, create it with YAML frontmatter (`name: coding-guidelines`, `description: "Audits and enforces cross-language coding standards and React/frontend architecture."`).

---

## Phase 1: Scan, Spec, Subtasks & Linter Verification (Steps 1 to PHASE_1_STEPS)

> [!IMPORTANT]
> **Phase 1 is dedicated to discovery, planning, and tooling setup. Do NOT refactor components in Phase 1.**

### Step 1: Ingest Authoritative React Guidelines

1. **Component Size Cap:** Any React component file (`.tsx` / `.jsx`) MUST NOT exceed **100 lines of code** (excluding comments/blank lines). Monolithic components must be decomposed into sub-components.
2. **`useEffect` Minimization:** Avoid using `useEffect` for data transformation or state synchronization. Calculate derived state inline during render or handle side effects directly in event handlers.
3. **Immutability & Pure Transforms:** Never mutate state directly. Use object/array spread syntax or immutable functional methods (`.map()`, `.filter()`, `.reduce()`).
4. **Hook Return Value Convention (Tuple Ban):** Custom React hooks MUST NOT return raw arrays/tuples (e.g. `return [value, setValue]`). They MUST return named property objects (e.g. `return { userProfile, isLoading, onUpdateProfile }`) to ensure safe extension and self-documenting callers.
5. **Component Diagrams:** Any feature or page composed of 3 or more components MUST include a Mermaid component diagram documenting the parent-child hierarchy.

### Step 2: Codebase-Wide Frontend Scan

Search all frontend files for:

- Component files exceeding 100 lines.
- Redundant `useEffect` hooks used for derived calculations.
- Direct state mutations (`state.items.push(x)` or `state.active = true`).
- Custom hooks returning raw tuples (`return [state, updateFn]`).
- Missing component hierarchy diagrams.

### Step 3: Write Master Audit Spec

Save the complete frontend audit to `.lovable/plans/pending/XX-react-frontend-audit.md`:

- List all oversized components and specify their planned sub-component extraction paths.
- Embed the Mermaid component hierarchy diagram.
- Register the spec in `.lovable/plans/index.md`.

### Step 4: Decompose into Subtasks

Break down into subtasks under `.lovable/plans/subtasks/XX-react-frontend/`:

- `01-component-decomposition.md` (Splitting components $> 100$ lines into modular sub-components)
- `02-hook-normalization.md` (Converting hook tuple returns to named objects)
- `03-effect-and-state-cleanup.md` (Removing redundant `useEffect` and enforcing immutable updates)

### Step 5: Linter Verification & CI/CD Connection (Mandatory Checklist)

- [ ] **Check Linter Script Existence:** Check if `linter-scripts/check-frontend-guidelines.mjs` exists.
- [ ] **Create Linter Script if Missing:** If missing, create `linter-scripts/check-frontend-guidelines.mjs` that scans `.tsx`/`.jsx` files for line counts $> 100$, detects custom hooks returning array literals, and verifies ESLint React hooks rules.
- [ ] **Local Linter Command:** Verify the linter runs locally with:
  ```bash
  node linter-scripts/check-frontend-guidelines.mjs
  # Or npm run lint if configured:
  npm run lint
  ```
- [ ] **CI/CD Integration:** Connect the linter into `.lovable/ai-fix-scripts/03-cicd-local-runner.py` under `JOBS`:
  ```python
  JOBS["lint:frontend"] = ["node", "linter-scripts/check-frontend-guidelines.mjs"]
  ```
  And verify it is present in `.github/workflows/ci.yml`.

---

## Phase 2: Autonomous Subtask Execution Loop (Steps PHASE_1_STEPS+1 to N)

> [!IMPORTANT]
> **AUTONOMOUS EXECUTION MANDATE — DO NOT STOP.**
> Sequentially execute each subtask, decomposing components and refactoring hooks until all frontend checks pass 100% green.

```text
STEP = 0
WHILE (STEP < PHASE_2_STEPS):
    STEP += 1

    1. Read the next subtask from .lovable/plans/subtasks/XX-react-frontend/
    2. Extract sub-components into dedicated files (ensuring each is <= 100 lines).
    3. Convert hook returns to named property objects and update caller sites.
    4. Run the frontend linter:
          node linter-scripts/check-frontend-guidelines.mjs
    5. Run the local CI runner:
          python .lovable/ai-fix-scripts/03-cicd-local-runner.py
    6. IF any check fails:
          - Diagnose failure, fix component structure, and re-test immediately.
       IF all checks pass (exit code 0):
          - Mark subtask completed and proceed to next subtask.

    7. When all subtasks are finished and local CI is 100% green:
          - BREAK and proceed to End of Tunnel.
```

---

## Authoritative React Code Reference

```typescript
// BAD: Monolithic 150-line component, custom hook returning tuple, redundant useEffect
export function useUserData(userId: string) {
    const [user, setUser] = useState<User | null>(null);
    return [user, setUser]; // BAD: Tuple return
}

// GOOD: Modular component <= 100 lines, named object hook return, derived state
export interface UseUserDataResult {
    userAccount: User | null;
    isLoading: boolean;
    onRefresh: () => Promise<void>;
}

export function useUserData(userId: string): UseUserDataResult {
    const [userAccount, setUserAccount] = useState<User | null>(null);
    const [isLoading, setIsLoading] = useState<boolean>(false);

    const onRefresh = useCallback(async () => {
        setIsLoading(true);
        const data = await fetchUser(userId);
        setUserAccount(data);
        setIsLoading(false);
    }, [userId]);

    return { userAccount, isLoading, onRefresh };
}
```

---

## Pre-Reply / Loop Checklist

- [ ] All `.tsx`/`.jsx` component files are $\le$ 100 lines.
- [ ] Custom hooks return named objects `{ data, isLoading }`, not tuples.
- [ ] No redundant `useEffect` for derived computations.
- [ ] `node linter-scripts/check-frontend-guidelines.mjs` exited with code 0.
- [ ] Local CI runner `python .lovable/ai-fix-scripts/03-cicd-local-runner.py` exited with code 0.

---

## No Automatic Releases (Strict Policy)

> [!CAUTION]
> This is a development refactoring workflow. You MUST NOT bump versions, update changelogs, or cut a release at the end of this task. Commits must remain standard development commits (e.g. `refactor(ui): decompose component hierarchy`).

---

## End of Tunnel Checklist

- [ ] Frontend linter and component tests pass with code 0.
- [ ] `03-cicd-local-runner.py` passes 100% green.
- [ ] Master plan moved to `.lovable/plans/completed/XX-react-frontend-audit.md`.
- [ ] Clean commit pushed to current branch.
- [ ] File Change Summary posted in chat.

---

## Metadata

- slug: cg-react-frontend
- priority: medium
- status: active
