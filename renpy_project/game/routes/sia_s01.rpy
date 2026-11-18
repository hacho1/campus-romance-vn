# Sia S01 · confirmed manuscript, text-first storyboard
# SOURCE: design_docs/story_sources/sia_s01.txt
# SHA256: 639f456ccd9bbeee488ab17f82b12cb0d29c6a4e7501660e27528cd6d2251280
# Rebuild only these two route files: tools/import_sia_first.py --write
# LD/SD/CG directions remain comments until the artwork pass.

default sia_s01_feedback_choice = None
default sia_creative_confidence = 0
default sia_s01_episode_draft_complete = False
default sia_s01_next_date_promise = False
default sia_s01_complete = False
default sia_webtoon_first_reader = False

label sia_s01:
    $ phone_timeline_enter("S01", "sia_s01")
    $ sia_begin_episode("S01", "내 웹툰의 첫 번째 독자")
    jump sia_s01_sc01

label sia_s01_sc01:
    $ phone_timeline_enter("S01", "sia_s01_sc01")
    # SOURCE S01 L27 SCENE 01. 천재 작가님의 긴급 호출
    # SOURCE S01 L29 [BG] 주인공 방 · 늦은 오전
    $ sia_draft_scene("주인공 방 · 늦은 오전")
    # SOURCE S01 L31 [BGM] Ordinary Campus
    $ story_draft_bgm("Ordinary Campus")
    # SOURCE S01 L33 # CONTI [FADE IN]
    # SOURCE S01 L37
    narrator "축제가 끝난 뒤로 캠퍼스는 평소의 모습으로 돌아왔다."
    # SOURCE S01 L39
    narrator "어제는 과제 때문에 바빴고, 오늘도 슬슬 다음 주 일정을 정리해야 한다."
    # SOURCE S01 L41
    narrator "그런데 요즘에는 강의와 과제 말고도 기다려지는 일이 하나 생겼다."
    # SOURCE S01 L43
    narrator "시아 씨가 보내는 메시지다."
    # SOURCE S01 L45 # CONTI [SFX] 휴대전화 진동
    # SOURCE S01 L47 # CONTI [UI] 시아 개인 메시지
    $ story_chat(True, title="시아")
    # SOURCE S01 L50 (시아)
    sia "야"
    # SOURCE S01 L52 (시아)
    sia "긴급상황"
    # SOURCE S01 L55 (주인공 · 메시지)
    mc "무슨 일이세요?"
    # SOURCE S01 L58 (시아)
    sia "내가 엄청난 걸 만들어버림"
    # SOURCE S01 L61 (주인공 · 메시지)
    mc "어떤 건데요?"
    # SOURCE S01 L64 (시아)
    sia "말로 설명하기엔 너무 대단함"
    # SOURCE S01 L67 (주인공 · 메시지)
    mc "……또 무슨 장난이에요?"
    # SOURCE S01 L70 (시아)
    sia "야ㅋㅋㅋㅋ"
    # SOURCE S01 L72 (시아)
    sia "이번엔 진짜라니까"
    # SOURCE S01 L75 (시아)
    sia "오늘 시간 됨?"
    # SOURCE S01 L78 (주인공 · 메시지)
    mc "오후에는 괜찮아요."
    # SOURCE S01 L81 (시아)
    sia "그럼 작업실로 와"
    # SOURCE S01 L83 (시아)
    sia "천재 작가님의 신작 시사회임"
    # SOURCE S01 L86 (주인공 · 메시지)
    mc "지난번에 보여주신 웹툰의 다음 편인가요?"
    # SOURCE S01 L89 (시아)
    sia "오"
    # SOURCE S01 L91 (시아)
    sia "눈치 빠른데?"
    # SOURCE S01 L93 (시아)
    sia "맞음"
    # SOURCE S01 L96 (시아)
    sia "근데 이번 건 아직 아무한테도 안 보여줬어"
    # SOURCE S01 L100
    narrator "아무에게도 보여주지 않은 새 원고."
    # SOURCE S01 L102
    narrator "지난번 작업실에서 봤던 웹툰이 떠올랐다."
    # SOURCE S01 L104
    narrator "서로 다른 성격의 두 캐릭터가 티격태격하면서 사건을 해결하는 이야기."
    # SOURCE S01 L106
    narrator "시아 씨는 그 작품에 대해 이야기할 때만큼은 평소보다 훨씬 진지했다."
    # SOURCE S01 L109 (주인공 · 메시지)
    mc "그럼 제대로 읽어볼게요."
    # SOURCE S01 L112 (시아)
    sia "좋아"
    # SOURCE S01 L114 (시아)
    sia "근데 재미없으면 재미없다고 해라"
    # SOURCE S01 L116 (시아)
    sia "천재도 가끔 실수하니까"
    # SOURCE S01 L119 (주인공 · 메시지)
    mc "시아 씨가 그런 말씀도 하시네요."
    # SOURCE S01 L122 (시아)
    sia "야"
    # SOURCE S01 L124 (시아)
    sia "취소"
    # SOURCE S01 L126 (시아)
    sia "나는 실수 안 함"
    # SOURCE S01 L130
    narrator "……역시."
    # SOURCE S01 L132 # CONTI [TRANSITION] 오후 1:50
    $ phone_timeline_cue("S01", "S01_L132")
    $ story_chat(False)
    # SOURCE S01 L134 [BG] 애니메이션학과 건물 · 복도
    $ sia_draft_scene("애니메이션학과 건물 · 복도")
    # SOURCE S01 L136 [BGM] Light Campus
    $ story_draft_bgm("Light Campus")
    # SOURCE S01 L140
    narrator "애니메이션학과 건물에 도착했다."
    # SOURCE S01 L142
    narrator "복도 한쪽에는 학생들의 작품이 붙어 있었고, 작업실 안쪽에서는 누군가 그림을 그리는 소리가 들렸다."
    # SOURCE S01 L144
    narrator "나는 시아 씨에게 메시지를 보냈다."
    $ story_chat(True, title="시아")
    # SOURCE S01 L147 (주인공 · 메시지)
    mc "시아 씨, 작업실 앞에 도착했어요."
    # SOURCE S01 L150 (시아)
    sia "오"
    # SOURCE S01 L152 (시아)
    sia "들어와"
    # SOURCE S01 L154 (시아)
    sia "자리는 이미 준비해뒀다"
    # SOURCE S01 L158
    narrator "자리까지?"
    # SOURCE S01 L160
    narrator "대체 뭘 준비한 거지."
    # SOURCE S01 L162
    narrator "나는 문을 열었다."
    # SOURCE S01 L164 # CONTI [SCENE 01 END]
    $ story_chat(False)
    jump sia_s01_sc02

