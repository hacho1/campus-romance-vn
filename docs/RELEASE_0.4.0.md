# 0.4.0 릴리스·수정 가이드

**공개 버전:** 0.4.0 / **build:** 2026110803  
**공개 주소:** <https://campus-romance-playtest.naiski.chatgpt.site/>

2026-11-08 공개 게시와 사후 검증을 완료했습니다. 기존 바탕화면 런처에서 **업데이트 확인 → 설치·업데이트**로 받습니다.

## 추가·변경 내용

- 공통 루트를 CH06·CH07까지 연결했습니다. 기존 CH05 끝에서 CH06으로 이어집니다.
- CH06에 사용자가 추가한 다림 원고를 반영하고, 중복된 시아 장면은 한 번만 실행하도록 정리했습니다.
- CH07에서는 호감도·신뢰도와 관계없이 다섯 사람 중 한 명을 선택할 수 있습니다. 확정 전에는 취소하고 다시 고를 수 있습니다.
- 로만 개별 루트 R01–R06의 해피·배드 엔딩과 해피 이후 시크릿 이야기를 추가했습니다. 다른 네 사람의 개별 루트는 아직 제작 중이며 다음 업데이트 안내를 표시합니다.
- 로만 해피 엔딩을 완료하면 엔딩 화면에서 시크릿 애프터를 다시 읽을 수 있습니다. 본편 종료 직후 강제로 진입하지 않습니다.
- 실제로 추가한 CG는 첨부 그림을 사용하는 `ending/roman_secret`입니다. 신규 스탠딩·SD·다른 CG 후보는 원고 행을 붙인 콘티 주석으로만 보존했습니다.
- 스토어의 내용 범위를 CH01–07 공통 루트와 로만 R01–R06으로 갱신했습니다. 시크릿 CG는 게임 안의 해금용이며 웹에 노출하지 않습니다.

## 확인된 결과

| 항목 | 현재 결과·기록 |
| --- | --- |
| 신규 대사 정확 대조 | **6,308개 PASS**. `tests/story_release_20261108/manuscript_comparison.json` |
| 스토어 내용·반응형·다운로드 | **36 PASS / 0 FAIL**. `tests/story_release_20261108/storefront/report.json` |
| 네이티브 Lint·공통/로만 분기·시크릿 | **PASS**. CH06 다섯 개인 분기·공통 복귀, CH07 저점수 선택·취소, 로만 36개 선택지와 해피·배드 판정, 시크릿 진입 제한·실제 CG·저장/불러오기·엔딩 화면 Replay·갤러리 해금 검증 |
| 이전 CH05 저장에서 이어 하기 | **PASS**. 이전 공개판에서 만든 저장을 새 코드로 불러와 이름·기존 수치·선택·파트너를 유지하고 CH06→CH07까지 진행 |
| R2 업로드·0.4.0 활성화 | **PASS**. 신규 58조각/3,883,690바이트 업로드, 기존 1,754조각 재사용. 개인 저장·개인키 제외 |
| 공개 HTTPS 사후 검사 | **PASS**. production CLI에서 0.4.0/0803·1,814파일 확인, raw manifest·고정 서명·CH06/R06/첨부 CG 실제 다운로드와 SHA256 검증 |
| 실제 공개 스토어 | **24 PASS / 0 FAIL**. 버전·공지 4개·런처 EXE 해시 일치, PC/모바일 3종과 콘솔 정상 |

공개 manifest: **0.4.0 / 2026110803**, SHA256 `1d08f93a38acbf74e0b06412980c26648ba223e9060269ad6c77d091fc2f165f`  
Site: **version 3**, 기존 공개 주소와 접근 범위 유지. Launcher **1.1**은 유지하고 공지·게임 파일을 갱신했습니다.  
검증 및 게시 영수증: [통합 QA 보고서](../tests/story_release_20261108/README.md), [검증 결과](../tests/story_release_20261108/RESULT.json), [게시 기록](../tests/story_release_20261108/release_0803/publication_receipt.json).

