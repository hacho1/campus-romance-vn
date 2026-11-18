# 테스트판 일러스트 열람 · 0.6.8

테스트판에서는 갤러리에 등록되어 있고 실제 파일이 준비된 일러스트를 미획득 상태에서도 볼 수 있다. LD, SPECIAL의 SD, ENDING 그림과 같은 장면의 표정 변형을 포함한다. 원래의 탭·썸네일·이전/다음·표정 전환 UI를 그대로 사용한다.

`campus_test_collections_preview()`가 참일 때 `cg_gallery_can_view_cut(key)`가 실제 이미지 존재를 확인해 열람을 허용한다. 이미지가 없는 미획득 장면은 계속 잠긴다. 이미 획득한 장면의 이미지가 아직 준비되지 않은 경우에는 기존 준비 중 안내를 유지한다.

이 기능은 열람 권한만 바꾼다.

- `cg_seen`, `cg_unlock`, `cg_start`의 획득·스토리 진입 규칙은 수정하지 않았다.
- `persistent.cg_seen`, `persistent.cg_sd_seen`, `persistent.gallery`, `persistent.endings`에 테스트 열람 기록을 쓰지 않는다.
- 시크릿 엔딩 CG 열람이 시크릿 스토리나 해피 엔딩 클리어를 해금하지 않는다.
- 표정 2장은 기존처럼 장면 1개의 썸네일에 묶이며, 감상 화면에서 클릭·Space·Enter로 바뀐다.
- 테스트판 플래그를 끄면 원래 획득 기록에 따른 갤러리 잠금으로 돌아간다.

관련 파일:

- `D:\CampusRomance_VN\renpy_project\game\systems\cg_system.rpy`
- `D:\CampusRomance_VN\renpy_project\game\screens_campus_gallery.rpy`
- 공통 테스트판 플래그: `D:\CampusRomance_VN\renpy_project\game\systems\test_chapters.rpy`

정적 검사에서는 기존 `cg_seen`·`cg_unlock`·`cg_start` 함수 본문의 동일성을 확인한다. 실제 Ren'Py 실행·갤러리 조작·저장 데이터 보존 검증은 통합 테스트 보고서에 기록한다.

2026-11-12 정적 검증 결과: 테스트판 여부 × 실제 이미지 여부 × 기존 획득 여부의 8가지 조합을 통과했다. `cg_seen`, `cg_unlock`, `cg_start`, `cg_end`, `cg_unlock_sd`, `cg_displayable` 함수의 AST가 변경 전 백업과 동일함을 확인했다. 준비된 그림을 테스트 열람할 때에는 획득 판정 함수도 호출하지 않는다.
