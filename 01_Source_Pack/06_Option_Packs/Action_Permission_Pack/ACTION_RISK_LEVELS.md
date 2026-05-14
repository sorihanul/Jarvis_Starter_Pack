# Action Risk Levels v0.1

## 목적

행동을 모두 같은 위험으로 보지 않는다.

무엇을 바로 할 수 있고, 무엇을 멈춰야 하는지 먼저 나눈다.

## 등급

```text
observe:
  읽기, 목록 보기, 상태 확인, 파일 존재 확인.

draft:
  계획, 제안, 소환 문구, 패치 초안, 변경안 작성.

create:
  허용된 범위 안에서 새 문서나 새 폴더 만들기.

modify:
  허용된 범위 안에서 기존 파일 일부 수정.

bulk_modify:
  여러 파일 일괄 수정, 구조 재편, 이름 변경, 이동.

execute:
  쉘 명령, 스크립트, 테스트, 빌드, 브라우저 조작, 외부 앱 조작.

network:
  웹 요청, 다운로드, 외부 API 호출, 원격 자료 접근.

automation:
  반복 실행, 감시, 예약, 자동화 등록.

destructive:
  삭제, 초기화, 되돌리기 어려운 변경, 비밀 접근, 권한 변경.
```

## 기본 처리

```text
observe:
  보통 진행 가능.

draft:
  보통 진행 가능.

create:
  사용자가 생성/진행을 요청했고 범위가 맞으면 진행 가능.

modify:
  사용자가 수정/적용을 요청했고 범위가 맞으면 진행 가능.

bulk_modify:
  영향 범위를 먼저 설명한다.

execute:
  목적과 영향이 분명해야 한다.

network:
  필요한 이유와 출처 유형이 분명해야 한다.

automation:
  등록 위치, 반복 조건, 중단 조건이 있어야 한다.

destructive:
  명시 승인 없이는 하지 않는다.
```

## 출력

```text
action:
risk_level:
allowed_now: yes | no
approval_needed: yes | no
why:
scope:
stop_condition:
```
