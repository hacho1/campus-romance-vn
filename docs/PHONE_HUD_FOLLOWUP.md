# 휴대폰 수동 열기와 HUD 후속 수정

작업 경로: `D:\CampusRomance_VN\renpy_project`  
백업: `backups/before-hud-motion-20261105-003232.zip`

현재 소스 구현과 네이티브 검사 결과를 설명합니다. 루트 작업자가 D드라이브의 QA 복사본에서 실제 실행한 **`hud_phone_followup` 8개 사례·52개 assertion이 모두 통과했습니다.** 근거는 [최종 실행 로그](../tests/hud-motion-final-hud_phone_followup.txt)입니다. 기존 검증 보고서를 이번 기능의 통과 근거로 합산하지 않습니다. 배포판은 계속 보류합니다.

## 고정 HUD 영역

1920×1080 가상 화면의 상단에 서로 다른 세 영역을 예약했습니다.

| 영역 | 좌표·크기 | 다음 영역까지 간격 |
| --- | --- | --- |
| 장소 | x=60, y=20, 520×66 | 휴대폰까지 20px |
| 휴대폰 | x=600, y=25, 154×56 | 퀵메뉴까지 26px |
| 퀵메뉴 | x=780, y=20, 1080×66 | 오른쪽 여백 60px |

긴 장소명은 조작에 필요한 표시만 말줄임하고 원문은 툴팁·접근성 이름에 유지합니다. `location_badge`, `current_location`, `quick_controls` ID를 보존했습니다. 일반 선택지에서도 퀵메뉴가 보이며 실제 저장·불러오기 action을 사용합니다. 선택지는 modal·zorder 150, 퀵메뉴는 zorder 170으로 두어 선택 모달을 유지하면서 퀵메뉴를 클릭할 수 있게 했습니다. 입력·게임 메뉴·휴대폰 기록 모달에서는 같은 HUD를 중복 표시하지 않습니다.

휴대폰이 열렸을 때의 오른쪽 퀵메뉴는 x=1365부터 표시합니다. `phone_toolbar_save`, `phone_toolbar_load`, `phone_toolbar_auto`, `phone_toolbar_menu` 등의 ID가 있으며 휴대폰 선택지에서도 사용합니다. `phone_toolbar_close`로 닫으면 현재 네이티브 메시지를 넘기지 않고 배경 화면의 휴대폰 버튼으로 돌아갑니다.

## 알림을 직접 여는 흐름

1. `story_chat(True, title=...)`가 대화를 시작하고 `audio/sfx/message.wav`를 한 번 재생합니다. 저장을 불러오며 이미 표시한 대화를 복원하는 동안에는 재생을 생략합니다.
2. 배경 위에 ‘핸드폰에 새 메시지 도착!’ 알림과 휴대폰 버튼을 표시합니다.
3. 플레이어가 휴대폰 버튼을 누르면 잠금화면이 열립니다.
4. **알림 열기 → 채팅 목록 → 해당 방**을 눌러 첫 메시지를 읽습니다.
5. 그때부터 원래 네이티브 대사·선택지·호감도·저장 흐름을 계속 진행합니다.

첫 메시지는 도착 시 한 번 기록하지만 올바른 대화방을 열기 전에는 읽음으로 만들거나 다음 대사로 넘기지 않습니다. 아직 닫혀 있거나 잠금·목록·다른 방을 읽는 동안에는 클릭·자동 진행·건너뛰기가 본편을 진행하지 않도록 막습니다. 대기 시간 때문에 자동 진행이 첫 메시지를 즉시 넘기지 않게, 실제 방에 들어올 때 SDK와 같은 계산식의 읽기 시간을 새로 시작합니다. 사용자 자동 진행 설정이나 효과음 볼륨 자체는 바꾸지 않습니다.

로드 중 이미 유지한 기록에 해당 스크립트가 다시 도달하더라도 동일한 stable key가 그 방의 기록에 있으면 다시 추가하지 않습니다. 마지막 메시지만 비교하지 않고 방 전체에서 중복을 확인하므로 sequence·안 읽은 수·대화 내역이 중복 증가하지 않습니다.

로드의 첫 실제 interaction 이전에 스크립트가 재실행한 방 열기는 새 사용자 읽음 조작으로 취급하지 않습니다. 이 짧은 복원 구간에는 저장된 안 읽은 수를 유지하고, 첫 interaction 뒤 플레이어가 실제 대화방을 열면 평소대로 읽음 처리합니다.

