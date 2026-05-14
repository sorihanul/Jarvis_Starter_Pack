# Codex Standard Roles v0.1

이 문서는 `Jarvis Starter`에서 권장하는 `Codex` 표준 역할 6개를 설명한다.

## 핵심 원칙

- 역할 설명 문서는 `MD`로 볼 수 있다.
- 하지만 실제 Codex 역할 파일은 반드시 `MD`가 아니라 `TOML`로 두는 편이 맞다.
- Codex 공개 문맥에서 가장 표준적인 표면은 `.codex/agents/*.toml` 계열의 standalone custom agent 파일이다.
- 이 모듈은 그 공식 표면과, 로컬 참고용 fragment 표면을 둘 다 제공한다.

즉:
- `AGENTS.md` = 프로젝트 지침
- `.codex/agents/*.toml.example` = 공식 custom agent 예시
- `roles/*.toml` = 로컬에서 참고하거나 수동 조합할 수 있는 fragment 예시

## 표준 역할 6개

1. `research`
- 문서, 코드, 구조, 경로 조사

2. `implementation`
- 제한된 파일 범위 안에서 실제 수정

3. `validation`
- 테스트, 검증, 리스크 확인

4. `synthesis`
- 여러 결과를 묶어 최종 응답으로 정리

5. `security_gate`
- 외부 입력, 출력, 명령, 민감정보 리스크 점검

6. `writing`
- 문체, 구조, 요구사항을 맞춘 초안/수정

## 포함된 TOML 파일

- `.codex/agents/research.toml.example`
- `.codex/agents/implementation.toml.example`
- `.codex/agents/validation.toml.example`
- `.codex/agents/synthesis.toml.example`
- `.codex/agents/security-gate.toml.example`
- `.codex/agents/writing.toml.example`
- `roles/research.toml`
- `roles/implementation.toml`
- `roles/validation.toml`
- `roles/synthesis.toml`
- `roles/security_gate.toml`
- `roles/writing.toml`

## 권장 연결 방식

### 기본 공개 예시

사용자는 먼저 `.codex/agents/*.toml.example`를 자기 프로젝트의 `.codex/agents/*.toml`로 복사해서 쓰는 편이 가장 단순하다.

각 파일은 최소:
- `name`
- `description`
- `developer_instructions`
를 가진 standalone custom agent 예시다.

### 로컬 참고 예시

사용자는 아래 조각을 로컬 참고 예시로 볼 수 있다.
다만 이 방식은 Codex 공개 문서의 기본 표면이 아니므로, 실제 적용 전 현재 버전 동작을 확인하는 편이 안전하다.

```toml
[agents.research]
description = "Read docs, inspect structure, and return facts and paths."
config_file = "../01_Modules/Codex_Agent_Starter/roles/research.toml"
```

필요하면 이 역할 파일들을 사용자 로컬 `.codex/roles/`로 복사해 써도 된다. 중요한 점은 `역할 정의 표면은 TOML`이어야 한다는 것이다.
