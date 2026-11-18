# 우리 사이, 그 이상 · 캠퍼스 UI 개편

2026-11-04 이미지 추가: 다섯 히로인이 같은 흰색 프릴 드레스를 입고 햇빛 아래 잔디밭에 나란히 누운 타이틀 1장과 본편 배경 11종을 제작·연결했습니다. 원본·사용 프롬프트·전체 미리보기는 [타이틀·배경 제작 기록](artwork/title_backgrounds_20261104/README.md)에 있습니다.

2026-11-04 SD 이미지 삽입: 준비된 SD 이벤트 12종·33컷을 게임에 연결했습니다. 각 대사·선택 분기에 맞춰 한 장씩 표시하며, 게임용은 1920×1080 무손실 WebP입니다. SD 선택지는 하단에 모아 표정과 손짓을 가리지 않도록 했습니다. 원화와 AI4x 확대본은 보존했고 [SD 삽입 기록](artwork/sd_integration_20261104/README.md)에 경로·대본 타이밍과 2026-11-05 실행 검증을 정리했습니다.

2026-11-05 BGM 삽입: 자료의 음악·정지 지시 55곳을 대조해 장면용 13곡을 제작·연결했습니다. 게임용 OGG의 음량과 반복 구간을 정리하고, CH03의 빠진 협력·엔딩 음악과 일상→무음→감정 음악 전환을 반영했습니다. 기존 메인곡과 최신 캐릭터·휴대폰 연출을 보존했습니다. [BGM 제작·삽입 기록](artwork/bgm_integration_20261105/README.md)에 곡별 미리듣기·실제 프롬프트·공식 출처·검증 근거가 있습니다.

<!-- typography-audit-status -->
스크린샷 후속 수정의 네이티브 검사 113개·464개 assertion과 Lint가 통과했습니다. 캡처 94개·텍스트 레이아웃 1,187개에서 영역 문제 0개, 실제 PNG 잉크 중심은 87/87항목 통과입니다. 근거·범위·배포 보류는 [UI_SCREENSHOT_FIXES.md](docs/UI_SCREENSHOT_FIXES.md)를 따르며 기존 0.3.0·0.2.0 보고서는 변경 전 시점의 기록으로 보존합니다.
<!-- /typography-audit-status -->

실제 Ren’Py 프로젝트는 `D:\CampusRomance_VN\renpy_project`입니다. 메인·휴대폰·갤러리·히로인 설명의 0.3.0 소스 UI를 구현했습니다. **SDK 네이티브 110개 사례·811개 assertion과 Lint 검증을 마쳤으며, 배포판은 사용자 요청으로 보류합니다.** 공식 챕터 테스트의 종료 단계 멈춤과 독립 EXE 클릭 미검증 범위는 [VERIFICATION_0.3.0.md](tests/VERIFICATION_0.3.0.md)에 명시합니다.

## 실행

[START_GAME.cmd](START_GAME.cmd)는 D드라이브의 현재 소스를 실행하며 개발 메뉴를 숨깁니다. [START_DEVELOPER.cmd](START_DEVELOPER.cmd)는 챕터·개인 이벤트·SD와 휴대폰 점검에 사용하는 개발 실행입니다. 기본 논리 창은 1280×720, 내부 캔버스는 1920×1080입니다.

이전 검증된 0.2.0은 [Windows EXE](builds/Windows/CampusRomance-0.2.0-win/CampusRomance.exe), [ZIP](builds/CampusRomance-0.2.0-win.zip), [88개 사례·538개 assertion 보고서](tests/VERIFICATION_0.2.0.md)를 보존합니다. 이 기록은 SD 전체 컷 전환 시점의 결과입니다.

저장·불러오기와 기존 플레이 기록을 유지합니다. 별도 폴더에 푼 배포본은 그 실행 환경의 저장 위치를 사용하므로 이전 저장은 원본을 보관한 채 옮겨 사용하세요. 검증용 저장과 실제 플레이 저장의 처리 범위는 해당 버전 검증 보고서를 기준으로 확인합니다.

## 새 UI

