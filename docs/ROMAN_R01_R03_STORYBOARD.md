# 로만 R01–R03 대사·콘티 반영 가이드

## 반영 범위

원고를 새 그림 없이 실행할 수 있는 대사 단계로 옮겼습니다. 24씬의 대사·독백 1,878줄, 선택지 7개(21개 응답), R03 조건 분기 2개를 포함합니다. 원고의 도입 설명·장면 구성표·완료 타이틀 연출은 대사에 넣지 않았습니다. 기존 원고의 문장을 교정하거나 사건을 재작성하지 않았습니다.

- `game/routes/roman_r01.rpy` → `roman_r01` 시작, R02로 연결
- `game/routes/roman_r02.rpy` → `roman_r02` 시작, R03로 연결
- `game/routes/roman_r03.rpy` → `roman_r03` 시작, R04로 연결
- 각 씬은 `roman_r01_sc01`과 같은 독립 label을 사용합니다.
- 시작 API는 `roman_begin_episode`, 배경/BGM은 `story_draft_scene`, `story_draft_bgm`입니다. 이 파일에서는 실제 스탠딩·LD·SD를 표시하지 않습니다.

## 원본 및 추적

모든 대사와 실행 지시는 `SOURCE R01 L42`처럼 원고 행을 남겼습니다. `CONTI SOURCE`는 추후 아트 작업 위치이며 지금은 실행하지 않습니다. UTF-8 원고의 SHA-256은 파일 상단 및 import audit에 기록되어 있습니다.

### R01 「책갈피에 남겨둔 약속」

원고 SHA-256: `4a290045ffefbae93ca78501a833d9953585cef0fa6d5f72b1262658d7e17eca`

| 씬 | 제목 |
|---|---|
| SC01 | 다음 페이지를 넘기기 전에 |
| SC02 | 책을 고르는 방식 |
| SC03 | 무서운 건 딱 질색이에요 |
| SC04 | 같은 문장을 다르게 읽는 우리 |
| SC05 | 아직은 보여드릴 수 없는 글 |
| SC06 | 첫 번째 독자가 되어주세요 |
| SC07 | 책갈피의 뒷면 |
| SC08 | 다음에는 제가 먼저 |

### R01 일러스트·표정 예정 위치

| 원고 행 | 씬 | 콘티 |
|---|---|---|
| L182 | SC02 | [LD] 로만 · 기본 미소 |
| L310 | SC02 | [LD] 로만 · 당황 |
| L385 | SC03 | [LD] 로만 · 굳은 표정 |
| L443 | SC03 | [SD EVENT] roman_r01_ghost_book_comedy |
| L445 | SC03 | [연출] 로만이 공포 소설을 들고 놀란 표정으로 굳어 있고, 주변에는 평범한 서점 책장과 스피커가 있는 완성형 SD 일러스트 1장. 주인공은 화면 밖에 존재. |
| L483 | SC03 | [전환] 일반 LD |
| L561 | SC04 | [LD] 로만 · 옅은 홍조 |
| L731 | SC05 | [ANIM] 로만 · 부드러운 눈 깜빡임과 미세 호흡 |
| L1075 | SC06 | [LD] 로만 · 붉어진 얼굴 |
| L1100 | SC07 | [ANIM] 로만 · 약한 머리카락 움직임, 자연스러운 눈 깜빡임 |

### R02 「조금씩, 가까워지는 거리」

원고 SHA-256: `696624f925095f73c43502037e3d27978ac43f46d44dca439d1fac7d7681796f`

| 씬 | 제목 |
|---|---|
| SC01 | 오늘은 제가 정했어요 |
| SC02 | 로만 씨에게 이런 면이? |
| SC03 | 강아지는 반칙이에요 |
| SC04 | 선배는 이미 알고 있었나요? |
| SC05 | 조금 특별한 부탁 |
| SC06 | 가까워지면 달라지는 것 |
| SC07 | 기다리는 사람의 마음 |
| SC08 | 다음 페이지에는 |

### R02 일러스트·표정 예정 위치

