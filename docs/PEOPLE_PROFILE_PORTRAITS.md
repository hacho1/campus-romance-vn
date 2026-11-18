# 만난 사람들 · 전용 프로필 그림과 두 명씩 보기

프로젝트: `D:\CampusRomance_VN\renpy_project`

## 변경 내용

사용자가 제공한 네 그림을 다음 인물의 프로필에 적용했습니다.

| 첨부 순서 | 인물 | 게임 이미지 경로 |
| --- | --- | --- |
| 1 | 스키 | `images/people/profile_ski.png` |
| 2 | 협합 | `images/people/profile_hyeophap.png` |
| 3 | 밤밤 | `images/people/profile_bambam.png` |
| 4 | 헤스 | `images/people/profile_hess.png` |

네 PNG는 모두 1232×1504이며 원본 파일을 그대로 복사했습니다. 재생성·보정·크기 변경·재인코딩은 하지 않았습니다. 원본과 프로젝트 이미지의 SHA256 일치 기록은 `D:\CampusRomance_VN\artwork\people_profiles_20261108\import_manifest.json`에 있습니다.

`CC대 학생들 → 만난 사람들!`의 소개는 한 페이지에 두 명씩 표시합니다. 첫 페이지는 스키·협합, 둘째 페이지는 밤밤·헤스입니다. 각 카드는 820×660으로 넓히고, 왼쪽의 432×528 사진 창에 그림 전체를 비율대로 담습니다. 오른쪽에는 기존 이름·학과·학년·간단한 소개와 한마디를 크게 배치합니다.

이전/다음 버튼과 좌우 방향키로 페이지를 바꿉니다. 끝에서 한 번 더 넘기면 처음으로 돌아갑니다. `우리의 페이지`는 앞에서 보던 히로인으로 돌아가며, 닫기와 Esc 동작도 유지합니다. 기존 히로인 다섯 명의 화면과 스토리·관계·비밀 메모는 변경하지 않습니다.

## 수정한 파일

프로젝트의 `game/` 기준:

- `screens_met_people.rpy`: 큰 카드, 세로 사진 창, 페이지 버튼·방향키.
- `data/met_people.rpy`: 페이지당 두 명, 전용 사진 우선 로드.
- `data/met_people.json`: 네 사진 경로와 표시 순서.
- `images/people/profile_ski.png`, `profile_hyeophap.png`, `profile_bambam.png`, `profile_hess.png`: 제공된 원본 파일.
- `tests/students_ui.rpy`: 두 페이지, 이미지 연결과 대체 표시 회귀 검사.

프로젝트 `README.html`과 상위 `README_profile_ui.md`의 사용·교체 안내도 갱신했습니다. 변경 전 파일은 `D:\CampusRomance_VN\backups\20261108_people_portraits` 및 `backups\20261108_people_portraits_tests`에 보관합니다.

## 사진 교체와 대체 표시

`met_people.json`의 `portrait_image` 경로에 있는 이미지를 사용합니다. 사진 창은 `contain` 방식으로 전체 이미지를 표시합니다. 전용 파일이 없으면 기존 스탠딩의 `portrait_crop` 부분을 대체 사진으로 사용하고, 그 이미지도 없으면 `사진 준비 중`을 표시합니다.

기존 소개 문구를 수정하려면 같은 JSON의 `intro`와 `quote`를 편집합니다. 새 인물은 `people`과 `order`에 함께 추가하며 페이지는 두 명씩 자동으로 나뉩니다.

## 검증과 실행판

두 페이지의 실제 Ren’Py 화면을 확인했습니다. 네 사진의 인물 연결·표시 순서가 맞고, 전체 세로 구도와 이름·소개·버튼이 지정 영역에 들어갑니다.

- 첫 페이지: `D:\CampusRomance_VN\tests\people_portraits_20261108\screenshots\met_people_page_1.png`
- 둘째 페이지: `D:\CampusRomance_VN\tests\people_portraits_20261108\screenshots\met_people_page_2.png`

