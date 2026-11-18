# Roman R02 · dialogue-only storyboard import
# SOURCE: design_docs/story_sources/roman_r02.txt
# SHA256: 696624f925095f73c43502037e3d27978ac43f46d44dca439d1fac7d7681796f
# Rebuild: tools/import_roman_first.py --write
# CONTI markers intentionally do not load standing, SD, or LD artwork.

default roman_r02_lunch_complete = False
default roman_r02_puppy_event = False
default roman_r02_darim_reunion = False
default roman_reading_application_submitted = False
default roman_r02_practice_started = False
default roman_next_date_promise = False
default roman_reassurance = 0
default roman_unrealistic_promise = 0
default roman_r02_complete = False
default roman_reading_deadline_known = False

label roman_r02:
    $ phone_timeline_enter("R02", "roman_r02")
    $ roman_begin_episode("R02", "조금씩, 가까워지는 거리")
    jump roman_r02_sc01

label roman_r02_sc01:
    $ phone_timeline_enter("R02", "roman_r02_sc01")
    # SOURCE R02 L25 # R02 SC01 · 오늘은 제가 정했어요
    # SOURCE R02 L27 [BG] 캠퍼스 강의동 복도 · 오전
    $ story_draft_scene("캠퍼스 강의동 복도 · 오전")
    # SOURCE R02 L29 [BGM] Ordinary Campus
    $ story_draft_bgm("Ordinary Campus")
    # CONTI SOURCE R02 L31 [FADE IN]
    # SOURCE R02 L35
    narrator "마지막 강의가 끝났다."
    # SOURCE R02 L37
    narrator "교수님이 다음 주 과제 이야기를 시작하셨을 때는 오늘 점심 약속을 놓치는 줄 알았다."
    # SOURCE R02 L39
    narrator "다행히 강의는 제시간에 끝났다."
    # SOURCE R02 L41
    narrator "나는 가방을 정리하며 휴대전화를 확인했다."
    # CONTI SOURCE R02 L43 [UI] 로만 개인 메시지
    $ story_chat(True, title="로만")
    # SOURCE R02 L46 (로만)
    roman "앗,,, 오늘 점심 약속 기억하고 계시죠……?"
    # SOURCE R02 L49 (주인공 · 메시지)
    mc "네. 기억하고 있어요. 어디로 가면 될까요?"
    # SOURCE R02 L52 (로만)
    roman "후후……."
    # SOURCE R02 L54 (로만)
    roman "오늘은 제가 정해도 된다고 하셨잖아요."
    # SOURCE R02 L57 (주인공 · 메시지)
    mc "네. 그래서 기다리고 있었어요."
    # SOURCE R02 L60 (로만)
    roman "그럼 학교 정문에서 만나요……!"
    # SOURCE R02 L62 (로만)
    roman "식당은 도착하면 알려드릴게요."
    # SOURCE R02 L66
    narrator "……비밀인가."
    # SOURCE R02 L68
    narrator "R01에서 로만 씨는 다음 식사 장소를 직접 고르겠다고 했었다."
    # SOURCE R02 L70
    narrator "그때는 작은 약속이라고 생각했는데."
    # SOURCE R02 L72
    narrator "오늘 아침부터 어떤 곳일지 은근히 신경 쓰였다."
    # CONTI SOURCE R02 L74 [TRANSITION] 오전 11:35 · 학교 정문
    $ phone_timeline_cue("R02", "R02_L74")
    $ story_chat(False)
    # SOURCE R02 L76 [BG] 캠퍼스 정문 · 맑은 낮
    $ story_draft_scene("캠퍼스 정문 · 맑은 낮")
    # CONTI SOURCE R02 L78 [LD] 로만 · 기본 미소
    # SOURCE R02 L82
    narrator "정문 근처에 도착하자 로만 씨가 보였다."
    # SOURCE R02 L84
    narrator "평소처럼 조용히 서 있었지만, 나를 발견하자 먼저 손을 흔들었다."
    # SOURCE R02 L87 (로만)
    roman "앗,,, 여기예요!"
    # SOURCE R02 L90 (주인공)
    mc "안녕하세요, 로만 씨."
    # SOURCE R02 L93 (로만)
    roman "안녕하세요……!"
    # SOURCE R02 L95 (로만)
    roman "오늘은 늦지 않으셨네요."
    # SOURCE R02 L98 (주인공)
    mc "제가 전에 늦은 적이 있었나요?"
    # SOURCE R02 L101 (로만)
    roman "아뇨……."
    # SOURCE R02 L103 (로만)
    roman "그냥 한번 말해보고 싶었어요."
    # SOURCE R02 L106 (주인공)
    mc "……저 놀리시는 거예요?"
    # SOURCE R02 L109 (로만)
    roman "후후……."
    # SOURCE R02 L111 (로만)
    roman "조금요."
    # SOURCE R02 L115
    narrator "로만 씨가 웃었다."
    # SOURCE R02 L117
    narrator "예전 같으면 이런 말은 먼저 하지 않았을 텐데."
    # SOURCE R02 L119
    narrator "나를 놀리는 게 점점 재미있어지는 모양이다."
    # SOURCE R02 L122 (주인공)
    mc "그래서 오늘은 어디로 가나요?"
    # SOURCE R02 L125 (로만)
    roman "음……."
    # SOURCE R02 L127 (로만)
    roman "조금만 더 걸어가면 돼요."
    # SOURCE R02 L130 (주인공)
    mc "아직도 비밀인가요?"
    # SOURCE R02 L133 (로만)
    roman "네."
    # SOURCE R02 L135 (로만)
    roman "오늘은 제가 안내할게요."
    # SOURCE R02 L139
    narrator "로만 씨는 한 발 먼저 걸었다."
    # SOURCE R02 L141
    narrator "나는 그 옆으로 나란히 걸었다."
    # SOURCE R02 L143
    narrator "평소와 별 차이 없는 학교 앞 거리였다."
    # SOURCE R02 L145
    narrator "그런데 오늘은 길 자체보다도 누군가와 함께 걷고 있다는 사실이 더 신경 쓰였다."
    # SOURCE R02 L148 (로만)
    roman "혹시 음식 못 드시는 건 없으시죠?"
    # SOURCE R02 L151 (주인공)
    mc "네. 대부분 잘 먹어요."
    # SOURCE R02 L154 (로만)
    roman "다행이에요……."
    # SOURCE R02 L156 (로만)
    roman "혹시 싫어하시면 어떡하나 조금 걱정했거든요."
    # SOURCE R02 L159 (주인공)
    mc "로만 씨가 고르신 곳이면 궁금한데요."
    # SOURCE R02 L162 (로만)
    roman "……."
    # SOURCE R02 L165 (로만)
    roman "그, 그런 기대는 조금 부담스러운데요……!"
    # SOURCE R02 L168 (주인공)
    mc "그럼 기대를 조금만 할게요."
    # SOURCE R02 L171 (로만)
    roman "앗,,, 그건 또 아쉬워요."
    # SOURCE R02 L175
    narrator "……어느 쪽에 맞춰야 하지?"
    # SOURCE R02 L177
    narrator "로만 씨는 내 표정을 보더니 웃음을 터뜨렸다."
    # SOURCE R02 L180 (로만)
    roman "후후…… 농담이에요."
    # SOURCE R02 L184
    narrator "생각보다 장난기가 있다."
    # SOURCE R02 L186
    narrator "그리고 그게 싫지 않았다."
    # CONTI SOURCE R02 L188 [SCENE 01 END]
    jump roman_r02_sc02

