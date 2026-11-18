# CH07 일러스트·엔딩 이름·개별 루트 스탠딩 — 0.6.11-test

원본 프로젝트: `D:\CampusRomance_VN\renpy_project`.
백업: `D:\CampusRomance_VN\backups\ch07_standing_20261115_210937`.

## CH07의 새 그림

| 그림 | 표시 시작 | 마지막 표시 대사 |
| --- | --- | --- |
| 카페의 다섯 사람 · SD | 카페 문을 열자 익숙한 사람들이 보였다. | 시아 「아 진짜ㅋㅋㅋ」 · SC03의 해당 대사 |
| 시아 · LD | 시아의 펜이 멈췄다. | 그런데 이번에는 평소처럼 크게 웃지는 않았다. |
| 로만 · LD | 우리는 창가에 나란히 앉았다. | 그렇게 새로운 이야기가 시작됐다. |
| 다림 · LD | 다림 「후후. 재미있었어요.」 | 그런 시간을 앞으로도 더 보내고 싶었다. |
| 오므 · LD | 우리는 벤치에 앉았다. | 그런데 조금도 어색하지 않았다. |
| 하린 · LD | 하린 선배는 새로 만드는 모형을 보여줬다. | 하린 「그런 것 같아요.」 |

시작 대사가 나오는 순간 그림을 표시하고, 마지막 대사까지 유지한 다음 기존 배경과 스탠딩으로 복귀한다. 전환은 0.35초 디졸브다. 제공 PNG의 바이트는 그대로 보존한다. 다림·오므 그림은 원본이1024×572, 나머지는2048×1152이며 `contain`으로 원래 화면비를 유지한다.

첫 그림은 완성형 SD 이벤트로 SPECIAL에, 나머지는 각 인물의 LD 갤러리에 등록한다. 대사·선택지·호감도는 바꾸지 않는다.

## 엔딩 이름

실제 해피·배드 완료 후 기존 대사창에서 `해피엔딩 <등록된 제목>` 또는 `배드엔딩 <등록된 제목>`을 표시한다. 사용자가 다음 입력을 하면 원래 엔딩 목록 또는 테스트 종료로 이어진다. 시크릿 제목이나 실제 해금 판정은 변경하지 않는다.

`game/systems/ending_result_dialogue.rpy`는 기존 ENDINGS 자료를 읽는 표시 전용 기능이다. 미해금·미구현·시크릿·없는 ID에는 결말 문구를 만들지 않는다. 열 군데 완료 경로의 삽입점은 `tools/apply_ending_result_dialogues.py`로 재적용할 수 있다.

## 개별 루트 스탠딩·제작 대기 구간

기존 스탠딩과 표정 자료를 사용해 개인 루트의 대면 구간을 배치한다. 전화·메시지·주인공 단독·일러스트 표시 중에는 부적절한 스탠딩을 띄우지 않는다. 대면 인원이 여럿이면 같은 장면의 배치를 유지하며 기존 발화자 강조를 사용한다.

로만 `roman_obsess_01`, `roman_obsess_02`는 원고에서 신규 제작을 요구하는 표정이므로 기존 표정을 대신 넣지 않는다. 미제공 특수 의상도 제작 대기 구간으로 구분한다. 앞으로 CG를 넣을 위치와 원문 행·씬·이미지 ID는 [제작 구간 목록](PRIVATE_ROUTE_ART_SLOTS.md)에 별도로 기록한다. 일반적인 미제공 CG 예정 구간에서는 기존 스탠딩 대화를 유지하고, 실제 CG가 표시되면 숨긴다.

현재 문장 위치를 쓰는 스탠딩 계획은 대사 편집 후 반드시 마지막에 재생성한다. 원문 파일이 없는 공개 RPYC 게임에서도 동작해야 하며 원본 `.rpy` 파일의 존재를 실행 조건으로 삼지 않는다.

