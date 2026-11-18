# CH06 다림·하린 일러스트와 시크릿 비밀메모 — 0.6.10-test

작업 경로: `D:\CampusRomance_VN\renpy_project`.
변경 전 백업: `D:\CampusRomance_VN\backups\ch06_darim_harin_20261114_163342`.

## 일러스트

| 컷 | 시작 | 종료·복귀 |
| --- | --- | --- |
| 다림 01 | 주인공 「선배, 많이 기다리셨어요?」가 표시될 때 | 「차분하게 웃는 모습과 달리 눈빛은 꽤 진지했다.」까지 표시 후 스탠딩 |
| 다림 02 | 「생각보다 재미있었어요.」 | 「그렇게 말씀하시니까 기분 좋네요.」까지 표시 후 스탠딩 |
| 하린 01 | 「……재미있네요.」 | 「……그런가.」와 바로 뒤 주인공의 연결 대사 1개까지 유지 |
| 하린 02 | 다음 하린 「…….」에서 첫 컷과 0.35초 디졸브 | 「나는 무슨 뜻인지 되묻고 싶었지만, 선배가 먼저 일어섰다.」가 나오는 순간 기존 배경·스탠딩 |

하린의 두 기준 대사 사이에는 원고상 주인공 대사 한 줄이 있다. 그 한 줄에 첫 그림을 유지해 스탠딩이 순간 끼어들지 않도록 했다. 대사 자체는 바꾸지 않았다.

네 첨부 PNG를 원본 바이트 그대로 설치했다. 다림 첫 그림은 1024×576, 나머지는 2048×1152이며 같은 16:9 영역에 `contain`으로 표시한다. 생성·크롭·보간 확대 파일은 만들지 않았다. 갤러리에는 DARIM·HARIN 각 한 항목으로 두 컷을 묶었다. 실제 플레이에서는 본 컷만 열리고 테스트판은 기존 전체 열람 정책을 따른다.

그림이 누락되면 기존 배경과 스탠딩으로 진행한다. 하린 두 번째 그림만 누락된 경우에도 첫 그림을 잘못 남기지 않고 스탠딩으로 복귀한다.

## 비밀메모

사용자가 제공한 네 문구를 `NOTE03.secret`에 문단 그대로 반영했다.

- 로만: 「특별한 선물」
- 시아: 「오늘의 작전」
- 오므: 「오늘 하루의 역할」
- 다림: 「선배의 작은 장난」

확정 원문은 `design_docs/story_sources/secret_notes_0610.json`, 재적용 도구는 `tools/update_secret_notes_0610.py`다. 메모 01·02, 해피·배드 문구, 하린 메모, 실제 엔딩 제목과 해금 조건은 바꾸지 않았다. 기존 스크롤 영역으로 긴 원문의 마지막 문단까지 읽을 수 있도록 확인한다.

## 변경 파일

- `game/routes/chapter06_official.rpy`: 새 연출 7블록. 기존 대사·선택·5/10점 그대로.
- `game/data/cg_registry.json`: CG 4개, 갤러리 그룹 2개.
- `game/data/secret_notes.json`: 시크릿 메모 4곳만 교체.
- `game/data/phone_ui.json`: CH06 줄 위치 조회 갱신.
- `game/options.rpy`: 버전.
- `game/images/cg/ch06/festival_darim_01.png`, `festival_darim_02.png`, `festival_lumi_01.png`, `festival_lumi_02.png`.
- `tools/apply_ch06_visual_revision.py`, `install_ch06_darim_harin_art_0610.py`, `update_secret_notes_0610.py`.

내부 인물 ID `lumi`와 기존 수집 ID는 유지한다. 재생성 후에는 `tools/import_roman_first.py --phone-cues`를 마지막에 실행한다.

## 검증·배포 기록

실행 결과: `tests/ch06_darim_harin_0610/RESULT.json`.
에셋 동일성: `asset_audit.json`. 대사·원본 코드 보존: `cg_source_audit.json`.
메모 교체 범위·원문: `notes_audit.json`. 세부 구간: `CG_INTERVALS.md`.
공개 검증: `tests/ch06_darim_harin_0610_public/RESULT.json`.

배포는 기존 온라인 서명 피드를 사용하며 런처 EXE 재설치는 필요하지 않다. 실제 공개 활성화 후 버전·다운로드 검증 수치를 아래에 기록한다.

### 실제 활성화 결과

- 게임 `0.6.10-test`, build `2026111401`, 2026-11-14.
- manifest SHA-256: `c264afe611cbce472ae3e12bf238623bc1af3970dc1ef823a8e34b772b568e12`.
- 전체1,898파일 / 621,821,119바이트. 신규90조각 / 14,398,567바이트 업로드, 기존1,806조각 재사용.
- 실제 서명 피드 활성화: `launcher_publish/r2_upload_result.json`.
- 네이티브11케이스·36검증, 컴파일·Lint 통과. 521개 소스의 QA후보·원본·배포 스냅샷 해시 일치.
- 기존 배포 RPYC에 대응하는95개의 RPY 원고 중 CH06/options 두 파일만 변경, 나머지93개 원고 불변. 컴파일 RPYC는 재빌드되며 바이너리 해시가 바뀔 수 있다. 이전 공개95RPYC seed를 공식 merge_names에 사용했고 활성본도 `compiled_seeds/2026111401`에 보존했다.
- 실제 공개 검증 PASS: 정상 TLS·고정 RSA, productionCLI `qa:false`, 사이트의 버전·빌드·공지5개 일치. 대표9파일 / 10,950,273바이트 실제 HTTPS 재구성 및 원본4PNG 동일성 확인. 기존367이미지 불변. 갤러리2항목·4컷, 비밀메모4곳만 변경, 전화는 CH06 줄 위치22개만 갱신.
