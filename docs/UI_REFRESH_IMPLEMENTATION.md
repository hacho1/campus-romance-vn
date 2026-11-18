# 메인·휴대폰·갤러리·히로인 UI 개편 구현 기록

<!-- typography-audit-status -->
글꼴·텍스트 영역의 후속 점검은 진행 중입니다. 최종 실행 결과와 남은 범위는 [UI_TEXT_AUDIT.md](UI_TEXT_AUDIT.md)에 따로 기록합니다. 기존 0.3.0·0.2.0 보고서는 각 변경 전 시점의 검증 기록으로 보존합니다.
<!-- /typography-audit-status -->

기존 `D:\CampusRomance_VN\renpy_project`를 유지한 UI 개편입니다. 0.3.0 소스 UI 구현과 SDK 네이티브 110개 사례·811개 assertion 및 Lint 검증을 완료했습니다. **배포판은 사용자 요청으로 보류합니다.** 공식 챕터 QA가 PASSED 요약 뒤 종료 단계에서 멈춘 점과 독립 EXE 클릭 미검증 범위를 [VERIFICATION_0.3.0.md](../tests/VERIFICATION_0.3.0.md)에 구분합니다. 앞선 0.2.0 SD 전환의 [88개 사례·538개 assertion 기록](../tests/VERIFICATION_0.2.0.md)은 해당 버전의 기록으로 보존합니다.

## 설계 기준

현대 대학생 청춘 로맨스의 밝은 하늘·아이보리·화이트를 바탕으로 합니다. 메인·갤러리·휴대폰은 그림과 읽기를 위한 여백을 우선하고, 학생증 페이지에서만 종이·사진·스티커의 스크랩북 감성을 집중합니다. 대사와 선택은 Ren’Py가 계속 출력합니다. 캐릭터·주인공·최종 CG·SD 그림은 새로 생성하지 않았습니다.

글꼴 역할은 `game/typography.rpy`에 모았습니다. init -200의 `CAMPUS_BODY_FONT`는 Noto Sans KR, `CAMPUS_TITLE_FONT`는 Noto Serif KR, `CAMPUS_NOTE_FONT`는 작은 장식 손메모용 개구 Regular입니다. init 999는 공통 상속 스타일과 Bold 대체를 적용합니다. 원본 TTF와 OFL 고지는 `game/fonts/`에 있고 이전 Noto·Nanum 파일은 유지합니다. 긴 대사·답장은 생략하지 않으며, 공간이 제한된 방 제목·저장명만 전체 내용 툴팁·접근성 이름을 남겨 말줄임으로 표시합니다.

## 메인과 히로인 설명

`screens_campus_main.rpy`는 상단 중앙의 작은 손글씨 로고, 중앙 대표 그림, 하단 중앙 2열×3행의 여섯 메뉴를 제공합니다. 메뉴는 게임 시작·불러오기·갤러리·히로인 설명·엔딩·옵션입니다. 이어하기·종료는 작은 보조 항목이며 개발실은 개발 모드에서만 표시합니다.

메인 대표 그림은 LD-01과 같은 `images/cg/ld_01_main_visual.webp`(또는 PNG)를 사용합니다. 다섯 히로인이 꽃밭에 둥글게 누워 하늘을 보는 구도이며 주인공은 넣지 않습니다. 최종 그림이 없을 때는 기존 캠퍼스 배경과 작은 준비 문구를 표시합니다. 화면 방문은 `cg_unlock("ld_01")`에 연결합니다.

히로인 설명은 기존 `profiles` 화면을 사용합니다. 사진·이름·나이·학년·학과·MBTI·취향·소개·기존 한마디를 표시하고 앞뒷면, 다섯 캐릭터 전환, 사진·스티커·세 비밀 메모 상호작용과 잠금 조건을 유지합니다. 새 배경사나 비밀 설정을 만들지 않았습니다. [메인·히로인 가이드](UI_MAIN_HEROINES.md)와 [프로필 가이드](../README_profile_ui.md)를 따릅니다.

## 휴대폰

`screens_phone.rpy`와 `systems/phone_system.rpy`가 잠금화면·목록·대화방·답장 UI를 제공합니다. 기존 `story_chat(True, title=...)` 구간을 자동으로 연결하므로 본편의 고정 대사·답장을 유지합니다. 원형 프사·발신자·좌우 말풍선·시간·미읽음 배지와 스크롤을 표시합니다. 휴대폰의 네이티브 선택지만 자연스러운 답장 후보로 배치합니다. 개발 전용 세 답장 시연은 본편 선택지와 구분합니다.

대화와 보고 있는 화면은 현재 세이브의 상태이며 영구 수집과 합치지 않습니다. 구 저장에 남아 있는 메시지를 이관하는 `phone_migrate_after_load()`를 사용합니다. 날짜·시각은 연출용 기본값입니다. [휴대폰 가이드](PHONE_UI_GUIDE.md)에 API·프사·배경·저장 수정 방법을 설명합니다.

## LD와 갤러리

`data/cg_registry.json`, `systems/cg_system.rpy`, `screens_campus_gallery.rpy`가 LD 표시와 갤러리를 담당합니다. 탭은 COMMON / ROMAN / SIA / DARIM / OMU / RUMI / SPECIAL / ENDING입니다. 내부 루미 ID `lumi`를 유지합니다.

