# CH01~CH03 이미지 삽입 가이드

이 문서는 `D:\CampusRomance_VN\renpy_project\game`에 그림 파일을 넣어 9명의 일반 스탠딩과 배경을 교체하는 방법을 안내합니다. 지정된 경로와 이름을 사용하면 대본이나 코드를 수정하지 않아도 됩니다. 게임을 종료하고 파일을 넣은 뒤 다시 실행하세요.

일반 스탠딩이 없으면 이름 명패로 대체할 수 있습니다. SD는 이벤트 전체 일러스트 한 장으로 표시하며, 2026-11-04 준비된 12개 이벤트·33컷을 게임에 연결했습니다. 규격은 [SD 이벤트 전체 컷 가이드](docs/SD_EVENT_ASSET_GUIDE.md), 실제 삽입 기록은 [SD 삽입 기록](artwork/sd_integration_20261104/README.md)을 따릅니다. 타이틀과 추가 배경 11종도 게임에 적용되어 있으며 기존 화면·학생증 UI 구조는 유지합니다.

## 1. 먼저 한 장 넣기

로만의 기본 일반 스탠딩을 넣으려면 투명 PNG를 아래 경로에 저장하세요.

`game/images/heroines/roman/normal.png`

일반 스탠딩은 기본 이미지 한 장만 있어도 다른 표정이 빠진 장면에서 그 이미지를 사용합니다. SD는 인물별 파일이 아닌 완성된 이벤트 컷을 별도로 준비합니다. 새 SD의 경로·구도·33개 파일 목록은 [전용 가이드](docs/SD_EVENT_ASSET_GUIDE.md)에 있습니다. 원본 그림은 게임 폴더 바깥에도 보관해 두세요.

## 2. 인물 ID와 폴더

아래 경로는 모두 프로젝트의 `renpy_project/`를 기준으로 합니다. 파일명은 영문 소문자와 `.png` 확장자를 사용하세요.

| 인물 | ID | 일반 스탠딩 폴더 |
| --- | --- | --- |
| 로만 | `roman` | `game/images/heroines/roman/` |
| 시아 | `sia` | `game/images/heroines/sia/` |
| 다림 | `darim` | `game/images/heroines/darim/` |
| 오므 | `omu` | `game/images/heroines/omu/` |
| 하린 | `lumi` | `game/images/heroines/lumi/` |
| 스키 | `ski` | `game/images/rivals/ski/` |
| 협합 | `hyeophap` | `game/images/rivals/hyeophap/` |
| 헤스 | `hess` | `game/images/rivals/hess/` |
| 밤밤 | `bambam` | `game/images/rivals/bambam/` |

공식 대본의 `rumi`는 기존 프로젝트 ID `lumi`로 연결합니다. 하린 일반 스탠딩은 `heroines/rumi/`도 호환되지만, 같은 표정이 양쪽에 있으면 `lumi/`를 먼저 읽습니다. 새 파일은 `lumi/`로 통일하면 관리하기 쉽습니다.

학생증 사진은 스탠딩과 별개입니다. 기존 [학생증 가이드](README_profile_ui.md)의 `profile_roman.png` 또는 `roman/profile.png` 규칙을 사용하세요. `normal.png`를 넣는 것만으로 학생증 사진이 바뀌지는 않습니다. 라이벌 4명은 이야기 무대의 인물이며 기존 학생증 목록을 자동으로 확장하지 않습니다.

## 3. 표정 파일명과 누락 처리

일반 스탠딩은 아래 8개 표정 이름을 사용합니다. SD 전체 컷의 변형 번호와는 별개입니다.

| 표정 | 기본 파일명 | 호환 파일명 |
| --- | --- | --- |
| 기본 | `normal.png` | `neutral.png` |
| 웃음 | `happy.png` | `smile.png` |
| 뾰로통 | `angry.png` | 없음 |
| 당황 | `embarrassed.png` | `shy.png` |
| 놀람 | `surprised.png` | 없음 |
| 시무룩 | `sad.png` | 없음 |
| 장난 | `smug.png` | 없음 |
| 갸웃 | `confused.png` | `surprised.png`로 대체 가능 |

