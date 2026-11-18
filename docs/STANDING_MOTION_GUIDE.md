# 일반 스탠딩 모션 가이드

일반 대화의 화자 강조와 짧은 행동 연출만 다룹니다. 대사, 선택지 ID, 관계 수치와 SD·LD 완성 컷 구성은 바꾸지 않습니다.

## 화자 강조

`story_mode`가 `normal` 또는 `emotion`이면 화자의 밝기를 올리고 듣는 인물은 `BrightnessMatrix(-0.18)`를 적용합니다. 픽시 AI 스탠딩은 1920×1080 게임 화면에서 872×1308의 고정 표시 크기를 사용합니다. 인원이 들어오거나 화자가 바뀔 때 스탠딩 크기와 이미지의 불투명도를 유지합니다.

해설, 주인공, 운영위원 등 화면 밖의 목소리가 나올 때는 4인 이상이면 같은 어두운 톤을 유지하며 1~3인은 기본 밝기로 표시합니다. 화자가 실제로 바뀔 때만 0.16초 동안 강조가 부드럽게 이동합니다. 같은 사람이 연속으로 말하는 동안에는 `story_focus_serial`과 시작 시각을 바꾸지 않습니다.

한 구도에는 최대 5명이 한 줄로 섭니다. 양 팀을 합쳐 6명 이상인 대화에서는 히로인 팀과 라이벌 팀을 별도 구도로 표시합니다. 화자가 다른 팀에 속하면 그 팀을 보여 주고, 주인공 대사나 내레이션에서는 직전 구도를 유지합니다. 표정 변경에는 `story_stage(faces={"roman": "embarrassed"})`처럼 `faces`만 전달합니다. 오므의 기본 표정은 두 번째 전신 포즈인 `omu_direct.png`에 연결하고 같은 포즈의 웃음·놀람 등 표정을 사용합니다.

## 연출 API

```renpy
# 기존 행동 API는 그대로 사용합니다.
$ story_effect("jump", "roman")
$ story_effect("shake", "sia")
$ story_move("roman", 610, 795)

# 작은 반응 아이콘. 종류는 heart / exclamation / lightbulb입니다.
$ story_icon("roman", "heart")
$ story_icon("sia", "exclamation", duration=0.9)
$ story_icon("lumi", "lightbulb")

# 출입장은 명시적으로 호출한 곳에서만 재생합니다.
$ story_enter("sia", side="right", face="happy", position=(1310,795))
$ story_exit("sia", side="left")
```

`story_stage(cast=...)`는 지정한 인원을 한 번에 배치합니다. `story_enter`는 새로 등장하는 인물을 왼쪽이나 오른쪽 끝에 배치하고 0.28초 동안 수평으로 들입니다. 이미 지정한 위치는 유지하며 자동 슬롯만 필요한 만큼 이동합니다. `story_exit`는 활동 캐스트에서 제외한 뒤 0.26초 동안 화면 밖으로 보냅니다.

활동 캐스트는 히로인 다섯 명과 라이벌 네 명까지 포함하며 화면에는 현재 구도의 인물만 표시합니다. 퇴장 도중 같은 인물이 다시 입장하면 이전 퇴장 표시를 정리합니다. 새 장면이나 명시적인 캐스트 교체는 지난 장면의 출입장·아이콘을 정리합니다. SD·LD가 끝나면 전환 전에 서 있던 인원을 모두 복원할 수 있습니다.

아이콘은 기본 0.9초 뒤 사라지며, 같은 인물에게 새 아이콘을 주면 교체합니다. 소리는 추가하지 않습니다. 세 SVG는 `game/images/ui/stage_effects/`에서 색과 형태를 수정할 수 있습니다.

## 저장·롤백·이동 설정

캐스트, 위치, 방향, 표정과 기존 `story_effects` 튜플은 Ren’Py 저장 상태입니다. 모션 표시에는 효과 토큰과 별도 시작 시각을 사용하므로 대사가 바뀌거나 화면이 다시 계산되어도 같은 효과를 처음부터 재생하지 않습니다.

불러온 상태에서는 활동 캐스트·위치·방향을 유지하고, 짧은 흔들림·점프·아이콘·남아 있던 퇴장 표시를 완료 상태로 정리합니다. 기존 효과 튜플을 지우지 않고 표시만 완료 처리하여 구 저장과의 호환성을 유지합니다. 로드 직후 UI 경계에서도 같은 정리를 수행합니다. 롤백은 저장된 활동 캐스트와 위치를 복원하며, 이미 지난 표시 시각 때문에 퇴장 잔상이 계속 남지 않습니다.

환경설정의 화면 전환 효과를 끄면 화자 강조는 즉시 확정하고, 입장자는 최종 위치에 나타나며 퇴장은 즉시 끝납니다. 아이콘의 정보는 짧게 표시하되 개별 인물 이동은 재생하지 않습니다.