LD-01~LD-12를 등록합니다. 필수 9종은 메인·CH01 첫 전원 집합·CH02 발표 직전·CH03 나무 그늘 공통 대화·CH03 개인 이벤트 다섯 종류이고, 추천 3종은 첫날 마무리·라이벌 긴장·발표 후 해방감입니다. 등록·슬롯 수가 실제 그림의 납품 수를 뜻하지 않습니다. 이미지 경로·씬·구도는 [CG 갤러리 가이드](CG_GALLERY_GUIDE.md)를 따릅니다.

`cg_start()`는 LD 한 장을 표시하며 일반 스탠딩을 숨기고 `cg_end()`로 복원합니다. 대사는 기존 대본에 남깁니다. 영구 수집은 `persistent.cg_seen`에, 실제로 본 SD 변형은 `persistent.cg_sd_seen`에 기록합니다. 잠긴 슬롯은 실제 파일이 있어도 그림을 로드하지 않습니다. 해금된 항목에 그림이 없으면 자리표시자를 보여 줍니다. 큰 보기의 이전·다음은 같은 탭의 획득 항목만 순환합니다.

SPECIAL은 SD 12이벤트·33변형과 이전에 수집한 `festival_note` 메모를 보존합니다. 이전 메모 때문에 새 LD-02를 임의 해금하지 않습니다. ENDING은 기존 15개 엔딩의 향후 CG 슬롯이며, 이번 UI 개편으로 엔딩을 새로 완성·해금하지 않습니다. 회상 라벨은 현재 등록되지 않았으므로 회상 재생은 TODO입니다.

## 파일별 책임

아래 `game/`은 `renpy_project/` 기준입니다.

| 파일 | 책임 |
| --- | --- |
| `game/typography.rpy` | Noto Sans 본문·Noto Serif 제목·작은 개구 손메모의 세 폰트 상수와 압축 메타데이터 도우미 |
| `game/screens_campus_main.rpy` | 메인 그림·상단 로고·하단 메뉴·메인 LD 방문 |
| `game/screens_character_profile.rpy` | 기존 다섯 스크랩북과 제목·앞면 한마디 보완 |
| `game/screens_phone.rpy` | 휴대폰과 네이티브 say/choice/퀵메뉴 표시 |
| `game/systems/phone_system.rpy` | 방·메시지·화면·읽음·불러오기 이관 |
| `game/data/phone_ui.json` | 연출 날짜·시각·배경 설정 |
| `game/data/cg_registry.rpy` / `cg_registry.json` | LD 12종 등록표 |
| `game/systems/cg_system.rpy` | LD 시작·종료·복원, CG/SD 획득 |
| `game/screens_campus_gallery.rpy` | 8탭·잠금 썸네일·큰 보기 |
| `game/systems/story_runtime.rpy` | 기존 채팅·일반 무대와 새 UI의 연결 |
| `game/systems/state.rpy` | 기존 저장 이관과 휴대폰 상태 복원 |
| `game/routes/chapter01_official.rpy`~`chapter03_official.rpy` | 기존 사건·대사를 유지한 LD 표시 위치 |
| `game/images/ui/campus_main/`, `game/images/ui/phone/` | 텍스트를 가리지 않는 코드형 SVG 소품 |

메인·휴대폰·갤러리의 새 화면은 init offset 900에서 기존 화면을 대체합니다. 일반 대사·선택지·세이브 흐름과 기존 학생증 데이터는 연결해서 유지합니다. 기존 `theme_spring.rpy`를 새 메인 구조의 정의로 읽지 말고 각 새 파일을 기준으로 수정하세요.

## 저장·원문 보존·증거

이름 입력·호감·신뢰·분기·대사 기록·자동 진행·엔딩 기록의 기존 의미를 유지합니다. 진행 중인 LD·휴대폰 화면은 세이브로, CG 획득은 영구 컬렉션으로 구분합니다. SD는 앞서 구현한 완성 컷 시스템을 사용하고 LD와 개별 SD 스프라이트를 합성하지 않습니다. 구 저장과 원문 보존의 실제 검증 범위는 새 버전 보고서에 기록했습니다.

C 작업 폴더에 있던 참조 PNG 네 개는 `design_docs/source_attachments/` 아래 원래 상대 구조로 옮겼습니다. 크기·SHA-256 대조 후 정확한 C 원본 네 개만 제거한 결과는 [전송 기록](../tests/c-drive-project-transfer.json)에 있습니다. 사용자 원문 사본은 `design_docs/story_sources/`에 보존합니다.

## 남은 제작과 확인

최종 인물·메인·LD·SD 그림, 이후 루트·엔딩 CG와 회상 재생, 사람이 읽는 속도의 플레이 시간은 미완성입니다. 새 메인 여섯 메뉴·폰 각 화면/세 답장·갤러리 잠금/큰 보기·원래 저장·분기·한글 긴 문장·창 크기별 겹침·배포 EXE는 [0.3.0 최종 검증](../tests/VERIFICATION_0.3.0.md)에서 실제로 실행한 항목만 완료로 확인합니다.
