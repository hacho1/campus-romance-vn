# Roman R03 · dialogue-only storyboard import
# SOURCE: design_docs/story_sources/roman_r03.txt
# SHA256: 7695db26f758c70f9af7831ba06e474766d0ca7d775f12e81b01c7238090dd72
# Rebuild: tools/import_roman_first.py --write
# CONTI markers intentionally do not load standing, SD, or LD artwork.

default roman_r03_conflict_resolved = False
default roman_reassurance_dependency = 0
default roman_creative_autonomy = 0
default roman_approval_dependency = 0
default roman_r03_complete = False
default roman_manuscript_submitted = False

label roman_r03:
    $ phone_timeline_enter("R03", "roman_r03")
    $ roman_begin_episode("R03", "말하지 않아도 알 거라고 생각했어요")
    jump roman_r03_sc01

label roman_r03_sc01:
    $ phone_timeline_enter("R03", "roman_r03_sc01")
    # SOURCE R03 L28 # R03 SC01 · 조금 늦은 답장
    # SOURCE R03 L30 [BG] 주인공 방 · 오후
    $ story_draft_scene("주인공 방 · 오후")
    # SOURCE R03 L32 [BGM] Ordinary Afternoon
    $ story_draft_bgm("Ordinary Afternoon")
    # CONTI SOURCE R03 L34 [FADE IN]
    # SOURCE R03 L38
    narrator "로만 씨와 마지막으로 만난 지 사흘이 지났다."
    # SOURCE R03 L40
    narrator "그동안 우리는 몇 번 메시지를 주고받았다."
    # SOURCE R03 L42
    narrator "수업 이야기, 점심 메뉴 이야기, 우연히 발견한 책 이야기."
    # SOURCE R03 L44
    narrator "그리고 낭독회 준비 이야기."
    # SOURCE R03 L46
    narrator "원고 제출 마감이 가까워진 탓인지, 요즘 로만 씨는 꽤 바쁜 모양이었다."
    # CONTI SOURCE R03 L48 [SFX] 휴대전화 진동
    # CONTI SOURCE R03 L50 [UI] 로만 개인 메시지
    $ story_chat(True, title="로만")
    # SOURCE R03 L53 (로만)
    roman "앗,,, 오늘도 좋은 오후 보내고 계세요……?"
    # SOURCE R03 L56 (주인공 · 메시지)
    mc "네. 로만 씨는 원고 잘 쓰고 계세요?"
    # SOURCE R03 L59 (로만)
    roman "네……!"
    # SOURCE R03 L61 (로만)
    roman "조금씩 고치고 있어요."
    # SOURCE R03 L63 (로만)
    roman "그런데 생각보다 시간이 오래 걸리네요……."
    # SOURCE R03 L66 (주인공 · 메시지)
    mc "그럴 것 같아요. 처음 참가하시는 행사니까 더 신경 쓰이시겠어요."
    # SOURCE R03 L69 (로만)
    roman "맞아요……."
    # SOURCE R03 L71 (로만)
    roman "그래도 이번에는 꼭 완성해 보려고요."
    # SOURCE R03 L74 (주인공 · 메시지)
    mc "좋아요. 너무 무리하지는 마세요."
    # SOURCE R03 L77 (로만)
    roman "후후…… 네."
    # SOURCE R03 L79 (로만)
    roman "아, 그리고……."
    # SOURCE R03 L81 (로만)
    roman "오늘 저녁에는 시간 괜찮으세요?"
    # SOURCE R03 L85
    narrator "오늘 저녁?"
    # SOURCE R03 L87
    narrator "일정을 확인했다."
    # SOURCE R03 L89
    narrator "당장 해야 할 과제는 없었다."
    # SOURCE R03 L91
    narrator "하지만 로만 씨는 원고를 마무리해야 할 텐데."
    # SOURCE R03 L94 (주인공 · 메시지)
    mc "저는 괜찮은데요. 로만 씨는 원고 때문에 바쁘시지 않으세요?"
    # SOURCE R03 L97 (로만)
    roman "아……."
    # SOURCE R03 L99 (로만)
    roman "그렇기는 해요."
    # SOURCE R03 L101 (로만)
    roman "그래도 잠깐 만나서 이야기하면 좋을 것 같아서요."
    # SOURCE R03 L105
    narrator "로만 씨는 원고를 쓰느라 바쁜데도 시간을 내려고 한다."
    # SOURCE R03 L107
    narrator "괜히 내가 방해하는 건 아닐까."
    # SOURCE R03 L110 (주인공 · 메시지)
    mc "원고 제출이 얼마 안 남았잖아요."
    # SOURCE R03 L112 (주인공 · 메시지)
    mc "오늘은 글 쓰시는 데 집중하셔도 괜찮아요. 다음에 만나도 되니까요."
    # CONTI SOURCE R03 L114 [SFX] 메시지 읽음
    # SOURCE R03 L118
    narrator "잠시 답장이 없었다."
    # SOURCE R03 L120
    narrator "그러다가 짧은 메시지가 도착했다."
    # SOURCE R03 L123 (로만)
    roman "……아."
    # SOURCE R03 L125 (로만)
    roman "네……! 그럼 다음에 뵐게요."
    # SOURCE R03 L128 (주인공 · 메시지)
    mc "네. 원고 준비 잘하세요."
    # SOURCE R03 L131 (로만)
    roman "……후후."
    # SOURCE R03 L133 (로만)
    roman "고마워요."
    # CONTI SOURCE R03 L135 [UI] 스마트폰 화면 종료
    $ story_chat(False)
    # SOURCE R03 L139
    narrator "잘한 선택이라고 생각했다."
    # SOURCE R03 L141
    narrator "원고 마감도 얼마 남지 않았고, 로만 씨에게는 중요한 행사니까."
    # SOURCE R03 L143
    narrator "며칠만 지나면 다시 편하게 만날 수 있을 것이다."
    # SOURCE R03 L145
    narrator "……그런데."
    # SOURCE R03 L147
    narrator "조금 전 메시지에서 로만 씨가 아쉬워했던 것 같기도 하다."
    # SOURCE R03 L150 (주인공 · 혼잣말)
    mc "……아니겠지."
    # SOURCE R03 L154
    narrator "괜히 내가 너무 깊게 생각하는 걸 거다."
    # SOURCE R03 L156
    narrator "로만 씨도 바쁘다고 했으니까."
    # SOURCE R03 L158
    narrator "지금은 준비에 집중하는 게 좋겠지."
    # SOURCE R03 L160
    narrator "나는 휴대전화를 내려놓았다."
    # CONTI SOURCE R03 L162 [FADE OUT]
    # CONTI SOURCE R03 L164 [SCENE 01 END]
    jump roman_r03_sc02

