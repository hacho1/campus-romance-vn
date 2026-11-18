# 《우리 사이, 그 이상》 0.5.0-test 작업 기록

기준일: 2026-11-08. 프로젝트: `D:\CampusRomance_VN\renpy_project`. **0.5.0-test / build `2026110805` 공개 게시와 사후 검증을 완료했다.** 기존 개발 사이트 주소는 <https://campus-romance-playtest.naiski.chatgpt.site/>를 유지한다. 게임을 종료하고 기존 런처에서 **업데이트 확인 → 설치·업데이트**로 받는다. 런처 EXE와 Site 코드를 다시 배포하지 않고 게임 파일·버전·공지만 갱신했다.

## 사용자 요청별 구현

아래 경로는 `D:\CampusRomance_VN\renpy_project\game` 기준이다. 원고 대사와 선택 문구를 고치기 위한 작업이 아니라 UI·시간·연출·표시를 개선하는 작업이다.

| 번호 | 요청 | 구현 및 위치 |
| --- | --- | --- |
| 1 | 테스트 챕터 선택 | 메인 메뉴 `챕터 선택 · 테스트`. 공통 CH01–07·로만 R01–R06·시크릿 총14개 진입점. `systems/test_chapters.rpy`, `screens_test_chapters.rpy`, `screens_campus_main.rpy`. Replay 컨텍스트에 수집 상태를 복제하여 실제 세이브·앨범·엔딩 수집에 반영하지 않으며 선택한 구간 끝에서 복귀한다. |
| 2 | 휴대폰 오전·오후·밤, 날짜·다음날 구분 | OS 시계 대신 원고의 장면 시간과 이야기 날짜를 사용한다. 메시지 작성 당시 시각을 보존하고 오늘·어제·해당 날짜 구분자를 표시한다. `systems/phone_timeline.rpy`, `data/phone_ui.json`, `screens_phone.rpy`, 각 route의 시간 cue. |
| 3 | 휴대폰 확대 | 줌0.74→0.88, 약18.9% 확대. 폰을 보는 독백은 하단 전용 대사창으로 옮겨 겹침을 피한다. 채팅 목록·선택 답장·수동 알림 게이트 유지. `screens_phone.rpy`. |
| 4 | CC대 학생들 헤더 중앙 정렬 | 제목 뒤 종이 배경을 정리하고 제목·`만난 사람들!` 버튼을 상단 탭 중앙 y=98에 맞춘다. `screens_character_profile.rpy`. |
| 5 | 시크릿 CG 갤러리 추가·선명도·크기 | 동일 ID `ending/roman_secret`를 ROMAN·ENDING에서 공유한다. 시크릿 완주 기록이 있는 이전 저장의 수집도 복구한다. 원본1344×768을 보존하고 GPT 보정본1672×941을3840×2160으로 규격화하여 전체 프레임을 표시한다. `systems/cg_system.rpy`, `data/cg_registry.json`, `images/cg/endings/roman_secret_hd.png`, `tools/register_roman_release.py`. |
| 6 | GPT 배경 제작 | 작은 서점·저녁 정원/연못·게임 체험 부스·로만의 방, 인물 없는 새 배경4장1920×1080. `images/backgrounds/refresh_20261108/`, `systems/story_draft_runtime.rpy` 장소 매핑. |
| 7 | 음악·효과음 제작 | 원본 작곡·악기 합성 BGM2곡과 시작/실패/클리어/심장 박동 SFX4개. `audio/generated_refresh/`, `data/audio.json`, `systems/refresh_audio.rpy`. 원고 cue 연결은 연출 후처리 도구가 담당한다. |
| 8 | 회상 장면 노란 톤 구분 | 옅은 노란 톤과 회상 배지. CH02·로만 R01/R04·CH06 하린 회상에 cue 연결. 폰을 열면 자체 시점 배지만 보여 중복을 숨긴다. `systems/story_presentation.rpy`, route cue, `tools/apply_presentation_cues.py`. |
| 9 | 히로인 시점 휴대폰 좌우 | 로만 POV에서 로만의 메시지는 오른쪽, 주인공은 왼쪽. 연락 상대 이름·프로필·읽지 않음 처리도 시점에 맞추며 새 장면에서 주인공 시점으로 돌아간다. `systems/phone_timeline.rpy`, `systems/phone_system.rpy`, `screens_phone.rpy`, 원고 POV cue. |
| 10 | 신뢰 표시 대신 빨간/검은 하트 | 프로필·선택 알림에 빨간 해피 호감도와 검은 배드 수치를0–100으로 표시한다. 기존 신뢰 값은 저장 호환을 위해 내부 보존한다. 로만의 명시 지원/위험 카운터를 연결하고 다른4인의 미작성 배드 조건을 임의로 만들지 않는다. `systems/heart_system.rpy`, `systems/state.rpy`, `systems/story_runtime.rpy`, `screens_character_profile.rpy`, `images/ui/hearts/`. |

