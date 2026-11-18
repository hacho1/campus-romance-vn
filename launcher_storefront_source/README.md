# Windows 런처 제품 페이지 소스

이 폴더는 사이트에 복사할 정적 제품 페이지다. 원본 Ren'Py 프로젝트나 실제 Site 체크아웃을 수정하지 않는다. 런타임 의존성이나 빌드 단계 없이 `index.html`, `styles.css`, `app.js`, `assets/`를 제공한다.

## 게임 내용 표기

공통 루트는 CH01–07, 현재 포함된 개별 루트는 로만 R01–R06이다. 로만의 해피·배드 엔딩과 해피 엔딩 완료 후 읽는 시크릿 이야기를 안내한다. 시아·다림·오므·하린의 개별 루트는 제작 중이다. 모든 개별 루트나 개인 데이트가 완성됐다고 표기하지 않는다.

시크릿 첨부 CG는 게임 내 해금용으로 유지하며 이 페이지에 복사하거나 노출하지 않는다. 기존 타이틀 아트·스크린샷·색·배치는 유지한다. 제품의 버전과 build는 실제 R2 manifest에서 읽고 예정 배포 번호를 하드코딩하지 않는다.

## 배포에 포함할 파일

다음만 기존 사이트의 배포 폴더로 복사한다.

```text
index.html
styles.css
app.js
assets/
```

`.taste-skill/`, 이 README, DESIGN.md, 자산 감사 결과는 검토 자료이며 공개 페이지 필수 파일이 아니다.

root가 다음 실제 산출물을 같은 배포 루트에 준비한다. 이 소스 폴더에는 가짜 EXE나 임의 manifest를 넣지 않는다.

```text
downloads/CampusRomanceLauncher.exe
releases/latest.json
```

## 배포 metadata 계약

`latest.json`은 `schema: 1`, `product: "campus-romance"`, `version: string`, `build: integer`, `release_notes: string[]`를 제공한다. 페이지는 버전·빌드·변경 사항만 읽는다. `files`와 다운로드 청크는 PC 런처가 사용한다.

외부 데이터를 HTML로 삽입하지 않는다. 노트는 `textContent`로 표시하며 길이와 항목 수를 제한한다. manifest 오류는 다시 확인 버튼을 제공하고, EXE 파일이 없으면 다운로드 링크를 준비 중 상태로 둔다.

## QA hooks

| 항목 | Hook |
| --- | --- |
| 버전 상태 | `#release[data-release-state="loading\|ready\|error"]` |
| 상태 메시지 | `#release-status` |
| 버전 정보 | `#release-details`, `#release-version`, `#release-build`, `#release-notes` |
| 다시 읽기 | `#release-retry` |
| 다운로드 상태 | `.download-block[data-download-state="checking\|ready\|unavailable"]` |
| 다운로드 링크 | `#download-launcher[aria-disabled]` |
| 다운로드 안내 | `#download-status` |
| 게임 화면 선택 | `.screen-choice[aria-pressed]` |
| 큰 화면 | `#screen-open`, `#screen-dialog`, `.dialog-close` |

1280/768/390 폭, metadata 성공·지연·오류, EXE 존재·누락, 이미지 선택, dialog Escape, 키보드 포커스, reduced motion을 확인한다. `.exe` 링크는 브라우저 소유자가 비공개 사이트에 접근할 수 있는 상태에서 검증해야 한다. 비공개 사이트에 대한 설치 클라이언트의 익명 업데이트 접근은 별도 배포 설정이며 이 페이지가 활성화하지 않는다.

## 자산

단체 메인 비주얼과 3개 네이티브 게임 화면을 원본에서 바이트 그대로 복사했다. 상세 경로와 SHA256 비교는 `asset_manifest.json`에 기록한다. 외부 이미지·웹 폰트·분석 도구·쿠키 스크립트를 추가하지 않았다.
