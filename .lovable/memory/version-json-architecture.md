# Global Version JSON Architecture (Single Source of Truth)

Every repository must enforce `version.json` at its root as the **absolute single source of truth (SSOT)** for all versioning information across the entire codebase. 

No individual component should manually hardcode or guess its version.

## Architecture & Structure
The `version.json` file is designed to support both a global version and distinct component versions (e.g., frontend, backend).

```json
{
  "name": "target-project-name",
  "version": "1.0.0",
  "frontend": {
    "version": "inherit"
  },
  "backend": {
    "version": "inherit"
  },
  "promptArchitectByRiseupAsia": {
    "version": "v1.2.0",
    "installed_at": "..."
  }
}
```


### Changelog Management
- **Changelog Configuration:** ersion.json acts as the source of truth for how the changelog should be updated. It must include a "changelog" object dictating the ile_path and ormat to be used by AI agents.

### The "Inherit" Protocol
- **Global Version:** The `"version"` property at the root of the JSON file dictates the global master version for the repository.
- **Component Inheritance:** Components (like `"frontend"` or `"backend"`) can have their `"version"` set to the string `"inherit"`. 
- **Behavior:** When a component is set to `"inherit"`, it means it strictly inherits the global version. Any CI/CD pipeline, build script, or code base that imports `version.json` must read the global `"version"` if the component is marked as `"inherit"`.

### Codebase Import Enforcement
Every code base inside the repository MUST import this root `version.json` file at runtime or build-time to establish its version information. 
- You MUST NOT duplicate version strings in `package.json`, `main.go`, or environment files if they can be dynamically imported from `version.json`. 
- If a component specifies its own discrete version (e.g., `"version": "1.2.3"` instead of `"inherit"`), it operates on an independent release cycle.

## Rule for AI Agents
Whenever you are asked to cut a release, bump versions, or execute release management:
1. Always start with the root `version.json`.
2. Do not touch component versions if they are set to `"inherit"`—they automatically scale when the global version is bumped.
3. If an explicit sub-component bump is requested, verify if it is unlinked from the global version before proceeding.

