# Memory Access Tree Example v0.1

## 예시: 자비스 스타터 메모리 표면

```yaml
node: "[[Jarvis Starter memory surface]]"
tree_kind: "region_tree"
domain: "Jarvis_Starter_Pack"
summary: "자비스 스타터에서 세션 기록, 캡슐, 메모리 구현, 재정렬 기준을 다시 확인할 때 쓰는 파일 후보 지도."

anchors:
  maps:
    - path: "MAP.md"
      use: "현재 폴더 구조와 작업 레이어 확인."
  files:
    - path: "TASKS/JARVIS_SESSION_CONTINUITY_MINIMUM_v0.1.md"
      use: "세션 연속성에 필요한 최소 표면 확인."
    - path: "TASKS/JARVIS_CONTEXT_REALIGNMENT_NOTE_v0.1.md"
      use: "세션이 길어졌을 때 다시 확인할 순서 확인."
    - path: "03_Memory/Jarvis_Memory.py"
      use: "메모리 압축 스크립트 사용 여부 확인."
  logs:
    - path: "LOGS/"
      use: "현재 작업과 직접 연결된 실행 흔적만 확인."
  capsules:
    - path: "CAPSULES/"
      use: "완료된 판단의 압축본이 필요할 때만 확인."

open_when:
  - "세션 복귀 속도가 느려진 이유를 확인할 때"
  - "기억, 로그, 캡슐, 재정렬 기준을 함께 정리할 때"
  - "현재 작업에 필요한 기록 파일 후보를 줄여야 할 때"

do_not_open:
  - "단일 문서 교정만 필요한 경우"
  - "현재 요청이 메모리나 세션 연속성과 관계없는 경우"
  - "이미 사용자가 확인할 파일을 정확히 지정한 경우"

read_order_hint:
  - "MAP.md"
  - "TASKS/JARVIS_SESSION_CONTINUITY_MINIMUM_v0.1.md"
  - "TASKS/JARVIS_CONTEXT_REALIGNMENT_NOTE_v0.1.md"
  - "필요할 때만 LOGS 또는 CAPSULES"

stop_when:
  - "이번 작업에 필요한 파일 2~4개를 고르면 중단"
  - "현재 작업이 실행 순서 문제로 바뀌면 TASKS의 현재 안건 문서로 이동"

missing_nodes:
  - node: "[[Jarvis Starter memory map]]"
    reason: "기억 관련 파일이 더 늘어나면 별도 MEMORY_MAP 후보가 필요함."
    priority: "medium"

link_state:
  keep:
    - "JARVIS_SESSION_CONTINUITY_MINIMUM_v0.1.md"
    - "JARVIS_CONTEXT_REALIGNMENT_NOTE_v0.1.md"
  weak:
    - "오래된 로그 중 현재 세션과 직접 연결되지 않는 기록"
  prune_candidate: []
  archived: []

last_checked: 2026-05-14
```

## 사용 문장

- "Memory Access Tree 기준으로 이번 작업에서 다시 확인할 파일만 골라."
- "이 주제의 region tree를 짧게 만들어."
- "이 파일 연결은 keep, weak, prune_candidate 중 어디에 둘지 판단해."
