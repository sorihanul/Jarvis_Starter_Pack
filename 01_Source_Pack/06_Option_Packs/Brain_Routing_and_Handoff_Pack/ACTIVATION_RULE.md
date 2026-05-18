# Activation Rule

## Activate

Activate `Brain_Routing_and_Handoff_Pack` when the request needs brain selection, same-thread brain-lens application, separate-thread handoff, or returned-output integration.

Typical triggers:

```text
어떤 브레인을 읽어야 할지 정해야 한다
현재 스레드에서 다른 브레인 규칙을 잠깐 적용해야 한다
별도 스레드에 넘길 브레인 호출문이 필요하다
여러 브레인 산출물을 다시 읽고 통합해야 한다
읽기 전용 원본에 대해 직접 수정이 아니라 패치 브리프를 넘겨야 한다
```

## Do Not Activate

Do not activate when:

```text
단일 도메인 브레인이 이미 작업을 맡고 있다
단순 답변, 단순 요약, 단순 수정이다
브레인 선택이나 인계가 필요 없다
라우팅 표면을 만들 만큼 반복 가치가 없다
```

## Activation Test

Before using this pack, answer:

```text
Which brain should be read?
Can the current thread read it and work under that lens?
Does a separate thread need a launch prompt?
What output must return?
Who integrates the returned output?
```

If these questions are unnecessary, do not use this pack.
