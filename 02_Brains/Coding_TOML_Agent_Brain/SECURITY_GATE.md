# Security Gate

## rule

Working code is not enough when security-sensitive surfaces exist.

## security checks

```text
input_validation:
auth_permission:
secret_exposure:
dependency_risk:
XSS_risk:
SQL_injection_risk:
path_traversal_risk:
SSRF_risk:
CORS_or_origin_risk:
logging_sensitive_data:
```

## use when

```text
auth_or_permission:true
personal_data:true
payment:true
file_upload:true
public_deploy:true
new_dependency:true
external_input:true
```
