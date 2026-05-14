# Track Expansion v0.1

## 목적

프로젝트가 커질 때만 파트별 단기 로드맵을 추가한다.

## 기본값

처음부터 팀을 많이 만들지 않는다.

기본:
- `MISSION`
- `ROADMAP`
- `ORCHESTRATOR`

## 확장 조건

아래 중 하나면 트랙을 추가한다.

1. 설계와 구현이 분리되어야 할 때
2. 보안 검토가 따로 필요할 때
3. 검증이 독립적으로 돌아야 할 때
4. 디버그 전용 팀이 필요할 때
5. 최적화 전용 팀이 필요할 때

## 권장 트랙 예

- `DESIGN_TRACK`
- `SECURITY_TRACK`
- `VALIDATION_TRACK`
- `DEBUG_TRACK`
- `OPTIMIZATION_TRACK`

## 원칙

1. 모든 프로젝트에 모든 트랙을 만들지 않는다.
2. 트랙은 단기/실행 중심이다.
3. 전체 방향은 여전히 `MISSION`과 `ROADMAP`이 잡는다.
4. 트랙은 프로젝트를 돕는 부속판이지, 프로젝트를 대체하지 않는다.
