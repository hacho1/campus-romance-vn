# HUD·휴대폰·밤 배경·스탠딩 후속 수정

프로젝트: `D:\CampusRomance_VN\renpy_project`  
수정 전 백업: `backups/before-hud-motion-20261105-003232.zip`  
배포판은 만들지 않습니다. 기존 바탕화면 바로가기는 D드라이브 소스 프로젝트를 실행합니다.

## 적용한 동작

- 장소 표시, 휴대폰 버튼, 퀵메뉴를 서로 겹치지 않는 영역에 배치했습니다. 선택지에서도 위쪽 저장·불러오기를 조작할 수 있습니다.
- 설정 슬라이더의 막대와 손잡이를 같은 40px 높이 안에 그렸습니다. 손잡이의 실제 보이는 중심과 막대의 중심이 같습니다. 레일의 두 끝에는 손잡이가 잘리지 않을 여백을 둡니다.
- 관계 알림은 대칭 패널과 고정 높이 행을 사용합니다. 이름, 호감·신뢰 항목, 증감 수치를 각 영역의 가운데에 둡니다. 관계 수치 처리와 2.2초 만료는 그대로입니다.
- 작은 원형 프사는 기존 캐릭터별 취향 스티커를 사용합니다. 제공한 실제 프로필 사진이 있으면 먼저 사용합니다.
- 폰 조작 패널을 PNG로 교체해 SVG를 아홉 조각으로 늘릴 때 보이던 가로 이음새를 없앴습니다.
- 새 메시지에는 두 음의 짧은 알림음과 **핸드폰에 새 메시지 도착!** 안내를 사용합니다. 휴대폰 버튼 → 잠금 알림 → 대화 목록 → 해당 방을 직접 눌러 읽습니다. 기다리는 동안 자동·건너뛰기가 메시지를 넘기지 않습니다.
- CH01 첫 학사 알림과 지원 확인, CH01·CH02 운영위원회 공지, CH01~CH03의 개인·단체 채팅이 이 흐름을 사용합니다. 기존 문장은 원래 순서로 표시합니다. 학사·지원·운영위원회 알림은 별도 대화방에 보관합니다.
- 밤의 주인공 방과 캠퍼스는 별도 밤 그림을 사용합니다. 창밖·하늘까지 밤이며 원래 낮 그림은 보존합니다. 기존 밤 저장도 배경만 교체해 복원합니다.
- 일반 스탠딩에서는 여러 명 중 화자가 조금 커지고 밝아지며, 비화자는 불투명도를 유지한 채 살짝 어두워집니다. 떨림·점프·좌우 입퇴장·하트·느낌표·전구를 재사용할 수 있습니다. LD·SD는 기존 완성 컷 한 장 방식을 유지합니다.

## 수정 위치

| 경로 (`renpy_project/game/` 기준) | 내용 |
| --- | --- |
| `screens_phone.rpy`, `systems/phone_system.rpy` | 상단 배치, 선택지 퀵메뉴, 원형 프사, 알림과 수동 열기 |
| `theme_spring.rpy`, `images/ui/controls/slider_*.png` | 슬라이더 중심·손잡이 영역 |
| `screens_application_feedback.rpy` | 관계 알림의 대칭 패널과 가운데 행 |
| `systems/story_lighting.rpy`, `images/backgrounds/*_night.png` | 시간대별 배경과 구 저장 복원 |
| `systems/story_runtime.rpy`, `screens_story_stage.rpy`, `images/ui/stage_effects/` | 화자 강조·일반 스탠딩 모션·감정 표시 |
| `routes/chapter01_official.rpy`, `routes/chapter02_official.rpy`, `routes/chapter03_official.rpy` | 원문을 유지한 휴대폰 이벤트 연결과 스탠딩 모션 호출 |
| `data/phone_ui.json`, `audio/sfx/message.wav` | 공지 방 등록, 연출용 시각, 두 음 알림음 |

슬라이더 도형은 `tools/build_slider_surfaces.py`로 다시 생성합니다. 레일과 손잡이의 높이를 서로 다르게 줄이면 기존 수직 편향이 다시 생길 수 있습니다.

스탠딩 연출 호출 예:

```renpy
$ story_effect("shake", "sia")
$ story_effect("jump", "roman")
$ story_icon("roman", "heart")
$ story_icon("lumi", "lightbulb")
$ story_enter("lumi", side="right")
$ story_exit("lumi", side="right")
```

CH01 루미 개인 작업 장면에는 짧은 입퇴장·전구, 저녁 대화에는 시아 떨림·로만 점프와 느낌표, CH03 로만의 마지막 약속에는 작은 하트를 연결했습니다. 화면 효과 끄기 설정은 이동을 줄이면서 최종 상태를 유지합니다. 개발 실행의 챕터 연출 점검에서는 모든 모션을 직접 눌러 볼 수 있습니다.

## 검증 기록

Ren’Py 8.5.3의 격리된 QA 프로젝트에서 기능별 테스트 63개와 본편 경로 1개, 총 64개 사례와 검사 451개를 통과했습니다. 실제 렌더 이미지의 위치 검사 22개와 Lint도 통과했습니다. 휴대폰의 잠금화면·목록·대화방 저장 복원 3개는 별도로 재실행했습니다.

- 실제 챕터 테스트에서는 첫 알림의 잠금화면을 불러와 메시지 1개와 안 읽은 상태를 확인했습니다. 답장을 보낸 뒤 불러왔을 때는 호감도 +2, 신뢰도 +1, 선택 기록 1개가 유지됐습니다. 지원 확인과 운영위원회 공지도 직접 열어 원문과 다음 대사를 확인했습니다. [휴대폰 테스트 로그](../tests/hud-motion-final-official_phone_entry_followup.txt)
- 로만 → 시아 → 다림을 선택한 본편 경로에서 14개 알림을 차례로 열고 CH03 끝까지 진행했습니다. 이 경로에서 선택 16개, 장면 27개, SD 이벤트 12개를 확인했습니다. [본편 경로 로그](../tests/hud-motion-official-chapter-path.txt)
- 스크립트 백업과 현재 소스의 대사, 선택지, 분기, 진행 플래그를 비교했습니다. QA는 별도 저장 경로에서 실행했습니다. [검증 집계](../tests/HUD_MOTION_VERIFICATION.json)
- [첫 메시지 도착 화면](../tests/official-phone-entry-screenshots/first_school_notification.png) · [잠금화면 복원](../tests/official-phone-entry-screenshots/first_school_saved_lock_restored.png) · [선택지 상단 퀵메뉴](../tests/official-phone-entry-screenshots/first_authored_choice_with_toolbar.png) · [환경설정](../design_docs/review_20261105/after-settings.png)

자세한 교체·수정법은 [휴대폰과 HUD](PHONE_HUD_FOLLOWUP.md), [밤 배경](STORY_LIGHTING_GUIDE.md), [스탠딩 모션](STANDING_MOTION_GUIDE.md)을 참고합니다. 최종 인물 일러스트는 이번 작업에서 생성하지 않았습니다. 밤 배경의 생성 해상도와 캔버스 표시 방법은 밤 배경 가이드에 기록했습니다.
