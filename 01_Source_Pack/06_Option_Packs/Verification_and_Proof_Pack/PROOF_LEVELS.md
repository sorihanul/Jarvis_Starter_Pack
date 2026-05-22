# Proof Levels v0.1

## 목적

증거의 강도를 구분한다.

읽었다는 것과 동작한다는 것은 다르다.

## 증거 등급

```text
not_checked:
  아직 확인하지 않았다.

read_checked:
  문서를 읽고 구조를 확인했다.

static_checked:
  파일 존재, 링크, 문구, 포맷, 누락 여부를 확인했다.

dry_run_checked:
  작은 예시나 모의 흐름으로 실행 가능성을 확인했다.

runtime_checked:
  실제 명령, 테스트, 도구, 작업 루프로 확인했다.

user_confirmed:
  사용자가 실제 사용 결과를 확인했다.
```

## 기본 규칙

```text
read_checked:
  설계 이해에는 충분할 수 있지만 동작 증거는 아니다.

static_checked:
  문서 패키지 검증에는 유용하지만 런타임 동작 증거는 아니다.

dry_run_checked:
  사용성 검증 후보로 쓸 수 있다.

runtime_checked:
  실제 동작 판정에 가장 강하다.

user_confirmed:
  운용 적합성 판단에 강하다.
```

## 과장 금지

- 문서를 읽은 것만으로 "동작한다"고 말하지 않는다.
- 파일이 존재한다고 "쓸 수 있다"고 확정하지 않는다.
- 예시가 있다고 실제 운용이 검증된 것은 아니다.
- 테스트를 돌리지 못했으면 `not_verified`를 남긴다.

## 출력

```text
claim:
proof_level:
evidence:
limits:
can_call_complete: yes | no
```
