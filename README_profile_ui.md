# 캐릭터 다이어리 UI 수정 가이드

<!-- typography-audit-status -->
스크린샷 후속 수정의 네이티브 검사 113개·464개 assertion과 Lint가 통과했습니다. 캡처 94개·텍스트 레이아웃 1,187개에서 영역 문제 0개, 실제 PNG 잉크 중심은 87/87항목 통과입니다. 근거·범위·배포 보류는 [UI_SCREENSHOT_FIXES.md](docs/UI_SCREENSHOT_FIXES.md)를 따르며 기존 0.3.0·0.2.0 보고서는 변경 전 시점의 기록으로 보존합니다.
<!-- /typography-audit-status -->

실제 프로젝트: `D:\CampusRomance_VN\renpy_project`

메인 메뉴의 **CC대 학생들**을 누르면 사진과 소개 메모가 있는 다이어리 보드가 열립니다. 기존 히로인 다섯 명의 설명·사진·비밀 메모·호감도·신뢰도 화면은 그대로 사용합니다. 인물 이름이나 이전/다음, 키보드 좌우 방향키로 다섯 명을 전환합니다. 돌아가기 또는 Esc로 닫습니다. 메모의 앞면은 기본 정보, 뒷면은 인물 관계와 한 줄 소개입니다.

제목 옆 **만난 사람들!**을 누르면 전용 프로필 그림과 짧은 소개를 두 명씩 크게 볼 수 있습니다. 첫 페이지는 **스키·협합**, 둘째 페이지는 **밤밤·헤스**입니다. 이전/다음 또는 좌우 방향키로 페이지를 전환합니다. 사용자가 제공한 네 장의 그림을 재인코딩 없이 사용하고, 세로 구도 전체가 사진 창 안에 보이도록 비율을 유지합니다. 옆에는 학과·학년·짧은 소개와 대본의 한마디를 배치합니다. 처음부터 네 명을 볼 수 있고 새로운 해금·호감도 시스템은 추가하지 않습니다. **우리의 페이지**로 돌아오면 앞에서 고른 히로인이 유지됩니다.

전용 사진과 두 명씩 보기 변경은 네이티브 검사 3개·43개 assertion, Lint, 버튼 5개의 PNG 글자 중심 검사와 패키지 EXE의 저장·불러오기 검사까지 통과했습니다. 수정 파일·화면·최종 실행판과 기존 저장 보존 근거는 [PEOPLE_PROFILE_PORTRAITS.md](docs/PEOPLE_PROFILE_PORTRAITS.md)에 정리했습니다. 앞선 네 명 한 화면 버전은 [STUDENTS_UI_UPDATE.md](docs/STUDENTS_UI_UPDATE.md)에 기록을 보존합니다.

본편에서 **학생증**을 열면 선택한 히로인의 호감도와 신뢰도(0–100)를 앞·뒷면 하단에서 확인할 수 있습니다. 수치는 현재 플레이의 저장 데이터에서 읽습니다. 하린은 표시 이름이며 프로필·세이브·이미지에 사용하는 ID는 계속 `lumi`입니다.

## 파일

- `game/screens_character_profile.rpy`: 화면·전환·hover·팝업
- `game/data/character_profiles.rpy`: 프로필 데이터 로드, 사진·스티커 클릭 처리
- `game/data/profile_pages.json`: 성격 메모와 사진·스티커 문구, 프로필 테마
- `game/data/secret_notes.json`: 공식 비밀 메모 25개와 후보 엔딩 표시
- `game/systems/secret_notes.rpy`: 영구 수집과 기존 진행 기록 복원
- `game/data/heroines.json`: 확정 프로필과 관계의 원본
- `game/screens_met_people.rpy`: 만난 사람들 네 인물의 사진 메모 화면
- `game/data/met_people.json`: 스키·협합·헤스·밤밤의 간단한 공개 소개
- `game/data/met_people.rpy`: 소개 데이터와 전용 사진·대체 스탠딩·페이지 처리
- `game/images/ui/profile/`: 종이·스티커·마스킹 테이프·사진 자리표시자
- `game/tests/profile_ui.rpy`: 다섯 인물 및 미리보기 격리 테스트. 배포 빌드에서는 제외

