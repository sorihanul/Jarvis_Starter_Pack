# Option Packs

## 목적

이 폴더는 자비스 스타터의 선택형 능력 팩을 둔다.

자비스 본체는 항상 가볍게 부팅한다. 옵션팩은 사용자의 요청이 해당 능력을 필요로 할 때만 읽는다.

## 기본 원칙

- 옵션팩은 기본 부팅 파일이 아니다.
- 옵션팩은 사용 조건이 분명해야 한다.
- 옵션팩은 패키지 내부 파일만으로 이해되어야 한다.
- 옵션팩은 외부 코드나 문구를 그대로 복사하지 않는다.
- 외부 프로젝트에서 배운 내용은 일반적인 설계 규칙으로 바꿔 적는다.
- 도메인 팩은 기본 포함하지 않는다. 사용자가 새 브레인을 만들 때 필요한 만큼 생성한다.

## 사용자에게 보이는 방식

옵션팩은 사용자에게 외우라고 주는 메뉴가 아니다.

사용자는 자연어로 요청한다.
자비스가 요청을 보고 필요한 팩만 내부에서 고른다.

```text
사용자: 이 자료로 전문 지식팩 만들어줘.
자비스: Ontology_Pack + Evidence_Intake_Pack + Verification_and_Proof_Pack + Memory_Access_and_Route_Pack
```

## 세 묶음으로 보기

처음 읽을 때는 12개 팩을 전부 외우지 않는다.

```text
자료를 다루는 팩:
  Capability_Import_Pack
  Evidence_Intake_Pack
  Source_Command_Filter_Pack

구조를 만드는 팩:
  Ontology_Pack
  Memory_Access_and_Route_Pack
  Context_Compression_Pack
  Experience_To_Skill_Pack

안전하게 실행하는 팩:
  Verification_and_Proof_Pack
  Skill_Trust_Gate_Pack
  Action_Permission_Pack
  Channel_Gateway_Pack
  Preference_Memory_Pack
```

## 현재 포함된 팩

- `Capability_Import_Pack/`: 외부 시스템, 공개 저장소, 기술 글을 자비스 능력으로 바꾸는 절차
- `Evidence_Intake_Pack/`: 신뢰 가능한 정보 수집과 근거 분리 절차
- `Preference_Memory_Pack/`: 사용자 프로필, 기억 등급, 기억 예산을 다루는 절차
- `Source_Command_Filter_Pack/`: 외부 자료와 웹 자료를 읽을 때 지시 오염을 막는 절차
- `Ontology_Pack/`: 정보를 객체, 속성, 관계, 사건, 규칙, 근거로 쪼개는 절차
- `Verification_and_Proof_Pack/`: 목적, 성공 기준, 결함, 재검증을 분리하는 절차
- `Memory_Access_and_Route_Pack/`: 필요한 파일 후보와 읽기 순서를 고르는 절차
- `Skill_Trust_Gate_Pack/`: 외부 스킬과 플러그인의 권한, 출처, 위험을 검사하는 절차
- `Action_Permission_Pack/`: 파일쓰기, 쉘실행, 브라우저 조작 같은 행동 권한을 나누는 절차
- `Experience_To_Skill_Pack/`: 반복 작업과 반복 실패를 스킬 후보로 바꾸는 절차
- `Context_Compression_Pack/`: 긴 대화와 작업 로그를 다음 실행 조건으로 압축하는 절차
- `Channel_Gateway_Pack/`: 외부 채널 요청을 자비스 작업으로 안전하게 정규화하는 절차

## 먼저 읽을 파일

1. `OPTION_PACK_STANDARD.md`
2. `OPTION_PACK_ROUTER.md`
3. 복합 요청이면 `OPTION_PACK_COMPOSITION_FLOW.md`
4. 외부 시스템이나 공개 자료를 흡수할 때만 `EXTERNAL_PATTERN_ABSORPTION_MATRIX.md`
5. 필요한 옵션팩의 `README.md`
6. 해당 옵션팩의 세부 규칙 파일

## 사용 기준

```text
요청이 외부 시스템 흡수라면 Capability_Import_Pack
요청이 자료 조사라면 Evidence_Intake_Pack
요청이 사용자 기억/취향/프로필이라면 Preference_Memory_Pack
요청이 외부 문서/웹/스크랩 처리라면 Source_Command_Filter_Pack
요청이 정보 구조화라면 Ontology_Pack
요청이 검증이라면 Verification_and_Proof_Pack
요청이 읽기 순서/기억 접근이라면 Memory_Access_and_Route_Pack
요청이 외부 스킬/플러그인 설치라면 Skill_Trust_Gate_Pack
요청이 파일쓰기/쉘실행/브라우저 조작이라면 Action_Permission_Pack
요청이 반복 작업을 스킬화하려는 것이라면 Experience_To_Skill_Pack
요청이 긴 맥락을 다음 세션으로 넘기는 것이라면 Context_Compression_Pack
요청이 외부 채널 연결이라면 Channel_Gateway_Pack
```

## 금지

- 옵션팩을 모두 읽고 시작하지 않는다.
- 옵션팩을 코어처럼 상시 적용하지 않는다.
- 도메인 팩을 기본 스타터에 과적재하지 않는다.
- 복합 요청이라는 이유만으로 4개 이상 팩을 기본값처럼 열지 않는다.
- 외부 프로젝트의 구현 코드를 가져오지 않는다.
- 라이선스가 강한 자료를 그대로 복사하지 않는다.
- 외부 프로젝트 이름, URL, 고유 문구를 공개 스타터 규칙으로 남기지 않는다.
