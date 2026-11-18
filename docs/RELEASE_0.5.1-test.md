# 0.5.1-test · CH04 저녁 개인 CG

게임 원본: `D:\CampusRomance_VN\renpy_project`. 배포 build: `2026110806`.

## 변경 범위

CH04 SC08-B~E에 사용자가 제공한 일러스트 4장을 넣었다. 각 인물이 주인공을 부르는 첫 대사는 기존 스탠딩으로 보여주며, 그 대사를 읽고 넘기면 0.38초 디졸브로 CG가 나타난다. 이후 개인 대화가 끝날 때까지 유지하고 공통 귀갓길로 복귀할 때 종료한다. 로만 SC08-A의 기존 동작은 유지한다.

| 장면 | CG가 나타나기 직전의 대사 | CG ID | 갤러리 |
| --- | --- | --- | --- |
| SC08-B 시아 | `야, [player_name].` | `ch04_evening_sia` | SIA |
| SC08-C 다림 | `[player_name] 씨.` | `ch04_evening_darim` | DARIM |
| SC08-D 오므 | `야.` | `ch04_evening_omu` | OMU |
| SC08-E 하린 | `[player_name] 씨.` | `ch04_evening_lumi` | HARIN |

이미지는 모두 원본 PNG 2048×1152와 바이트·SHA256이 일치한다. 리사이즈·재생성·크롭 없이 1920×1080 게임 화면에 비율을 유지하여 표시한다. 새 장면은 기존 SC06 표정 CG와 별개의 갤러리 항목이며 해당 장면을 본 뒤에만 열린다.

## 수정 파일

- `game/routes/chapter04_official.rpy`: 각 첫 대사 이후 CG 시작, 개인 분기 종료 시 CG 종료.
- `game/data/cg_registry.json`: 4개 독립 CG와 갤러리 순서.
- `game/images/cg/ch04_evening_sia.png`, `ch04_evening_darim.png`, `ch04_evening_omu.png`, `ch04_evening_lumi.png`: 첨부 원본 복사.
- `game/data/phone_ui.json`: 추가된 연출문에 맞춰 CH04의 구버전 저장 위치용 시간표 행 번호만 재계산.
- `game/options.rpy`: 게임 버전 `0.5.1-test`.

작업 백업은 `backups/sc08_evening_cgs_20261108`에 있다. 원본 가져오기 기록은 `tests/sc08_cgs_051/import_manifest.json`, 재현 스크립트는 `tools/apply_sc08_evening_cgs_051.py`다. CH04 원본은 수동 편집 방식이며 대본 전체를 다시 가져오지 않았다.

## 검증

수정 전 백업과 비교하여 20개 route 파일의 대사·선택지 11,387개가 순서까지 일치한다. 변경된 route는 CH04 하나뿐이다. 기존 CG 등록 항목과 수집 ID를 수정하지 않았고, 휴대폰 데이터는 CH04 위치 조회표 외에 변경하지 않았다. 정적 비교 기록: `tests/sc08_cgs_051/source_parity.json`, `chapter04.diff`.

격리된 Ren'Py 실제 실행에서 6개 케이스·110개 검증·8개 훅이 모두 통과했다. 네 신규 분기와 기존 로만 분기의 첫 대사/등장/유지/종료, 0.38초 전환, 5개 갤러리 탭의 잠금·해금·앞뒤 이동, 대표 CG 저장·불러오기를 검사했다. Lint 오류·경고·traceback은 0개다. 최종 게임 원본과 검사본 460개 파일의 SHA256이 일치하며 실제 플레이 저장 파일 14개의 내용·수정 시각은 바뀌지 않았다.

화면 검사는 격리 SDL dummy·소프트웨어 렌더링을 사용했으며 실제 전경 창/GPU 검사는 포함하지 않는다. 증거 26장과 결과는 `tests/sc08_cgs_051/native/README.md`, `RESULT.json`에 있다.

## 온라인 게시

같은 공개 채널에 `0.5.1-test / build2026110806`을 활성화했다. 총 1,837파일·563,774,891바이트, 기존 조각 1,770개를 재사용하고 새 65조각·14,709,427바이트를 업로드했다. 전체 ZIP이나 새 설치 프로그램을 만들지 않았고 사이트·런처 EXE는 변경하지 않았다.

Manifest SHA256: `56869ac0db4e8f715cd550fcc244d101219128ee8a9a2e2719d5028d4a459459`. 고정 RSA 서명과 source/SDK 원본 보존 검사도 통과했다. 서명 키·게시 토큰·개인 저장은 배포하지 않는다. 플레이어는 기존 런처에서 **업데이트 확인 → 설치·업데이트 → 게임 시작**으로 받는다.

공개 다운로드 검사도 통과했다. QA 주소 변경 없이 실제 production 런처 CLI가 `qa:false`, `status:ok`, 버전·build·1,837파일을 확인했고 게임 다운로드/설치는 0이었다. 공개 manifest 823,465바이트와 고정 query의 서명을 받아 RSA·공지 3개가 로컬 활성본과 정확히 일치함을 검증했다. 대표 5개 청크·12,463,783바이트를 실제 GET해 CH04 컴파일 파일과 첨부 원본 4장의 크기·SHA256을 대조했다. 전체 게임 설치나 사이트 레이아웃 재검사는 하지 않았다.

최종 공개 결과·불변 영수증: `tests/sc08_cgs_051/public_verify/RESULT.json`, `run-1794145255607`. 기존 플레이어 저장을 바꾸지 않고 같은 런처의 온라인 업데이트로 제공된다.