구버전 저장은 스크립트가 확장되면서 같은 CH05 장면의 앞 대사로 복귀할 수 있습니다. 수치와 선택 기록 보존 및 새 챕터 진입을 실제로 확인했습니다. 실제 사용자 `.save` 8개는 이전 기록과 SHA256이 같습니다. `persistent`는 작업 전부터 실행 중이던 게임의 종료 시각과 일치하는 변경이 있어 과거 해시만으로 불변을 판정하지 않았으며 현재 파일을 그대로 보존했습니다. 전체 게임의 공개 HTTPS 신규 설치나 사용자의 실제 저장을 덮어쓰는 설치는 실행하지 않았습니다.

## 수정할 위치

기준 원본은 `D:\CampusRomance_VN\renpy_project`입니다. 원고 행과 `SOURCE`/`CONTI` 주석으로 수정 위치를 찾습니다.

- 공통 루트: `game/routes/chapter06_official.rpy`, `chapter07_official.rpy`
- 로만 본편: `game/routes/roman_r01.rpy`부터 `roman_r06.rpy`
- 로만 시크릿: `game/routes/roman_secret.rpy`

연결·기록·배포를 위해 바꾼 파일은 다음과 같습니다. 경로는 기준 원본의 `game` 아래입니다.

| 파일 | 역할 |
| --- | --- |
| `routes/chapter05_official.rpy`, `routes/roman.rpy` | 기존 챕터·로만 진입점과 새 대본 연결 |
| `systems/story_draft_runtime.rpy` | 신규 대본 공용 배경·BGM·루트·엔딩 처리 |
| `systems/story_runtime.rpy` | 하린 이름의 기존 저장 키 별칭 유지 |
| `systems/cg_system.rpy` | 시크릿 진입 조건과 완료 후 앨범 해금 |
| `screens_story_stage.rpy`, `screens_ending_diary.rpy` | CH06/07 이어 하기와 시크릿 Replay |
| `data/routes.json`, `data/endings.json`, `data/cg_registry.json`, `data/secret_notes.json` | 로만 루트·엔딩·CG·비밀 메모 등록 |
| `options.rpy` | 0.4.0 버전 설정; 기존 저장 경로 유지 |
| `images/cg/endings/roman_secret.png` | 사용자 첨부 원본 그대로 보관 |

제품 페이지 원본은 `D:\CampusRomance_VN\launcher_storefront_source`, 배포 파일은 `D:\CampusRomance_VN\launcher_publish\feed`입니다. 변경 전 코드 백업은 `D:\CampusRomance_VN\backups\story_ch06_ch07_roman_20261108`에 있습니다.

원고를 수정한 경우 해당 import 도구와 생성 코드의 일치 여부를 확인한 뒤 다시 대조·통합 검사합니다. 스탠딩·일러스트를 추가할 때는 아래 가이드의 콘티 위치를 사용합니다.

- [CH06–CH07 대사·콘티 가이드](CH06_CH07_STORYBOARD.md)
- [로만 R01–R03 대사·콘티 가이드](ROMAN_R01_R03_STORYBOARD.md)
- [로만 R04–R06·시크릿 콘티 가이드](ROMAN_R04_R06_CONTI_GUIDE.md)
- [로만 후반 조건·엔딩 판정 구현 설명](ROMAN_R04_R06_IMPLEMENTATION.md)
- [PC 런처 준비·서명·증분 게시 절차](LAUNCHER_UPDATE_WORKFLOW.md)

게임 내용만 바뀌면 새 build로 payload를 준비하고 서명한 뒤 R2에 증분 게시합니다. 제품 페이지·런처·Worker 코드가 바뀔 때만 기존 Site를 다시 배포합니다. 공개한 `2026110803`을 이후 수정 배포에서 재사용하지 않습니다.