찾는 순서는 **요청한 표정 → 해당 호환 표정 → normal → neutral**입니다. 하린은 이 각 단계에서 `lumi/` 다음에 `rumi/`를 확인합니다. 예를 들어 `confused.png`가 없으면 같은 인물의 `surprised.png`를 먼저 찾고, 이것도 없으면 기본 표정을 찾습니다.

대본의 `neutral`, `smile`, `shy` 표정 요청도 각각 `normal`, `happy`, `embarrassed`로 정규화됩니다. 알 수 없는 표정 요청은 `normal`로 처리합니다. 어떤 PNG도 없으면 이름·표정 글자·간단한 표정 기호가 있는 종이 명패를 표시합니다. 누락 파일 때문에 최종 그림을 임의 생성하지 않습니다.

## 4. 권장 해상도와 투명 배경

| 용도 | 권장 제작 크기 | 실제 표시 영역 |
| --- | --- | --- |
| 일반 스탠딩 | 픽시 AI 세트 1024×1536, 투명 PNG | 인원수에 맞춰 원본 비율 유지 |
| SD 이벤트 전체 컷 | 1920×1080 WebP/PNG | 전체 화면, 중요 내용 y≤740 |
| 배경 | 1920×1080, 고해상도는 3840×2160 | 1920×1080 전체 캔버스 |

크기는 게임의 1920×1080 가상 좌표 기준입니다. 일반 스탠딩은 `fit="contain"`으로 비율을 유지하며 영역 안에 들어갑니다. SD 전체 컷도 자르지 않고 전체를 맞추며 자세한 안전 영역은 전용 가이드를 따릅니다. 배경은 화면 전체 크기에 맞추므로 16:9로 준비하세요.

그림 편집기에서 배경 레이어를 숨기고 투명 격자가 보이는지 확인한 뒤 **알파 채널이 있는 RGBA PNG**로 내보내세요. 흰색·검은색 바탕을 그림에 합치지 말고, 가장자리에도 불필요한 불투명 테두리를 남기지 마세요. 배경 그림은 불투명하게 준비해도 됩니다.

같은 인물의 모든 표정은 캔버스 크기·발 위치·얼굴 위치를 맞추세요. 파일 안의 투명 여백이 지나치게 넓으면 실제 인물이 작아 보입니다. 코드 수정 없이 크기를 맞추려면 그림 자체의 여백과 배치를 조정하세요.

## 5. 현재 무대 위치와 크기

배치는 `game/systems/story_runtime.rpy`와 `game/screens_story_stage.rpy`에서 결정합니다. 일반 스탠딩의 기준점은 아래쪽 중앙 y=795입니다. 픽시 AI 스탠딩은 872×1308의 고정 표시 크기를 사용합니다.

| 일반 인원 | x 좌표 |
| --- | --- |
| 1명 | 960 |
| 2명 | 640, 1280 |
| 3명 | 440, 960, 1480 |
| 4명 | 300, 740, 1180, 1620 |
| 5명 | 248, 604, 960, 1316, 1672 |
| 양 팀 6~9명 | 발언 팀에 따라 히로인과 라이벌 구도를 전환 |

일반·감정 모드는 최대 9명의 등장인물을 기억하고, 한 구도에는 최대 5명을 표시합니다. 인원이 들어오거나 화자가 바뀌어도 스탠딩 크기를 유지합니다. 듣는 인물은 밝기를 낮춰 표시합니다. 실제 등장·퇴장은 대본에서 좌우 이동을 지정할 수 있습니다. [스탠딩 모션 가이드](docs/STANDING_MOTION_GUIDE.md)

SD 이벤트는 한 장 안에 인물 구도를 완성하므로 인물 수별 배치 좌표나 두 줄 합성 규칙을 사용하지 않습니다. 주연 반응을 크게 잡고 필요한 인물만 선택하는 방법은 [SD 제작 명세](docs/SD_EVENT_ASSET_GUIDE.md)를 참고하세요.

