# Obsidian Runtime Surface Module v0.1

## 목적

이 문서는 Obsidian을 단순 메모 앱으로 붙이는 설계가 아니라,  
`Jarvis Starter Pack` 안에서 **인간이 읽고 탐색하고 검토하는 운용 표면**으로 편입하는 설계안이다.
여기서 설명하는 구조는 기본 스타터 본체가 아니라, 필요 시 덧붙이는 옵션 레이어다.

핵심 질문은 이것이다.

- LLM은 어디를 읽고 어디를 쓰는가
- 인간은 어디를 보고 어디서 판단하는가
- Obsidian은 이 둘 사이에서 무엇을 맡는가

이 문서는 그 답을 `raw / wiki / schema` 3층 구조로 고정한다.

---

## 한 줄 정의

**Obsidian은 Jarvis의 뇌가 아니라, Jarvis가 유지하는 지식층을 사람이 읽고 탐색하는 운영 표면이다.**

---

## 왜 wiki여야 하는가

raw source를 매번 다시 검색하고 다시 읽게 만들면,
질문은 반복될수록 비슷한 비용을 계속 낸다.

반대로 wiki는 다르다.

- 한 번 읽은 source가 다시 축적된다
- 답변 과정에서 만들어진 정리가 다시 자산이 된다
- 연결과 허브가 시간이 갈수록 더 좋아진다
- 질의 결과가 다음 질의를 더 빠르게 만든다

즉 wiki는 일회성 응답 캐시가 아니라 **누적되는 지식 산출물(compounding artifact)** 이다.

Obsidian을 붙인다는 것은 단순 검색면을 추가하는 것이 아니라,
이 누적 산출물을 사람이 따라갈 수 있는 시각적 표면을 붙이는 일이다.

---

## 왜 넣어야 하는가

LLM 시스템이 커질수록 문제가 하나 생긴다.

- 원본 자료는 계속 쌓인다
- 정리 문서는 점점 늘어난다
- 관계와 충돌은 더 복잡해진다
- 사람이 전체를 눈으로 훑기가 어려워진다

이때 Obsidian은 다음 일을 맡을 수 있다.

- wiki 문서를 눈으로 읽기
- 링크를 따라가며 탐색하기
- graph view로 연결 상태 보기
- index와 log를 빠르게 확인하기
- raw source와 compiled knowledge를 구분해서 보기

즉 Obsidian은 생산 엔진이 아니라 **운용 확인면**이다.

---

## 기본 구조

Obsidian을 붙일 때는 다음 세 층을 분리해야 한다.

### 1. Raw Sources

원본 자료 보관층이다.

- 웹 클리핑
- PDF
- 기사
- 논문
- 회의록
- 대화 기록
- 이미지

원칙:

- 이 층은 원본이다
- LLM은 읽기만 한다
- 수정하지 않는다
- source of truth는 여기다

### 2. Wiki Layer

LLM이 유지하는 지식층이다.

- topic page
- entity page
- concept page
- synthesis page
- comparison page
- reading companion page

원칙:

- 인간이 직접 쓰는 층이 아니다
- LLM이 만들고 갱신한다
- 질문 결과도 가치가 있으면 다시 이 층으로 편입한다
- cross-reference는 여기서 유지한다

### 3. Schema Layer

LLM이 어떻게 움직여야 하는지 정하는 규칙층이다.

- `AGENTS.md`
- `START_HERE.md`
- `MAP.md`
- ingest rule
- query rule
- lint rule
- naming rule

원칙:

- 이 층이 없으면 LLM은 generic chatbot로 돌아간다
- 이 층이 있으면 LLM은 disciplined wiki maintainer로 움직인다

---

## Jarvis Starter Pack에 넣을 때의 해석

Jarvis Starter Pack 기준으로는 이렇게 읽는다.

- `raw` = 외부 입력과 원본 저장소
- `wiki` = LLM이 유지하는 markdown knowledge base
- `schema` = starter pack core/protocol/policy/rule 문서

즉 Obsidian은 `knowledge layer viewer`이자 `runtime reading surface`다.

중요한 점은 이거다.

