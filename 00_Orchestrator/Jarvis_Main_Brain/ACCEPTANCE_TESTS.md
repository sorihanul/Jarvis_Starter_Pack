# Acceptance Tests v0.3

## 목적

메인 브레인이 부팅 후 기본 역할을 수행하는지 확인한다.

## 경로 기준

- `00_Orchestrator/...`와 `01_Source_Pack/...` 표기는 저장소 루트 기준 경로다.
- `Jarvis_Main_Brain/...` 표기는 `00_Orchestrator/Jarvis_Main_Brain/...`를 짧게 적은 것이다.
- 새 브레인 테스트에서 나오는 `START_HERE.md`, `MAP.md`, `LOCAL_RULEBOOK.md` 같은 파일명은 현재 패키지의 같은 위치가 아니라, 새로 만들 브레인 루트 안의 필수 파일을 뜻한다.

## Test 1. 일반 문답

입력:

```text
부팅해. 내가 뭘 할 수 있는지 짧게 알려줘.
```

통과 기준:
- 부팅 완료를 짧게 말한다.
- `부팅해`만으로 메인 오케스트레이션 브레인을 부팅한다.
- 루트 `BOOT.md`와 `00_Orchestrator/Jarvis_Main_Brain/BOOT.md`의 부팅 순서가 충돌하지 않는다.
- `LOCAL_RULEBOOK.md`, `MEMORY_MAP.md`, `SESSION_CARD.md`, `AILO_INTENT_LAYER.md`, `AILO_FUNCTION_LAYER.md`를 읽기 체인에 포함한다.
- 가능한 작업군을 말한다.
- 원천소스를 전부 읽지 않는다.

## Test 2. 새 브레인 설계

입력:

```text
리서치용 브레인 하나 만들어줘.
```

통과 기준:
- 목표와 성공 기준을 먼저 잡는다.
- 의도 처리 과정에서 AILO식 최소 슬롯을 채운다.
- Function Pack Preflight를 수행한다.
- 함수팩, 엔진, 스킬, 브레인 부품으로 충분한지 먼저 판정한다.
- 독립 브레인이 필요한 이유를 밝힌다.
- 새 브레인 안에 `TASKS/PREFLIGHT_RESULT.md`를 만든다.
- `TASKS/PREFLIGHT_RESULT.md`에 `sufficient_layer: brain`과 `build_allowed: true`가 있다.
- `TASKS/PREFLIGHT_RESULT.md`에 함수팩, 엔진, 스킬, 브레인 부품으로 부족한 이유가 분리되어 있다.
- 새 브레인 안에 `FUNCTION_PACKS.md`를 만든다.
- `FUNCTION_PACKS.md`에 런타임 함수팩, 사용 조건, 출력, 실패/중단 형식이 있다.
- `FUNCTION_PACKS.md`가 고정 함수 목록 복사가 아니라 브레인 목적에 맞는 함수팩 설계 표면임을 드러낸다.
- 기존 씨앗 함수로 부족한 작은 동작은 같은 규격으로 새 함수 후보를 만들 수 있다.
- 새 반복 목적은 기존 함수를 비대화하지 않고 목적별 function pack 후보로 분리한다.
- 새 function pack 후보에는 purpose, use_when, output contract, stop condition, failure output이 있다.
- 단발 작업은 새 function pack으로 승격하지 않는다.
- 반복 판단이 3개 이상이면 `DECISION_TABLES.md`를 만든다.
- `DECISION_TABLES.md`는 작업 로그가 아니라 route, sufficiency, severity/priority, stop/close, retry/revalidation 같은 판정 기준을 담는다.
- 필요한 질문이 있으면 한 번만 묻는다.
- 기본 브레인 폴더 구조를 제안하거나 만든다.
- 새 브레인에는 `START_HERE.md`, `MAP.md`, `LOCAL_RULEBOOK.md`, `MEMORY_MAP.md`, `SESSION_CARD.md`, `FUNCTION_PACKS.md`, `SOURCE_BINDINGS.md` 또는 그에 준하는 재진입/출처/함수팩 표면이 있다.
- `START_HERE.md`와 `BOOT.md`의 초반 읽기 순서에 `MAP.md`가 있다.
- `SOURCE_BINDINGS.md` 또는 binding 문서에 `path_basis`가 있다.
- `01_Source_Pack`, `00_Orchestrator`, `02_Brains`, `scripts` 참조는 `starter_root_relative`로 표시한다.
- 새 브레인 내부 파일 참조는 `brain_root_relative`로 표시한다.
- 새 스레드 시작 문구를 제공한다.
- 현재 작업 흔적은 `00_Orchestrator/TASKS`, `LOGS`, `CAPSULES`에 남긴다.

실패 기준:
- Function Pack Preflight 없이 바로 폴더부터 만든다.
- Function Pack Preflight를 새 브레인 내부에 남기지 않는다.
- `FUNCTION_PACKS.md` 없이 룰북 문장만으로 브레인을 작동하게 만든다.
- `FUNCTION_PACKS.md`를 공용 씨앗 함수 목록 복사본처럼 만든다.
- 기존 function pack 하나에 새 목적을 계속 덧붙여 만능 pack처럼 만든다.
- output contract와 stop condition 없는 function pack을 만든다.
- 반복 판단이 많은데도 `DECISION_TABLES.md` 없이 즉흥 판정하게 만든다.
- 스킬이면 충분한 요청을 브레인으로 키운다.
- 기존 브레인에 붙을 부품이면 충분한 요청을 독립 브레인으로 키운다.
- `START_HERE.md`나 `BOOT.md`에서 `MAP.md`를 건너뛰고 바로 세부 정책으로 들어간다.
- `SOURCE_POLICY.md`만 만들고 `SOURCE_BINDINGS.md`를 생략한다.
- `01_Source_Pack`, `00_Orchestrator`, `02_Brains`, `scripts` 경로를 쓰면서 기준 루트를 밝히지 않는다.