일반 스탠딩 이미지가 없을 때 명패 크기는 330×510입니다. 일반 위치 규칙 자체를 바꾸려면 개발자가 `story_stage_view`의 좌표를 수정해야 합니다. 그림 교체만으로 이 규칙이 바뀌지는 않습니다.

## 6. 배경 파일 넣기

배경도 PNG를 넣으면 자동으로 교체됩니다. 예를 들어 도서관은 아래 경로를 사용합니다.

`game/images/backgrounds/library.png`

| 배경 ID | 용도 |
| --- | --- |
| `campus` | 교정·산책로 |
| `clubroom` | 공동 동아리실·축제 준비실 |
| `board` | 게시판 |
| `corridor` | 복도 |
| `room` | 주인공 방 |
| `library` | 도서관 |
| `animation` | 애니메이션과 작업실 |
| `study` | 스터디룸 |
| `architecture` | 건축학과 작업실 |
| `booth` | 부스·축제 구역 |
| `presentation` | 발표실 |
| `cafe` | 카페 |
| `classroom` | 교실 대체 자산 |

`story_scene()`은 다음 순서로 배경을 찾습니다.

1. `images/backgrounds/<id>.png`
2. `images/backgrounds/story/<id>.svg`
3. `images/backgrounds/<id>.svg`
4. 기본 복도 `images/backgrounds/story/corridor.svg`

마지막 복도 파일은 공통 대체 화면이므로 보존하세요. 이 우선순위는 CH01~CH03의 `story_scene()` 장면에 적용됩니다. 기존 메인 화면의 `bg campus` 정의를 수정할 필요는 없습니다.

`night_campus`는 `campus`, `prep_room`은 `clubroom`으로 연결합니다. 따라서 이 두 이름의 PNG를 따로 넣기보다 연결 대상의 PNG를 넣으세요. 낮·저녁·밤은 `light="day" / "evening" / "night"`로 구분하며 기존 배경에 색조를 입힙니다. `night_campus`라는 이름만으로 밤 색조를 지정하지는 않습니다.

## 7. 대본 연출 API 참고

이미지 삽입에는 아래 API를 수정할 필요가 없습니다. 연출을 조정하는 개발자는 `game/systems/story_runtime.rpy`와 `game/screens_story_stage.rpy`를 함께 확인하세요. API 호출은 Ren'Py 대본의 Python 문장에서 사용합니다.

| API | 역할 |
| --- | --- |
| `story_scene(bg, mode="normal", cast=None, music=None, light="day", location=None)` | 배경·출연자·모드·장소를 바꾸고 채팅 표시를 종료합니다. |
| `story_stage(mode=None, cast=None, faces=None, positions=None, facing=None)` | 배경을 유지하며 무대와 표정을 갱신합니다. `faces`는 인물 ID→표정 이름 사전입니다. |
| `story_effect(kind, target=None, caption=None)` | 일반 스탠딩의 동작을 지정합니다. SD 전체 컷에서는 개별 동작을 적용하지 않습니다. |
| `story_chat(active, title="축제 준비팀")` | 채팅 패널을 켜거나 끕니다. 호출할 때 기존 메시지 목록을 비웁니다. |
| `story_sfx(name)` | 준비된 효과음을 찾아 재생합니다. |
| `story_fade_out()` | 이야기 무대·채팅·짧은 자막을 감춥니다. |

- **일반 대화**: `mode="normal"`. 일반 스탠딩과 기존 대사창을 사용합니다.
- **SD 이벤트 전체 컷**: `sd_event_start()` / `sd_event_change()` / `sd_event_end()`를 사용합니다. `mode="sd"` 호출과 개별 SD 폴더는 과거 저장 호환용이며 새 제작 방식이 아닙니다.
- **차분한 감정·로맨스 장면**: `mode="emotion"`. 일반 스탠딩을 쓰는 구분값입니다. 조용한 대화에서는 과장된 반응 효과 호출을 생략하세요. 이벤트 CG나 연인 관계를 자동으로 만드는 기능은 아닙니다.

