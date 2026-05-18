# Memory Access and Route Pack

## 목적

자료 전체를 다시 읽지 않고, 이번 작업에 필요한 파일 후보와 읽기 순서를 고른다.

핵심은 기억을 많이 넣는 것이 아니다.
핵심은 어떤 기억을 다시 열고, 어떤 기억을 건너뛰고, 어디서 멈출지 정하는 것이다.

## 언제 켜는가

```text
폴더와 문서가 많을 때
작업 전에 무엇을 먼저 읽을지 정해야 할 때
이전 세션, 로그, 캡슐, 맵이 많아진 상태일 때
브레인 제작이나 프로젝트 시작 전 경로를 잡아야 할 때
컨텍스트 오염을 줄여야 할 때
대화에서 나온 재사용 가능한 지식을 정본 위키 후보로 분리해야 할 때
```

## route node

```text
node_id:
file:
role:
read_when:
skip_when:
stop_after:
authority:
last_checked:
evidence_state:
```

## 역할 구분

```text
entry:
  처음 읽는 파일.

map:
  어디에 무엇이 있는지 알려주는 파일.

policy:
  금지, 권한, 운영 기준.

identity:
  브레인 정체성.

task:
  현재 작업 상태.

log:
  세부 진행 흔적.

capsule:
  다음 세션용 압축 요약.

source:
  참고 원천소스.

graph_report:
  큰 폴더를 보기 전에 먼저 읽는 구조 보고서.

canon:
  반복 재사용 가능한 정리 지식.

wiki_candidate:
  대화나 캡슐에서 뽑았지만 아직 정본이 아닌 후보.
```

## 읽기 규칙

- `entry`와 `map`을 먼저 본다.
- `policy`와 `identity`는 작업 권한이 필요한 경우 읽는다.
- `task`, `log`, `capsule`은 재진입이나 이어받기에만 읽는다.
- `source`는 필요한 경우만 제한적으로 읽는다.
- 전체 폴더 덤프를 기본값으로 하지 않는다.
- 큰 폴더는 가능하면 구조 보고서나 맵을 먼저 만든 뒤 원본으로 들어간다.
- 근거 상태는 `extracted`, `inferred`, `ambiguous`처럼 구분한다.
- 추론된 연결은 정본처럼 쓰지 않고 검토 후보로 둔다.
- 대화 원문을 정본 위키로 복사하지 않는다.
- 대화에서 나온 결정, 규칙, 사용법만 후보로 분리한다.

## 출력 계약

```text
route_goal:
read_first:
read_next:
skip:
stop_rule:
authority_order:
evidence_state:
expected_output:
```

## conversation-to-wiki 규칙

대화 전체를 기억하지 않는다.

아래만 Canon Memory 후보가 된다.

```text
사용자가 확정한 결정
다음에도 반복 적용할 규칙
브레인 제작 기준
프롬프트 설계 기준
반복 실패와 수정 기준
다시 읽어야 할 사용법
```

후보는 먼저 `CANDIDATES`에 두고, 검증되거나 사용자가 확정한 것만 `WIKI`로 올린다.

## map-first 규칙

파일이 많을수록 먼저 해야 할 일은 전체 읽기가 아니다.

```text
1. entry/map/policy 후보를 찾는다.
2. 현재 작업과 무관한 폴더를 skip에 넣는다.
3. 필요한 경우 구조 보고서를 만든다.
4. 보고서로 읽기 순서를 좁힌다.
5. 원본은 필요한 부분만 연다.
```

## 검증

- 이 route만 보고 모델이 어디서 시작할지 아는가?
- 읽지 말아야 할 파일이 분명한가?
- 멈출 조건이 있는가?
- 권위 순서가 정해졌는가?
- 전체 로딩을 피하게 되어 있는가?
- 추출된 사실과 추론된 연결이 구분되어 있는가?