- Obsidian은 브레인을 대체하지 않는다
- Obsidian은 팩토리를 대체하지 않는다
- Obsidian은 에이전트 시스템을 대체하지 않는다

대신 이것을 가능하게 한다.

- 사람이 지식층을 눈으로 따라가기
- 사람이 링크와 허브를 확인하기
- 사람이 유지 상태를 감시하기

---

## 권장 폴더 모델

최소 구조는 이렇게 간다.

```text
vault/
  raw/
    inbox/
    clipped/
    assets/
  wiki/
    index.md
    log.md
    topics/
    entities/
    concepts/
    syntheses/
  schema/
    AGENTS.md
    START_HERE.md
    MAP.md
    INGEST_RULES.md
    QUERY_RULES.md
    LINT_RULES.md
```

설명:

- `raw/`
  - 원본 입력층
- `wiki/`
  - LLM이 유지하는 지식층
- `schema/`
  - LLM 운용 규칙층

핵심은 폴더 이름보다 **세 층의 분리**다.
즉, 아래 예시는 권장 예시일 뿐이며 파일명이나 폴더명은 실제 운영 환경에 맞게 바꿔도 된다.

---

## 권장 운영 파일

### `index.md`

역할:

- 위키 전체 항목의 카탈로그
- 각 페이지 링크와 한 줄 설명
- category 단위 탐색 입구

효과:

- LLM이 query 전에 먼저 읽을 얇은 지도
- 인간도 graph에 들어가기 전에 전체를 훑을 수 있음

### `log.md`

역할:

- ingest
- query
- lint
- revision

같은 운영 기록을 시간 순서로 남김

효과:

- 최근 무엇이 바뀌었는지 추적 가능
- 위키 진화 과정을 timeline으로 확인 가능

---

## 기본 운용 루프

### 1. Ingest

새 자료가 들어오면:

- raw에 저장
- LLM이 읽음
- wiki에 요약/주제/엔티티/개념 페이지 갱신
- index 갱신
- log에 기록

### 2. Query

질문이 들어오면:

- index를 먼저 본다
- relevant page를 읽는다
- answer를 만든다
- 가치가 있으면 answer를 wiki로 다시 편입한다

핵심:

- 답변은 끝이 아니다
- 좋은 답변은 다시 wiki를 두껍게 만든다
- 즉 query는 소비가 아니라 **지식층의 재적재 루프**이기도 하다

### 3. Lint

주기적으로:

- orphan page 확인
- stale claim 확인
- contradiction 확인
- missing cross-reference 확인
- 빈 category 확인

즉 위키 건강검진을 한다.

---

## 인간과 LLM의 역할 분리

### 인간

- source를 고른다
- 질문을 던진다
- 강조점을 결정한다
- 결과를 읽고 판단한다

### LLM

- 요약한다
- 링크를 건다
- 관련 페이지를 갱신한다
- 충돌을 표시한다
- bookkeeping을 맡는다

즉 인간은 `판단`, LLM은 `유지관리`를 맡는다.

---

## Git과 버전 이력

wiki는 notes app처럼 보여도, 실제로는 **버전 이력 있는 knowledge repo**로 다루는 편이 좋다.

권장:

- vault 전체를 git으로 관리
- ingest / page split / merge / contradiction fix 를 commit 단위로 남김
- 중요한 page 개편은 diff로 검토
- stale claim 제거와 구조 변경도 이력으로 추적

이유:

- 지식층이 어떻게 바뀌었는지 다시 볼 수 있다
- 잘못된 합성이나 과한 압축을 되돌릴 수 있다
- LLM이 만든 변경을 인간이 검토하기 쉬워진다

즉 Obsidian은 viewer지만, 그 뒤의 wiki는 **git-backed maintained artifact**로 보는 게 맞다.

---

## Obsidian 기능을 넣을 때의 우선순위

우선순위는 이 순서가 좋다.

1. markdown vault
2. links
3. index.md
4. log.md
5. graph view
6. attachments/assets
7. clipper
8. optional plugins

이 순서가 좋은 이유:

- 처음부터 플러그인에 기대지 않는다
- 기본 markdown 운용이 먼저 선다
- 나중에 필요한 것만 붙인다