기본 정보는 노트 줄 y=364부터 48px 간격으로 정렬합니다. 좋아함·싫어함과 소개도 같은 줄 간격을 따르며 긴 내용은 단어 단위로 나누어 지정 영역에서 스크롤합니다. 앞면의 중복 인용문과 사진 바깥에 떠 있던 손메모는 제거했고, 기존 한마디는 뒷면에 남깁니다. 오른쪽 해금 안내는 어두운 정자체와 밝은 메모지를 사용합니다.

만난 사람들에 인물을 추가하려면 `met_people.json`의 `people`과 `order`에 같은 ID를 넣습니다. `name`, `department`, `year`, `intro`가 기본 필드이며 `quote`, `paper`, `portrait_image`, `portrait_crop`을 함께 지정할 수 있습니다. `portrait_image`는 `images/people/profile_ski.png`와 같은 게임 기준 경로입니다. 현재 전용 파일명은 `profile_ski.png`, `profile_hyeophap.png`, `profile_bambam.png`, `profile_hess.png`이고 모두 `game/images/people/`에 있습니다. 전용 그림이 없으면 기존 스탠딩을 사용하고, 그 이미지도 없으면 사진 준비 안내를 표시합니다. `portrait_crop`은 스탠딩을 대체 사진으로 쓸 때만 적용하는 왼쪽·위·너비·높이 비율입니다. 소개는 두 카드씩 페이지가 나뉩니다. 알려지지 않은 나이·MBTI 등은 임의로 추가하지 않습니다.

## 사진 교체

다음 파일을 넣으면 다음 실행부터 자동으로 사용합니다. PNG, 권장 822×1000 또는 1233×1500. 내부 1920×1080 캔버스의 사진 표시 영역은 411×500이며 중앙 기준으로 비율을 유지해 채웁니다. 중앙 인물이 잘리지 않도록 여백을 두세요. 목록 썸네일도 같은 사진을 사용합니다.

| 인물 | 우선 경로 | 기존 호환 경로 |
|---|---|---|
| 로만 | `game/images/heroines/profile_roman.png` | `game/images/heroines/roman/profile.png` |
| 시아 | `game/images/heroines/profile_sia.png` | `game/images/heroines/sia/profile.png` |
| 다림 | `game/images/heroines/profile_darim.png` | `game/images/heroines/darim/profile.png` |
| 오므 | `game/images/heroines/profile_omu.png` | `game/images/heroines/omu/profile.png` |
| 하린 | `game/images/heroines/profile_lumi.png` | `game/images/heroines/lumi/profile.png` |

우선 경로가 있으면 기존 호환 경로보다 먼저 사용합니다. 둘 다 없으면 `photo_placeholder.svg`로 실행됩니다. 실제 히로인 이미지는 생성하지 않았습니다.

## 클릭과 기록

스티커를 클릭하면 작은 메모를 볼 수 있습니다. 발견한 스티커는 `persistent.profile_discoveries`에 기록됩니다. 사진 모서리와 **일상 사진**은 사진 뒷면을, **뒷면 보기**는 인물 관계를 엽니다.

**비밀 메모** 탭이나 오른쪽의 세 슬롯을 눌러 수집 상태를 확인합니다. 잠긴 슬롯에는 안내 문구만 표시됩니다.

| 슬롯 | 수집 조건 |
| --- | --- |
| NOTE 01 · 첫인상 너머 | 해당 인물의 CH01·CH02·CH03 개인 이벤트 중 하나를 완료 |
| NOTE 02 · 그날의 진심 | 해당 인물의 CH04 핵심 개인 이벤트 완료 |
| NOTE 03 · 마지막에 남은 것 | 해당 인물의 실제 HAPPY·BAD·SECRET 엔딩 완료. 각 종류를 별도로 열람 |

NOTE 01·02는 기존 영구 수집 집합인 `persistent.profile_secrets`에 `roman.note01`과 같은 키로 저장합니다. NOTE 03은 엔딩 목록과 같은 `persistent.endings` 기록을 읽습니다. 이전 슬롯을 불러오거나 새 게임을 시작해도 수집한 메모를 읽을 수 있습니다. 구버전에서 개인 이벤트를 마친 증거가 있으면 자동으로 복원합니다. 이전 발견 기록과 호감도 기준의 옛 키는 보존합니다. 공식 메모에는 이벤트 완료 조건을 적용합니다. 화면에는 하린으로 표시하고 기존 내부 ID `lumi`를 사용합니다.

