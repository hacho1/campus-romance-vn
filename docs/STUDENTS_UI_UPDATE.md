# CC대 학생들 · 소개 화면 변경

프로젝트: `D:\CampusRomance_VN\renpy_project`

## 적용 내용

- 메인 메뉴의 `히로인 설명`을 `CC대 학생들`로 변경했습니다.
- 기존 다섯 히로인의 프로필·비밀 메모·일상 사진·호감도·신뢰도 화면은 유지합니다.
- 소개 화면 제목 옆 `만난 사람들!`을 누르면 스키·협합·헤스·밤밤의 간단한 소개가 열립니다.
- 네 인물의 기존 스탠딩을 사진으로 재사용하고, 학과·학년·짧은 소개·대본 속 한마디를 표시합니다. 사진은 비율을 유지하며 340×284 창 안에서만 보입니다.
- `우리의 페이지`를 누르면 앞에서 선택한 히로인으로 돌아갑니다. 닫기 또는 Esc로 메뉴를 닫습니다.
- 네 소개는 처음부터 볼 수 있습니다. 별도의 관계 수치나 수집 조건은 추가하지 않습니다.

## 수정 파일

프로젝트의 `game/` 기준:

- `screens_campus_main.rpy`: 메인 메뉴 이름.
- `screens_character_profile.rpy`: 기존 제목과 새 소개 화면 진입 버튼.
- `screens_met_people.rpy`: 새 소개 화면, 사진 프레임, 복귀·닫기.
- `data/met_people.rpy`: 소개 데이터 로드와 스탠딩 사진 처리.
- `data/met_people.json`: 네 명의 공개 소개.
- `tests/students_ui.rpy`: 새 화면과 기존 프로필 회귀 검사.
- `tests/campus_ui.rpy`, `tests/integration.rpy`, `tests/screenshot_polish.rpy`: 변경된 메뉴·제목 문자열만 갱신.

사용 안내는 프로젝트 `README.html`과 상위 `README_profile_ui.md`에 반영했습니다.

## 보존 확인

백업: `D:\CampusRomance_VN\backups\20261107_students_ui`

백업과 비교해 기존 다섯 히로인 화면의 탭·인물 목록부터 파일 끝까지 동일함을 확인했습니다. 메인 메뉴 파일도 요청한 표시 문구 외에는 동일합니다. 스토리·선택지·관계 데이터·영구 수집 구조는 이 작업에서 수정하지 않았습니다.

## 검증

독립 저장 폴더와 소프트웨어 렌더러를 사용한 Ren’Py 네이티브 실행에서 3개 사례·34개 상위 assertion을 통과했습니다. 검사 안에서 다섯 프로필의 앞·뒷면과 비밀 메모, 네 명의 소개 데이터·사진·텍스트 위치, 선택 인물 복귀, 게임 중 관계 값 보존, 이미지 누락 대체 표시와 Esc 동작을 확인했습니다.

최종 사진 프레임 수정 후의 화면을 직접 확인했습니다. 네 인물의 사진은 프레임 안에 들어가며 이름·본문·인용문과 겹치지 않습니다.

Ren’Py Lint는 오류·경고 없이 통과했습니다. 8개 카드 상태의 텍스트 32개가 카드 안에 들어가며, 실제 PNG의 새 버튼 3개도 글자 중심 검사를 통과했습니다. 원본과 테스트 복사본의 관련 10개 파일 해시가 일치하고 기존 검사 세 파일은 표시 문구 외에 바뀌지 않았습니다.

- 검사 로그: `D:\CampusRomance_VN\tests\students_ui_20261107\native-students-ui-final.log`
- 검사 종합: `D:\CampusRomance_VN\tests\students_ui_20261107\README.md`
- 실제 배치 근거: `D:\CampusRomance_VN\tests\students_ui_20261107\layout_evidence.json`
- 새 화면: `D:\CampusRomance_VN\tests\students_ui_20261107\screenshots\met_people_four_cards.png`
- 기존 히로인 화면: `D:\CampusRomance_VN\tests\students_ui_20261107\screenshots\heroine_roman_front.png`

## Windows 실행판

최종 위치: `D:\CampusRomance_VN\dist\20261107_students_001350064`

- 바로 실행: `READY\CampusRomance-0.3.0-win\CampusRomance.exe`
- 공유용 ZIP: `CampusRomance-0.3.0-20261107-students-win.zip` (약 414.51 MiB)

실제 패키지 EXE의 격리 실행 검사 1개 사례·18개 상위 assertion을 통과했습니다. 새 소개 화면의 네 인물·사진 프레임, 원래 프로필 복귀, 갤러리, 이야기 시작, 저장·불러오기를 확인했습니다. 인자 없이 EXE를 시작하는 검사도 정상 종료했습니다. 두 실행 검사 모두 별도 QA 복사본을 사용했으며 최종 실행 폴더에 검사 코드를 넣지 않았습니다.

배포 감사에서 실행에 필요한 98개 파일(컴파일 스크립트 42개 포함)의 원본 일치와 새 소개 JSON의 포함을 확인했습니다. 공유용 ZIP에는 개인 저장이나 개발용 검사 파일이 없습니다. 사진 수정 전 중간 빌드는 별도 기록으로 남겼으며 위 경로가 최종본입니다.

최신 개인 저장 폴더인 원본 프로젝트의 `saves`에서 슬롯 8개와 `persistent`를 **새 로컬 실행판의 `saves`에만** 복사했습니다. 복사 전후 원본·이전 실행판은 그대로이며 새 복사본의 파일 해시와 수정 시각이 일치합니다. 공유용 ZIP 해시도 변하지 않았습니다.

- 배포 검증: `D:\CampusRomance_VN\tests\distribution_students_20261107\README.md`
- 개인 저장 복사 근거: `D:\CampusRomance_VN\tests\distribution_students_20261107\local_save_transfer.json`

이 작업에 남은 필수 구현은 없습니다. 다른 조연의 소개를 추가하려면 `met_people.json`을 확장하면 됩니다. 이후 개별 루트·엔딩 등 게임 전체의 남은 콘텐츠 범위는 실행판 `README.html`을 따릅니다.