기존 `screens_character_profile.rpy`와 `screens_campus_main.rpy`의 SHA256은 앞선 검증본과 일치합니다. 기존 다섯 히로인 소개와 메인 메뉴는 이 작업에서 수정하지 않았습니다.

독립 저장 폴더와 소프트웨어 렌더러를 사용한 네이티브 검사 3개 사례·43개 SDK assertion·12개 hook을 통과했습니다. 두 페이지의 인물·사진, 이전/다음과 좌우키 순환, 기존 다섯 프로필, 선택 인물 복귀, 게임 중 관계 값 보존, 전용 사진 누락 시 스탠딩 대체 및 모든 이미지 누락 시 안내 표시를 확인했습니다. 검사 복사본의 관련 7개 파일과 원본 PNG 네 장의 해시가 프로젝트와 일치합니다.

Ren’Py Lint는 오류·경고 없이 통과했습니다. 새 헤더·페이지 조작 버튼 5개의 실제 PNG 글자 중심 검사도 통과했습니다(최대 중심 차이 2.5px).

- 네이티브 검사 종합: `D:\CampusRomance_VN\tests\people_portraits_20261108\README.md`
- 네이티브 로그: `D:\CampusRomance_VN\tests\people_portraits_20261108\native-people-portraits-final.log`

앞선 네 명 한 화면 버전의 기록은 `STUDENTS_UI_UPDATE.md`에 별도로 보존합니다.

## 최종 Windows 실행판

- 실행 파일: `D:\CampusRomance_VN\dist\20261108_people_portraits\READY\CampusRomance-0.3.0-win\CampusRomance.exe`
- 공유용 ZIP: `D:\CampusRomance_VN\dist\20261108_people_portraits\CampusRomance-0.3.0-20261108-people-win.zip` (약 423.66 MiB)

실제 패키지 EXE의 격리 검사 1개 사례·18개 SDK assertion과 사진·배치 helper를 통과했습니다. 두 페이지의 전용 파일 연결·해상도·사진 창, 버튼·좌우키 순환, 원래 프로필 복귀, 갤러리 표정 전환, 이야기 시작, 저장·불러오기를 확인했습니다. 인자 없는 일반 시작도 타이틀에 도달해 종료 코드 0으로 마쳤습니다.

패키지 감사에서 런타임 파일 103개의 해시, 컴파일 스크립트 42개의 최신성, 전용 PNG 네 장의 1232×1504 크기와 원본 해시 일치를 확인했습니다. 공유 ZIP에 개인 세이브·persistent·개발 검사를 넣지 않았습니다. 실행 검사는 별도 QA 복사본과 독립 저장 폴더에서 소프트웨어 렌더러로 수행했으며 실제 GPU 창·다른 PC 환경은 검사 범위 밖입니다.

최신 저장 폴더인 `renpy_project\saves`의 슬롯 8개와 `persistent`, 총 9개를 새 로컬 READY의 `saves`에만 복사했습니다. 원본과 이전 실행판 두 곳의 저장은 그대로이고 복사본의 해시·수정 시각이 일치합니다. 공유용 ZIP 해시도 변하지 않았습니다.

기존 바탕화면 바로가기는 `D:\CampusRomance_VN\START_GAME.cmd`를 통해 수정된 원본 프로젝트를 실행하므로 그대로 사용할 수 있습니다. 바로가기나 실행 스크립트 자체는 수정하지 않았습니다.

- 배포 검사 종합: `D:\CampusRomance_VN\tests\distribution_people_portraits_20261108\README.md`
- 저장 보존 근거: `D:\CampusRomance_VN\tests\distribution_people_portraits_20261108\local_save_transfer.json`

이 요청에 남은 필수 구현은 없습니다. 이후 인물을 추가할 때도 전용 사진과 JSON 항목을 등록하면 같은 두 명씩 보기 구성을 사용할 수 있습니다.