label sia_s01_sc02:
    $ phone_timeline_enter("S01", "sia_s01_sc02")
    # SOURCE S01 L168 SCENE 02. 첫 독자의 특권
    # SOURCE S01 L170 [BG] 애니메이션학과 작업실 · 오후
    $ sia_draft_scene("애니메이션학과 작업실 · 오후")
    # SOURCE S01 L172 [BGM] Creative Afternoon
    $ story_draft_bgm("Creative Afternoon")
    # SOURCE S01 L174 # CONTI [LD] 시아 · 장난스러운 미소
    # SOURCE S01 L177 (시아)
    sia "어서 오시게, 감상 담당."
    # SOURCE S01 L180 (주인공)
    mc "안녕하세요, 천재 작가님."
    # SOURCE S01 L183 (시아)
    sia "오."
    # SOURCE S01 L185 (시아)
    sia "오늘은 호칭이 마음에 드는데?"
    # SOURCE S01 L189
    narrator "시아 씨는 의자를 하나 끌어왔다."
    # SOURCE S01 L191
    narrator "책상 위에는 태블릿과 스케치북, 비어 있는 음료 컵이 놓여 있었다."
    # SOURCE S01 L194 (시아)
    sia "자, 여기 앉아."
    # SOURCE S01 L197 (주인공)
    mc "정말 준비해두셨네요."
    # SOURCE S01 L200 (시아)
    sia "당연하지."
    # SOURCE S01 L202 (시아)
    sia "VIP석이거든."
    # SOURCE S01 L205 (주인공)
    mc "다른 좌석도 있나요?"
    # SOURCE S01 L208 (시아)
    sia "없어."
    # SOURCE S01 L211 (주인공)
    mc "그럼 그냥 의자 아닌가요?"
    # SOURCE S01 L214 (시아)
    sia "……."
    # SOURCE S01 L216 (시아)
    sia "너 오늘 시작부터 너무 날카로운데?"
    # SOURCE S01 L220
    narrator "시아 씨는 웃으며 태블릿을 돌렸다."
    # SOURCE S01 L222
    narrator "화면에는 전에 봤던 웹툰의 두 주인공이 등장했다."
    # SOURCE S01 L224
    narrator "제목은 여전히 「우당탕탕, 둘이서」."
    # SOURCE S01 L226
    narrator "하지만 이번에는 새로운 장면이 추가되어 있었다."
    # SOURCE S01 L229 (시아)
    sia "지난번에 본 게 첫 번째 이야기였잖아."
    # SOURCE S01 L232 (주인공)
    mc "네. 두 사람이 함께 사건을 해결하던 내용이었죠."
    # SOURCE S01 L235 (시아)
    sia "맞아."
    # SOURCE S01 L237 (시아)
    sia "이번에는 그다음 날 이야기야."
    # SOURCE S01 L240 (주인공)
    mc "어떤 사건이 생기나요?"
    # SOURCE S01 L243 (시아)
    sia "그건 직접 보셔야죠, 손님."
    # SOURCE S01 L246 (주인공)
    mc "방금은 감상 담당이라고 하셨잖아요."
    # SOURCE S01 L249 (시아)
    sia "아 진짜ㅋㅋ"
    # SOURCE S01 L251 (시아)
    sia "그냥 읽어!"
    # SOURCE S01 L255
    narrator "나는 화면을 바라봤다."
    # SOURCE S01 L257
    narrator "첫 장면은 작은 방이었다."
    # SOURCE S01 L259
    narrator "활발한 성격의 캐릭터가 무언가를 잔뜩 준비하고 있었고, 차분한 캐릭터는 그 모습을 보며 한숨을 쉬고 있었다."
    # SOURCE S01 L261
    narrator "두 사람은 함께 대회에 참가하기로 했지만, 준비 방법을 두고 의견이 갈리고 있었다."
    # SOURCE S01 L263
    narrator "활발한 캐릭터는 일단 해보자고 했고."
    # SOURCE S01 L265
    narrator "차분한 캐릭터는 계획부터 세워야 한다고 주장했다."
    # SOURCE S01 L269
    narrator "처음에는 익숙한 티격태격이었다."
    # SOURCE S01 L271
    narrator "그런데 이야기가 진행될수록 분위기가 달라졌다."
    # SOURCE S01 L273
    narrator "활발한 캐릭터는 상대가 자신을 믿지 않는다고 생각했다."
    # SOURCE S01 L275
    narrator "차분한 캐릭터는 상대가 자기 의견을 무시한다고 생각했다."
    # SOURCE S01 L277
    narrator "결국 두 사람은 크게 다투고 각자 다른 방향으로 걸어갔다."
    # SOURCE S01 L280 (주인공)
    mc "……어."
    # SOURCE S01 L283 (시아)
    sia "왜?"
    # SOURCE S01 L286 (주인공)
    mc "이번에는 조금 진지한 이야기네요."
    # SOURCE S01 L289 (시아)
    sia "그치?"
    # SOURCE S01 L291 (시아)
    sia "첫 번째는 그냥 둘이 잘 맞는다는 걸 보여주려고 했거든."
    # SOURCE S01 L294 (주인공)
    mc "이번에는 안 맞는 부분을 보여주시는 거군요."
    # SOURCE S01 L297 (시아)
    sia "오."
    # SOURCE S01 L299 (시아)
    sia "맞아."
    # SOURCE S01 L303
    narrator "시아 씨는 잠깐 웃었다."
    # SOURCE S01 L306 (시아)
    sia "둘이 성격이 다르잖아."
    # SOURCE S01 L308 (시아)
    sia "그런데 맨날 장난만 치면서 잘 지내면 좀 이상하지 않냐?"
    # SOURCE S01 L311 (주인공)
    mc "그러네요."
    # SOURCE S01 L314 (시아)
    sia "그래서 한 번쯤 진짜 싸우는 장면도 넣어보고 싶었어."
    # SOURCE S01 L318
    narrator "나는 다음 장면으로 넘겼다."
    # SOURCE S01 L320
    narrator "서로 떨어져 있던 두 사람이 우연히 같은 장소에 도착했다."
    # SOURCE S01 L322
    narrator "둘은 상대를 발견하고 잠시 멈췄다."
    # SOURCE S01 L324
    narrator "한 명이 먼저 입을 열었다."
    # SOURCE S01 L326
    narrator "하지만 다음 컷에서 이야기는 멈춰 있었다."
    # SOURCE S01 L328 # CONTI [UI] 웹툰 마지막 컷 · 미완성
    # SOURCE S01 L332
    narrator "말풍선이 비어 있었다."
    # SOURCE S01 L335 (주인공)
    mc "……여기가 마지막인가요?"
    # SOURCE S01 L338 (시아)
    sia "응."
    # SOURCE S01 L341 (주인공)
    mc "아직 대사를 안 넣으셨네요."
    # SOURCE S01 L344 (시아)
    sia "……."
    # SOURCE S01 L346 (시아)
    sia "그게 문제야."
    # SOURCE S01 L350
    narrator "시아 씨는 태블릿을 다시 자기 쪽으로 돌렸다."
    # SOURCE S01 L353 (시아)
    sia "여기서 무슨 말을 해야 할지 모르겠거든."
    # SOURCE S01 L356 (주인공)
    mc "화해하는 장면인가요?"
    # SOURCE S01 L359 (시아)
    sia "그럴 생각이긴 한데……."
    # SOURCE S01 L362 (시아)
    sia "그냥 '미안해' 한마디로 끝내기에는 좀 이상하잖아."
    # SOURCE S01 L366
    narrator "시아 씨는 화면을 바라봤다."
    # SOURCE S01 L368
    narrator "늘 장난스럽던 표정이 조금 진지해졌다."
    # SOURCE S01 L371 (시아)
    sia "난 둘이 제대로 이야기했으면 좋겠어."
    # SOURCE S01 L373 (시아)
    sia "근데 그게 생각보다 어렵네."
    # SOURCE S01 L375 # CONTI [SCENE 02 END]
    jump sia_s01_sc03

label sia_s01_sc03:
    $ phone_timeline_enter("S01", "sia_s01_sc03")
    # SOURCE S01 L379 SCENE 03. 그 장면은 좀 이상하지 않아?
    # SOURCE S01 L381 [BG] 애니메이션학과 작업실 · 오후
    $ sia_draft_scene("애니메이션학과 작업실 · 오후")
    # SOURCE S01 L383 [BGM] Playful Discussion
    $ story_draft_bgm("Playful Discussion")
    # SOURCE S01 L387
    narrator "시아 씨는 다시 태블릿을 내 쪽으로 돌렸다."
    # SOURCE S01 L390 (시아)
    sia "자."
    # SOURCE S01 L392 (시아)
    sia "그래서 첫 독자의 의견이 필요하다는 말씀."
    # SOURCE S01 L395 (주인공)
    mc "어떤 부분이 가장 고민이세요?"
    # SOURCE S01 L398 (시아)
    sia "대사."
    # SOURCE S01 L400 (시아)
    sia "특히 누가 먼저 말을 거느냐."
    # SOURCE S01 L403 (주인공)
    mc "음……."
    # SOURCE S01 L407
    narrator "나는 마지막 몇 컷을 다시 읽었다."
    # SOURCE S01 L409
    narrator "두 캐릭터 모두 자신이 잘못한 부분이 있었다."
    # SOURCE S01 L411
    narrator "그런데 한 명만 먼저 사과하면 모든 문제가 해결되는 것처럼 보일 수도 있겠다."
    # SOURCE S01 L414 (주인공)
    mc "둘 다 하고 싶은 말이 있어 보이는데요."
    # SOURCE S01 L417 (시아)
    sia "그치?"
    # SOURCE S01 L420 (주인공)
    mc "그럼 누가 먼저 말하느냐보다, 상대가 뭐라고 대답하는지가 더 중요하지 않을까요?"
    # SOURCE S01 L423 (시아)
    sia "……."
    # SOURCE S01 L425 (시아)
    sia "오."
    # SOURCE S01 L429
    narrator "시아 씨가 화면을 바라봤다."
    # SOURCE S01 L432 (시아)
    sia "그거 괜찮은데?"
    # SOURCE S01 L435 (주인공)
    mc "한 명이 먼저 말을 꺼내고, 다른 한 명도 자기 잘못을 인정하면 어떨까요?"
    # SOURCE S01 L438 (시아)
    sia "……음."
    # SOURCE S01 L440 (시아)
    sia "근데 그럼 너무 착하게만 끝나지 않냐?"
    # SOURCE S01 L443 (주인공)
    mc "꼭 그렇게 끝날 필요는 없죠."
    # SOURCE S01 L445 (주인공)
    mc "사과하고 나서도 서로 생각이 다를 수 있으니까요."
    # SOURCE S01 L448 (시아)
    sia "……."
    # SOURCE S01 L451 (시아)
    sia "야."
    # SOURCE S01 L454 (주인공)
    mc "네?"
    # SOURCE S01 L457 (시아)
    sia "너 은근 스토리 잘 짠다?"
    # SOURCE S01 L460 (주인공)
    mc "그 정도는 아닌데요."
    # SOURCE S01 L463 (시아)
    sia "아니, 진짜."
    # SOURCE S01 L465 (시아)
    sia "그런 방향은 생각 못 했어."
    # SOURCE S01 L469
    narrator "시아 씨는 태블릿에 몇 줄 적었다."
    # SOURCE S01 L471
    narrator "그러다가 다시 나를 바라봤다."
    # SOURCE S01 L474 (시아)
    sia "근데 여기서 주인공이 갑자기 울면 어떨까?"
    # SOURCE S01 L477 (주인공)
    mc "갑자기요?"
    # SOURCE S01 L480 (시아)
    sia "응."
    # SOURCE S01 L482 (시아)
    sia "그러면 상대가 당황해서……."
    # SOURCE S01 L485 (주인공)
    mc "시아 씨."
    # SOURCE S01 L488 (시아)
    sia "왜."
    # SOURCE S01 L491 (주인공)
    mc "그건 조금 갑작스럽지 않나요?"
    # SOURCE S01 L494 (시아)
    sia "……."
    # SOURCE S01 L497 (시아)
    sia "쳇."
    # SOURCE S01 L501
    narrator "시아 씨가 장난스럽게 입술을 삐죽 내밀었다."
    # SOURCE S01 L504 (시아)
    sia "너 내 아이디어 너무 쉽게 반대하는 거 아니냐?"
    # SOURCE S01 L507 (주인공)
    mc "시아 씨가 솔직하게 말씀해 달라고 하셨잖아요."
    # SOURCE S01 L510 (시아)
    sia "……."
    # SOURCE S01 L512 (시아)
    sia "맞네."
    # SOURCE S01 L516
    narrator "시아 씨는 웃음을 터뜨렸다."
    # SOURCE S01 L519 (시아)
    sia "ㅋㅋㅋ 아, 진짜."
    # SOURCE S01 L521 (시아)
    sia "반박을 못 하겠네."
    # SOURCE S01 L525
    narrator "잠시 뒤 시아 씨는 다시 화면을 바라봤다."
    # SOURCE S01 L528 (시아)
    sia "근데 진짜로 물어보자."
    # SOURCE S01 L531 (주인공)
    mc "네."
    # SOURCE S01 L534 (시아)
    sia "내가 방금 말한 장면, 왜 별로라고 생각했어?"
    # SOURCE S01 L537 (주인공)
    mc "지금까지 두 캐릭터가 갈등을 해결하는 방식과 조금 다르니까요."
    # SOURCE S01 L539 (주인공)
    mc "갑자기 울기보다, 평소와 다르게 솔직하게 이야기하는 게 더 의미 있을 것 같아요."
    # SOURCE S01 L542 (시아)
    sia "……."
    # SOURCE S01 L545 (시아)
    sia "그렇구나."
    # SOURCE S01 L549
    narrator "시아 씨는 잠시 생각했다."
    # SOURCE S01 L551
    narrator "그러더니 펜을 들고 마지막 컷의 구도를 조금 고쳤다."
    # SOURCE S01 L554 (시아)
    sia "그럼 울지는 말고."
    # SOURCE S01 L556 (시아)
    sia "둘 다 서로 쳐다보면서 이야기하게 해볼까."
    # SOURCE S01 L559 (주인공)
    mc "좋아요."
    # SOURCE S01 L562 (시아)
    sia "대신 마지막에 웃기는 대사 하나는 넣을 거야."
    # SOURCE S01 L565 (주인공)
    mc "그건 꼭 필요한가요?"
    # SOURCE S01 L568 (시아)
    sia "당연하지."
    # SOURCE S01 L570 (시아)
    sia "내 만화잖아."
    # SOURCE S01 L574
    narrator "시아 씨는 자신만만하게 웃었다."
    # SOURCE S01 L577 (시아)
    sia "진지한 얘기했다고 갑자기 내 만화가 다른 작품이 되면 안 되지."
    # SOURCE S01 L580 (주인공)
    mc "그건 맞네요."
    # SOURCE S01 L583 (시아)
    sia "봤지?"
    # SOURCE S01 L585 (시아)
    sia "천재 작가님은 다 계획이 있다고."
    # SOURCE S01 L588 (주인공)
    mc "아까는 결말을 못 정하셨다면서요?"
    # SOURCE S01 L591 (시아)
    sia "……."
    # SOURCE S01 L593 (시아)
    sia "야, 그 얘기는 잊어라."
    # SOURCE S01 L597
    narrator "결국 나는 웃음을 참지 못했다."
    # SOURCE S01 L599
    narrator "시아 씨도 같이 웃었다."
    # SOURCE S01 L601 # CONTI [SCENE 03 END]
    jump sia_s01_sc04