label roman_r03_sc02:
    $ phone_timeline_enter("R03", "roman_r03_sc02")
    # SOURCE R03 L167 # R03 SC02 · 기다리지 않아도 괜찮다면서
    # SOURCE R03 L169 [BG] 캠퍼스 도서관 앞 · 저녁
    $ story_draft_scene("캠퍼스 도서관 앞 · 저녁")
    # SOURCE R03 L171 [BGM] Quiet Campus
    $ story_draft_bgm("Quiet Campus")
    # SOURCE R03 L175
    narrator "수업을 마치고 도서관 근처를 지나던 길이었다."
    # SOURCE R03 L177
    narrator "익숙한 모습이 눈에 들어왔다."
    # SOURCE R03 L179
    narrator "로만 씨였다."
    # SOURCE R03 L181
    narrator "벤치에 앉아 노트를 펼쳐놓고 있었다."
    # SOURCE R03 L183
    narrator "원고를 확인하는 모양이었다."
    # SOURCE R03 L185
    narrator "……그런데 평소보다 조금 피곤해 보였다."
    # SOURCE R03 L188 (주인공)
    mc "로만 씨."
    # SOURCE R03 L191 (로만)
    roman "……앗!"
    # SOURCE R03 L193 (로만)
    roman "[player_name] 씨……!"
    # SOURCE R03 L196 (주인공)
    mc "안녕하세요. 여기서 원고 쓰고 계셨어요?"
    # SOURCE R03 L199 (로만)
    roman "네……."
    # SOURCE R03 L201 (로만)
    roman "도서관에서 쓰다가 잠깐 나왔어요."
    # SOURCE R03 L204 (주인공)
    mc "많이 진행하셨어요?"
    # SOURCE R03 L207 (로만)
    roman "음……."
    # SOURCE R03 L209 (로만)
    roman "거의 다 썼는데, 마지막 부분이 계속 마음에 걸려서요."
    # SOURCE R03 L212 (주인공)
    mc "그렇군요."
    # SOURCE R03 L216
    narrator "로만 씨는 노트를 덮었다."
    # SOURCE R03 L218
    narrator "그러다가 나를 잠시 바라봤다."
    # SOURCE R03 L221 (로만)
    roman "……오랜만이네요."
    # SOURCE R03 L224 (주인공)
    mc "그러게요. 며칠 못 뵀네요."
    # SOURCE R03 L227 (로만)
    roman "후후…… 네."
    # SOURCE R03 L231
    narrator "잠깐 정적이 흘렀다."
    # SOURCE R03 L233
    narrator "평소 같으면 로만 씨가 읽고 있는 책에 관해 이야기했을 텐데."
    # SOURCE R03 L235
    narrator "오늘은 무슨 말을 해야 할지 조금 망설여졌다."
    # SOURCE R03 L238 (주인공)
    mc "원고 마감이 얼마 안 남았죠?"
    # SOURCE R03 L241 (로만)
    roman "네. 이틀 남았어요."
    # SOURCE R03 L244 (주인공)
    mc "그럼 정말 바쁘시겠네요."
    # SOURCE R03 L247 (로만)
    roman "……그렇죠."
    # SOURCE R03 L251
    narrator "로만 씨는 작은 미소를 지었다."
    # SOURCE R03 L253
    narrator "그런데 그 미소가 조금 어색해 보였다."
    # SOURCE R03 L256 (로만)
    roman "저기……."
    # SOURCE R03 L259 (주인공)
    mc "네?"
    # SOURCE R03 L262 (로만)
    roman "혹시 오늘은……."
    # CONTI SOURCE R03 L264 [SFX] 도서관 안내 방송
    # SOURCE R03 L267 (안내 방송)
    narrator "안내 방송: 잠시 후 열람실 일부 구역의 이용 시간이 종료됩니다."
    # SOURCE R03 L271
    narrator "로만 씨는 말을 멈췄다."
    # SOURCE R03 L273
    narrator "그리고 도서관 입구를 바라봤다."
    # SOURCE R03 L276 (로만)
    roman "……아."
    # SOURCE R03 L278 (로만)
    roman "아직 자료를 안 챙겼네요."
    # SOURCE R03 L281 (주인공)
    mc "그럼 먼저 들어가 보셔야겠어요."
    # SOURCE R03 L284 (로만)
    roman "……."
    # SOURCE R03 L286 (로만)
    roman "네."
    # SOURCE R03 L289 (주인공)
    mc "원고 마무리 잘하세요. 제출 끝나면 같이 식사해요."
    # SOURCE R03 L292 (로만)
    roman "……네."
    # SOURCE R03 L294 (로만)
    roman "그럴게요."
    # SOURCE R03 L298
    narrator "로만 씨는 노트를 품에 안았다."
    # SOURCE R03 L300
    narrator "한 걸음 움직였다가 다시 돌아봤다."
    # SOURCE R03 L303 (로만)
    roman "[player_name] 씨."
    # SOURCE R03 L306 (주인공)
    mc "네?"
    # SOURCE R03 L309 (로만)
    roman "……아니에요."
    # SOURCE R03 L311 (로만)
    roman "오늘도 좋은 저녁 보내세요."
    # SOURCE R03 L314 (주인공)
    mc "로만 씨도요."
    # SOURCE R03 L318
    narrator "로만 씨는 도서관 안으로 들어갔다."
    # SOURCE R03 L320
    narrator "나는 잠시 그 자리에 서 있었다."
    # SOURCE R03 L322
    narrator "……뭔가 말하려던 것 같은데."
    # SOURCE R03 L324
    narrator "왜 끝까지 묻지 않았을까."
    # SOURCE R03 L326
    narrator "그 순간에는 그냥 바빠서 그런 거라고 생각했다."
    # SOURCE R03 L328
    narrator "그런데 돌아가는 길에도 로만 씨의 마지막 표정이 자꾸 떠올랐다."
    # CONTI SOURCE R03 L330 [TRANSITION] 같은 날 · 오후 9:20
    $ phone_timeline_cue("R03", "R03_L330")
    # SOURCE R03 L332 [BG] 주인공 방 · 밤
    $ story_draft_scene("주인공 방 · 밤")
    # CONTI SOURCE R03 L334 [UI] 스마트폰 화면
    # SOURCE R03 L338
    narrator "로만 씨에게 연락할까."
    # SOURCE R03 L340
    narrator "잘 들어가셨냐고 물어보면 될까."
    # SOURCE R03 L342
    narrator "아니면 원고 때문에 바쁠 테니 오늘은 그냥 두는 게 좋을까."
    # SOURCE R03 L344
    narrator "메시지 작성창을 열었다."
    # SOURCE R03 L347 (주인공 · 작성 중)
    narrator "로만 씨, 아까 무슨 말씀 하시려던 거예요?"
    # SOURCE R03 L351
    narrator "……."
    # SOURCE R03 L353
    narrator "조금 부담스러울 수도 있겠다."
    # SOURCE R03 L355
    narrator "나는 문장을 지웠다."
    # SOURCE R03 L358 (주인공 · 혼잣말)
    mc "마감 끝나고 이야기하면 되겠지."
    # SOURCE R03 L362
    narrator "그렇게 생각하며 휴대전화를 내려놓았다."
    # CONTI SOURCE R03 L364 [SCENE 02 END]
    jump roman_r03_sc03

label roman_r03_sc03:
    $ phone_timeline_enter("R03", "roman_r03_sc03")
    # SOURCE R03 L367 # R03 SC03 · 그 사람이 싫어진 건 아닌데
    # SOURCE R03 L369 [BG] 교내 카페 · 점심
    $ story_draft_scene("교내 카페 · 점심")
    # SOURCE R03 L371 [BGM] Calm Daily
    $ story_draft_bgm("Calm Daily")
    # SOURCE R03 L375
    narrator "점심을 먹으려고 카페에 들렀다."
    # SOURCE R03 L377
    narrator "주문을 마치고 빈자리를 찾는데 익숙한 목소리가 들렸다."
    # SOURCE R03 L380 (다림)
    darim "어머, [player_name] 씨."
    # SOURCE R03 L383 (주인공)
    mc "다림 선배, 안녕하세요."
    # SOURCE R03 L386 (다림)
    darim "혼자 오셨어요?"
    # SOURCE R03 L389 (주인공)
    mc "네. 선배도요?"
    # SOURCE R03 L392 (다림)
    darim "저는 다음 강의까지 시간이 조금 남아서요."
    # SOURCE R03 L394 (다림)
    darim "괜찮으시면 같이 앉으실래요?"
    # SOURCE R03 L397 (주인공)
    mc "좋아요."
    # SOURCE R03 L399 [BG] 카페 창가 자리
    $ story_draft_scene("카페 창가 자리")
    # SOURCE R03 L403
    narrator "다림 선배는 노트북을 닫고 음료를 한 모금 마셨다."
    # SOURCE R03 L406 (다림)
    darim "요즘은 어떻게 지내세요?"
    # SOURCE R03 L409 (주인공)
    mc "그냥 수업 듣고 과제하면서 지내고 있어요."
    # SOURCE R03 L412 (다림)
    darim "후후. 축제 준비하던 때보다 여유롭겠네요."
    # SOURCE R03 L415 (주인공)
    mc "그렇죠. 그런데 가끔은 좀 허전해요."
    # SOURCE R03 L418 (다림)
    darim "저도 그래요."
    # SOURCE R03 L422
    narrator "우리는 축제 때 있었던 일을 잠시 이야기했다."
    # SOURCE R03 L424
    narrator "그러다 다림 선배가 물었다."
    # SOURCE R03 L427 (다림)
    darim "아, 로만 씨하고는 요즘도 자주 만나세요?"
    # SOURCE R03 L430 (주인공)
    mc "……아."
    # SOURCE R03 L433 (다림)
    darim "왜 그러세요?"
    # SOURCE R03 L436 (주인공)
    mc "요즘은 조금 바쁘신 것 같더라고요."
    # SOURCE R03 L438 (주인공)
    mc "낭독회 원고 때문에요."
    # SOURCE R03 L441 (다림)
    darim "맞아요. 마감이 얼마 안 남았죠."
    # SOURCE R03 L444 (주인공)
    mc "그래서 되도록 방해하지 않으려고요."
    # SOURCE R03 L447 (다림)
    darim "……방해요?"
    # SOURCE R03 L450 (주인공)
    mc "네. 준비에 집중하셔야 하니까요."
    # SOURCE R03 L454
    narrator "다림 선배는 잠시 생각했다."
    # SOURCE R03 L457 (다림)
    darim "후후. 배려해 주시는 거군요."
    # SOURCE R03 L460 (주인공)
    mc "그런데 제가 제대로 하고 있는 건지는 모르겠어요."
    # SOURCE R03 L463 (다림)
    darim "무슨 일이 있으셨어요?"
    # SOURCE R03 L466 (주인공)
    mc "로만 씨가 저녁에 만나자고 하셨는데 제가 다음에 보자고 했거든요."
    # SOURCE R03 L468 (주인공)
    mc "마감이 가까워서 걱정됐어요."
    # SOURCE R03 L471 (다림)
    darim "아……."
    # SOURCE R03 L474 (주인공)
    mc "그리고 어제 도서관에서도 뭔가 말씀하시려다가 그냥 가셨어요."
    # SOURCE R03 L477 (다림)
    darim "……."
    # SOURCE R03 L481
    narrator "다림 선배는 바로 대답하지 않았다."
    # SOURCE R03 L484 (다림)
    darim "음……."
    # SOURCE R03 L486 (다림)
    darim "제가 로만 씨 마음을 대신 설명할 수는 없지만요."
    # SOURCE R03 L489 (주인공)
    mc "네."
    # SOURCE R03 L492 (다림)
    darim "한 가지는 말씀드릴 수 있을 것 같아요."
    # SOURCE R03 L494 (다림)
    darim "로만 씨가 먼저 만나자고 하셨다면, 나름대로 시간을 생각하고 제안하셨을 수도 있잖아요."
    # SOURCE R03 L497 (주인공)
    mc "……아."
    # SOURCE R03 L500 (다림)
    darim "바쁘다고 해서 누구도 만나고 싶지 않은 건 아니니까요."
    # SOURCE R03 L504
    narrator "그 말을 듣자 며칠 전의 대화가 떠올랐다."
    # SOURCE R03 L506
    narrator "오늘 저녁에는 시간 괜찮으세요?"
    # SOURCE R03 L508
    narrator "그래도 잠깐 만나서 이야기하면 좋을 것 같아서요."
    # SOURCE R03 L510
    narrator "로만 씨는 그렇게 말했었다."
    # SOURCE R03 L512
    narrator "그런데 나는 원고가 중요하다는 이유로 다음에 보자고 했다."
    # SOURCE R03 L515 (주인공)
    mc "……그러네요."
    # SOURCE R03 L518 (다림)
    darim "물론 실제로 어떤 마음이었는지는 직접 물어보셔야겠지만요."
    # SOURCE R03 L521 (주인공)
    mc "네. 그게 맞겠죠."
    # SOURCE R03 L524 (다림)
    darim "후후."
    # SOURCE R03 L526 (다림)
    darim "그리고 너무 어렵게 생각하지 않으셔도 돼요."
    # SOURCE R03 L530
    narrator "다림 선배는 웃었다."
    # SOURCE R03 L533 (다림)
    darim "로만 씨도 자기 생각이 있는 사람이니까요."
    # SOURCE R03 L535 (다림)
    darim "필요하면 직접 말씀하실 수 있도록 들어주시면 되죠."
    # SOURCE R03 L538 (주인공)
    mc "그렇게 해볼게요."
    # SOURCE R03 L541 (다림)
    darim "좋아요."
    # CONTI SOURCE R03 L543 [시간 경과 · 오후 1:05]
    $ phone_timeline_cue("R03", "R03_L543")
    # SOURCE R03 L547
    narrator "카페를 나서기 전에 다림 선배가 덧붙였다."
    # SOURCE R03 L550 (다림)
    darim "참, 로만 씨 원고 이야기는 로만 씨랑 직접 나눠보세요."
    # SOURCE R03 L552 (다림)
    darim "제가 수업에서 듣는 이야기를 전부 옮기면 곤란하니까요."
    # SOURCE R03 L555 (주인공)
    mc "네. 당연하죠."
    # SOURCE R03 L558 (다림)
    darim "그럼 좋은 하루 보내세요."
    # SOURCE R03 L561 (주인공)
    mc "선배도요."
    # SOURCE R03 L565
    narrator "다림 선배와 헤어진 뒤 휴대전화를 꺼냈다."
    # SOURCE R03 L567
    narrator "나는 로만 씨를 방해하지 않으려고 했다."
    # SOURCE R03 L569
    narrator "하지만 어쩌면 로만 씨가 어떻게 생각하는지 물어보지도 않고, 혼자서 모든 걸 결정해 버린 건 아닐까."
    # SOURCE R03 L572 (주인공 · 혼잣말)
    mc "……한번 이야기해 봐야겠네."
    # CONTI SOURCE R03 L574 [UI] 로만 개인 메시지
    $ story_chat(True, title="로만")
    # SOURCE R03 L577 (주인공 · 메시지)
    mc "로만 씨, 원고 준비는 잘되고 계세요?"
    # SOURCE R03 L580 (주인공 · 메시지)
    mc "마감 끝나고 시간 괜찮으시면 같이 이야기하고 싶어요."
    # SOURCE R03 L584
    narrator "보내고 나니 조금 마음이 놓였다."
    # SOURCE R03 L586
    narrator "하지만 한편으로는 여전히 궁금했다."
    # SOURCE R03 L588
    narrator "왜 나는 처음부터 이렇게 연락하지 못했을까."
    # CONTI SOURCE R03 L590 [SCENE 03 END]
    $ story_chat(False)
    jump roman_r03_sc04