SD 이벤트나 LD CG가 켜진 동안에는 일반 스탠딩 화면 전체를 표시하지 않습니다. 새 출입장·아이콘 API와 기존 이동·행동 API도 완성 컷 안에서 개별 인물을 합성하지 않습니다.

## 개발용 시연

개발실의 **공통 루트 · 챕터와 SD 연출 → 일반 스탠딩 · 모션 시연**으로 들어갑니다. `standing_motion_preview` 라벨에서 화자 교대, 해설, 점프, 흔들림, 세 아이콘과 좌우 출입장을 차례로 볼 수 있습니다. 마지막 조작 화면에서는 대사 진행 없이 버튼으로 다시 시험할 수 있습니다. 일반 배포 모드에서는 진입 라벨과 조작 화면이 모두 비활성입니다.

## 배경 조명 연결

`story_scene`은 선택한 조명을 `story_light`에 `day` / `evening` / `night`로 저장하고, 배경 한 장의 생성은 `story_background_display(bg, light)`에 맡깁니다. 실제 야간 자산과 색 보정, 구 저장의 야간 배경 복구는 `systems/story_lighting.rpy`가 담당합니다. 이 모션 모듈은 SD·LD 레이어나 조명 복원 로직을 바꾸지 않습니다.

## 검증

새 네이티브 모음은 `standing_motion_followup`입니다. 실제 렌더 Transform의 확대·밝기·alpha, 같은 화자의 연속 대사, 점프·흔들림 타이밍, 입장·퇴장 정리, 세 아이콘, 실제 저장/불러오기와 롤백, SD·LD 분리, 이동 효과 끄기와 개발 시연을 확인합니다. 실행은 별도 `CAMPUS_SAVE_DIR`을 지정한 QA 복사본에서만 진행하며 플레이어 저장은 사용하지 않습니다.

CH01~CH03에는 놀람·당황·진지함 등 예정했던 표정을 일반 대화의 해당 대사에 연결했습니다. 전용 이미지가 없는 표정은 같은 캐릭터의 가까운 표정을 사용합니다. 입장 예시는 CH01 동아리실의 시아·오므와 CH02 상자 사고 직전의 스키·협합입니다. CH03 회의는 발언 팀에 맞춰 두 구도를 오갑니다. 밤 산책로에서는 헤어지는 대사에 맞춰 양쪽으로 퇴장한 뒤 선택된 히로인이 다시 등장합니다.

픽시 AI 스탠딩 47장의 알파를 점검했고 시아·다림·루미·스키 21장의 흰 잔여 배경이나 과하게 지워진 밝은 부분을 수정했습니다. 원본 PNG의 크기와 정렬은 유지했습니다. [투명 처리 검증 기록](../artwork/pixai_review/matte-recheck-20261105/before-after.json)

이전 단체 배치 검증에서는 CH01의 4인 대화, CH03 두 팀 회의, SD·LD와 저장 복원 뒤 캐스트 복귀를 확인했습니다. 투명 처리 뒤 CH01 대화도 다시 렌더링했습니다. 당시 기존 모션 모음은 13개 중 12개가 통과했고, 묶음 실행에서 짧은 흔들림 프레임을 놓친 한 사례는 단독 재실행에서 통과했습니다.

- [이전 4인 배치](../tests/standing_ensemble_20261105/evidence/03-four-darim-speaks.png) · [투명 처리 전후](../artwork/pixai_review/matte-recheck-20261105/matte-corrections-closeup.png)
- [배치 실행](../tests/standing_ensemble_20261105/renpy-layout-run.txt) · [최종 이미지 재검증](../tests/standing_ensemble_20261105/renpy-matte-final.txt) · [기존 모션 검사](../tests/standing_ensemble_20261105/renpy-motion-final.txt) · [흔들림 재실행](../tests/standing_ensemble_20261105/renpy-shake-retest.txt) · [Lint](../tests/standing_ensemble_20261105/renpy-lint.txt)

최신 고정 크기 검증에서는 1~9명의 합류·퇴장 전후에 표시된 인물의 렌더 크기를 측정했습니다. CH03 본편의 두 팀 전환과 내레이션 중 팀을 저장하고 불러오는 동작, CH01 복도에서 오므가 두 번째 기본 포즈에서 놀란 표정으로 바뀌는 동작을 확인했습니다. Ren’Py 테스트 4개와 Lint가 통과했습니다.

- [히로인 팀](../tests/standing_fixed_scale_20261105/evidence/09-review-heroine-team.png) · [라이벌 팀](../tests/standing_fixed_scale_20261105/evidence/08-review-rival-team.png) · [오므 기본](../tests/standing_fixed_scale_20261105/evidence/06-omu-neutral.png) · [오므 놀람](../tests/standing_fixed_scale_20261105/evidence/07-omu-surprised.png)
- [실행 로그](../tests/standing_fixed_scale_20261105/renpy-run.txt) · [Lint](../tests/standing_fixed_scale_20261105/renpy-lint.txt)
