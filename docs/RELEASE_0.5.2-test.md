# 0.5.2-test · CH05 준비와 설치 일러스트

작업 원본: `D:\CampusRomance_VN\renpy_project`. 배포 build: `2026110901`.

## 장면 연결

| 첨부 | 시작 | 종료/교체 | 등록 ID |
| --- | --- | --- | --- |
| 1 · 동아리실 단체 준비 | SC02 네 번째 독백 `하린 선배의 앞에는 완성된 부스 모형이 놓여 있었다.`를 넘긴 뒤 | SC02 종료, 발표 장소로 이동 | `ch05_final_prep_01` |
| 2 · 시아와 오므의 상자 | SC08 `ch05_booth_install_01` | `ch05_booth_install_02` 시작 | `ch05_booth_install_01` |
| 3 · 우리 팀 전시 부스 | `ch05_booth_install_02` | `ch05_rival_install_comedy` 시작 | `ch05_booth_install_02` |
| 4 · 라이벌 쿠키 부스 | `ch05_rival_install_comedy` | `완성된 축제 부스 · 노을` 배경으로 전환 | `ch05_rival_install_comedy` |
| 5 · 단체 사진 | 기존 `ch05_team_memory_photo` CG 이벤트 | 기존 CG 종료 시점 유지 | `ch05_team_memory_photo` |

SC02 처음 네 독백은 배경만 표시하고 스탠딩·SD 그림을 숨긴다. 첨부1은 0.30초 디졸브로 등장해 해당 장면 끝까지 유지하며 중간에 별도 SD 컷으로 바꾸지 않는다. SC08의 첨부2→3→4 역시 중간에 스탠딩을 끼우지 않고 이어진다. 노을 지점에서는 SD를 끝내고 명시적인 다섯 히로인 스탠딩과 배경으로 복귀한다. 단체 사진의 기존 시작·종료 지점은 바꾸지 않았다.

## 원본 보존과 갤러리

첨부 PNG 5장은 2048×1152 원본 바이트와 SHA256이 모두 같다. 재생성·리사이즈·크롭 없이 비율을 유지하여 표시한다. SD4장은 SPECIAL, 마지막 단체 사진은 COMMON에 등록했다. 기존 수집 ID는 유지했고 기존 SD 등록을 삭제하지 않았다. 기존 플레이에서 같은 단체 사진 ID를 수집했다면 새 COMMON 항목에서도 그 기록을 사용한다.

## 수정 파일

- `game/routes/chapter05_official.rpy`: 시작·교체·종료 지점과 첫 네 독백의 스탠딩 숨김.
- `game/data/sd_events.json`: SD4장의 새 PNG 경로, 구도 설명, SPECIAL 등록.
- `game/data/cg_registry.json`: 기존 단체 사진 ID의 PNG 교체 및 COMMON 목록 추가.
- `game/images/sd_events/ch05_final_prep_01.png`, `ch05_booth_install_01.png`, `ch05_booth_install_02.png`, `ch05_rival_install_comedy.png`.
- `game/images/cg/ch05_team_memory_photo.png`.
- `game/data/phone_ui.json`: 추가/삭제된 연출문에 맞춰 CH05의 구버전 저장 위치용 시간표 행 번호만 재계산.
- `game/options.rpy`: `0.5.2-test`.

백업은 `backups/ch05_art_20261109`, 원본 가져오기 기록은 `tests/ch05_art_052/import_manifest.json`에 있다. `tools/apply_ch05_art_052.py`는 백업과 첨부 가져오기·연출 편집에 사용한 일회성 작업 스크립트다.

## 검증

정적 비교: 20개 route의 대사·선택지 11,387개가 수정 전과 순서까지 같다. 변경된 route는 CH05뿐이다. SD 등록 ID와 다른 CG 정보는 유지했고 휴대폰의 변화는 CH05 위치 조회표뿐이다. `tests/ch05_art_052/source_parity.json`과 세 diff에 기록했다.

격리 Ren'Py 실제 실행의 3개 케이스·46개 SDK 검증·5개 훅이 통과했다(실패0, 116.70초). SC02의 첫 네 독백에 스탠딩·SD가 없고 이후 준비 컷이 연속 유지되는지, SC08 세 그림과 노을의 다섯 스탠딩 복귀가 대사 흐름 전체에서 정상인지 확인했다. SD·CG 각각 저장/불러오기와 잠금·해금·갤러리 확대를 검사했다. 디졸브 중간 캡처와 전환이 끝난 정지 화면을 구분해 실제 PNG도 검수했다.

Lint 오류·경고·traceback은 0개다. 최종 게임 원본과 격리 검사본 465개 파일의 SHA256이 같으며 실제 플레이 저장 파일 14개의 내용·수정 시각도 바뀌지 않았다.

검사는 SDL dummy·소프트웨어 렌더링과 별도 저장 폴더를 사용하는 격리 실행이며 전경 창이나 GPU 검사를 주장하지 않는다. 세부 증거는 `tests/ch05_art_052/native`에 있다.

## 런처 온라인 업데이트

같은 공개 채널에 `0.5.2-test / build2026110901`을 활성화했다. 총1,842파일·579,248,002바이트이며 기존1,773조각을 재사용하고 새67조각·17,833,337바이트를 업로드했다. 고정 RSA로 서명한 manifest SHA256은 `251579548fd70c47d99609cf85b16866df8061f1c89f8309bb50ba1ff9f334e1`이다. 원본 SDK·실행파일·플레이 저장을 유지하고 전체 ZIP을 생성하지 않았다.

기존 런처1.1과 설치/공지 화면이 같은 활성 채널에서 새 버전·공지3개를 읽는다. 런처 EXE와 사이트 코드는 변경하지 않았다. **기존 런처에서 업데이트 확인 → 설치·업데이트 → 게임 시작**으로 받으며 런처를 다시 내려받을 필요가 없다.

공개 검증도 첫 실행에서 통과했다. 실제 production CLI는 QA 주소 변경 없이 `qa:false`, `status:ok`, `0.5.2-test/build2026110901`, 1,842파일을 확인했고 게임 다운로드·설치는 0이었다. 공개 manifest825,848바이트·고정 query 서명·RSA·공지3개가 로컬 활성본과 정확히 일치했다. 대표6청크15,564,375바이트를 실제 GET하여 CH05 컴파일 대본90,043바이트와 첨부5장의 공개 파일이 원본/배포 후보의 바이트·SHA256과 같음을 확인했다.

최종 결과와 불변 영수증은 `tests/ch05_art_052/public_verify/RESULT.json`, `run-1794152052135`에 있다. 사용자 PC의 실제 게임 설치나 플레이 저장을 바꾸지 않고 채널과 공개 파일을 읽어 검사했다.
