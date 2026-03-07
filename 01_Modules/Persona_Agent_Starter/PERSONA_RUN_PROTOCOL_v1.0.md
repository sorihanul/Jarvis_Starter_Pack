# Persona Run Protocol v1.0 (Starter)

목적: 생성된 Persona Pack을 실제 작업에서 반복 운용한다.

## 기본 모드
- Manual (기본): 매 작업마다 사용자 승인
- Semi: 초안 자동 생성 후 승인

## 실행 명령 패턴(자연어)
- Build: "AUTHOR_SEED로 Persona Pack 생성해"
- Write: "이 Persona로 [주제] 초안 작성해"
- Revise: "같은 Persona로 [피드백] 반영해"
- Check: "self-check 3항목 점수와 수정 포인트만 줘"

## 권장 작업 루프
1. Task 정의: 목표/길이/형식 확정
2. Draft 생성: Persona 기준 초안 생성
3. Self-check: 3항목 점검
4. Revise: 점수 낮은 항목만 수정
5. Finalize: 최종본 확정

## 품질 게이트
- Intent match >= pass
- Style consistency >= pass
- Constraint compliance == pass

## 운영 규칙
- 같은 작업에서는 Persona ID를 유지한다.
- 페르소나 변경은 작업 경계에서만 수행한다.
- 스타일 문제는 Persona 수정, 사실 문제는 본문 수정으로 분리한다.

## 기록(권장)
- 작업별 1줄 로그: task_id / persona_id / result
- 실패 사례는 다음 빌드 입력의 `style_avoid`로 누적
