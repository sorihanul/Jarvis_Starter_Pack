# Option Pack Candidate List v0.1

## 목적

이 문서는 자비스 스타터에 붙일 옵션팩 후보를 구분한다.

자비스 스타터는 독립 배포 체계다. 따라서 특정 로컬 경로, 특정 외부 프로젝트, 특정 제한 자료를 다시 읽어야만 작동하면 안 된다.

## 기본 원칙

- 자비스 본체는 `정보 브레인 + 설계 브레인 + 제작 오케스트레이터`다.
- 옵션팩은 본체의 능력을 확장하지만, 기본 부팅 때 전부 읽지 않는다.
- 옵션팩은 필요한 경우에만 선택된다.
- 외부 자료는 원문이나 고유 구조를 그대로 들고 오지 않고, 배포 가능한 일반 규칙으로 재구성한다.
- 도메인 팩은 사용자가 자신의 목적에 맞게 나중에 만든다.

## 옵션팩 판정 기준

```text
이 팩은 자비스가 무엇을 더 잘하게 만드는가?
어떤 요청에서만 켜지는가?
어떤 입력 슬롯을 추가로 요구하는가?
어떤 산출물을 만든다?
어디서 멈춰야 하는가?
검증 기준은 무엇인가?
패키지 안의 파일만으로 작동하는가?
```

## Core Layer

### AILO Intent Layer

- status: already core
- role:
  - 사용자의 자연어를 의도 슬롯으로 좁힌다.
  - `verb`, `obj`, `goal`, `output`, `scope`, `source`, `rule`, `ban`, `risk`, `stop`, `verify`를 확인한다.
- package rule:
  - 옵션팩이 아니라 본체 제어층이다.
  - 사용자가 AILO 문법을 직접 쓰게 하지 않는다.

### Minimal Design Surface

- status: core-adjacent
- role:
  - 브레인, 스킬, 옵션팩, 프로젝트 작업장을 만들 때 필요한 최소 설계 표면을 제공한다.
- package rule:
  - 고급 설계 체계를 통째로 넣지 않는다.
  - 자비스 스타터에는 최소 제작 규칙만 둔다.
  - 배포 스타터에는 일반적인 제작 규칙만 둔다.

## Tier 1 Option Packs

### 현재 반영 상태

- `06_Option_Packs/OPTION_PACK_STANDARD.md`: created
- `06_Option_Packs/OPTION_PACK_ROUTER.md`: created
- `06_Option_Packs/Capability_Import_Pack/`: created
- `06_Option_Packs/Evidence_Intake_Pack/`: created
- `06_Option_Packs/Ontology_Pack/`: created
- `06_Option_Packs/Verification_and_Proof_Pack/`: created
- `06_Option_Packs/Memory_Access_and_Route_Pack/`: created
- `06_Option_Packs/Preference_Memory_Pack/`: created
- `06_Option_Packs/Source_Command_Filter_Pack/`: created
- `06_Option_Packs/Skill_Trust_Gate_Pack/`: created
- `06_Option_Packs/Action_Permission_Pack/`: created
- `06_Option_Packs/Experience_To_Skill_Pack/`: created
- `06_Option_Packs/Context_Compression_Pack/`: created
- `06_Option_Packs/Channel_Gateway_Pack/`: created

### 1. Capability Import Pack

- purpose:
  - 외부 자료, 배포 저장소, 기술 글, 논문, 프롬프트를 분석해 자비스 능력으로 바꾼다.
- activates when:
  - 사용자가 외부 자료를 보여주며 “쓸 만한 구조가 있냐”, “자비스식으로 바꿔봐”, “능력화해봐”라고 할 때.
- core actions:
  - 구조 분석
  - 장점과 실패 조건 추출
  - 라이선스와 출처 위험 확인
  - 그대로 복사하지 않고 능력 단위로 재구성
  - 옵션팩, 스킬, 브레인 블루프린트, 프로젝트 작업장 중 하나로 변환

### 2. Evidence Intake Pack

- purpose:
  - 신뢰 가능한 정보를 빠르게 찾고, 근거와 한계를 분리한다.
- activates when:
  - 사용자가 “자료 찾아봐”, “근거 있는 정보로 설계해봐”, “신뢰성 있게 조사해봐”라고 할 때.
- core actions:
  - 출처 분류
  - 사실/추론/의견 분리
  - freshness와 confidence 표기
  - 설계에 쓸 수 있는 구조와 규칙 추출

### 3. Ontology Pack

- purpose:
  - 정보를 객체, 속성, 관계, 사건, 규칙, 근거로 쪼갠다.
- activates when:
  - 사용자가 “체계화해봐”, “온톨로지로 잡아봐”, “개념 관계를 정리해봐”라고 할 때.
