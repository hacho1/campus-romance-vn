# CH06–CH07 대사·콘티 반영 가이드

새 장면의 스탠딩·LD·SD는 이번 단계에서 표시하지 않습니다. 실제 대사·독백·선택지·기존 휴대폰 흐름을 먼저 연결했고, 새 그림과 애니메이션의 예정 위치는 `CONTI SOURCE` 주석으로 보존했습니다. 모든 신규 배경과 BGM은 공유 `story_draft_scene` / `story_draft_bgm`을 사용합니다.

## 파일과 연결

- `game/routes/chapter06_official.rpy`: CH05에서 고른 축제 파트너의 이벤트 한 개만 재생한 뒤 CH07로 연결
- `game/routes/chapter07_official.rpy`: 다섯 인물 모두 선택할 수 있는 최종 루트 선택, 확인/재선택, 선택 인물의 재회 후 `common_route_dispatch`로 연결
- `tools/import_ch06_ch07.py --write`: 보존 원고에서 두 소유 파일과 audit를 재생성
- 원고는 `design_docs/story_sources/chapter06.txt`, `chapter06_darim.txt`, `chapter07.txt`를 사용합니다. 원본 SHA는 생성 파일 상단과 audit에 기록합니다.

## 원고 중복과 다림 보완

CH06 원고의 SC04-B 시아가 L1214와 L1543에서 두 번 나옵니다. 두 본문을 공백 행을 제외한 문장 단위로 비교해 완전 동일함을 확인했습니다. 첫 번째만 실행하며, L1543–1871은 중복으로 제외했습니다. 원본 파일은 수정하지 않았습니다.

사용자가 추가 제공한 `chapter06_darim.txt`를 정식 SC04-C로 통합했습니다. `SOURCE CH06_DARIM Lnn`으로 추적되며 3개 소씬, 대사·독백 105줄, `ch04_partner` 추가 대화와 완료 플래그를 포함합니다. 준비 중 문구는 없습니다. 진행 요원은 전용 Character `ch06_game_staff`를 사용합니다.

0.4.1에서는 CH07 SC01의 L183/185와 SC02의 L207/209가 같은 알림을 반복 소개하는 구간임을 반영했습니다. SC01에서만 시아의 「야 / 다들 살아 있냐?」를 전송하고 SC02는 오므의 답장으로 이어집니다. 재생에서 제외한 두 문장은 `scene_echoes` audit와 SOURCE 주석에 남기며 원고 자체는 바꾸지 않습니다. 기존 저장의 해당 장면 중복 말풍선은 불러올 때만 한 쌍으로 정리합니다. 다른 장면이나 개인 채팅의 반복 대사는 제거하지 않습니다.

| 파트너 | CH06 개인 이벤트 label | 복귀 |
|---|---|---|
| roman | ch06_sc04_roman | ch06_sc05 |
| sia | ch06_sc04_sia | ch06_sc05 |
| darim | ch06_sc04_darim | ch06_sc05 |
| omu | ch06_sc04_omu | ch06_sc05 |
| lumi | ch06_sc04_lumi | ch06_sc05 |

다림은 `ch06_sc04_darim_01` → `_02` → `_03` 순서로 진행합니다. CH05의 `ch06_festival_partner`를 그대로 사용하며 재선택하지 않습니다. 하린의 실제 내부 ID는 `lumi`; 원고의 `harin`/이전 `rumi` 값은 `story_id`로 정규화합니다. 원고 플래그명 `ch06_harin_festival_event`, `harin_route_unlocked`, 기억 ID `harin_space`는 보존했습니다.

## CH07 최종 선택과 회수

다섯 선택지에는 호감도 제한이 없습니다. 첫 메뉴에서는 `ch07_route_candidate`만 변경합니다. 확인 화면에서 진행을 눌러야 기존 `story_apply`로 `selected_route` 및 `route_locked=True`를 적용합니다. 아직 결정하지 않기를 누르면 후보 메뉴로 돌아갑니다. 다른 인물의 SC06은 실행하지 않습니다.

- 후보 선택: `ch07_final_choice`
- 확인: `ch07_final_confirmation`
- 확정 후 서술: `ch07_sc05_confirmed`
- 선택 인물 재회: `ch07_sc06_roman/sia/darim/omu/lumi` → `ch07_sc07`
- 완료: `story_complete_chapter(7)` + `common_route_complete` → `common_route_dispatch`

CH07 SC02의 개인 문자, SC05의 축제 기억, SC07의 마지막 개인 문자는 각각 이번 회차의 선택에 맞는 1개 분기만 출력합니다. SC06의 CH04 약속 회수도 당시 파트너가 일치할 때만 출력합니다. CH06에 5개, CH07에 20개의 조건 구간이 있습니다. 기존 호감도·신뢰도는 초기화하지 않습니다.

## 휴대폰·임시 인물·효과음

단체방과 각 인물의 개인방은 기존 `story_chat`을 사용합니다. 독백은 일반 narrator 대사창에 남기며 육성 혼잣말을 메시지로 발송하지 않습니다. CH06의 방 이름 변경은 기존 그룹 대화의 실제 저장된 제목을 「우리 사이」로 전환합니다. 같은 방 이름 변경으로 폰을 닫았다 다시 열거나 알림을 한 번 더 재생하지 않습니다. 안내 방송, 진행 요원, 운영본부, 방문객 A–E는 이 장 전용 Character이며 스탠딩 이미지를 자동 추가하지 않는 system callback을 사용합니다. 현재 없는 원고 효과음은 콘티로만 남겼고, 개인방 알림은 기존 메시지 효과음을 사용합니다.

## 일러스트·애니메이션 예정 위치