이번 계획은 본편30개·시크릿5개·하린 배드 별도 파일, 총36파일의24,359개 대사/선택지 위치를 다룬다. 제작 예정 위치49개와 로만의 신규 표정 대기134개 위치를 구분했다. 이는 정적 구간 목록의 범위이며 모든 대사를 자동 재생해 검증했다는 의미가 아니다.

재생성 순서는 `tools/refresh_route_presentation_0611.py`로 묶었다. 대본 가져오기·CH07그림 재적용 후 이 도구를 마지막에 실행하면 엔딩 이름 호출, 휴대폰 위치, 스탠딩 계획 순서로 갱신한다.

## 수정·재생성 파일

- `game/routes/chapter07_official.rpy`: 새 그림 구간12블록.
- `game/routes/roman_r06.rpy`, `game/systems/{sia,omu,darim,harin}_story_runtime.rpy`: 해피·배드 제목 표시 호출10곳.
- `game/systems/ending_result_dialogue.rpy`: 결말 제목 표시.
- `game/systems/private_route_standing.rpy`, `game/data/private_route_staging.json`: 개인 루트 구간 계획·표시.
- `game/data/cg_registry.json`, `game/data/sd_events.json`: 그림 등록.
- `game/data/phone_ui.json`: 변경된 대본 줄 위치 조회.
- `game/images/cg/ch07/`: 새 그림6장. 공통 SD도 이 폴더의 원본 파일을 SD 레지스트리로 연결한다.
- `game/options.rpy`: 버전.
- `tools/install_ch07_art_0611.py`, `apply_ch07_visual_revision.py`, `apply_ending_result_dialogues.py`, `build_private_route_staging.py`.
- `tools/import_ch06_ch07.py`: CH07 그림 재적용 연결.

## 검증 근거

- `tests/ch07_standing_0611/cg_source_audit.json`: 그림 표시 블록 제거 후 원문 동일성.
- `cg_asset_audit.json`, `cg_intervals.json`: 원본 그림·정확한 구간.
- `RESULT.json`, `docs/CH07_STANDING_QA_0.6.11.md`: 실제 네이티브 실행 범위와 한계.
- `tests/ch07_standing_0611_public/RESULT.json`: 실제 공개 파일·서명·사이트 검증.

실제 배포가 완료되면 아래에 활성화 정보를 기록한다. 기존 런처의 업데이트 피드를 사용한다.

## 실제 활성화 정보

- `0.6.11-test` / build `2026111501`, 2026-11-15.
- manifest SHA-256: `85aa039d147ea0f5e49c4cd039b7f93996277ba3e06081b93cc689cf47f85a20`.
- 전체1,907파일 / 642,419,775바이트. 새96조각 / 24,564,802바이트 업로드, 기존1,809조각 재사용.
- 실제 서명 피드 활성화 영수증: `launcher_publish/r2_upload_result.json`.
- 공개97RPYC를 `launcher_publish/compiled_seeds/2026111501`에 보존했다.
- 컴파일·Lint, 네이티브71케이스(69본검사+원문없는배포형2검사), 530입력소스/공개스냅샷 해시 일치. QA전후 실제53저장/persistent 기록의 바이트·수정시각 동일.
- 추후 대본 수정으로 스탠딩 좌표가 오래된 경우 배포 도구가 출처 SHA 불일치를 거부한다. 실제36파일 결합과 변조한 테스트 원고의 거부를 `publish_staging_guard.json`에서 확인했다. `refresh_route_presentation_0611.py` 실행 및 재검증 후 배포한다.
- 실제 공개 검증 PASS: 고정RSA·정상TLS·productionCLI `qa:false`, 사이트 버전/빌드/공지5개 일치. 대표15파일 / 21,057,624바이트를 HTTPS로 재구성해 검증했다. 여섯 PNG 원본 동일, 기존371이미지·메모·엔딩·점수·해금 자료 불변. 기존 원고95개 중88개는 그대로이며 나머지7개도 승인된 표시 삽입만 제거하면 백업과 일치한다.
