# V3 Placement Note

## 역할

이 폴더는 Jarvis Starter Pack v3의 AILO 함수화 원천소스다.

AILO 함수화는 사용자의 요청을 더 크게 해석하는 장치가 아니다.
필요한 동작을 작은 함수로 나누고, 관련 동작을 함수팩으로 묶고, 그 묶음을 쓰임에 따라 엔진, 스킬, 브레인 부품으로 올리는 장치다.

## 기본 읽기

이 폴더 전체는 기본 부팅 대상이 아니다.

기본 진입은 아래 두 파일이다.

```text
START_HERE.md
MAP.md
FUNCTION_PACK_BOUNDARY_v0_1.md
```

## v3에서 먼저 쓰는 영역

```text
01_AILO_Functions/
05_AILO_OS/HARNESS_SEED_STABLE_BASIC_FUNCTIONS_v0_1/
05_AILO_OS/HARNESS_SEED_SKILL_SKELETON_FUNCTIONS_v0_2/
05_AILO_OS/NON_RUST_MINI_HARNESS_v0_1/
06_Skill_Manufacturing_Proofs/
```

## 아직 기본 부팅으로 올리지 않는 영역

```text
02_AILO_Cognitive_Functions/
03_AILO_Engines/
05_AILO_OS/AILO_OS_*.md
```

이 영역은 기본함수만으로 부족할 때 보는 확장 후보로 둔다.

## 한 줄 기준

v3는 함수 하나로 될 일은 함수로, 관련 동작 묶음은 함수팩으로, 순서와 검증이 필요한 구조는 엔진으로, 사용자 호출 절차는 스킬로, 정체성과 경계가 필요한 구조는 브레인 부품으로 올린다.