label sia_s01_sc04:
    $ phone_timeline_enter("S01", "sia_s01_sc04")
    # SOURCE S01 L605 SCENE 04. 천재 작가도 배가 고프다
    # SOURCE S01 L607 # CONTI [TIME] 오후 3:10 · 작업실 → 학교 앞 분식집 · SD 이벤트 1장
    $ phone_timeline_cue("S01", "S01_L607")
    # SOURCE S01 L609 # CONTI [HEADING] S01 SC04 · 천재 작가도 배가 고프다
    # SOURCE S01 L611 [BG] 애니메이션학과 작업실 · 오후
    $ sia_draft_scene("애니메이션학과 작업실 · 오후")
    # SOURCE S01 L613 [BGM] Light Comedy
    $ story_draft_bgm("Light Comedy")
    # SOURCE S01 L617
    narrator "웹툰 이야기를 나누다 보니 어느새 한 시간이 넘게 지났다."
    # SOURCE S01 L619
    narrator "시아 씨는 마지막 컷을 몇 번이나 다시 그렸다."
    # SOURCE S01 L621
    narrator "인물의 눈썹을 조금 올리기도 하고, 말풍선 위치를 바꾸기도 했다."
    # SOURCE S01 L623
    narrator "그런데 작업에 집중하던 시아 씨의 표정이 갑자기 굳었다."
    # SOURCE S01 L626 (시아)
    sia "……."
    # SOURCE S01 L629 (주인공)
    mc "왜 그러세요?"
    # SOURCE S01 L632 (시아)
    sia "큰일 났어."
    # SOURCE S01 L635 (주인공)
    mc "무슨 일이에요?"
    # SOURCE S01 L638 (시아)
    sia "……."
    # SOURCE S01 L641 (시아)
    sia "배고파."
    # SOURCE S01 L645
    narrator "……."
    # SOURCE S01 L647
    narrator "정말 큰일이긴 하네."
    # SOURCE S01 L650 (주인공)
    mc "점심 안 드셨어요?"
    # SOURCE S01 L653 (시아)
    sia "응."
    # SOURCE S01 L655 (시아)
    sia "조금만 그리고 먹으려고 했는데."
    # SOURCE S01 L658 (주인공)
    mc "그 조금이 몇 시간이었는데요?"
    # SOURCE S01 L661 (시아)
    sia "……."
    # SOURCE S01 L663 (시아)
    sia "그런 건 묻지 마."
    # SOURCE S01 L667
    narrator "시아 씨는 의자 등받이에 몸을 기댔다."
    # SOURCE S01 L670 (시아)
    sia "아아아."
    # SOURCE S01 L672 (시아)
    sia "천재 작가님이 굶어 죽는다."
    # SOURCE S01 L675 (주인공)
    mc "그러니까 밥을 드셔야죠."
    # SOURCE S01 L678 (시아)
    sia "야, 밥 먹으러 가자."
    # SOURCE S01 L681 (주인공)
    mc "좋아요. 어디로 갈까요?"
    # SOURCE S01 L684 (시아)
    sia "떡볶이."
    # SOURCE S01 L687 (주인공)
    mc "바로 정하시네요."
    # SOURCE S01 L690 (시아)
    sia "중요한 건 빠르게 정하는 편이거든."
    # SOURCE S01 L694
    narrator "웹툰 결말은 한 시간 넘게 고민하시던데."
    # SOURCE S01 L696
    narrator "……그건 말하지 말자."
    # SOURCE S01 L698 # CONTI [TRANSITION] 오후 3:25
    $ phone_timeline_cue("S01", "S01_L698")
    # SOURCE S01 L700 [BG] 학교 앞 분식집 · 오후
    $ sia_draft_scene("학교 앞 분식집 · 오후")
    # SOURCE S01 L702 [BGM] Playful Lunch
    $ story_draft_bgm("Playful Lunch")
    # SOURCE S01 L706
    narrator "분식집에 도착하자 시아 씨는 메뉴판을 보지도 않고 주문했다."
    # SOURCE S01 L709 (시아)
    sia "떡볶이 하나, 튀김 하나, 김밥도 하나!"
    # SOURCE S01 L712 (주인공)
    mc "다 드실 수 있으세요?"
    # SOURCE S01 L715 (시아)
    sia "당연하지."
    # SOURCE S01 L718 (주인공)
    mc "저도 같이 먹는 걸로 계산하신 거죠?"
    # SOURCE S01 L721 (시아)
    sia "……."
    # SOURCE S01 L723 (시아)
    sia "어?"
    # SOURCE S01 L727
    narrator "시아 씨가 잠깐 멈췄다."
    # SOURCE S01 L730 (시아)
    sia "아."
    # SOURCE S01 L732 (시아)
    sia "맞네."
    # SOURCE S01 L735 (주인공)
    mc "설마 혼자 다 드시려고 하셨어요?"
    # SOURCE S01 L738 (시아)
    sia "아니거든?"
    # SOURCE S01 L741 (시아)
    sia "너도 먹으라고 시킨 거거든?"
    # SOURCE S01 L745
    narrator "조금 전 반응과는 다른 이야기인데."
    # SOURCE S01 L748 (시아)
    sia "뭐야, 그 표정."
    # SOURCE S01 L751 (주인공)
    mc "아무 말도 안 했는데요."
    # SOURCE S01 L754 (시아)
    sia "눈으로 말했잖아!"
    # SOURCE S01 L758
    narrator "나는 결국 웃음을 터뜨렸다."
    # SOURCE S01 L760 # CONTI [SFX] 음식 내려놓는 소리
    # SOURCE S01 L763 (직원)
    sia_staff "주문하신 음식 나왔습니다."
    # SOURCE S01 L766 (시아)
    sia "오오!"
    # SOURCE S01 L770
    narrator "시아 씨의 관심은 순식간에 음식으로 옮겨갔다."
    # SOURCE S01 L773 (시아)
    sia "야, 먹자."
    # SOURCE S01 L776 (주인공)
    mc "네. 잘 먹겠습니다."
    # SOURCE S01 L778 # CONTI [시간 경과 · 오후 3:40]
    $ phone_timeline_cue("S01", "S01_L778")
    # SOURCE S01 L782
    narrator "우리는 음식을 먹으며 작업실에서 있었던 이야기를 이어갔다."
    # SOURCE S01 L784
    narrator "시아 씨는 웹툰에 넣을 개그 장면을 몇 개 더 생각해냈다."
    # SOURCE S01 L786
    narrator "그중 일부는 꽤 재미있었다."
    # SOURCE S01 L788
    narrator "그리고 일부는……"
    # SOURCE S01 L791 (시아)
    sia "야, 이번엔 주인공이 문 열자마자 떡볶이가 쏟아지는 거야."
    # SOURCE S01 L794 (주인공)
    mc "왜 하필 떡볶이예요?"
    # SOURCE S01 L797 (시아)
    sia "지금 먹고 있잖아."
    # SOURCE S01 L800 (주인공)
    mc "그게 이유예요?"
    # SOURCE S01 L803 (시아)
    sia "충분한 이유 아니냐?"
    # SOURCE S01 L807
    narrator "시아 씨는 너무 당당했다."
    # SOURCE S01 L810 (주인공)
    mc "그럼 나중에 김밥도 등장하겠네요."
    # SOURCE S01 L813 (시아)
    sia "오."
    # SOURCE S01 L815 (시아)
    sia "너 천재냐?"
    # SOURCE S01 L818 (주인공)
    mc "……."
    # SOURCE S01 L821 (시아)
    sia "야, 잠깐만."
    # SOURCE S01 L824 (시아)
    sia "진짜 넣어볼까?"
    # SOURCE S01 L827 (주인공)
    mc "시아 씨, 제발요."
    # SOURCE S01 L830 (시아)
    sia "ㅋㅋㅋㅋㅋ"
    # SOURCE S01 L832 # CONTI [SD EVENT] `sia_s01_food_comedy`
    # SOURCE S01 L834 # CONTI [연출] 분식집 테이블 앞에서 아이디어가 떠올랐다며 신나 하는 시아와 떡볶이·김밥·튀김이 놓인 상황을 담은 완성형 SD 1장. 주인공 외형은 표시하지 않는다.
    # SOURCE S01 L836 # CONTI [전환] 일반 LD
    # SOURCE S01 L840
    narrator "시아 씨는 한참 웃었다."
    # SOURCE S01 L842
    narrator "그러다가 젓가락을 내려놓았다."
    # SOURCE S01 L845 (시아)
    sia "근데 진짜 신기하다."
    # SOURCE S01 L848 (주인공)
    mc "뭐가요?"
    # SOURCE S01 L851 (시아)
    sia "나 원래 작업하다 막히면 혼자 엄청 끙끙대거든."
    # SOURCE S01 L854 (주인공)
    mc "네."
    # SOURCE S01 L857 (시아)
    sia "근데 오늘은 너랑 떠드니까 아이디어가 계속 나오네."
    # SOURCE S01 L860 (주인공)
    mc "그럼 도움이 된 건가요?"
    # SOURCE S01 L863 (시아)
    sia "당연하지."
    # SOURCE S01 L865 (시아)
    sia "앞으로도 계속 부려먹어야겠다."
    # SOURCE S01 L868 (주인공)
    mc "……부려먹는다고요?"
    # SOURCE S01 L871 (시아)
    sia "응."
    # SOURCE S01 L874 (시아)
    sia "감상 담당 겸 아이디어 담당."
    # SOURCE S01 L877 (주인공)
    mc "월급은요?"
    # SOURCE S01 L880 (시아)
    sia "없어."
    # SOURCE S01 L883 (주인공)
    mc "그럼 퇴사하겠습니다."
    # SOURCE S01 L886 (시아)
    sia "야!!"
    # SOURCE S01 L890
    narrator "시아 씨가 크게 웃었다."
    # SOURCE S01 L893 (시아)
    sia "아, 진짜."
    # SOURCE S01 L895 (시아)
    sia "너랑 있으면 시간 금방 간다."
    # SOURCE S01 L899
    narrator "그 말을 듣고 잠깐 젓가락을 멈췄다."
    # SOURCE S01 L901
    narrator "시아 씨는 아무렇지도 않게 다시 떡볶이를 먹고 있었다."
    # SOURCE S01 L903
    narrator "……그냥 평범한 말이었겠지."
    # SOURCE S01 L905
    narrator "그런데 조금 기분이 좋았다."
    # SOURCE S01 L907 # CONTI [SCENE 04 END]
    jump sia_s01_sc05

