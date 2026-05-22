# Context Compression Pack

## 목적

긴 대화, 긴 작업 로그, 많은 파일을 다음 작업에 필요한 조건으로 압축한다.

핵심은 많이 요약하는 것이 아니다.
핵심은 다음 실행에 필요한 조건만 남기고 나머지는 경로로 보관하는 것이다.

## 언제 켜는가

```text
스레드가 길어졌을 때
작업이 여러 날 이어질 때
다음 세션으로 넘겨야 할 때
파일 수가 많아 전체를 다시 읽기 어려울 때
현재 목적과 과거 흔적이 섞여 판단 기준이 불명확할 때
```

## 압축 대상

```text
goal:
  현재 목적

decisions:
  이미 확정된 결정

constraints:
  금지, 범위, 권한

current_state:
  현재 어디까지 왔는가

open_risks:
  아직 닫히지 않은 문제

next_actions:
  바로 이어서 할 일

route:
  다시 읽어야 할 파일 후보

evidence:
  판단을 되찾을 수 있는 근거 경로

stop_rule:
  다음 작업자가 어디서 멈춰야 하는지
```

## 압축하지 않는 것

- 긴 원문 전체
- 반복 감상
- 이미 버린 선택지
- 다음 행동과 무관한 세부 흔적
- 검증되지 않은 추측

## 출력 계약

```text
compressed_context:
goal:
decisions:
constraints:
current_state:
open_risks:
next_actions:
route_files:
evidence_files:
do_not_carry:
stop_rule:
```

## 압축 방식

```text
keep:
  다음 실행 조건으로 바로 필요한 것.

route:
  다시 읽어야 할 파일 경로.

drop:
  다음 행동과 무관한 세부 흔적.

mark_uncertain:
  확인하지 않은 판단.
```

압축은 원문을 대체하지 않는다.
압축은 다음 작업자가 원문을 다시 읽을지 결정하게 하는 실행 조건이다.

## 검증

- 이 압축만 보고 다음 작업자가 바로 시작할 수 있는가?
- 근거가 필요한 내용은 파일 경로로 되찾을 수 있는가?
- 오래된 결정과 최신 결정이 섞이지 않았는가?
- 다음 행동과 무관한 정보가 너무 많이 남지 않았는가?
- 멈출 조건이 없어서 다음 작업자가 계속 과독하게 되지 않는가?
