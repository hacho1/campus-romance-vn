> **이 문서는 이전 브라우저 게임 실험의 보존 기록입니다. 현재 운영은 PC 런처 설치·증분 업데이트로 전환했습니다.** 최신 명령·경로·운영 상태는 [LAUNCHER_UPDATE_WORKFLOW.md](LAUNCHER_UPDATE_WORKFLOW.md)를 따릅니다. 아래 웹 빌드·비공개 게시 절차는 당시 기록이며 현재 Site의 배포 방식이나 접근 범위를 뜻하지 않습니다. 같은 Site 주소는 PC 런처 제품 페이지로 재사용하며, 사용자의 공개 승인에 따라 접근 범위는 public(revision 2)입니다. 실제 R2의 build2026110801 활성화와 동일 feed 재게시(추가 전송0바이트)는 완료했습니다. HTTPS 최종 검증 결과는 최신 문서를 확인합니다.

# CC대 웹 플레이테스트 갱신

## 원본과 배포 원칙

- 게임의 기준 원본은 `D:\CampusRomance_VN\renpy_project`다. 게임 수정은 이 프로젝트에 반영한다.
- 웹 빌드는 `D:\CampusRomance_VN\web_preview\renpy_project`의 격리 복사본에서 만든다. 웹 대응을 위한 빌드 설정과 생성 파일은 원본으로 역복사하지 않는다.
- Windows 배포본은 사용자가 명시적으로 요청했을 때만 만든다. 게임 수정이나 웹 갱신만으로 Windows 배포본을 자동 생성하지 않는다.
- 웹 플레이테스트는 비공개로 게시한다.

## 재사용할 웹사이트

| 항목 | 고정값 |
| --- | --- |
| Site ID | `appgprj_6aef4bed943081918cd1e61b5d2b7185` |
| 사이트 체크아웃 | `D:\CampusRomance_VN\web_preview\site` |
| 연결 메타데이터 | `site\.openai\hosting.json` |
| 예정 주소 | `https://campus-romance-playtest.naiski.chatgpt.site` |

모든 후속 갱신은 이 Site ID와 `hosting.json`을 재사용한다. 갱신 때 새 사이트를 만들지 않는다. ID와 파일 내용이 다르면 게시를 중단하고 기존 사이트 연결을 확인한다.

현재 게시 상태: **확정 대기**. 위 주소는 예정 주소이며, 게시와 접속 검증 전에는 사용 가능한 주소로 안내하지 않는다.

## 갱신 순서

1. 원본의 변경 내용을 확정하고 원본 코드·실제 세이브의 SHA256 기준값을 기록한다.
2. 원본을 격리된 웹 작업 폴더로 복사한다. 실제 사용자 세이브를 웹 배포 파일에 포함하지 않는다.
3. 격리 복사본을 공식 Ren'Py Web 도구로 내보낸다.
4. 웹 산출물을 로컬에서 실행하고 브라우저 QA를 수행한다. 시작, 화면 전환, 텍스트·이미지, 저장·불러오기 등 실제 확인 결과를 기록한다.
5. 검증된 산출물을 기존 사이트 체크아웃의 `dist`로 동기화한다.
6. Sites 소스 갱신 도우미로 파일과 메타데이터를 준비하고, 고정 Site ID에 **비공개**로 게시한다.
7. 게시 주소에서 접속·실행을 확인하고, 원본 코드와 실제 세이브를 기준값과 다시 비교한다.

## 실행 경로와 명령

| 작업 | 경로 또는 명령 | 상태 |
| --- | --- | --- |
| 격리 게임 복사본 | `web_preview\renpy_project` | 저장·캐시·테스트 제외 |
| 웹 내보내기 도구 | `web_preview\export_tools\build_web.ps1` | 빌드·정적 감사 PASS |
| 공식 웹 내보내기 결과 | `web_preview\export` | SDK 8.5.3 공식 `web_build`, 274파일·437.22 MiB |
| 사이트에 반영할 파일 | `web_preview\site\dist` | `site_tools\prepare_site.py`로 생성 |
| Sites 소스 갱신 도우미 | `web_preview\site_tools\site_workflow.ps1` | 고정 Site ID 재사용, 소스 업로드 중 |
| 비공개 게시 | Sites 도구에서 기존 Site ID로 게시 | 최종 상태 대기 |

위 상대 경로는 `D:\CampusRomance_VN` 기준이다. 웹 빌드를 다시 만드는 명령은 다음과 같다.

```powershell
& 'D:\CampusRomance_VN\web_preview\export_tools\build_web.ps1'
```

이 명령은 `prepare_mirror.py`로 격리 복사본을 준비한 뒤 공식 Ren'Py Web 빌드를 실행한다. 원본의 실제 저장·캐시·테스트와 사용 참조가 없는 레거시 폰트 3개는 웹 복사본에서 제외한다.