label roman_r02_sc02:
    $ phone_timeline_enter("R02", "roman_r02_sc02")
    # SOURCE R02 L191 # R02 SC02 · 로만 씨에게 이런 면이?
    # SOURCE R02 L193 [BG] 학교 앞 작은 파스타 식당 · 점심
    $ story_draft_scene("학교 앞 작은 파스타 식당 · 점심")
    # SOURCE R02 L195 [BGM] Cozy Lunch
    $ story_draft_bgm("Cozy Lunch")
    # SOURCE R02 L199
    narrator "로만 씨가 안내한 곳은 학교에서 조금 떨어진 작은 식당이었다."
    # SOURCE R02 L201
    narrator "창가에는 화분이 놓여 있었고, 벽에는 손글씨로 적힌 메뉴가 걸려 있었다."
    # SOURCE R02 L204 (로만)
    roman "여기예요……!"
    # SOURCE R02 L207 (주인공)
    mc "분위기가 좋네요."
    # SOURCE R02 L210 (로만)
    roman "후후…… 다행이에요."
    # SOURCE R02 L212 (로만)
    roman "전에 친구랑 왔었는데 맛있었거든요."
    # SOURCE R02 L215 (주인공)
    mc "그럼 로만 씨 추천 메뉴가 있나요?"
    # SOURCE R02 L218 (로만)
    roman "네!"
    # SOURCE R02 L222
    narrator "로만 씨는 바로 메뉴판을 펼쳤다."
    # SOURCE R02 L224
    narrator "그리고 조금 의외일 만큼 진지한 표정으로 음식 설명을 시작했다."
    # SOURCE R02 L227 (로만)
    roman "여기 토마토 파스타도 맛있고요."
    # SOURCE R02 L229 (로만)
    roman "크림 파스타도 괜찮아요."
    # SOURCE R02 L231 (로만)
    roman "그리고 버섯 리소토도 맛있는데……."
    # SOURCE R02 L234 (주인공)
    mc "전부 맛있나 봐요."
    # SOURCE R02 L237 (로만)
    roman "앗,,, 네……."
    # SOURCE R02 L240 (로만)
    roman "그러네요."
    # SOURCE R02 L244
    narrator "로만 씨는 메뉴판을 다시 내려다봤다."
    # SOURCE R02 L247 (로만)
    roman "……어떡하죠?"
    # SOURCE R02 L250 (주인공)
    mc "뭐가요?"
    # SOURCE R02 L253 (로만)
    roman "추천하려고 데려왔는데 제가 더 고민하고 있어요."
    # SOURCE R02 L256 (주인공)
    mc "그럼 두 가지 시켜서 나눠 먹을까요?"
    # SOURCE R02 L259 (로만)
    roman "……!"
    # SOURCE R02 L262 (로만)
    roman "그거 좋은 생각이에요."
    # SOURCE R02 L266
    narrator "우리는 서로 다른 메뉴를 주문했다."
    # SOURCE R02 L268
    narrator "잠시 뒤 음식이 나왔다."
    # SOURCE R02 L271 (로만)
    roman "앗,,, 맛있겠다……."
    # SOURCE R02 L275
    narrator "로만 씨의 눈이 조금 반짝였다."
    # SOURCE R02 L277
    narrator "책 이야기할 때와 비슷한 표정이었다."
    # SOURCE R02 L280 (주인공)
    mc "많이 좋아하시는 것 같아요."
    # SOURCE R02 L283 (로만)
    roman "네……!"
    # SOURCE R02 L285 (로만)
    roman "저 여기 파스타 좋아하거든요."
    # SOURCE R02 L288 (주인공)
    mc "책이랑 강아지만 좋아하시는 줄 알았는데요."
    # SOURCE R02 L291 (로만)
    roman "앗,,, 제가 그렇게 보였어요?"
    # SOURCE R02 L294 (주인공)
    mc "그런 건 아니지만요."
    # SOURCE R02 L297 (로만)
    roman "후후……."
    # SOURCE R02 L299 (로만)
    roman "그럼 오늘은 하나 더 알아가셨네요."
    # SOURCE R02 L303
    narrator "그 말이 은근히 마음에 들었다."
    # SOURCE R02 L305
    narrator "로만 씨에 대해 하나 더 알게 됐다는 것."
    # SOURCE R02 L307
    narrator "그런 걸 세고 있었던 건 아닌데, 오늘은 조금 특별하게 느껴졌다."
    # CONTI SOURCE R02 L309 [시간 경과 · 오후 12:15]
    $ phone_timeline_cue("R02", "R02_L309")
    # SOURCE R02 L312 (로만)
    roman "아, 맞다."
    # SOURCE R02 L315 (주인공)
    mc "네?"
    # SOURCE R02 L318 (로만)
    roman "저번에 추천해드린 책은 읽어보셨어요?"
    # SOURCE R02 L321 (주인공)
    mc "아직 다 읽지는 못했어요."
    # SOURCE R02 L324 (로만)
    roman "앗,,, 그러셨군요."
    # SOURCE R02 L327 (주인공)
    mc "그런데 초반은 재미있었어요."
    # SOURCE R02 L330 (로만)
    roman "정말요?"
    # SOURCE R02 L333 (주인공)
    mc "네. 등장인물들이 생각보다 서로 다르더라고요."
    # SOURCE R02 L336 (로만)
    roman "후후. 그 부분이 좋아요."
    # SOURCE R02 L339 (주인공)
    mc "로만 씨는 성격이 다른 사람들이 가까워지는 이야기를 좋아하시나 봐요."
    # SOURCE R02 L342 (로만)
    roman "음……."
    # SOURCE R02 L345 (로만)
    roman "꼭 그런 건 아닌데요."
    # SOURCE R02 L347 (로만)
    roman "사람들이 처음부터 서로를 다 이해할 수는 없잖아요."
    # SOURCE R02 L350 (주인공)
    mc "그렇죠."
    # SOURCE R02 L353 (로만)
    roman "그래서 조금씩 알아가는 이야기가 좋아요."
    # SOURCE R02 L355 (로만)
    roman "처음에는 몰랐던 면을 발견하기도 하고……."
    # SOURCE R02 L358 (로만)
    roman "같은 사람인데도 다르게 보일 때가 있잖아요."
    # SOURCE R02 L362
    narrator "로만 씨는 그렇게 말한 뒤 식탁 위의 컵을 바라봤다."
    # SOURCE R02 L365 (주인공)
    mc "지금도 그런가요?"
    # SOURCE R02 L368 (로만)
    roman "……네?"
    # SOURCE R02 L371 (주인공)
    mc "제가 처음 만났을 때랑은 좀 다르게 보이나 해서요."
    # SOURCE R02 L374 (로만)
    roman "……."
    # CONTI SOURCE R02 L376 [LD] 로만 · 당황
    # SOURCE R02 L379 (로만)
    roman "앗,,, 그건……."
    # SOURCE R02 L382 (주인공)
    mc "어려운 질문이었나요?"
    # SOURCE R02 L385 (로만)
    roman "조금요……!"
    # SOURCE R02 L389
    narrator "로만 씨는 잠시 고민했다."
    # SOURCE R02 L391
    narrator "그러다가 조심스럽게 말했다."
    # SOURCE R02 L394 (로만)
    roman "처음에는……."
    # SOURCE R02 L396 (로만)
    roman "말을 걸어주셔서 고마운 분이라고 생각했어요."
    # SOURCE R02 L399 (주인공)
    mc "지금은요?"
    # SOURCE R02 L402 (로만)
    roman "……."
    # SOURCE R02 L405 (로만)
    roman "지금은……."
    # SOURCE R02 L407 (로만)
    roman "제가 먼저 말을 걸고 싶은 분이에요."
    # SOURCE R02 L411
    narrator "……."
    # SOURCE R02 L413
    narrator "이상하다."
    # SOURCE R02 L415
    narrator "분명 별로 어려운 문장은 아닌데."
    # SOURCE R02 L417
    narrator "듣고 나니 무슨 말을 해야 할지 잠깐 고민하게 됐다."
    # SOURCE R02 L420 (주인공)
    mc "저도 로만 씨랑 이야기하는 게 좋아요."
    # SOURCE R02 L423 (로만)
    roman "……후후."
    # SOURCE R02 L426 (로만)
    roman "그럼 다행이에요."
    # CONTI SOURCE R02 L428 [시간 경과 · 오후 12:40]
    $ phone_timeline_cue("R02", "R02_L428")
    # SOURCE R02 L432
    narrator "식사를 마치고 계산을 끝냈다."
    # SOURCE R02 L434
    narrator "밖으로 나오자 오후 햇살이 따뜻했다."
    # SOURCE R02 L437 (로만)
    roman "오늘 식당은 어떠셨어요?"
    # SOURCE R02 L440 (주인공)
    mc "정말 좋았어요."
    # SOURCE R02 L443 (로만)
    roman "……다행이다."
    # SOURCE R02 L446 (주인공)
    mc "다음에는 제가 좋은 곳을 찾아볼게요."
    # SOURCE R02 L449 (로만)
    roman "앗,,, 그러면 기대해도 되는 건가요?"
    # SOURCE R02 L452 (주인공)
    mc "네. 많이 기대하셔도 돼요."
    # SOURCE R02 L455 (로만)
    roman "후후……."
    # SOURCE R02 L457 (로만)
    roman "그럼 저도 일부러 조금 놀려드릴게요."
    # SOURCE R02 L460 (주인공)
    mc "벌써부터 예고하시는 거예요?"
    # SOURCE R02 L463 (로만)
    roman "네."
    # SOURCE R02 L465 (로만)
    roman "오늘은 제가 이겼으니까요."
    # SOURCE R02 L469
    narrator "……승부였어, 이거?"
    # SOURCE R02 L471
    narrator "로만 씨는 웃으며 앞서 걸었다."
    # SOURCE R02 L473
    narrator "나는 그 뒤를 따라갔다."
    # SOURCE R02 L475
    narrator "오늘은 책이 아니라 새로운 표정을 하나 더 발견한 것 같았다."
    # SOURCE R02 L477 [FLAG] `roman_r02_lunch_complete = True`
    $ story_flag("roman_r02_lunch_complete", True)
    # CONTI SOURCE R02 L479 [SCENE 02 END]
    jump roman_r02_sc03

