# 0.6.9-test — 하린 루트 및 오므 배드엔딩 개정

## 원고와 백업

- 원본 8개: `HARIN_OMU_SOURCE_IMPORT_0.6.9.json`에 실제 발견 경로·D 사본·SHA-256 기록.
- 추가 하린 배드 원고: 사용자가 대화에서 직접 제공한 SC05-B~08-B 및 에필로그. `design_docs/story_sources/harin_h06_bad.txt`, 출처 기록은 `tests/harin_omu_069/harin_bad_source_record.json`.
- 변경 전 전체 프로젝트: `D:\CampusRomance_VN\backups\harin_omu_story_20261112_200841`.

## 반영 범위

- 하린 H01~H06·해피 「미완성이라서 아름다운」·배드 「완벽한 타인」·시크릿 「오늘만큼은 고양이랍니다♡」.
- 기존 `lumi` 인물/라우트/엔딩 ID 유지. 신규 원고의 `harin_*` 기억 플래그와 `harin_h01`~`harin_h06` 라벨은 별도로 보관.
- 테스트 챕터 선택에 하린 7개 진입점 추가. H01부터 시작하면 같은 테스트 안에서 H06까지 선택·호감도·메시지가 이어짐.
- CH07 하린 선택 시 H01 연결. 이전 업데이트의 공통 루트 완료 화면에서도 하린 이어 읽기 가능.
- 엔딩 화면 시크릿 버튼을 다섯 명에 맞게 배치. 일반 플레이에서는 각 인물의 해피엔딩이 필요함.
- 오므는 개정 원고가 명시한 O04 SC04~08, O05 SC06~08, O06 SC04·배드·에필로그만 교체. O01~O03·기존 O06 해피·시크릿 유지.
- 오므 기존 `omu_bad` 엔딩 ID·선택 ID·씬 라벨 보존, 표시 제목은 「흐려진 나의 시선」. 새 배드는 사고·사별 대신 관계와 기억의 왜곡을 다룸.

## 호감도·선택 기록

모든 실제 선택 보상은 5/10점 단위이며, 새 신뢰도는 만들지 않았다. 하린은 공통 루트의 본인 선택과 자신의 H01~H06 선택만 판정에 사용한다. 핵심 부정 행동이 H04·H05·H06에 반복되고 미해결인 경우에만 배드로 이어진다. 혼합 선택은 원고에 있는 H06 SC05-H 회복 대화를 완료해야 해피를 기록한다.

오므는 O04~O06의 실제 개정 행동을 구분해 기록한다. 이전 버전의 같은 선택 ID·이전 플래그를 새로 생긴 기억 왜곡 사건으로 추정하지 않는다. 기존 획득 기록은 삭제하지 않는다.

## 대사와 재생성

- 하린: `tools/import_harin_route.py` — 원문 SHA·행 분류·대사 동일성 감사.
- 오므: `tools/import_omu_bad_revision.py` — 기존 세 씬 파일의 지정 구간에 개정 원고를 적용하는 오버레이. 기본 오므 importer에도 오버레이 연결.
- 공통 연결: `tools/integrate_harin_069.py`.
- 마지막에 `tools/import_roman_first.py --phone-cues` 실행. 이 명령은 대사를 바꾸지 않고 새 SOURCE 태그·날짜·시간·시점 조회를 재생성한다.
- `tools/phone_harin_omu_069.py`: 하린 H01~H06/HSECRET 기본 시각·날짜와 오므 개정 출처 매핑. 정확한 시각이 없는 밤/저녁은 문서화된 연출 기본값을 사용한다.

하린 importer를 다시 실행하면 전화 연출문도 초기화되므로 항상 마지막에 phone-cues를 재생성한다. 사용자 원본 C 파일에는 쓰지 않는다.

## 이미지

이번 반영은 대사·배경·콘티 우선 단계다. 신규 스탠딩/CG/SD 이미지를 만들지 않았고 개인 루트의 자동 스탠딩 배치는 꺼 두었다. 원고에 있는 이미지 ID·포즈·표정 방향은 SOURCE 주석으로 남아 있다. 이미지가 없는 장면은 기존 배경에서 계속 읽을 수 있다.

하린 배드 CG `harin_h06_bad_perfect_stranger` 및 하린 시크릿 고양이 코스프레 CG는 미제공 상태다. 오므의 새 배드에도 이전 사고·사별 그림을 대신 표시하지 않는다.

## 실행 검증·온라인 배포

실제 결과는 `tests/harin_omu_069/RESULT.json`과 `tests/harin_omu_069_public/RESULT.json`에 기록한다. 온라인 활성화 전에는 완료로 간주하지 않는다. 런처 바이너리는 변경하지 않고 기존 서명 업데이트 피드의 게임 파일·공지로 배포한다. 실행 중인 게임을 종료한 뒤 런처에서 업데이트를 적용한다.

## 수정 파일 목록

프로젝트 소스·데이터 30개 변경의 전체 목록은 `tests/harin_omu_069/changed_files.json`에 있다. 주요 파일:

- `game/routes/harin_h01.rpy`~`harin_h06.rpy`, `harin_h06_bad.rpy`, `harin_secret.rpy`, `lumi.rpy`
- `game/routes/omu_o04.rpy`~`omu_o06.rpy`
- `game/systems/harin_story_runtime.rpy`, `harin_relationship_policy.rpy`
- `game/systems/omu_story_runtime.rpy`, `omu_relationship_policy.rpy`
- `game/systems/heart_system.rpy`, `phone_timeline.rpy`, `story_draft_runtime.rpy`, `test_chapters.rpy`
- `game/screens_test_chapters.rpy`, `screens_ending_diary.rpy`, `screens_story_stage.rpy`
- `game/data/harin_relationship_choices.json`, `omu_relationship_choices.json`, `endings.json`, `routes.json`, `secret_notes.json`, `phone_ui.json`
- `game/options.rpy`

그 밖에 위 재생성 도구·원고 사본·QA 산출물·이 문서만 D드라이브에 추가했다. 이미지·아이콘·음악·다른 인물의 루트 원고는 수정하지 않았다.

### 활성화 기록

- 게임 `0.6.9-test`, build `2026111204`
- 실제 R2 활성화 완료: `launcher_publish/r2_upload_result.json`
- SHA-256 `94d571be40bc63f13edfdcb112579e494c86f5aeedf79f823a83583c2e00b6d8`
- 1,894파일 / 611,291,247바이트. 새 조각90개 / 3,889,301바이트, 기존1,802개 재사용.
- 네이티브15케이스·74검증, 컴파일·Lint 통과. 최종517소스의 게임 원본·QA 후보·공개 스냅샷 동일성 확인. 실제39저장·persistent 기록은 검사 전후 내용과 수정시각 동일.
- 활성95RPYC 원본을 `launcher_publish/compiled_seeds/2026111204`에 보존했다.
- 공개 production CLI(`qa:false`), 고정 RSA·TLS, 대표37파일 5,589,582바이트 실제 HTTPS 다운로드 검증 통과. 기존367이미지 불변. 실제 사이트에서 0.6.9 버전·하린/오므 공지 표시 확인.
