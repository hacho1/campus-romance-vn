# 우리 사이, 그 이상 · PC 런처

설치형 Ren’Py 게임을 한 번 받은 뒤 변경된 파일과 조각만 받는 Windows 런처입니다. 브라우저에서 게임을 다시 구현하지 않습니다. 계정·결제·런처 자체 자동 업데이트는 이번 범위에 포함하지 않습니다.

## 산출물과 실행 방식

- 사용자가 받을 단일 파일: `build/CampusRomanceLauncher.exe`.
- 격리 검증 도구: `build/CampusRomanceUpdater.Cli.exe`. QA 도구는 사용자용 다운로드에 포함할 필요가 없습니다.
- 기본 설치 위치: `D:\CampusRomance_VN\Installed`. D드라이브가 없으면 사용자 LocalAppData의 CampusRomance 폴더를 제안합니다. 사용자가 다른 위치를 선택할 수 있습니다.
- 관리되는 게임: `<설치 위치>/Game/`. 런처와 게임 폴더를 분리합니다.
- 실제 GUI의 첫 설치가 성공하면 런처를 `<설치 위치>/CampusRomanceLauncher.exe`로 복사하고 바탕화면에 **우리 사이, 그 이상 런처** 바로가기를 만듭니다. 같은 이름의 다른 파일/바로가기를 덮어쓰지 않습니다. 기존 게임 바로가기는 유지합니다.
- 업데이트는 런처에서 **업데이트 확인 → 설치·업데이트 → 게임 시작** 순서로 사용합니다. 설치된 게임 실행은 채널 접속 없이 가능합니다.
- Launcher1.1 UI 개선 때 이 PC의 `D:\CampusRomance_VN\Installed`에는 런처 EXE만 준비하고 같은 위치를 가리키는 바탕화면 **우리 사이, 그 이상 런처** 바로가기를 만들었습니다. 전체 게임 설치·실행·저장 기록 가져오기는 수행하지 않았습니다.

## 빌드

.NET Framework 4.8이 있는 Windows 환경에서 추가 패키지나 dotnet CLI 없이 빌드합니다.

```powershell
& 'D:\CampusRomance_VN\launcher_app\scripts\build_icon.ps1'
& 'D:\CampusRomance_VN\launcher_app\scripts\build_launcher.ps1'
```

`assets/launcher-source.png`는 사용자가 제공한 원본이며 그림은 수정하지 않습니다. 아이콘 변환은16/24/32/48/64/128/256 크기를 가진 ICO를 만들고, GUI EXE의 Windows 아이콘과 `CampusRomance.LauncherIcon` 리소스에 같은 파일을 내장합니다.

컴파일러는 `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe`입니다. 런처는 GUI EXE 하나에 공유 코어·업데이트 공개키를 내장합니다. `config/update_public_key.xml`이 없으면 빌드를 거부합니다. `config/feed_config.json`의 `feed_base_url`이 있으면 이 값도 리소스로 내장하며, 기본 채널은 다음 주소입니다.

```text
https://campus-romance-playtest.naiski.chatgpt.site/
```

서명용 개인키는 이 앱에 포함하지 않습니다. 공개키/채널은 일반 사용자 GUI에서 바꿀 수 없습니다. HTTPS를 사용하며 인증이 필요한 비공개 채널은 런처가 접근 오류로 안내합니다. 업데이트 서버 공개/배포는 별도 게시 작업입니다.

## 서명된 피드

- Manifest: `<feed base>/releases/latest.json`.
- 서명: `<feed base>/releases/latest.sig?manifest=<받은 raw JSON의 SHA-256>`, raw UTF-8 JSON 바이트의 RSA-2048 PKCS#1 SHA-256 서명을 Base64 ASCII로 저장. JSON을 받은 직후 서버의 최신 버전이 바뀌어도 같은 manifest의 서명을 요청합니다. 기존 정적 서버는 query를 무시하고 파일을 반환해 호환됩니다.
- 조각 URL은 **feed base 기준** `payload/chunks/<sha256>.bin`입니다. releases 폴더 기준이 아닙니다.
- schema=1, product=`campus-romance`, version 문자열, 증가하는 build Int64, executable, total_bytes Int64, files, release_notes를 사용합니다.
- 각 파일은 path/size/sha256/chunks를 갖습니다. 각 조각은 sha256/size/url을 갖고 최대8MiB입니다. 빈 파일은 chunks=[]와 빈 데이터의 SHA-256을 사용합니다.
- 서명이 확인되기 전 JSON 해석이나 설치 위치의 파일 변경을 하지 않습니다. 이전 설치 기록에도 원본 manifest와 서명을 보존해 오프라인 검증에 사용합니다.
- 설치된 build보다 낮은 배포는 거부합니다. 같은 build의 manifest 내용이 바뀌는 것도 거부하므로 manifest 변경 시 build를 올려야 합니다.