## 변경 파일 그룹과 수정 가이드

- 챕터·연출: 새 테스트 챕터 화면/런타임, 회상 모듈, 기존 메인 메뉴 진입 버튼, 원고 route의 시간·시점·연출 cue, `tools/apply_presentation_cues.py`.
- 휴대폰: 화면·기록 런타임과 시간 데이터. [PHONE_TIMELINE_0.5.md](PHONE_TIMELINE_0.5.md).
- 관계 표시: 하트 런타임·선택 효과 연결·프로필/알림·SVG. [HEART_SYSTEM_0.5.md](HEART_SYSTEM_0.5.md).
- 시크릿 CG: 보정 이미지·레지스트리·갤러리 수집 호환·등록 도구. [CG_RESTORATION_0.5.md](CG_RESTORATION_0.5.md).
- 배경·음원: 새 파일10개, 장소/BGM 매핑과 재생 helper, 원본 생성 프롬프트·악보·MIDI·무손실 마스터·측정 결과. [REFRESH_ASSETS_0.5.md](REFRESH_ASSETS_0.5.md).
- 버전: `options.rpy`의 개발 후보 표기 `0.5.0-test`.

작업물·생성 원본·음악 마스터·백업은 `D:\CampusRomance_VN` 아래 보관한다. 사용자 원본 저장을 강제로 불러오거나 변경하지 않았다.

## 기존 저장 호환

- 기존 `affection`, `trust`, 원고 카운터·선택 로그·진행 플래그는 보존한다. 신뢰의 UI 표시를 없애도 해당 내부 데이터를 삭제하지 않는다.
- 하트 스키마가 없는 저장은 기존 값과 명시 카운터에서 한 번만 복원한다. 새 하트·스키마는 일반 저장/롤백 상태이며 영구 보상 장부에 중복 적립하지 않는다. 옛 슬롯 요약에 카운터 정보가 없으면 메뉴의 검은 하트를 `—`로 표시하고 강제 로드하지 않는다.
- 이전 폰 저장은 문장 위치를 이용해 현재 이야기 시각·시점을 보완한다. 기존 메시지 날짜와 정상 반복 문장은 보존한다. CH07 인사 중복 복구는 실제0.4.1 공개판 형식의 키도 추가 검증했다.
- 기존 시크릿 완주 기록이 있으면 CG 전용 수집 키가 없더라도 앨범을 연다. 해피만 완료한 상태는 시크릿 CG 잠금을 유지한다.
- 테스트 챕터 재생은 실제 플레이·수집 상태와 분리한다. 실제 저장·수집을 갱신하는 동작으로 사용하지 않는다.

## 확인된 검사

네이티브 기능 검사와 실제 공개 업데이트 검사를 구분한다. 상세 조건·로그는 각 QA 보고서를 기준으로 한다.

