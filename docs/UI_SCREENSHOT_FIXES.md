# 스크린샷 지적 사항 수정 기록

프로젝트: `D:\CampusRomance_VN\renpy_project`  
참고: `design_docs/review_20261104/reference-01.png` ~ `reference-13.png`  
수정 전 백업: `backups/before-screenshot-ui-fixes-20261104-224619.zip`

<!-- screenshot-review-status -->
**최종 네이티브 검사 113개/464개 assertion과 Lint가 통과했습니다.** 스크린샷 조작 12개/37개, 신청·관계 알림 6개/51개, 메인·휴대폰·갤러리 21개/223개, 전체 텍스트 영역 74개/153개를 집계했습니다. 실제 렌더 캡처 94개·텍스트 레이아웃 1,187개에서 영역 문제 0개, 실제 PNG 잉크 중심 87/87항목 통과, 상태·대비 기록 176개 중 실패 0개입니다. [검증 요약 JSON](UI_SCREENSHOT_FIXES_SUMMARY.json)에 근거와 실행 환경을 구분했습니다. 실제 플레이어 저장 33개는 전후 파일 집합·SHA-256이 같고 복원·삭제하지 않았습니다. 배포판은 사용자 요청으로 계속 보류합니다.
<!-- /screenshot-review-status -->

## 글꼴과 실제 버튼 중심

읽는 글자와 장식을 구분했습니다.

| 역할 | 상수 | 파일 |
| --- | --- | --- |
| 대사·버튼·메시지·프로필 정보 | `CAMPUS_BODY_FONT` | `fonts/NotoSansKR.ttf` |
| 로고·주요 제목·프로필 이름 | `CAMPUS_TITLE_FONT` | `fonts/NotoSerifKR.ttf` |
| 작은 장식 손메모 | `CAMPUS_NOTE_FONT` | `fonts/Gaegu-Regular.ttf` |

경로는 `game/typography.rpy`의 init -200에서 바꿉니다. 공통 상속 스타일과 Bold 대체는 init 999입니다. 폰트와 해당 OFL 고지는 `game/fonts/`에 함께 있고, 이전 폰트 파일은 삭제하지 않았습니다. 개구 손글씨를 로고·본문·조작 제목에 사용하지 않습니다.

글꼴 렌더 상자를 가운데에 두는 것만으로 보이는 글자까지 가운데에 놓이지는 않았습니다. 이전 캡처에서 일부 조작의 보이는 잉크 중심은 배경 중심보다 오른쪽 약 4.8px·아래 약 8.4px에 있었습니다. 기존 PNG의 비대칭 투명 여백과 한 줄 글자에 상속된 줄 간격을 함께 수정했습니다.

`images/ui/controls/button.png`, `button_hover.png`, `button_selected.png`는 보이는 배경과 레이아웃 상자의 중심이 같은 실행 자산입니다. SVG를 아홉 조각으로 확대할 때 나타난 경계 이음새를 피하려고 실행에는 각 약 1KB의 PNG 세 장을 사용합니다. 편집용 SVG는 남겨 두고 `tools/build_control_surfaces.py`로 PNG를 재생성합니다. `spring_panel()`과 명시적인 `campus_control`·`campus_control_text` 스타일이 idle·hover·selected·selected-hover·비활성 상태의 배경과 글자를 모두 지정합니다. 설정·파일 페이지·돌아가기·프로필 탭에 같은 규칙을 적용했습니다. 퀵메뉴·장소 표시·페이지 제목의 기울어진 기존 종이 배경도 균형 잡힌 PNG로 교체했습니다. `zz_ui_readability.rpy`는 조작 글자를 양축 가운데에 놓고 줄 간격을 0으로 하며, 현재 소스의 실제 잉크 보정은 `xoffset 2`, `yoffset -2`입니다. hover·selected에서도 어두운 글자를 유지합니다. 본문 단락의 별도 줄 간격과 스크롤은 유지합니다. 페이지 제목의 명조 글자는 별도로 `yoffset -4`를 사용합니다. [실제 PNG 잉크 측정](../tests/screenshot-polish-ink-results.json)은 87항목 모두 허용 오차 안에 들었고, 폰트 메트릭을 잉크 중심의 증거로 대신 사용하지 않았습니다.

## 화면별 변경

