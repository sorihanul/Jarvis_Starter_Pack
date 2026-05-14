# Permission Mapping Rule v0.1

## 목적

스킬이 요구하는 권한을 행동 등급으로 바꾼다.

스킬 설명이 아니라 실제 접근면을 기준으로 판단한다.

## 권한 슬롯

```text
reads_files:
writes_files:
modifies_existing_files:
deletes_or_moves_files:
runs_shell:
runs_browser:
uses_network:
downloads_files:
uses_external_api:
reads_secrets:
writes_remote:
registers_automation:
calls_other_agents:
```

## 등급 매핑

```text
read_only:
  reads_files만 있거나 정보 읽기 중심이다.

write_local:
  writes_files 또는 modifies_existing_files가 있다.

execute_local:
  runs_shell 또는 runs_browser가 있다.

networked:
  uses_network, downloads_files, uses_external_api가 있다.

secret_touching:
  reads_secrets가 있다.

remote_effect:
  writes_remote가 있다.

automation:
  registers_automation이 있다.

delegating:
  calls_other_agents가 있다.

destructive:
  deletes_or_moves_files가 있다.
```

## 자동 상향

아래 조건은 위험 등급을 올린다.

```text
unknown_source + execute_local:
  review 이상

networked + secret_touching:
  deny 또는 explicit approval

remote_effect:
  explicit approval

automation:
  explicit approval

destructive:
  explicit approval

obfuscated behavior:
  deny
```

## 출력

```text
skill_name:
permission_map:
highest_permission:
permission_reason:
requires_action_permission_pack: yes | no
```
