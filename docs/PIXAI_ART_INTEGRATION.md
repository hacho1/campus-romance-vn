# 픽시 AI 일러스트 적용 기록

원본은 `artwork/pixai_*`에 보관하고, 게임에서 사용하는 파일은 `renpy_project/game/images/`에 배치했습니다.

## 타이틀과 스탠딩

- 꽃밭에 누운 다섯 히로인 일러스트를 타이틀과 COMMON 갤러리의 LD-01에 연결했습니다. 2048×1152 원본 픽셀과 구도를 유지했습니다. 타이틀 글자 주변을 밝히고 얼굴이 모인 가운데 영역에는 원화 색을 살렸습니다.
- 로만·시아·다림·오므·루미·스키·협합·헤스·밤밤의 스탠딩 47장을 투명 PNG로 정리했습니다. 새 표정이 없는 경우 같은 캐릭터의 새 기본 이미지를 사용하며, 기존 B/C 포즈도 사용할 수 있습니다. 루미는 `pixai_lumi_v2`에서 가져왔습니다. [스탠딩 파일 목록](../artwork/pixai_review/standing-matte-inventory.json)

## 본편 일러스트

| 유형 | 적용한 장면 |
| --- | --- |
| 공통 LD 5장 | CH01 첫 전원 집합, CH02 라이벌 첫 만남·발표 직전·발표 종료, CH03 나무 그늘 대화 |
| 개인 LD 5장 | CH03의 로만·시아·다림·오므·루미 개인 이벤트 |
| CH01 SD 3장 | 복도 시아·오므 말다툼, 첫 회의, 공간 배정 문제 |
| CH02 SD 3장 | 시아·스키 첫 만남, 면접 결과, 발표 후 신경전 |
| CH03 SD 1장 | 첫 방문객의 질문 |

LD-02는 루미의 합류를 설명하는 두 문장 뒤 다림의 인사부터 표시하고 시아가 말을 걸기 전에 스탠딩으로 복귀합니다. 대사와 선택지 원문은 그대로입니다. CG와 SD의 수집 시점은 본편에서 해당 컷을 볼 때이며 타이틀 LD-01은 메인 메뉴 방문 때 수집합니다.

LD-03 후보는 주인공 방 장면에 주인공으로 읽힐 수 있는 인물이 그려져 있어 자리표시자를 유지했습니다. 인물이나 동작이 대본과 다른 SD 후보 5장은 기존 컷을 유지했습니다. 일부 단체 LD의 머리색과 장식은 스탠딩과 차이가 있습니다. [SD 교체 목록과 보류 사유](../artwork/pixai_review/sd_scene_integration.json)

## 적용 위치와 백업

| 게임 경로 | 변경 |
| --- | --- |
| `images/cg/` | 타이틀 LD-01과 본편 LD 10장 |
| `images/sd_events/` | 이벤트 7개 변형의 기존 파일 교체 |
| `images/standings/pixai_20261105/` | 스탠딩 9명·47장 |
| `data/ld_standing_registry.rpy` | 새 표정 선택과 기존 포즈 경로 |
| `routes/chapter01_official.rpy`, `data/cg_registry.json` | LD-02 표시 시점과 갤러리 장면 정보 |
| `images/ui/campus_main/main_wash.svg` | 타이틀 글자 주변 대비 |

교체 전 파일은 `backups/before-pixai-title-20261105-190524-474/`, `before-pixai-ld-20261105-190700-967/`, `before-pixai-standings-20261105-190843/`, `before-pixai-sd-20261105-190910/`에 있습니다.

## 확인 자료

Ren’Py 8.5.3 격리 실행의 테스트 5개·검사 34개와 Lint가 통과했습니다. 타이틀과 갤러리, 복도 대화에서 스탠딩과 SD 사이의 전환, 첫 전원 집합과 로만 개인 CG의 표시 및 수집을 실제 화면에서 확인했습니다. 등록된 SD 33컷과 일반 스탠딩 216개 표정·포즈 조합의 파일 연결도 확인했습니다.

- [타이틀](../tests/pixai_integration_20261105/evidence/01-title.png) · [복도 스탠딩](../tests/pixai_integration_20261105/evidence/03-standings-in-story.png) · [복도 SD 컷](../tests/pixai_integration_20261105/evidence/04-sd-in-story.png) · [로만 개인 이벤트](../tests/pixai_integration_20261105/evidence/07-roman-private-ld.png)
- [Ren’Py 실행 로그](../tests/pixai_integration_20261105/renpy-run.txt) · [Lint 로그](../tests/pixai_integration_20261105/renpy-lint.txt)
