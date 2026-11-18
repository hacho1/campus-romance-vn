# SD 이벤트 전환 독립 검증 기록

검증 대상: D:\CampusRomance_VN\renpy_project, Ren’Py 8.5.3.26051504. 2026-11-04.

CH01~CH03의 SD 장면은 개별 캐릭터 자동 배치 대신 등록된 완성 컷 하나를 표시한다. 12개 이벤트와 33개 변형 컷이 연결되어 있으며, 이미지가 없는 변형은 제목·이벤트 ID·등장인물·구도·필요 파일명을 가진 안내 화면을 표시한다. 최종 캐릭터 원화와 SD 일러스트는 생성하지 않았다.

## 변경한 파일

아래 경로는 프로젝트 루트 D:\CampusRomance_VN 기준이다. 같은 프로젝트를 작업하던 ‘현대 캠퍼스 미연시 제작’ 채팅의 전환 작업을 포함하여 현재 소스와 변경 전 백업을 대조했다.

- game 시스템: renpy_project/game/systems/sd_event_system.rpy (신규), systems/story_runtime.rpy, systems/state.rpy
- 등록 데이터: renpy_project/game/data/sd_event_registry.rpy (신규), data/sd_events.json (신규), data/sd_legacy_text_map.json (신규), data/story_assets.json
- 화면: renpy_project/game/screens_story_stage.rpy, screens.rpy
- 대본 연결: renpy_project/game/routes/chapter01_official.rpy, chapter02_official.rpy, chapter03_official.rpy
- 테스트: renpy_project/game/tests/sd_event_integration.rpy, legacy_sd_event.rpy, sd_independent_legacy.rpy, sd_independent_rollback.rpy, 00_independent_save_isolation.rpy (신규), chapters_integration.rpy, integration.rpy, staging_smoke.rpy
- 검사 도구: tools/check_sd_events.py, tools/verify_sd_events_audit.py (독립 정적 검사)
- 제작 명세: docs/SD_EVENT_ASSET_GUIDE.md

변경 전 원문·선택지·조건·들여쓰기·진행 명령·관계 수치·음향 명령의 보존 여부를 백업과 대조했다. CH01/02/03 보호 문장 968/1131/1219개가 기준과 일치한다.

## 실행 결과

| 검사 | 결과 | 로그 |
| --- | --- | --- |
| 최종 Ren’Py Lint | 오류 없음 | tests/independent-sd-lint.txt |
| 독립 정적 감사 | 112 통과, 0 실패 | tests/sd-independent-audit.json |
| 전체 SD 검사 | 40 테스트, 179 assertion 통과 | tests/sd-independent-integration-final.txt |
| 공식 CH01~03 진행 | 6개 완주 경로 + 3개 모드 저장 복원 + 개발자/누락 에셋 검사, 10 테스트 통과 | tests/official-chapters-sd-events.txt |
| 실제 구버전 SD 저장 | 2 테스트, 26 assertion 통과 | tests/legacy-sd-event.txt |
| 구버전 도움 분기 복원 | 6 테스트, 30 assertion 통과 | tests/sd-independent-legacy-after.txt |
| 실제 롤백/재진행 | 1 테스트 통과 | tests/sd-independent-rollback.txt |
| 기존 단체 채팅 저장 복원 | 1 테스트, 3 assertion 통과 | tests/independent-sd-chat.txt |
| 테스트 저장 격리 | 1 테스트 통과, 보호 저장 파일 25개 SHA256 전후 일치 | tests/sd-independent-save-isolation.txt |

40개 SD 검사는 33개 누락 컷, PNG/WebP의 단일 이미지 표시와 확장자 대체, 변형 교체, 일반 스탠딩 복귀, 진입 전·도중·종료 후 저장, 전환 설정, 미등록 ID/변형을 포함한다. 테스트용 단색 PNG/WebP는 배포에서 제외된다.

실제 구버전 대사 저장 검사는 이전 SD 9인 상태를 새 이벤트 컷으로 복원하며, 저장 대사를 유지하고 다음 대사로 진행하는지 확인한다. 테스트 진입 라벨을 처음부터 재실행하여 통과하는 방식은 사용하지 않는다.

롤백 검사는 일반 → 컷01 → 컷02 → 일반의 네이티브 대사 체크포인트를 되돌린 뒤 다시 진행한다. 컷02·컷01·원래 일반 화면, 표정·위치·방향과 이벤트 화면 복원을 확인했다.

## 독립 점검 중 수정한 문제

1. CH02 도움 선택 직후에는 rival_helped가 아직 False이므로, 구버전 저장 복원에서 도움 컷03을 반응 컷02로 잘못 낮추던 문제를 재현했다. 명백한 도움 분기 앵커에 help_branch 메타데이터를 추가하고 해당 앵커에서는 보정을 생략한다. 공통 대사는 기존 플래그로 분기한다. 호감도·선택지·플래그 적용 시점은 그대로다. 수정 전 3개 실패를 확인했고 수정 후 6개 모두 통과했다.
2. 최종 컷 교체 위치를 기준으로 sd_legacy_text_map.json을 다시 생성했다. 예: ‘너까지 그러지 마!’는 음료수 사건 컷03으로 연결된다. tools/check_sd_events.py는 원문과 들여쓰기 보존 및 33컷의 상호작용 지점도 함께 검사한다.
3. Ren’Py는 config.savedir 외에 game/saves도 자동 등록하여 테스트끼리 persistent 쓰기가 충돌할 수 있었다. tests/00_independent_save_isolation.rpy의 python early 후크는 CAMPUS_SAVE_DIR가 설정된 검사에서만 초기 저장 읽기·병합·쓰기 위치를 전용 폴더로 제한한다. SDK와 일반 플레이 저장 설정은 수정하지 않았다. 적용 후 실제 슬롯·persistent를 쓰고 기존 저장 25개의 SHA256이 그대로인 것을 확인했다. 기존 폴더의 파일을 임의 삭제하거나 되돌리지 않았다.

## 백업

- 전체 전환 전 소스: backups/before-sd-event-cuts-source-20261104-140501.zip
- 도움 분기 보정 전: backups/independent-sd-legacy-fix-20261104-144124.zip
- 저장 폴더 증거 보관: backups/independent-save-evidence-20261104-145433.zip

## 남은 이미지 작업과 검증 범위

최종 SD 그림 33컷은 제작 대기 상태이며, 현재 안내 화면으로 플레이할 수 있다. 실제 그림을 넣은 뒤에는 얼굴·손짓이 y=740 이하의 안전 영역에 있는지 시각 검수를 해야 한다. 파일 규격·장면별 배치·표정·포즈·삽입 경로는 SD_EVENT_ASSET_GUIDE.md에 있다.

이 기록은 위 소스와 로그의 독립 검증이다. 모든 과거 버전·모든 사용자 저장 파일을 전수 검사했다는 뜻은 아니며, Windows 배포본의 별도 실행 확인은 이 표의 소스 테스트와 구분한다.
