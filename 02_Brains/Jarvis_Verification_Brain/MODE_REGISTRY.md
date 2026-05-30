# Mode Registry

## `structure_validation`

폴더, 파일, 링크, 부팅 경로, 필수 표면을 검증한다.

## `document_validation`

문서 목적, 읽기 순서, 출력 계약, 금지 범위를 검증한다.

## `brain_validation`

브레인 정체성, 재진입 표면, 함수팩, 출처 바인딩, 작업 적치면을 검증한다.

## `code_validation`

코드 변경, 테스트, 에러 경로, 회귀 위험을 검증한다.

## `release_hygiene`

개인 경로, 생성물, 공개 부적합 흔적, 배포 체크를 검증한다.

## `proof_review`

증거 수준과 검증 주장이 맞는지 검토한다.

## `revalidation`

수정 뒤 같은 기준으로 다시 확인한다.

## 선택 규칙

- 브레인이나 폴더는 `brain_validation` 또는 `structure_validation`을 먼저 쓴다.
- 문서 계약은 `document_validation`을 쓴다.
- 코드 변경은 `code_validation`을 쓴다.
- 배포 전이면 `release_hygiene`을 붙인다.
- 수정 후에는 `revalidation`으로 닫는다.
