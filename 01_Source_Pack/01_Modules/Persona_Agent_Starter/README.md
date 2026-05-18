# Persona Agent Starter

## 목적

이 모듈은 특정 역할, 말투, 판단 기준을 가진 페르소나형 에이전트를 만들 때 사용한다.

페르소나는 장식용 캐릭터가 아니다.
목표는 작업 방식, 금지, 판단 기준, 출력 자세를 일관되게 고정하는 것이다.

## 언제 읽는가

```text
사용자가 특정 역할의 에이전트를 만들고 싶어 할 때
글쓰기, 조사, 검증, 비서, 코딩 같은 반복 역할이 필요할 때
브레인의 말투보다 작업 자세와 판단 기준을 고정해야 할 때
```

## 읽기 순서

1. `PERSONA_BUILD_SPEC_v1.0.md`
2. `PERSONA_SEED_TEMPLATE_v1.0.md`
3. `PERSONA_RUN_PROTOCOL_v1.0.md`
4. `PERSONA_DISTRIBUTABLE_MODE_v1.0.md`

## 사용 원칙

- 사용자가 긴 페르소나 설정을 직접 쓰게 하지 않는다.
- 목적, 역할, 금지, 출력 기준을 먼저 잡는다.
- 실제 작업에 도움이 되지 않는 성격 묘사는 줄인다.
- 배포형 페르소나는 특정 개인, 제한 체계, 기기 고유 작업 경로에 의존하지 않는다.

## 산출물

```text
persona_name:
role:
main_tasks:
must_do:
must_not_do:
input_style:
output_style:
handoff_prompt:
acceptance_test:
```

## 금지

- 유명인의 실제 문체를 그대로 재현한다고 주장하지 않는다.
- 캐릭터성 때문에 작업 정확도를 낮추지 않는다.
- 정체성과 작업 로그를 섞지 않는다.
- 원천소스를 새 페르소나 안에 통째로 복사하지 않는다.
