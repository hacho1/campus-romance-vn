---
name: "우리 사이, 그 이상"
description: "청량한 캠퍼스 그림, 읽기 쉬운 메시지, 절제된 종이 메모를 위한 Ren’Py UI."
platform: "Windows / Ren’Py"
canvas: "1920x1080 virtual pixels"
colors:
  main-ink: "#3c596b"
  main-logo: "#4c657d"
  main-paper: "#fffefb"
  main-hover: "#e6f2f6"
  main-accent: "#287388"
  phone-ink: "#293f49"
  phone-muted: "#586e77"
  gallery-ink: "#394b63"
  gallery-muted: "#586c7c"
  gallery-paper: "#f2f6f8"
  gallery-selected: "#dcecf3"
  spring-ink: "#414579"
  spring-muted: "#65698d"
  spring-paper: "#fffafd"
  spring-cream: "#fffaf2"
  spring-pink-hover: "#ffe0f0"
  spring-pink-selected: "#f8d8ec"
  spring-border: "#c8c5e8"
  roman-paper: "#fffdf2"
  sia-paper: "#fff6fb"
  darim-paper: "#f8fbf4"
  omu-paper: "#f3f9fb"
  lumi-paper: "#f7f8ff"
typography:
  main-logo: "Noto Serif KR / 70px"
  main-menu: "Noto Sans KR / 29px"
  body: "Noto Sans KR / 30px"
  dialogue: "Noto Sans KR / 34px"
  phone-message: "Noto Sans KR / 25px"
  phone-name: "Noto Sans KR / 21px"
  gallery-tab: "Noto Sans KR / 23px"
  gallery-title: "Noto Serif KR / 54px"
  profile-name: "Noto Serif KR / 54px"
components:
  main-menu-panel: "860x225 at 530,815 / 2 columns x 3 rows"
  phone-shell: "660x1018 at 630,28"
  phone-display: "614x918 inside shell"
  gallery-tile: "480x330 / 3 columns x 2 rows"
  dialogue: "1800x235 at 60,814"
  profile-binder: "1140x780 at 375,200"
---

# 《우리 사이, 그 이상》 UI 설계 기준

<!-- typography-audit-status -->
스크린샷 후속 수정의 네이티브 검사 113개·464개 assertion과 Lint가 통과했습니다. 캡처 94개·텍스트 레이아웃 1,187개에서 영역 문제 0개, 실제 PNG 잉크 중심은 87/87항목 통과입니다. 근거·범위·배포 보류는 [UI_SCREENSHOT_FIXES.md](docs/UI_SCREENSHOT_FIXES.md)를 따르며 기존 0.3.0·0.2.0 보고서는 변경 전 시점의 기록으로 보존합니다.
<!-- /typography-audit-status -->

## 방향과 적용 범위

청량한 현대 캠퍼스 로맨스의 그림을 넓게 감상하고, 한국어 대사와 메시지를 편하게 읽는 화면입니다. 이번 0.3.0 개편에서는 메인·갤러리·휴대폰의 장식을 줄이고 사진·종이·스티커는 히로인 설명에 집중합니다. 최신 사용자 요청의 상단 로고·하단 메뉴·스마트폰·8탭 갤러리 구조를 현재 기준으로 사용합니다.

최종 캐릭터·메인·LD·SD·CG 그림은 새로 생성하지 않았습니다. 메인 꽃밭의 다섯 히로인 구도는 앞으로 넣을 그림의 제작 명세이며 현재는 기존 캠퍼스 배경으로 대체합니다. 주인공의 얼굴·성별·몸·손·실루엣을 확정하지 않습니다.

이 문서는 설계와 소스 구조를 설명합니다. 소스 UI와 SDK 네이티브 검증은 완료했으며 배포판은 사용자 요청으로 보류합니다. 실제 실행·창 크기·저장 범위와 공식 챕터 QA 종료 한계·독립 EXE 클릭 미검증은 [VERIFICATION_0.3.0.md](tests/VERIFICATION_0.3.0.md)에 기록합니다. 이전 [0.2.0 보고서](tests/VERIFICATION_0.2.0.md)는 SD 전체 컷 전환 시점의 검증으로 보존합니다.

## 화면별 중심

