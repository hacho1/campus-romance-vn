# 다림 시크릿 · 이번에는 제가 놀릴게요 · 0.6.5-test

원본 게임: `D:\CampusRomance_VN\renpy_project`.

새로 제공된 시크릿 원고 **「이번에는 제가 놀릴게요」**와 첨부 일러스트를 반영한다. 이전 제작 예고명은 실제 새 시크릿의 제목으로 갱신했다. 기존 D01~D06 본문·선택·5/10점 정책과 다른 루트는 유지한다. 새 스탠딩·SD·표정 차분은 만들지 않는다.

## 대본·그림

- 원고 `design_docs/story_sources/darim_secret.txt`:14,018바이트, SHA256 `7f7a032c7f7157dde7e5a4cb7c574d33b7e6c296fb182554a41b053005ff26d8`. 사용자의 첨부와 바이트가 같다.
- 대사/서술256개·5씬·선택지0개·점수 변화0. 인용 대사178개와 화자/본문256개 독립 대조·변환 재생성 동일성 검사가 통과했다. 기획/연출 설명은 실제 대사와 구분한다.
- 첨부PNG는 `game/images/cg/endings/darim_secret.png`에 원본 그대로 복사했다. **2048×1152·2,543,021바이트**, SHA256 `88aa612f098803c22a96006cdc34e239285894618bf21dc49aef8635f1a6f175`. 생성·보정·크롭·업스케일하지 않았다.
- 원문334행 `[CG MAIN] darim_secret_tease`에서 `ending/darim_secret`을0.35초 디졸브로 표시한다. SC04 배경476행에서0.3초 전환으로 내린다. 원본 비율은 `screen_fit=contain`으로 유지한다.
- 원문386행의1초 멈춤과 마지막 서술4문장을 보존했다. SC01 메시지는41~80행만 채팅으로 표시하고, 집 앞 직접 대사 전에 닫는다.

## 진입·수집

일반 플레이는 **다림 해피 엔딩 → 엔딩 목록 → 다림 시크릿 읽기**로 들어간다. `persistent.endings`의 `darim_happy`가 필수이고, 단순한 예고 플래그로 선행 조건을 대신하지 않는다. 실제 읽기 전에는 시크릿 엔딩/CG가 수집되지 않는다.

첫 시크릿에서도 지정 장면의 그림은 표시되며, 끝까지 완료하면 `darim_secret` 기록과 CG가 해금된다. 갤러리 **DARIM/ENDING** 두 탭에서 같은 한 작품으로 조회한다. 엔딩 화면의 로만·시아·다림·오므 시크릿 버튼4개는 기존 종이 영역 안의 한 줄에 배치했다.

테스트 챕터 선택의 다림 그룹에 시크릿1개를 추가했다. 테스트의 임시 해피 기록·수집은 별도 Persistent 사본에만 적용한다. 원래 플레이의 점수·메시지·선택을 지우거나 덮어쓰지 않는다. 공식 Ren'Py Replay는 중간 저장을 비활성화하므로, 실제 Replay 복원과 별도의 일반 실행 저장/불러오기를 구분해서 검사한다.

작중 시간은499/DSECRET, 해피 이후 몇 달의 같은 토요일16:00→17:00→17:10/20/30→18:10→19:00이다. PC 현재 시각을 읽지 않는다. 기존35에피소드 시간 큐 처리에서 대사는 그대로이며, 이전40개 루트 파일은 바이트가 같다. `DARIM_SECRET_PHONE_CUE_AUDIT.json` 참조.

## 백업·파일

수정 전 `D:\CampusRomance_VN\backups\darim_secret_20261110_234525`에 **676파일·522,418,794바이트**를 백업했다.

신규 파일:

- `renpy_project/game/routes/darim_secret.rpy`
- `renpy_project/game/images/cg/endings/darim_secret.png`
- `tools/import_darim_secret.py`
- `design_docs/story_sources/darim_secret.txt`
- `docs/DARIM_SECRET_IMPORT_AUDIT.json`, `DARIM_SECRET_IMPORT_STATIC_RESULT.json`, `DARIM_SECRET_IMPORT_GUIDE.md`, `DARIM_SECRET_ASSET_IMPORT.json`

기존 수정 파일(아래는 `renpy_project/game` 기준):

- `systems/darim_story_runtime.rpy`, `systems/test_chapters.rpy`, `systems/phone_timeline.rpy`
- `data/endings.json`, `data/cg_registry.json`, `data/phone_ui.json`
- `screens_ending_diary.rpy`, `screens.rpy`, `screens_story_stage.rpy`, `options.rpy`
- 별도 제작 도구 `D:/CampusRomance_VN/tools/import_roman_first.py`에 DSECRET 시간 큐를 추가했다.

