# 0.6.0-test · 호감도 개편과 시아 S02

기준 원본은 `D:\CampusRomance_VN\renpy_project`다. 점수는 사용자의 마지막 지시를 우선하여 **실제 5·10점**으로 고정했다. 1·2에 배율을 곱하지 않는다.

## A. 이전 구조와 발견한 문제

기존 `affection`/`trust` 사전과 `relationship_apply`, `story_apply`, `apply_choice`가 있었고, v1 하트는 이 두 값과 로만의 관계 카운터를 자동 합산했다. 신뢰도가 해피 관계와 같은 뜻으로 취급되고 일부 선택은 기존 보상과 카운터가 겹쳤다. UI의 빨간/검은 게이지는 이미 존재했다.

R06의 이전 판정은 마지막 `respect` 선택이면 누적 상태와 무관하게 해피였다. 새 판정은 실제 누적 점수·서로 다른 위험 행동·반복된 에피소드·최종 행동을 함께 사용한다. 원문 대사와 엔딩 내용은 바꾸지 않았다. CH07 직접 히로인 선택도 유지한다.

## B. 변경 파일

경로는 `D:\CampusRomance_VN` 기준이다.

| 파일 | 변경 |
| --- | --- |
| `renpy_project/game/systems/heart_system.rpy` | schema2, 선택 정책, 안전한 이전·원본 보관, 5점 격자, 독립 게이지, R06 판정, 저장 메타 연결 |
| `renpy_project/game/systems/state.rpy` | 신뢰도/기존 점수 연산 중단, 기존 변수 호환 보관, CH07 점수 제한 제거, NOTE03 이전 |
| `renpy_project/game/systems/story_runtime.rpy` | 선택 ID로 실제 보상 적용, 신뢰도 기반 동행 추정 제거 |
| `renpy_project/game/data/relationship_choices.json` | 공통·로만·구 CH01 전체 선택 200개 ID의 의미별 정책 |
| `renpy_project/game/data/sia_relationship_choices.json` | 시아 S01~S02의 9개 선택 결과 |
| `renpy_project/game/data/choices.json` | 구 CH01 선택의 원래 플래그를 유지하고 검토한 5/10점 효과 연결 |
| `renpy_project/game/data/routes.json`, `endings.json`, `profile_pages.json` | 폐기된 `min_trust` 기획 필드 제거, 시아 S02까지의 부분 구현 상태 |
| `renpy_project/game/routes/chapter01_official.rpy`~`chapter04_official.rpy`, `roman_r01.rpy`, `roman_r02.rpy` | 구 저장 실행 위치를 위해 이전 인수 문장을 호환용으로 유지하되, 인수는 무시하고 정책 ID만 실제 보상에 사용 |
| `renpy_project/game/routes/roman_r06.rpy` | 판정 함수·관계 조건을 새 점수에 연결, 심박/집착 관련 조건의 단위 유지 |
| `renpy_project/game/systems/secret_notes.rpy` | NOTE01/02 장면 기반 유지, NOTE03 해피 기본 해금, 기존 열람권 보존 |
| `renpy_project/game/screens_character_profile.rpy`, `screens_application_feedback.rpy`, `screens.rpy` | 해피·배드 호감도 명칭, 실제 값·이전 안내, 기존 알림 재사용 |
| `renpy_project/game/routes/sia.rpy`, `sia_s01.rpy`, `sia_s02.rpy`, `systems/sia_story_runtime.rpy` | CH07 시아 선택에서 확정 원고 S01→S02→저장 가능한 준비 중 화면 |
| `renpy_project/game/systems/story_draft_runtime.rpy`, `test_chapters.rpy`, `phone_timeline.rpy` | 시아 분기·테스트 진입·휴대폰 에피소드 지원 |
| `renpy_project/game/screens_test_chapters.rpy`, `screens_story_stage.rpy` | 시아 테스트 목록과 S02 완료/저장 안내 |
| `renpy_project/game/data/phone_ui.json` | 16개 에피소드의 최종 행 번호·시간·시점 조회표 |
| `tools/import_sia_first.py`, `import_roman_first.py`, `import_roman_later.py` | 원고 변환 및 전화 재계산, 새 판정의 재생성 안정성 |
| `renpy_project/game/options.rpy` | 버전 0.6.0-test |
| `renpy_project/game/data/cg_registry.json`, `images/cg/endings/sia_secret.png` | 사용자가 제공한 시아 시크릿 그림 원본 등록, SIA/ENDING에서 대본 준비 중 잠금 |
| `launcher_publish/prepare_payload.py` | 직전 공개 RPYC 이름 정보를 보존한 공식 재컴파일 |