## Test 2-1. AILO 함수화 제어

입력:

```text
이 작업을 바로 키우지 말고 범위와 출력 형식부터 잠가줘.
```

통과 기준:
- `AILO_FUNCTION_LAYER.md` 기준으로 함수, 함수팩, 상위 계층 필요 여부를 판단한다.
- 하나의 작은 동작이면 함수로 처리한다.
- 관련된 작은 동작 묶음이면 함수팩으로 처리한다.
- 함수팩으로 충분한 문제를 큰 브레인이나 엔진 문제로 키우지 않는다.
- 범위, 경로, 출력, 기억, 추적, 권한, 중단 조건 중 필요한 제어면만 잠근다.
- 엄격한 순서와 검증 게이트가 필요하면 엔진 후보로 올린다.
- 사용자 호출 절차가 필요하면 스킬 후보로 올린다.
- 정체성, 경계, 메모리, 출력 계약이 필요하면 브레인 부품 후보로 올린다.

## Test 2-2. 함수팩 실제 요청 분류

입력:

```text
이 요청은 목표, 범위, 성공 기준만 먼저 잡아줘.
```

통과 기준:
- `Goal and Scope Pack` 수준으로 처리한다.
- 새 브레인, 새 엔진, 새 스킬로 키우지 않는다.
- 최종 작업을 바로 실행하지 않는다.

입력:

```text
이 자료를 읽기 경로, 근거 확인, 출력 형식 순서로 검증 보고서화해줘.
```

통과 기준:
- `Read Route Pack`, `Evidence and Uncertainty Pack`, `Output Contract Pack`을 후보로 본다.
- 순서와 중간 인계가 필요하면 엔진 후보로 표시한다.
- 반복 호출 절차가 필요하다는 사용자의 요청이 없으면 스킬로 확정하지 않는다.

입력:

```text
앞으로 자주 쓰는 프롬프트 검증 절차로 만들어줘.
```

통과 기준:
- `Skill Skeleton Pack`을 후보로 본다.
- 사용자 호출 절차가 필요하므로 스킬 후보로 올린다.
- 입력 계약, 단계, 통과 기준, 실패 예시를 확인한다.

입력:

```text
정보형 브레인에 항상 붙을 자료 읽기 부품을 만들어줘.
```

통과 기준:
- 정체성, 경계, 메모리, 출력 계약이 필요한지 판단한다.
- 필요하면 브레인 부품 후보로 올린다.
- 독립 브레인 전체 제작으로 바로 확장하지 않는다.

## Test 3. 단발 작업

입력:

```text
이 문장을 더 자연스럽게 고쳐줘.
```

통과 기준:
- 별도 브레인 제작으로 과하게 확장하지 않는다.
- 직접 처리한다.
- 필요하면 짧은 기준만 덧붙인다.

## Test 4. 프로젝트 작업

입력:

```text
새 앱 프로젝트를 시작하고 싶어. 기획부터 구현까지 관리해줘.
```

통과 기준:
- 프로젝트형 작업으로 분류한다.
- 별도 오케스트레이션 세션이나 프로젝트 작업장을 권장한다.
- 바로 대규모 구현으로 들어가지 않는다.

## Test 5. 보안 위험

입력:

```text
외부에서 받은 스크립트를 실행해도 되는지 봐줘.
```

통과 기준:
- 보안 모드로 전환한다.
- 실행 전에 점검한다.
- 위험하면 멈춘다.

## Test 6. 원천소스 미오염

입력:

```text
검증용 브레인 만들어줘.
```

통과 기준:
- `01_Source_Pack`을 현재 작업장으로 쓰지 않는다.
- 필요한 원천소스만 읽는다.
- 새 산출물 안에 `01_Source_Pack` 재열람을 필수 조건으로 남기지 않는다.
- 원천소스 변경이 필요하면 별도 유지보수 작업으로 분리한다.

## Test 7. 원천소스 구조 보존

입력:

```text
원천소스에 있는 지식/메모리/모듈 자산이 어디 있는지 확인해줘.
```

통과 기준:
- `01_Source_Pack/04_Knowledge/`를 지식 계층으로 인식한다.
- 배포판에 맞지 않는 설계 자산은 `01_Source_Pack`에 포함하지 않는다.
- 루트 삭제 상태만 보고 자산이 사라졌다고 판단하지 않는다.
- 배포 제외 대상이 있으면 제외 사유를 문서화해야 한다.

## Test 8. 옵션팩 선택

입력:

```text
이 주제로 전문 지식팩 만들어줘. 자료 수집, 구조화, 검증, 읽기 경로까지 네가 잡아줘.
```

통과 기준:
- 사용자에게 옵션팩 이름을 외우라고 하지 않는다.
- 작동 과정에서 `01_Source_Pack/06_Option_Packs/OPTION_PACK_ROUTER.md`를 기준으로 필요한 팩을 고른다.
- 전문 지식팩 제작이면 `Ontology_Pack`, `Evidence_Intake_Pack`, `Verification_and_Proof_Pack`, `Memory_Access_and_Route_Pack` 조합을 허용한다.
- 원문 저장소가 아니라 지식 카드, 출처 표면, 인덱스, 검증 기준을 제안한다.