## 검증·공개

공식 Ren'Py 8.5.3에서 채택한 **4케이스·15개 명시 SDK 검증**이 통과했다. 공개0.6.4에서 실제 다림 해피 엔딩 저장을 만들고 같은 버전에서 재로드하는 기준 검사도 **1케이스·2검증** 통과했다. 최종 강제 컴파일85개와 Lint는 오류·경고가 없다.

- 해피 이전의 시크릿 라벨·CG·완료 기록 접근은 잠긴다.
- 실제0.6.4 해피 저장을0.6.5로 불러와 같은 엔딩 위치를 복원하고, 실제 **다림 시크릿 읽기** 버튼을 눌러 첫 CG 미수집→완료 후 단일 작품 수집을 확인했다. 회상 종료 뒤 원래 점수·선택·폰·배경·캐스트·엔딩 판정은 복원된다.
- 일반 실행의 CG 지점에서 저장/불러오기·CG 경계 롤백을 확인했다. 공식 Replay의 저장 제한을 우회하지 않았다.
- 다림 테스트 항목7개를 확인했다. 기존40개 루트·4개 호감도 카탈로그와 실제 사용자 기록14개의 SHA256·수정시간은 유지됐다. 최종499개 소스/에셋이 QA 사본·배포 snapshot과 일치한다.

네 버튼의 배치 좌표는 원본 화면 코드와 실제 다림 버튼 클릭으로 검토했다. 별도의 자동 기하 검사1개는 Button 자식에 절대좌표가 있다고 가정했지만 위치가 Fixed 부모에 있어 하네스 오류가 났고, 통과한 검사 수에 포함하지 않았다. 버튼은 x330/640/950/1260·너비290·높이52로 기존 종이 안에 배치한다. 실제 UI의 모든 픽셀을 자동으로 인증했다는 뜻은 아니다.

근거: `tests/darim_secret_065/ROOT_CLOSEOUT.json`, `native_results.json`, `final_source_audit.json`, `snapshot_qa_parity.json`, `lint-final.log`. 원문256문장/5씬은 정적으로 대조하고 실제 시크릿 완료도 실행했다. 전경과 커서를 보존한 SDL dummy/software 검사이며 음향의 청감 품질과 하드웨어 렌더링은 별도 범위다.

### 온라인 배포

기존 공개 채널 <https://campus-romance-playtest.naiski.chatgpt.site/>에 **0.6.5-test / build2026111002**를 활성화했다. 전체1,876파일·588,666,721바이트, manifest SHA256은 `8489d90114f23821acd88d135664ba2432ef81d0450261f0d666f1db9de60fb5`다.

첫 업로드가 연결 종료로 중단되어, 이미 받은 조각을 재사용한 단일 작업자 재시도로 완료했다. 최종 재시도는 **23조각·4,866,839바이트**를 추가하고1,851조각을 재사용했다. 부분 업로드 중에는 기존 공개판을 유지했으며, 모든 조각이 갖춰진 뒤 서명 manifest를 활성화했다.

QA override 없는 실제 production CLI가 새 버전/build를 인식했다. 공개 RSA 서명·공지5개와 대표 **13파일·2,930,490바이트** 실제 HTTPS 다운로드가 snapshot과 일치한다. 첨부PNG는 C의 원본·D의 제품·snapshot·공개본까지 같은 SHA/크기/2048×1152이며, DARIM/ENDING 단일 작품·해피 선행·완료 수집·회상 연결도 확인했다. 기존 이미지·4개 정책·루트 데이터·40개 기존 대본도 보존했다. `tests/darim_secret_065_public/RESULT.json` 참조.

이번 공개본 **85개 RPYC**는 `launcher_publish/compiled_seeds/2026111002`에 다음 업데이트용으로 보존했다. Site/런처 EXE는 유지하며 활성 manifest로 버전/공지를 갱신한다. 기존 런처에서 **업데이트 확인 → 설치·업데이트**로 받는다. 사용자 실제 게임 설치나 저장을 QA 사본으로 덮어쓰지 않았다.

## 후속 작업

SC02/SC04 주방과 식탁/현관의 전용 배경은 기존 실내 그림을 임시로 재사용한다. 제공된 메인 CG 이외의 스탠딩이나 새 그림은 후속 미술 작업이다.