| 원고 행 | 씬 | 콘티 |
|---|---|---|
| L78 | SC01 | [LD] 로만 · 기본 미소 |
| L376 | SC02 | [LD] 로만 · 당황 |
| L601 | SC03 | [SD EVENT] `roman_r02_puppy_encounter` |
| L603 | SC03 | [연출] 작은 강아지 앞에 쪼그려 앉은 로만이 환하게 웃는 SD 이벤트 일러스트 1장. 주인공은 화면 밖에 있으며, 강아지 보호자는 그리지 않거나 화면 가장자리만 표시. |
| L658 | SC03 | [전환] 일반 LD |
| L1042 | SC05 | [LD] 로만 · 기본 |
| L1044 | SC05 | [ANIM] 느린 눈 깜빡임, 미세 호흡 |
| L1320 | SC06 | [ANIM] 로만 · 눈 깜빡임, 머리카락 미세 움직임 |
| L1417 | SC06 | [LD] 로만 · 당황 |
| L1847 | SC08 | [LD] 로만 · 기본 미소 |
| L2017 | SC08 | [ANIM] 로만 눈 깜빡임 후 홍조 표정 전환 |

### R03 「말하지 않아도 알 거라고 생각했어요」

원고 SHA-256: `7695db26f758c70f9af7831ba06e474766d0ca7d775f12e81b01c7238090dd72`

| 씬 | 제목 |
|---|---|
| SC01 | 조금 늦은 답장 |
| SC02 | 기다리지 않아도 괜찮다면서 |
| SC03 | 그 사람이 싫어진 건 아닌데 |
| SC04 | 보내지 못한 메시지 |
| SC05 | 말하지 않아도 알 줄 알았어요 |
| SC06 | 필요한 건 대답이 아니라 |
| SC07 | 조금 이기적이어도 될까요? |
| SC08 | 아직 보내지 않은 문장 |

### R03 일러스트·표정 예정 위치

| 원고 행 | 씬 | 콘티 |
|---|---|---|
| L601 | SC04 | [연출] 일반적인 주인공 독백창 대신 로만의 내면 장면임을 구분하는 화면 전환. 새로운 CG나 애니메이션 필수 아님. |
| L1420 | SC07 | [표정] 로만 · 놀람 → 수줍은 미소 |

## 선택지와 수치

모든 선택지 보상은 기존 `story_apply` 한 번으로 묶어 적용합니다. 원고의 `roman_affection += N` / `roman_trust += N`은 전역 호감도·신뢰도에 5배 단위로 반영됩니다. 예: 원고 +2는 UI 수치 +10입니다. 그 외 `roman_*` 누적 카운터는 원고의 정수 그대로 유지합니다. R01 선택지 3의 `호감 +2 · roman_affection += 2`는 같은 보상의 중복 설명으로 한 번(+10)만 반영합니다.

| ID | 선택 | 호감 원고 단위 | 신뢰 원고 단위 | 플래그·카운터 |
|---|---|---:|---:|---|
| roman_r01_choice01_a | 저는 일상 소설이 끌리네요. | 0 | 0 | {'roman_r01_book_choice': 'daily'} |
| roman_r01_choice01_b | 이 단편집도 재미있어 보이는데요? | 0 | 0 | {'roman_r01_book_choice': 'mystery'} |
| roman_r01_choice01_c | 로만 씨가 좋아하시는 책을 같이 읽고 싶어요. | 0 | 0 | {'roman_r01_book_choice': 'recommendation'} |
| roman_r01_choice02_a | 다른 해석을 듣는 게 재미있어요. | 0 | 0 | {'roman_mutual_understanding': '+1'} |
| roman_r01_choice02_b | 로만 씨는 생각을 깊이 하시는 것 같아요. | 1 | 0 | {} |
| roman_r01_choice02_c | 로만 씨가 좋아하시는 해석을 더 듣고 싶어요. | 0 | 0 | {'roman_shared_reading': '+1'} |
| roman_r01_choice03_a | 서로 다른 생각도 편하게 이야기해요. | 0 | 2 | {'roman_mutual_respect': '+1'} |
| roman_r01_choice03_b | 로만 씨 글을 앞으로도 읽고 싶어요. | 2 | 0 | {} |
| roman_r01_choice03_c | 다른 사람보다 제가 먼저 읽어드릴게요. | 0 | 0 | {'roman_first_reader_promise': True} |
| roman_r02_choice01_a | 저도 좋은 걸 보면 로만 씨가 생각날 때가 있어요. | 2 | 0 | {} |
| roman_r02_choice01_b | 이렇게 편하게 이야기해 주셔서 좋아요. | 0 | 2 | {} |
| roman_r02_choice01_c | 그럼 다음에는 제가 먼저 좋은 장소를 찾아볼게요. | 0 | 0 | {'roman_next_date_promise': True} |
| roman_r02_choice02_a | 늦을 수는 있지만, 서로 편한 시간에 이야기해요. | 0 | 0 | {'roman_mutual_respect': '+2'} |
| roman_r02_choice02_b | 걱정되시면 언제든 물어보셔도 돼요. | 0 | 0 | {'roman_reassurance': '+1'} |
| roman_r02_choice02_c | 앞으로는 로만 씨를 기다리게 하지 않을게요. | 0 | 0 | {'roman_unrealistic_promise': '+1'} |
| roman_r03_choice01_a | 서로 필요한 걸 직접 이야기하자. | 0 | 0 | {'roman_r03_conflict_resolved': True, 'roman_mutual_respect': '+2'} |
| roman_r03_choice01_b | 로만 씨가 외롭지 않게 내가 더 자주 연락하겠다. | 0 | 0 | {'roman_r03_conflict_resolved': False, 'roman_reassurance_dependency': '+1'} |
| roman_r03_choice01_c | 이제는 아무 걱정도 하지 않아도 된다고 약속한다. | 0 | 0 | {'roman_r03_conflict_resolved': False, 'roman_reassurance_dependency': '+2', 'roman_unrealistic_promise': '+1'} |
| roman_r03_choice02_a | 로만 씨가 쓰고 싶은 이야기라면 존중하고 싶어요. | 0 | 0 | {'roman_creative_autonomy': '+2'} |
| roman_r03_choice02_b | 읽어보면 제 생각도 솔직하게 말씀드릴게요. | 0 | 0 | {'roman_mutual_understanding': '+1'} |
| roman_r03_choice02_c | 로만 씨가 쓰신 글이라면 뭐든 좋아할 것 같아요. | 0 | 0 | {'roman_approval_dependency': '+1'} |

