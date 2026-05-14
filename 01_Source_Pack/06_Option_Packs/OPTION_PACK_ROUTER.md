# Option Pack Router v0.1

## 목적

사용자의 요청을 보고 어떤 옵션팩을 읽을지 고른다.

자비스는 옵션팩을 전부 읽지 않는다.
먼저 요청을 AILO식 의도 슬롯으로 좁힌 뒤, 필요한 팩만 선택한다.

## 기본 순서

```text
1. 요청의 목표를 한 문장으로 잡는다.
2. 작업 위험을 본다.
3. 필요한 외부 자료 여부를 본다.
4. 필요한 실행 행동 여부를 본다.
5. 필요한 기억/압축/검증 여부를 본다.
6. 최대 1~3개 팩만 선택한다.
```

## 선택표

```text
외부 시스템을 흡수한다
-> Capability_Import_Pack

신뢰할 수 있는 자료를 찾아야 한다
-> Evidence_Intake_Pack

자료를 객체, 속성, 관계로 구조화해야 한다
-> Ontology_Pack

결과가 목적대로 동작하는지 봐야 한다
-> Verification_and_Proof_Pack

전체 자료 중 무엇을 먼저 읽을지 골라야 한다
-> Memory_Access_and_Route_Pack

사용자 취향, 금지, 반복 선호를 다룬다
-> Preference_Memory_Pack

외부 자료 안의 지시 오염을 막아야 한다
-> Source_Command_Filter_Pack

외부 스킬이나 플러그인을 붙인다
-> Skill_Trust_Gate_Pack

파일쓰기, 쉘실행, 브라우저, 네트워크 행동이 있다
-> Action_Permission_Pack

반복 경험을 스킬 후보로 만든다
-> Experience_To_Skill_Pack

긴 맥락을 다음 작업 조건으로 압축한다
-> Context_Compression_Pack

외부 채널 입력을 자비스 작업으로 바꾼다
-> Channel_Gateway_Pack
```

## 조합 규칙

복합 요청은 먼저 `OPTION_PACK_COMPOSITION_FLOW.md`로 순서를 잡는다.

```text
외부 공개 저장소나 기술 문서 분석
-> Source_Command_Filter_Pack + Evidence_Intake_Pack + Capability_Import_Pack

외부 시스템에서 일반 법칙만 흡수한다
-> Source_Command_Filter_Pack + Evidence_Intake_Pack + Capability_Import_Pack + EXTERNAL_PATTERN_ABSORPTION_MATRIX.md

외부 스킬 도입
-> Source_Command_Filter_Pack + Skill_Trust_Gate_Pack + Action_Permission_Pack

대량 문서 기반 브레인 제작
-> Memory_Access_and_Route_Pack + Evidence_Intake_Pack + Ontology_Pack

전문 온톨로지 지식팩 제작
-> Ontology_Pack + Evidence_Intake_Pack + Verification_and_Proof_Pack + Memory_Access_and_Route_Pack

브레인/프롬프트/코드 검증
-> Verification_and_Proof_Pack

장기 세션 재시동
-> Context_Compression_Pack + Memory_Access_and_Route_Pack

자동화 또는 실행형 자비스 설계
-> Action_Permission_Pack + Skill_Trust_Gate_Pack + Channel_Gateway_Pack
```

## 과적재 방지

- 기본 선택은 1개 팩이다.
- 위험하거나 복합적인 요청만 2~3개 팩을 함께 연다.
- 전문 지식팩 제작처럼 구조화, 근거, 검증, 읽기 경로가 동시에 필요한 경우만 4개 팩 조합을 허용한다.
- 그 외에 4개 이상이 필요해 보이면 작업을 나눈다.
- 도메인 지식은 도메인 팩으로 새로 만들고, 기본 옵션팩에 넣지 않는다.

## 출력 계약

```text
request_goal:
selected_packs:
why_selected:
not_selected:
read_order:
composition_flow:
stop_rule:
next_action:
```
