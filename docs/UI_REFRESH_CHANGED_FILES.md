# 0.3.0 UI 개편 변경 파일

비교 기준: `backups/before-campus-ui-refresh-v020.zip`의 0.2.0 Windows 배포본. 현재 `renpy_project/game`의 소스·데이터·자산을 파일 바이트와 SHA-256으로 대조했습니다. 새 파일 29개, 수정 10개, 삭제 0개입니다.

캐시·테스트·저장·컴파일 결과(.rpyc/.pyc)·자동 생성 `script_version.txt`와 로그는 제품 파일 비교에서 제외합니다. 소스 UI의 네이티브 110개 사례·811개 assertion과 Lint 검증을 완료했습니다. 배포판은 사용자 요청으로 보류하며, 공식 챕터 QA 종료 단계와 독립 EXE 클릭 미검증 범위는 [0.3.0 검증 보고서](../tests/VERIFICATION_0.3.0.md)를 기준으로 확인합니다. 전체 해시는 [JSON 변경 기록](../tests/ui-refresh-changed-files-v030.json)에 있습니다.

## 연결 시스템

| 변경 | 경로 |
| --- | --- |
| 추가 | `renpy_project/game/systems/cg_system.rpy` |
| 추가 | `renpy_project/game/systems/phone_system.rpy` |
| 수정 | `renpy_project/game/systems/sd_event_system.rpy` |
| 수정 | `renpy_project/game/systems/state.rpy` |
| 수정 | `renpy_project/game/systems/story_runtime.rpy` |

## 화면과 가독성

| 변경 | 경로 |
| --- | --- |
| 추가 | `renpy_project/game/screens_campus_gallery.rpy` |
| 추가 | `renpy_project/game/screens_campus_main.rpy` |
| 수정 | `renpy_project/game/screens_character_profile.rpy` |
| 추가 | `renpy_project/game/screens_phone.rpy` |
| 수정 | `renpy_project/game/screens_story_stage.rpy` |
| 추가 | `renpy_project/game/zz_ui_readability.rpy` |

## 기존 공식 대본의 연출 연결

| 변경 | 경로 |
| --- | --- |
| 수정 | `renpy_project/game/routes/chapter01_official.rpy` |
| 수정 | `renpy_project/game/routes/chapter02_official.rpy` |
| 수정 | `renpy_project/game/routes/chapter03_official.rpy` |

## 등록 데이터

| 변경 | 경로 |
| --- | --- |
| 추가 | `renpy_project/game/data/cg_registry.json` |
| 추가 | `renpy_project/game/data/cg_registry.rpy` |
| 추가 | `renpy_project/game/data/phone_ui.json` |
| 수정 | `renpy_project/game/data/sd_legacy_text_map.json` |

## UI 자산

| 변경 | 경로 |
| --- | --- |
| 추가 | `renpy_project/game/images/cg/README.txt` |
| 추가 | `renpy_project/game/images/ui/campus_main/main_wash.svg` |
| 추가 | `renpy_project/game/images/ui/campus_main/menu_hover.svg` |
| 추가 | `renpy_project/game/images/ui/campus_main/menu_panel.svg` |
| 추가 | `renpy_project/game/images/ui/phone/avatar_darim.svg` |
| 추가 | `renpy_project/game/images/ui/phone/avatar_group.svg` |
| 추가 | `renpy_project/game/images/ui/phone/avatar_lumi.svg` |
| 추가 | `renpy_project/game/images/ui/phone/avatar_mc.svg` |
| 추가 | `renpy_project/game/images/ui/phone/avatar_omu.svg` |
| 추가 | `renpy_project/game/images/ui/phone/avatar_roman.svg` |
| 추가 | `renpy_project/game/images/ui/phone/avatar_sia.svg` |
| 추가 | `renpy_project/game/images/ui/phone/avatar_system.svg` |
| 추가 | `renpy_project/game/images/ui/phone/hover.svg` |
| 추가 | `renpy_project/game/images/ui/phone/incoming.svg` |
| 추가 | `renpy_project/game/images/ui/phone/mask.svg` |
| 추가 | `renpy_project/game/images/ui/phone/outgoing.svg` |
| 추가 | `renpy_project/game/images/ui/phone/panel.svg` |
| 추가 | `renpy_project/game/images/ui/phone/reply.svg` |
| 추가 | `renpy_project/game/images/ui/phone/send.svg` |
| 추가 | `renpy_project/game/images/ui/phone/shell.svg` |

## 설정

| 변경 | 경로 |
| --- | --- |
| 수정 | `renpy_project/game/options.rpy` |

## 검증·도구 파일

아래 파일은 이번 UI 연결과 검증에 사용하는 현재 개발 파일입니다. 기준 Windows ZIP에는 테스트와 루트 도구가 원래 제외되어 있으므로, 그 ZIP에 없다는 이유만으로 새 파일이라고 판정하지 않습니다. 현재 크기·해시를 JSON에 별도로 남깁니다.

| 경로 | 역할 |
| --- | --- |
| `renpy_project/game/tests/campus_ui.rpy` | 새 메인·프로필·갤러리·폰 UI와 저장 상태 네이티브 검증 |
| `renpy_project/game/tests/chapters_integration.rpy` | 공식 CH01~03 경로·LD 획득·일반/감정/SD/LD 저장 복원 검증 |
| `renpy_project/game/tests/integration.rpy` | 메뉴명 변경을 반영한 기존 회귀 검증 |
| `tools/integrate_campus_ui.py` | 기존 대사와 분기를 보존하는 LD/폰 연출 연결 |
| `tools/prepare_ui_qa.py` | 원본 저장과 격리된 D드라이브 QA 복사본 준비 |
| `tools/Run-Checks.ps1` | QA 복사본의 Lint 및 네이티브 검증 실행 |
| `tools/Run-UIRegression.ps1` | 버전별 로그로 기존 UI 회귀 검증 실행 |
| `tools/Build-Windows.ps1` | QA 복사본에서 D드라이브 Windows ZIP 빌드 |
| `tools/verify_build.py` | 현재 버전의 배포 구조·오염 여부 점검 |
| `tools/verify_packaged_source.py` | 현재 소스·데이터·자산과 배포본 바이트 대조 |
| `tools/write_ui_verification_report.py` | 최종 근거를 엄격히 검증한 소스 UI 보고서 생성; 배포 보류 모드 지원 |

최종 캐릭터·메인·LD·SD 원화는 추가하지 않았습니다. 신규 자산은 UI 프레임·마스크·패널 등 코드형 SVG입니다. 기존 저장 파일과 테스트용 저장은 변경 파일 목록에 포함하지 않습니다.