| 화면 | 수정 내용 |
| --- | --- |
| 메인 | 정돈된 명조 로고, 중립적인 본문·메뉴, 기존 대표 그림과 하단 여섯 메뉴 유지 |
| 설정·저장·불러오기 | 버튼의 실제 배경과 글자 중심 정렬, 읽기 쉬운 활성 색. 저장 슬롯의 그림·시간·이름 높이를 분리하고 긴 이름은 전체 툴팁·접근성 이름 보존 |
| 히로인 설명 | 상단 세 탭·학과 배지·앞뒷면 버튼 양축 정렬. 이름을 명조로 표시하고 실제 노트 줄에 기본 정보와 소개 배치 |
| 프로필 문구 | 사진 바깥에 떠 있던 손메모와 앞면의 중복 인용문 제거. 기존 한마디는 뒷면에 유지. 해금 안내는 밝은 메모지 위의 어두운 정자체로 표시 |
| 갤러리 | 명조 앨범 제목, 종이 바탕·폴라로이드 테두리·절제된 테이프와 기존 스티커. 8탭·수집·잠금·큰 보기·이전/다음 유지 |
| 엔딩 | 새 줄노트에 이름·자물쇠·안내문 정렬. 15개 엔딩의 미구현 상태·실제 수집 기록 변경 없음 |
| 이름 신청 | 이름을 정하기 전 새 게임의 화자는 ‘나’. 사용자가 기존 저장에 정한 이름은 그대로 유지. 신청 버튼과 Enter가 같은 제출 연출 사용 |
| 선택 결과 | 왼쪽에 실제로 적용된 호감·신뢰 증감만 잠시 표시하며 약 2.2초 후 사라짐 |
| 클릭 소리 | 기존 0.05 수준 피크의 소리를 0.62 수준의 짧은 원본 절차 생성 종이 탭으로 교체. 개인 효과음 볼륨 설정 유지 |

프로필은 기존 노트 SVG의 y=364부터 48px 간격인 줄을 사용합니다. 기본 정보는 y=324·372·420·468의 40px 행, 취향은 y=516·564부터, 소개는 y=660 제목과 y=708 이후의 행에 맞춥니다. 긴 값은 단어 또는 긴 단어의 글자 경계에서 나누며 원문을 없애지 않고 지정 영역에서 스크롤합니다.

엔딩의 이름·자물쇠 행은 실제 종이 줄 y=420·510·600·690·780에서 끝나고, 안내문은 y=900 줄에 맞춥니다. 새 `images/ui/diary_polish/`는 종이·선·테두리 같은 도형만 포함합니다. 이번 스크린샷 수정에서 인물·SD 일러스트를 새로 만들지 않았습니다.

## 신청 연출과 관계 알림

`application_name_input`은 네이티브 이름 입력의 결과를 받아 `application_send_animation`을 한 번 호출합니다. **신청하기**와 Enter는 같은 입력 반환 경로를 사용합니다. 종이 → 접힌 종이 → 비행기 → 전송완료 → 페이드 순서이며, 효과 끄기 설정에서도 같은 결과와 진행을 유지합니다. 새 게임의 빈 입력은 ‘나’를 사용하고 예전 저장의 사용자 지정 이름을 임의로 바꾸지 않습니다.

관계 알림은 선택 효과를 적용하기 전후의 실제 차이를 표시합니다. 수치 제한에 걸려 적용되지 않은 증가분을 만들어 표시하지 않으며, 화면에서 관계 값을 다시 계산하거나 영구 수집 기록을 해금하지 않습니다. 알림은 플레이 시간 약 2.2초 뒤 사라지고 불러오기 경계에서도 정리합니다.

클릭음은 `audio/sfx/click.wav`입니다. [소리 측정](../tests/ui-click-sound-review.json)에 44.1kHz 모노·약 0.095초·피크 약 0.62와 개인 볼륨 설정 미변경을 기록했습니다. 실제 들리는 크기는 사용자의 효과음 볼륨을 따릅니다.

## 주요 수정 파일

아래 `game/`은 `D:\CampusRomance_VN\renpy_project` 기준입니다.