label sia_s01_sc05:
    $ phone_timeline_enter("S01", "sia_s01_sc05")
    # SOURCE S01 L909 S01 SC05 · 웃기는 게 전부는 아니거든
    # SOURCE S01 L911 [BG] 캠퍼스 야외 벤치 · 늦은 오후
    $ sia_draft_scene("캠퍼스 야외 벤치 · 늦은 오후")
    # SOURCE S01 L913 [BGM] Gentle Afternoon
    $ story_draft_bgm("Gentle Afternoon")
    # SOURCE S01 L917
    narrator "분식집에서 나온 뒤 시아 씨와 함께 캠퍼스로 돌아왔다."
    # SOURCE S01 L919
    narrator "바로 작업실로 돌아가려고 했지만, 시아 씨가 잠깐 쉬었다 가자고 했다."
    # SOURCE S01 L921
    narrator "우리는 나무 그늘 아래 벤치에 앉았다."
    # SOURCE S01 L924 (시아)
    sia "으아."
    # SOURCE S01 L926 (시아)
    sia "살겠다."
    # SOURCE S01 L929 (주인공)
    mc "이제 좀 괜찮으세요?"
    # SOURCE S01 L932 (시아)
    sia "응. 배부르니까 세상이 아름답다."
    # SOURCE S01 L935 (주인공)
    mc "아까까지는 굶어 죽으신다면서요."
    # SOURCE S01 L938 (시아)
    sia "그건 과거의 나야."
    # SOURCE S01 L941 (주인공)
    mc "불과 한 시간 전인데요."
    # SOURCE S01 L944 (시아)
    sia "과거는 과거지."
    # SOURCE S01 L948
    narrator "시아 씨는 웃으며 음료를 한 모금 마셨다."
    # SOURCE S01 L950
    narrator "그러다가 휴대전화에 저장된 웹툰 장면을 다시 열었다."
    # SOURCE S01 L953 (시아)
    sia "……야."
    # SOURCE S01 L956 (주인공)
    mc "네?"
    # SOURCE S01 L959 (시아)
    sia "아까 그 장면 말인데."
    # SOURCE S01 L962 (주인공)
    mc "마지막에 두 사람이 화해하는 장면이요?"
    # SOURCE S01 L965 (시아)
    sia "응."
    # SOURCE S01 L968 (시아)
    sia "너는 그거 진짜 괜찮았어?"
    # SOURCE S01 L971 (주인공)
    mc "네. 다만 아직 완성된 건 아니니까 조금 더 봐야겠죠."
    # SOURCE S01 L974 (시아)
    sia "……맞지."
    # SOURCE S01 L978
    narrator "시아 씨는 고개를 끄덕였다."
    # SOURCE S01 L980
    narrator "잠깐 바람이 불었다."
    # SOURCE S01 L983 (시아)
    sia "사실 나 처음부터 만화 그리는 거 좋아했거든."
    # SOURCE S01 L986 (주인공)
    mc "그럴 것 같았어요."
    # SOURCE S01 L989 (시아)
    sia "학교에서도 맨날 낙서하고."
    # SOURCE S01 L991 (시아)
    sia "친구들 얼굴 이상하게 그려서 놀리고."
    # SOURCE S01 L994 (주인공)
    mc "지금도 그러시잖아요."
    # SOURCE S01 L997 (시아)
    sia "야ㅋㅋㅋ"
    # SOURCE S01 L1000 (시아)
    sia "그건 맞아."
    # SOURCE S01 L1004
    narrator "시아 씨는 웃었다."
    # SOURCE S01 L1006
    narrator "하지만 곧 조금 진지한 표정이 됐다."
    # SOURCE S01 L1009 (시아)
    sia "근데 내가 좋아하는 거랑, 다른 사람이 좋아해 주는 건 또 다른 문제잖아."
    # SOURCE S01 L1012 (주인공)
    mc "그렇죠."
    # SOURCE S01 L1015 (시아)
    sia "내가 보기에는 웃긴데 남들은 하나도 안 웃을 수도 있고."
    # SOURCE S01 L1017 (시아)
    sia "내가 진짜 열심히 그린 장면인데 그냥 넘어갈 수도 있고."
    # SOURCE S01 L1021
    narrator "시아 씨는 휴대전화를 내려놓았다."
    # SOURCE S01 L1024 (시아)
    sia "그래서 가끔 무섭긴 해."
    # SOURCE S01 L1027 (주인공)
    mc "어떤 게요?"
    # SOURCE S01 L1030 (시아)
    sia "내가 생각하는 재미있는 이야기가 사실은 나만 재미있는 거면 어떡하지 싶어서."
    # SOURCE S01 L1034
    narrator "시아 씨가 이런 걱정을 한다는 게 조금 의외였다."
    # SOURCE S01 L1036
    narrator "늘 자신감 넘치는 사람이었으니까."
    # SOURCE S01 L1039 (주인공)
    mc "그럴 때도 있겠죠."
    # SOURCE S01 L1042 (시아)
    sia "……어?"
    # SOURCE S01 L1045 (주인공)
    mc "모든 사람이 똑같은 장면에서 웃지는 않잖아요."
    # SOURCE S01 L1047 (주인공)
    mc "그렇다고 시아 씨가 재미없다는 뜻은 아니죠."
    # SOURCE S01 L1051
    narrator "시아 씨는 잠시 나를 바라봤다."
    # SOURCE S01 L1054 (시아)
    sia "……."
    # SOURCE S01 L1057 (시아)
    sia "너 가끔 되게 이상하다."
    # SOURCE S01 L1060 (주인공)
    mc "왜요?"
    # SOURCE S01 L1063 (시아)
    sia "보통 이런 말 하면 그냥 '아니야, 너 그림 재미있어'라고 하잖아."
    # SOURCE S01 L1066 (주인공)
    mc "그런 말도 할 수 있지만요."
    # SOURCE S01 L1069 (주인공)
    mc "저는 제가 재미있게 읽었던 부분을 직접 말씀드리고 싶어요."
    # SOURCE S01 L1072 (시아)
    sia "……."
    # SOURCE S01 L1076
    narrator "시아 씨는 천천히 웃었다."
    # SOURCE S01 L1079 (시아)
    sia "그게 더 좋네."
    # SOURCE S01 L1082 (주인공)
    mc "정말요?"
    # SOURCE S01 L1085 (시아)
    sia "응."
    # SOURCE S01 L1088 (시아)
    sia "그냥 무조건 잘한다고 해주는 것보다."
    # SOURCE S01 L1090 (시아)
    sia "어디가 좋았는지 말해주는 게 더 믿기거든."
    # SOURCE S01 L1094
    narrator "시아 씨는 다시 태블릿 화면을 켰다."
    # SOURCE S01 L1097 (시아)
    sia "나 웃기는 거 좋아해."
    # SOURCE S01 L1099 (시아)
    sia "사람들이 내 그림 보고 웃으면 진짜 기분 좋거든."
    # SOURCE S01 L1102 (시아)
    sia "근데 그것만 그리고 싶은 건 아니야."
    # SOURCE S01 L1105 (주인공)
    mc "그럼 어떤 이야기도 그리고 싶으세요?"
    # SOURCE S01 L1108 (시아)
    sia "음……."
    # SOURCE S01 L1112
    narrator "시아 씨는 잠시 고민했다."
    # SOURCE S01 L1115 (시아)
    sia "읽고 나서 조금 오래 생각나는 이야기?"
    # SOURCE S01 L1118 (주인공)
    mc "좋네요."
    # SOURCE S01 L1121 (시아)
    sia "그치?"
    # SOURCE S01 L1124 (시아)
    sia "막 엄청 거창할 필요는 없고."
    # SOURCE S01 L1126 (시아)
    sia "평범한 장면 하나라도 기억에 남으면 좋겠어."
    # SOURCE S01 L1130
    narrator "시아 씨는 자기 손을 내려다봤다."
    # SOURCE S01 L1133 (시아)
    sia "근데 아직 그런 걸 잘 그릴 수 있을지는 모르겠네."
    # SOURCE S01 L1136 (주인공)
    mc "계속 그리다 보면 조금씩 알게 되지 않을까요?"
    # SOURCE S01 L1139 (시아)
    sia "……."
    # SOURCE S01 L1142 (시아)
    sia "맞네."
    # SOURCE S01 L1145 (시아)
    sia "그럼 계속 그려야겠다."
    # SOURCE S01 L1149
    narrator "이번에는 장난스럽지 않았다."
    # SOURCE S01 L1151
    narrator "자신이 하고 싶은 일을 직접 결정한 사람의 표정이었다."
    # SOURCE S01 L1153 # CONTI [CG 후보] 시아가 오후 햇살 아래에서 휴대전화를 내려놓고 평소보다 차분하게 웃는 모습.
    # SOURCE S01 L1156 (시아)
    sia "야, 근데."
    # SOURCE S01 L1159 (주인공)
    mc "네?"
    # SOURCE S01 L1162 (시아)
    sia "오늘 이런 얘기 다른 사람한테 하면 안 된다?"
    # SOURCE S01 L1165 (주인공)
    mc "왜요?"
    # SOURCE S01 L1168 (시아)
    sia "나 천재 이미지 유지해야 하거든."
    # SOURCE S01 L1171 (주인공)
    mc "걱정하시는 모습도 나쁘지 않은데요?"
    # SOURCE S01 L1174 (시아)
    sia "……."
    # SOURCE S01 L1177 (시아)
    sia "아, 진짜!"
    # SOURCE S01 L1179 (시아)
    sia "너는 왜 꼭 그런 말을 아무렇지도 않게 하냐?"
    # SOURCE S01 L1183
    narrator "시아 씨의 얼굴이 살짝 붉어졌다."
    # SOURCE S01 L1185
    narrator "나는 웃었다."
    # SOURCE S01 L1187
    narrator "……이 사람은 진지할 때도 재미있네."
    # SOURCE S01 L1189 # CONTI [SCENE 05 END]
    jump sia_s01_sc06

