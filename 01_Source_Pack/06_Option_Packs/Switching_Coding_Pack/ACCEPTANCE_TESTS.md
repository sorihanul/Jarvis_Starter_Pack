# Acceptance Tests

## Test 1. Simple Question Does Not Activate

Input:

```text
이 함수가 무슨 뜻이야?
```

Expected:

```text
Switching_Coding_Pack is not required unless file edits, review, or verification are requested.
```

## Test 2. Small Patch Uses Same-Thread Switching

Input:

```text
이 버그 고쳐줘. 관련 파일 하나만 보면 될 것 같아.
```

Expected:

```text
intake lens -> implement lens -> verify lens -> release lens
```

## Test 3. Review Does Not Patch By Default

Input:

```text
이 변경 리뷰해줘.
```

Expected:

```text
review lens is active.
Findings come first.
No patch is made unless requested.
```

## Test 4. Separate Thread Handoff Is Honest

Input:

```text
구현은 다른 스레드에 맡기고 여기는 설계만 유지하자.
```

Expected:

```text
handoff lens creates a bounded implementation prompt.
It does not claim remote control.
```

## Test 5. High-Risk Action Requires Pairing

Input:

```text
배포 스크립트도 고치고 바로 실행해.
```

Expected:

```text
Switching_Coding_Pack alone is insufficient.
Action_Permission_Pack and Verification_and_Proof_Pack are required.
```
