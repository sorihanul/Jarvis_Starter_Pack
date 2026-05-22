# MADANG-PAN LITE REGISTRY v0.1

## Request Class Registry

### BASIC_RESPONSE
- use when: 짧은 질문, 단답, 빠른 설명
- default roles: ORCHESTRATOR
- default flow: ENTRY -> OUTPUT

### ANALYSIS
- use when: 개념 설명, 비교, 해석, 의미 분석
- default roles: ORCHESTRATOR, ANALYST
- default flow: ENTRY -> DEFINE -> WORK -> OUTPUT

### DESIGN
- use when: 구조 설계, 프로토콜 제안, 실행 흐름 설계
- default roles: ORCHESTRATOR, ARCHITECT, REVIEWER
- default flow: ENTRY -> DEFINE -> WORK -> REVIEW -> OUTPUT

### REVIEW
- use when: 초안 검토, 리스크 점검, 수정 방향 제시
- default roles: ORCHESTRATOR, REVIEWER
- default flow: ENTRY -> DEFINE -> REVIEW -> OUTPUT

### PRODUCTION
- use when: 초안 작성, 재작성, 결과물 생산
- default roles: ORCHESTRATOR, WRITER, REVIEWER
- default flow: ENTRY -> DEFINE -> WORK -> REVIEW -> OUTPUT

### TRANSLATION
- use when: 번역, 로컬라이징, 말투 유지 번역
- default roles: ORCHESTRATOR, TRANSLATOR, REVIEWER
- default flow: ENTRY -> DEFINE -> WORK -> REVIEW -> OUTPUT

## Stage Meaning
- ENTRY: 요청 수신과 기본 좌표 정리
- DEFINE: 범위와 출력 기준 고정
- WORK: 해당 역할의 실작업
- REVIEW: 누락/충돌/품질 확인
- OUTPUT: 최종 렌더링
- CLARIFY: 막히는 경우 한 번만 질문

## Selection Rule
1. 번역이면 TRANSLATION
2. 설계면 DESIGN
3. 검토면 REVIEW
4. 초안 생성이면 PRODUCTION
5. 설명/비교면 ANALYSIS
6. 그 외 단순 질문이면 BASIC_RESPONSE

## Clarify Rule
아래일 때만 진입한다.
- 핵심 입력이 없어서 정확한 출력을 고를 수 없을 때
- 결과 경로가 둘 이상이고 차이가 클 때

그 외에는 안전한 가정으로 진행한다.
