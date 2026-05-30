# Current Task

## 상태

- status: idle
- owner: Jarvis_Verification_Brain
- active_scope: none
- current_target: none
- current_goal: none
- runtime_session_id: assign_on_boot
- next_action: wait_for_verification_request

## 배포 기준

- packaged_state: dormant_reference_brain
- first_runtime_action: 검증 대상, 목표, 성공 기준을 요청한다.

## 사용 규칙

- 새 검증 요청이 들어오면 대상, 목표, 성공 기준, 증거 수준을 짧게 기록한다.
- 장기 검증 후보는 `VERIFICATION_QUEUE.md`로 보낸다.
- 자세한 기록은 `../LOGS/SESSION_OPS_LOG.md`에 둔다.
- 다음 세션 인계는 `../CAPSULES/CURRENT_CAPSULE.md`에 둔다.
