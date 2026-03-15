# Project Workspace Lite Overview v0.1

## 목적

스타터 팩 사용자가 복잡한 전역 체계 없이도 `프로젝트 단위로 즉시 작업`을 시작하게 하는 최소 작업장 설계다.

## 왜 필요한가

기존 스타터에는 아래 축이 이미 있다.
- 전면 분류: `Madang_Pan_Lite_Starter`
- 순차 코딩 레일: `Coding_Sequential_Agent_Starter`
- 안전 점검: `security_gate_agent`, `security_checklist`

하지만 `프로젝트 하나를 열고 문서 3종으로 정렬하는 시작점`은 약하다.

이 모듈은 그 빈칸만 메운다.

## 핵심 모델

프로젝트는 아래 3문서로 굴린다.

1. `MISSION`
- 왜 이 작업을 하는가
- 이번 범위는 어디까지인가

2. `ROADMAP`
- 프로젝트 내부 단계와 마일스톤은 어떻게 전개되는가

3. `ORCHESTRATOR`
- 누가 어떤 순서로 움직이는가
- 순차형인지, 검토형인지, 팀형인지

그리고 시작 전에 `BOOT_ENTRY`로 세션 자각을 고정한다.

## 위치

이 모듈은 `전역 운영체계`가 아니라 `개별 프로젝트 시작 레일`이다.

즉:
- 전체 자비스를 통제하지 않는다.
- 프로젝트 하나를 안정적으로 열어 주는 역할만 맡는다.

정식 프로젝트 위치:
- `TASKS/PROJECTS/<project_id>/`

정식 템플릿 위치:
- `TASKS/PROJECTS/_TEMPLATES/`

## 기본 원칙

1. 작은 프로젝트는 `MISSION + ROADMAP + ORCHESTRATOR`만 있으면 된다.
2. 전역 로드맵은 선택이다.
3. 팀별 분화는 필요할 때만 한다.
4. 작업장은 가볍게 시작하고, 커질 때만 확장한다.
