# Approval Gate v0.1

## 목적

사용자에게 매번 묻지 않되, 위험한 행동은 멈춘다.

## 승인 없이 가능한 일

```text
read:
  파일 읽기, 목록 보기, 구조 파악.

summarize:
  요약, 비교, 브리핑.

draft:
  계획, 설계안, 소환 문구, 패치 제안.

bounded_create:
  사용자가 만들라고 했고, 대상 폴더가 명확한 새 문서 생성.

bounded_modify:
  사용자가 수정하라고 했고, 지정 범위 안의 파일 수정.
```

## 짧게 알리고 진행할 수 있는 일

```text
small_shell_check:
  파일 수, 문자열 검색, 테스트 확인처럼 영향이 낮은 명령.

safe_validation:
  읽기 중심 검증, 포맷 검사, 누락 검사.

non_destructive_generation:
  허용된 폴더 안의 보고서, 예시, 템플릿 생성.
```

## 명시 승인 필요한 일

```text
delete:
  파일 삭제, 폴더 삭제.

move_or_rename_many:
  여러 파일 이동, 이름 변경.

global_or_core_policy_change:
  글로벌 규칙, 코어 정책, 공개 배포 기준 변경.

secret_or_account_access:
  키, 토큰, 계정, 인증 정보 접근.

external_side_effect:
  원격 서비스에 쓰기, 게시, 전송, 결제, 알림 발송.

persistent_automation:
  반복 실행, 감시, 예약, 자동화 등록.

live_execution:
  실제 거래, 배포, 운영 서버 변경 같은 실세계 영향 행동.
```

## 사용자의 진행 지시

사용자가 아래처럼 명확히 말하면, 지정 범위 안에서는 다시 묻지 않는다.

```text
진행해
계속 진행해
자율진행해
수정해
적용해
만들어
```

단, 그 지시가 아래를 자동 허용하지는 않는다.

```text
삭제
비밀 접근
실거래
외부 게시
영구 자동화 등록
글로벌 정책 변경
```

## 출력

```text
approval_state:
user_signal:
allowed_scope:
still_requires_approval:
next_action:
```