label roman_r02_sc03:
    $ phone_timeline_enter("R02", "roman_r02_sc03")
    # SOURCE R02 L482 # R02 SC03 · 강아지는 반칙이에요
    # SOURCE R02 L484 [BG] 캠퍼스 근처 산책로 · 오후
    $ story_draft_scene("캠퍼스 근처 산책로 · 오후")
    # SOURCE R02 L486 [BGM] Light Walk
    $ story_draft_bgm("Light Walk")
    # SOURCE R02 L490
    narrator "점심을 먹은 뒤 우리는 학교로 돌아가는 대신 근처 산책로를 조금 걷기로 했다."
    # SOURCE R02 L492
    narrator "로만 씨는 평소보다 말을 많이 했다."
    # SOURCE R02 L494
    narrator "최근에 읽은 책 이야기."
    # SOURCE R02 L496
    narrator "영문학 수업에서 발표했던 작품 이야기."
    # SOURCE R02 L498
    narrator "그리고 다음에 보고 싶은 영화 이야기까지."
    # SOURCE R02 L500
    narrator "그렇게 걷고 있을 때였다."
    # CONTI SOURCE R02 L502 [SFX] 강아지 짖는 소리
    # SOURCE R02 L505 (로만)
    roman "……!"
    # SOURCE R02 L508 (주인공)
    mc "왜 그러세요?"
    # SOURCE R02 L511 (로만)
    roman "저기……!"
    # SOURCE R02 L515
    narrator "로만 씨가 가리킨 곳에는 작은 강아지 한 마리가 있었다."
    # SOURCE R02 L517
    narrator "보호자와 함께 산책하던 강아지는 길가에 멈춰 서서 꼬리를 흔들고 있었다."
    # SOURCE R02 L520 (로만)
    roman "앗,,, 너무 귀여워요……!"
    # SOURCE R02 L523 (주인공)
    mc "강아지 정말 좋아하시네요."
    # SOURCE R02 L526 (로만)
    roman "네……!"
    # SOURCE R02 L528 (로만)
    roman "저렇게 꼬리 흔드는 거 보면 너무 좋아요."
    # SOURCE R02 L532
    narrator "로만 씨의 목소리가 조금 높아졌다."
    # SOURCE R02 L534
    narrator "아까 서점에서 책을 설명하던 때와 또 달랐다."
    # SOURCE R02 L537 (로만)
    roman "……아."
    # SOURCE R02 L540 (주인공)
    mc "네?"
    # SOURCE R02 L543 (로만)
    roman "저 너무 티 냈나요……?"
    # SOURCE R02 L546 (주인공)
    mc "아니요. 좋아하시는 게 잘 보여서요."
    # SOURCE R02 L549 (로만)
    roman "앗,,, 부끄러워요……."
    # SOURCE R02 L553
    narrator "강아지가 우리 쪽을 바라봤다."
    # SOURCE R02 L555
    narrator "로만 씨는 그 자리에 멈춰 섰다."
    # SOURCE R02 L558 (로만)
    roman "……."
    # SOURCE R02 L561 (주인공)
    mc "혹시 가까이 가보고 싶으세요?"
    # SOURCE R02 L564 (로만)
    roman "……조금요."
    # SOURCE R02 L567 (주인공)
    mc "그럼 보호자분께 먼저 여쭤볼까요?"
    # SOURCE R02 L570 (로만)
    roman "네……!"
    # SOURCE R02 L572 [BG] 산책로 · 강아지 근처
    $ story_draft_scene("산책로 · 강아지 근처")
    # SOURCE R02 L575 (주인공)
    mc "안녕하세요. 혹시 강아지 잠깐 쓰다듬어 봐도 괜찮을까요?"
    # SOURCE R02 L578 (보호자)
    narrator "보호자: 네, 괜찮아요. 천천히 손 내밀어 주세요."
    # SOURCE R02 L581 (로만)
    roman "앗,,, 감사합니다……!"
    # SOURCE R02 L585
    narrator "로만 씨는 조심스럽게 손을 내밀었다."
    # SOURCE R02 L587
    narrator "강아지가 냄새를 맡더니 가까이 다가왔다."
    # SOURCE R02 L590 (로만)
    roman "……!"
    # SOURCE R02 L592 (로만)
    roman "안녕……?"
    # SOURCE R02 L596
    narrator "로만 씨의 얼굴에 웃음이 번졌다."
    # SOURCE R02 L599 (로만)
    roman "너무 귀여워……."
    # CONTI SOURCE R02 L601 [SD EVENT] `roman_r02_puppy_encounter`
    # CONTI SOURCE R02 L603 [연출] 작은 강아지 앞에 쪼그려 앉은 로만이 환하게 웃는 SD 이벤트 일러스트 1장. 주인공은 화면 밖에 있으며, 강아지 보호자는 그리지 않거나 화면 가장자리만 표시.
    # SOURCE R02 L606 (보호자)
    narrator "보호자: 강아지 좋아하시나 봐요."
    # SOURCE R02 L609 (로만)
    roman "앗,,, 네……!"
    # SOURCE R02 L612 (보호자)
    narrator "보호자: 평소에도 사람을 잘 따르는 편이에요."
    # SOURCE R02 L615 (로만)
    roman "정말 착하네요……."
    # SOURCE R02 L619
    narrator "로만 씨는 강아지의 머리를 조심스럽게 쓰다듬었다."
    # SOURCE R02 L621
    narrator "평소에는 다른 사람에게 먼저 다가가는 것도 조금 망설이는데."
    # SOURCE R02 L623
    narrator "강아지 앞에서는 고민하는 시간이 거의 없었다."
    # SOURCE R02 L626 (주인공)
    mc "로만 씨, 정말 행복해 보이세요."
    # SOURCE R02 L629 (로만)
    roman "……네?"
    # SOURCE R02 L632 (주인공)
    mc "표정이요."
    # SOURCE R02 L635 (로만)
    roman "앗,,, 그, 그런가요?"
    # SOURCE R02 L639
    narrator "로만 씨는 부끄러운 듯 웃었다."
    # SOURCE R02 L641
    narrator "그때 강아지가 로만 씨의 손등을 살짝 핥았다."
    # SOURCE R02 L644 (로만)
    roman "앗!"
    # SOURCE R02 L646 (로만)
    roman "……후후."
    # SOURCE R02 L648 (로만)
    roman "간지러워……."
    # SOURCE R02 L652
    narrator "……아."
    # SOURCE R02 L654
    narrator "이건 조금 반칙인데."
    # SOURCE R02 L656
    narrator "이렇게 좋아하는 모습을 보고 있으면 나까지 기분이 좋아진다."
    # CONTI SOURCE R02 L658 [전환] 일반 LD
    # SOURCE R02 L661 (보호자)
    narrator "보호자: 저희는 이제 가볼게요."
    # SOURCE R02 L664 (로만)
    roman "네……! 감사합니다."
    # SOURCE R02 L667 (주인공)
    mc "좋은 하루 보내세요."
    # SOURCE R02 L671
    narrator "강아지가 멀어지는 동안 로만 씨는 몇 번이나 뒤돌아봤다."
    # SOURCE R02 L674 (로만)
    roman "……너무 귀여웠어요."
    # SOURCE R02 L677 (주인공)
    mc "그러게요."
    # SOURCE R02 L680 (로만)
    roman "나중에 또 만나면 좋겠네요……."
    # SOURCE R02 L683 (주인공)
    mc "그럼 다음에 산책하다가 또 만날 수도 있겠죠."
    # SOURCE R02 L686 (로만)
    roman "……후후."
    # SOURCE R02 L688 (로만)
    roman "그럼 다음에도 같이 산책해요."
    # SOURCE R02 L691 (주인공)
    mc "좋아요."
    # SOURCE R02 L695
    narrator "로만 씨는 잠시 나를 바라봤다."
    # SOURCE R02 L698 (로만)
    roman "그런데……."
    # SOURCE R02 L701 (주인공)
    mc "네?"
    # SOURCE R02 L704 (로만)
    roman "강아지 보느라 [player_name] 씨한테 말을 별로 못 했네요."
    # SOURCE R02 L707 (주인공)
    mc "괜찮아요. 로만 씨가 즐거워하셔서 저도 좋았어요."
    # SOURCE R02 L710 (로만)
    roman "……."
    # SOURCE R02 L713 (로만)
    roman "앗,,, 그럼……."
    # SOURCE R02 L715 (로만)
    roman "다음에는 [player_name] 씨가 좋아하시는 것도 같이 보러 가요."
    # SOURCE R02 L718 (주인공)
    mc "제가 좋아하는 거요?"
    # SOURCE R02 L721 (로만)
    roman "네."
    # SOURCE R02 L723 (로만)
    roman "저도 알고 싶어요."
    # SOURCE R02 L727
    narrator "로만 씨가 조금 장난스럽게 웃었다."
    # SOURCE R02 L730 (로만)
    roman "저만 좋아하는 거 보여드리면 불공평하잖아요."
    # SOURCE R02 L733 (주인공)
    mc "그건 그렇네요."
    # SOURCE R02 L737
    narrator "그 말이 마음에 들었다."
    # SOURCE R02 L739
    narrator "로만 씨는 자기 이야기를 보여주는 것만큼 내 이야기를 듣고 싶어 하는 사람이었다."
    # SOURCE R02 L741 [FLAG] `roman_r02_puppy_event = True`
    $ story_flag("roman_r02_puppy_event", True)
    # CONTI SOURCE R02 L743 [SCENE 03 END]
    jump roman_r02_sc04

label roman_r02_sc04:
    $ phone_timeline_enter("R02", "roman_r02_sc04")
    # SOURCE R02 L746 # R02 SC04 · 선배는 이미 알고 있었나요?
    # SOURCE R02 L748 [BG] 캠퍼스 강의동 앞 · 오후
    $ story_draft_scene("캠퍼스 강의동 앞 · 오후")
    # SOURCE R02 L750 [BGM] Campus Afternoon
    $ story_draft_bgm("Campus Afternoon")
    # SOURCE R02 L754
    narrator "산책을 마치고 학교로 돌아왔다."
    # SOURCE R02 L756
    narrator "로만 씨는 교양 수업에 들러야 한다고 했다."
    # SOURCE R02 L758
    narrator "아직 수업 시작까지는 시간이 조금 남아 있었다."
    # SOURCE R02 L761 (주인공)
    mc "여기서 수업 들으세요?"
    # SOURCE R02 L764 (로만)
    roman "네. 다림 선배랑 같이 듣는 수업이에요."
    # SOURCE R02 L767 (주인공)
    mc "아, 두 분이 같이 듣는다고 하셨었죠."
    # SOURCE R02 L770 (로만)
    roman "후후…… 네."
    # SOURCE R02 L774
    narrator "그때 강의동 입구에서 익숙한 목소리가 들렸다."
    # SOURCE R02 L777 (다림)
    darim "어머?"
    # SOURCE R02 L779 (다림)
    darim "[player_name] 씨?"
    # SOURCE R02 L782 (주인공)
    mc "다림 선배, 안녕하세요."
    # SOURCE R02 L785 (로만)
    roman "앗,,, 선배!"
    # SOURCE R02 L788 (다림)
    darim "두 분이 같이 계셨네요."
    # SOURCE R02 L791 (로만)
    roman "아…… 네."
    # SOURCE R02 L794 (다림)
    darim "후후. 오늘은 무슨 일로요?"
    # SOURCE R02 L797 (주인공)
    mc "로만 씨랑 점심 먹고 산책하고 왔어요."
    # SOURCE R02 L800 (다림)
    darim "아, 그러셨군요."
    # SOURCE R02 L804
    narrator "다림 선배는 로만 씨를 바라봤다."
    # SOURCE R02 L806
    narrator "그리고 아주 잠깐 미소를 지었다."
    # SOURCE R02 L809 (다림)
    darim "로만 씨, 오늘 식당 정하신다고 하셨죠?"
    # SOURCE R02 L812 (로만)
    roman "앗,,, 선배!"
    # SOURCE R02 L815 (주인공)
    mc "……네?"
    # SOURCE R02 L818 (다림)
    darim "아, 제가 말하면 안 되는 거였나요?"
    # SOURCE R02 L821 (로만)
    roman "그, 그런 건 아닌데……!"
    # SOURCE R02 L825
    narrator "로만 씨의 얼굴이 붉어졌다."
    # SOURCE R02 L827
    narrator "다림 선배는 조용히 웃었다."
    # SOURCE R02 L830 (다림)
    darim "후후. 사실 로만 씨가 며칠 전에 식당 추천을 물어보셨거든요."
    # SOURCE R02 L833 (주인공)
    mc "정말요?"
    # SOURCE R02 L836 (로만)
    roman "……."
    # SOURCE R02 L839 (로만)
    roman "그게……."
    # SOURCE R02 L841 (로만)
    roman "메뉴를 잘못 고르면 어쩌나 싶어서요……."
    # SOURCE R02 L844 (주인공)
    mc "오늘 정말 맛있었어요."
    # SOURCE R02 L847 (로만)
    roman "……후후."
    # SOURCE R02 L849 (로만)
    roman "다행이에요."
    # SOURCE R02 L852 (다림)
    darim "엄청 고민하셨거든요."
    # SOURCE R02 L855 (로만)
    roman "서, 선배……!"
    # SOURCE R02 L858 (다림)
    darim "알겠어요. 이제 그만할게요."
    # SOURCE R02 L862
    narrator "다림 선배의 말에 괜히 웃음이 나왔다."
    # SOURCE R02 L864
    narrator "로만 씨는 평소에 수줍어하면서도 오늘은 직접 식당을 정해 데려갔다."
    # SOURCE R02 L866
    narrator "그렇게까지 고민한 줄은 몰랐다."
    # SOURCE R02 L869 (주인공)
    mc "그렇게 고민해서 정해주신 거였군요."
    # SOURCE R02 L872 (로만)
    roman "앗,,, 별거 아니에요……."
    # SOURCE R02 L875 (주인공)
    mc "그래도 감사해요. 정말 즐거웠어요."
    # SOURCE R02 L878 (로만)
    roman "……."
    # SOURCE R02 L880 (로만)
    roman "네."
    # SOURCE R02 L884
    narrator "로만 씨는 조금 안심한 듯 웃었다."
    # CONTI SOURCE R02 L886 [시간 경과 · 오후 2:10]
    $ phone_timeline_cue("R02", "R02_L886")
    # SOURCE R02 L889 (다림)
    darim "그런데 로만 씨."
    # SOURCE R02 L892 (로만)
    roman "네?"
    # SOURCE R02 L895 (다림)
    darim "낭독 행사 신청은 어떻게 하셨어요?"
    # SOURCE R02 L898 (주인공)
    mc "아, 그 이야기 하셨었죠."
    # SOURCE R02 L901 (로만)
    roman "……."
    # SOURCE R02 L904 (로만)
    roman "아직이요."
    # SOURCE R02 L907 (다림)
    darim "마감이 이번 주였죠?"
    # SOURCE R02 L910 (로만)
    roman "네……."
    # SOURCE R02 L914
    narrator "로만 씨의 목소리가 조금 작아졌다."
    # SOURCE R02 L917 (다림)
    darim "로만 씨가 오래 준비하신 거잖아요."
    # SOURCE R02 L919 (다림)
    darim "너무 부담 갖지 않으셔도 되지만, 하고 싶은 마음이 있다면 도전해 보셔도 좋겠어요."
    # SOURCE R02 L922 (로만)
    roman "……네."
    # SOURCE R02 L925 (다림)
    darim "후후. 그럼 저 먼저 들어갈게요."
    # SOURCE R02 L927 (다림)
    darim "[player_name] 씨도 다음에 봬요."
    # SOURCE R02 L930 (주인공)
    mc "네. 선배, 수업 잘 들으세요."
    # SOURCE R02 L933 (다림)
    darim "두 분도 남은 하루 잘 보내세요."
    # SOURCE R02 L937
    narrator "다림 선배는 먼저 건물 안으로 들어갔다."
    # SOURCE R02 L939
    narrator "로만 씨는 잠시 강의동을 바라봤다."
    # SOURCE R02 L942 (주인공)
    mc "행사 신청 때문에 고민되세요?"
    # SOURCE R02 L945 (로만)
    roman "……조금요."
    # SOURCE R02 L948 (주인공)
    mc "그럼 수업 끝나고 생각해보셔도 되죠."
    # SOURCE R02 L951 (로만)
    roman "……."
    # SOURCE R02 L954 (로만)
    roman "네."
    # SOURCE R02 L957 (로만)
    roman "오늘 이야기 많이 했으니까……."
    # SOURCE R02 L959 (로만)
    roman "조금 더 고민해 볼게요."
    # SOURCE R02 L963
    narrator "나는 고개를 끄덕였다."
    # SOURCE R02 L965
    narrator "로만 씨는 강의동 입구에서 돌아섰다."
    # SOURCE R02 L968 (로만)
    roman "오늘 정말 즐거웠어요."
    # SOURCE R02 L971 (주인공)
    mc "저도요. 수업 잘 들으세요."
    # SOURCE R02 L974 (로만)
    roman "……후후. 네!"
    # SOURCE R02 L978
    narrator "그렇게 헤어졌다."
    # SOURCE R02 L980
    narrator "오늘은 평범한 점심 약속이었다."
    # SOURCE R02 L982
    narrator "그런데 로만 씨가 어떤 것을 좋아하고, 어떤 일에 용기를 내고 싶어 하는지 조금 더 알게 됐다."
    # SOURCE R02 L984
    narrator "그것만으로도 꽤 의미 있는 하루였다."
    # SOURCE R02 L986 [FLAG] `roman_r02_darim_reunion = True`
    $ story_flag("roman_r02_darim_reunion", True)
    # CONTI SOURCE R02 L988 [SCENE 04 END]
    jump roman_r02_sc05

