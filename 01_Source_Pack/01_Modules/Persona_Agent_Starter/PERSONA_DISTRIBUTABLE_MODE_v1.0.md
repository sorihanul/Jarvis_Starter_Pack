# Persona Distributable Mode v1.0 (Starter)

목적: 외부 공유 시 민감 운용 정보 노출을 막는다.

## 배포 허용
- Persona Card 요약
- 배포형 샘플 문장
- 고수준 스타일 가이드

## 민감 정보 제외
- 민감 튜닝값
- 민감 평가 상세 로그
- 보호용 규칙/구조
- 실험 중인 운영 파라미터

## 배포 변환 규칙
1. 원본 JSON에서 민감 필드 제거
2. 수치 파라미터는 범주형으로 치환(예: high/mid/low)
3. 상세 오류 로그는 요약 문장으로만 변환

## 배포 체크리스트
- 개인 정보(PII) 없음
- 보호 규칙 노출 없음
- 타인 문체 복제 지시 없음
- 위험 도메인 직접 지시 없음

## 배포형 출력 템플릿
```yaml
persona_name: ""
role: ""
domain: ""
style_summary:
  do: []
  avoid: []
distributable_sample: ""
notes: "민감 파라미터와 보호 규칙은 배포 산출물에 넣지 않는다"
```