같은 복원 구간에서 이미 저장된 `choice_log`에 들어 있는 휴대폰 선택 효과는 `phone_is_replaying_choice(choice_id)`로 판별합니다. `story_apply`가 그 효과를 다시 더하지 않도록 연결하며, 실제 첫 interaction 이후의 선택과 일반 되돌리기는 이 한정된 guard의 대상이 아닙니다. 전역 선택 중복 방지 규칙을 새로 적용하지 않습니다.

새 알림 뒤 처음 열기는 잠금화면부터이며, 읽다가 닫은 뒤 다시 열면 기존 lock/list/chat 위치를 유지합니다. UI 숨기기·되돌리기·새 gate 저장 복원은 새 네이티브 검사에서 확인하도록 구성했습니다. 예전 저장의 이미 열린 휴대폰은 gate schema 0→1 이관에서 기존 읽기 체크포인트를 유지합니다. 네이티브 불러오기가 callback의 변경을 되돌리는 경우를 위해 before-load의 세션 표식과 첫 실제 interaction의 한 번 이관을 함께 사용합니다.

`phone_ui.json`의 `service_threads`에 학사 알림(`campus_notice`), 축제 지원 확인(`festival_application`), 운영위원회 공지(`festival_committee`)를 등록합니다. 세 공지 방과 단체방·개인방은 각각 기록을 보관합니다. 첫 학사 알림은 같은 설정 파일의 `notice_time`(기본 14:20)을 사용합니다. 나머지 방은 챕터 시각을 사용합니다. CH02 운영위원회 공지의 내레이션 문장 세 개는 같은 방에서 시스템 메시지로 표시하며 대본 문구와 순서는 유지합니다.

## 구현 계약

| 상태·함수 | 역할 |
| --- | --- |
| `phone_is_open` | 실제 휴대폰 프레임 열림 여부 |
| `phone_notification_pending` | 새 알림을 아직 앱에서 열지 않은 상태 |
| `phone_gate_schema` | 이전 자동 열림 저장과 새 수동 열림 저장 구분 |
| `phone_read_ready_at` | 실제 대화방에 들어온 뒤 자동 진행 허용 시각 |
| `phone_open_current()` | 새 알림은 lock, 읽던 방은 기존 화면으로 열기 |
| `phone_close_current()` | 본편 대사를 넘기지 않고 닫기 |
| `phone_allow_dismiss()` / `phone_afm_allow()` | 잘못된 화면에서 대사·자동 진행 차단 |
| `phone_reset_read_delay()` | 실제 대화방에서 읽기 시간 다시 시작 |
| `phone_sync_skip_permission()` | 읽을 수 없는 화면에서만 SDK 건너뛰기 허용을 잠시 중지하고 원래 값 복원 |
| `phone_is_replaying_choice(choice_id)` | 로드의 짧은 control replay 중 저장된 휴대폰 선택 효과 재적용 판별 |

현재 구현은 라우트에 이미 있던 `story_sfx("message")`를 사용합니다. `phone_begin()`에서 같은 소리를 중복 재생하지 않습니다. 새 이벤트도 **SFX → story_chat(True) → 기존 원문 → story_chat(False)** 순서를 따릅니다. 새 효과음은 44.1kHz 모노·약 0.36초·피크 약 0.42의 원본 절차 생성 두 음이며, 외부 음원을 사용하지 않았습니다.

## 프사와 패널

기존 개별 프로필 PNG·WebP가 있으면 우선 원형 사진으로 사용합니다. 없으면 기존 `diary_sticker(actor)`의 래스터 아틀라스에서 로만의 강아지·책, 시아의 드로잉 모티프, 다림의 게임·고양이, 오므의 카메라, 루미의 설계 모티프를 가져와 원형 마스크 안에 비율을 유지해 넣습니다. 글자만 있던 히로인 대체 프사를 취향 그림으로 바꾼 것이며 새 캐릭터·SD 그림을 생성하지 않았습니다. 공통 방·학사 알림·플레이어는 기존 공통 아이콘을 유지합니다.

오른쪽 자동·메뉴 버튼 등에 생기던 가로 이음선은 SVG를 조각내 늘리는 배경에서 발생했습니다. `phone_panel()`은 이제 `panel.png`, `hover.png`, `reply.png`, `incoming.png`, `outgoing.png`의 원본 코드 도형 PNG를 28px 경계로 사용합니다. 편집 참고 SVG는 남기고 크기·반경·색 정보는 `images/ui/phone/panel_geometry.json`에 둡니다.

