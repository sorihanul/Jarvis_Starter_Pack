# 70 Examples

## Writing Route

```text
request:
  소설 초고를 점검해줘.

route:
  read Writer Brain entry files in the same thread

mode:
  same_thread_lens

integrate:
  main brain returns to user goal and reports revision targets
```

## Research Handoff

```text
request:
  외부 자료를 조사해서 설계에 반영해줘.

route:
  create handoff prompt for Research Brain

mode:
  separate_thread_handoff

integrate:
  main brain reads returned source summary and decides what to absorb
```

## Publishing Release Check

```text
request:
  배포 전에 패키지를 점검해줘.

route:
  use Verification Brain and Release Gate Brain outputs

mode:
  integration_only or separate_thread_handoff

integrate:
  main brain decides release readiness
```

## Memory Route

```text
request:
  이 대화에서 다음에도 쓸 규칙만 남겨줘.

route:
  read Memory/Canon rules

mode:
  same_thread_lens

integrate:
  main brain writes candidate or handoff, not raw conversation dump
```

## Simple Non-Use Example

```text
request:
  문서 하나 요약해줘.

decision:
  do not use this pack

reason:
  one brain can complete it
```