label roman_r03_sc04:
    $ phone_timeline_enter("R03", "roman_r03_sc04")
    # SOURCE R03 L593 # R03 SC04 · 보내지 못한 메시지
    # CONTI SOURCE R03 L595 [POV] 로만
    $ phone_perspective_set("roman")
    # SOURCE R03 L597 [BG] 도서관 구석 자리 · 오후
    $ story_draft_scene("도서관 구석 자리 · 오후")
    # SOURCE R03 L599 [BGM] Quiet Pages
    $ story_draft_bgm("Quiet Pages")
    # CONTI SOURCE R03 L601 [연출] 일반적인 주인공 독백창 대신 로만의 내면 장면임을 구분하는 화면 전환. 새로운 CG나 애니메이션 필수 아님.
    # SOURCE R03 L605
    narrator "도서관 구석 자리."
    # SOURCE R03 L607
    narrator "로만은 원고를 펼쳐놓고 마지막 문장을 고치고 있었다."
    # SOURCE R03 L609
    narrator "이미 몇 번이나 수정한 부분이었다."
    # SOURCE R03 L611
    narrator "문장을 지웠다."
    # SOURCE R03 L613
    narrator "다시 썼다."
    # SOURCE R03 L615
    narrator "그런데 여전히 마음에 들지 않았다."
    # SOURCE R03 L618 (로만 · 혼잣말)
    roman "……이것도 아닌 것 같아요."
    # SOURCE R03 L622
    narrator "로만은 펜을 내려놓았다."
    # SOURCE R03 L624
    narrator "원고 마감까지 하루."
    # SOURCE R03 L626
    narrator "지난주에는 참가 신청을 하는 것만으로도 꽤 큰 용기가 필요했다."
    # SOURCE R03 L628
    narrator "지금은 어떻게든 자신의 글을 완성하고 싶었다."
    # SOURCE R03 L630
    narrator "그런데 요즘은 자꾸 다른 생각이 끼어들었다."
    # CONTI SOURCE R03 L632 [SFX] 휴대전화 진동
    # CONTI SOURCE R03 L634 [UI] 주인공 메시지 도착
    $ story_chat(True, title="로만")
    # SOURCE R03 L637 (주인공 · 메시지)
    mc "로만 씨, 원고 준비는 잘되고 계세요?"
    # SOURCE R03 L639 (주인공 · 메시지)
    mc "마감 끝나고 시간 괜찮으시면 같이 이야기하고 싶어요."
    # SOURCE R03 L643
    narrator "로만은 한참 화면을 바라봤다."
    # SOURCE R03 L645
    narrator "그리고 작게 웃었다."
    # SOURCE R03 L648 (로만 · 혼잣말)
    narrator "……연락 주셨네."
    # SOURCE R03 L652
    narrator "반가웠다."
    # SOURCE R03 L654
    narrator "분명 반가웠다."
    # SOURCE R03 L656
    narrator "그런데 문득 며칠 전의 일이 떠올랐다."
    # SOURCE R03 L658
    narrator "그날 로만은 원고를 잠시 내려놓고 함께 저녁을 먹고 싶었다."
    # SOURCE R03 L660
    narrator "새로 쓴 글이 마음에 들지 않는다는 이야기도 하고 싶었고, 그냥 평범하게 밥을 먹으면서 웃고 싶었다."
    # SOURCE R03 L662
    narrator "하지만 주인공은 다음에 만나자고 했다."
    # SOURCE R03 L664
    narrator "원고에 집중하는 게 좋겠다고."
    # SOURCE R03 L666
    narrator "틀린 말은 아니었다."
    # SOURCE R03 L668
    narrator "오히려 자신을 생각해서 한 말이라는 것도 알고 있었다."
    # SOURCE R03 L670
    narrator "그런데……."
    # SOURCE R03 L673 (로만 · 혼잣말)
    narrator "……조금 서운했는데."
    # SOURCE R03 L677
    narrator "로만은 메시지 작성창을 열었다."
    # CONTI SOURCE R03 L679 [UI] 메시지 작성 · 전송하지 않음
    # SOURCE R03 L681
    narrator "사실은 그날 잠깐 만나고 싶었어요."
    # SOURCE R03 L685
    narrator "손가락이 멈췄다."
    # SOURCE R03 L687
    narrator "이렇게 보내면 괜히 부담을 주는 건 아닐까."
    # SOURCE R03 L689
    narrator "원고도 아직 끝나지 않았는데, 서운한 마음까지 말할 필요가 있을까."
    # SOURCE R03 L691
    narrator "로만은 잠시 고민했다."
    # SOURCE R03 L693
    narrator "그리고 문장을 지웠다."
    # SOURCE R03 L695
    narrator "다시 적었다."
    # SOURCE R03 L697
    narrator "마감 끝나면 꼭 만나요."
    # SOURCE R03 L701
    narrator "이번에도 바로 보내지 않았다."
    # SOURCE R03 L703
    narrator "로만은 노트 옆에 놓인 책갈피를 바라봤다."
    # SOURCE R03 L705
    narrator "축제 때 만들었던 작은 파란 꽃 책갈피였다."
    # SOURCE R03 L708 (로만 · 혼잣말)
    narrator "……저도 기다리라고만 하면 안 되겠죠."
    # SOURCE R03 L712
    narrator "로만은 천천히 메시지를 입력했다."
    # CONTI SOURCE R03 L714 [UI] 최종 전송 메시지
    # SOURCE R03 L717 (로만)
    roman "앗,,, 연락 주셔서 고마워요……!"
    # SOURCE R03 L719 (로만)
    roman "원고는 거의 다 썼어요."
    # SOURCE R03 L721 (로만)
    roman "제출 끝나면 같이 이야기하고 싶어요."
    # SOURCE R03 L723 (로만)
    roman "사실 저도 드리고 싶은 말씀이 있거든요."
    # CONTI SOURCE R03 L725 [UI] 스마트폰 화면 종료
    $ story_chat(False)
    # SOURCE R03 L729
    narrator "전송 버튼을 누른 뒤 로만은 노트를 다시 펼쳤다."
    # SOURCE R03 L731
    narrator "그러나 이번에는 곧바로 글을 쓰지 않았다."
    # SOURCE R03 L733
    narrator "먼저 노트 한쪽에 짧은 문장을 적었다."
    # SOURCE R03 L735
    narrator "말하지 않으면 상대는 알 수 없다."
    # SOURCE R03 L737
    narrator "로만은 그 문장을 한 번 읽었다."
    # SOURCE R03 L740 (로만 · 혼잣말)
    roman "……이번에는 직접 말해볼래요."
    # SOURCE R03 L744
    narrator "로만은 다시 펜을 들었다."
    # SOURCE R03 L746
    narrator "원고 마지막 부분에 적혀 있던 문장을 천천히 고치기 시작했다."
    # CONTI SOURCE R03 L748 [POV END]
    $ phone_perspective_set("mc")
    # CONTI SOURCE R03 L750 [FADE TO BLACK]
    # CONTI SOURCE R03 L752 [SCENE 04 END]
    jump roman_r03_sc05