전체 Ren'Py 프로젝트(그림·음악·저장·캐시·테스트 포함 **641파일/514,582,035바이트**)와 문서·원고를 수정 전에 `backups/relationship_overhaul_20261109_132545`에 복사했다. 기존 SDK·옛 배포판·이전 백업을 다시 중첩 복사하지 않았다. `backups/relationship_overhaul_latest.json`과 백업 내부 manifest에 범위를 기록했다.

## C. 새 점수와 저장 호환

- 저장 변수 이름은 호환을 위해 `red_hearts[hero]` / `black_hearts[hero]`를 유지하며 의미는 각각 **해피 / 배드 호감도**다. 내부 하린 ID는 `lumi`를 유지한다.
- 정책 JSON의 `happy` / `bad`는 실제 0·5·10이다. 가벼운 건강한 선택 +5, 중요한 존중/경계/창작 선택 +10, 경미한 회피/의존 강화 배드 +5, 중대한 통제/비현실적 약속 배드 +10이다. 취향·동행·장소 등은 근거가 없으면 0으로 기억만 남긴다.
- `heart_apply_choice(..., choice_id=...)`가 검토 정책을 한 번 적용한다. 두 게이지는 독립적이며, 한쪽 증가로 다른 쪽을 줄이지 않는다. 0~100, 5점 단위이며 95에서 +10을 받으면 실제 +5로 100이 된다.
- `story_apply`는 기존 값/기억 플래그를 보존한다. 카운터를 새 점수에 더하지 않는다. `affection` / `trust`는 삭제하지 않지만 새 선택·UI·엔딩 판단에 사용하지 않는다.
- 구 저장은 해당 플레이의 `choice_log`만 읽어 정책으로 재구성한다. 다른 플레이의 persistent 선택 모음을 합산하지 않는다. 구 신뢰도나 v1 자동 합산 하트를 새 해피에 그대로 복사하지 않는다.
- 이전 수치·옛 단위·선택 기록은 `heart_migration_archive`에 보관한다. 확인되지 않는 선택 ID와 구 비영점 수치는 보수적으로 재분류 안내를 표시한다. 로그 없는 점수를 의미가 같은 것으로 추측하지 않으므로 **새 게이지가 예전 총합과 달라질 수 있다.** 이는 저장 파일 삭제가 아니다.
- Ren'Py의 불러오기는 직전 체크포인트로 돌아가 마지막 선택을 재실행할 수 있다. 불러올 슬롯의 안전한 JSON 요약을 별도로 보관해 `saved_slot_summary`, `checkpoint_*`, `resumed_choice_log`를 구분한다. 새 게이지에 원래 요약을 더하지 않는다. v2 저장에는 이 구버전 복원을 다시 적용하지 않는다.
- 원래 서명 검증/확인 과정을 그대로 호출하는 제품 내부 연결만 사용한다. 서명 확인이 끝나기 전에는 메타를 소비하지 않고 취소·실패 때 임시 상태를 지운다. SDK 파일 수정이나 자체 세이브 역직렬화는 사용하지 않는다.
- 불러온 구 저장을 다시 저장할 때도 아카이브가 유지되도록 공식 `retain_after_load()`로 일회성 변환을 보존한다. 일반 선택 롤백을 전역 차단하지 않으며 재실행된 선택 ID의 점수·기억 로그를 중복 적용하지 않는다.

완전한 이전 선택 기록이 없는 저장은 새 기준의 과거 점수를 정확하게 복원할 수 없다. 원본 수치와 확인 가능한 선택 결과를 별도로 보관·안내하는 한계가 있다. 기존 진행·완료 엔딩·갤러리·메모 기록을 초기화하지 않는다.

### 로만 판정의 명시적 기준

`bad`는 실제 누적 배드 호감도, 위험 횟수는 정책상 배드가 붙은 서로 다른 선택 ID의 수이며 에피소드 수는 서로 다른 로만 R장 수다.

| 최종 행동 | 배드 조건 |
| --- | --- |
| 경계 존중 `respect` | 배드≥40, 위험 선택≥5, 서로 다른 R장≥3 |
| 대화로 조율 `negotiate` | 배드≥40·위험≥4·R장≥2, 또는 배드≥30·위험≥4·R장≥2·해피<40 |
| 과도한 의존 수용 `surrender` | 배드≥30·위험≥3·R장≥2, 또는 배드≥20·위험≥3·R장≥2·해피<25 |

