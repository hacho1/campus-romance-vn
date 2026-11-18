# CH06 축제 일러스트 연결 · 0.6.6-test

- 작업 위치: `D:\CampusRomance_VN\renpy_project`
- 공개 버전: **0.6.6-test / build 2026111201**, 2026-11-12.
- 업데이트 주소: https://campus-romance-playtest.naiski.chatgpt.site/
- 백업: `D:\CampusRomance_VN\backups\ch06_cg_revision_20261111_233943`

## 반영 내용

기존 다림 CH06 축제 이벤트가 이미 있어 새 원고로 교체하지 않았다. 다림 3개 소장면, 다른 인물의 대사·선택지·조건·5/10점 정책은 그대로 유지했다.

첨부된 실제 그림을 기준으로 개장 SD 1장, 로만/시아/오므 각 2장을 연결했다. 시아 그림의 추가 중복 2장은 제외했다. 일곱 장 모두 2048×1152 PNG 원본과 게임 파일, 배포 파일의 바이트가 동일하다. 새 그림을 생성하거나 자르거나 확대 보정하지 않았다.

각 이미지의 정확한 시작/종료 대사는 [구간표](CH06_SCRIPT_066.md)에 있다. 0.35초 디졸브를 설정했으며 구간 종료 후 기존 배경과 스탠딩으로 복귀한다. 오므의 마지막 대사가 CH04 조건에 따라 생략되는 경우에도 다음 공통 장면 전에 그림을 닫는다. CH06의 다른 SD 제작 지시는 실행하지 않고 기존 스탠딩으로 진행한다.

갤러리는 ROMAN/SIA/OMU에 한 항목씩 추가했다. 각 항목 안에서 본 컷만 전환 가능하고 아직 보지 않은 컷은 열리지 않는다. 개장 SD는 SPECIAL에 등록했다. 기존 CG 37개와 SD 이벤트 36개 데이터, 기존 이미지 360개는 보존했다.

CH06 대면 장소 34곳의 기존 스탠딩을 확인했다. CH07은 23개 장소 전환 중 대면 12곳/히로인 대사 289개가 모두 연결돼 있었다. 주인공 혼자 있는 장면과 전화 대사 109개에는 스탠딩을 추가하지 않았다. 고정 크기와 발화자 밝기, 히로인/라이벌 그룹 전환은 기존 동작을 사용한다.

## 변경 파일

- `game/routes/chapter06_official.rpy`: 새 표시 구간 14블록만 추가. 이 블록을 제거하면 변경 전 소스와 정확히 같다.
- `game/data/cg_registry.json`: LD 6컷, 갤러리 3항목.
- `game/data/sd_events.json`: 개장 SD 이벤트 1개.
- `game/data/phone_ui.json`: CH06 대본 줄 위치 변경에 맞춘 timeline_positions만 갱신.
- `game/options.rpy`: 0.6.6-test 버전.
- `game/images/sd_events/ch06_festival_opening_01.png`
- `game/images/cg/ch06/festival_roman_01.png`, `festival_roman_02.png`
- `game/images/cg/ch06/festival_sia_01.png`, `festival_sia_02.png`
- `game/images/cg/ch06/festival_omu_01.png`, `festival_omu_02.png`
- `tools/install_ch06_festival_art_066.py`: 원본 그림 설치/등록/해시 기록.
- `tools/apply_ch06_visual_revision.py`, `tools/import_ch06_ch07.py`: 재가져오기 후 구간 재적용.

상대 경로의 game은 renpy_project 아래, tools는 D:\CampusRomance_VN 아래다. CH07과 다른 루트 소스 40개는 바이트 단위로 그대로다.

## 검증

- 실제 Ren'Py 8.5.3: **14케이스·38검증 통과**. 구 공개 0.6.5 기준 저장 생성도 별도 1케이스·2검증 통과.
- 개장 SD의 첫/마지막 대사 및 다섯 스탠딩 복구, 6개 CG 구간, CG 중간 저장/불러오기 확인.
- 다림만 선택 시 기존 3개 소장면 후 공통 SC05 복귀, 하린만 선택 시 다른 개인 이벤트를 실행하지 않음 확인.
- CH07 다섯 인물의 첫 대면 스탠딩 실행 확인. CH07 전체 문장 연결은 별도 소스 감사로 확인.
- 갤러리 한 항목/본 컷만 열기와 그림 누락 시 기존 스탠딩 유지 확인.
- 공식 Lint: 오류 없음. 26,257 대사 블록, 102 메뉴, 65 스크린.
- 검증 후보·게임 원본·배포 snapshot **506파일 해시 일치**. 실제 사용자 저장 14개의 해시·수정 시각 불변.
- 실제 production 런처 CLI qa:false, 고정 RSA 서명, 공개 대표 **20파일·22,714,828바이트 HTTPS 다운로드** 확인.

실행 테스트는 포커스와 마우스를 건드리지 않는 SDL dummy/software 모드로 수행했다. 대사 경계 검증에서는 애니메이션을 끄고 상태를 확인했으며 0.35초 전환 설정은 소스에서 확인했다. GPU/실제 창 전체 플레이 검증으로 확대 해석하지 않는다.

시아 두 번째 그림의 겹친 윤곽은 제공된 원본에도 있다. 전환 후 정지 화면과 원본을 대조했으며 이번 요청에서는 원본 그대로 유지했다. 그림을 교정하려면 추후 해당 원본을 교체하면 된다.

## 공개 배포

기존 런처의 **업데이트 확인 → 설치·업데이트**로 받는다. 런처 EXE나 사이트 재설치는 필요 없다. 사이트/런처 공지는 활성 manifest에서 읽는다. 사용자의 실제 게임 설치는 테스트 목적으로 변경하지 않았다.

- 전체: 1,883파일 / 610,746,995바이트 / 1,881고유 조각.
- 새 업로드: 83조각 / 25,439,146바이트, 기존 1,798조각 재사용.
- manifest SHA256: `edbcda4a52eebd4c06bfd7f4fe77f8207970322bb5784cffc837ad8220aad46c`
- 서명·활성화 영수증: `launcher_publish/r2_upload_result.json`
- 다음 업데이트의 저장 위치 호환용 공개 RPYC 85개: `launcher_publish/compiled_seeds/2026111201`

## 근거

- `tests/ch06_visual_066/RESULT.json`, `snapshot_source_audit.json`, `asset_audit.json`
- `tests/ch06_visual_066/CH07_STANDING_AUDIT.md`, `CH06_SCRIPT_AUDIT.json`
- `tests/ch06_visual_066/screenshots/current/`
- `tests/ch06_visual_066_public/RESULT.json`