- **메인:** 상단 중앙의 작은 로고, 그림이 넓게 보이는 중앙, 하단 중앙의 2열×3행 메뉴입니다. 게임 시작·불러오기·갤러리·히로인 설명·엔딩·옵션을 제공합니다. 이어하기·종료는 작은 보조 항목입니다.
- **대표 그림:** 로만·시아·오므·다림·하린이 같은 흰색 프릴 드레스를 입고 햇빛 아래 잔디밭에 나란히 누운 LD-01을 사용합니다. 주인공은 등장하지 않습니다. 타이틀과 COMMON 갤러리에 연결되어 있습니다.
- **휴대폰:** 첫 알림은 직접 열고, 잠금화면에서 해당 대화방으로 바로 이동합니다. 같은 장면의 단체방과 개인방은 휴대폰이 열린 채 이어집니다. 원형 프사·시간·안 읽은 메시지 수·좌우 말풍선과 원래 네이티브 선택지의 답장 UI를 사용합니다. 본편의 고정 메시지에 새 선택지를 만들지 않습니다.
- **히로인 설명:** 사진·나이·학과·MBTI·취향·소개를 실제 노트 줄에 맞춘 스크랩북입니다. 앞면의 중복 인용문과 바깥 손메모는 제거하고 기존 한마디는 뒷면에 남깁니다. 다섯 명 전환과 사진·스티커·잠긴 세 비밀 메모를 유지합니다. 본편의 학생증에서는 현재 저장의 호감도와 신뢰도를 앞·뒷면 하단에 표시합니다.
- **갤러리:** COMMON / ROMAN / SIA / DARIM / OMU / HARIN / SPECIAL / ENDING. LD 12종을 등록하고, 획득한 항목의 큰 보기·이전/다음·제목·챕터·씬을 제공합니다. 미획득 그림은 실제 파일이 있어도 공개하지 않습니다.
- **SD와 LD:** SD 12이벤트·33변형은 코미디용 전체 컷, LD는 감정과 여운을 위한 별도 전체 그림입니다. SPECIAL은 실제 본 SD 변형과 기존 첫 회의 메모를 보존합니다.

CH01 → CH02 → CH03, 본 장면 27개와 개인 이벤트 15종을 유지합니다. 한 플레이에서는 챕터마다 고른 한 명의 개인 이벤트를 진행합니다. 기존 호감·신뢰·선택 상대·협력·특별한 순간·저녁 대화·이름 입력·기록·자동 진행의 의미를 유지합니다.

0.3.0 UI 개편 당시 최종 인물·메인·LD·SD·CG 원화는 생성하지 않았으며, 이후 추가한 타이틀과 배경은 위 제작 기록을 따릅니다. CH04 이후·개별 루트·15개 엔딩과 시크릿 담당자는 미완성이며, 갤러리 슬롯이나 CH03 완료가 엔딩 해금을 뜻하지 않습니다. 회상 재생은 TODO입니다.

현재 본문·버튼·대사는 **Noto Sans KR**, 로고·이름·주요 제목은 **Noto Serif KR**, 작은 장식 손메모만 **개구 Regular**를 사용합니다. 경로는 `game/typography.rpy`에서 바꿉니다. 긴 대사와 답장 내용은 유지하고, 압축된 방 제목·저장명만 말줄임과 전체 내용 툴팁을 사용합니다. 긴 답장·메모는 영역 안에서 스크롤합니다.

첫 이름 입력 전 화자는 ‘나’이며, 예전 저장에 직접 정한 이름은 유지합니다. 참가 신청의 **신청하기**와 Enter는 같은 종이 접기 → 비행기 → 전송완료 → 페이드 흐름을 사용합니다. 선택으로 실제 호감·신뢰가 바뀌면 왼쪽에 실제 증감만 약 2.2초 표시합니다. 바탕화면 실행 바로가기는 D드라이브의 `START_GAME.cmd`를 가리킵니다. 이번 작업에서 배포판은 만들지 않습니다.

본편에서 **UI 숨기기**를 누르면 배경과 스탠딩만 남습니다. 화면을 클릭하거나 H 키를 누르면 같은 대사로 돌아옵니다. **옵션 → 텍스트**에서 속도 막대, 네 가지 빠른 설정, 미리보기를 사용할 수 있습니다.

## 수정 가이드