그 밖은 해피다. 마지막 선택을 기록하지 않은 구 저장은 오류 없이 해피 쪽으로 연결한다. 원고의 실제 `respect` 경로는 최대 배드45라서 50점 기준은 도달 불가능함을 검토 중 발견해 40점으로 조정했다. 실제 40점·5선택·4에피소드 경로가 존재한다. 한두 위험 선택만으로 배드가 되지 않으며 충분히 반복된 위험은 마지막 긍정 답변 한 번으로 사라지지 않는다.

## D. 대본 적용 현황

| 범위 | 적용 |
| --- | --- |
| CH01~CH07 | 기존 선택 전체를 정책에 연결, 대사·개인 이벤트·CH07 직접 선택 보존 |
| 로만 R01~R06 | 기존 선택을 정책에 연결, 엔딩 내용 보존·판정만 변경 |
| 로만 시크릿 | 해피 완료 이후 별도 해금, 배드 필요 조건 없음 |
| 시아 S01 | 확정 원고 8씬·663대사/서술·3갈래 피드백, 해피5/10·배드0 |
| 시아 S02 | 확정 원고 8씬·892대사/서술·6갈래, 인형 이름0·감정 표현해피5/10·배드0 |

시아의 리듬 게임 패배, 인형 뽑기/작명, 포토부스, 식사, 오므 조우, 가벼운 질투, 산책과 약속을 유지했다. S03~S06·시아 엔딩은 만들지 않았다. 원고 파일명 R01/R02와 본문 S01/S02의 차이는 본문 기준으로 처리했다. HTML/WritingBlock·편집 설명은 실제 대사가 아니며 SOURCE/CONTI와 원고 감사에 남긴다. `SIA_STORY_IMPORT.md`, `SIA_IMPORT_AUDIT.json`, `SIA_IMPORT_STATIC_RESULT.json`에 근거가 있다.

사용자가 마지막으로 제공한 시아 시크릿 CG는 원본 PNG(2048×1152, 2,829,983바이트)를 변형 없이 추가했다. SHA256은 `da09ff6d8ea001bbbf9509e377f1da86560e88c8939b35f798de12e1c1d95f03`다. SIA/ENDING 탭에 같은 한 작품으로 등록하되 정식 시크릿 대본이 없어 잠겨 있다. 실제 시작·해금 요청은 거절되고 기존 컬렉션은 바뀌지 않음을 실행 검증했다. 이 그림 추가가 시아 엔딩의 구현 완료를 의미하지 않는다.

NOTE01/02는 개인 장면으로 열리고 점수 임계값을 억지로 추가하지 않았다. 새 NOTE03은 해피 엔딩 후 열린다. 업데이트 전 이미 열람할 수 있었던 NOTE03은 legacy 열람권을 합집합으로 보존한다. 엔딩과 메모 본문은 유지한다.

## E. 검증

기존 구현된 19개 route의 대사·선택문 11,387개가 수정 전과 순서까지 같다. 원래 미구현 안내였던 `sia.rpy`만 새 원고로 연결했으므로 이 비교에서 제외한다. 시아 신규 1,555개 대사와 9개 선택지는 원고와 별도로 대조했다. 모든 실보상은5/10이며 신뢰도 조건·연산은 새 판정에서 제외했다. 구 저장이 참조하는 Python 명령 이름을 유지하기 위해 기존 호출의 호환 인수는 남겼지만 신뢰도나 1·2 단위 보상을 계산하지 않는다. 실제 점수는 JSON의 5·10점 정책만 사용한다.

선택 의미와 시스템 안정성을 독립적으로 교차 검토했다. 실제 발견한 부분 기록 안내 누락·서명 확인 중 메타 조기 소비 문제를 수정했다. 설치된 아레나의 8명 동시 토너먼트 실행을 주장하지 않으며, 실제 수행한 두 관점의 코드 리뷰·경계 검사 결과만 `RELATIONSHIP_CHOICE_AUDIT.md`, `RELATIONSHIP_REVIEW_060.md`에 기록한다.

실제 Ren'Py 8.5.3에서 **22케이스·66개 SDK 검증·29개 확인 지점 전부 통과**했다. 7개 챕터 전환, CH07의 다섯 히로인 직접 선택·취소, 로만 최종 메뉴 여섯 경로와 판정 경계, 시아 S01→S02의 세 메뉴와 완료 후 저장을 검사했다. 시아 원고 전체 1,555대사와 209정책은 별도 정적 대조했다. 모든 경로의 조합을 처음부터 끝까지 전수 플레이한 것은 아니다.