처음 수집할 때만 알림을 띄웁니다. **환경설정 → 기타 → 비밀 메모 알림**에서 끌 수 있습니다. 개발실의 사진·스티커 미리보기는 별도로 동작합니다.

## 메모와 비밀 추가

`secret_notes.json`에서 공식 제목과 본문을 수정합니다. 각 인물의 `note03` 아래에 엔딩 종류별 제목과 본문이 있습니다. 다림 SECRET, 오므 BAD·SECRET, 하린 SECRET은 `pending` 후보입니다. 이 네 항목은 스토리 확정 후 후보 표시를 해제합니다. 다른 엔딩도 실제 구현을 등록한 뒤 루트 종료에서 `unlock_ending(ending_id)`를 호출하면 해당 기록이 열립니다.

추후 개인 이벤트에서 보충 수집을 제공하려면 완료 지점에서 `secret_note_unlock(hero, 1)` 또는 `secret_note_unlock(hero, 2)`를 호출합니다. 장식·사진·스티커 문구는 `profile_pages.json`에서 수정합니다. 기존 프로필 데이터에는 이전 시안도 보존되어 있습니다.


## 새 캐릭터 추가

`heroines.json`에 기본 정보, `profile_pages.json`에 기존 인물과 동일한 필드, `systems/state.rpy`의 `HEROINE_ORDER`에 영문 ID를 추가합니다. `diary_sticker`의 매핑과 대체 SVG도 추가하고 사진은 위 규칙을 따릅니다. 왼쪽 목록은 현재 다섯 명 높이에 맞춰져 있으므로 더 많아지면 스크롤 또는 높이 조정이 필요합니다. 공략 가능한 인물로 확장하려면 별도로 루트 파일과 엔딩 데이터를 추가해야 합니다.

## 시각 요소

이름·주요 제목은 `CAMPUS_TITLE_FONT`(Noto Serif KR), 본문과 조작은 `CAMPUS_BODY_FONT`(Noto Sans KR), 작은 장식 손메모만 `CAMPUS_NOTE_FONT`(개구 Regular)를 사용합니다. 세 상수는 `game/typography.rpy`의 init -200에 있고, 공통 스타일은 같은 파일의 init 999에서 적용합니다. 폰트 TTF와 해당 OFL 고지는 `game/fonts/`에 함께 보관합니다. 사용하지 않는 이전 폰트도 호환·선택 용도로 남겨 둡니다. 최신 색상·패널 스타일은 `theme_spring.rpy`의 `init 999`에서 적용됩니다. `profile_pages.json`의 `paper`는 오른쪽 노트의 연한 색을 바꿉니다. 이전 `accent`/`photo_angle` 필드는 현재 화면에서 사용하지 않습니다. 현재 사진 기울기는 로만·시아·다림·오므 −3°, 하린 0°입니다.

최신 스티커는 `images/ui/spring/stickers_atlas.png`입니다. 투명 PNG를 3열×2행으로 나누어 좌상단부터 로만/시아/다림/오므/하린/공통 순서로 읽습니다. 현재 원본은 1536×1024, 각 칸은 512×512입니다. 파일이 없으면 `images/ui/profile/sticker_<id>.svg`로 대체됩니다. 스티커 그림 교체 시 각 칸 바깥은 투명하게 두고, 셀 안쪽에 여백을 유지하세요. 확대 hover와 클릭은 그림 파일과 분리되어 있습니다.

`tools/create_profile_ui.py`와 `refine_profile_assets.py`는 초기 자산 제작 스크립트이며 재실행하면 기본 데이터를 다시 씁니다. 커스텀 수정 후에는 먼저 `backups/`에 백업하고, 필요한 출력 부분만 수정해서 사용하세요.

Figma 편집 파일: https://www.figma.com/design/BIYnwRqDHe6PiUjbOtq4x0?node-id=7-80

위 링크는 이전 편집 가능한 다이어리 시안입니다. 최종 봄빛 전체 화면은 Figma Starter 도구 호출 한도로 동기화가 끝나지 않았습니다. 현재 런타임은 Ren’Py 소스와 `images/ui/spring/stickers_atlas.png`를 사용합니다. 이전 Figma 동기화 상태는 `design_docs/FIGMA.md`, 0.3.0 화면의 실제 실행 결과는 [VERIFICATION_0.3.0.md](tests/VERIFICATION_0.3.0.md)를 기준으로 확인하세요.