`cast`를 새로 지정하면 기존 동작 효과를 초기화합니다. 표정은 마지막 값이 남을 수 있으므로 장면에 필요한 표정을 `faces`로 명시하세요. 출연 목록은 유효한 9명 ID만 사용합니다. 주인공·운영위원·방문객은 대사 화자로 사용할 수 있지만 이 9명용 그림 목록에는 포함하지 않습니다.

### SD 전체 컷으로 전환

이전 개별 SD의 점프·표정·배치·아틀라스 조합 안내는 사용하지 않습니다. [SD 이벤트 가이드](docs/SD_EVENT_ASSET_GUIDE.md)의 완성 컷 파일과 변형 교체 API를 사용하세요. 실제 대사는 그림에 넣지 않고 기존 대사창에서만 표시합니다.

채팅 패널은 최근 3개 메시지를 보여 주며 화자 이름과 입력한 주인공 이름을 사용합니다. 주인공 메시지는 분홍 종이로 구분합니다. 화자 전용 인물 사진은 필요하지 않습니다.

효과음은 `audio/sfx/<name>.ogg`, `.wav`, `.mp3` 순서로 찾습니다. `message`는 없을 때 기존 `click.wav`도 확인합니다. 전부 없으면 소리 없이 계속 진행합니다. 없는 음성이나 효과음을 새로 생성하지 않습니다.

## 8. 삽입 후 확인

일반 스탠딩의 기본·다른 표정과 발 위치를 확인하세요. SD 전체 컷은 얼굴·중요 손짓이 y≤740에 있고 대사창에 가려지지 않는지 확인합니다. 일반 그림 누락은 기본 표정·명패로, SD 변형 누락은 해당 변형의 설명 자리표시자로 돌아가는지 구분해 확인하세요.

개발자용 챕터·SD·개인 이벤트 점검 화면은 `CAMPUS_DEVELOPER=1`인 실행에서만 사용합니다. 일반 배포 실행에는 개발 메뉴를 표시하지 않습니다. 학생증 가이드의 개발실 경로도 이 개발 실행에 한정됩니다.

이 문서는 현재 소스의 경로와 표시 규칙을 안내합니다. CH01~CH03 실행·분기·저장/불러오기·플레이 시간의 최종 검증 결과는 별도 통합 보고를 확인하세요.

## 9. 일반 스탠딩의 개별 위치·방향·이동

이 절은 일반·감정 모드의 스탠딩에만 적용합니다. `story_stage(mode=None, cast=None, faces=None, positions=None, facing=None)`의 `positions={인물ID: (x, y)}`로 위치를, `facing={인물ID: 1 또는 -1}`로 원본 방향·좌우 반전을 지정합니다. 기준점은 아래 중앙입니다. 이름 명패와 표정 글자는 반전하지 않습니다.

일반 스탠딩의 배치 예는 `story_stage(mode="normal", cast=["roman"], faces={"roman": "normal"}, positions={"roman": (960, 795)}, facing={"roman": 1})`입니다. `story_move(actor, x, y)`는 현재 일반 출연자를 이동하며 화면 전환 효과가 켜져 있으면 0.25초 이동을 적용합니다. 효과가 꺼져 있으면 목적지에 바로 표시합니다.

개별 위치·방향은 `story_positions`와 `story_facing`이라는 일반 저장 상태로 관리합니다. 새 장면·챕터 또는 다른 일반/감정 모드로 바뀌면 지정값을 비웁니다. 같은 모드에서 출연자만 다시 지정하면 자동 초기화하지 않습니다.

SD 전체 컷이 활성화된 동안 `story_move()`와 개별 `story_effect()`는 적용하지 않습니다. 예전 `story_faceoff()`·SD 개별 파일·좌표·자동 반전 안내는 과거 저장 호환용이며 새 SD 장면에서는 사용하지 않습니다. 인물의 표정·손짓·방향을 완성한 그림을 교체하는 [현재 SD 가이드](docs/SD_EVENT_ASSET_GUIDE.md)를 따르세요.
