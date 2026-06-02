# Source Bindings

## path basis

```text
brain_root_relative:
  paths inside this Coding_TOML_Agent_Brain folder

project_relative:
  paths inside 01_PROJECT/

external_repo:
  target repo copied or referenced by the user

user_given_absolute:
  explicit local path supplied by the user
```

## binding rules

- Treat `01_PROJECT/` as the default project surface.
- Treat `AGENTS/`, `TASKS/`, `MEMORY/`, `REPORTS/`, `LOGS/`, and `CAPSULES/` as operational surfaces.
- Do not publish operational surfaces by default.
- If an external repo is used, bind the source before drafting active agents.
