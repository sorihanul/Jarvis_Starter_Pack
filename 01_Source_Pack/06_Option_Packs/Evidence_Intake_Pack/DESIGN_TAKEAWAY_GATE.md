# Design Takeaway Gate v0.1

## 목적

자료에서 좋은 말이 아니라 자비스에 쓸 수 있는 설계 법칙만 남긴다.

## 통과 조건

설계 반영은 아래를 만족해야 한다.

```text
grounded:
  근거가 있다.

reusable:
  특정 제품이나 서비스에 묶이지 않는다.

bounded:
  사용 조건과 중단 조건이 있다.

layered:
  자비스의 어느 층에 들어갈지 정해져 있다.

testable:
  작은 검증 방법이 있다.
```

## 보류 조건

```text
claim_only:
  주장만 있고 확인이 없다.

marketing_only:
  홍보 문구에 가깝다.

tool_required:
  실행 도구나 설치가 있어야만 검증된다.

too_broad:
  코어 전체를 바꾸려 한다.

domain_specific:
  기본 스타터가 아니라 도메인 팩에 들어가야 한다.
```

## 설계 반영 등급

```text
adopt:
  지금 자비스 규칙으로 반영해도 된다.

candidate:
  규칙 후보로 둘 수 있다.

hold:
  검증 전까지 보류한다.

reject:
  반영하지 않는다.
```

## 출력

```text
takeaway:
evidence_state:
design_grade: adopt | candidate | hold | reject
target_layer:
use_when:
stop_when:
validation_needed:
reason:
```
