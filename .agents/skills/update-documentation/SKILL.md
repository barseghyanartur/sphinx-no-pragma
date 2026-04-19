---
name: update-documentation
description: Documentation policy, auto-fix alignment, and change reporting for this repository
---

# update-documentation

## Purpose

Keep documentation aligned with code and policy. This single skill handles documentation authority, auto-fixing misalignments, and reporting changes.

---

## 1. Operation mode

- **Pure agent-based synchronization**: Documentation is updated by agents reading code and editing doc files directly.
- **No scripts are used**: There is no automated doc-sync script. Agents perform all synchronization manually.
- **Docs are updated to match code; code is never changed to match docs**: Source of truth is always the code.

---

## 2. Ground truth and authority hierarchy

| Artifact | Role | Authority level |
|---|---|---|
| `sphinx_no_pragma.py` | Source code | **Ground truth** — API, CLI, defaults, exceptions, config behavior |
| `AGENTS.md` | Policy | Must match code reality |
| `.agents/skills/**/*.md` | Procedures | Must match code reality |
| `README.rst` | User-facing docs | Derived — must match code and policy |
| `docs/*.rst` | Detailed docs | Derived — must match code and policy |
| Auto-generated / vendored docs | Generated | **Not modified** |

**Explicit exclusions**: Auto-generated documentation (e.g., `sphinx_no_pragma.egg-info/`, generated API docs) is never modified.

---

## 3. Agent-based sync process (step-by-step)

### Step 1: Extract ground truth from code

Read `sphinx_no_pragma.py` and extract:

- Public API: `DEFAULT_IGNORE_COMMENTS_ENDINGS`, `NoPragmaLiteralInclude`, `setup()`
- CLI-relevant behavior (if any)
- Default values, environment variables, configuration options
- Exceptions and edge cases

### Step 2: Scan documentation files

Read the following files (if they exist):

- `README.rst`
- `AGENTS.md`
- `.agents/skills/**/*.md`
- `docs/*.rst` (all RST files in docs/)
- `CONTRIBUTING.md`
- `SECURITY.md`
- `CHANGELOG.rst`
- `CODE_OF_CONDUCT.md` / `CODE_OF_CONDUCT.rst`

### Step 3: Identify misalignments

Check for:

- Missing items (features documented in code but absent from docs)
- Outdated references (old function names, removed config values)
- Broken paths (references to files that no longer exist)
- Stale defaults (default values in docs that differ from code)
- Wrong examples (code blocks that do not match actual API behavior)

### Step 4: Auto-fix documentation safely

- Update tables, examples, and references to match code.
- Never invent behavior — only document what is observable in code.
- Preserve existing document structure and intent.
- Minimize diffs: only change what is misaligned.

### Step 5: Report changes

Provide a report containing:

- List of files changed
- What changed in each file
- What could not be fixed and why
- Any items requiring human review

---

## 4. Documentation files overview and targeting rules

Based on the repository scan, the following documentation files exist:

| File | Responsibility | Audience |
|---|---|---|
| `README.rst` | Project overview, badges, installation, usage examples, features | End users |
| `AGENTS.md` | Agent governance rules and repository facts | Agents / contributors |
| `.agents/skills/**/*.md` | Agent procedures and standards | Agents |
| `docs/index.rst` | Main docs page | Readers |
| `docs/changelog.rst` | Changelog | Readers |
| `docs/code_of_conduct.rst` | Code of conduct | Contributors |
| `docs/conf.py` | Sphinx configuration | Developers |
| `docs/contributor_guidelines.rst` | Contributor guidelines | Contributors |
| `docs/demo.rst` | Demo page | Readers |
| `docs/documentation.rst` | Documentation guide | Readers |
| `docs/llms.rst` | LLM-facing documentation | LLMs |
| `docs/package.rst` | Package documentation | Readers |
| `docs/security.rst` | Security information | Readers / security reporters |
| `docs/source_tree.rst` | Source tree documentation | Readers |
| `docs/sphinx_no_pragma.rst` | Package reference | Developers |
| `CONTRIBUTING.md` | Contribution guidelines | Contributors |
| `SECURITY.md` | Security policy | Security reporters |
| `CHANGELOG.rst` | Changelog | Users |
| `CODE_OF_CONDUCT.md` / `.rst` | Code of conduct | Contributors |

### When to update each file

| Change type | Files to update |
|---|---|
| Adding a feature or config option | `README.rst`, relevant `docs/*.rst`, `AGENTS.md` if architectural |
| Changing default values | `README.rst`, `docs/*.rst` where defaults are shown |
| Adding CLI commands / options | `README.rst` examples, `docs/*.rst` usage sections |
| Changing public API (`DEFAULT_IGNORE_COMMENTS_ENDINGS`, `setup()` return) | `README.rst`, `docs/sphinx_no_pragma.rst`, `docs/package.rst` |
| Modifying agent governance | `AGENTS.md`, affected `SKILL.md` files |
| Updating contributor process | `CONTRIBUTING.md`, `docs/contributor_guidelines.rst` |

---

## 5. Feature-specific documentation checklist

### Adding an exception or new pragma marker

1. Update `DEFAULT_IGNORE_COMMENTS_ENDINGS` in `sphinx_no_pragma.py`.
2. Update the list in `README.rst` under "Fine-tuning what to strip".
3. Update `docs/sphinx_no_pragma.rst` if it documents the pragma list.
4. Add an entry to `CHANGELOG.rst`.

### Adding CLI commands or options

1. Update `README.rst` with the new command in the Usage section.
2. Update `docs/*.rst` files if the command has dedicated documentation.
3. Ensure code examples in docs are runnable and accurate.

### Adding or changing public API

1. Update `README.rst` with new API usage examples.
2. Update `docs/sphinx_no_pragma.rst` for reference documentation.
3. Update `docs/package.rst` if package-level docs exist.
4. Ensure code blocks in docs match the actual API.

### Changing defaults or limits

1. Find all occurrences of the default value in `README.rst` and `docs/*.rst`.
2. Update them to reflect the new default.
3. Ensure consistency across all files.

---

## 6. Code example rules (documentation-as-tests)

- If Markdown or RST code blocks are intended to be runnable tests, they must use the project's naming conventions.
- The project uses `:name:` directives in RST code blocks (e.g., `:name: test_docs_conf_extensions`). Preserve these.
- Do not introduce pseudo-code examples where runnable examples are expected.
- All code examples in `docs/` should match actual API behavior.

---

## 7. Validation checklist (before reporting completion)

Before declaring documentation sync complete, verify:

- [ ] `README.rst` examples match actual API and CLI behavior.
- [ ] `AGENTS.md` matches current architecture and workflows.
- [ ] `SKILL.md` descriptions remain accurate.
- [ ] Cross-references and file paths are valid.
- [ ] No auto-generated / vendored docs were modified.
- [ ] Any documentation tests required by the repository are respected.

---

## 8. What NOT to do

- **Do not modify source code** to match documentation. Code is ground truth.
- **Do not weaken policy** encoded in `AGENTS.md` or `SKILL.md` files.
- **Do not silently delete content**; preserve intent while correcting facts.
- **Do not reformat docs unnecessarily**; minimize diffs and only fix misalignments.
- **Do not claim documentation is complete** without verifying against code.
