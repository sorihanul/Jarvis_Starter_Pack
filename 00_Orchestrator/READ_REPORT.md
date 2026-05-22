# Read Report

## 목적

이 파일은 오케스트레이터가 route-first로 무엇을 읽었는지 남기는 최신 1회 감사 표면이다.

큰 원천소스, Canon Memory, 옵션팩을 열 때는 먼저 route/index를 보고, 실제로 연 파일과 건너뛴 파일을 여기에 남긴다.

## 기록 원칙

모든 작업마다 쓰지 않는다.

아래 경우에만 이 파일을 덮어쓴다.

- Canon Memory를 열었다.
- 큰 Source Pack을 route로 골라 읽었다.
- `Memory_Access_and_Route_Pack`을 사용했다.
- route를 건너뛰었다.
- 이번 읽기 경로가 다음 재사용에 영향을 준다.

아래 경우에는 쓰지 않는다.

- 단순 질의응답
- 명백한 로컬 파일 1~2개 확인
- route, canon, wiki, source bundle, archive를 열지 않은 작업
- 보고해도 다음 재진입 비용을 줄이지 못하는 작업

이 파일은 누적 로그가 아니다.
필요할 때 최신 보고 1개만 덮어쓴다.
오래 남길 교훈은 `CANON_MEMORY/CANDIDATES/` 또는 `CANON_MEMORY/WIKI/`로 분리한다.

## 보고 양식

```text
task:
route_file_read_first:
selected_files:
skipped_files:
opened_canon_notes:
route_bypass_reason:
route_update_needed:
next_route_fix:
```

## 현재 보고

현재 활성 읽기 보고 없음.
