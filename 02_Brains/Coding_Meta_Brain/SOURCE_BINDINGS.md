# Source Bindings

## path basis

```text
brain_root_relative:
  paths inside this Coding_Meta_Brain folder

project_relative:
  paths inside 01_PROJECT/

external_repo:
  target repo copied or referenced by the user

user_given_absolute:
  explicit local path supplied by the user
```

## binding rules

- Treat `01_PROJECT/` as the default project surface for a case instance.
- Treat root brain files, `THREADS/`, `MEMORY/`, `LOGS/`, and `CAPSULES/` as operational surfaces.
- Do not publish operational surfaces unless the user explicitly asks for an archive of the whole case workspace.
- If an external repo is used, record the source in `TASKS/CURRENT_TASK.md` before modifying it.