| 파일 | 책임 |
| --- | --- |
| `game/typography.rpy` | 글꼴 역할·가변 이름표 폭·압축 메타데이터 도우미 |
| `game/zz_ui_readability.rpy` | 조작 글자의 줄 간격·중심·활성 상태 색 |
| `game/theme_spring.rpy` | 균형 잡힌 버튼 자산 연결·기본 화면·설정·신청 입력 |
| `game/screens.rpy` | 저장 슬롯·도움말·알림·개발 메뉴의 텍스트 영역 |
| `game/screens_campus_main.rpy` | 명조 로고·메인 조작 |
| `game/screens_phone.rpy` | 대사·선택·휴대폰·긴 이름과 답장 표시 |
| `game/screens_character_profile.rpy` | 노트 줄·프로필 조작·긴 메모·해금 안내 |
| `game/screens_campus_gallery.rpy` | 사진첩·전체 보기·긴 메타데이터 |
| `game/screens_ending_diary.rpy` | 줄노트의 엔딩 기록 전용 화면 |
| `game/screens_application_feedback.rpy` | 종이 접기·전송 연출과 관계 알림 화면 |
| `game/systems/application_feedback.rpy` | 신청 반환 흐름·실제 증감 알림과 만료 |
| `game/systems/state.rpy`, `game/systems/story_runtime.rpy` | 기본 이름과 기존 선택 효과의 연결 |
| `game/images/ui/controls/`, `diary_polish/`, `application/` | 실행용 PNG·편집용 SVG와 종이·앨범·전송 도형 |
| `tools/build_control_surfaces.py` | 이음새 없는 버튼 PNG 재생성 |
| `game/audio/sfx/click.wav` | 새 클릭음 |

## 실행·데이터·검증

바탕화면 실행 바로가기의 대상은 D드라이브 `START_GAME.cmd`, 작업 폴더는 `D:\CampusRomance_VN`으로 확인했습니다. 게임 소스·SDK·그림·백업·검증 결과는 `D:\CampusRomance_VN` 안에 있고, 바탕화면에 게임 프로젝트를 복제하지 않습니다. 독립 배포 EXE는 이번 작업에서 생성·검증 완료로 보고하지 않습니다.

실제 검사는 저장을 제외한 QA 복사본 `tests/ui_refresh_fixture/renpy_project`에서 수행합니다. 이번 작업 전 플레이어 파일은 `game/saves` 19개와 프로젝트 `saves` 14개, 총 33개입니다. [작업 전](../tests/screenshot-review-player-saves-before.json)·[작업 후 대조](../tests/screenshot-review-player-saves-after.json)에서 33개 파일의 SHA-256과 파일 집합이 같았습니다. 추가·삭제·변경·복원 작업은 없었으며 과거의 21개 스냅샷으로 현재 저장을 되돌리지 않습니다.

실제 통과 결과의 최종 근거:

- [스크린샷 조작·프로필·엔딩 검사](../tests/screenshot-polish-final.txt)
- [전체 텍스트 영역 검사](../tests/layout-screenshot-review-final.txt)
- [이름 신청·관계 알림 검사](../tests/application-feedback-final.txt)
- [메인·휴대폰·갤러리 회귀 검사](../tests/campus-ui-screenshot-review-final.txt)
- [Lint](../tests/lint-screenshot-review.txt)
- [실제 캡처의 잉크 중심 비교](../tests/screenshot-polish-ink-results.json)
- [검사 중 수집한 화면 상태](../tests/screenshot-polish-checks.json)

최종 Lint는 2026-11-05 00:14:51에 exit 0으로 끝났고 오류·경고가 없었습니다. QA 통계 3,097개 대사 블록·36개 메뉴·50개 화면은 개발 테스트를 포함한 값이며 사람의 플레이 분량을 뜻하지 않습니다. 전체 텍스트 검사의 첫 재시작은 software 렌더러 시작 단계에서 멈춰 소유한 QA 프로세스만 종료했습니다. 그 시도에서는 레이아웃 assertion이 실행되지 않아 통과 수에 넣지 않았습니다. 개발 모드를 끈 예비 시도도 최종 통과 수에서 제외했습니다. 최종적으로 `CAMPUS_DEVELOPER=1`, `RENPY_RENDERER=gl2`, `CAMPUS_SAVE_DIR=D:\CampusRomance_VN\tests\saves-typography-audit`에서 QA 복사본을 재실행해 74개/153개 assertion이 exit 0으로 끝났습니다. 개발 모드 1은 개발 화면까지 포함한 QA 검사 환경이며 일반 실행은 `START_GAME.cmd`의 개발 모드 0을 유지합니다.

영역 검사는 기록된 94개 캡처·1,187개 레이아웃을 대상으로 하며 가능한 모든 미래 문구·외부 저장에 대한 보장을 뜻하지 않습니다. 독립 배포 EXE는 검사하지 않았습니다. 이전 실패·진단 로그는 원인 확인 이력이며 최종 통과 수에 섞지 않습니다. [0.3.0](../tests/VERIFICATION_0.3.0.md)·[0.2.0](../tests/VERIFICATION_0.2.0.md) 보고서도 이번 스크린샷 수정 전 시점의 이력으로 유지합니다.