| 화면 | 먼저 보일 것 | 주변 UI의 역할 |
| --- | --- | --- |
| 메인 | 넓은 대표 그림과 상단의 타이틀 | 여섯 주요 메뉴를 하단에 모아 그림의 중앙을 비움 |
| 일반 대화·LD | 인물 표정·큰 장면과 기존 대사 | 익숙한 이름표·대사창·기록·저장으로 읽기 유지 |
| SD | 과장된 표정·손짓이 담긴 완성 컷 한 장 | 개별 SD 캐릭터 배치 없이 컷을 교체하고 네이티브 대사 유지 |
| 휴대폰 | 중앙 스마트폰과 좌우 말풍선 | 방·시간·프사·답장을 친숙한 정보 밀도로 배치 |
| 갤러리 | 수집한 LD 썸네일과 큰 그림 | 탭·제목·장면 이동을 가장자리로 둠 |
| 히로인 설명 | 사진과 메모의 캐릭터성 | 스티커·접힌 쪽지에 작은 상호작용을 모음 |

## 색과 글꼴

아이보리·화이트·옅은 하늘색을 기본으로 사용합니다. 메인은 청회색 잉크와 작은 하늘색 hover, 휴대폰은 짙은 청록 계열 글자와 연한 중성 바탕, 갤러리는 낮은 채도의 청회색으로 읽기 위계를 만듭니다. 기존 대사창과 스크랩북의 연보라 잉크·연핑크 선택 색은 유지합니다. 화면마다 같은 장식과 카드 모양을 반복하지 않습니다.

글꼴은 `game/typography.rpy`에서 역할별로 관리합니다. `CAMPUS_BODY_FONT`는 `fonts/NotoSansKR.ttf`로 대사·메시지·조작·프로필 정보를 읽고, `CAMPUS_TITLE_FONT`는 `fonts/NotoSerifKR.ttf`로 로고·이름·주요 제목을 표시합니다. `CAMPUS_NOTE_FONT`의 `fonts/Gaegu-Regular.ttf`는 작은 장식 손메모에만 사용합니다. 상수는 init -200에서, 공통 상속 스타일과 손메모 Bold 대체는 init 999에서 적용합니다. 사용하지 않는 이전 폰트 파일은 호환·선택 용도로 보존합니다. 가상 캔버스의 글자 크기는 물리 창에서 Ren’Py가 함께 축소합니다. 한글 줄바꿈은 기본 `korean-with-spaces` 스타일을 유지하며 긴 싫어하는 것·답장·소개 문장은 실제 창에서 확인해야 합니다.

선택된 밝은 버튼에서도 어두운 글자를 유지합니다. 흰 바탕의 작은 흰 글자, 본문 뒤의 복잡한 꽃 장식, 필요 없는 발광·두꺼운 테두리를 기본 상태로 만들지 않습니다.

