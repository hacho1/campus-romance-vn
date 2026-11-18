# CH01~CH03 구현 범위와 검증 기록 읽기

사용자 제공 공식 대본을 정적 Ren'Py `say`·`menu`·`if`·`label`로 변환한 공통 루트입니다. 실제 프로젝트는 `D:\CampusRomance_VN\renpy_project`이며 신규 시작은 `chapter01`에서 CH02·CH03으로 이어집니다.

이 문서는 구현 구조와 범위를 정리합니다. **최신 최종 검증·배포 상태는 [VERIFICATION_0.2.0.md](tests/VERIFICATION_0.2.0.md)**를 확인하세요. 해당 보고서는 통합 실행이 끝난 뒤 갱신하는 참조점이며, 이 문서 자체가 모든 테스트·배포 빌드 성공을 뜻하지 않습니다.

## 공식 원문과 변환

원문 사본 4개를 [design_docs/story_sources/](design_docs/story_sources/)에 보존합니다.

| 원문 | 용도 |
| --- | --- |
| [development_brief.txt](design_docs/story_sources/development_brief.txt) | 제작 요구와 구현 범위 |
| [chapter01.txt](design_docs/story_sources/chapter01.txt) | CH01 공식 대본 |
| [chapter02.txt](design_docs/story_sources/chapter02.txt) | CH02 공식 대본 |
| [chapter03.txt](design_docs/story_sources/chapter03.txt) | CH03 공식 대본 |

[chapter01_conversion.py](tools/chapter01_conversion.py), [chapter02_conversion.py](tools/chapter02_conversion.py), [chapter03_conversion.py](tools/chapter03_conversion.py)가 각 대본을 `game/routes/chapter01_official.rpy`~`chapter03_official.rpy`로 옮깁니다. 아래 `game/`은 `renpy_project/` 기준입니다. 게임은 원문 텍스트를 실시간 파싱하지 않고 변환된 네이티브 문장을 실행하므로 대사·선택지 위치를 저장과 되돌리기 흐름에 연결합니다.

BG/BGM/SFX·FLAG·조건·공통 복귀 등 제작 지시는 연출·분기로 옮깁니다. 대사 앞의 원문 행 주석과 [CH01](design_docs/chapter01_conversion_notes.md)·[CH02](design_docs/chapter02_conversion_notes.md)·[CH03 변환 기록](design_docs/chapter03_conversion_notes.md)으로 대응을 확인할 수 있습니다.

## 장면·개인 이벤트·선택 집계

| 범위 | CH01 | CH02 | CH03 | 전체 |
| --- | --- | --- | --- | --- |
| 본 장면 | 9 | 9 | 9 | 27 |
| 개인 이벤트 종류 | 5 | 5 | 5 | 15 |
| 모든 분기의 선택지 문자열 | 29 | 32 | 29 | 90 |

개인 이벤트는 각 챕터의 본 장면 안에서 갈라지는 다섯 상대의 콘텐츠입니다. 한 회차에 15종을 순서대로 보는 구조가 아니며, **챕터마다 선택한 한 명의 개인 이벤트**만 진행합니다. 신규 시작으로 CH01~CH03을 통과하는 한 경로의 메뉴 결정은 **총 16번**입니다. 모든 분기의 선택지 문자열 90개와 한 경로의 결정 횟수를 구분하세요.

- CH01 「이 조합으로 축제가 가능해?」: 팀 합류, 첫 작업 상대, 공간 문제, 다음 날로 이어지는 메시지.
- CH02 「우리 옆 부스가 수상하다」: 라이벌 첫 만남, 기획 개선, 도움 선택, 발표, 다음 시범 운영 준비.
- CH03 「시범 운영부터 사고라고?」: 방문객 관점의 문제와 철회 의사, 전시 원칙, 특별한 개인 순간, 두 팀 협력, 선택 상대와의 저녁·마지막 메시지.

CH03 SC06에서 고른 상대가 SC09 저녁 대화와 마지막 개인 메시지에도 이어집니다. 개인 이벤트와 특별한 순간을 기록하되 고백·연인 관계·개별 엔딩 진입으로 표시하지 않습니다.

## 원문 보존과 추가 대사

주요 사건·대사·선택 결과를 네이티브 대본에 유지합니다. CH03에는 이전 선택과 책 이벤트를 회수하는 **조건부 연결 문장 11개만 추가**했습니다. CH01 같은 상대 5개, CH02 같은 상대 5개, 로만 책 플래그 1개로 구분되며 해당 조건을 만족할 때만 표시합니다. 이 연결에 별도 호감·신뢰 보너스를 만들지 않습니다.

CH03의 중복된 조건표 바깥 대사 배치와 닫는 따옴표 등 최소 문법·구조 처리는 변환 기록에 남깁니다. CH01 인원 수·시각 표현, CH02·CH03의 과거 개인 이벤트 회상 등 미승인 편집안은 [STORY_REVISION_SUGGESTIONS.md](STORY_REVISION_SUGGESTIONS.md)에 분리합니다. 이 문서는 해당 수정안을 승인하거나 적용하지 않습니다.

## 현재 SD 연출과 일반 무대

