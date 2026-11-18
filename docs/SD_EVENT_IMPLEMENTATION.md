# SD 이벤트 전체 컷 구현 기록

이 문서는 CH01~CH03의 개별 SD 스프라이트 무대를 **이벤트별 완성 일러스트 한 장**으로 교체한 범위와 검증 근거를 정리합니다. 실제 대사·선택지·분기 결과는 Ren'Py 대본에 남기고 그림에는 넣지 않습니다.

## 구현 범위

본 장면은 챕터마다 9개, 총 27개입니다. 개인 이벤트는 다섯 히로인×세 챕터의 15종이며 한 회차에는 챕터마다 선택한 하나를 진행합니다. SD 등록표에는 12개 이벤트·33개 변형이 있습니다. 등록 수는 완성 그림의 납품 수나 한 회차에 표시되는 컷 수와 다릅니다.

일반 스탠딩·표정·감정 장면, 채팅과 기존 메뉴·학생증·저장 UI를 유지합니다. 초기 시스템 구현 당시에는 최종 그림을 생성하지 않았으며, 이후 준비된 SD 이벤트 12종·33컷은 2026-11-04 게임에 삽입했습니다. 원화·적용 경로·검증은 [SD 삽입 기록](../artwork/sd_integration_20261104/README.md)에 따릅니다. CH04 이후와 개별 엔딩은 이 작업의 완료 범위에 포함하지 않습니다.

작업 전 백업: `backups/before-sd-event-cuts-source-20261104-140501.zip`.

## 구조와 파일

아래 `game/` 경로는 `renpy_project/` 기준입니다.

| 파일 | 역할 |
| --- | --- |
| `game/data/sd_events.json` | 이벤트 ID, 챕터·씬·제목·출연 맥락·구도, 각 변형의 파일·설명·선택 자막, 전환 설정 |
| `game/data/sd_event_registry.rpy` | 등록표를 `SD_EVENT_REGISTRY`와 `SD_EVENT_SETTINGS`로 로드 |
| `game/systems/sd_event_system.rpy` | 컷 선택·전환·종료, 일반 무대 보관·복원, 저장 호환 |
| `game/systems/story_runtime.rpy` | 장면·채팅·챕터 전환 시 SD 종료, 기존 SD 호출의 호환 연결 |
| `game/screens_story_stage.rpy` | SD 전체 컷 활성 중 일반 스탠딩 무대를 숨기고 일반 렌더러를 유지 |
| `game/routes/chapter01_official.rpy` ~ `chapter03_official.rpy` | 대사 흐름에 맞춘 전체 컷 시작·변형·종료 연결 |
| `game/data/sd_legacy_text_map.json` | 기존 저장의 대사 위치를 이벤트·변형에 연결하는 호환 자료 |
| `game/images/sd_events/` | 완성 WebP/PNG를 넣는 위치 |

`sd_events` 레이어에는 완성 컷을 정확히 한 장 표시합니다. 인물 아틀라스 절단·개별 SD 그림 배치·자동 반전·개별 점프를 새 컷에 적용하지 않습니다. 구도·표정·시선·손짓은 그림에 포함하고, 기존 대사창·화자 명패·선택지는 네이티브 UI로 유지합니다. 자막이 필요한 경우 `overlay_caption`만 UI로 겹칩니다.

## 파일과 API 규칙

기본 경로는 `images/sd_events/<event_id>_<variant>.webp`이며 변형 번호는 `01`처럼 두 자리입니다. 등록 경로가 없으면 같은 이름의 PNG도 찾습니다. 요청 변형이 없을 때 다른 번호의 컷을 대신 표시하지 않고 해당 컷의 설명 자리표시자를 엽니다.

API는 `sd_event_start(event_id, variant="01", transition=None)`, `sd_event_change(variant, transition=None)`, `sd_event_end(mode=None, cast=None, transition=None, restore=True)`입니다. 기본 디졸브는 등록표의 0.22초이며 호출별로 덮어쓸 수 있습니다. 화면 전환 효과를 끄거나 `transition=0`이면 즉시 교체합니다.

현재 ID·변형은 `sd_event_current`와 `sd_event_variant_id`에 기록합니다. 시작 직전의 일반 모드·출연자·표정·위치·방향과 숨긴 master 레이어 인물도 보관합니다. 기본 종료는 보관한 무대를 복원하고, 새 장면 전환 등은 복원 없이 정리할 수 있습니다. 불러오기 연결은 활성 컷을 다시 표시하거나 구 저장을 등록 컷으로 연결하는 경로를 갖습니다. 실제 기존 저장 검증의 최신 상태는 아래 기록에서 별도로 확인합니다.