label roman_r02_sc05:
    $ phone_timeline_enter("R02", "roman_r02_sc05")
    # SOURCE R02 L991 # R02 SC05 · 조금 특별한 부탁
    # SOURCE R02 L993 [BG] 캠퍼스 작은 정원 · 늦은 오후
    $ story_draft_scene("캠퍼스 작은 정원 · 늦은 오후")
    # SOURCE R02 L995 [BGM] Gentle Afternoon
    $ story_draft_bgm("Gentle Afternoon")
    # CONTI SOURCE R02 L997 [FADE IN]
    # SOURCE R02 L1001
    narrator "로만 씨와 점심을 먹은 지 이틀이 지났다."
    # SOURCE R02 L1003
    narrator "그날 이후에도 우리는 가끔 메시지를 주고받았다."
    # SOURCE R02 L1005
    narrator "오늘 먹은 음식 이야기."
    # SOURCE R02 L1007
    narrator "수업에서 들은 재미있는 문장 이야기."
    # SOURCE R02 L1009
    narrator "그리고 길에서 만난 강아지 이야기까지."
    # SOURCE R02 L1011
    narrator "처음에는 책 이야기가 대부분이었는데 이제는 조금 달라졌다."
    # SOURCE R02 L1013
    narrator "……무슨 일이 없어도 연락하게 됐다."
    # CONTI SOURCE R02 L1015 [SFX] 휴대전화 진동
    # CONTI SOURCE R02 L1017 [UI] 로만 개인 메시지
    $ story_chat(True, title="로만")
    # SOURCE R02 L1020 (로만)
    roman "앗,,, [player_name] 씨."
    # SOURCE R02 L1022 (로만)
    roman "혹시 오늘 잠깐 시간 괜찮으세요……?"
    # SOURCE R02 L1025 (주인공 · 메시지)
    mc "네. 오후에는 괜찮아요."
    # SOURCE R02 L1028 (로만)
    roman "그럼 정원 쪽에서 잠깐 만날 수 있을까요?"
    # SOURCE R02 L1030 (로만)
    roman "드릴 말씀이 있어요."
    # SOURCE R02 L1034
    narrator "드릴 말씀?"
    # SOURCE R02 L1036
    narrator "평소보다 조금 진지한 메시지였다."
    # SOURCE R02 L1038
    narrator "무슨 일일까."
    # CONTI SOURCE R02 L1040 [TRANSITION] 오후 4:30 · 캠퍼스 정원
    $ phone_timeline_cue("R02", "R02_L1040")
    $ story_chat(False)
    # CONTI SOURCE R02 L1042 [LD] 로만 · 기본
    # CONTI SOURCE R02 L1044 [ANIM] 느린 눈 깜빡임, 미세 호흡
    # SOURCE R02 L1048
    narrator "정원 벤치에 도착했을 때 로만 씨는 이미 앉아 있었다."
    # SOURCE R02 L1050
    narrator "무릎 위에는 익숙한 노트가 놓여 있었다."
    # SOURCE R02 L1053 (주인공)
    mc "로만 씨."
    # SOURCE R02 L1056 (로만)
    roman "앗,,, 오셨어요!"
    # SOURCE R02 L1059 (주인공)
    mc "많이 기다리셨어요?"
    # SOURCE R02 L1062 (로만)
    roman "아니에요. 저도 방금 왔어요."
    # SOURCE R02 L1066
    narrator "로만 씨는 노트 표지를 손가락으로 만지작거렸다."
    # SOURCE R02 L1069 (주인공)
    mc "무슨 일이세요?"
    # SOURCE R02 L1072 (로만)
    roman "……저."
    # SOURCE R02 L1074 (로만)
    roman "낭독 행사에 신청했어요."
    # SOURCE R02 L1077 (주인공)
    mc "정말요?"
    # SOURCE R02 L1080 (로만)
    roman "네……!"
    # SOURCE R02 L1084
    narrator "로만 씨는 휴대전화 화면을 보여줬다."
    # SOURCE R02 L1086
    narrator "교내 문학 낭독 행사 참가 신청 접수 확인 메시지였다."
    # SOURCE R02 L1089 (주인공)
    mc "축하드려요! 결국 신청하셨군요."
    # SOURCE R02 L1092 (로만)
    roman "……후후."
    # SOURCE R02 L1094 (로만)
    roman "아직 축하받을 정도는 아닌데요……."
    # SOURCE R02 L1097 (주인공)
    mc "하고 싶으셨던 일에 도전하셨잖아요."
    # SOURCE R02 L1100 (로만)
    roman "……."
    # SOURCE R02 L1103 (로만)
    roman "그렇게 말씀해 주시니까 조금 기뻐요."
    # SOURCE R02 L1107
    narrator "로만 씨는 노트를 내려다봤다."
    # SOURCE R02 L1110 (로만)
    roman "사실 신청 버튼을 누르기 전에 한참 고민했어요."
    # SOURCE R02 L1112 (로만)
    roman "아직 글이 완성된 것도 아니고……."
    # SOURCE R02 L1114 (로만)
    roman "사람들 앞에서 읽어본 적도 많지 않아서요."
    # SOURCE R02 L1117 (주인공)
    mc "그럴 수 있죠."
    # SOURCE R02 L1120 (로만)
    roman "그런데 지난번에 같이 책 이야기했던 게 생각났어요."
    # SOURCE R02 L1123 (주인공)
    mc "서점에서요?"
    # SOURCE R02 L1126 (로만)
    roman "네."
    # SOURCE R02 L1128 (로만)
    roman "같은 문장도 서로 다르게 읽을 수 있다고 했잖아요."
    # SOURCE R02 L1131 (주인공)
    mc "기억해요."
    # SOURCE R02 L1134 (로만)
    roman "그래서……."
    # SOURCE R02 L1136 (로만)
    roman "제가 쓴 글도 누군가에게는 제가 생각하지 못한 의미가 될 수 있겠다는 생각이 들었어요."
    # SOURCE R02 L1140
    narrator "로만 씨는 조용히 웃었다."
    # SOURCE R02 L1143 (로만)
    roman "그런 생각을 하니까 조금 덜 무섭더라고요."
    # SOURCE R02 L1146 (주인공)
    mc "좋은 이유네요."
    # SOURCE R02 L1149 (로만)
    roman "……후후."
    # SOURCE R02 L1152 (로만)
    roman "그래서 부탁드리고 싶은 게 있어요."
    # SOURCE R02 L1155 (주인공)
    mc "네. 말씀하세요."
    # SOURCE R02 L1158 (로만)
    roman "낭독 행사 전에 연습을 해야 하거든요."
    # SOURCE R02 L1160 (로만)
    roman "혹시……."
    # SOURCE R02 L1162 (로만)
    roman "제 연습을 들어주실 수 있을까요?"
    # SOURCE R02 L1165 (주인공)
    mc "물론이죠."
    # SOURCE R02 L1168 (로만)
    roman "……정말요?"
    # SOURCE R02 L1171 (주인공)
    mc "네. R01 때도 말씀드렸잖아요."
    # SOURCE R02 L1175
    narrator "……아차."
    # SOURCE R02 L1177
    narrator "이야기 속에서 챕터 번호 같은 걸 말할 리는 없지."
    # SOURCE R02 L1179
    narrator "나는 자연스럽게 말을 고쳤다."
    # SOURCE R02 L1182 (주인공)
    mc "전에 제가 연습 상대가 되어드릴 수 있다고 말씀드렸잖아요."
    # SOURCE R02 L1185 (로만)
    roman "앗,,, 맞아요……!"
    # SOURCE R02 L1188 (로만)
    roman "기억하고 계셨네요."
    # SOURCE R02 L1191 (주인공)
    mc "네. 약속했으니까요."
    # SOURCE R02 L1195
    narrator "로만 씨는 노트를 품에 안았다."
    # SOURCE R02 L1198 (로만)
    roman "……고마워요."
    # CONTI SOURCE R02 L1200 [시간 경과 · 오후 4:50]
    $ phone_timeline_cue("R02", "R02_L1200")
    # SOURCE R02 L1202 [BG] 캠퍼스 정원 벤치 · 노을
    $ story_draft_scene("캠퍼스 정원 벤치 · 노을")
    # SOURCE R02 L1206
    narrator "로만 씨는 짧은 연습 원고를 펼쳤다."
    # SOURCE R02 L1208
    narrator "아직 발표할 완성 원고는 아니었다."
    # SOURCE R02 L1210
    narrator "목소리를 가다듬는 연습을 위한 문장이었다."
    # SOURCE R02 L1213 (로만)
    roman "그럼…… 시작해볼게요."
    # SOURCE R02 L1216 (주인공)
    mc "네. 편하게 하세요."
    # SOURCE R02 L1220
    narrator "로만 씨는 첫 문장을 읽었다."
    # SOURCE R02 L1222
    narrator "처음에는 목소리가 조금 떨렸다."
    # SOURCE R02 L1224
    narrator "하지만 두 번째 문장부터는 훨씬 또렷해졌다."
    # SOURCE R02 L1227 (로만)
    roman "……."
    # SOURCE R02 L1230 (로만)
    roman "어, 어떠셨어요?"
    # SOURCE R02 L1233 (주인공)
    mc "좋았어요. 처음보다 뒤쪽이 훨씬 자연스러웠어요."
    # SOURCE R02 L1236 (로만)
    roman "……정말요?"
    # SOURCE R02 L1239 (주인공)
    mc "네. 다만 첫 문장에서는 조금 긴장하신 것 같아요."
    # SOURCE R02 L1242 (로만)
    roman "아…… 맞아요."
    # SOURCE R02 L1245 (로만)
    roman "처음이 제일 어려워요."
    # SOURCE R02 L1248 (주인공)
    mc "그럼 첫 문장만 한 번 더 읽어볼까요?"
    # SOURCE R02 L1251 (로만)
    roman "……네."
    # SOURCE R02 L1255
    narrator "우리는 첫 문장을 여러 번 연습했다."
    # SOURCE R02 L1257
    narrator "처음에는 로만 씨가 자꾸 멈췄지만, 몇 번 지나자 조금씩 편안해졌다."
    # SOURCE R02 L1260 (로만)
    roman "……후우."
    # SOURCE R02 L1263 (주인공)
    mc "이번에는 정말 자연스러웠어요."
    # SOURCE R02 L1266 (로만)
    roman "……후후."
    # SOURCE R02 L1268 (로만)
    roman "다행이에요."
    # SOURCE R02 L1272
    narrator "로만 씨는 노트를 덮었다."
    # SOURCE R02 L1274
    narrator "그러다가 조용히 말했다."
    # SOURCE R02 L1277 (로만)
    roman "혼자 연습할 때보다 덜 무서워요."
    # SOURCE R02 L1280 (주인공)
    mc "그럼 다음에도 같이 연습해요."
    # SOURCE R02 L1283 (로만)
    roman "……네."
    # SOURCE R02 L1286 (로만)
    roman "그런데……."
    # SOURCE R02 L1289 (주인공)
    mc "네?"
    # SOURCE R02 L1292 (로만)
    roman "다음에는 제가 혼자서도 한번 해볼게요."
    # SOURCE R02 L1295 (주인공)
    mc "좋아요. 로만 씨가 연습하신 걸 나중에 들어볼게요."
    # SOURCE R02 L1299
    narrator "로만 씨는 고개를 끄덕였다."
    # SOURCE R02 L1301
    narrator "그 모습이 좋았다."
    # SOURCE R02 L1303
    narrator "도움이 필요할 때는 부탁하고, 혼자 해보고 싶은 일은 스스로 해보는 사람."
    # SOURCE R02 L1305
    narrator "나는 앞으로도 그런 로만 씨의 모습을 보고 싶었다."
    # SOURCE R02 L1307 [FLAG] `roman_reading_application_submitted = True`
    $ story_flag("roman_reading_application_submitted", True)
    # SOURCE R02 L1309 [FLAG] `roman_r02_practice_started = True`
    $ story_flag("roman_r02_practice_started", True)
    # CONTI SOURCE R02 L1311 [SCENE 05 END]
    jump roman_r02_sc06