label roman_r03_sc05:
    $ phone_timeline_enter("R03", "roman_r03_sc05")
    # SOURCE R03 L755 # R03 SC05 · 말하지 않아도 알 줄 알았어요
    # SOURCE R03 L757 [BG] 캠퍼스 작은 정원 · 늦은 오후
    $ story_draft_scene("캠퍼스 작은 정원 · 늦은 오후")
    # SOURCE R03 L759 [BGM] Quiet Sunset
    $ story_draft_bgm("Quiet Sunset")
    # CONTI SOURCE R03 L761 [FADE IN]
    # SOURCE R03 L765
    narrator "로만 씨가 낭독회 원고를 제출했다."
    # SOURCE R03 L767
    narrator "어젯밤에 접수 확인 메시지를 받았고, 오늘은 잠깐 만나기로 했다."
    # SOURCE R03 L769
    narrator "한동안 원고를 붙잡고 있었으니 지금쯤 조금 홀가분해졌을까."
    # SOURCE R03 L771
    narrator "정원에 도착하자 벤치에 앉아 있는 로만 씨가 보였다."
    # SOURCE R03 L773
    narrator "무릎 위에는 늘 가지고 다니던 노트가 있었다."
    # SOURCE R03 L776 (주인공)
    mc "로만 씨."
    # SOURCE R03 L779 (로만)
    roman "앗,,, 오셨어요."
    # SOURCE R03 L782 (주인공)
    mc "안녕하세요. 원고 제출하신 거 축하드려요."
    # SOURCE R03 L785 (로만)
    roman "……후후. 고마워요."
    # SOURCE R03 L788 (주인공)
    mc "기분이 어떠세요?"
    # SOURCE R03 L791 (로만)
    roman "조금 후련해요."
    # SOURCE R03 L793 (로만)
    roman "그런데 제출하고 나니까 또 이상한 데가 보이는 것 같아서……."
    # SOURCE R03 L796 (주인공)
    mc "이미 제출하셨잖아요."
    # SOURCE R03 L799 (로만)
    roman "그러니까요."
    # SOURCE R03 L801 (로만)
    roman "이제는 고칠 수도 없는데 자꾸 생각나요."
    # SOURCE R03 L805
    narrator "로만 씨는 작게 웃었다."
    # SOURCE R03 L807
    narrator "하지만 조금 전과 달리 웃음이 금방 사라졌다."
    # SOURCE R03 L810 (로만)
    roman "저기……."
    # SOURCE R03 L813 (주인공)
    mc "네?"
    # SOURCE R03 L816 (로만)
    roman "오늘은 꼭 말씀드리고 싶은 게 있어요."
    # SOURCE R03 L819 (주인공)
    mc "네. 듣고 있어요."
    # SOURCE R03 L823
    narrator "로만 씨는 두 손을 무릎 위에 모았다."
    # SOURCE R03 L825
    narrator "잠시 정적이 흘렀다."
    # SOURCE R03 L828 (로만)
    roman "그날……."
    # SOURCE R03 L830 (로만)
    roman "제가 저녁에 만나자고 했던 날이요."
    # SOURCE R03 L833 (주인공)
    mc "네."
    # SOURCE R03 L836 (로만)
    roman "사실은 원고 이야기를 하고 싶었어요."
    # SOURCE R03 L838 (로만)
    roman "그런데 그것만은 아니었고……."
    # SOURCE R03 L842
    narrator "로만 씨가 시선을 내렸다."
    # SOURCE R03 L845 (로만)
    roman "그냥 같이 밥 먹고 싶었어요."
    # SOURCE R03 L848 (주인공)
    mc "……아."
    # SOURCE R03 L851 (로만)
    roman "계속 글만 쓰고 있으니까 조금 답답하기도 했고."
    # SOURCE R03 L853 (로만)
    roman "무엇보다……."
    # SOURCE R03 L855 (로만)
    roman "그냥 [player_name] 씨랑 이야기하고 싶었어요."
    # SOURCE R03 L859
    narrator "나는 아무 말도 하지 못했다."
    # SOURCE R03 L861
    narrator "그런 이유였구나."
    # SOURCE R03 L864 (로만)
    roman "그런데 원고에 집중하라고 하시니까……."
    # SOURCE R03 L866 (로만)
    roman "제가 너무 자주 만나자고 했나 싶었어요."
    # SOURCE R03 L869 (주인공)
    mc "……."
    # SOURCE R03 L872 (로만)
    roman "물론 저를 배려해 주신 거라는 건 알아요."
    # SOURCE R03 L874 (로만)
    roman "그런데 조금……."
    # SOURCE R03 L877 (로만)
    roman "서운했어요."
    # SOURCE R03 L879 [BGM] 아주 작게 줄어듦
    $ story_draft_bgm("아주 작게 줄어듦")
    # SOURCE R03 L883
    narrator "로만 씨는 마지막 말을 조심스럽게 꺼냈다."
    # SOURCE R03 L885
    narrator "그러고는 내 반응을 기다렸다."
    # SOURCE R03 L888 (주인공)
    mc "……그랬군요."
    # SOURCE R03 L891 (로만)
    roman "……네."
    # SOURCE R03 L894 (주인공)
    mc "저는 로만 씨가 바쁘실 거라고 생각했어요."
    # SOURCE R03 L896 (주인공)
    mc "중요한 원고를 쓰고 계셨으니까요."
    # SOURCE R03 L899 (로만)
    roman "알아요."
    # SOURCE R03 L902 (주인공)
    mc "그래서 만나자고 하셔도 제가 방해하는 건 아닐까 걱정됐어요."
    # SOURCE R03 L905 (로만)
    roman "……."
    # SOURCE R03 L908 (로만)
    roman "그런데 저는 제가 시간을 내서 만나고 싶었던 거였어요."
    # SOURCE R03 L912
    narrator "그 말이 조금 아프게 들렸다."
    # SOURCE R03 L914
    narrator "화가 난 목소리는 아니었다."
    # SOURCE R03 L916
    narrator "하지만 분명한 서운함이 있었다."
    # SOURCE R03 L919 (주인공)
    mc "……제가 그걸 제대로 생각하지 못했네요."
    # SOURCE R03 L922 (로만)
    roman "……."
    # SOURCE R03 L925 (주인공)
    mc "로만 씨가 직접 만나고 싶다고 하셨는데, 제가 혼자서 안 만나는 게 낫겠다고 결정했어요."
    # SOURCE R03 L928 (로만)
    roman "……네."
    # SOURCE R03 L932
    narrator "로만 씨는 고개를 끄덕였다."
    # SOURCE R03 L934
    narrator "하지만 곧바로 웃지는 않았다."
    # SOURCE R03 L937 (로만)
    roman "저도 말씀드리지 않았잖아요."
    # SOURCE R03 L939 (로만)
    roman "그날 꼭 만나고 싶었다고."
    # SOURCE R03 L942 (주인공)
    mc "그러네요."
    # SOURCE R03 L945 (로만)
    roman "그래서……."
    # SOURCE R03 L948 (로만)
    roman "말하지 않아도 알 줄 알았어요."
    # SOURCE R03 L952
    narrator "나는 조용히 그 말을 되새겼다."
    # SOURCE R03 L954
    narrator "말하지 않아도 알 줄 알았다."
    # SOURCE R03 L956
    narrator "우리는 책 속 문장에 관해서는 서로 다른 해석을 이야기할 수 있었다."
    # SOURCE R03 L958
    narrator "그런데 정작 우리 마음에 대해서는 그러지 못했다."
    # SOURCE R03 L961 (로만)
    roman "저기……."
    # SOURCE R03 L964 (주인공)
    mc "네?"
    # SOURCE R03 L967 (로만)
    roman "제가 이렇게 말하는 게 혹시 불편하세요?"
    # SOURCE R03 L971
    narrator "로만 씨의 목소리가 조금 작아졌다."
    # SOURCE R03 L974 (주인공)
    mc "아니요."
    # SOURCE R03 L976 (주인공)
    mc "서운하셨다면 말씀해 주시는 게 좋아요."
    # SOURCE R03 L979 (로만)
    roman "……."
    # SOURCE R03 L983
    narrator "로만 씨는 잠시 나를 바라봤다."
    # SOURCE R03 L986 (로만)
    roman "정말요?"
    # SOURCE R03 L989 (주인공)
    mc "네. 저도 로만 씨가 어떤 생각을 하셨는지 알고 싶으니까요."
    # SOURCE R03 L993
    narrator "로만 씨는 조금 숨을 고르는 듯했다."
    # SOURCE R03 L995
    narrator "그리고 천천히 고개를 끄덕였다."
    # SOURCE R03 L998 (로만)
    roman "……네."
    # SOURCE R03 L1000 (로만)
    roman "그럼 저도 이번에는 끝까지 이야기해 볼게요."
    # CONTI SOURCE R03 L1002 [SCENE 05 END]
    jump roman_r03_sc06