SD 코미디는 **12개 이벤트·33개 변형의 완성 일러스트 한 장**을 표시·교체합니다. 인물별 SD 스프라이트 조합·자동 배치·점프를 새 SD 제작 방식으로 사용하지 않습니다. 대사·화자 이름·선택지는 그림에 넣지 않고 기존 Ren'Py UI에서 표시합니다.

[SD 제작 가이드](docs/SD_EVENT_ASSET_GUIDE.md)는 각 파일의 구도·표정·손짓과 1920×1080·안전 영역 y≤740 규칙을, [SD 구현 문서](docs/SD_EVENT_IMPLEMENTATION.md)는 시작·교체·종료 API와 저장 상태를 설명합니다. 현재 최종 SD 일러스트는 미포함이며 요청한 컷이 없으면 그 이벤트·변형의 설명 자리표시자를 표시합니다.

일반·감정 장면의 스탠딩과 8개 표정, 채팅, 기존 메인·학생증·갤러리·설정 UI는 유지합니다. 일반 이미지와 배경은 [IMAGE_ASSET_GUIDE.md](IMAGE_ASSET_GUIDE.md), 학생증은 [README_profile_ui.md](README_profile_ui.md)를 참고하세요. 최종 일반 캐릭터·SD·CG 그림을 새로 생성하거나 작업 도구를 새로 설치하지 않았습니다.

## 저장과 구 CH01 연결

일반 진행에는 호감·신뢰·작업 상대·준비도·라이벌 태도·협력·방문객 정책·특별한 순간·챕터 완료 등을 저장합니다. 영구 수집 기록은 일반 진행과 구분합니다.

기존 0.1 저장을 지우지 않고 구 `label ch01`을 보존합니다. 구 CH01을 재개한 뒤 완료 화면의 **다음 챕터로**를 선택하면 새 `chapter02`로 연결합니다. `after_load`에서는 `story_migrate_save()`와 `sd_event_migrate_after_load()`를 통해 새 기본 필드·ID와 SD 표시를 연결합니다. 기존 관계 값과 영구 수집 기록을 초기화하는 이관은 하지 않습니다.

실제 구 저장 재개·저장/불러오기 결과는 [최신 최종 검증](tests/VERIFICATION_0.2.0.md)과 [기존 저장 호환 기록](tests/legacy-sd-event.txt)을 확인하세요. 소스에 호환 경로가 있다는 사실과 모든 저장 사례를 실행 검증했다는 주장을 구분합니다.

## 분량과 플레이 시간

목표는 CH01 45~60분, CH02 60~90분, CH03 70~100분입니다. **사람이 읽고 선택하는 속도로 목표 시간을 달성했는지는 아직 검증하지 않았습니다.**

[chapter-volume-and-timing.json](tests/chapter-volume-and-timing.json)은 다음 두 범위를 구분합니다. 최종 여섯 통합 경로의 기록으로 갱신했습니다. 표시 분량과 자동 엔진 시간은 사람의 플레이 시간과 구분합니다.

| 기록 | 의미 |
| --- | --- |
| `scripts.*.display_text_statements_including_menu_prompts` / `characters_all_branches` | 선택하지 않은 개인 이벤트까지 포함한 모든 분기의 전체 발화·문자 합계 |
| `scripts.*.menu_options_all_branches` | 모든 분기에 작성된 선택지 문자열 수 |
| `runs[*].partners` | 해당 자동 실행에서 고른 챕터별 상대 |
| `chapter_metrics.displayed_lines` / `displayed_characters` | 그 실행의 한 경로에서 실제로 표시된 발화·문자 수 |
| `chapter_metrics.engine_seconds` | 그 자동 실행에 걸린 엔진 시간 |

현재 측정 방식은 즉시 텍스트 표시(`text_cps=0`)·전환 없음·자동 넘김입니다. 자동 진행의 수초·수십 초는 사람의 독서 시간이 아닙니다. 모든 분기 문자를 합해 한 회차 분량이나 플레이 시간을 계산하지 마세요. 목표 시간을 확인하려면 실제 읽기 속도에서 선택·대기·연출을 포함한 별도 플레이 측정이 필요합니다.

## 검증 기록과 남은 범위

최신 결과는 [VERIFICATION_0.2.0.md](tests/VERIFICATION_0.2.0.md)를 기준으로 확인합니다. 세부 근거는 [공식 챕터 연결 기록](tests/official-chapters-sd-events.txt), [SD 통합 기록](tests/sd-event-integration-final.txt), [SD 전환 감사](tests/sd-migration-audit.json), [기존 저장 호환 기록](tests/legacy-sd-event.txt)입니다. 진행 중인 검증이나 미생성 배포 빌드를 이 링크만으로 성공이라고 표시하지 않습니다.

CH04 이후, 개별 루트·15개 엔딩, 시크릿 담당자 확정, 최종 그림, 사람 기준 플레이 시간은 별도 범위입니다. 최종 배포 확인 범위는 검증 보고서를 참조하세요. 일반 실행은 [START_GAME.cmd](START_GAME.cmd), 개발 점검은 [START_DEVELOPER.cmd](START_DEVELOPER.cmd)를 사용합니다.