검증된 내보내기 결과를 사이트에 준비하는 명령은 다음과 같다.

```powershell
& 'D:\CampusRomance_VN\tools\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe' -B -X utf8 'D:\CampusRomance_VN\web_preview\site_tools\prepare_site.py' 'D:\CampusRomance_VN\web_preview\export'
```

이 준비 도구는 생성 폴더 `site\dist`를 내보내기 결과로 교체하고, 한국어 로딩 안내와 자산 캐시 버전을 적용한다. 서비스 워커는 게임 자산 캐시만 갱신하며 저장 데이터가 있는 IndexedDB를 지우거나 수정하지 않는다.

Sites 소스 작업은 다음 래퍼로 실행한다. Sites 도구가 발급한 작업 요청과 단기 자격 증명은 숨김 표준 입력으로 전달하며 명령 인자나 문서에 기록하지 않는다. 이 래퍼는 해당 프로세스에만 Git `safe.directory`를 설정한다.

```powershell
& 'D:\CampusRomance_VN\web_preview\site_tools\site_workflow.ps1'
```

비공개 게시와 게시 주소 확인은 Sites 도구에서 진행하며, 새 Site를 생성하지 않는다.

## 저장 데이터

브라우저 저장과 Windows 저장은 서로 분리된다. 웹 저장 경로는 `/home/web_user/.renpy/campus-romance`이며 브라우저의 IDBFS/IndexedDB에 유지된다. 현재 Windows 저장 위치는 `D:\CampusRomance_VN\renpy_project\saves`다. 웹 게시나 코드 갱신으로 두 환경의 세이브가 자동 동기화되지는 않는다.

환경 사이에서 저장을 옮길 때는 웹 메뉴의 **저장 내보내기·저장 가져오기**를 명시적으로 사용한다. 실제 저장·재접속 및 환경 간 가져오기 호환성 검증은 **확인 대기**다.

## 이번 실행의 검증 기록

| 검증 | 상태 |
| --- | --- |
| 공식 Ren'Py Web 내보내기 | PASS: 274파일, 458,457,853바이트(437.22 MiB) |
| 정적 배포 감사 | PASS: 최신 compiled 스크립트 42개, JSON 14개, 이미지·오디오·폰트 363개 해시 확인 |
| Sites 파일 크기 제한 | PASS: 최대 `game.zip` 25,753,317바이트, 25 MiB 미만; wasm/data도 각 25 MiB 미만 |
| 전용 인물 사진 4장 | PASS: 원본 해상도·바이트 일치 |
| 로컬 실제 WASM 실행 | PASS: `http://127.0.0.1:18731`, 메인·프로필·전화 확인 |
| 브라우저 저장·재접속·불러오기 | 최종 QA 대기 |
| 비공개 게시 | 대기 |
| 게시 주소 실행 확인 | 대기 |
| 원본·실제 세이브 최종 비교 | PASS: 코드·데이터 56개, 기존 저장 21개, 활성 저장 9개, 이전 READY 저장 9개 변경 없음 |

웹 내보내기 감사 근거는 `web_preview\export_tools\web_export_audit.json`이다. 브라우저 QA와 게시 여부는 각 단계 완료 후 별도로 갱신한다.

보존 기준값은 `tests\web_preview_20261108\source_preservation\baseline.json`에 있다. 파일 내용은 기록하지 않고 경로·파일 크기·SHA256만 기록했다.

- 원본의 테스트 외 `.rpy`와 `data\*.json`: 56개
- 원본의 기존 `game\saves` 폴더: 21개
- 이전 `dist\20261108_people_portraits\READY\CampusRomance-0.3.0-win\saves`: 9개

최종 비교를 실행한 결과, 위 세 범위 모두 추가·삭제·변경이 0개였다. 활성 Windows 저장 파일 9개는 이전 배포 때 확보한 `tests\distribution_people_portraits_20261108\local_save_transfer.json`의 정확한 해시와 별도로 비교해 모두 일치했다. 이 활성 저장 비교는 당시 스냅샷에 포함된 최상위 파일 9개가 범위이며, `sync` 하위 폴더는 해당 스냅샷 범위 밖이다.

비교 재실행 명령:

```powershell
& 'D:\CampusRomance_VN\tests\web_preview_20261108\source_preservation\Verify-SourcePreservation.ps1' -Mode Compare
& 'D:\CampusRomance_VN\tests\web_preview_20261108\source_preservation\Verify-ActiveSaves.ps1'
```

결과는 같은 폴더의 `comparison.json`과 `active_saves_comparison.json`에 기록된다. 이번 결과는 모든 범위의 `unchanged`와 `all_unchanged`가 참이다. 기준값은 덮어쓰지 않았으며 실제 저장 파일도 수정하지 않았다.
