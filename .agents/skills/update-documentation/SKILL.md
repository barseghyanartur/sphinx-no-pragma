---
name: update-documentation
description: Documentation policy, synchronization, and update procedures
---

## Operation Mode

- Pure agent-based synchronization
- No scripts are used for documentation updates
- Documentation is updated to match code; code is never changed to match docs

## Ground Truth and Authority Hierarchy

- Code is ground truth for API, CLI, defaults, exceptions, configuration behavior
- AGENTS.md and SKILL.md are policy and must match reality
- README/docs are derived and must match code and policy
- Auto-generated/vendored docs are not modified

## Agent-based Sync Process

1. **Extract ground truth** from code (public API, CLI, exceptions, defaults, env vars, config)
2. **Scan documentation** files (README.rst, AGENTS.md, SKILL.md, docs/)
3. **Identify misalignments** (missing items, outdated references, broken paths, stale defaults, wrong examples)
4. **Auto-fix documentation** safely (tables, examples, references, sections; never invent behavior)
5. **Report changes** (files changed, what changed, what could not be fixed, why)

## Documentation Files Overview

### README.rst
- Primary user-facing documentation
- Installation instructions, usage examples, feature overview
- Update when: adding/changing CLI commands, changing configuration defaults, adding/removing features

### docs/*.rst
- Sphinx documentation source
- Detailed usage and API reference
- Update when: adding new documentation sections, changing API behavior

### AGENTS.md
- Repository governance file
- Update when: changing architecture, adding new configuration options

### SKILL.md files
- Agent procedure files
- Update when: changing development workflow or procedures

## Feature-specific Checklist

### Adding an exception
- Document in README.rst under appropriate section
- Update examples if needed

### Adding CLI commands/options
- Document in README.rst usage section
- Update examples in docs/ if applicable

### Changing defaults/limits
- Update README.rst configuration section
- Ensure consistency across all documentation

### Adding public API
- Update docs/sphinx_no_pragma.rst with proper RST
- Add examples to relevant documentation files

## Validation Checklist

Before reporting completion:
- [ ] README examples match actual API/CLI
- [ ] AGENTS.md matches architecture and workflows
- [ ] SKILL.md descriptions remain accurate
- [ ] Cross-references and file paths are valid
- [ ] No generated docs were modified
- [ ] Documentation tests required by repository pass

## What NOT to Do

- Do not modify source code to match docs
- Do not weaken policy encoded in SKILL.md or AGENTS.md
- Do not silently delete content; preserve intent while correcting facts
- Do not reformat docs unnecessarily; minimize diffs
