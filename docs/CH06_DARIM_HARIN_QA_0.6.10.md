# CH06 다림·하린 CG / 비밀 메모 QA 0.6.10

2026-11-14, frozen `0.6.10-test` 후보 검증 결과: **PASS**. Compile·lint 종료 코드 0, native 11 cases / 36 assertions 통과. 첫 실행에서 모두 통과했고 product 수정 없이 종료했다.

## 범위와 격리

- 후보: `tests/ch06_darim_harin_0610/candidate`.
- SDK: Ren'Py 8.5.3, 기존 공개 빌드 `2026111204`의 compiled script ID seed 사용.
- `SDL_VIDEODRIVER=dummy`, SW renderer 및 검증용 framebuffer 보정 fixture 사용. 운영체제 UI·포커스·실제 마우스 입력을 사용하지 않는다.
- 저장·persistent·TEMP·TMP는 QA 하위 D: 경로로 격리한다. 실제 저장 파일의 SHA-256 및 수정 시간을 실행 전후 비교한다.
- product/game에 테스트 코드를 추가하지 않는다. 실제 CH06 장면/CG 및 프로필 모달 화면을 후보에 복사해 실행한다.

## 경계 검증 결과

- 다림 1: `선배, 많이 기다리셨어요?`에서 첫 컷, `차분하게 웃는 모습과 달리 눈빛은 꽤 진지했다.`까지 유지, 다음 진행 요원 대사에서 standing.
- 다림 2: `생각보다 재미있었어요.`에서 두 번째 컷, `그렇게 말씀하시니까 기분 좋네요.`까지 유지, 다음 대사에서 standing.
- 하린 1: `……재미있네요.`에서 첫 컷, `……그런가.` 및 사이 주인공 대사까지 유지.
- 하린 2: 바로 다음 하린 `…….`에서 CG 간 직접 교체; `나는 무슨 뜻인지 되묻고 싶었지만, 선배가 먼저 일어섰다.`에는 standing 복귀.
- 다림 CG에서 native save/load, CG 종료 및 하린 CG 전환 경계에서 native rollback 후 재진행.
- 각 캐릭터 앨범 항목 하나에 두 컷, 일반 획득 순서, test preview의 비파괴 열람, 네 이미지 누락 시 시작 거부 및 after-load standing 복귀.
- 로만·시아·오므·다림 NOTE03 secret의 제목/본문을 사용자 원문 fixture와 정확히 대조하고 실제 프로필 모달의 최하단까지 스크롤한다. production happy gate 및 test preview가 earned records를 생성하지 않는지 검증한다.

## 결과

| 실행 | 통과 case | 통과 native assertion | 로그 |
| --- | ---: | ---: | --- |
| CG 실제 경계·저장/불러오기·롤백·앨범·누락 art | 5 | 24 | `cg-first.log` |
| 4개 메모 원문·production gate·스크롤 + test preview | 5 | 10 | `notes-first.log` |
| 실제 저장 위치 격리 sentinel | 1 | 2 | `isolation-final.log` |
| 합계 | 11 | 36 | 모두 PASSED |

각 명명 suite를 선택해 실행했으므로 다른 suite의 `skipped/not run`은 선택 범위 밖 항목이다. 위 숫자는 실제 실행·통과 항목과 Ren'Py가 집계한 assertion statement 수이며, helper 내부 Python assert를 더하지 않았다.

네 CG의 native image load와 실제 화면을 확인했다. 다림 1은 1024×576, 나머지는 2048×1152이며 모두 16:9, `screen_fit=contain`, crop 없음으로 비율을 보존한다. 다림 CG 종료 뒤 `smug`/`embarrassed`, 하린 종료 뒤 `embarrassed` standing 복귀도 상태와 실제 프레임에서 확인했다. 하린의 CG1→CG2 사이에는 `cg_end`가 없고 두 번째 `cg_start`의 transition 인수는 0.35다. 두 번째 이미지가 없으면 해당 실제 분기에서 CG1을 내리고 standing으로 복귀했다.

일반 앨범은 캐릭터별 한 카드/두 컷이다. 미획득→첫 컷 획득→두 컷 획득 순서를 확인했고 test preview 열람 전후 획득 collection은 동일했다. 네 자산 각각의 누락 시작 거부와 활성 CG의 after-load 복귀도 검증했다.

메모의 기대값은 game 데이터가 아닌 `design_docs/story_sources/secret_notes_0610.json`에서 보존한 사용자 원문의 `expected_notes.json`이다. 네 제목과 본문이 공백·빈 줄·문장부호까지 일치했다. 실제 모달 viewport에서 마지막 문단까지 이동한 뒤 하단 문장과 닫기 버튼이 함께 보이는지 14개 증거 프레임을 검토했다.

| 메모 | 본문 글자 수 | viewport page | 최하단 value / range |
| --- | ---: | ---: | ---: |
| 로만 | 148 | 191 | 403 / 403 |
| 시아 | 157 | 191 | 511 / 511 |
| 오므 | 164 | 191 | 511 / 511 |
| 다림 | 185 | 191 | 511 / 511 |

`systems/cg_system.rpy`, `systems/secret_notes.rpy`, `systems/test_chapters.rpy`는 백업과 SHA-256이 같아 gate·preview 구현 변경이 없다. CH06은 7개 신규 visual block 밖의 모든 기존 실행문이 백업과 같다. frozen source 521개 파일은 실행 뒤에도 동일했고 실제 저장/persistent가 있던 2개 위치의 파일 bytes와 수정 시간도 전후 동일했다.

## 증거

- `tests/ch06_darim_harin_0610/native_results.json`: 실제 대사, CG key, 원본 이미지 크기, 복귀 표정, 메모 스크롤 수치.
- `tests/ch06_darim_harin_0610/source_records_audit.json`: 원본 실행문·gate 소스·frozen source·실제 저장 parity.
- `tests/ch06_darim_harin_0610/seed_audit.json`: 공개 build 2026111204의 95개 compiled script seed.
- `tests/ch06_darim_harin_0610/screenshots/current`: 네 CG 시작, 하린 standing 복귀, 네 메모 top/bottom 및 다림 test-preview bottom 총 14개 PNG.
- `tests/ch06_darim_harin_0610/fixtures`: 후보 전용 helper와 tests. 실제 product에는 복사하지 않는다.

검증은 실제 CH06 하위 장면과 실제 프로필 모달을 대상으로 하는 bounded offscreen native 검사다. 장 전체/모든 개인 루트 완주를 집계하지 않았고 GPU 전환 모션 평가는 포함하지 않았다.