| 하려는 작업 | 문서 |
| --- | --- |
| 이번 UI 구조와 파일별 책임 | [UI_REFRESH_IMPLEMENTATION.md](docs/UI_REFRESH_IMPLEMENTATION.md) |
| 메인 비주얼·로고·메뉴·히로인 소개 | [UI_MAIN_HEROINES.md](docs/UI_MAIN_HEROINES.md) |
| 잠금화면·대화방·답장·폰 프사·날짜 | [PHONE_UI_GUIDE.md](docs/PHONE_UI_GUIDE.md) |
| LD 12종·8탭·획득·큰 보기·그림 경로 | [CG_GALLERY_GUIDE.md](docs/CG_GALLERY_GUIDE.md) |
| SD 33컷 제작·교체 | [SD_EVENT_ASSET_GUIDE.md](docs/SD_EVENT_ASSET_GUIDE.md) |
| 일반 스탠딩·표정·배경 | [IMAGE_ASSET_GUIDE.md](IMAGE_ASSET_GUIDE.md) |
| 사진과 세 단계 비밀 메모 | [README_profile_ui.md](README_profile_ui.md) |
| 원문 변환·분량·승인 전 편집안 | [CHAPTERS_IMPLEMENTATION.md](CHAPTERS_IMPLEMENTATION.md), [STORY_REVISION_SUGGESTIONS.md](STORY_REVISION_SUGGESTIONS.md) |
| 스크린샷 지적·글꼴·픽셀 정렬·신청 연출 | [UI_SCREENSHOT_FIXES.md](docs/UI_SCREENSHOT_FIXES.md) |
| 제품·색·폰트·배치 기준 | [PRODUCT.md](PRODUCT.md), [DESIGN.md](DESIGN.md) |

## 주요 파일

아래 `game/`은 `renpy_project/` 기준입니다.

| 파일 | 역할 |
| --- | --- |
| `game/typography.rpy` | Noto Sans 본문·Noto Serif 제목·작은 개구 손메모의 역할과 메타데이터 말줄임 |
| `game/screens_campus_main.rpy` | 상단 로고·하단 메뉴·대표 CG |
| `game/screens_phone.rpy` / `game/systems/phone_system.rpy` | 스마트폰 화면과 현재 세이브의 대화 |
| `game/data/phone_ui.json` | 연출용 날짜·시각·배경 설정 |
| `game/screens_character_profile.rpy` | 기존 히로인 스크랩북·상호작용 |
| `game/data/cg_registry.json` / `game/data/cg_registry.rpy` | LD 12종 등록 |
| `game/systems/cg_system.rpy` / `game/screens_campus_gallery.rpy` | LD 표시·복원·수집·갤러리 |
| `game/systems/sd_event_system.rpy` / `game/data/sd_events.json` | SD 완성 컷 12이벤트·33변형 |
| `game/routes/chapter01_official.rpy`~`chapter03_official.rpy` | 네이티브 공식 대사·분기와 연출 위치 |
| `design_docs/story_sources/` | 개발 프롬프트·공식 원문 사본 |

## 저장 위치와 검증

SDK·소스·백업·결과물은 D 프로젝트 안에 둡니다. 자동 검증과 빌드는 `tests/ui_refresh_fixture/renpy_project`의 분리된 복사본에서 수행합니다. `CAMPUS_SAVE_DIR`을 지정해도 Ren’Py는 실행 프로젝트의 `game/saves`에 저장을 함께 기록하므로 원본 프로젝트로 검증을 실행하지 않습니다. 이번 스크린샷 수정의 작업 전 기준은 실제 플레이 저장 33개(`game/saves` 19개·프로젝트 `saves` 14개)이며 [작업 전 스냅샷](tests/screenshot-review-player-saves-before.json)을 기준으로 대조합니다. 이전 0.3 작업 당시의 21개 [저장 보존 기록](tests/player-save-preservation-current.json)은 과거 기록으로 보존하며 현재 사용자 저장을 그 상태로 되돌리지 않습니다. C 작업 폴더의 참조 PNG 네 개도 `design_docs/source_attachments/` 아래 원래 상대 구조로 이동했으며 [크기·SHA-256·원본 제거 확인 기록](tests/c-drive-project-transfer.json)을 남겼습니다.

새 UI의 Lint·분기·저장·갤러리 잠금·스마트폰 이동/답장·창 크기 검사 결과와 실제 EXE 검증 여부는 [0.3.0 최종 보고서](tests/VERIFICATION_0.3.0.md)에 기록합니다. 이전 [0.2.0 검증](tests/VERIFICATION_0.2.0.md)은 그대로 보존합니다. SDK는 `tools/renpy-8.5.3-sdk`에 있고 검사·빌드 도구는 `tools/`에 있습니다. 공식 대본 변환기를 재실행할 때는 후속 LD·SD·BGM 연출 연결도 감사해야 합니다.

목표 플레이 시간은 CH01 45~60분, CH02 60~90분, CH03 70~100분입니다. 자동 넘김 시간과 사람이 읽는 시간은 구분하며 실제 플레이 시간은 별도 측정이 필요합니다.
