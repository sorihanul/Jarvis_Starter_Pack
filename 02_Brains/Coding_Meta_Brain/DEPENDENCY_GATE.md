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
Prefer standard library, existing dependency, or documented framework feature.

## output

```text
dependency_name:
why_needed:
alternatives:
checks_done:
risk_level:
approval_needed:
```
