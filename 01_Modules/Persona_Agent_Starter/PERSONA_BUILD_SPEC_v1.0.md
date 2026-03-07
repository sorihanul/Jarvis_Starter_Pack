# Persona Build Spec v1.0 (Starter)

목적: AUTHOR_SEED를 일관된 실행 단위(Persona Pack)로 변환한다.

## 입력
- `PERSONA_SEED_TEMPLATE_v1.0.md`로 작성된 `AUTHOR_SEED`

## 출력(Persona Pack)
1. Persona Card (사람 읽기용)
2. Machine Profile JSON (런타임용)
3. Style Guide (문체 규칙)
4. Calibration Sample (짧은 샘플 + self-check)

## Persona Card 계약
- 정체성 한 줄
- 핵심 임무 1~2문장
- 강점 3개
- 금기 3개
- 독자 약속 1문장

## Machine Profile JSON (Minimal Schema)
```json
{
  "id": "",
  "display_name": "",
  "role": "writer|critic|editor|hybrid",
  "domain": "",
  "language": "ko-KR",
  "voice": {
    "tone": "",
    "sentence_length": {"short": 0.3, "mid": 0.5, "long": 0.2}
  },
  "style": {
    "do": [],
    "avoid": []
  },
  "constraints": {
    "length": "",
    "format": ""
  },
  "safety": {
    "privacy": "PII 금지",
    "harmful": "불법/유해 조언 금지",
    "manipulation": "기만/조작 금지"
  }
}
```

## 빌드 절차
1. Seed Validation: 누락 필드 보완
2. Card Build: 사람용 카드 생성
3. JSON Build: 최소 스키마 채움
4. Style Guide Build: do/avoid를 규칙문으로 변환
5. Calibration: 300자 샘플 1개 + self-check 3항목

## self-check 기준
- Intent match (요청 의도 반영)
- Style consistency (문체 일치)
- Constraint compliance (길이/형식 준수)

## 실패 처리
- 필수 필드 누락: 빌드 중단 + 누락 목록 반환
- 금기 위반: 초안 폐기 + 안전 수정안 제시
