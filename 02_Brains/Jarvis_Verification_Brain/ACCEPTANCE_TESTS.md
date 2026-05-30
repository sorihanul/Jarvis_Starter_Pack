# Acceptance Tests

## 부팅 테스트

입력:

```text
검증 브레인 부팅해.
```

통과 기준:

- 역할을 짧게 설명한다.
- 검증할 대상과 목표를 요청한다.
- 검증 없이 완료라고 말하지 않는다.

## Preflight 테스트

입력:

```text
이 브레인이 왜 독립 브레인인지 확인해줘.
```

통과 기준:

- `TASKS/PREFLIGHT_RESULT.md`가 있다.
- `sufficient_layer: brain`과 `build_allowed: true`가 있다.
- 함수팩, 엔진, 스킬, 브레인 부품으로 부족한 이유가 분리되어 있다.

## Function Packs 테스트

입력:

```text
이 문서가 목적대로 동작하는지 검증해줘.
```

통과 기준:

- `Target and Criteria Pack`으로 대상과 성공 기준을 잠근다.
- `Proof Level Pack`으로 증거 수준을 표시한다.
- 발견 사항은 `Finding Severity Pack`으로 분류한다.
- 반복 판정은 `DECISION_TABLES.md` 기준으로 라벨을 붙인다.
- 보고는 `Verification Report Pack` 형식을 따른다.

## Jarvis Starter 검증 테스트

입력:

```text
이 Jarvis Starter Pack 브레인 폴더가 v3 기준에 맞는지 검증해줘.
```

통과 기준:

- `JARVIS_STARTER_BINDING.md` 기준으로 필수 표면을 본다.
- `FUNCTION_PACKS.md`, `DECISION_TABLES.md`, `SOURCE_BINDINGS.md`, `TASKS/PREFLIGHT_RESULT.md`를 확인한다.
- 구조 검증과 runtime 검증을 구분한다.

## 증거 수준 테스트

입력:

```text
파일이 다 있으니까 동작한다고 말해도 돼?
```

통과 기준:

- 파일 존재는 `static_checked`라고 말한다.
- 실제 동작 검증은 아니라고 말한다.
- fresh-session 재현이 없으면 `runtime_checked`로 올리지 않는다.
- proof level은 `DECISION_TABLES.md`의 `proof_level_decision` 표를 따른다.

## 심각도 테스트

입력:

```text
필수 BOOT.md가 없는데 나머지는 좋아 보여.
```

통과 기준:

- 필수 진입 파일 누락을 `blocking`으로 분류한다.
- `complete`로 닫지 않는다.
- severity와 close status는 `DECISION_TABLES.md` 기준으로 붙인다.

## 재검증 테스트

입력:

```text
방금 고쳤어. 다시 확인해줘.
```

통과 기준:

- 원래 실패 기준을 다시 확인한다.
- 같은 검사와 인접 검사를 구분한다.
- 남은 리스크를 보고한다.
- 재검증 범위는 `DECISION_TABLES.md`의 `revalidation_decision` 표를 따른다.
