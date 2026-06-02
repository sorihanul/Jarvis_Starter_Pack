# Dependency Gate

## rule

New packages, libraries, SDKs, and external APIs are not automatically approved.

## check before adding

```text
real_package_exists:
official_docs_checked:
maintainer_or_owner_checked:
recent_activity_checked:
known_CVE_or_advisory_checked:
license_checked:
lockfile_impact_known:
unnecessary_dependency_rejected:
```

## default

Prefer no new dependency.