| 범위 | 현재 결과 |
| --- | --- |
| 챕터·Replay·갤러리·회상 | `tests/ui_refresh_050/visual_replay`: native22case/77assertions PASS. 14진입점, 수집 clone 격리, 구간 경계, 갤러리, 회상4곳·저장/불러오기 포함. 별도 `chapter_picker` 정적36항목 PASS. |
| 폰 | 순수/모의41항목 및 옛 저장3assertions PASS. `tests/ui_refresh_050/integration` native3case/13assertions PASS 보고. |
| 하트 | 모의23항목 PASS, native2case/13assertions PASS. 저장·롤백·구점수 복원·엔딩 판정 및 최종 채색 SVG 렌더 확인. |
| 헤더 | 최종 1280·1600 창 설정에서 제목·버튼·탭의 실제 잉크 중심 정렬 및 채색 하트 검수 PASS. 종이 배경 위치도 보정. |
| 배경·음원 | `tests/ui_refresh_050/assets_native`: native1case/11assertions PASS. 실제 SDK PCM 활성·SDL dummy 장치에서 BGM2개/SFX4개 디코드·재생 및 배경4개의 map/light/tint/1920×1080 확인. 관련15파일 source/fixture SHA 일치. |
| 원고·사용자 저장 보존 | 14개 route의 대사·선택 문장 11,269개 순서까지 동일. `docs/REFRESH_STORY_PARITY_0.5.json`. visual_replay 후보/최종 456파일 SHA 일치, 사용자 저장 두 경로의 54파일 SHA·수정시각 불변. |
| 최종 통합·Lint·배포 소스 일치 | PASS. 최종 Lint 오류·경고·traceback 0, 후보/제품 456파일 SHA 일치. payload 작성 중 원본 game script 73개 해시 불변, 개인 저장 제외·Windows ZIP 생성 없음. |
| 공개 업데이트·서명·청크·공지 확인 | PASS. production CLI의 `qa:false`, 0.5.0-test/0805·1,833파일·다운로드0 확인. 공개 raw manifest·고정 SHA query 서명 RSA, 대표4파일 실제 다운로드·조립 SHA 및 공지5개 문장 일치. |

한계: 네이티브 QA는 격리 SDK의 dummy/SW 렌더다. 실제 SDL 창 표면의 1280×720·1600×900 크기를 확인하고, 정상 가상 캔버스 PNG와 SDK 글자 측정·명시적 크기 축소로 검수했다. 해당 환경의 물리 RGB 프레임버퍼 PNG 오류는 제품 오류로 수정하지 않았으며 실제 GPU/사용자 전경 조작 검증으로 표시하지 않는다. 시크릿 보정 파일의3840×2160은 출력 규격이며 실제4K 원본 세부의 복원을 보장하지 않는다. 생성 보정은 미세한 선·디테일이 달라질 수 있고 원본은 그대로 남아 있다. 음악 서비스 요청은 크레딧 부족으로 접수0건이어서 승인된 로컬 원본 작곡·합성으로 완성했다. 클리핑·루프 경계와 SDK 재생은 확인했으나 사람의 실제 청취는 수행하지 않았다. 다른4인의 개별 배드 원고가 없으므로 배드 수치를 추정하지 않으며 추후 명시 카운터 API로 확장한다.

## 출시 확인

- 최종 헤더·SVG1280/1600 렌더: PASS
- 최종 통합·Lint·생산/배포 SHA 일치: PASS
- 실제 게시 버전 / build: `0.5.0-test / 2026110805`
- manifest SHA: `82280a90ef263d90769a569cb37a4853b0857a97f63c39498bfbb71a6a31e647`; 고정 서명·production CLI PASS
- 전체 관리 파일: 1,833개·551,395,805바이트. 기존 1,756조각 재사용, 신규75조각·25,749,961바이트 업로드.
- 대표 공개 파일: 하트 런타임 RPYC, 테스트 챕터 RPYC, 시크릿 HD CG, 새 dark BGM의 실제 청크8,617,403바이트 검증 PASS. 전체 게임 신규 설치는 하지 않았다.
- QA: [화면·Replay·회상·갤러리](../tests/ui_refresh_050/visual_replay/README.md), [폰·하트·구저장](../tests/ui_refresh_050/integration/README.md), [음원·배경](../tests/ui_refresh_050/assets_native/README.md), [공개 서명·파일·공지](../tests/ui_refresh_050/public_verify/README.md).