## 보존과 복구

- 파일 크기와 SHA-256을 먼저 검사해 달라진 파일만 준비합니다. 이미 검증된 조각은 `.campus-launcher/chunks`에서 재사용합니다.
- 조각별 크기/SHA-256을 확인하고, 조립한 완성 파일도 다시 검사합니다. 바뀔 파일을 모두 staging한 뒤에 적용합니다.
- 업데이트 중인 같은 설치 위치는 named mutex와 파일 잠금으로 보호합니다. Game 내부 EXE/엔진 프로세스가 실행 중이면 업데이트를 거부합니다.
- 적용 전 복구 journal을 기록하고 기존 관리 파일을 backup으로 옮깁니다. 적용 오류는 이전 상태로 복구합니다. 프로세스가 중단되면 다음 **설치·업데이트**에서 journal을 보고 복구합니다.
- `.installed-state.json`을 원자적으로 교체한 시점이 커밋입니다. transaction ID도 기록해 같은 빌드의 파일 복구 중 중단되는 경우를 구분합니다.
- 새 manifest에서 사라진 파일은 **이전의 서명된 관리 목록에 있고, 현재 내용도 이전 해시와 같을 때만** 제거합니다. 수정된 예전 파일은 보존합니다.
- saves, game/saves, persistent, 사용자 로그·스크린샷·내보내기 폴더를 관리 대상으로 받지 않습니다. Windows 예약 이름, 절대경로, `..`, ADS, 심볼릭 링크/junction도 거부합니다. `renpy/exports/**`만은 실제 엔진 Python 모듈이므로 사용자 exports와 구분합니다.
- Game 안의 사용자 폴더를 통째로 삭제하지 않습니다. 캐시와 트랜잭션 정리는 런처의 별도 관리 폴더 안에서만 수행합니다.

## 이 개발 PC의 기존 기록 가져오기

실제 GUI에서만 `D:\CampusRomance_VN\renpy_project\saves`의 top-level *.save와 persistent를 감지합니다. 둘 다 있을 때 **이 PC의 기존 플레이 기록 가져오기**가 기본 선택됩니다. 첫 설치가 성공했고 사용자가 선택했으며 대상 Game/saves에 플레이 기록이 없을 때만 한 묶음으로 복사합니다.

원본 파일을 staging해 해시/수정 시각/파일 목록이 변하지 않았는지 확인하고, 원본을 이동·삭제·덮어쓰지 않습니다. 대상에 이미 top-level 또는 하위 플레이 기록이 있으면 가져오지 않습니다. 일반 업데이트에는 이 분기가 실행되지 않습니다. 저장 기록을 피드나 웹사이트에 올리지 않습니다.

CLI는 이 기능을 포함하지 않습니다. `LauncherForm(false)`도 실제 저장 폴더를 감지하지 않습니다. QA는 GUI assembly의 `SaveMigration.ImportIfEmpty(sourceFixture,targetFixture)`에 명시적 fixture 경로만 넘겨 검사합니다.

## CLI 계약

```text
CampusRomanceUpdater.Cli.exe check --root INSTALL_ROOT
CampusRomanceUpdater.Cli.exe update --root INSTALL_ROOT
CampusRomanceUpdater.Cli.exe play --root INSTALL_ROOT
```

기본 stdout은 단일 JSON입니다. status/code/message, installed_build/latest_build, installed_version/version, update_available, changed_files/deleted_files, downloaded_chunks/downloaded_bytes/reused_chunks, total_bytes, recovery_performed를 반환합니다. 다운로드 통계는 manifest/signature를 제외한 실제 payload 전송량입니다.

테스트 전용:

```text
CampusRomanceUpdater.Cli.exe update --root QA_ROOT --qa --feed-base http://127.0.0.1:PORT/ --public-key QA_PUBLIC.xml
```

HTTP는 명시적 --qa와 loopback일 때만 허용합니다. --public-key/--feed-base 재정의, --fail-after-apply N, --crash-after-apply N, hold-lock --hold-lock-ms N도 QA CLI에서만 허용합니다. GUI EXE는 --qa를 거부합니다. QA play는 실행 파일을 검증하고 경로만 반환하며 실제 게임을 띄우지 않습니다.