label roman_r03_sc06:
    $ phone_timeline_enter("R03", "roman_r03_sc06")
    # SOURCE R03 L1005 # R03 SC06 · 필요한 건 대답이 아니라
    # SOURCE R03 L1007 [BG] 캠퍼스 작은 정원 · 노을
    $ story_draft_scene("캠퍼스 작은 정원 · 노을")
    # SOURCE R03 L1009 [BGM] Gentle Emotional
    $ story_draft_bgm("Gentle Emotional")
    # SOURCE R03 L1013
    narrator "로만 씨는 노트를 옆자리에 내려놓았다."
    # SOURCE R03 L1015
    narrator "평소에는 무슨 이야기를 할 때마다 노트를 만지작거리곤 했는데."
    # SOURCE R03 L1017
    narrator "이번에는 아무것도 들지 않은 채 나를 바라봤다."
    # SOURCE R03 L1020 (로만)
    roman "제가 원고를 쓰는 동안……."
    # SOURCE R03 L1022 (로만)
    roman "많이 바쁜 건 맞았어요."
    # SOURCE R03 L1025 (주인공)
    mc "네."
    # SOURCE R03 L1028 (로만)
    roman "그래도 가끔은 다른 이야기도 하고 싶었어요."
    # SOURCE R03 L1030 (로만)
    roman "원고가 잘 안 써질 때도 있고, 좋은 문장이 떠올랐을 때도 있고……."
    # SOURCE R03 L1033 (로만)
    roman "그런 걸 [player_name] 씨한테 이야기하고 싶었거든요."
    # SOURCE R03 L1037
    narrator "로만 씨는 잠시 웃었다."
    # SOURCE R03 L1040 (로만)
    roman "그런데 연락드릴 때마다 괜히 고민하게 됐어요."
    # SOURCE R03 L1042 (로만)
    roman "지금 보내도 되나."
    # SOURCE R03 L1044 (로만)
    roman "너무 많이 보내는 건 아닐까."
    # SOURCE R03 L1047 (주인공)
    mc "……."
    # SOURCE R03 L1050 (로만)
    roman "그러다 보니까 평소보다 더 어색해졌어요."
    # SOURCE R03 L1054
    narrator "그 말이 이해됐다."
    # SOURCE R03 L1056
    narrator "사실 나도 비슷했다."
    # SOURCE R03 L1058
    narrator "원고를 방해할까 봐 먼저 연락하지 않았고, 하고 싶은 말이 있어도 마감이 끝난 다음으로 미뤘다."
    # SOURCE R03 L1061 (주인공)
    mc "저도 그랬어요."
    # SOURCE R03 L1064 (로만)
    roman "……정말요?"
    # SOURCE R03 L1067 (주인공)
    mc "네. 로만 씨가 바쁘시니까 제가 먼저 연락하지 않는 게 좋겠다고 생각했거든요."
    # SOURCE R03 L1070 (로만)
    roman "……."
    # SOURCE R03 L1073 (로만)
    roman "그럼 우리 둘 다……."
    # SOURCE R03 L1075 (로만)
    roman "서로 생각한다고 조금 멀어진 거네요."
    # SOURCE R03 L1079
    narrator "로만 씨가 작게 웃었다."
    # SOURCE R03 L1081
    narrator "하지만 아직 마음에 남은 질문이 있는 것 같았다."
    # SOURCE R03 L1084 (로만)
    roman "그럼 앞으로는 어떻게 하면 좋을까요?"
    # SOURCE R03 L1087 (로만)
    roman "저는……."
    # SOURCE R03 L1089 (로만)
    roman "이런 일이 또 생기지 않았으면 좋겠어요."
    # SOURCE R03 L1091 [CHOICE 01 · 앞으로의 연락]
    menu:
        # SOURCE R03 L1093 선택지
        "서로 필요한 걸 직접 이야기하자.":
            # SOURCE R03 L1096 (주인공)
            mc "다음에는 서로 어떤 시간이 필요한지 직접 이야기해요."
            # SOURCE R03 L1098 (주인공)
            mc "바쁠 때는 바쁘다고 말씀드리고, 만나고 싶을 때는 그 마음도 솔직하게 말해요."
            # SOURCE R03 L1101 (로만)
            roman "……."
            # SOURCE R03 L1104 (로만)
            roman "후후……."
            # SOURCE R03 L1106 (로만)
            roman "그렇게 하면 좋겠어요."
            # SOURCE R03 L1109 (로만)
            roman "그럼 저도 다음에는 그냥 만나고 싶다고 말씀드릴게요."
            # SOURCE R03 L1112 (주인공)
            mc "네. 저도 그럴게요."
            # SOURCE R03 L1114 [FLAG] `roman_mutual_respect += 2`
            # SOURCE R03 L1116 [FLAG] `roman_r03_conflict_resolved = True`
            $ story_apply("roman_r03_choice01_a", values={'roman_r03_conflict_resolved': True}, counters={'roman_mutual_respect': 2})
        # SOURCE R03 L1120 선택지
        "로만 씨가 외롭지 않게 내가 더 자주 연락하겠다.":
            # SOURCE R03 L1123 (주인공)
            mc "앞으로는 제가 먼저 더 자주 연락드릴게요."
            # SOURCE R03 L1125 (주인공)
            mc "로만 씨가 혼자 기다리시지 않도록요."
            # SOURCE R03 L1128 (로만)
            roman "……정말요?"
            # SOURCE R03 L1131 (주인공)
            mc "네. 제가 좀 더 신경 쓰면 되겠죠."
            # SOURCE R03 L1134 (로만)
            roman "……."
            # SOURCE R03 L1137 (로만)
            roman "그러면 조금 기쁠 것 같아요."
            # SOURCE R03 L1141
            narrator "로만 씨는 웃었다."
            # SOURCE R03 L1143
            narrator "하지만 금방 다시 말했다."
            # SOURCE R03 L1146 (로만)
            roman "그런데 [player_name] 씨도 바쁘실 때가 있잖아요."
            # SOURCE R03 L1149 (주인공)
            mc "그럴 때는 최대한 시간 내볼게요."
            # SOURCE R03 L1152 (로만)
            roman "……후후."
            # SOURCE R03 L1154 (로만)
            roman "고마워요."
            # SOURCE R03 L1158
            narrator "로만 씨는 고맙다고 했다."
            # SOURCE R03 L1160
            narrator "하지만 나는 아직 로만 씨가 원하는 게 얼마나 자주 연락하는 것인지, 아니면 그냥 솔직한 이야기를 나누는 것인지 제대로 묻지 않았다."
            # SOURCE R03 L1162 [FLAG] `roman_reassurance_dependency += 1`
            # SOURCE R03 L1164 [FLAG] `roman_r03_conflict_resolved = False`
            $ story_apply("roman_r03_choice01_b", values={'roman_r03_conflict_resolved': False}, counters={'roman_reassurance_dependency': 1})
        # SOURCE R03 L1168 선택지
        "이제는 아무 걱정도 하지 않아도 된다고 약속한다.":
            # SOURCE R03 L1171 (주인공)
            mc "로만 씨는 걱정하지 않으셔도 돼요."
            # SOURCE R03 L1173 (주인공)
            mc "앞으로 제가 다 알아서 할게요."
            # SOURCE R03 L1176 (로만)
            roman "……."
            # SOURCE R03 L1179 (로만)
            roman "다…… 알아서요?"
            # SOURCE R03 L1182 (주인공)
            mc "네. 로만 씨가 서운하지 않도록 제가 더 신경 쓸게요."
            # SOURCE R03 L1185 (로만)
            roman "……."
            # SOURCE R03 L1188 (로만)
            roman "그렇게까지 하지 않으셔도 되는데……."
            # SOURCE R03 L1191 (주인공)
            mc "괜찮아요."
            # SOURCE R03 L1195
            narrator "로만 씨는 잠시 망설였다."
            # SOURCE R03 L1197
            narrator "그러다가 작게 웃었다."
            # SOURCE R03 L1200 (로만)
            roman "……고마워요."
            # SOURCE R03 L1202 (로만)
            roman "그렇게 말씀해 주시니까 마음이 놓여요."
            # SOURCE R03 L1206
            narrator "로만 씨의 표정이 조금 편안해졌다."
            # SOURCE R03 L1208
            narrator "그런데 이상하게도, 우리는 정확히 무엇을 약속한 건지 이야기하지 않았다."
            # SOURCE R03 L1210
            narrator "언제 연락할지."
            # SOURCE R03 L1212
            narrator "바쁠 때는 어떻게 할지."
            # SOURCE R03 L1214
            narrator "각자 원하는 시간이 다를 때는 어떻게 할지."
            # SOURCE R03 L1216
            narrator "그런 것은 여전히 모호한 채 남아 있었다."
            # SOURCE R03 L1218 [FLAG] `roman_reassurance_dependency += 2`
            # SOURCE R03 L1220 [FLAG] `roman_unrealistic_promise += 1`
            # SOURCE R03 L1222 [FLAG] `roman_r03_conflict_resolved = False`
            $ story_apply("roman_r03_choice01_c", values={'roman_r03_conflict_resolved': False}, counters={'roman_reassurance_dependency': 2, 'roman_unrealistic_promise': 1})
    # SOURCE R03 L1229 (로만)
    roman "……저기."
    # SOURCE R03 L1232 (주인공)
    mc "네?"
    # SOURCE R03 L1235 (로만)
    roman "오늘 이야기하길 잘한 것 같아요."
    # SOURCE R03 L1239
    narrator "로만 씨는 노트를 다시 집어 들었다."
    # SOURCE R03 L1242 (로만)
    roman "처음에는 조금 무서웠거든요."
    # SOURCE R03 L1245 (주인공)
    mc "어떤 게요?"
    # SOURCE R03 L1248 (로만)
    roman "서운했다고 말씀드리면……."
    # SOURCE R03 L1250 (로만)
    roman "혹시 저를 귀찮아하실까 봐요."
    # SOURCE R03 L1253 (주인공)
    mc "……그런 생각을 하셨군요."
    # SOURCE R03 L1256 (로만)
    roman "네."
    # SOURCE R03 L1258 (로만)
    roman "그래도 이번에는 이야기하고 싶었어요."
    # SOURCE R03 L1261 (로만)
    roman "계속 혼자 고민하는 건 싫어서요."
    # SOURCE R03 L1265
    narrator "나는 로만 씨를 바라봤다."
    # SOURCE R03 L1267
    narrator "조용하고 수줍은 사람이었다."
    # SOURCE R03 L1269
    narrator "하지만 지금은 자기 감정을 직접 설명하려고 애쓰고 있었다."
    # SOURCE R03 L1271
    narrator "그 모습이 어쩐지 대단하게 느껴졌다."
    # SOURCE R03 L1274 (주인공)
    mc "이렇게 이야기해 주셔서 감사해요."
    # SOURCE R03 L1277 (로만)
    roman "……후후."
    # SOURCE R03 L1279 (로만)
    roman "저도 들어주셔서 고마워요."
    # CONTI SOURCE R03 L1281 [SCENE 06 END]
    jump roman_r03_sc07

