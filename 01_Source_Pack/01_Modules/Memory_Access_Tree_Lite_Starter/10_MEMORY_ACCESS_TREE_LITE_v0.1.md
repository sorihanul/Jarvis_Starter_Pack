# Memory Access Tree Lite v0.1

## 정의

`Memory Access Tree Lite`는 자비스의 기억 접근 지도다.

자비스가 저장한 기억을 모두 읽는 대신, 특정 주제에서 다시 확인할 파일 후보와 제외할 파일 후보를 얇게 기록한다.

## 메모리 안에서의 위치

```text
저장 메모리
  - LOGS
  - CAPSULES
  - 03_Memory
  - 위키와 정본 문서

접근 메모리
  - MAP
  - MEMORY_MAP
  - Memory Access Tree

실행 메모리
  - SESSION_CARD
  - CURRENT_TASK 또는 TASKS의 현재 안건
  - SESSION_OPS_LOG 또는 LOGS의 현재 기록
```

이 모듈은 `접근 메모리`에 속한다.

## 두 가지 나무

### 1. `world_tree`

`world_tree`는 도메인 입구를 고르는 얇은 지도다.

사용자가 넓은 주제를 말했을 때 어느 도메인으로 들어갈지 정한다. 세부 파일을 많이 나열하지 않는다.

원칙:
- 주 도메인 하나를 고른다.
- 필요할 때만 보조 도메인 하나를 더 고른다.
- 도메인이 정해지면 멈춘다.

### 2. `region_tree`

`region_tree`는 한 도메인 안에서 파일 후보를 고르는 기억 지도다.

특정 주제와 연결된 실제 파일, 폴더, 스킬, 로그, 캡슐, 프로젝트 문서를 기록한다.

원칙:
- 실제 경로를 적는다.
- 언제 확인할지 적는다.
- 언제 확인하지 않을지 적는다.
- 이번 작업에 충분한 파일 수를 정하고 멈춘다.

## 기본 노드 필드

- `node`
- `tree_kind`
- `summary`
- `anchors`
- `open_when`
- `do_not_open`
- `read_order_hint`
- `stop_when`
- `missing_nodes`
- `link_state`
- `last_checked`

## 다른 표면과의 차이

| 표면 | 역할 |
|---|---|
| `MAP.md` | 폴더 위치와 핵심 파일 안내 |
| `Memory Access Tree` | 주제별 파일 후보와 제외 조건 기록 |
| `TASKS` | 지금 처리하는 안건 |
| `LOGS` | 실행 흔적과 검증 기록 |
| `CAPSULES` | 압축된 결론과 인수인계 |
| `SKILLS` | 반복 가능한 실행 절차 |

## 운용 절차

1. 사용자의 요청에서 주제를 확인한다.
2. 도메인이 불명확하면 `world_tree`에서 도메인을 고른다.
3. 도메인이 명확하면 `region_tree`에서 파일 후보를 고른다.
4. `open_when`과 `do_not_open`을 비교한다.
5. `read_order_hint`에 따라 최소 파일만 확인한다.
6. `stop_when`에 도달하면 더 확인하지 않는다.
7. 새 연결이 보이면 `missing_nodes`나 `link_state`에 기록한다.

## 금지

- 노드를 긴 설명문으로 만들지 않는다.
- 폴더 전체를 노드 하나에 몰아넣지 않는다.
- 오래된 연결을 바로 삭제하지 않는다.
- `weak`, `prune_candidate`, `archived` 상태를 먼저 쓴다.
- 이 모듈을 기본 부팅 필수 문서로 만들지 않는다.

## 한 줄 결론

`Memory Access Tree Lite`는 기억을 저장하는 장치가 아니라, 저장된 기억 중 이번 작업에 필요한 파일을 고르는 장치다.