폰트 파일과 해당 OFL 고지는 `game/fonts/`에 함께 보관합니다. 현재 읽기·제목 폰트는 [Noto Sans KR](https://github.com/google/fonts/tree/main/ofl/notosanskr)·[Noto Serif KR](https://github.com/google/fonts/tree/main/ofl/notoserifkr)이고, 작은 손메모의 [개구](https://github.com/google/fonts/tree/main/ofl/gaegu)도 라이선스 고지를 유지합니다.

대사와 답장은 말줄임으로 없애지 않습니다. 긴 답장·비밀 메모는 정해진 영역에서 스크롤하며, 방 제목·저장명 같은 압축 메타데이터에만 말줄임을 사용하고 전체 내용은 툴팁·접근성 이름에 유지합니다. 갤러리의 긴 제목·장면 정보도 이동 버튼과 분리된 영역에서 읽습니다.

## 메인 타이틀

`game/screens_campus_main.rpy`가 화면을 정의합니다. 로고는 (960,60)을 중심으로 한 줄의 명조 70px이며 작은 기존 부제를 붙입니다. 메뉴는 (530,815)의 860×225 반투명 패널에 2열×3행으로 둡니다.

| 왼쪽 | 오른쪽 |
| --- | --- |
| 게임 시작 | 불러오기 |
| 갤러리 | 히로인 설명 |
| 엔딩 | 옵션 |

메뉴는 밝은 얇은 면과 약한 경계·그림자만 사용합니다. hover는 옅은 하늘색과 잉크 색 변화이며 확대·이동을 사용하지 않습니다. 이어하기·종료는 상단의 작은 보조 동작이고 개발실은 개발 모드에서만 표시합니다.

메인 그림은 `cg_asset("ld_01")`와 연결합니다. 다섯 히로인이 꽃밭에 둥글게 누워 하늘을 바라보며 주인공은 등장하지 않습니다. 얼굴·중요 손짓은 상단 로고(y=60~190)와 하단 패널(x=530~1390, y=815~1040)을 피해 중앙에 두어야 합니다. 파일이 없으면 기존 캠퍼스 배경과 작은 준비 문구를 사용하고, 실제 그림을 넣으면 문구가 사라집니다. 그림 아래의 밝은 기본 면은 투명 PNG에도 유지합니다.

## 휴대폰

`game/screens_phone.rpy`가 (630,28)의 660×1018 스마트폰 프레임을 표시합니다. 내부는 614×918이며 상단 시각·통신 상태, 헤더, 스크롤 메시지, 하단 진행·답장 영역을 구분합니다. 흰색·연회색과 둥근 말풍선을 사용하되 특정 메신저의 로고·상표를 복제하지 않습니다.

- 잠금화면: 큰 시간·날짜·배경과 알림 미리보기. 알림 열기는 목록으로 이동합니다.
- 목록: 원형 프사·방 이름·마지막 메시지·시각·미읽음 배지. 방을 열면 해당 방을 읽음으로 바꿉니다.
- 대화방: 수신은 왼쪽, 플레이어는 오른쪽. 단체방은 발신자 이름·프사를 함께 표시합니다. 날짜가 달라지면 날짜 구분을 표시합니다.
- 답장: 기존 네이티브 선택지를 말풍선 아래의 후보 2~3개처럼 배치합니다. 본편의 고정 답장에 새로운 선택을 만들지 않습니다.

진행 중인 방에서만 다음 대사가 넘어가고, 다른 방이나 잠금화면을 읽을 때는 본편 진행을 보류합니다. 대화 열람은 현재 세이브의 이력이며 영구 갤러리와 합치지 않습니다. 프사·배경·시간·저장 API는 [PHONE_UI_GUIDE.md](docs/PHONE_UI_GUIDE.md)에 있습니다.

## LD·SD와 갤러리

일반 스탠딩은 기본 대화의 표정 교체, LD는 진지한 감정·관계·여운, SD는 과장된 반응과 단체 개그에 사용합니다. LD와 SD는 각각 완성 그림 한 장을 표시하며 인물별 그림으로 분해·합성하지 않습니다. 대사·화자 이름·선택지는 이미지에 넣지 않습니다. 일반 장면의 중요 얼굴·손짓은 y≤740에 두어 이름표(y=771)와 대사창(y=814)을 피합니다.

갤러리는 `screens_campus_gallery.rpy`의 COMMON / ROMAN / SIA / DARIM / OMU / HARIN / SPECIAL / ENDING 상단 탭을 사용합니다. 썸네일은 480×330, 한 페이지 3열×2행입니다. LD 12종은 메인·공통 장면·CH03 개인 장면을 등록하고, SPECIAL에는 실제 본 SD 33변형과 기존에 수집한 첫 회의 메모를 둡니다. HARIN는 표시 이름이며 내부 ID `lumi`를 유지합니다.

잠긴 항목은 실제 이미지 파일도 로드하지 않고 자물쇠·미수집 상태로 표시합니다. 해금 후 그림이 있으면 선명하게, 그림이 없으면 제목을 가진 준비 화면으로 표시합니다. 큰 보기는 1920×1080 영역에 `fit="contain"`으로 표시하고, 아래 정보 줄·이전/다음·닫기를 제공합니다. H로 안내를 숨길 수 있습니다. 현재 탭의 획득 항목만 이동하며 엔딩·회상은 실제 구현 상태를 넘어서 공개하지 않습니다.

현재 LD 위치·복원할 무대는 일반 저장 상태입니다. `persistent.cg_seen`과 `persistent.cg_sd_seen`은 본 장면의 영구 수집이며, 기존 `persistent.gallery`·`persistent.endings`를 지우지 않습니다. 자세한 제작·교체·획득 규칙은 [CG_GALLERY_GUIDE.md](docs/CG_GALLERY_GUIDE.md)와 [SD_EVENT_ASSET_GUIDE.md](docs/SD_EVENT_ASSET_GUIDE.md)에 있습니다.

## 히로인 스크랩북

기존 `screens_character_profile.rpy`의 왼쪽 다섯 명 목록, 열린 바인더, 폴라로이드, 오른쪽 세 장의 접힌 비밀 쪽지를 유지합니다. 새 메뉴 이름은 히로인 설명이며, 앞면은 이름·나이·학년·학과·MBTI·취향·소개를 실제 48px 노트 줄에 맞춥니다. 바깥의 떠 있던 손메모와 앞면의 중복 인용문은 제거하고, 뒷면에서 관계와 기존 한마디를 읽습니다.

사진·스티커·쪽지는 클릭 가능한 기존 영역을 유지합니다. 사진이 없어도 틀과 대체 문구가 남고, 캐릭터별 스티커는 실제 인물 외형을 대신 확정하지 않는 소품입니다. 앞뒷면·캐릭터 전환은 짧은 디졸브를 사용하고, 스티커 확대는 기존 작은 반응만 유지합니다.

| 비밀 메모 | 기존 조건 |
| --- | --- |
| 1 | 호감 2·신뢰 2 또는 해당 CH01 비밀 플래그 |
| 2 | 호감 6·신뢰 4 |
| 3 | 해당 개별 루트 진입 또는 해당 엔딩 기록 |

루트·엔딩 기록으로 이전 메모도 열리며 이미 발견한 기록은 계속 읽을 수 있습니다. 개발용 해금 미리보기는 실제 발견 기록을 만들지 않습니다. 이번 UI 개편은 엔딩·루트 완성을 추가하지 않습니다. 상세 이미지·데이터 수정은 [README_profile_ui.md](README_profile_ui.md)를 따릅니다.

## 버튼과 기록의 정렬

`images/ui/controls/button.png`, `button_hover.png`, `button_selected.png`는 보이는 배경과 레이아웃 사각형이 같은 중심을 갖는 실행 자산입니다. `spring_panel()`과 명시적 `campus_control`·`campus_control_text` 스타일이 idle·hover·selected·selected-hover·비활성 상태를 모두 지정합니다. SVG를 아홉 조각으로 확대할 때 생긴 경계 이음새를 피하려고 실행에는 PNG를 사용하며, 편집용 SVG와 재생성기 `tools/build_control_surfaces.py`는 함께 유지합니다. `zz_ui_readability.rpy`는 한 줄 조작 글자의 줄 간격을 0으로 두고 양축 가운데 정렬, 어두운 hover·selected 색, 실제 잉크 중심 보정(`xoffset 2`, `yoffset -2`)을 적용합니다. 본문 단락의 명시적 줄 간격과 스크롤은 유지합니다. 실제 PNG 잉크 중심 87항목은 통과했으며, 최종 범위는 후속 검증 기록을 기준으로 확인합니다. 페이지 제목은 명조 `yoffset -4`를 별도로 적용합니다.

갤러리는 명조 앨범 제목과 폴라로이드 테두리·작은 테이프를 사용합니다. `screens_ending_diary.rpy`는 별도 줄노트의 이름·자물쇠를 y=420·510·600·690·780, 안내문을 y=900 줄에 맞춥니다. `images/ui/diary_polish/`는 이 종이·테두리 도형만 포함하며 새 인물 그림이 아닙니다.

## 소스와 그림 교체 경계

새 메인·폰·갤러리 화면은 init offset 900에서 앞선 화면을 대체합니다. `theme_spring.rpy`의 init999 스타일은 기존 대사·공통 메뉴·종이 자산의 바탕이고, 새 화면의 명시적 색·스타일이 해당 영역에 적용됩니다. HTML/CSS나 Figma가 런타임에 렌더링되는 구조는 아닙니다.

| 영역 | 우선 확인할 소스 |
| --- | --- |
| 메인 | `screens_campus_main.rpy`, `images/ui/campus_main/` |
| 휴대폰 | `screens_phone.rpy`, `systems/phone_system.rpy`, `data/phone_ui.json` |
| 갤러리·LD | `screens_campus_gallery.rpy`, `systems/cg_system.rpy`, `data/cg_registry.json` |
| 히로인 | `screens_character_profile.rpy`, `data/profile_pages.json`, `data/heroines.json` |
| SD | `systems/sd_event_system.rpy`, `data/sd_events.json` |

이전 콜라주·스티커 시안은 스크랩북 재질의 참고 자료입니다. 이전 Figma 파일·부분 동기화 스크립트·`.impeccable` HTML/CSS 미리보기는 현재 새 UI 화면을 완전히 반영했다고 표시하지 않습니다. 실제 코드와 새 버전의 실행 화면·검증 기록을 기준으로 수정합니다.

## 유지할 기준

그림의 중요한 표정과 읽을 문장이 서로 가리지 않아야 합니다. 버튼 hover는 배치가 움직이지 않게 하고, 잠금 상태는 색에만 의존하지 않고 문구·아이콘을 함께 사용합니다. 누락 이미지는 해당 장면의 준비 화면으로 대체하고 다른 인물·다른 컷을 대신 보여 주지 않습니다. 한국어 긴 문장과 다섯 프로필, 폰 메시지·답장, 갤러리 탭·뷰어는 최종 실제 창에서 확인한 범위만 완료로 보고합니다.