| 원고 | 행 | label | 콘티 |
|---|---|---|---|
| CH06 | L196 | ch06_sc01 | [SD EVENT] `ch06_festival_opening` |
| CH06 | L198 | ch06_sc01 | [연출] 개장 직전 단체 코미디. 시아가 숨을 고르고, 오므는 카메라를 든 채 어이없어하며, 로만은 웃고, 다림과 하린은 준비물을 정리하는 완성형 SD 일러스트 1장. 별도의 SD 포즈 교체 없음. |
| CH06 | L206 | ch06_sc01 | [전환] 일반 LD 스탠딩 |
| CH06 | L367 | ch06_sc02 | [SD EVENT] `ch06_rival_comedy` |
| CH06 | L369 | ch06_sc02 | [연출] 스키가 칭찬받고 얼어붙은 순간, 협합은 무심하게 다음 손님을 가리키고, 헤스·밤밤은 태연한 표정인 SD 단체 일러스트 1장. |
| CH06 | L405 | ch06_sc02 | [전환] 일반 LD 스탠딩 |
| CH06_DARIM | L10 | ch06_sc04_darim_01 | [LD] 다림 · 기본 미소 |
| CH06 | L909 | ch06_sc04_roman | [ANIM] 로만 기본 LD · 자연스러운 눈 깜빡임 |
| CH06 | L1140 | ch06_sc04_roman | [ANIM] 로만이 눈을 깜빡인 뒤 시선을 아래로 내리는 표정 전환 |
| CH06 | L1220 | ch06_sc04_sia | [ANIM] 시아 기본 LD · 가벼운 눈 깜빡임 |
| CH06 | L1362 | ch06_sc04_sia | [ANIM] 시아의 미소가 작아지고, 한 차례 눈을 깜빡이는 표정 전환 |
| CH06 | L1878 | ch06_sc04_omu | [ANIM] 오므 기본 LD · 눈 깜빡임, 머리카락의 약한 움직임 |
| CH06 | L2127 | ch06_sc04_omu | [ANIM] 오므의 시선이 잠시 아래로 내려갔다 돌아오는 표정 전환 |
| CH06 | L2144 | ch06_sc04_omu | [연출] CH05의 팀 단체 사진과 대비되는 둘만의 사진. 주인공의 외형을 특정하지 않는 구도 또는 사진 결과를 직접 보여주지 않고 오므의 반응으로 처리. |
| CH06 | L2238 | ch06_sc04_lumi | [ANIM] 하린 기본 LD · 자연스러운 눈 깜빡임 |
| CH06 | L2240 | ch06_sc04_lumi | [연출] SC04 시작 시 오전의 약속을 짧게 회상한 뒤 현재 시점으로 돌아온다. |
| CH06 | L2349 | ch06_sc04_lumi | [ANIM] 하린의 눈 깜빡임 후 작고 수줍은 미소 |
| CH06 | L2765 | ch06_sc05 | [SD EVENT] `ch06_festival_joint_response` |
| CH06 | L2767 | ch06_sc05 | [연출] 단체 SD 한 장. 스키·시아는 방문객의 우회 방향을 안내하고, 협합·헤스·밤밤은 대기줄을 정리한다. 다림·로만·오므·하린은 각자의 위치에서 안전한 이동을 돕는다. 주인공의 모습은 표시하지 않는다. |
| CH06 | L2769 | ch06_sc05 | [전환] 일반 LD 및 배경 |
| CH07 | L451 | ch07_sc03 | [SD EVENT] `ch07_reunion_comedy` |
| CH07 | L453 | ch07_sc03 | [연출] 이번 챕터의 유일한 신규 SD 단체 일러스트. 시아가 억울해하는 가운데 오므가 카메라를 들고, 하린은 장난스럽게 웃고, 로만과 다림은 그 모습을 지켜보는 장면. 한 장으로 고정하고 대사만 진행. |
| CH07 | L455 | ch07_sc03 | [전환] 일반 LD 스탠딩 |
| CH07 | L690 | ch07_sc04 | [연출] 플레이어가 이번 회차에서 실제 경험한 이벤트 중 대표 장면만 표시. |
| CH07 | L1081 | ch07_sc06_roman | [ANIM] 로만 · 눈 깜빡임, 잔잔한 머리카락 움직임 |
| CH07 | L1131 | ch07_sc06_roman | [ANIM] 로만의 눈 깜빡임 후 미세한 홍조 표정 전환 |
| CH07 | L1474 | ch07_sc06_sia | [ANIM] 시아의 미소가 작아지며 한 번 눈을 깜빡이는 표정 전환 |
| CH07 | L1791 | ch07_sc06_darim | [ANIM] 다림의 눈 깜빡임 후 부드러운 미소 |
| CH07 | L2030 | ch07_sc06_omu | [ANIM] 오므가 살짝 시선을 피했다가 다시 바라보는 표정 전환 |
| CH07 | L2292 | ch07_sc06_lumi | [ANIM] 하린 · 눈 깜빡임, 미세 호흡 |
| CH07 | L2353 | ch07_sc06_lumi | [ANIM] 하린의 시선 회피, 옅은 홍조 표정 |

## 검증 범위

0.4.0 당시 정적 검사 결과는 `CH06_CH07_STORYBOARD_STATIC_CHECK.json`에 보존했습니다. 당시 CH06 대사·독백 1,223줄(다림 추가 105줄 포함), CH07 870줄을 대조했습니다. 0.4.1의 CH07은 반복 알림 두 줄을 제외한 868줄이며, 나머지 본문은 동일합니다. 최신 중복 수정·저장 복구 검증은 `tests/phone_scene_echo_20261108`을 따릅니다.

이 검사는 원본 게임을 실행하지 않습니다. 실제 Ren'Py Lint, 분기·저장·휴대폰 검증 결과는 부모 작업의 통합 QA 기록을 따릅니다.