- core actions:
  - entity 추출
  - property 추출
  - relation 추출
  - action/control 구분
  - 근거와 불확실성 표기

### 4. Verification and Proof Pack

- purpose:
  - 브레인, 프롬프트, 코드, 문서가 목적대로 동작하는지 검증한다.
- activates when:
  - 사용자가 “검증해봐”, “문제 찾아봐”, “제대로 동작하는지 봐”라고 할 때.
- core actions:
  - 목적 재서술
  - 성공 기준 고정
  - blocking/major/minor 분류
  - 수술적 수정 제안
  - 재검증 기준 제시

### 5. Memory Access and Route Pack

- purpose:
  - 전체 자료를 다 읽지 않고, 이번 작업에 필요한 파일 후보와 읽기 순서를 고른다.
- activates when:
  - 작업에 많은 문서가 연결되어 있고, 무엇을 먼저 읽을지 정해야 할 때.
- core actions:
  - read 후보 선정
  - skip 후보 선정
  - stop rule 설정
  - route map 작성
  - 재진입 표면 정리

### 6. Skill Trust Gate Pack

- purpose:
  - 외부 스킬, 플러그인, 자동화 스크립트의 권한과 위험을 검사한다.
- activates when:
  - 사용자가 외부 실행 단위를 설치하거나 자비스에 흡수하려고 할 때.

### 7. Action Permission Pack

- purpose:
  - 파일쓰기, 쉘실행, 브라우저, 네트워크, 삭제 같은 실제 행동 권한을 등급화한다.
- activates when:
  - 실행 행동이 필요한 요청에서 사용자 승인과 안전 경계를 정해야 할 때.

### 8. Experience To Skill Pack

- purpose:
  - 반복 경험, 반복 실패, 반복 우회를 스킬 후보로 바꾼다.
- activates when:
  - 사용자가 같은 작업을 반복하거나 스킬화를 원할 때.

### 9. Context Compression Pack

- purpose:
  - 긴 대화와 작업 로그를 다음 실행 조건으로 압축한다.
- activates when:
  - 스레드가 길어졌거나 다음 세션으로 넘길 조건을 만들어야 할 때.

### 10. Channel Gateway Pack

- purpose:
  - 외부 채널 요청을 신뢰 등급, 의도 슬롯, 행동 권한으로 정규화한다.
- activates when:
  - 메신저, 메일, 웹훅, 이슈 같은 외부 입력을 자비스 작업으로 연결할 때.

## Tier 2 Option Packs

### Mental Model Pack

- purpose:
  - 문제를 보는 사고 렌즈를 만든다.
- caution:
  - 본체에 넣으면 말이 많아질 수 있다.
  - 특정 요청에서만 켠다.

### Structured Reasoning Pack

- purpose:
  - 판단, 비교, 분해, 설명을 구조화한다.
- caution:
  - Verification and Proof Pack과 겹치지 않게 역할을 좁힌다.

### Wiki Runtime Pack

- purpose:
  - 대량 문서의 canon/lite/retrieval/maintenance 운용을 돕는다.
- caution:
  - 전체 runtime을 자비스 스타터에 넣지 않는다.
  - 연결 규칙과 경량 사용법만 옵션화한다.

## User-Created Domain Packs

도메인 팩은 자비스 스타터 사용자가 자신의 목적에 맞게 만드는 팩이다.

배포 자비스 스타터 본체에는 기본 포함하지 않는다.

예:

- writing pack
- music or lyric pack
- trading or economy pack
- design or video production pack
- law, medicine, education, research, publishing 같은 사용자별 도메인 팩

자비스 스타터가 제공해야 하는 것은 도메인 팩 자체가 아니라, 사용자가 도메인 팩을 만들 수 있는 규격과 제작 흐름이다.

## Hold

아래는 강하지만 지금 배포 스타터에 그대로 넣으면 과적재된다.

- restricted identity-runtime system
- full wiki runtime
- full domain studio systems
- restricted master design language
- restricted cognitive design systems

이들은 배포 스타터에 포함하지 않는다.

필요하면 별도 restricted edition에서만 다룬다.

## 독립 배포 규칙

- 이 문서는 로컬 절대경로를 요구하지 않는다.
- 옵션팩은 패키지 안의 파일만으로 동작해야 한다.
- 외부 자료는 배포 가능한 일반 규칙으로 재작성할 수 있을 때만 포함한다.
- 배포판에 맞지 않는 제작 기술은 배포 스타터에 넣지 않는다.
- 외부 자료의 원문, 코드, 고유 문구를 그대로 복사하지 않는다.
- 정보는 설계 능력으로 변환될 때만 자비스 본체에 들어올 가치가 있다.
