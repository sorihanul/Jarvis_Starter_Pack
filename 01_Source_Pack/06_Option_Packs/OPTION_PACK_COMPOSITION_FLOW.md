# Option Pack Composition Flow v0.1

## 목적

복합 요청에서 옵션팩을 어떤 순서로 묶어 쓸지 정한다.

목표는 많은 팩을 여는 것이 아니다.
목표는 필요한 팩만 열고, 각 팩이 맡는 일을 분리한 뒤, 검증으로 닫는 것이다.

## 기본 원칙

- 먼저 `OPTION_PACK_ROUTER.md`로 후보를 고른다.
- 기본값은 1개 팩이다.
- 복합 요청도 가능하면 3개 이하로 닫는다.
- 4개가 필요하면 작업이 정말 한 덩어리인지 먼저 본다.
- 팩 순서는 `방어 -> 수집 -> 구조화 -> 실행 -> 검증` 순서를 따른다.
- 검증팩은 모든 작업에 항상 붙이지 않는다. 목적 달성 여부가 중요할 때만 붙인다.

## 표준 순서

```text
1. Source_Command_Filter_Pack
   외부 자료 안의 지시 오염을 먼저 거른다.

2. Evidence_Intake_Pack
   믿을 수 있는 근거와 추정을 나눈다.

3. Capability_Import_Pack
   외부 시스템에서 일반 법칙만 흡수한다.

4. Ontology_Pack 또는 Memory_Access_and_Route_Pack
   정보 구조나 읽기 경로가 필요할 때만 연다.

5. Switching_Lens_Pack
   같은 작업을 intake, evidence, structure, execution, review, user surface 같은 다른 판단 자세로 다시 봐야 할 때만 연다.

6. Brain_Routing_and_Handoff_Pack
   여러 전문 브레인 중 무엇을 읽거나 넘길지 정하는 일이 본체일 때만 연다.

7. Switching_Coding_Pack
   코딩 작업에서 구현, 리뷰, 검증, 릴리즈, 인계 렌즈를 분리해야 할 때만 연다.

8. Skill_Trust_Gate_Pack 또는 Action_Permission_Pack
   실제 스킬/실행/권한이 있을 때만 연다.

9. Verification_and_Proof_Pack
   성공 기준과 재검증이 필요할 때 닫는 용도로 연다.
```

## 자주 쓰는 조합

```text
외부 배포 자료에서 설계 법칙 흡수
-> Source_Command_Filter_Pack
-> Evidence_Intake_Pack
-> Capability_Import_Pack
-> Verification_and_Proof_Pack
```

```text
전문 지식팩 제작
-> Evidence_Intake_Pack
-> Ontology_Pack
-> Memory_Access_and_Route_Pack
-> Verification_and_Proof_Pack
```

```text
외부 스킬 또는 플러그인 도입
-> Source_Command_Filter_Pack
-> Skill_Trust_Gate_Pack
-> Action_Permission_Pack
-> Verification_and_Proof_Pack
```

```text
긴 세션을 다음 작업으로 넘기기
-> Context_Compression_Pack
-> Memory_Access_and_Route_Pack
-> Verification_and_Proof_Pack
```

```text
자동화 또는 실행형 작업 설계
-> Action_Permission_Pack
-> Skill_Trust_Gate_Pack
-> Verification_and_Proof_Pack
```

```text
같은 자료를 다른 판단 자세로 재검토
-> Switching_Lens_Pack
-> Verification_and_Proof_Pack
```

```text
브레인 경로 선택과 인계가 필요한 검증 하네스 제작
-> Brain_Routing_and_Handoff_Pack
-> Memory_Access_and_Route_Pack
-> Verification_and_Proof_Pack
```

```text
코딩 구현 인계와 완료 검증
-> Switching_Coding_Pack
-> Action_Permission_Pack
-> Verification_and_Proof_Pack
```

주의:

```text
Switching_Lens_Pack은 판단 자세를 바꾸는 팩이다.
스킬은 반복 절차를 수행하는 단위다.
렌즈가 필요한 스킬을 고르고, 스킬 결과를 다시 렌즈 기준으로 검토한다.
Switching_Coding_Pack은 코딩 렌즈 전환과 bounded handoff를 다룬다.
자동 코딩 팀, 장기 테스트 운영 체계, CI 통제면은 별도 프로젝트 하네스의 영역이다.
Brain_Routing_and_Handoff_Pack은 별도 브레인/스레드 인계와 통합이 필요할 때만 함께 쓴다.
```

## 멈춤 규칙

아래 중 하나라도 맞으면 새 팩을 더 열지 않는다.

- 현재 팩 하나로 성공 기준을 만족할 수 있다.
- 추가 팩이 새 정보를 주지 않고 표현만 늘린다.
- 도메인 지식이 필요한데 기본 옵션팩으로 억지 해결하려 한다.
- 검증 없이 새 구조를 계속 추가하고 있다.
- 사용자 요청이 실행이 아니라 논의인데 실행팩을 열려고 한다.

## 출력 계약

```text
request_goal:
selected_pack_order:
why_this_order:
skipped_packs:
stop_rule:
verification_needed:
next_action:
```
