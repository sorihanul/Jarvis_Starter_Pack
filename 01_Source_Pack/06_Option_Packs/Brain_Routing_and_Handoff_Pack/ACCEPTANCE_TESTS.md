# Acceptance Tests

## Test 1. Simple Task Rejects Routing

Input:

```text
문서 하나 요약해줘.
```

Expected:

```text
Brain_Routing_and_Handoff_Pack is not selected.
```

## Test 2. Brain Choice Selects Routing

Input:

```text
이 작업은 글쓰기 브레인으로 할지 검증 브레인으로 할지 먼저 골라줘.
```

Expected:

```text
Brain_Routing_and_Handoff_Pack is selected.
selected route is declared.
same-thread or separate-thread mode is declared.
```

## Test 3. Separate Thread Creates Handoff

Input:

```text
검증 브레인 스레드에 넘길 호출문을 만들어줘.
```

Expected:

```text
handoff prompt is created.
target brain entry files are named.
expected output is declared.
```

## Test 4. Control Misunderstanding Is Rejected

Input:

```text
상위 브레인이 하부 브레인을 조작하게 해줘.
```

Expected:

```text
request is reframed as route, read, handoff, and integrate.
direct control claim is rejected.
```

## Test 5. Integration Is Required

Pass when:

```text
returned output is read and accepted or rejected by the main integration step.
```

Fail when:

```text
returned output is treated as final without integration.
```

## Test 6. Coding Handoff Is Bounded

Input:

```text
이 기능 구현은 별도 코딩 스레드에 넘기고, 나는 최종 판단만 하겠다.
```

Expected:

```text
Brain_Routing_and_Handoff_Pack may be selected.
Action_Permission_Pack may be selected if edits or commands are expected.
handoff includes target files, do_not_touch, success criteria, tests, and return format.
main thread remains final integration owner.
```

## Test 7. Obvious Same-Thread Route Avoids Surface Overload

Input:

```text
이 짧은 검토는 검증 브레인 관점으로만 잠깐 봐줘.
```

Expected:

```text
same-thread lens mode may be used.
route decision is visible.
full BRAIN_ROUTE_REGISTRY.md is not required.
ROUTE_LOG.md is not required unless the route decision is non-obvious or must be remembered.
main thread returns to final integration before answering.
```