---

## 붙여도 좋은 기능

### 기본적으로 추천

- Web Clipper
- local attachment download
- graph view

### 상황 따라 추천

- Dataview
- Marp
- search helper
- local markdown search engine
- optional CLI search / lint bridge

원칙:

- Obsidian 기능을 늘리는 것이 목적이 아니다
- wiki 운용을 더 잘 보이게 만드는 기능만 붙인다

---

## Starter Pack에 넣을 때의 모듈 정의

이 모듈은 다음처럼 정의할 수 있다.

### module role

`Obsidian Runtime Surface`

### trigger

- 지식층이 커져서 눈으로 확인할 표면이 필요할 때
- LLM이 유지한 wiki를 사람이 따라가며 검토해야 할 때
- raw source / wiki / schema를 분리 운용해야 할 때

### not this

- Obsidian을 브레인 본체로 쓰는 설계
- 사람이 wiki를 직접 손으로 다 유지하는 설계
- raw source와 compiled page가 섞이는 설계

### output

- vault structure
- index/log discipline
- ingest/query/lint loop
- human/LLM role split
- compounding wiki discipline
- git-backed change trace

---

## 도입 시 주의점

### 1. Obsidian을 과대평가하지 말 것

Obsidian은 인터페이스다.  
브레인도 아니고 에이전트도 아니다.

### 2. raw와 wiki를 섞지 말 것

이게 섞이면 source of truth가 무너진다.

### 3. 인간이 직접 유지보수자가 되지 말 것

인간이 다 고치기 시작하면 유지 비용이 다시 폭발한다.

### 4. schema 없이 vault만 만들지 말 것

규칙이 없으면 LLM은 페이지를 제멋대로 만든다.

---

## 추천 도입 순서

1. raw / wiki / schema 3층 고정
2. `index.md`, `log.md` 추가
3. ingest rule 문서화
4. query rule 문서화
5. lint rule 문서화
6. Obsidian에서 실제 읽기/탐색 시작
7. 필요하면 search/dataview/marp 추가

주의:
- 이 순서는 `Obsidian` 옵션을 붙일 때의 권장 순서다.
- 스타터 본체 자체가 이 파일들을 반드시 지금 당장 가져야 한다는 뜻은 아니다.
- `AGENTS.md`, `INGEST_RULES.md`, `QUERY_RULES.md`, `LINT_RULES.md` 같은 이름은 schema layer 예시다.

---

## 확장 포인트

기본 운용이 자리 잡은 뒤에는 다음 확장을 붙일 수 있다.

### 1. Local Search Bridge

- ripgrep
- local markdown index
- optional CLI search helper

용도:

- vault 전체에서 빠른 recall
- orphan / duplicate / stale phrase 탐색
- index 이전의 저수준 탐색 보조

### 2. Citation Discipline

- wiki page에 raw source 링크를 남김
- 중요한 주장에는 source path 또는 note link를 남김
- compaction 과정에서도 trace를 잃지 않게 함

### 3. Export / Compile Surface

- 읽는 표면은 Obsidian
- 외부 전달은 handoff / brief / packet 으로 compile
- 즉 vault를 그대로 배포하지 않고, 목적별 산출로 떨굼

핵심은:

- viewer와 exporter를 섞지 않는다
- wiki는 지식 유지층
- handoff는 전달층

---

## 다른 브레인에게 보여줄 때의 설명

이 모듈을 설명할 때는 이렇게 말하면 된다.

> Obsidian은 Jarvis의 뇌가 아니라, Jarvis가 유지하는 지식층을 사람이 읽고 검토하는 표면이다.  
> raw source는 건드리지 않고, LLM이 wiki를 유지하며, schema가 그 운용 규칙을 잡는다.

---

## 한 줄 결론

**Obsidian을 넣는다는 것은 메모 앱을 추가하는 것이 아니라, `raw / wiki / schema`를 눈으로 운용하는 표면을 Starter Pack 안에 공식 편입하는 일이다.**

---

## 참고 자료

- Concept note:
  - Andrej Karpathy, *LLM Wiki*  
    [https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- Official:
  - https://obsidian.md
  - https://help.obsidian.md