label sia_s01_sc06:
    $ phone_timeline_enter("S01", "sia_s01_sc06")
    # SOURCE S01 L1193 SCENE 06. 지우지 않은 마지막 컷
    # SOURCE S01 L1195 # CONTI [TIME] 오후 5:05 · 애니메이션학과 작업실 · 첫 중요한 선택지
    $ phone_timeline_cue("S01", "S01_L1195")
    # SOURCE S01 L1197 # CONTI [HEADING] S01 SC06 · 지우지 않은 마지막 컷
    # SOURCE S01 L1199 [BG] 애니메이션학과 작업실 · 저녁 전
    $ sia_draft_scene("애니메이션학과 작업실 · 저녁 전")
    # SOURCE S01 L1201 [BGM] Creative Evening
    $ story_draft_bgm("Creative Evening")
    # SOURCE S01 L1205
    narrator "우리는 다시 작업실로 돌아왔다."
    # SOURCE S01 L1207
    narrator "시아 씨는 태블릿을 켜고 마지막 컷을 열었다."
    # SOURCE S01 L1209
    narrator "빈 말풍선이 여전히 남아 있었다."
    # SOURCE S01 L1212 (시아)
    sia "자."
    # SOURCE S01 L1214 (시아)
    sia "이제 진짜 마지막 문제다."
    # SOURCE S01 L1217 (주인공)
    mc "화해 장면이요?"
    # SOURCE S01 L1220 (시아)
    sia "응."
    # SOURCE S01 L1223 (시아)
    sia "아까 이야기 듣고 몇 개 생각해봤거든."
    # SOURCE S01 L1227
    narrator "시아 씨는 스케치 세 장을 보여줬다."
    # SOURCE S01 L1229
    narrator "첫 번째는 두 인물이 서로 사과하고 웃는 장면이었다."
    # SOURCE S01 L1231
    narrator "두 번째는 화해하려다가 다시 말다툼을 시작하는 장면이었다."
    # SOURCE S01 L1233
    narrator "세 번째는 두 사람이 아직 어색하지만 나란히 걸어가는 장면이었다."
    # SOURCE S01 L1236 (시아)
    sia "어때?"
    # SOURCE S01 L1239 (주인공)
    mc "셋 다 느낌이 다르네요."
    # SOURCE S01 L1242 (시아)
    sia "그치."
    # SOURCE S01 L1245 (시아)
    sia "나는 마지막 것도 마음에 드는데."
    # SOURCE S01 L1248 (시아)
    sia "독자들이 답답하다고 할까 싶기도 해."
    # SOURCE S01 L1252
    narrator "나는 세 장을 다시 살펴봤다."
    # SOURCE S01 L1254
    narrator "세 번째 장면에서는 두 사람이 완전히 화해한 것 같지는 않았다."
    # SOURCE S01 L1256
    narrator "하지만 서로를 외면하지 않고 같은 방향으로 걸어가고 있었다."
    # SOURCE S01 L1259 (주인공)
    mc "시아 씨는 어떤 장면이 제일 마음에 드세요?"
    # SOURCE S01 L1262 (시아)
    sia "음……."
    # SOURCE S01 L1265 (시아)
    sia "세 번째."
    # SOURCE S01 L1268 (주인공)
    mc "왜요?"
    # SOURCE S01 L1271 (시아)
    sia "둘이 이제 한 번 싸웠다고 갑자기 완벽하게 이해하는 사이가 되는 건 이상하잖아."
    # SOURCE S01 L1274 (주인공)
    mc "그렇죠."
    # SOURCE S01 L1277 (시아)
    sia "그래서 아직 조금 어색해도."
    # SOURCE S01 L1279 (시아)
    sia "같이 가보자는 느낌으로 끝내고 싶었어."
    # SOURCE S01 L1283
    narrator "시아 씨는 세 번째 그림을 바라봤다."
    # SOURCE S01 L1286 (시아)
    sia "근데 너는 어떻게 생각하냐?"
    # SOURCE S01 L1288 [CHOICE 01 · 마지막 컷에 대한 감상]
    menu:
        # SOURCE S01 L1290 선택지
        "세 번째 컷이 가장 기억에 남아요.":
            # SOURCE S01 L1293 (주인공)
            mc "저는 세 번째 컷이 가장 기억에 남아요."
            # SOURCE S01 L1295 (주인공)
            mc "모든 문제가 해결된 건 아니지만, 두 사람이 계속 함께해보려는 마음이 보여요."
            # SOURCE S01 L1298 (시아)
            sia "……."
            # SOURCE S01 L1300 (시아)
            sia "오."
            # SOURCE S01 L1303 (시아)
            sia "그거 내가 의도한 느낌이랑 비슷한데?"
            # SOURCE S01 L1306 (주인공)
            mc "그럼 잘 전달된 거네요."
            # SOURCE S01 L1309 (시아)
            sia "ㅋㅋㅋ 그런 것 같네."
            # SOURCE S01 L1311 [FLAG] `sia_s01_feedback_choice = "open"`
            # SOURCE S01 L1313 [FLAG] `sia_creative_confidence += 1`
            $ story_apply("sia_s01_choice01_a", values={'sia_s01_feedback_choice': 'open'}, counters={'sia_creative_confidence': 1})
        # SOURCE S01 L1317 선택지
        "두 번째 컷은 시아 씨다운 장난이 살아 있어요.":
            # SOURCE S01 L1320 (주인공)
            mc "두 번째 컷도 좋아요."
            # SOURCE S01 L1322 (주인공)
            mc "진지하게 화해하려다가 다시 티격태격하는 게 시아 씨 작품답거든요."
            # SOURCE S01 L1325 (시아)
            sia "……!"
            # SOURCE S01 L1327 (시아)
            sia "야, 그치?"
            # SOURCE S01 L1330 (주인공)
            mc "다만 갈등을 그냥 개그로 넘기지 않았다는 느낌은 조금 더 필요할 것 같아요."
            # SOURCE S01 L1333 (시아)
            sia "오케이."
            # SOURCE S01 L1336 (시아)
            sia "그럼 두 번째의 개그를 세 번째에 조금 섞어볼까?"
            # SOURCE S01 L1338 [FLAG] `sia_s01_feedback_choice = "comedy"`
            # SOURCE S01 L1340 [FLAG] `sia_creative_confidence += 1`
            $ story_apply("sia_s01_choice01_b", values={'sia_s01_feedback_choice': 'comedy'}, counters={'sia_creative_confidence': 1})
        # SOURCE S01 L1344 선택지
        "제가 정답을 고르기보다는 시아 씨 생각을 듣고 싶어요.":
            # SOURCE S01 L1347 (주인공)
            mc "세 장 다 장점이 있어서 하나만 고르기 어렵네요."
            # SOURCE S01 L1349 (주인공)
            mc "시아 씨가 가장 표현하고 싶은 감정이 뭔지 조금 더 듣고 싶어요."
            # SOURCE S01 L1352 (시아)
            sia "……."
            # SOURCE S01 L1354 (시아)
            sia "오."
            # SOURCE S01 L1357 (시아)
            sia "그거 어려운 질문인데?"
            # SOURCE S01 L1360 (주인공)
            mc "천재 작가님이시잖아요."
            # SOURCE S01 L1363 (시아)
            sia "……."
            # SOURCE S01 L1365 (시아)
            sia "아, 그걸 여기서 써먹네ㅋㅋ"
            # SOURCE S01 L1368 (시아)
            sia "좋아. 그럼 설명해줄게."
            # SOURCE S01 L1370 [FLAG] `sia_s01_feedback_choice = "discussion"`
            # SOURCE S01 L1372 [FLAG] `sia_mutual_trust += 1`
            $ story_apply("sia_s01_choice01_c", values={'sia_s01_feedback_choice': 'discussion'})
    # SOURCE S01 L1380
    narrator "우리는 마지막 컷에 대해 한참 이야기했다."
    # SOURCE S01 L1382
    narrator "시아 씨는 세 번째 구도를 기본으로 유지하기로 했다."
    # SOURCE S01 L1384
    narrator "대신 두 캐릭터가 나란히 걷는 마지막 장면에 작은 농담 하나를 추가했다."
    # SOURCE S01 L1386
    narrator "활발한 캐릭터가 먼저 입을 열었다."
    # SOURCE S01 L1388
    narrator "「야, 다음엔 내 말 좀 들어라?」"
    # SOURCE S01 L1390
    narrator "차분한 캐릭터가 대답했다."
    # SOURCE S01 L1392
    narrator "「너도 내 말 좀 듣고.」"
    # SOURCE S01 L1394
    narrator "그리고 마지막 말풍선에는 짧은 문장이 들어갔다."
    # SOURCE S01 L1396
    narrator "「……그럼 다음에는 같이 생각하자.」"
    # SOURCE S01 L1399 (주인공)
    mc "……좋네요."
    # SOURCE S01 L1402 (시아)
    sia "그치?"
    # SOURCE S01 L1405 (주인공)
    mc "진지한데 마지막은 조금 웃기기도 해요."
    # SOURCE S01 L1408 (시아)
    sia "바로 그거야."
    # SOURCE S01 L1412
    narrator "시아 씨는 만족스러운 표정으로 화면을 바라봤다."
    # SOURCE S01 L1415 (시아)
    sia "야, 근데."
    # SOURCE S01 L1418 (주인공)
    mc "네?"
    # SOURCE S01 L1421 (시아)
    sia "아까 그거 있잖아."
    # SOURCE S01 L1424 (주인공)
    mc "어떤 거요?"
    # SOURCE S01 L1427 (시아)
    sia "네가 말한 의견들."
    # SOURCE S01 L1430 (시아)
    sia "진짜 도움이 됐어."
    # SOURCE S01 L1433 (주인공)
    mc "다행이네요."
    # SOURCE S01 L1436 (시아)
    sia "근데 마지막은 내가 정했다?"
    # SOURCE S01 L1439 (주인공)
    mc "네. 시아 씨 작품이니까요."
    # SOURCE S01 L1442 (시아)
    sia "……."
    # SOURCE S01 L1446
    narrator "시아 씨는 잠깐 웃었다."
    # SOURCE S01 L1449 (시아)
    sia "좋네."
    # SOURCE S01 L1452 (시아)
    sia "내가 그리고 싶은 걸 그리면서도 다른 사람 의견을 들을 수 있다는 거."
    # SOURCE S01 L1455 (주인공)
    mc "그게 좋은 피드백 아닐까요?"
    # SOURCE S01 L1458 (시아)
    sia "그렇지."
    # SOURCE S01 L1461 (시아)
    sia "역시 감상 담당 채용하길 잘했어."
    # SOURCE S01 L1464 (주인공)
    mc "아직 근로계약서도 안 썼는데요."
    # SOURCE S01 L1467 (시아)
    sia "ㅋㅋㅋ"
    # SOURCE S01 L1470 (시아)
    sia "그럼 종신계약으로 하자."
    # SOURCE S01 L1473 (주인공)
    mc "그건 좀 곤란한데요."
    # SOURCE S01 L1476 (시아)
    sia "야, 바로 거절하냐?"
    # SOURCE S01 L1480
    narrator "시아 씨는 웃으며 태블릿을 내려놓았다."
    # SOURCE S01 L1483 (시아)
    sia "아무튼."
    # SOURCE S01 L1485 (시아)
    sia "다음 편도 보여줄게."
    # SOURCE S01 L1488 (주인공)
    mc "기대할게요."
    # SOURCE S01 L1491 (시아)
    sia "……응."
    # SOURCE S01 L1493 (시아)
    sia "나도 기대된다."
    # SOURCE S01 L1497
    narrator "시아 씨는 자신이 완성한 마지막 컷을 다시 한번 확인했다."
    # SOURCE S01 L1499
    narrator "그리고 저장 버튼을 눌렀다."
    # SOURCE S01 L1501 # CONTI [SFX] 파일 저장 효과음
    # SOURCE S01 L1503 # CONTI [UI] 원고 저장 완료
    # SOURCE S01 L1505 [FLAG] `sia_s01_episode_draft_complete = True`
    $ story_flag("sia_s01_episode_draft_complete", True)
    # SOURCE S01 L1507 # CONTI [SCENE 06 END]
    jump sia_s01_sc07