## 그림 제작 기준

1920×1080·16:9의 완성 WebP/PNG 한 장을 변형마다 준비합니다. `fit="contain"`으로 전체를 표시하며 자르지 않습니다. 얼굴·입·중요 손짓은 y≤740에 두어 y=771 화자 명패와 y=814 대사창을 피합니다. 투명 그림은 단순한 파스텔 평면 위에 표시하고 전체 배경이 있는 그림도 받습니다.

실제 대사·화자 이름은 그림에 넣지 않습니다. 주인공의 얼굴·몸·손·실루엣을 확정하지 않습니다. 9명 전원을 작게 채울 필요 없이 해당 반응의 중심 인물을 크게 선택할 수 있습니다. 상세한 이벤트별 33컷 제작 명세는 [SD_EVENT_ASSET_GUIDE.md](SD_EVENT_ASSET_GUIDE.md)에 있습니다.

## 원문 보존과 감사

SD 전환 감사를 통해 CH01~CH03의 대사·들여쓰기·선택지·분기·상태·음향이 전환 전후 같은 범위로 기록됩니다. [sd-migration-audit.json](../tests/sd-migration-audit.json)의 `gameplay_indentation_audio`는 세 챕터 모두 `unchanged`, 이벤트 12개·변형 33개·미처리 큐 0개입니다. `legacy_anchors`는 2346개로 기록되어 있습니다.

이는 이번 SD 전환의 전후 비교입니다. 앞선 원문 변환에서 적용한 중복 조건 배치·따옴표 정리와 조건부 연결 대사까지 없었다는 뜻은 아닙니다. 그 구분과 미승인 제안은 [STORY_REVISION_SUGGESTIONS.md](../STORY_REVISION_SUGGESTIONS.md)에 보존합니다.

## 확정 검증과 최신 기록

| 기록 | 이 문서에서 확인한 범위 |
| --- | --- |
| [SD 통합 검증](../tests/sd-event-integration-final.txt) | 40개 실행 사례·179개 assertion 통과, `Status: PASSED`. 로그에는 나머지 선택되지 않은 사례도 구분되어 있습니다. |
| [SD 전환 감사](../tests/sd-migration-audit.json) | 세 챕터 보존 비교, 12개 이벤트·33개 변형, 미처리 큐 0개 |

[공식 챕터 연결](../tests/official-chapters-sd-events.txt)은 10개 사례·160개 assertion, [이전 SD 저장](../tests/legacy-sd-event.txt)은 2개 사례·26개 assertion을 통과했습니다. 기존 UI 35개 사례·165개 assertion 및 0.1 저장 1개 사례·8개 assertion을 포함한 소스 검사는 총 88/538입니다. Lint·패키지·실제 Windows EXE에서 확인한 범위는 [최종 검증 보고서](../tests/VERIFICATION_0.2.0.md)에 별도로 기록합니다.

자동 진행 시간은 사람의 읽기 시간이 아닙니다. 45~60 / 60~90 / 70~100분이라는 챕터별 목표 달성이나 전체 수동 플레이 완료를 이 기록만으로 주장하지 않습니다.

## 실행과 문서 사용

일반 실행은 [START_GAME.cmd](../START_GAME.cmd), 개발 점검은 [START_DEVELOPER.cmd](../START_DEVELOPER.cmd)를 사용합니다. 개발 메뉴는 `CAMPUS_DEVELOPER=1`인 실행에만 표시합니다.

아티스트·에셋 담당자는 [SD 전체 컷 가이드](SD_EVENT_ASSET_GUIDE.md), 일반 스탠딩·배경 담당자는 [이미지 가이드](../IMAGE_ASSET_GUIDE.md), 학생증 담당자는 [프로필 가이드](../README_profile_ui.md)를 읽으면 됩니다. 전체 진입 안내는 [README](../README.md)에 있습니다.

공식 대본 변환기를 재실행할 때는 SD 연결이 유지되는지 전후 감사를 다시 확인하세요. 기존 개별 SD 도우미가 소스에 남아 있어도 과거 저장 호환용이며 새 그림 제작 방식으로 되돌리지 않습니다.