Exit: 0성공, 2서명, 3manifest/경로, 4다운그레이드/동일빌드충돌, 5동시실행/게임실행중, 6다운로드/해시/적용/복구, 1기타. QA 강제 중단은 73입니다.

## 파일 구조와 검증

- `src/UpdateModels.cs`: JSON 모델과 엄격한 필수 타입 파싱.
- `src/SafePaths.cs`: 경로·사용자 데이터·reparse 방어.
- `src/UpdateEngine.cs`: 서명, 검사, 조각 다운로드, 트랜잭션 적용/복구, 오프라인 실행.
- `src/Program.cs`: 고정 설정과 CLI.
- `src/LauncherForm.cs`: 한국어 화면, 취소/진행률, 첫 UI설치 후 런처/바로가기.
- `src/SaveMigration.cs`: 명시적 경로로 테스트 가능한 첫 설치 기록 복사.

QA의 격리 CLI E2E 21케이스가 통과했습니다. 첫 설치3163B/50조각, 무변경0B, 한 파일 변경64B/새 조각1개로 HTTP 실측과 통계가 일치했습니다. 서명·경로·다운그레이드·동시 실행·게임 실행중·손상/중단·rollback·강제 중단 후 recovery를 검사했습니다. 추가 metadata race에서는 JSON101을 받은 직후 서버 포인터가102로 바뀌어도, 받은 JSON의 SHA-256 query로101의 서명을 가져와 check/update가 일관되게 통과했습니다. 실제 전체 프로덕션 manifest의 경로/서명 검사도 통과했습니다.

GUI 화면은 `LauncherForm(false)`와 DrawToBitmap으로 렌더해 내용을 확인했으며 visible=false였습니다. 이후 metadata 요청 프로토콜만 보완한 최종 GUI는57,344바이트이고 화면/migration 소스는 같습니다. migration fixture 4케이스(첫 복사/기존 대상 보존/하위 대상 기록 보존/경로 겹침)와 원본 해시·시각 유지도 PASS입니다. HTTP 서버를 종료한 뒤 QA play에서 네트워크0을 확인하고, 실제 UpdateEngine.Play(Qa=false)도 창을 만들지 않는 WinExe stub의 marker 생성으로 검증했습니다. 원본과 동일한 native snapshot의 Ren’Py Lint도 clean입니다.

최종 코어로21케이스를 다시 실행했습니다. 사용자용 EXE SHA-256은 `5b57ff6f6bd34afdb60c6c1194eb3ceb582ece54da7ce9e276331ba2e97e2448`입니다. 사용자 승인으로 배포 채널을 공개했고 실제 R2에 build2026110801을 활성화했습니다. production CLI의 HTTPS check(재정의 없음), 실제 EXE 다운로드와 대표청크 SHA256, 공개 페이지 버전 표시가 통과했습니다. 같은 feed 재게시 시1799개 조각을 재사용하고 추가 전송0바이트를 확인했습니다. 사용자 PC에서 실제 전체 첫 설치와 바탕화면 바로가기 생성은 실행하지 않았습니다.

초기 검증 근거는 `D:\CampusRomance_VN\tests\launcher_update_20261108`에 있습니다. 초기 런처 작성은 기존 Ren’Py 원본·실제 저장·이전 배포판을 수정하지 않았습니다. 이후 게임 아이콘 요청은 options.rpy의 창 아이콘 설정과 전용 ICO/PNG 자산에만 적용했으며 실제 저장과 이전 배포 EXE는 보존했습니다.

## Launcher1.1 화면 개선

상단 `설치 / 공지` 탭으로 나눴습니다. 설치 화면의 경로·기록 가져오기·내 PC·업데이트 채널·작업 버튼은 유지하고, 새 소식은 공지 탭의 최신 버전/build와 스크롤 읽기 영역으로 옮겼습니다. 진행·전송량·취소·작업 버튼은 공통 영역이므로 공지를 읽어도 상태를 확인할 수 있습니다. 컨트롤과 worker를 재생성하지 않아 경로와 진행 상태를 유지합니다. Ctrl+1/2 및 Ctrl+Tab으로도 전환합니다.

새 EXE는375,296바이트, SHA256 `144dac93108f4d40c5b1ae0394a68a247763432e87db7c4cac5c98cea18430dc`입니다. 기존1.0 검증 기록과 구분하며 런처 변경은 화면·아이콘·버전 정보에 한정합니다. 업데이트 코어와 개인키는 그대로이고, 게임 EXE·창 아이콘 적용은 게임 build2026110802로 게시했습니다. 실제 저장 데이터는 변경하지 않았습니다. 새 검증 기록은 `tests\launcher_ui_20261108`에 있습니다.