label roman_r02_sc06:
    $ phone_timeline_enter("R02", "roman_r02_sc06")
    # SOURCE R02 L1314 # R02 SC06 · 가까워지면 달라지는 것
    # SOURCE R02 L1316 [BG] 캠퍼스 산책로 · 해 질 무렵
    $ story_draft_scene("캠퍼스 산책로 · 해 질 무렵")
    # SOURCE R02 L1318 [BGM] Warm Evening
    $ story_draft_bgm("Warm Evening")
    # CONTI SOURCE R02 L1320 [ANIM] 로만 · 눈 깜빡임, 머리카락 미세 움직임
    # SOURCE R02 L1324
    narrator "연습을 마친 뒤 우리는 강의동 쪽으로 걸었다."
    # SOURCE R02 L1326
    narrator "해가 기울면서 산책로에는 긴 그림자가 생겼다."
    # SOURCE R02 L1328
    narrator "로만 씨는 노트를 가방에 넣고 두 손으로 가방끈을 잡았다."
    # SOURCE R02 L1331 (로만)
    roman "오늘도 시간 내주셔서 감사해요."
    # SOURCE R02 L1334 (주인공)
    mc "아니에요. 저도 즐거웠어요."
    # SOURCE R02 L1337 (로만)
    roman "……후후."
    # SOURCE R02 L1341
    narrator "조금 걸었을 때 로만 씨가 먼저 말을 꺼냈다."
    # SOURCE R02 L1344 (로만)
    roman "저기……."
    # SOURCE R02 L1347 (주인공)
    mc "네?"
    # SOURCE R02 L1350 (로만)
    roman "요즘은 제가 먼저 연락드리는 일이 많아진 것 같아요."
    # SOURCE R02 L1353 (주인공)
    mc "그러네요."
    # SOURCE R02 L1356 (로만)
    roman "……혹시 귀찮지는 않으세요?"
    # SOURCE R02 L1359 (주인공)
    mc "전혀요."
    # SOURCE R02 L1362 (로만)
    roman "……다행이에요."
    # SOURCE R02 L1366
    narrator "로만 씨는 작게 웃었다."
    # SOURCE R02 L1368
    narrator "하지만 무언가 더 묻고 싶은 표정이었다."
    # SOURCE R02 L1371 (주인공)
    mc "혹시 걱정되는 일 있으세요?"
    # SOURCE R02 L1374 (로만)
    roman "아……."
    # SOURCE R02 L1377 (로만)
    roman "그냥……."
    # SOURCE R02 L1379 (로만)
    roman "너무 자주 연락드리면 부담스러우실 수도 있을 것 같아서요."
    # SOURCE R02 L1382 (주인공)
    mc "바쁠 때는 답장이 늦을 수도 있겠지만, 연락 주시는 건 좋아요."
    # SOURCE R02 L1385 (로만)
    roman "……."
    # SOURCE R02 L1388 (로만)
    roman "그럼 저도 바쁠 때는 조금 늦게 답장드려도 되겠죠?"
    # SOURCE R02 L1391 (주인공)
    mc "당연하죠."
    # SOURCE R02 L1394 (로만)
    roman "……후후."
    # SOURCE R02 L1397 (로만)
    roman "그럼 좋겠어요."
    # SOURCE R02 L1401
    narrator "로만 씨는 조금 안심한 것 같았다."
    # SOURCE R02 L1403
    narrator "그런데 나는 문득 궁금해졌다."
    # SOURCE R02 L1406 (주인공)
    mc "로만 씨는 요즘 저랑 자주 만나는 게 어떠세요?"
    # SOURCE R02 L1409 (로만)
    roman "……네?"
    # SOURCE R02 L1412 (주인공)
    mc "저는 즐거운데요. 로만 씨는 어떤지 궁금해서요."
    # SOURCE R02 L1415 (로만)
    roman "……."
    # CONTI SOURCE R02 L1417 [LD] 로만 · 당황
    # SOURCE R02 L1421
    narrator "로만 씨가 잠시 걸음을 늦췄다."
    # SOURCE R02 L1424 (로만)
    roman "저, 저도……."
    # SOURCE R02 L1426 (로만)
    roman "좋아요."
    # SOURCE R02 L1429 (주인공)
    mc "다행이네요."
    # SOURCE R02 L1432 (로만)
    roman "……그런데."
    # SOURCE R02 L1435 (주인공)
    mc "네?"
    # SOURCE R02 L1438 (로만)
    roman "예전에는 혼자 책 읽는 시간이 제일 편했거든요."
    # SOURCE R02 L1441 (주인공)
    mc "네."
    # SOURCE R02 L1444 (로만)
    roman "지금도 좋아해요."
    # SOURCE R02 L1446 (로만)
    roman "그런데 요즘은……."
    # SOURCE R02 L1448 (로만)
    roman "좋은 문장을 읽으면 [player_name] 씨한테도 이야기해드리고 싶어져요."
    # SOURCE R02 L1452
    narrator "나는 잠깐 말을 잊었다."
    # SOURCE R02 L1455 (로만)
    roman "그리고 맛있는 걸 먹으면……."
    # SOURCE R02 L1457 (로만)
    roman "다음에 같이 와보고 싶고요."
    # SOURCE R02 L1460 (로만)
    roman "귀여운 강아지를 보면……."
    # SOURCE R02 L1462 (로만)
    roman "같이 보면 좋겠다는 생각도 들어요."
    # SOURCE R02 L1466
    narrator "로만 씨는 마지막 말을 하고 고개를 숙였다."
    # SOURCE R02 L1469 (로만)
    roman "앗,,, 제가 너무 많이 이야기했네요……."
    # SOURCE R02 L1472 (주인공)
    mc "아니에요."
    # SOURCE R02 L1476
    narrator "조금 더 길게 대답하고 싶었다."
    # SOURCE R02 L1478
    narrator "그런데 생각보다 말이 바로 나오지 않았다."
    # SOURCE R02 L1480
    narrator "……왜 이렇게 신경 쓰이지?"
    # SOURCE R02 L1482 [CHOICE 01 · 로만의 솔직한 말]
    menu:
        # SOURCE R02 L1484 선택지
        "저도 좋은 걸 보면 로만 씨가 생각날 때가 있어요.":
            # SOURCE R02 L1487 (주인공)
            mc "저도 가끔 그래요. 로만 씨가 좋아하실 만한 걸 보면 생각나더라고요."
            # SOURCE R02 L1490 (로만)
            roman "……!"
            # SOURCE R02 L1493 (로만)
            roman "……정말요?"
            # SOURCE R02 L1496 (주인공)
            mc "네."
            # SOURCE R02 L1499 (로만)
            roman "……후후."
            # SOURCE R02 L1501 (로만)
            roman "그럼 저만 그런 게 아니었네요."
            # SOURCE R02 L1503 [FLAG] `roman_affection += 2`
            $ story_apply("roman_r02_choice01_a", affection={'roman': 2})
        # SOURCE R02 L1505 선택지
        "이렇게 편하게 이야기해 주셔서 좋아요.":
            # SOURCE R02 L1508 (주인공)
            mc "로만 씨가 편하게 이야기해 주시는 게 좋아요."
            # SOURCE R02 L1511 (로만)
            roman "……."
            # SOURCE R02 L1514 (로만)
            roman "그럼 앞으로도 조금씩 말씀드릴게요."
            # SOURCE R02 L1516 [FLAG] `roman_trust += 2`
            $ story_apply("roman_r02_choice01_b", trust={'roman': 2})
        # SOURCE R02 L1518 선택지
        "그럼 다음에는 제가 먼저 좋은 장소를 찾아볼게요.":
            # SOURCE R02 L1521 (주인공)
            mc "이번에는 제가 로만 씨가 좋아하실 만한 곳을 찾아볼게요."
            # SOURCE R02 L1524 (로만)
            roman "……후후."
            # SOURCE R02 L1526 (로만)
            roman "그럼 기대하고 있을게요."
            # SOURCE R02 L1529 (로만)
            roman "대신 저도 추천할 곳 하나 더 찾아둘래요."
            # SOURCE R02 L1531 [FLAG] `roman_next_date_promise = True`
            $ story_apply("roman_r02_choice01_c", values={'roman_next_date_promise': True})
    # SOURCE R02 L1537
    narrator "우리는 다시 걷기 시작했다."
    # SOURCE R02 L1539
    narrator "처음 만났을 때와는 조금 달랐다."
    # SOURCE R02 L1541
    narrator "그때는 로만 씨가 무슨 생각을 하는지 몰라 조심스러웠다."
    # SOURCE R02 L1543
    narrator "지금은 조금씩 알게 됐다."
    # SOURCE R02 L1545
    narrator "그런데 이상하게도, 알게 될수록 더 궁금해진다."
    # SOURCE R02 L1547 [BG] 캠퍼스 갈림길 · 노을
    $ story_draft_scene("캠퍼스 갈림길 · 노을")
    # SOURCE R02 L1550 (로만)
    roman "저는 여기서 가면 돼요."
    # SOURCE R02 L1553 (주인공)
    mc "네. 오늘 연습 수고 많으셨어요."
    # SOURCE R02 L1556 (로만)
    roman "후후…… 감사합니다."
    # SOURCE R02 L1560
    narrator "로만 씨는 잠시 걸음을 멈췄다."
    # SOURCE R02 L1563 (로만)
    roman "저기."
    # SOURCE R02 L1566 (주인공)
    mc "네?"
    # SOURCE R02 L1569 (로만)
    roman "오늘……."
    # SOURCE R02 L1571 (로만)
    roman "만나자고 연락드리길 잘한 것 같아요."
    # SOURCE R02 L1574 (주인공)
    mc "저도 만나서 좋았어요."
    # SOURCE R02 L1577 (로만)
    roman "……."
    # SOURCE R02 L1580 (로만)
    roman "그럼 다음에도 연락드릴게요."
    # SOURCE R02 L1583 (주인공)
    mc "네. 기다릴게요."
    # SOURCE R02 L1587
    narrator "로만 씨는 작게 손을 흔들었다."
    # SOURCE R02 L1589
    narrator "그 모습이 멀어질 때까지 바라보다가 나도 돌아섰다."
    # SOURCE R02 L1591
    narrator "그런데 몇 걸음 지나지 않아 자꾸 뒤를 돌아보게 됐다."
    # SOURCE R02 L1593
    narrator "……이거."
    # SOURCE R02 L1595
    narrator "그냥 친한 사람이라서 그런 걸까?"
    # CONTI SOURCE R02 L1599 [SCENE 06 END]
    jump roman_r02_sc07

