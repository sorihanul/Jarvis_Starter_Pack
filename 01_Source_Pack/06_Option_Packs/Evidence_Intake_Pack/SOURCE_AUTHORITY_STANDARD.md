# Source Authority Standard v0.1

## 목적

자료를 모두 같은 무게로 다루지 않는다.

출처의 위치와 확인 상태를 먼저 나눈 뒤, 설계에 쓸 수 있는지 판단한다.

## 출처 등급

```text
primary:
  원본 문서, 공식 발표, 원 논문, 원 저장소, 직접 관찰한 파일.

artifact:
  실제 파일, 설정, 테스트 결과, 실행 로그, 산출물.

secondary:
  신뢰 가능한 해설, 기술 글, 문서화된 사례.

commentary:
  소셜 글, 요약글, 의견글, 추천글.

unknown:
  출처가 불분명하거나 확인할 수 없는 자료.
```

## 우선순위

```text
1. primary
2. artifact
3. secondary
4. commentary
5. unknown
```

`commentary`는 방향을 잡는 데 쓸 수 있다.
하지만 사실 확정이나 기능 판정의 단독 근거로 쓰지 않는다.

## 최신성 확인

아래 항목은 날짜나 버전 확인이 필요하다.

```text
software_behavior:
  도구 기능, 설치법, 설정법, API 동작.

product_claim:
  제품이 무엇을 지원한다는 주장.

performance_or_score:
  성능, 점수, 비교 우위.

policy_or_license:
  라이선스, 사용 조건, 권한 정책.
```

## 출력

```text
source_label:
source_type: primary | artifact | secondary | commentary | unknown
observed_at:
version_or_date:
authority_reason:
limits:
```