label sia_s01_sc07:
    $ phone_timeline_enter("S01", "sia_s01_sc07")
    # SOURCE S01 L1511 SCENE 07. 너한테는 먼저 보여주고 싶어
    # SOURCE S01 L1513 # CONTI [TIME] 오후 6:00 · 작업실 앞 복도와 건물 입구 · 관계의 변화
    $ phone_timeline_cue("S01", "S01_L1513")
    # SOURCE S01 L1515 # CONTI [HEADING] S01 SC07 · 너한테는 먼저 보여주고 싶어
    # SOURCE S01 L1517 [BG] 애니메이션학과 작업실 · 저녁
    $ sia_draft_scene("애니메이션학과 작업실 · 저녁")
    # SOURCE S01 L1519 [BGM] Gentle Evening
    $ story_draft_bgm("Gentle Evening")
    # SOURCE S01 L1523
    narrator "작업이 끝난 뒤 시아 씨는 태블릿을 정리했다."
    # SOURCE S01 L1525
    narrator "나는 가방을 챙겼다."
    # SOURCE S01 L1528 (시아)
    sia "야, 오늘 진짜 오래 있었네."
    # SOURCE S01 L1531 (주인공)
    mc "그러게요. 거의 반나절이 지났어요."
    # SOURCE S01 L1534 (시아)
    sia "어쩐지 배가 또 고프더라."
    # SOURCE S01 L1537 (주인공)
    mc "벌써요?"
    # SOURCE S01 L1540 (시아)
    sia "천재 작가는 에너지 소모가 크거든."
    # SOURCE S01 L1543 (주인공)
    mc "그럼 다음에는 간식 챙겨올게요."
    # SOURCE S01 L1546 (시아)
    sia "오."
    # SOURCE S01 L1548 (시아)
    sia "너 진짜 유능한 직원이네?"
    # SOURCE S01 L1552
    narrator "시아 씨는 웃으며 가방을 멨다."
    # SOURCE S01 L1554
    narrator "우리는 함께 작업실을 나왔다."
    # SOURCE S01 L1556 [BG] 애니메이션학과 복도 · 저녁
    $ sia_draft_scene("애니메이션학과 복도 · 저녁")
    # SOURCE S01 L1560
    narrator "복도에는 아직 작업하는 학생들이 있었다."
    # SOURCE S01 L1562
    narrator "시아 씨는 몇몇 학생과 가볍게 인사를 나눴다."
    # SOURCE S01 L1564
    narrator "그중 한 학생이 시아 씨를 불렀다."
    # SOURCE S01 L1567 (동기)
    sia_classmate "시아야, 네 개인 웹툰 작업 어디까지 했어?"
    # SOURCE S01 L1570 (시아)
    sia "오, 거의 다 했지."
    # SOURCE S01 L1573 (동기)
    sia_classmate "진짜? 나중에 보여줘."
    # SOURCE S01 L1576 (시아)
    sia "응. 정리 좀 더 하면."
    # SOURCE S01 L1579 (동기)
    sia_classmate "오케이. 기대한다!"
    # SOURCE S01 L1583
    narrator "시아 씨는 손을 흔들었다."
    # SOURCE S01 L1585
    narrator "잠시 뒤 우리는 계단을 내려갔다."
    # SOURCE S01 L1588 (주인공)
    mc "다른 분들도 시아 씨 웹툰을 기다리시네요."
    # SOURCE S01 L1591 (시아)
    sia "뭐, 그렇지."
    # SOURCE S01 L1594 (시아)
    sia "근데 아직 공개할 정도로 다듬은 건 아니야."
    # SOURCE S01 L1597 (주인공)
    mc "그럼 오늘 저한테 보여주신 건 정말 초안이었네요."
    # SOURCE S01 L1600 (시아)
    sia "응."
    # SOURCE S01 L1603 (시아)
    sia "너한테는 먼저 보여주고 싶었거든."
    # SOURCE S01 L1607
    narrator "……."
    # SOURCE S01 L1609
    narrator "나는 잠깐 걸음을 늦췄다."
    # SOURCE S01 L1612 (주인공)
    mc "왜요?"
    # SOURCE S01 L1615 (시아)
    sia "어?"
    # SOURCE S01 L1618 (주인공)
    mc "다른 분들보다 먼저 보여주고 싶으셨던 이유요."
    # SOURCE S01 L1621 (시아)
    sia "……."
    # SOURCE S01 L1625
    narrator "시아 씨는 잠시 계단 아래를 바라봤다."
    # SOURCE S01 L1627
    narrator "평소라면 바로 장난스러운 대답이 나왔을 텐데."
    # SOURCE S01 L1629
    narrator "이번에는 조금 생각하는 것 같았다."
    # SOURCE S01 L1632 (시아)
    sia "그냥……."
    # SOURCE S01 L1634 (시아)
    sia "네가 제대로 읽어주니까."
    # SOURCE S01 L1637 (주인공)
    mc "네."
    # SOURCE S01 L1640 (시아)
    sia "재미없으면 재미없다고도 말하고."
    # SOURCE S01 L1642 (시아)
    sia "좋은 부분은 왜 좋은지도 말하잖아."
    # SOURCE S01 L1645 (시아)
    sia "그리고……."
    # SOURCE S01 L1649
    narrator "시아 씨는 잠시 말을 멈췄다."
    # SOURCE S01 L1652 (주인공)
    mc "그리고요?"
    # SOURCE S01 L1655 (시아)
    sia "……."
    # SOURCE S01 L1658 (시아)
    sia "너랑 이야기하는 게 재미있으니까."
    # SOURCE S01 L1662
    narrator "시아 씨는 조금 민망한 듯 웃었다."
    # SOURCE S01 L1665 (시아)
    sia "아, 진짜."
    # SOURCE S01 L1667 (시아)
    sia "이런 거 꼭 말로 설명해야 하냐?"
    # SOURCE S01 L1670 (주인공)
    mc "제가 궁금해서요."
    # SOURCE S01 L1673 (시아)
    sia "……."
    # SOURCE S01 L1675 (시아)
    sia "알아."
    # SOURCE S01 L1679
    narrator "시아 씨는 내 쪽을 바라봤다."
    # SOURCE S01 L1682 (시아)
    sia "그냥 네 반응이 궁금해."
    # SOURCE S01 L1685 (시아)
    sia "내가 뭔가 그렸을 때 네가 어떻게 생각할지."
    # SOURCE S01 L1687 (시아)
    sia "어디서 웃을지."
    # SOURCE S01 L1689 (시아)
    sia "어떤 장면을 좋아할지."
    # SOURCE S01 L1693
    narrator "시아 씨는 작게 웃었다."
    # SOURCE S01 L1696 (시아)
    sia "그래서 먼저 보여주고 싶었어."
    # SOURCE S01 L1699 (주인공)
    mc "……그렇군요."
    # SOURCE S01 L1702 (시아)
    sia "왜."
    # SOURCE S01 L1704 (시아)
    sia "실망했냐?"
    # SOURCE S01 L1707 (주인공)
    mc "아니요."
    # SOURCE S01 L1709 (주인공)
    mc "오히려 조금 기쁜데요."
    # SOURCE S01 L1712 (시아)
    sia "……."
    # SOURCE S01 L1714 # CONTI [표정] 시아 · 당황 → 옅은 홍조
    # SOURCE S01 L1717 (시아)
    sia "……야."
    # SOURCE S01 L1720 (주인공)
    mc "네?"
    # SOURCE S01 L1723 (시아)
    sia "그런 말은 좀……."
    # SOURCE S01 L1726 (시아)
    sia "……예고하고 해라."
    # SOURCE S01 L1730
    narrator "시아 씨는 시선을 돌렸다."
    # SOURCE S01 L1732
    narrator "나는 괜히 웃음이 나왔다."
    # SOURCE S01 L1735 (주인공)
    mc "시아 씨도 갑자기 말씀하셨잖아요."
    # SOURCE S01 L1738 (시아)
    sia "……."
    # SOURCE S01 L1740 (시아)
    sia "그건 그렇네."
    # SOURCE S01 L1744
    narrator "시아 씨는 결국 웃음을 터뜨렸다."
    # SOURCE S01 L1746 [BG] 애니메이션학과 건물 앞 · 저녁
    $ sia_draft_scene("애니메이션학과 건물 앞 · 저녁")
    # SOURCE S01 L1750
    narrator "건물 밖으로 나오니 하늘이 조금 어두워져 있었다."
    # SOURCE S01 L1753 (시아)
    sia "야, 오늘 고마웠다."
    # SOURCE S01 L1756 (주인공)
    mc "저도 재미있었어요."
    # SOURCE S01 L1759 (시아)
    sia "다음에는 작업실 말고 밖에서도 놀자."
    # SOURCE S01 L1762 (주인공)
    mc "좋아요. 어디 가고 싶으세요?"
    # SOURCE S01 L1765 (시아)
    sia "음……."
    # SOURCE S01 L1768 (시아)
    sia "일단 게임센터?"
    # SOURCE S01 L1771 (주인공)
    mc "갑자기요?"
    # SOURCE S01 L1774 (시아)
    sia "왜. 너 게임 못하냐?"
    # SOURCE S01 L1777 (주인공)
    mc "아니요. 못한다고 말씀드린 건 아닌데요."
    # SOURCE S01 L1780 (시아)
    sia "오호."
    # SOURCE S01 L1783 (시아)
    sia "자신 있다는 거지?"
    # SOURCE S01 L1786 (주인공)
    mc "그 정도도 아닌데요."
    # SOURCE S01 L1789 (시아)
    sia "좋아. 승부다."
    # SOURCE S01 L1793
    narrator "……언제 승부가 결정된 거지?"
    # SOURCE S01 L1796 (시아)
    sia "다음에 시간 맞춰서 가자."
    # SOURCE S01 L1799 (주인공)
    mc "네. 좋아요."
    # SOURCE S01 L1802 (시아)
    sia "오케이."
    # SOURCE S01 L1805 (시아)
    sia "도망가기 없기다?"
    # SOURCE S01 L1808 (주인공)
    mc "도망 안 가요."
    # SOURCE S01 L1811 (시아)
    sia "ㅋㅋㅋ 약속했다."
    # SOURCE S01 L1815
    narrator "시아 씨는 손을 흔들었다."
    # SOURCE S01 L1817
    narrator "나는 건물 앞에 잠시 서 있었다."
    # SOURCE S01 L1819
    narrator "오늘은 웹툰을 보러 왔다."
    # SOURCE S01 L1821
    narrator "그런데 돌아가는 지금은, 다음에 시아 씨와 만날 날이 더 기다려지고 있었다."
    # SOURCE S01 L1823 [FLAG] `sia_s01_next_date_promise = True`
    $ story_flag("sia_s01_next_date_promise", True)
    # SOURCE S01 L1825 # CONTI [SCENE 07 END]
    jump sia_s01_sc08