label roman_r02_sc07:
    $ phone_timeline_enter("R02", "roman_r02_sc07")
    # SOURCE R02 L1602 # R02 SC07 · 기다리는 사람의 마음
    # SOURCE R02 L1604 [BG] 주인공 방 · 저녁
    $ story_draft_scene("주인공 방 · 저녁")
    # SOURCE R02 L1606 [BGM] Quiet Room
    $ story_draft_bgm("Quiet Room")
    # CONTI SOURCE R02 L1608 [FADE IN]
    # SOURCE R02 L1612
    narrator "과제를 끝내고 노트북을 닫았다."
    # SOURCE R02 L1614
    narrator "생각보다 시간이 많이 지났다."
    # SOURCE R02 L1616
    narrator "휴대전화를 확인하니 로만 씨에게서 메시지가 와 있었다."
    # CONTI SOURCE R02 L1618 [UI] 로만 개인 메시지
    $ story_chat(True, title="로만")
    # CONTI SOURCE R02 L1620 [오후 3:42]
    $ phone_timeline_cue("R02", "R02_L1620")
    # SOURCE R02 L1623 (로만)
    roman "앗,,, 오늘 도서관에서 재미있는 책을 발견했어요!"
    # SOURCE R02 L1625 (로만)
    roman "나중에 같이 읽어보고 싶어요……."
    # CONTI SOURCE R02 L1627 [오후 5:06]
    $ phone_timeline_cue("R02", "R02_L1627")
    # SOURCE R02 L1630 (로만)
    roman "아…… 혹시 바쁘신가요?"
    # SOURCE R02 L1632 (로만)
    roman "급하게 답장 안 하셔도 괜찮아요……!"
    # CONTI SOURCE R02 L1634 [현재 · 오후 7:10]
    $ phone_timeline_cue("R02", "R02_L1634")
    # SOURCE R02 L1638
    narrator "……아."
    # SOURCE R02 L1640
    narrator "과제를 하는 동안 휴대전화를 무음으로 해뒀다."
    # SOURCE R02 L1642
    narrator "답장하려고 화면을 열었다."
    # CONTI SOURCE R02 L1644 [UI] 메시지 작성
    # SOURCE R02 L1647 (주인공 · 메시지)
    mc "로만 씨, 답장이 늦었네요. 과제하느라 휴대전화를 못 봤어요."
    # SOURCE R02 L1649 (주인공 · 메시지)
    mc "무슨 책 발견하셨어요?"
    # SOURCE R02 L1653
    narrator "잠시 뒤 읽음 표시가 나타났다."
    # CONTI SOURCE R02 L1655 [SFX] 새 메시지
    # SOURCE R02 L1658 (로만)
    roman "앗,,, 과제하고 계셨군요!"
    # SOURCE R02 L1660 (로만)
    roman "제가 방해한 건 아닌가 걱정했어요……."
    # SOURCE R02 L1663 (주인공 · 메시지)
    mc "아니에요. 괜찮아요."
    # SOURCE R02 L1666 (로만)
    roman "……다행이에요."
    # SOURCE R02 L1670
    narrator "잠시 후 로만 씨가 책 표지 사진을 보내줬다."
    # SOURCE R02 L1672
    narrator "영문학 수업에서 언급됐던 단편집이었다."
    # SOURCE R02 L1675 (주인공 · 메시지)
    mc "오, 재미있어 보여요. 다음에 같이 읽어봐요."
    # SOURCE R02 L1678 (로만)
    roman "네……!"
    # SOURCE R02 L1680 (로만)
    roman "그런데……."
    # SOURCE R02 L1684
    narrator "점 세 개가 찍힌 메시지가 도착했다."
    # SOURCE R02 L1686
    narrator "곧이어 다음 문장이 나타났다."
    # SOURCE R02 L1689 (로만)
    roman "혹시 제가 너무 자주 연락드리는 건 아닐까요……?"
    # SOURCE R02 L1693
    narrator "……또 그 걱정이구나."
    # SOURCE R02 L1695
    narrator "어제 산책하면서도 비슷한 이야기를 했다."
    # SOURCE R02 L1697
    narrator "로만 씨는 자신이 상대에게 부담을 주는 걸 꽤 신경 쓰는 모양이다."
    # SOURCE R02 L1700 (주인공 · 메시지)
    mc "저는 로만 씨랑 이야기하는 게 좋아요."
    # SOURCE R02 L1702 (주인공 · 메시지)
    mc "다만 과제할 때는 답장이 늦을 수도 있어요."
    # SOURCE R02 L1705 (로만)
    roman "……네."
    # SOURCE R02 L1707 (로만)
    roman "저도 그건 알아요."
    # SOURCE R02 L1710 (로만)
    roman "그런데 가끔은 괜히 신경 쓰이더라고요……."
    # SOURCE R02 L1714
    narrator "나는 잠시 생각했다."
    # SOURCE R02 L1716
    narrator "로만 씨가 직접 이야기해 줬으니 나도 솔직하게 답하고 싶었다."
    # SOURCE R02 L1718 [CHOICE 02 · 연락과 기다림]
    menu:
        # SOURCE R02 L1720 선택지
        "늦을 수는 있지만, 서로 편한 시간에 이야기해요.":
            # SOURCE R02 L1723 (주인공 · 메시지)
            mc "서로 바쁠 때는 늦게 답장해도 괜찮다고 생각해요."
            # SOURCE R02 L1725 (주인공 · 메시지)
            mc "대신 이야기하고 싶을 때는 편하게 연락해 주세요."
            # SOURCE R02 L1728 (로만)
            roman "……후후."
            # SOURCE R02 L1730 (로만)
            roman "네. 그게 좋겠어요."
            # SOURCE R02 L1732 (로만)
            roman "저도 제 시간 잘 보내고 있을게요."
            # SOURCE R02 L1734 [FLAG] `roman_mutual_respect += 2`
            $ story_apply("roman_r02_choice02_a", counters={'roman_mutual_respect': 2})
        # SOURCE R02 L1736 선택지
        "걱정되시면 언제든 물어보셔도 돼요.":
            # SOURCE R02 L1739 (주인공 · 메시지)
            mc "혹시 신경 쓰이시면 편하게 물어보세요."
            # SOURCE R02 L1741 (주인공 · 메시지)
            mc "제가 확인할 수 있을 때 말씀드릴게요."
            # SOURCE R02 L1744 (로만)
            roman "……네."
            # SOURCE R02 L1746 (로만)
            roman "그렇게 말해주시니까 조금 안심돼요."
            # SOURCE R02 L1748 [FLAG] `roman_reassurance += 1`
            $ story_apply("roman_r02_choice02_b", counters={'roman_reassurance': 1})
        # SOURCE R02 L1750 선택지
        "앞으로는 로만 씨를 기다리게 하지 않을게요.":
            # SOURCE R02 L1753 (주인공 · 메시지)
            mc "앞으로는 로만 씨를 기다리게 하지 않을게요."
            # SOURCE R02 L1757
            narrator "보내고 나니 조금 지나친 약속 같기도 했다."
            # SOURCE R02 L1759
            narrator "수업도 있고, 과제도 있고."
            # SOURCE R02 L1761
            narrator "항상 즉시 답장할 수는 없을 텐데."
            # SOURCE R02 L1764 (로만)
            roman "……정말요?"
            # SOURCE R02 L1766 (로만)
            roman "앗,,, 그렇게까지 해주실 필요는 없는데……."
            # SOURCE R02 L1769 (로만)
            roman "그래도…… 조금 기뻐요."
            # SOURCE R02 L1771 [FLAG] `roman_unrealistic_promise += 1`
            $ story_apply("roman_r02_choice02_c", counters={'roman_unrealistic_promise': 1})
    # SOURCE R02 L1777
    narrator "대화는 그렇게 마무리됐다."
    # SOURCE R02 L1779
    narrator "큰일은 아니었다."
    # SOURCE R02 L1781
    narrator "누군가를 좋아하게 되면 작은 일에도 신경이 쓰일 수 있으니까."
    # SOURCE R02 L1783
    narrator "그런데 오늘의 대화는 조금 기억에 남았다."
    # SOURCE R02 L1785
    narrator "로만 씨는 글 속 인물들이 서로의 마음을 말하지 않아도 알아주기를 바라지 않는다고 했었다."
    # SOURCE R02 L1787
    narrator "그런데 실제 대화에서는 아직 조금 어려운 것 같다."
    # SOURCE R02 L1789
    narrator "……어쩌면 나도 마찬가지일지도 모르고."
    # CONTI SOURCE R02 L1791 [SFX] 스마트폰 진동
    # SOURCE R02 L1794 (로만)
    roman "앗,,, 아까 말한 책 말인데요."
    # SOURCE R02 L1796 (로만)
    roman "다음에 같이 읽으면 좋겠어요."
    # SOURCE R02 L1799 (주인공 · 메시지)
    mc "좋아요. 그때는 저도 책 하나 추천해 드릴게요."
    # SOURCE R02 L1802 (로만)
    roman "……후후."
    # SOURCE R02 L1804 (로만)
    roman "기대하고 있을게요."
    # CONTI SOURCE R02 L1806 [UI] 스마트폰 화면 종료
    $ story_chat(False)
    # SOURCE R02 L1810
    narrator "나는 휴대전화를 내려놓았다."
    # SOURCE R02 L1812
    narrator "기다림이 따뜻할 수도 있다고 했던 로만 씨의 말이 떠올랐다."
    # SOURCE R02 L1814
    narrator "그런데 기다리는 시간이 언제나 따뜻하기만 한 건 아닐 것이다."
    # SOURCE R02 L1816
    narrator "그럼 우리는 앞으로 어떻게 해야 할까."
    # SOURCE R02 L1818
    narrator "……아직은 잘 모르겠다."
    # SOURCE R02 L1820
    narrator "다만 서로에게 물어볼 수 있는 사이라면, 조금씩 알아갈 수 있겠지."
    # CONTI SOURCE R02 L1822 [SCENE 07 END]
    jump roman_r02_sc08