## 수정 파일과 검사

- `game/screens_phone.rpy`: HUD·수동 도착 화면·선택지 위 퀵메뉴·원형 취향 프사
- `game/systems/phone_system.rpy`: gate·읽음·열기/닫기·이관·자동 진행 보호
- `game/images/ui/phone/*.png`, `panel_geometry.json`: 이음선 없는 패널
- `game/audio/sfx/message.wav`: 원본 두 음 알림
- `game/tests/hud_phone_followup.rpy`: 네이티브 8개 사례 정의. 배포에서 제외

`hud_phone_followup`의 통과 범위는 일반/폰 선택지의 실제 저장·불러오기와 키보드 진행, 상단 세 영역 간격, 첫 알림의 수동 열기, closed gate 저장 복원, 자동·건너뛰기·UI 숨김 중 첫 줄 보존, 닫기/재열기, 신·구 gate 이관, 다섯 모티프와 제공 사진 우선 사용, 학사 알림 방입니다. 소스 플레이어 저장을 실행 대상으로 쓰지 않고 D드라이브의 QA 복사본과 별도 QA 저장 폴더를 사용했습니다. 기존 전체 UI 회귀와 Lint의 최종 집계는 루트 보고서에 따로 기록합니다.

## 재실행에서 확인한 보정

중간 네이티브 실행은 8개 중 6개 통과·2개 실패였으며 최종 통과 결과가 아닙니다. 장소·휴대폰·퀵메뉴 간격 20px·26px는 실제 렌더 Window 기준으로 통과했습니다. Text ID를 Window로 잘못 읽던 검사 도구를 보정했으며 제품의 간격은 바꾸지 않았습니다.

키보드 진행을 막은 원인은 callable modal이 SDK의 렌더 단계에서 참으로 취급되어 native SayBehavior의 포커스를 차단한 것이었습니다. 최종 소스는 `say.modal False`로 두고, 닫힌 화면의 투명 입력 차단 버튼·명시 키·대사 허용 콜백·자동 진행 콜백으로 대기를 보호합니다. SDK 건너뛰기 타이머는 대사 허용 콜백을 우회하므로 읽을 수 없는 화면에 한해 기존 `_skipping` 허용 값을 보관하고 잠시 중지한 뒤 실제 방이나 일반 대화로 복귀할 때 원래 값으로 돌립니다. 정상 키보드 advance 검사는 그대로 유지했습니다.

불러오기 진단에서는 QA 저장 파일의 실제 roots는 schema 1·닫힘·새 알림 대기였지만 SDK가 로드 중 이전 대사 checkpoint로 되돌리며 schema 0·열림의 옛값을 복원하는 점을 확인했습니다. 본편 휴대폰의 실제 interaction에서 공식 `renpy.retain_after_load()`를 호출하여 저장 시점의 화면·읽음 값을 유지합니다. 이 API는 로드 시점의 데이터 유지에 사용하며 일반 되돌리기를 막지 않습니다. 메인 메뉴·게임 메뉴에는 적용하지 않습니다.

이전 schema 저장의 이관은 첫 after-load에서 발견한 구형 여부를 `renpy.session`에 보존하고 첫 실제 interaction에서 한 번만 적용합니다. schema 1의 닫힌 저장에는 강제 열기를 적용하지 않습니다. 새 저장과 schema 0을 재현한 저장으로 실행한 8개 사례에서 52개 검사를 통과했으며, 복원 진단은 다음과 같았습니다.

- 새 닫힌 저장: `HUD_CLOSED_GATE_LOAD 1 False True chat 1` — schema 1, 닫힘, 새 알림 대기, 메시지 1개 유지.
- 이전 열린 저장: `HUD_LEGACY_GATE_LOAD 1 True False chat campus_group` — schema 1로 이관, 열림, 새 알림 재발생 없음.

저장 재검증은 휴대폰의 잠금화면·목록·대화방을 각각 불러오는 기존 3개 사례와 실제 CH01의 첫 잠금화면 복원, 답장 보상 재적용 여부를 포함합니다. 실행 결과는 [후속 작업 검증 기록](HUD_MOTION_FOLLOWUP.md)에 모았습니다.