label sia_s01_sc08:
    $ phone_timeline_enter("S01", "sia_s01_sc08")
    # SOURCE S01 L1829 SCENE 08. 다음 편도 예약할게
    # SOURCE S01 L1831 # CONTI [TIME] 같은 날 밤 · 주인공 방 → 시아의 작업 공간 · S02 연결
    # SOURCE S01 L1833 # CONTI [HEADING] S01 SC08 · 다음 편도 예약할게
    # SOURCE S01 L1835 [BG] 주인공 방 · 밤
    $ sia_draft_scene("주인공 방 · 밤")
    # SOURCE S01 L1837 [BGM] Quiet Creative Night
    $ story_draft_bgm("Quiet Creative Night")
    # SOURCE S01 L1839 # CONTI [FADE IN]
    # SOURCE S01 L1843
    narrator "방으로 돌아와 가방을 내려놓았다."
    # SOURCE S01 L1845
    narrator "오늘은 생각보다 많은 이야기를 나눴다."
    # SOURCE S01 L1847
    narrator "웹툰의 마지막 컷."
    # SOURCE S01 L1849
    narrator "캐릭터들이 서로 다른 생각을 하는 이유."
    # SOURCE S01 L1851
    narrator "그리고 시아 씨가 앞으로 그리고 싶어 하는 이야기까지."
    # SOURCE S01 L1853
    narrator "처음에는 시아 씨를 그저 장난기 많은 사람이라고 생각했다."
    # SOURCE S01 L1855
    narrator "물론 지금도 장난을 많이 친다."
    # SOURCE S01 L1857
    narrator "엄청나게 많이."
    # SOURCE S01 L1859
    narrator "그런데 그 사람에게는 진지한 모습도 있었다."
    # SOURCE S01 L1861
    narrator "자신의 작품이 재미없으면 어떡하나 걱정하면서도."
    # SOURCE S01 L1863
    narrator "결국 자기가 그리고 싶은 이야기를 선택하는 사람."
    # SOURCE S01 L1865
    narrator "……조금 멋있었다."
    # SOURCE S01 L1867 # CONTI [SFX] 휴대전화 진동
    # SOURCE S01 L1869 # CONTI [UI] 시아 개인 메시지
    $ story_chat(True, title="시아")
    # SOURCE S01 L1872 (시아)
    sia "야"
    # SOURCE S01 L1875 (주인공 · 메시지)
    mc "네, 시아 씨."
    # SOURCE S01 L1878 (시아)
    sia "오늘 마지막 컷 수정한 거"
    # SOURCE S01 L1880 (시아)
    sia "다시 보니까 괜찮다ㅋㅋ"
    # SOURCE S01 L1883 (주인공 · 메시지)
    mc "다행이네요."
    # SOURCE S01 L1886 (시아)
    sia "근데 아직 완성은 아님"
    # SOURCE S01 L1889 (시아)
    sia "채색도 해야 하고"
    # SOURCE S01 L1891 (시아)
    sia "몇 컷 더 수정해야 돼"
    # SOURCE S01 L1894 (주인공 · 메시지)
    mc "그럼 아직 할 일이 많으시겠네요."
    # SOURCE S01 L1897 (시아)
    sia "응"
    # SOURCE S01 L1899 (시아)
    sia "근데 재미있어"
    # SOURCE S01 L1903
    narrator "그 말이 마음에 들었다."
    # SOURCE S01 L1905
    narrator "시아 씨는 바쁜 와중에도 즐겁게 작업하고 있었다."
    # SOURCE S01 L1908 (주인공 · 메시지)
    mc "완성되면 저도 다시 읽어보고 싶어요."
    # SOURCE S01 L1911 (시아)
    sia "당연하지"
    # SOURCE S01 L1913 (시아)
    sia "첫 독자잖아"
    # SOURCE S01 L1916 (주인공 · 메시지)
    mc "그럼 다음 편도 예약할게요."
    # SOURCE S01 L1919 (시아)
    sia "ㅋㅋㅋ"
    # SOURCE S01 L1921 (시아)
    sia "예약 접수 완료"
    # SOURCE S01 L1925
    narrator "잠시 뒤 메시지가 하나 더 왔다."
    # SOURCE S01 L1928 (시아)
    sia "야 근데"
    # SOURCE S01 L1931 (주인공 · 메시지)
    mc "네?"
    # SOURCE S01 L1934 (시아)
    sia "오늘 너랑 얘기한 거"
    # SOURCE S01 L1936 (시아)
    sia "좀 도움 많이 됐어"
    # SOURCE S01 L1939 (주인공 · 메시지)
    mc "저도 시아 씨랑 이야기해서 재미있었어요."
    # SOURCE S01 L1942 (시아)
    sia "……."
    # SOURCE S01 L1944 (시아)
    sia "아 진짜"
    # SOURCE S01 L1947 (시아)
    sia "너 또 그러네"
    # SOURCE S01 L1950 (주인공 · 메시지)
    mc "제가 뭘요?"
    # SOURCE S01 L1953 (시아)
    sia "몰라도 돼ㅋㅋ"
    # SOURCE S01 L1957
    narrator "……뭘 모른다는 거지?"
    # SOURCE S01 L1959
    narrator "나는 잠시 화면을 바라봤다."
    # SOURCE S01 L1961 # CONTI [SFX] 추가 메시지
    # SOURCE S01 L1964 (시아)
    sia "아 그리고"
    # SOURCE S01 L1966 (시아)
    sia "게임센터 약속 기억해라"
    # SOURCE S01 L1969 (주인공 · 메시지)
    mc "네. 기억하고 있어요."
    # SOURCE S01 L1972 (시아)
    sia "좋아"
    # SOURCE S01 L1974 (시아)
    sia "이번에는 내가 이긴다"
    # SOURCE S01 L1977 (주인공 · 메시지)
    mc "아직 무슨 게임인지도 안 정했는데요."
    # SOURCE S01 L1980 (시아)
    sia "그건 가서 정하면 됨"
    # SOURCE S01 L1983 (주인공 · 메시지)
    mc "너무 자신만만하신 거 아닌가요?"
    # SOURCE S01 L1986 (시아)
    sia "천재니까"
    # SOURCE S01 L1990
    narrator "……정말 한결같네."
    # SOURCE S01 L1992
    narrator "나는 웃으며 휴대전화를 내려놓았다."
    # SOURCE S01 L1994 # CONTI [TRANSITION] 같은 밤 · 애니메이션학과 작업실
    $ story_chat(False)
    # SOURCE S01 L1996 # CONTI [POV] 시아
    $ phone_perspective_set("sia")
    # SOURCE S01 L1998 [BG] 작업실 · 야간 조명
    $ sia_draft_scene("작업실 · 야간 조명")
    # SOURCE S01 L2000 [BGM] Soft Animation Theme
    $ story_draft_bgm("Soft Animation Theme")
    # SOURCE S01 L2004
    narrator "시아는 완성 직전의 웹툰을 다시 열었다."
    # SOURCE S01 L2006
    narrator "마지막 컷에는 두 캐릭터가 나란히 걸어가고 있었다."
    # SOURCE S01 L2008
    narrator "그 아래에는 조금 전에 추가한 대사가 들어가 있었다."
    # SOURCE S01 L2010
    narrator "「그럼 다음에는 같이 생각하자.」"
    # SOURCE S01 L2013 (시아 · 혼잣말)
    sia "……흠."
    # SOURCE S01 L2017
    narrator "시아는 화면을 확대했다."
    # SOURCE S01 L2019
    narrator "표정과 말풍선 위치를 다시 확인했다."
    # SOURCE S01 L2021
    narrator "처음 생각했던 것과는 조금 달라졌다."
    # SOURCE S01 L2023
    narrator "하지만 오히려 지금이 더 마음에 들었다."
    # SOURCE S01 L2026 (시아 · 혼잣말)
    sia "괜찮은데?"
    # SOURCE S01 L2030
    narrator "시아는 작게 웃었다."
    # SOURCE S01 L2032
    narrator "그러다가 휴대전화 화면을 켰다."
    # SOURCE S01 L2034
    narrator "조금 전 주인공과 나눴던 대화가 남아 있었다."
    # SOURCE S01 L2036
    narrator "저도 시아 씨랑 이야기해서 재미있었어요."
    # SOURCE S01 L2039 (시아 · 혼잣말)
    sia "……."
    # SOURCE S01 L2041 (시아 · 혼잣말)
    sia "아, 진짜."
    # SOURCE S01 L2045
    narrator "시아는 휴대전화를 뒤집어 놓았다."
    # SOURCE S01 L2047
    narrator "하지만 몇 초 지나지 않아 다시 집어 들었다."
    # SOURCE S01 L2050 (시아 · 혼잣말)
    sia "뭐야."
    # SOURCE S01 L2052 (시아 · 혼잣말)
    sia "왜 자꾸 생각나는데?"
    # SOURCE S01 L2056
    narrator "시아는 고개를 저었다."
    # SOURCE S01 L2059 (시아 · 혼잣말)
    sia "그냥 감상 담당이잖아."
    # SOURCE S01 L2063
    narrator "그렇게 말하고 다시 태블릿을 바라봤다."
    # SOURCE S01 L2065
    narrator "그런데 마지막 컷에 나오는 두 캐릭터가 조금 다르게 보였다."
    # SOURCE S01 L2067
    narrator "서로 다른 생각을 하면서도."
    # SOURCE S01 L2069
    narrator "계속 함께하고 싶어서 먼저 말을 꺼내는 두 사람."
    # SOURCE S01 L2071
    narrator "시아는 잠시 펜을 멈췄다."
    # SOURCE S01 L2074 (시아 · 혼잣말)
    sia "……설마."
    # SOURCE S01 L2078
    narrator "그리고 곧바로 웃었다."
    # SOURCE S01 L2081 (시아 · 혼잣말)
    sia "아냐, 아니야."
    # SOURCE S01 L2083 (시아 · 혼잣말)
    sia "일단 마감부터 끝내자."
    # SOURCE S01 L2087
    narrator "시아는 다시 펜을 들었다."
    # SOURCE S01 L2089
    narrator "그러나 입가에는 조금 전까지 없던 미소가 남아 있었다."
    # SOURCE S01 L2091 # CONTI [FADE TO BLACK]
    # SOURCE S01 L2093 # CONTI [TEXT]
    # SOURCE S01 L2095 # CONTI [TEXT] SIA ROUTE
    # SOURCE S01 L2097 # CONTI [TEXT] S01 COMPLETE
    # SOURCE S01 L2099 # CONTI [TEXT] 「내 웹툰의 첫 번째 독자」
    # SOURCE S01 L2101 # CONTI [TEXT] NEXT CHAPTER
    # SOURCE S01 L2103 # CONTI [TEXT] S02 「너랑 있으면 이상하게 재밌어」
    # SOURCE S01 L2105 [FLAG] `sia_s01_complete = True`
    $ story_flag("sia_s01_complete", True)
    # SOURCE S01 L2107 [FLAG] `sia_webtoon_first_reader = True`
    $ story_flag("sia_webtoon_first_reader", True)
    # SOURCE S01 L2109 # CONTI [NEXT] SIA ROUTE S02
    # SOURCE S01 L2111 # CONTI [CHAPTER S01 END]
    $ sia_complete_episode("S01")
    jump sia_s02