label roman_r02_sc08:
    $ phone_timeline_enter("R02", "roman_r02_sc08")
    # SOURCE R02 L1825 # R02 SC08 · 다음 페이지에는
    # SOURCE R02 L1827 [BG] 교내 도서관 · 저녁
    $ story_draft_scene("교내 도서관 · 저녁")
    # SOURCE R02 L1829 [BGM] Gentle Reading
    $ story_draft_bgm("Gentle Reading")
    # CONTI SOURCE R02 L1831 [FADE IN]
    # SOURCE R02 L1835
    narrator "며칠 뒤, 로만 씨와 다시 도서관에서 만났다."
    # SOURCE R02 L1837
    narrator "그동안 우리는 가끔 메시지를 주고받았고, 낭독회 연습도 조금씩 이어갔다."
    # SOURCE R02 L1839
    narrator "로만 씨는 예전보다 먼저 말을 거는 일이 많아졌다."
    # SOURCE R02 L1841
    narrator "좋아하는 책을 추천하기도 하고, 재미있는 문장을 발견하면 보내주기도 했다."
    # SOURCE R02 L1843
    narrator "그리고 가끔은 나를 놀렸다."
    # SOURCE R02 L1845
    narrator "……정말 가끔이지만."
    # CONTI SOURCE R02 L1847 [LD] 로만 · 기본 미소
    # SOURCE R02 L1850 (로만)
    roman "앗,,, 오늘은 제가 먼저 왔어요."
    # SOURCE R02 L1853 (주인공)
    mc "그러네요. 무슨 좋은 일 있으세요?"
    # SOURCE R02 L1856 (로만)
    roman "후후……."
    # SOURCE R02 L1858 (로만)
    roman "오늘은 숙제 하나 준비했거든요."
    # SOURCE R02 L1861 (주인공)
    mc "숙제요?"
    # SOURCE R02 L1864 (로만)
    roman "네."
    # SOURCE R02 L1868
    narrator "로만 씨가 종이 한 장을 내밀었다."
    # SOURCE R02 L1870
    narrator "종이에는 짧은 글이 적혀 있었다."
    # SOURCE R02 L1872
    narrator "얼마 전 정원에서 연습했던 글을 조금 고친 내용이었다."
    # SOURCE R02 L1875 (주인공)
    mc "직접 수정하신 거예요?"
    # SOURCE R02 L1878 (로만)
    roman "네……!"
    # SOURCE R02 L1880 (로만)
    roman "지난번에 첫 문장이 어렵다고 했잖아요."
    # SOURCE R02 L1883 (주인공)
    mc "네."
    # SOURCE R02 L1886 (로만)
    roman "그래서 혼자 연습하면서 문장도 조금 바꿨어요."
    # SOURCE R02 L1889 (주인공)
    mc "한번 읽어봐도 될까요?"
    # SOURCE R02 L1892 (로만)
    roman "……네."
    # SOURCE R02 L1896
    narrator "나는 종이를 읽었다."
    # SOURCE R02 L1898
    narrator "도서관 창가에 앉아 있던 사람이 누군가에게 보내려던 편지를 접는 이야기였다."
    # SOURCE R02 L1900
    narrator "편지에는 분명 하고 싶은 말이 있었다."
    # SOURCE R02 L1902
    narrator "하지만 마지막에는 그 말을 전하지 않고 자신의 가방 속에 넣어두었다."
    # SOURCE R02 L1905 (주인공)
    mc "……좋네요."
    # SOURCE R02 L1908 (로만)
    roman "정말요?"
    # SOURCE R02 L1911 (주인공)
    mc "네. 그런데 마지막에 왜 편지를 보내지 않았을까요?"
    # SOURCE R02 L1914 (로만)
    roman "음……."
    # SOURCE R02 L1917 (로만)
    roman "아직 그 사람에게 직접 말할 준비가 안 됐을 수도 있죠."
    # SOURCE R02 L1920 (주인공)
    mc "그렇군요."
    # SOURCE R02 L1923 (로만)
    roman "그런데 저는……."
    # SOURCE R02 L1925 (로만)
    roman "그 사람이 언젠가는 편지를 보내면 좋겠어요."
    # SOURCE R02 L1928 (주인공)
    mc "왜요?"
    # SOURCE R02 L1931 (로만)
    roman "하고 싶은 말이 있는 건 나쁜 일이 아니잖아요."
    # SOURCE R02 L1935
    narrator "로만 씨는 잠시 종이를 바라봤다."
    # SOURCE R02 L1938 (로만)
    roman "말하기 어려울 수는 있지만……."
    # SOURCE R02 L1940 (로만)
    roman "계속 숨기기만 하면 상대는 모를 수도 있으니까요."
    # SOURCE R02 L1943 (주인공)
    mc "……그렇겠네요."
    # SOURCE R02 L1947
    narrator "로만 씨의 목소리는 조용했다."
    # SOURCE R02 L1949
    narrator "하지만 그 안에는 분명한 마음이 있었다."
    # CONTI SOURCE R02 L1951 [시간 경과 · 오후 6:40]
    $ phone_timeline_cue("R02", "R02_L1951")
    # SOURCE R02 L1953 [BG] 도서관 창가 · 저녁
    $ story_draft_scene("도서관 창가 · 저녁")
    # SOURCE R02 L1957
    narrator "로만 씨는 연습 원고를 정리했다."
    # SOURCE R02 L1960 (로만)
    roman "오늘은 여기까지만 할게요."
    # SOURCE R02 L1963 (주인공)
    mc "벌써요?"
    # SOURCE R02 L1966 (로만)
    roman "후후. 너무 오래 읽으면 목이 아플 것 같아서요."
    # SOURCE R02 L1969 (주인공)
    mc "맞아요. 무리하지 않는 게 좋죠."
    # SOURCE R02 L1972 (로만)
    roman "……."
    # SOURCE R02 L1976
    narrator "로만 씨는 한동안 가방을 정리하지 않았다."
    # SOURCE R02 L1978
    narrator "뭔가 더 이야기하고 싶은 표정이었다."
    # SOURCE R02 L1981 (주인공)
    mc "로만 씨?"
    # SOURCE R02 L1984 (로만)
    roman "앗,,, 네."
    # SOURCE R02 L1987 (주인공)
    mc "하실 말씀 있으세요?"
    # SOURCE R02 L1990 (로만)
    roman "……."
    # SOURCE R02 L1993 (로만)
    roman "저 하나 여쭤봐도 될까요?"
    # SOURCE R02 L1996 (주인공)
    mc "네."
    # SOURCE R02 L1999 (로만)
    roman "혹시……."
    # SOURCE R02 L2001 (로만)
    roman "앞으로도 저랑 이렇게 자주 만나주실 수 있을까요?"
    # SOURCE R02 L2005
    narrator "나는 잠깐 생각했다."
    # SOURCE R02 L2007
    narrator "앞으로도."
    # SOURCE R02 L2009
    narrator "그 말이 이상하게 마음에 걸렸다."
    # SOURCE R02 L2012 (주인공)
    mc "네. 저도 로만 씨랑 계속 만나고 싶어요."
    # SOURCE R02 L2015 (로만)
    roman "……."
    # CONTI SOURCE R02 L2017 [ANIM] 로만 눈 깜빡임 후 홍조 표정 전환
    # SOURCE R02 L2020 (로만)
    roman "……후후."
    # SOURCE R02 L2022 (로만)
    roman "그럼 다행이에요."
    # SOURCE R02 L2025 (주인공)
    mc "그런데 왜 갑자기 물어보셨어요?"
    # SOURCE R02 L2028 (로만)
    roman "……그냥."
    # SOURCE R02 L2030 (로만)
    roman "요즘은 이런 시간이 좋아서요."
    # SOURCE R02 L2034
    narrator "로만 씨는 작은 목소리로 말했다."
    # SOURCE R02 L2037 (로만)
    roman "책을 같이 읽는 것도 좋고."
    # SOURCE R02 L2039 (로만)
    roman "점심 먹으면서 이야기하는 것도 좋고."
    # SOURCE R02 L2041 (로만)
    roman "……그냥 같이 걷는 것도 좋아요."
    # SOURCE R02 L2045
    narrator "나는 잠시 아무 말도 하지 못했다."
    # SOURCE R02 L2047
    narrator "로만 씨도 조용히 나를 바라봤다."
    # SOURCE R02 L2049
    narrator "처음 만났을 때라면 둘 다 어색하게 웃으며 넘어갔을 것이다."
    # SOURCE R02 L2051
    narrator "그런데 이번에는."
    # SOURCE R02 L2053
    narrator "그 말을 그냥 넘기고 싶지 않았다."
    # SOURCE R02 L2056 (주인공)
    mc "저도 그래요."
    # SOURCE R02 L2059 (로만)
    roman "……."
    # SOURCE R02 L2062 (주인공)
    mc "로만 씨랑 같이 있으면 시간이 금방 가요."
    # SOURCE R02 L2065 (로만)
    roman "……후후."
    # SOURCE R02 L2067 (로만)
    roman "저도요."
    # SOURCE R02 L2069 [BGM] 서서히 작아짐
    $ story_draft_bgm("서서히 작아짐")
    # SOURCE R02 L2073
    narrator "창밖으로 저녁 햇살이 마지막으로 들어왔다."
    # SOURCE R02 L2075
    narrator "로만 씨는 눈을 한 번 깜빡였다."
    # SOURCE R02 L2077
    narrator "그리고 조심스럽게 입을 열었다."
    # SOURCE R02 L2080 (로만)
    roman "그러면……."
    # SOURCE R02 L2084
    narrator "잠시 침묵."
    # SOURCE R02 L2087 (로만)
    roman "아니에요."
    # SOURCE R02 L2090 (주인공)
    mc "네?"
    # SOURCE R02 L2093 (로만)
    roman "……아직은 조금 부끄러워서요."
    # SOURCE R02 L2097
    narrator "로만 씨는 고개를 숙이며 웃었다."
    # SOURCE R02 L2100 (주인공)
    mc "괜찮아요. 천천히 말씀하세요."
    # SOURCE R02 L2103 (로만)
    roman "……네."
    # SOURCE R02 L2106 (로만)
    roman "그럼……."
    # SOURCE R02 L2108 (로만)
    roman "다음에 꼭 이야기해 드릴게요."
    # SOURCE R02 L2112
    narrator "그 말이 어떤 의미인지는 아직 알 수 없었다."
    # SOURCE R02 L2114
    narrator "하지만 분명한 건 하나 있었다."
    # SOURCE R02 L2116
    narrator "나도 이제 그 말을 듣고 싶었다."
    # SOURCE R02 L2118
    narrator "언젠가 로만 씨가 준비됐을 때."
    # SOURCE R02 L2120
    narrator "그리고 나 역시 내 마음을 조금 더 잘 알게 됐을 때."
    # CONTI SOURCE R02 L2122 [SFX] 휴대전화 알림
    # SOURCE R02 L2125 (로만)
    roman "……앗."
    # SOURCE R02 L2128 (주인공)
    mc "무슨 일이세요?"
    # SOURCE R02 L2131 (로만)
    roman "문학 낭독회 안내가 왔어요."
    # SOURCE R02 L2135
    narrator "로만 씨는 휴대전화를 확인했다."
    # SOURCE R02 L2137
    narrator "표정이 조금 진지해졌다."
    # SOURCE R02 L2140 (로만)
    roman "낭독 원고 최종 제출이 다음 주래요."
    # SOURCE R02 L2143 (주인공)
    mc "생각보다 얼마 안 남았네요."
    # SOURCE R02 L2146 (로만)
    roman "……네."
    # SOURCE R02 L2149 (로만)
    roman "그래서 당분간은 글을 조금 더 써야 할 것 같아요."
    # SOURCE R02 L2152 (주인공)
    mc "바쁘시겠네요."
    # SOURCE R02 L2155 (로만)
    roman "그럴 것 같아요."
    # SOURCE R02 L2159
    narrator "로만 씨는 잠시 망설이다가 말했다."
    # SOURCE R02 L2162 (로만)
    roman "그래도……."
    # SOURCE R02 L2164 (로만)
    roman "시간 되면 가끔 연락드릴게요."
    # SOURCE R02 L2167 (주인공)
    mc "좋아요. 다만 글 쓰시는 시간도 충분히 챙기세요."
    # SOURCE R02 L2170 (로만)
    roman "……네."
    # SOURCE R02 L2172 (로만)
    roman "후후. 알겠어요."
    # SOURCE R02 L2176
    narrator "로만 씨는 웃었다."
    # SOURCE R02 L2178
    narrator "나는 그 모습이 좋았다."
    # SOURCE R02 L2180
    narrator "하지만 한편으로는 조금 아쉬운 생각도 들었다."
    # SOURCE R02 L2182
    narrator "앞으로 며칠 동안은 지금처럼 자주 만나지 못할 수도 있겠구나."
    # SOURCE R02 L2184
    narrator "……그럼에도 괜찮겠지."
    # SOURCE R02 L2186
    narrator "서로 할 일이 있으니까."
    # SOURCE R02 L2188
    narrator "그게 당연한 일이다."
    # SOURCE R02 L2190 [BG] 도서관 앞 · 밤
    $ story_draft_scene("도서관 앞 · 밤")
    # SOURCE R02 L2194
    narrator "도서관 밖으로 나오자 바람이 조금 차가웠다."
    # SOURCE R02 L2196
    narrator "로만 씨는 가방끈을 고쳐 잡았다."
    # SOURCE R02 L2199 (로만)
    roman "오늘도 고마웠어요."
    # SOURCE R02 L2202 (주인공)
    mc "저도 즐거웠어요."
    # SOURCE R02 L2205 (로만)
    roman "……후후."
    # SOURCE R02 L2208 (로만)
    roman "다음에 또 뵐게요."
    # SOURCE R02 L2211 (주인공)
    mc "네. 원고 준비 잘하세요."
    # SOURCE R02 L2215
    narrator "로만 씨는 손을 흔들며 걸어갔다."
    # SOURCE R02 L2217
    narrator "나는 그 모습을 잠시 바라봤다."
    # SOURCE R02 L2219
    narrator "조금 더 함께하고 싶다는 생각이 들었다."
    # SOURCE R02 L2221
    narrator "하지만 오늘은 여기까지였다."
    # SOURCE R02 L2223
    narrator "……괜찮다."
    # SOURCE R02 L2225
    narrator "다음이 있으니까."
    # CONTI SOURCE R02 L2227 [FADE OUT]
    # SOURCE R02 L2229 [BGM] R02 Ending Theme
    $ story_draft_bgm("R02 Ending Theme")
    # CONTI SOURCE R02 L2231 [TEXT] 「ROMAN ROUTE」
    # CONTI SOURCE R02 L2233 [TEXT] 「R02 COMPLETE」
    # CONTI SOURCE R02 L2235 [TEXT] 「조금씩, 가까워지는 거리」
    # CONTI SOURCE R02 L2237 [TEXT] 「NEXT · R03 말하지 않아도 알 거라고 생각했어요」
    # SOURCE R02 L2239 [FLAG] `roman_r02_complete = True`
    $ story_flag("roman_r02_complete", True)
    # SOURCE R02 L2241 [FLAG] `roman_reading_deadline_known = True`
    $ story_flag("roman_reading_deadline_known", True)
    # CONTI SOURCE R02 L2243 [NEXT] ROMAN ROUTE R03
    # CONTI SOURCE R02 L2245 [SCENE 08 END]
    jump roman_r03
