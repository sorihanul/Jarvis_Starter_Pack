# Memory Access Node Template v0.1

아래 템플릿은 필요한 만큼만 채운다. 비어 있는 필드는 남기지 말고 삭제한다.

```yaml
node: "[[주제 이름]]"
tree_kind: "world_tree | region_tree"
domain: ""
summary: ""

anchors:
  maps:
    - path: ""
      use: ""
  files:
    - path: ""
      use: ""
  logs:
    - path: ""
      use: ""
  capsules:
    - path: ""
      use: ""
  skills:
    - path: ""
      use: ""

open_when:
  - ""

do_not_open:
  - ""

read_order_hint:
  - ""

stop_when:
  - ""

missing_nodes:
  - node: "[[나중에 만들 기억 자리]]"
    reason: ""
    priority: "low | medium | high"

link_state:
  keep:
    - ""
  weak:
    - ""
  prune_candidate:
    - ""
  archived:
    - ""

last_checked: YYYY-MM-DD
```

## 짧은 작성 규칙

- `summary`는 한두 문장으로 끝낸다.
- `anchors`에는 실제로 다시 확인할 파일만 적는다.
- `open_when`은 확인 조건이다.
- `do_not_open`은 제외 조건이다.
- `stop_when`은 컨텍스트 폭증을 막는 중단 조건이다.
- `missing_nodes`는 실패가 아니라 나중에 만들 기억 자리다.
- `link_state`는 삭제보다 약화, 보관, 대체를 먼저 판단한다.