R03 SC07·SC08은 `roman_r03_conflict_resolved`에 따라 대화가 달라집니다. A에서 True, B/C에서 False이며 후반 루트가 같은 값을 이어받습니다. 새 변수는 최초 도입 파일 한 곳에만 `default`로 선언했습니다.

## 휴대폰과 서술

보낸 메시지는 기존 로만 개인방 UI를 사용하며, 독백·서술은 기본 대사창으로 출력합니다. R03 SC02의 지운 작성문과 SC04의 미전송 두 문장은 채팅방에 발송되지 않도록 narrator로 출력합니다. 휴대폰 화면 중 육성 혼잣말도 채팅 로그에 기록하지 않습니다. R03 SC04의 로만 시점은 콘티에 명시되어 있습니다. 기존 메신저의 주인공 기준 좌우 정렬은 유지되므로, 향후 로만 POV 전용 휴대폰 구도를 만들 때 해당 구간을 별도로 다듬을 수 있습니다. 보호자·안내 방송은 기존 narrator 대사에 발신자 이름을 붙여 구분합니다.

## 효과음·아트 작업

휴대폰 개인방 시작은 기존 알림 효과음을 사용합니다. 원고의 강아지·스피커·책장 소리처럼 현재 없는 효과음은 SOURCE 콘티로 보존했습니다. 모든 스탠딩·SD·LD·미세 애니메이션 지시는 주석이며, 추후 에셋과 실제 연출을 추가할 때 해당 행을 교체하면 됩니다. 이번 단계에 새 이미지·스탠딩 표시 호출은 0개입니다.

## 재생성·검증

원고를 수정한 경우 D드라이브 SDK Python으로 `D:/CampusRomance_VN/tools/import_roman_first.py --write`를 실행합니다. 이 도구는 세 개의 소유 route 파일과 import audit만 갱신합니다. 이후 전체 프로젝트의 Ren'Py Lint와 저장·분기 테스트는 별도로 수행해야 합니다.

- `ROMAN_R01_R03_IMPORT_AUDIT.json`: 원고 행별 대사·선택지·효과·콘티 구조
- `ROMAN_R01_R03_STATIC_CHECK.json`: 생성 rpy와 원고 매핑 대사 1,878줄 일치, SOURCE 행 중복 0, Python 단문 구문 검사, 메뉴 7개/응답 21개, 실제 아트 표시 호출 0, 소유 default 중복 0
- 이 문서의 정적 검사는 원본 게임을 실행하지 않았습니다. Ren'Py 네이티브 실행 검증 결과는 통합 QA 기록을 따릅니다.