label roman_r03_sc07:
    $ phone_timeline_enter("R03", "roman_r03_sc07")
    # SOURCE R03 L1284 # R03 SC07 · 조금 이기적이어도 될까요?
    # SOURCE R03 L1286 [BG] 캠퍼스 산책로 · 저녁
    $ story_draft_scene("캠퍼스 산책로 · 저녁")
    # SOURCE R03 L1288 [BGM] Warm Evening
    $ story_draft_bgm("Warm Evening")
    # SOURCE R03 L1292
    narrator "우리는 정원을 나와 천천히 걸었다."
    # SOURCE R03 L1294
    narrator "조금 전까지 어색했던 분위기가 한결 편안해졌다."
    # SOURCE R03 L1296
    narrator "로만 씨는 가방끈을 고쳐 잡고 내 옆으로 걸었다."
    # SOURCE R03 L1299 (로만)
    roman "……후우."
    # SOURCE R03 L1302 (주인공)
    mc "이제 조금 편해지셨어요?"
    # SOURCE R03 L1305 (로만)
    roman "네……."
    # SOURCE R03 L1307 (로만)
    roman "사실 아까는 많이 긴장했어요."
    # SOURCE R03 L1310 (주인공)
    mc "그러셨을 것 같아요."
    # SOURCE R03 L1313 (로만)
    roman "말하고 싶은 게 있었는데……."
    # SOURCE R03 L1315 (로만)
    roman "계속 어떻게 시작해야 할지 모르겠더라고요."
    # SOURCE R03 L1319
    narrator "로만 씨는 잠시 웃었다."
    # SOURCE R03 L1322 (로만)
    roman "소설에서는 이런 장면을 몇 번이고 고쳐 쓸 수 있잖아요."
    # SOURCE R03 L1325 (주인공)
    mc "그렇죠."
    # SOURCE R03 L1328 (로만)
    roman "그런데 실제로는 그렇지 않으니까요."
    # SOURCE R03 L1330 (로만)
    roman "말을 꺼내고 나면 다시 지울 수도 없고……."
    # SOURCE R03 L1333 (주인공)
    mc "대신 다음 말을 할 수는 있잖아요."
    # SOURCE R03 L1336 (로만)
    roman "……."
    # SOURCE R03 L1339 (주인공)
    mc "처음부터 완벽하게 이야기하지 않아도 괜찮다고 생각해요."
    # SOURCE R03 L1343
    narrator "로만 씨가 걸음을 조금 늦췄다."
    # SOURCE R03 L1346 (로만)
    roman "……후후."
    # SOURCE R03 L1348 (로만)
    roman "맞아요."
    # SOURCE R03 L1350 (로만)
    roman "그럼 다음에는 조금 더 잘 말해볼게요."
    # CONTI SOURCE R03 L1352 [시간 경과 · 오후 6:35]
    $ phone_timeline_cue("R03", "R03_L1352")
    # SOURCE R03 L1354 [BG] 캠퍼스 갈림길 · 저녁
    $ story_draft_scene("캠퍼스 갈림길 · 저녁")
    # SOURCE R03 L1358
    narrator "갈림길에 도착했다."
    # SOURCE R03 L1360
    narrator "평소라면 이곳에서 서로 인사하고 헤어졌다."
    # SOURCE R03 L1362
    narrator "그런데 오늘 로만 씨는 바로 걸음을 옮기지 않았다."
    # SOURCE R03 L1365 (로만)
    roman "저기……."
    # SOURCE R03 L1368 (주인공)
    mc "네?"
    # SOURCE R03 L1371 (로만)
    roman "저 오늘 조금 이기적이어도 될까요?"
    # SOURCE R03 L1374 (주인공)
    mc "……이기적이요?"
    # SOURCE R03 L1377 (로만)
    roman "네."
    # SOURCE R03 L1381
    narrator "로만 씨는 눈을 한 번 깜빡였다."
    # SOURCE R03 L1383
    narrator "그러다가 조심스럽게 말을 이었다."
    # SOURCE R03 L1386 (로만)
    roman "오늘은 원고도 제출했고……."
    # SOURCE R03 L1388 (로만)
    roman "내일 아침 수업도 늦게 시작하거든요."
    # SOURCE R03 L1391 (주인공)
    mc "네."
    # SOURCE R03 L1394 (로만)
    roman "그래서……."
    # SOURCE R03 L1396 (로만)
    roman "조금만 더 같이 걷고 싶어요."
    # SOURCE R03 L1400
    narrator "……."
    # SOURCE R03 L1402
    narrator "나는 잠시 로만 씨를 바라봤다."
    # SOURCE R03 L1404
    narrator "그저 함께 조금 더 걷고 싶다는 부탁."
    # SOURCE R03 L1406
    narrator "그런데 로만 씨는 그것조차 조심스럽게 꺼내고 있었다."
    # SOURCE R03 L1409 (주인공)
    mc "그게 왜 이기적인 거예요?"
    # SOURCE R03 L1412 (로만)
    roman "……네?"
    # SOURCE R03 L1415 (주인공)
    mc "저도 괜찮은데요. 같이 조금 더 걸어요."
    # SOURCE R03 L1418 (로만)
    roman "……!"
    # CONTI SOURCE R03 L1420 [표정] 로만 · 놀람 → 수줍은 미소
    # SOURCE R03 L1423 (로만)
    roman "……정말요?"
    # SOURCE R03 L1426 (주인공)
    mc "네. 저도 아직 들어가고 싶지는 않았어요."
    # SOURCE R03 L1429 (로만)
    roman "……후후."
    # SOURCE R03 L1431 (로만)
    roman "그럼 조금만 더 걸어요."
    # SOURCE R03 L1433 [BG] 캠퍼스 작은 연못 · 저녁
    $ story_draft_scene("캠퍼스 작은 연못 · 저녁")
    # SOURCE R03 L1437
    narrator "우리는 조금 돌아가는 길을 택했다."
    # SOURCE R03 L1439
    narrator "연못 위로 저녁 불빛이 비치고 있었다."
    # SOURCE R03 L1441
    narrator "로만 씨는 걷다가 작은 나뭇잎 하나를 발견하고 잠시 멈췄다."
    # SOURCE R03 L1444 (로만)
    roman "……예쁘네요."
    # SOURCE R03 L1447 (주인공)
    mc "그러네요."
    # SOURCE R03 L1450 (로만)
    roman "이런 풍경을 보면 가끔 문장이 떠올라요."
    # SOURCE R03 L1453 (주인공)
    mc "지금도요?"
    # SOURCE R03 L1456 (로만)
    roman "네."
    # SOURCE R03 L1459 (주인공)
    mc "어떤 문장인데요?"
    # SOURCE R03 L1462 (로만)
    roman "……."
    # SOURCE R03 L1465 (로만)
    roman "비밀이에요."
    # SOURCE R03 L1468 (주인공)
    mc "또 비밀인가요?"
    # SOURCE R03 L1471 (로만)
    roman "후후……."
    # SOURCE R03 L1473 (로만)
    roman "이번에는 아직 정리되지 않아서요."
    # SOURCE R03 L1477
    narrator "로만 씨가 장난스럽게 웃었다."
    # SOURCE R03 L1480 (로만)
    roman "대신 나중에 보여드릴게요."
    # SOURCE R03 L1483 (주인공)
    mc "좋아요."
    # SOURCE R03 L1486 (로만)
    roman "……그런데."
    # SOURCE R03 L1489 (주인공)
    mc "네?"
    # SOURCE R03 L1492 (로만)
    roman "앞으로는 꼭 글이나 책 이야기만 하러 만나지 않아도 되죠?"
    # SOURCE R03 L1496
    narrator "나는 웃었다."
    # SOURCE R03 L1499 (주인공)
    mc "당연하죠."
    # SOURCE R03 L1501 (주인공)
    mc "오늘처럼 그냥 산책하자고 하셔도 돼요."
    # SOURCE R03 L1504 (로만)
    roman "……후후."
    # SOURCE R03 L1506 (로만)
    roman "그럼 앞으로도 가끔 같이 걸어요."
    # SOURCE R03 L1509 (주인공)
    mc "네. 좋아요."
    # SOURCE R03 L1511 [CONDITION] `roman_r03_conflict_resolved == True`
    if roman_r03_conflict_resolved == True:
        # SOURCE R03 L1514 (로만)
        roman "그리고 다음에는……."
        # SOURCE R03 L1516 (로만)
        roman "제가 만나고 싶으면 그냥 만나고 싶다고 말씀드릴게요."
        # SOURCE R03 L1519 (주인공)
        mc "네. 저도 그럴게요."
        # SOURCE R03 L1522 (로만)
        roman "……약속이에요."
    # SOURCE R03 L1524 [ELSE]
    else:
        # SOURCE R03 L1527 (로만)
        roman "그럼 다음에 제가 조금 외로우면……."
        # SOURCE R03 L1529 (로만)
        roman "연락드려도 되죠?"
        # SOURCE R03 L1532 (주인공)
        mc "네. 편하게 연락 주세요."
        # SOURCE R03 L1535 (로만)
        roman "……후후."
        # SOURCE R03 L1537 (로만)
        roman "그 말 기억할게요."
    # SOURCE R03 L1543
    narrator "우리는 연못을 지나 천천히 걸었다."
    # SOURCE R03 L1545
    narrator "오늘 처음에는 조금 어색했다."
    # SOURCE R03 L1547
    narrator "하지만 지금은 같이 걷는 것만으로도 기분이 편해졌다."
    # SOURCE R03 L1550 (로만)
    roman "오늘…… 고마웠어요."
    # SOURCE R03 L1553 (주인공)
    mc "저도 이야기해서 좋았어요."
    # SOURCE R03 L1556 (로만)
    roman "……네."
    # SOURCE R03 L1560
    narrator "로만 씨가 잠시 나를 바라봤다."
    # SOURCE R03 L1562
    narrator "그리고 아주 작은 목소리로 말했다."
    # SOURCE R03 L1565 (로만)
    roman "저는요."
    # SOURCE R03 L1567 (로만)
    roman "요즘 [player_name] 씨랑 보내는 시간이……."
    # SOURCE R03 L1571
    narrator "로만 씨가 잠시 말을 멈췄다."
    # SOURCE R03 L1574 (주인공)
    mc "네?"
    # SOURCE R03 L1577 (로만)
    roman "……아니에요."
    # SOURCE R03 L1579 (로만)
    roman "아직은 조금 부끄러워요."
    # SOURCE R03 L1582 (주인공)
    mc "그럼 나중에 말씀해 주세요."
    # SOURCE R03 L1585 (로만)
    roman "……후후."
    # SOURCE R03 L1587 (로만)
    roman "그럴게요."
    # SOURCE R03 L1591
    narrator "그 말의 뒷부분이 궁금했다."
    # SOURCE R03 L1593
    narrator "하지만 이번에는 굳이 재촉하고 싶지 않았다."
    # SOURCE R03 L1595
    narrator "내 마음에도 아직 다 설명하지 못한 부분이 있으니까."
    # CONTI SOURCE R03 L1597 [SCENE 07 END]
    jump roman_r03_sc08