실제 하트v1 저장의 불러오기→v2로 저장→다시 불러오기, 하트 도입 전 0.4.1 재현 저장, 일반 선택 롤백을 검사했다. 직전 **서명된 공개판 0.5.2에서 만든 CH01 선택 후 저장**을 새 버전에 불러와 **같은 문장 이름·같은 대사 위치**로 복귀하고 점수·기억 로그가 한 번만 적용됨을 확인했다. 변환 후 재저장·재불러오기까지 통과했다. 대사 이름 보존만으로 충분하지 않아 공통/로만 6파일의 **52개 옛 Python 호출 문장**도 정확히 유지했다. 그 인수는 계산에 쓰지 않는 호환용이며 실제 보상은 여전히 검토된 5·10점 정책뿐이다.

**Lint 종료0, 오류0·경고0·traceback0.** 최종 제품 471파일과 시험 복사본의 SHA가 전부 일치하고 실제 사용자 저장·persistent 14파일의 SHA와 수정 시간이 모두 그대로였다. 이전 QA 저장 2개도 바꾸지 않았다. UI 픽셀 6검사에서 게이지 폭·문구를 확인했고 알림 글자 중심 오차는 가상 해상도 최대1px였다. 실행은 D의 격리 복사본과 SDL dummy/software 표시로 진행했다. 사용자의 현재 화면을 조작하거나 실제 GPU 렌더링·전체 설치를 시험했다고 주장하지 않는다. 자세한 로그는 `tests/relationship_overhaul_060/native/README.md`, `RESULT.json`에 있다.

배포 코드도 보강했다. 직전 실제 공개 0.5.2의 서명된 RPYC58개를 해시 검증 후 보존하고 공식 SDK의 이름 병합을 사용한다. 실제 불변 대사11,305개의 문장 이름이 전부 유지됐으며, 이전의 RPYC 없는 방식은 같은11,305개가 전부 바뀌는 대조 결과를 확인했다. SDK를 바꾸지 않았다. `COMPILED_SAVE_COMPAT_060.md`에 원인·수정·검사·범위를 기록했다.


### 공개 업데이트 결과

**0.6.0-test / build2026110902**를 기존 URL `https://campus-romance-playtest.naiski.chatgpt.site/`에 활성화했다. 새 59조각·4,915,513바이트를 올리고 기존 1,787조각을 재사용했다. 전체 manifest는 1,848파일·582,317,032바이트이며 SHA256은 `26bde57a576160535ba64390a13ef92e5d071fca78c3bd5c4a85edf510c2bddf`다. 별도 전체 Windows ZIP은 만들지 않았다.

서명된 배포본과 최종 QA 복사본의 원본 471파일을 대조해 전부 일치했다. 게시 후 **production CLI(qa:false)**의 새 버전/파일 수 확인, 고정 RSA 서명·공지5개, 공개8파일의 실제 다운로드 SHA 대조도 통과했다. 두 정책 JSON의 209선택은 모두 실제0·5·10이고 시아 시크릿 원본 PNG와 등록 데이터도 공개본까지 동일했다. 기존 CH05 단체 사진 해시는 바뀌지 않았다. 이 확인은 실제 사용자의 전체 게임 설치를 수행한 것이 아니다.

Site·런처 EXE를 다시 만들 필요 없이 같은 채널의 새 버전과 공지를 읽는다. 플레이어는 게임을 닫고 기존 런처에서 **업데이트 확인 → 설치·업데이트 → 게임 시작**으로 받는다. 바탕화면의 기존 런처 바로가기를 그대로 사용한다. 새 버전 RPYC61개도 `launcher_publish/compiled_seeds/2026110902`에 보존해 다음 배포의 저장 이름 정보를 이어받는다.

근거: `launcher_publish/r2_upload_result.json`, `tests/relationship_overhaul_060/snapshot_qa_parity.json`, `tests/relationship_overhaul_060/public_verify/RESULT.json`, `public_verify/README.md`.

## F. 남은 작업

시아 S03~S06과 다른 히로인의 개별 루트 본대본·엔딩은 미구현이다. 시아의 게임센터/포토부스 등은 기존 배경으로 임시 표현하고 신규 LD/SD/스탠딩을 생성하지 않았다. 로만 후반의 미제작 스탠딩 지시는 콘티로 유지하며, 이미 연결된 심박 효과·조건과 제공된 일러스트는 유지한다. 후속 점수 정책을 바꿀 때에는 새 선택 ID와 저장 스키마 이전을 함께 검토해야 한다.