label roman_r03_sc08:
    $ phone_timeline_enter("R03", "roman_r03_sc08")
    # SOURCE R03 L1599 # R03 SC08 · 아직 보내지 않은 문장
    # SOURCE R03 L1601 [BG] 주인공 방 · 밤
    $ story_draft_scene("주인공 방 · 밤")
    # SOURCE R03 L1603 [BGM] Night Reading
    $ story_draft_bgm("Night Reading")
    # CONTI SOURCE R03 L1605 [FADE IN]
    # SOURCE R03 L1609
    narrator "방에 돌아와 가방을 내려놓았다."
    # SOURCE R03 L1611
    narrator "오늘은 평소보다 조금 긴 하루였다."
    # SOURCE R03 L1613
    narrator "로만 씨와 처음으로 서운했던 일을 직접 이야기했다."
    # SOURCE R03 L1615
    narrator "그동안 서로를 배려한다고 생각했던 행동이, 상대에게는 다른 의미로 전달될 수도 있다는 걸 알게 됐다."
    # SOURCE R03 L1617
    narrator "이상한 기분이다."
    # SOURCE R03 L1619
    narrator "분명 조금 불편한 대화였는데."
    # SOURCE R03 L1621
    narrator "끝나고 나니 오히려 마음이 편해졌다."
    # SOURCE R03 L1624 (주인공 · 혼잣말)
    mc "……말하길 잘했네."
    # SOURCE R03 L1628
    narrator "나는 책상에 놓인 책을 펼쳤다."
    # SOURCE R03 L1630
    narrator "로만 씨가 추천해 줬던 책이었다."
    # SOURCE R03 L1632
    narrator "그 사이에는 작은 파란 꽃 책갈피가 끼워져 있었다."
    # SOURCE R03 L1634
    narrator "함께 읽고 싶은 이야기가 생겼어요."
    # SOURCE R03 L1636
    narrator "예전에는 그 문장을 단순한 추천이라고 생각했다."
    # SOURCE R03 L1638
    narrator "지금은 조금 다르게 보였다."
    # SOURCE R03 L1640
    narrator "어쩌면 로만 씨가 함께 나누고 싶었던 것은 책 속 이야기만은 아니었을지도 모른다."
    # CONTI SOURCE R03 L1642 [SFX] 휴대전화 진동
    # CONTI SOURCE R03 L1644 [UI] 로만 개인 메시지
    $ story_chat(True, title="로만")
    # SOURCE R03 L1647 (로만)
    roman "앗,,, 오늘 집에는 잘 들어가셨어요?"
    # SOURCE R03 L1650 (주인공 · 메시지)
    mc "네. 로만 씨도 잘 들어가셨어요?"
    # SOURCE R03 L1653 (로만)
    roman "네……!"
    # SOURCE R03 L1655 (로만)
    roman "오늘 이야기 들어주셔서 고마웠어요."
    # SOURCE R03 L1658 (주인공 · 메시지)
    mc "저도 이야기해 주셔서 감사해요."
    # SOURCE R03 L1661 (로만)
    roman "……후후."
    # SOURCE R03 L1663 (로만)
    roman "사실 조금 무서웠는데……."
    # SOURCE R03 L1665 (로만)
    roman "말하고 나니까 마음이 편해졌어요."
    # SOURCE R03 L1667 [CONDITION] `roman_r03_conflict_resolved == True`
    if roman_r03_conflict_resolved == True:
        # SOURCE R03 L1670 (주인공 · 메시지)
        mc "앞으로도 하고 싶은 이야기가 있으면 편하게 말씀해 주세요."
        # SOURCE R03 L1673 (로만)
        roman "네."
        # SOURCE R03 L1675 (로만)
        roman "서로 바쁠 때도 있겠지만, 그럴 때는 직접 이야기해요."
        # SOURCE R03 L1678 (주인공 · 메시지)
        mc "좋아요."
        # SOURCE R03 L1681 (로만)
        roman "……후후. 약속이에요."
    # SOURCE R03 L1683 [ELSE]
    else:
        # SOURCE R03 L1686 (로만)
        roman "다음에는 조금 더 오래 같이 있고 싶어요."
        # SOURCE R03 L1689 (주인공 · 메시지)
        mc "저도요."
        # SOURCE R03 L1692 (로만)
        roman "……네."
        # SOURCE R03 L1694 (로만)
        roman "그럼 다음에도 기다리고 있을게요."
        # SOURCE R03 L1698
        narrator "다정한 메시지였다."
        # SOURCE R03 L1700
        narrator "그런데 우리가 오늘 한 약속이 정확히 무엇이었는지는 아직 조금 모호했다."
    # SOURCE R03 L1705 (로만)
    roman "아, 그리고……."
    # SOURCE R03 L1707 (로만)
    roman "오늘 말씀드리지 못한 게 하나 있어요."
    # SOURCE R03 L1710 (주인공 · 메시지)
    mc "어떤 건데요?"
    # SOURCE R03 L1713 (로만)
    roman "제가 낭독회에 제출한 원고요."
    # SOURCE R03 L1715 (로만)
    roman "원래 쓰던 이야기랑 조금 달라졌거든요."
    # SOURCE R03 L1718 (주인공 · 메시지)
    mc "어떤 부분이 달라졌어요?"
    # SOURCE R03 L1721 (로만)
    roman "음……."
    # SOURCE R03 L1723 (로만)
    roman "처음에는 누군가를 기다리는 사람에 관한 이야기였는데요."
    # SOURCE R03 L1725 (로만)
    roman "지금은 기다리는 동안 그 사람이 어떤 선택을 하는지가 더 중요해졌어요."
    # SOURCE R03 L1729
    narrator "기다림과 선택."
    # SOURCE R03 L1731
    narrator "로만 씨가 예전부터 좋아하던 소재였다."
    # SOURCE R03 L1734 (주인공 · 메시지)
    mc "로만 씨가 쓰고 싶은 방향으로 바뀐 건가요?"
    # SOURCE R03 L1737 (로만)
    roman "……네."
    # SOURCE R03 L1739 (로만)
    roman "이번에는 제가 직접 그렇게 써보고 싶었어요."
    # SOURCE R03 L1742 (주인공 · 메시지)
    mc "그럼 좋네요. 나중에 읽어보고 싶어요."
    # SOURCE R03 L1745 (로만)
    roman "앗,,, 그런데……."
    # SOURCE R03 L1747 (로만)
    roman "이번 원고는 조금 더 개인적인 이야기라서요."
    # SOURCE R03 L1749 (로만)
    roman "아직은 전부 보여드리기 어려울 것 같아요."
    # SOURCE R03 L1752 (주인공 · 메시지)
    mc "괜찮아요. 보여주고 싶으실 때 말씀해 주세요."
    # SOURCE R03 L1755 (로만)
    roman "……후후."
    # SOURCE R03 L1757 (로만)
    roman "고마워요."
    # CONTI SOURCE R03 L1759 [UI] 잠시 후 추가 메시지
    # SOURCE R03 L1762 (로만)
    roman "그런데 [player_name] 씨."
    # SOURCE R03 L1765 (주인공 · 메시지)
    mc "네?"
    # SOURCE R03 L1768 (로만)
    roman "제가 쓴 글을 읽고……."
    # SOURCE R03 L1770 (로만)
    roman "생각하셨던 것과 다르다고 느끼셔도 괜찮을까요?"
    # SOURCE R03 L1774
    narrator "무슨 뜻일까."
    # SOURCE R03 L1776
    narrator "글의 내용이 예상과 다르다는 건가?"
    # SOURCE R03 L1778
    narrator "아니면 로만 씨의 생각이 내가 알고 있던 모습과 다르다는 뜻일까."
    # SOURCE R03 L1780 [CHOICE 02 · 로만의 글과 선택]
    menu:
        # SOURCE R03 L1782 선택지
        "로만 씨가 쓰고 싶은 이야기라면 존중하고 싶어요.":
            # SOURCE R03 L1785 (주인공 · 메시지)
            mc "제가 예상했던 내용과 달라도 괜찮아요."
            # SOURCE R03 L1787 (주인공 · 메시지)
            mc "로만 씨가 어떤 이야기를 쓰고 싶으셨는지 듣고 싶어요."
            # SOURCE R03 L1790 (로만)
            roman "……."
            # SOURCE R03 L1792 (로만)
            roman "네."
            # SOURCE R03 L1794 (로만)
            roman "그럼 저도 조금 더 솔직하게 써볼게요."
            # SOURCE R03 L1796 [FLAG] `roman_creative_autonomy += 2`
            $ story_apply("roman_r03_choice02_a", counters={'roman_creative_autonomy': 2})
        # SOURCE R03 L1798 선택지
        "읽어보면 제 생각도 솔직하게 말씀드릴게요.":
            # SOURCE R03 L1801 (주인공 · 메시지)
            mc "그때 읽어보고 제 생각도 솔직하게 말씀드릴게요."
            # SOURCE R03 L1804 (로만)
            roman "후후……."
            # SOURCE R03 L1806 (로만)
            roman "네. 저는 그런 이야기가 좋아요."
            # SOURCE R03 L1808 [FLAG] `roman_mutual_understanding += 1`
            $ story_apply("roman_r03_choice02_b", counters={'roman_mutual_understanding': 1})
        # SOURCE R03 L1810 선택지
        "로만 씨가 쓰신 글이라면 뭐든 좋아할 것 같아요.":
            # SOURCE R03 L1813 (주인공 · 메시지)
            mc "로만 씨가 쓰신 글이라면 어떤 내용이든 좋아할 것 같아요."
            # SOURCE R03 L1816 (로만)
            roman "……정말요?"
            # SOURCE R03 L1819 (주인공 · 메시지)
            mc "네."
            # SOURCE R03 L1822 (로만)
            roman "……후후."
            # SOURCE R03 L1824 (로만)
            roman "그렇게 말씀해 주시니까 기뻐요."
            # SOURCE R03 L1828
            narrator "로만 씨가 기뻐하는 건 좋았다."
            # SOURCE R03 L1830
            narrator "하지만 아직 읽지도 않은 글을 무조건 좋아한다고 말하는 게 정말 도움이 될까."
            # SOURCE R03 L1832
            narrator "나는 잠시 생각했지만, 더 이야기를 이어가지는 않았다."
            # SOURCE R03 L1834 [FLAG] `roman_approval_dependency += 1`
            $ story_apply("roman_r03_choice02_c", counters={'roman_approval_dependency': 1})
    # SOURCE R03 L1839 (로만)
    roman "오늘은 정말 고마웠어요."
    # SOURCE R03 L1841 (로만)
    roman "다음에는 조금 더 긴 이야기를 들려드릴게요."
    # SOURCE R03 L1844 (주인공 · 메시지)
    mc "네. 기대할게요. 좋은 밤 보내세요."
    # SOURCE R03 L1847 (로만)
    roman "……후후."
    # SOURCE R03 L1849 (로만)
    roman "좋은 밤 보내세요……!"
    # CONTI SOURCE R03 L1851 [UI] 스마트폰 화면 종료
    $ story_chat(False)
    # SOURCE R03 L1855
    narrator "나는 휴대전화를 내려놓았다."
    # SOURCE R03 L1857
    narrator "처음에는 로만 씨가 어떤 사람인지 알고 싶었다."
    # SOURCE R03 L1859
    narrator "이제는 그 사람이 무슨 생각을 하는지, 어떤 이야기를 쓰는지까지 궁금해졌다."
    # SOURCE R03 L1861
    narrator "그런데 가까워진다는 건 좋은 모습만 알아가는 일은 아닌 것 같다."
    # SOURCE R03 L1863
    narrator "서운한 마음도 듣고."
    # SOURCE R03 L1865
    narrator "내가 잘못 이해한 부분도 인정하고."
    # SOURCE R03 L1867
    narrator "생각이 다를 때는 그 차이까지 받아들여야 한다."
    # SOURCE R03 L1869
    narrator "……그래도."
    # SOURCE R03 L1871
    narrator "나는 로만 씨를 더 알고 싶다."
    # CONTI SOURCE R03 L1873 [TRANSITION] 같은 밤 · 로만의 방
    # CONTI SOURCE R03 L1875 [POV] 로만
    $ phone_perspective_set("roman")
    # SOURCE R03 L1877 [BG] 로만의 책상 · 스탠드 조명
    $ story_draft_scene("로만의 책상 · 스탠드 조명")
    # SOURCE R03 L1879 [BGM] Quiet Piano
    $ story_draft_bgm("Quiet Piano")
    # SOURCE R03 L1883
    narrator "로만은 낭독회 원고가 담긴 노트를 펼쳤다."
    # SOURCE R03 L1885
    narrator "원고는 이미 제출했다."
    # SOURCE R03 L1887
    narrator "하지만 별도로 쓰고 있던 더 긴 소설은 아직 끝나지 않았다."
    # SOURCE R03 L1889
    narrator "책상 한편에는 수정한 문장들이 적힌 종이가 쌓여 있었다."
    # SOURCE R03 L1891
    narrator "로만은 마지막 페이지를 펼쳤다."
    # SOURCE R03 L1893
    narrator "그곳에는 두 가지 결말이 적혀 있었다."
    # SOURCE R03 L1895
    narrator "하나는 기다리던 사람이 결국 혼자 걸어가는 이야기."
    # SOURCE R03 L1897
    narrator "다른 하나는 누군가가 돌아오기를 기다리며 자신의 하루를 멈추는 이야기."
    # SOURCE R03 L1899
    narrator "로만은 두 번째 결말을 오래 바라봤다."
    # SOURCE R03 L1902 (로만 · 혼잣말)
    roman "……이건 아닌 것 같아요."
    # SOURCE R03 L1906
    narrator "그녀는 펜을 들었다."
    # SOURCE R03 L1908
    narrator "그리고 마지막 문장 아래에 새로운 문장을 적었다."
    # SOURCE R03 L1910
    narrator "누군가를 기다리는 동안에도, 나는 나의 이야기를 계속 써야 한다."
    # SOURCE R03 L1912
    narrator "로만은 잠시 웃었다."
    # SOURCE R03 L1914
    narrator "그러다가 옆에 놓인 휴대전화를 바라봤다."
    # SOURCE R03 L1916
    narrator "오늘 나눴던 대화가 떠올랐다."
    # SOURCE R03 L1919 (로만 · 혼잣말)
    roman "……좋아해도 되는 걸까요."
    # SOURCE R03 L1923
    narrator "작은 목소리였다."
    # SOURCE R03 L1925
    narrator "아직 누구에게도 전하지 못한 마음이었다."
    # SOURCE R03 L1927
    narrator "로만은 노트를 덮었다."
    # SOURCE R03 L1929
    narrator "이번에는 그 마음을 지우지는 않았다."
    # CONTI SOURCE R03 L1931 [FADE TO BLACK]
    # CONTI SOURCE R03 L1933 [TEXT] ROMAN ROUTE · R03 COMPLETE
    # CONTI SOURCE R03 L1935 [TEXT] 「말하지 않아도 알 거라고 생각했어요」
    # CONTI SOURCE R03 L1937 [NEXT] NEXT · R04 「지우지 못한 문장」
    # SOURCE R03 L1939 [FLAG] `roman_r03_complete = True`
    $ story_flag("roman_r03_complete", True)
    # SOURCE R03 L1941 [FLAG] `roman_manuscript_submitted = True`
    $ story_flag("roman_manuscript_submitted", True)
    # CONTI SOURCE R03 L1943 [NEXT] ROMAN ROUTE R04
    # CONTI SOURCE R03 L1945 [CHAPTER R03 END]
    jump roman_r04
