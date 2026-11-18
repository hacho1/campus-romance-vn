# CH07 · original manuscript dialogue-only import
# SOURCE: design_docs/story_sources/chapter07.txt
# SHA256: 6b573dad2a25e391a489f296c531b854cecedeb99c8031c8c15535f202015ee7
# Rebuild: tools/import_ch06_ch07.py --write


label chapter07:
    $ phone_timeline_enter("CH07", "chapter07")
    $ story_begin_chapter(7, "우리 사이, 그 이상의 시작")
    jump ch07_sc01

label ch07_sc01:
    $ phone_timeline_enter("CH07", "ch07_sc01")
    # SOURCE CH07 L42 알림이 울리지 않는 아침
    # SOURCE CH07 L44 [BG] 주인공 방 · 늦은 오전
    $ story_draft_scene("주인공 방 · 늦은 오전")
    # SOURCE CH07 L46 [BGM] Quiet Morning
    $ story_draft_bgm("Quiet Morning")
    # CONTI SOURCE CH07 L48 [FADE IN]
    # SOURCE CH07 L52
    narrator "……조용하다."
    # SOURCE CH07 L54
    narrator "정말 조용하다."
    # SOURCE CH07 L56
    narrator "휴대전화도 울리지 않고, 누군가 일찍 모이자고 재촉하지도 않는다."
    # SOURCE CH07 L58
    narrator "축제가 끝난 지 일주일."
    # SOURCE CH07 L60
    narrator "드디어 대학생다운 평범한 하루가 돌아왔다."
    # SOURCE CH07 L63 주인공 · 혼잣말
    mc "……좋네."
    # SOURCE CH07 L67
    narrator "알람을 맞추지 않아도 되고."
    # SOURCE CH07 L69
    narrator "아침부터 발표 자료를 확인하지 않아도 되고."
    # SOURCE CH07 L71
    narrator "갑자기 단체 채팅방에 호출될 일도 없다."
    # SOURCE CH07 L73
    narrator "이것이야말로 내가 원했던 평화로운 대학생활이다."
    # CONTI SOURCE CH07 L75 [시간 경과 · 오전 10:35]
    $ phone_timeline_cue("CH07", "CH07_L75")
    # SOURCE CH07 L79
    narrator "……."
    # CONTI SOURCE CH07 L81 [시간 경과 · 오전 10:48]
    $ phone_timeline_cue("CH07", "CH07_L81")
    # SOURCE CH07 L85
    narrator "……너무 조용한데?"
    # SOURCE CH07 L87
    narrator "나는 침대 옆에 놓아둔 휴대전화를 집었다."
    # CONTI SOURCE CH07 L89 [UI] 스마트폰 화면
    # SOURCE CH07 L91
    narrator "「새 메시지 없음」"
    # SOURCE CH07 L94 주인공 · 혼잣말
    mc "……다들 바쁜가."
    # SOURCE CH07 L98
    narrator "당연하지."
    # SOURCE CH07 L100
    narrator "축제가 끝났으니까."
    # SOURCE CH07 L102
    narrator "시아는 밀린 작품을 그릴 테고, 오므는 사진을 정리하고 있을 것이다."
    # SOURCE CH07 L104
    narrator "로만은 책을 읽거나 글을 쓸지도 모르고."
    # SOURCE CH07 L106
    narrator "다림 선배는 수업이나 과제로 바쁠 것이다."
    # SOURCE CH07 L108
    narrator "하린 선배도 작업실로 돌아갔겠지."
    # SOURCE CH07 L110
    narrator "모두 자기 생활이 있다."
    # SOURCE CH07 L112
    narrator "나 역시 마찬가지다."
    # SOURCE CH07 L114
    narrator "그런데 왜 이렇게 신경이 쓰이지?"
    # CONTI SOURCE CH07 L116 [UI] 단체 채팅방 「우리 사이 (6)」
    $ story_chat(True, title="우리 사이")
    $ phone_threads["campus_group"]["title"] = "우리 사이"
    # SOURCE CH07 L120
    narrator "마지막 메시지는 사흘 전이었다."
    # SOURCE CH07 L123 시아
    sia "야 이 사진 누가 찍었냐ㅋㅋㅋㅋ"
    # SOURCE CH07 L126 오므
    omu "내가"
    # SOURCE CH07 L129 시아
    sia "내 표정 왜 이러는데"
    # SOURCE CH07 L132 오므
    omu "니 원래 그런 표정 많이 짓는다"
    # SOURCE CH07 L135 하린
    lumi "저도 비슷하게 기억하는데요."
    # SOURCE CH07 L138 시아
    sia "아 진짜ㅋㅋㅋ"
    # SOURCE CH07 L141 다림
    darim "사진 보내주셔서 감사해요. 후후."
    # SOURCE CH07 L144 로만
    roman "앗,,, 저도 저장했어요……!"
    # SOURCE CH07 L148
    narrator "나는 그 대화를 다시 읽었다."
    # SOURCE CH07 L150
    narrator "별것 아닌 내용이었다."
    # SOURCE CH07 L152
    narrator "그런데 웃음이 났다."
    # CONTI SOURCE CH07 L154 [UI] 갤러리 · CH05 단체 사진 / CH06 축제 사진
    $ story_chat(False)
    # SOURCE CH07 L158
    narrator "사진 속에는 익숙한 얼굴들이 있었다."
    # SOURCE CH07 L160
    narrator "처음에는 서로 이름을 외우는 것부터 어려웠는데."
    # SOURCE CH07 L162
    narrator "이제는 누가 어떻게 웃는지까지 기억한다."
    # SOURCE CH07 L165 주인공 · 혼잣말
    mc "……다들 잘 지내겠지."
    # SOURCE CH07 L169
    narrator "나는 휴대전화를 내려놓았다."
    # SOURCE CH07 L171
    narrator "그러다가 다시 집었다."
    # SOURCE CH07 L173
    narrator "……아니, 왜 자꾸 확인하는 거야."
    # CONTI SOURCE CH07 L175 [SFX] 진동
    # SOURCE CH07 L178 주인공 · 혼잣말
    mc "어?"
    # CONTI SOURCE CH07 L180 [UI] 새 메시지 도착
    $ story_chat(True, title="우리 사이")
    $ phone_threads["campus_group"]["title"] = "우리 사이"
    # SOURCE CH07 L183 시아
    sia "야"
    # SOURCE CH07 L185 시아
    sia "다들 살아 있냐?"
    # SOURCE CH07 L189
    narrator "……."
    # SOURCE CH07 L191
    narrator "하필 이 타이밍에?"
    # SOURCE CH07 L193
    narrator "나도 모르게 웃음이 터졌다."
    # CONTI SOURCE CH07 L195 [SCENE 01 END]
    $ story_chat(False)
    jump ch07_sc02

label ch07_sc02:
    $ phone_timeline_enter("CH07", "ch07_sc02")
    # SOURCE CH07 L198 다들 살아 있냐?
    # SOURCE CH07 L200 [BG] 주인공 방
    $ story_draft_scene("주인공 방")
    # SOURCE CH07 L202 [BGM] Light Comedy
    $ story_draft_bgm("Light Comedy")
    # CONTI SOURCE CH07 L204 [UI] 단체 채팅방 「우리 사이 (6)」
    $ story_chat(True, title="우리 사이")
    $ phone_threads["campus_group"]["title"] = "우리 사이"
    # SOURCE CH07 L207 시아
    # SCENE ECHO: already sent in SC01; continue with Omu's reply.
    # SOURCE CH07 L209 시아
    # SCENE ECHO: already sent in SC01; continue with Omu's reply.
    # SOURCE CH07 L212 오므
    omu "살아 있다"
    # SOURCE CH07 L215 시아
    sia "와 답장 빠르네"
    # SOURCE CH07 L218 오므
    omu "니가 알림을 다섯 개나 보내잖아"
    # SOURCE CH07 L221 시아
    sia "그 정도는 안 보냈거든?"
    # SOURCE CH07 L224 하린
    lumi "연속으로 세 번 보내셨네요."
    # SOURCE CH07 L227 시아
    sia "하린아 넌 왜 그걸 세고 있냐"
    # SOURCE CH07 L230 하린
    lumi "화면에 나오는데요."
    # SOURCE CH07 L233 다림
    darim "다들 오랜만이에요."
    # SOURCE CH07 L236 로만
    roman "앗,,, 안녕하세요……!"
    # SOURCE CH07 L239 시아
    sia "와 다 살아 있네"
    # SOURCE CH07 L241 시아
    sia "그럼 오늘 모일래?"
    # SOURCE CH07 L244 오므
    omu "왜"
    # SOURCE CH07 L247 시아
    sia "그냥"
    # SOURCE CH07 L249 시아
    sia "축제 끝났다고 진짜 안 볼 거냐?"
    # SOURCE CH07 L252 다림
    darim "후후. 갑자기 모이는 것도 재미있겠네요."
    # SOURCE CH07 L255 하린
    lumi "오늘 오후에는 시간 괜찮아요."
    # SOURCE CH07 L258 로만
    roman "저도 수업 끝나면 가능해요……!"
    # SOURCE CH07 L261 오므
    omu "내도 오후에는 된다"
    # SOURCE CH07 L264 시아
    sia "좋아 그럼 결정"
    # SOURCE CH07 L267 시아
    sia "[player_name]은?"
    # SOURCE CH07 L270 주인공 · 메시지
    mc "저도 괜찮아요. 어디서 만날까요?"
    # SOURCE CH07 L273 시아
    sia "학교 앞 카페 어때"
    # SOURCE CH07 L276 다림
    darim "거기 자리 넓으니까 괜찮겠네요."
    # SOURCE CH07 L279 하린
    lumi "그럼 세 시쯤?"
    # SOURCE CH07 L282 시아
    sia "오케이"
    # SOURCE CH07 L285 오므
    omu "근데 시아야"
    # SOURCE CH07 L288 시아
    sia "왜"
    # SOURCE CH07 L291 오므
    omu "니 오늘도 늦는 거 아니제?"
    # SOURCE CH07 L294 시아
    sia "야 이제 그 얘기는 그만해라"
    # SOURCE CH07 L297 하린
    lumi "역사가 반복될 가능성은 충분하죠."
    # SOURCE CH07 L300 시아
    sia "아 진짜ㅋㅋㅋㅋ"
    # SOURCE CH07 L304
    narrator "채팅창이 순식간에 시끄러워졌다."
    # SOURCE CH07 L306
    narrator "아까까지 조용하다고 생각했던 게 거짓말 같았다."
    # SOURCE CH07 L309 주인공 · 혼잣말
    narrator "……그래. 이게 익숙하지."
    # SOURCE CH07 L313
    narrator "나는 옷을 갈아입고 가방을 챙겼다."
    # SOURCE CH07 L315
    narrator "처음으로 축제 자료 하나 없이 이 사람들을 만나러 간다."
    # SOURCE CH07 L317
    narrator "이상하게도, 그게 조금 기대됐다."
    # CONTI SOURCE CH07 L319 [TRANSITION] 오후 2:40
    $ phone_timeline_cue("CH07", "CH07_L319")
    $ story_chat(False)
    # SOURCE CH07 L321 [BG] 캠퍼스 앞 거리
    $ story_draft_scene("캠퍼스 앞 거리")
    # SOURCE CH07 L325
    narrator "카페로 가는 길은 축제 준비 때와 똑같았다."
    # SOURCE CH07 L327
    narrator "그런데 마음은 조금 달랐다."
    # SOURCE CH07 L329
    narrator "오늘은 해야 할 일이 없다."
    # SOURCE CH07 L331
    narrator "제출할 보고서도, 수정해야 할 영상도 없다."
    # SOURCE CH07 L333
    narrator "그냥 만나서 이야기하면 된다."
    # CONTI SOURCE CH07 L335 [SFX] 개인 메시지 알림
    # SOURCE CH07 L337 [CONDITION] `ch06_festival_partner`의 메시지 중 하나만 출력
    if story_id(ch06_festival_partner) == "roman":
        # SOURCE CH07 L339 로만
        $ story_chat(True, title="로만")
        # SOURCE CH07 L341 로만
        roman "앗,,, 저 카페 근처예요."
        # SOURCE CH07 L343 로만
        roman "혹시 길에서 만나면 같이 들어가실래요……?"
        # SOURCE CH07 L346 주인공 · 메시지
        mc "좋아요. 저도 거의 다 왔어요."
        $ story_chat(False)
    elif story_id(ch06_festival_partner) == "sia":
        # SOURCE CH07 L348 시아
        $ story_chat(True, title="시아")
        # SOURCE CH07 L350 시아
        sia "야 나 벌써 근처임"
        # SOURCE CH07 L352 시아
        sia "오늘은 진짜 안 늦는다"
        # SOURCE CH07 L355 주인공 · 메시지
        mc "시아 씨가 먼저 도착하시면 조금 놀랄 것 같은데요."
        # SOURCE CH07 L358 시아
        sia "야ㅋㅋㅋ"
        $ story_chat(False)
    elif story_id(ch06_festival_partner) == "darim":
        # SOURCE CH07 L360 다림
        $ story_chat(True, title="다림")
        # SOURCE CH07 L362 다림
        darim "저 조금 일찍 도착할 것 같아요."
        # SOURCE CH07 L364 다림
        darim "오시는 길 조심하세요."
        # SOURCE CH07 L367 주인공 · 메시지
        mc "네, 선배도요. 금방 뵐게요."
        $ story_chat(False)
    elif story_id(ch06_festival_partner) == "omu":
        # SOURCE CH07 L369 오므
        $ story_chat(True, title="오므")
        # SOURCE CH07 L371 오므
        omu "나 근처에서 사진 좀 찍고 있다"
        # SOURCE CH07 L373 오므
        omu "도착하면 연락해라"
        # SOURCE CH07 L376 주인공 · 메시지
        mc "네. 금방 갈게요."
        $ story_chat(False)
    elif story_id(ch06_festival_partner) == "lumi":
        # SOURCE CH07 L378 하린
        $ story_chat(True, title="하린")
        # SOURCE CH07 L380 하린
        lumi "혹시 카페 가는 길이에요?"
        # SOURCE CH07 L382 하린
        lumi "저도 작업실에서 막 나왔어요."
        # SOURCE CH07 L385 주인공 · 메시지
        mc "네. 같이 가실래요?"
        # SOURCE CH07 L388 하린
        lumi "후후. 좋아요."
        $ story_chat(False)
    # SOURCE CH07 L394
    narrator "휴대전화를 주머니에 넣었다."
    # SOURCE CH07 L396
    narrator "오늘은 조금 다른 이야기가 생길지도 모르겠다."
    # CONTI SOURCE CH07 L398 [SCENE 02 END]
    jump ch07_sc03

label ch07_sc03:
    $ phone_timeline_enter("CH07", "ch07_sc03")
    # SOURCE CH07 L400 일이 아니어도 모이는 사람들
    # SOURCE CH07 L402 [BG] 학교 앞 카페 · 오후
    $ story_draft_scene("학교 앞 카페 · 오후", cast=["roman", "sia", "darim", "omu", "lumi"], standing=True)
    # COMMON STANDING BEGIN CH07 L402
    $ story_stage_fade_in(["roman", "sia", "darim", "omu", "lumi"])
    # COMMON STANDING END CH07 L402
    # SOURCE CH07 L404 [BGM] Friendly Afternoon
    $ story_draft_bgm("Friendly Afternoon")
    # SOURCE CH07 L408
    # CH07 VISUAL 0611 BEGIN ch07_reunion_comedy-start
    $ sd_event_start("ch07_reunion_comedy", "01", transition=0.35)
    # CH07 VISUAL 0611 END ch07_reunion_comedy-start
    narrator "카페 문을 열자 익숙한 사람들이 보였다."
    # SOURCE CH07 L410
    narrator "시아는 소파에 비스듬히 앉아 있었고, 오므는 휴대전화로 사진을 보고 있었다."
    # SOURCE CH07 L412
    narrator "다림 선배는 메뉴판을 살펴보고 있었고, 로만은 창가 쪽에 앉아 있었다."
    # SOURCE CH07 L414
    narrator "하린 선배는 시아가 무언가를 이야기하는 걸 듣고 있었다."
    # SOURCE CH07 L417 시아
    # COMMON STANDING BEGIN CH07 L417
    $ story_stage(faces={"sia": "happy", "darim": "happy", "roman": "happy"})
    # COMMON STANDING END CH07 L417
    sia "야! 여기!"
    # SOURCE CH07 L420 주인공
    mc "안녕하세요. 다들 먼저 오셨네요."
    # SOURCE CH07 L423 오므
    omu "어. 니도 앉아라."
    # SOURCE CH07 L426 로만
    roman "앗,,, 오셨어요……!"
    # SOURCE CH07 L429 다림
    darim "오시는 길 괜찮으셨어요?"
    # SOURCE CH07 L432 주인공
    mc "네. 그런데 시아 씨가 벌써 와 계시네요?"
    # SOURCE CH07 L435 시아
    # COMMON STANDING BEGIN CH07 L435
    $ story_stage(faces={"sia": "angry"})
    # COMMON STANDING END CH07 L435
    sia "야."
    # SOURCE CH07 L437 시아
    sia "그게 그렇게 놀랄 일이냐?"
    # SOURCE CH07 L440 하린
    # COMMON STANDING BEGIN CH07 L440
    $ story_stage(faces={"lumi": "smug"})
    # COMMON STANDING END CH07 L440
    lumi "조금 역사적인 순간이긴 하네요."
    # SOURCE CH07 L443 시아
    sia "하린아!"
    # SOURCE CH07 L446 오므
    omu "인증사진이라도 찍어놓을까."
    # SOURCE CH07 L449 시아
    # COMMON STANDING BEGIN CH07 L449
    $ story_stage(faces={"sia": "happy"})
    # COMMON STANDING END CH07 L449
    sia "아 진짜ㅋㅋㅋ"
    # CH07 VISUAL 0611 BEGIN ch07_reunion_comedy-end
    $ sd_event_end(transition=0.35)
    # CH07 VISUAL 0611 END ch07_reunion_comedy-end
    # CONTI SOURCE CH07 L451 [SD EVENT] `ch07_reunion_comedy`
    # CONTI SOURCE CH07 L453 [연출] 이번 챕터의 유일한 신규 SD 단체 일러스트. 시아가 억울해하는 가운데 오므가 카메라를 들고, 하린은 장난스럽게 웃고, 로만과 다림은 그 모습을 지켜보는 장면. 한 장으로 고정하고 대사만 진행.
    # CONTI SOURCE CH07 L455 [전환] 일반 LD 스탠딩
    # SOURCE CH07 L459
    narrator "나는 자리에 앉았다."
    # SOURCE CH07 L461
    narrator "이상했다."
    # SOURCE CH07 L463
    narrator "며칠 전까지만 해도 같은 테이블에 앉으면 가장 먼저 자료를 펼쳤는데."
    # SOURCE CH07 L465
    narrator "오늘은 테이블 위에 음료와 간식밖에 없었다."
    # SOURCE CH07 L468 다림
    darim "다들 요즘 어떻게 지내셨어요?"
    # SOURCE CH07 L471 시아
    sia "나는 밀린 작업 하고 있었지."
    # SOURCE CH07 L474 오므
    omu "축제 끝나자마자 또 작업이네."
    # SOURCE CH07 L477 시아
    sia "애니메이션학과는 원래 그런 곳이야."
    # SOURCE CH07 L480 하린
    lumi "저도 작업실에서 살고 있었어요."
    # SOURCE CH07 L483 주인공
    mc "선배도 많이 바쁘셨군요."
    # SOURCE CH07 L486 하린
    lumi "네. 그래도 축제 준비가 끝나서 조금 여유는 생겼어요."
    # SOURCE CH07 L489 로만
    roman "저는…… 책도 읽고 글도 조금 썼어요."
    # SOURCE CH07 L492 다림
    darim "저는 과제 정리했어요."
    # SOURCE CH07 L495 시아
    # COMMON STANDING BEGIN CH07 L495
    $ story_stage(faces={"sia": "confused"})
    # COMMON STANDING END CH07 L495
    sia "야, 우리 왜 이렇게 재미없는 대학생들 같냐?"
    # SOURCE CH07 L498 오므
    omu "원래 대학생이 그렇지."
    # SOURCE CH07 L501 시아
    sia "아니, 그래도 축제 때는 좀 더 화려했잖아."
    # SOURCE CH07 L504 주인공
    mc "그때는 매일 사고가 있었으니까요."
    # SOURCE CH07 L507 시아
    sia "……맞네."
    # SOURCE CH07 L510 시아
    sia "그럼 지금이 더 좋은 건가?"
    # SOURCE CH07 L513 하린
    lumi "사고가 없다는 점에서는요."
    # SOURCE CH07 L517
    # COMMON STANDING BEGIN CH07 L517
    $ story_stage(faces={"roman": "happy", "sia": "happy", "darim": "happy", "omu": "happy", "lumi": "happy"})
    # COMMON STANDING END CH07 L517
    narrator "모두 웃었다."
    # SOURCE CH07 L519
    narrator "조금 전까지 느꼈던 어색함이 금방 사라졌다."
    # SOURCE CH07 L522 로만
    roman "앗,,, 그런데 오늘은 회의 안 하는 거죠……?"
    # SOURCE CH07 L525 다림
    darim "네. 오늘은 진짜 아무 일정 없어요."
    # SOURCE CH07 L528 시아
    sia "와, 선배 입에서 그런 말 나오니까 신기하다."
    # SOURCE CH07 L531 다림
    darim "후후. 저도 쉴 때는 쉬어요."
    # SOURCE CH07 L534 오므
    omu "그럼 오늘은 뭐 할 건데?"
    # SOURCE CH07 L537 시아
    sia "일단 먹고."
    # SOURCE CH07 L540 하린
    lumi "그다음은요?"
    # SOURCE CH07 L543 시아
    # COMMON STANDING BEGIN CH07 L543
    $ story_stage(faces={"sia": "confused"})
    # COMMON STANDING END CH07 L543
    sia "……."
    # SOURCE CH07 L545 시아
    sia "그건 먹으면서 생각하지."
    # SOURCE CH07 L548 주인공
    mc "시아 씨다운 계획이네요."
    # SOURCE CH07 L551 시아
    # COMMON STANDING BEGIN CH07 L551
    $ story_stage(faces={"sia": "smug"})
    # COMMON STANDING END CH07 L551
    sia "그치? 완벽하지?"
    # SOURCE CH07 L554 오므
    omu "그게 계획이가."
    # SOURCE CH07 L558
    narrator "오늘은 누가 의장을 맡을 필요도 없었다."
    # SOURCE CH07 L560
    narrator "어떤 안건을 통과시킬 필요도 없었다."
    # SOURCE CH07 L562
    narrator "그냥 이렇게 함께 이야기하고 있었다."
    # SOURCE CH07 L564
    narrator "그런데도 시간이 금방 지나갔다."
    # CONTI SOURCE CH07 L566 [시간 경과 · 오후 3:35]
    $ phone_timeline_cue("CH07", "CH07_L566")
    # SOURCE CH07 L569 시아
    sia "야, 근데 축제 때 사진 있잖아."
    # SOURCE CH07 L572 오므
    omu "어."
    # SOURCE CH07 L575 시아
    sia "그거 다시 보여줘."
    # SOURCE CH07 L578 오므
    omu "왜?"
    # SOURCE CH07 L581 시아
    sia "내 표정 정상적으로 나온 것도 있을 거 아니야."
    # SOURCE CH07 L584 오므
    omu "……있겠지."
    # SOURCE CH07 L587 시아
    # COMMON STANDING BEGIN CH07 L587
    $ story_stage(faces={"sia": "confused"})
    # COMMON STANDING END CH07 L587
    sia "왜 그렇게 자신 없어?"
    # SOURCE CH07 L590 로만
    # COMMON STANDING BEGIN CH07 L590
    $ story_stage(faces={"roman": "happy"})
    # COMMON STANDING END CH07 L590
    roman "후후……."
    # SOURCE CH07 L593 다림
    darim "저도 사진 다시 보고 싶어요."
    # SOURCE CH07 L596 하린
    lumi "그럼 같이 볼까요?"
    # SOURCE CH07 L600
    narrator "오므가 갤러리를 열었다."
    # SOURCE CH07 L602
    narrator "모두가 자연스럽게 화면 쪽으로 몸을 기울였다."
    # SOURCE CH07 L604
    narrator "그렇게 우리는 다시 축제 이야기를 꺼내기 시작했다."
    # SOURCE CH07 L606
    narrator "하지만 이번에는 해야 할 일을 정하기 위해서가 아니었다."
    # SOURCE CH07 L608
    narrator "그저 함께했던 순간이 재미있어서였다."
    # CONTI SOURCE CH07 L610 [SCENE 03 END]
    jump ch07_sc04

label ch07_sc04:
    $ phone_timeline_enter("CH07", "ch07_sc04")
    # SOURCE CH07 L613 우리 사이에 남은 이야기
    # SOURCE CH07 L615 [BG] 카페 · 창가 자리
    $ story_draft_scene("카페 · 창가 자리", cast=["roman", "sia", "darim", "omu", "lumi"], standing=True)
    # COMMON STANDING BEGIN CH07 L615
    $ story_stage_fade_in(["roman", "sia", "darim", "omu", "lumi"])
    # COMMON STANDING END CH07 L615
    # SOURCE CH07 L617 [BGM] Warm Memories
    $ story_draft_bgm("Warm Memories")
    # SOURCE CH07 L621
    narrator "오므의 휴대전화 화면에는 축제 사진들이 차례로 나타났다."
    # SOURCE CH07 L623
    narrator "CH05에서 함께 찍었던 단체 사진."
    # SOURCE CH07 L625
    narrator "축제 당일의 전시 부스."
    # SOURCE CH07 L627
    narrator "그리고 방문객들이 전시를 둘러보던 모습."
    # SOURCE CH07 L630 오므
    omu "이게 설치 끝난 날 찍은 거고."
    # SOURCE CH07 L632 오므
    omu "이건 축제 당일."
    # SOURCE CH07 L635 다림
    darim "와, 하루 차이인데 분위기가 많이 다르네요."
    # SOURCE CH07 L638 로만
    roman "앗,,, 사람이 정말 많았어요."
    # SOURCE CH07 L641 하린
    lumi "그래도 통로는 잘 확보됐네요."
    # SOURCE CH07 L644 시아
    # COMMON STANDING BEGIN CH07 L644
    $ story_stage(faces={"sia": "smug"})
    # COMMON STANDING END CH07 L644
    sia "야, 너는 사진 보고도 동선부터 보냐?"
    # SOURCE CH07 L647 하린
    lumi "직업병 같은 걸까요?"
    # SOURCE CH07 L650 시아
    sia "아직 취업도 안 했잖아ㅋㅋ"
    # SOURCE CH07 L654
    narrator "사진을 넘기던 오므가 잠시 멈췄다."
    # SOURCE CH07 L656
    narrator "화면에는 처음 준비하던 시절의 어수선한 테이블이 있었다."
    # SOURCE CH07 L659 오므
    omu "이것도 남겨놨다."
    # SOURCE CH07 L662 주인공
    mc "CH04 때 같이 골랐던 사진이네요."
    # SOURCE CH07 L665 오므
    omu "어. 기억하네?"
    # SOURCE CH07 L668 주인공
    mc "그럼요."
    # SOURCE CH07 L671 다림
    darim "그 사진 전시했을 때 반응도 좋았죠."
    # SOURCE CH07 L674 로만
    roman "아…… 맞아요. 준비 과정이 보여서 좋다고 하셨어요."
    # SOURCE CH07 L677 시아
    sia "그때 진짜 정신없었는데."
    # SOURCE CH07 L680 하린
    # COMMON STANDING BEGIN CH07 L680
    $ story_stage(faces={"lumi": "happy"})
    # COMMON STANDING END CH07 L680
    lumi "이제는 그것도 추억이네요."
    # SOURCE CH07 L684
    narrator "그 말이 조금 이상하게 들렸다."
    # SOURCE CH07 L686
    narrator "불과 얼마 전까지 현재였던 일이 벌써 추억이 되어 있었다."
    # CONTI SOURCE CH07 L688 [UI] 축제 주요 기억 회상
    # CONTI SOURCE CH07 L690 [연출] 플레이어가 이번 회차에서 실제 경험한 이벤트 중 대표 장면만 표시.
    # CONTI SOURCE CH07 L692 [TEXT/PLAN] - CH01: 팀원들과 처음 만난 날
    # CONTI SOURCE CH07 L693 [TEXT/PLAN] - CH02: 스키 팀과의 첫 경쟁
    # CONTI SOURCE CH07 L694 [TEXT/PLAN] - CH03: 시범 운영과 두 팀의 협력
    # CONTI SOURCE CH07 L695 [TEXT/PLAN] - CH04: 선택 히로인과 나눈 개인적인 대화
    # CONTI SOURCE CH07 L696 [TEXT/PLAN] - CH05: 최종 평가와 축제 전날의 단체 사진
    # CONTI SOURCE CH07 L697 [TEXT/PLAN] - CH06: 함께 축제를 즐긴 상대와의 순간
    # CONTI SOURCE CH07 L699 [화면 복귀]
    # SOURCE CH07 L703
    narrator "처음에는 정말 아무것도 몰랐다."
    # SOURCE CH07 L705
    narrator "그저 축제 부스 하나를 준비하는 일이라고 생각했다."
    # SOURCE CH07 L707
    narrator "그런데 그 일을 하면서 예상하지 못한 사람들을 만났다."
    # SOURCE CH07 L709
    narrator "그리고 그 사람들이 내 일상에 조금씩 들어왔다."
    # SOURCE CH07 L712 시아
    sia "야, 근데 이제 생각해보면 웃기지 않냐?"
    # SOURCE CH07 L715 주인공
    mc "어떤 게요?"
    # SOURCE CH07 L718 시아
    sia "처음에는 다들 어색했는데."
    # SOURCE CH07 L720 시아
    sia "이제는 같이 있는 게 너무 당연하잖아."
    # SOURCE CH07 L723 다림
    darim "그러게요."
    # SOURCE CH07 L726 로만
    # COMMON STANDING BEGIN CH07 L726
    $ story_stage(faces={"roman": "embarrassed"})
    # COMMON STANDING END CH07 L726
    roman "앗,,, 저는 처음에는 다들 너무 활발해서 조금 놀랐어요……."
    # SOURCE CH07 L729 오므
    omu "대부분 시아 때문 아이가."
    # SOURCE CH07 L732 시아
    sia "야!"
    # SOURCE CH07 L735 하린
    lumi "반박하기는 어렵겠네요."
    # SOURCE CH07 L739
    # COMMON STANDING BEGIN CH07 L739
    $ story_stage(faces={"roman": "happy", "sia": "happy", "darim": "happy", "omu": "happy", "lumi": "happy"})
    # COMMON STANDING END CH07 L739
    narrator "또 웃었다."
    # SOURCE CH07 L742 다림
    darim "그런데 오늘처럼 가끔 보는 것도 좋겠어요."
    # SOURCE CH07 L745 로만
    roman "네……! 저도요."
    # SOURCE CH07 L748 시아
    sia "그럼 다음에도 불시에 소집한다?"
    # SOURCE CH07 L751 오므
    omu "불시 말고 미리 말해라."
    # SOURCE CH07 L754 하린
    lumi "우리에게도 개인 일정은 있으니까요."
    # SOURCE CH07 L757 시아
    sia "알았어ㅋㅋ"
    # SOURCE CH07 L761
    narrator "각자 자기 삶이 있다."
    # SOURCE CH07 L763
    narrator "그래서 오늘처럼 모이려면 서로 시간을 내야 한다."
    # SOURCE CH07 L765
    narrator "예전에는 축제라는 일이 있어서 매일 만났다."
    # SOURCE CH07 L767
    narrator "앞으로는 그런 이유가 없어도 만나게 될까."
    # SOURCE CH07 L770 주인공
    mc "저는 다음에도 이렇게 모이면 좋겠어요."
    # SOURCE CH07 L773 다림
    darim "저도요."
    # SOURCE CH07 L776 로만
    roman "후후……."
    # SOURCE CH07 L779 시아
    sia "좋아. 그럼 다음 모임도 확정."
    # SOURCE CH07 L782 오므
    omu "날짜부터 정해라."
    # SOURCE CH07 L785 시아
    sia "……아, 맞다."
    # CONTI SOURCE CH07 L787 [시간 경과 · 오후 4:20]
    $ phone_timeline_cue("CH07", "CH07_L787")
    # SOURCE CH07 L791
    narrator "조금씩 자리를 정리하기 시작했다."
    # SOURCE CH07 L793
    narrator "로만은 도서관에 들러야 했고, 하린 선배는 작업실로 돌아가야 했다."
    # SOURCE CH07 L795
    narrator "다림 선배에게는 다음 강의가 있었고, 오므는 사진을 정리할 일이 있었다."
    # SOURCE CH07 L797
    narrator "시아 역시 마감해야 할 작업이 있었다."
    # SOURCE CH07 L800 시아
    sia "아, 벌써 가야 하냐."
    # SOURCE CH07 L803 하린
    lumi "시아 씨가 제일 바쁘다고 하지 않으셨어요?"
    # SOURCE CH07 L806 시아
    sia "그건 맞는데."
    # SOURCE CH07 L808 시아
    # COMMON STANDING BEGIN CH07 L808
    $ story_stage(faces={"sia": "sad"})
    # COMMON STANDING END CH07 L808
    sia "막상 헤어지려니까 아쉽잖아."
    # SOURCE CH07 L811 주인공
    mc "그럼 다음에 또 만나면 되죠."
    # SOURCE CH07 L814 시아
    # COMMON STANDING BEGIN CH07 L814
    $ story_stage(faces={"sia": "happy"})
    # COMMON STANDING END CH07 L814
    sia "……그렇지."
    # SOURCE CH07 L818
    narrator "오늘 우리는 축제 이야기를 많이 했다."
    # SOURCE CH07 L820
    narrator "하지만 이상하게도, 각자가 앞으로 할 일에 관한 이야기가 더 기억에 남았다."
    # SOURCE CH07 L822
    narrator "로만이 읽고 싶다는 책."
    # SOURCE CH07 L824
    narrator "시아가 만들고 있다는 웹툰."
    # SOURCE CH07 L826
    narrator "다림 선배와 아직 끝나지 않은 게임 승부."
    # SOURCE CH07 L828
    narrator "오므가 찍으러 가고 싶다는 풍경."
    # SOURCE CH07 L830
    narrator "하린 선배가 새로 시작한 설계."
    # SOURCE CH07 L832
    narrator "축제는 끝났지만, 이 사람들의 이야기는 계속된다."
    # SOURCE CH07 L834
    narrator "나도 그중 한 사람의 다음 이야기를 조금 더 가까이에서 보고 싶었다."
    # CONTI SOURCE CH07 L836 [SCENE 04 END]
    jump ch07_sc05

label ch07_sc05:
    $ phone_timeline_enter("CH07", "ch07_sc05")
    # SOURCE CH07 L839 오늘은 내가 먼저
    # SOURCE CH07 L841 [BG] 캠퍼스 산책로 · 늦은 오후
    $ story_draft_scene("캠퍼스 산책로 · 늦은 오후")
    # SOURCE CH07 L843 [BGM] Quiet Sunset
    $ story_draft_bgm("Quiet Sunset")
    # SOURCE CH07 L847
    narrator "카페에서 나온 뒤 모두와 인사를 나눴다."
    # SOURCE CH07 L849
    narrator "이번에는 다음 회의 일정도, 제출해야 할 자료도 없었다."
    # SOURCE CH07 L851
    narrator "그냥 헤어지는 거였다."
    # SOURCE CH07 L853
    narrator "나는 천천히 캠퍼스를 걸었다."
    # SOURCE CH07 L855
    narrator "주변에는 강의를 마치고 돌아가는 학생들이 있었다."
    # SOURCE CH07 L857
    narrator "누군가는 친구와 저녁 약속을 잡고 있었고, 누군가는 통화하면서 웃고 있었다."
    # SOURCE CH07 L859
    narrator "평범한 풍경이었다."
    # SOURCE CH07 L861
    narrator "나 역시 조금 전까지 친구들과 시간을 보내고 왔다."
    # SOURCE CH07 L863
    narrator "그런데 마음 한쪽에 묘한 아쉬움이 남았다."
    # SOURCE CH07 L866 주인공 · 혼잣말
    mc "……또 만나면 되는데."
    # SOURCE CH07 L870
    narrator "그렇다."
    # SOURCE CH07 L872
    narrator "다음에 또 만나면 된다."
    # SOURCE CH07 L874
    narrator "그렇게 어려운 일도 아니다."
    # SOURCE CH07 L876
    narrator "그런데 나는 왜 누군가의 다음 약속이 기다려지는 걸까."
    # SOURCE CH07 L878
    narrator "왜 그 사람과는 단체 모임이 아니라 둘이서 만나고 싶은 걸까."
    # SOURCE CH07 L880 [BG] 캠퍼스 벤치 · 노을
    $ story_draft_scene("캠퍼스 벤치 · 노을")
    # SOURCE CH07 L884
    narrator "나는 잠시 벤치에 앉았다."
    # SOURCE CH07 L886
    narrator "휴대전화에는 그동안 받은 개인 메시지가 남아 있었다."
    # SOURCE CH07 L888
    narrator "책 이야기."
    # SOURCE CH07 L890
    narrator "그림 이야기."
    # SOURCE CH07 L892
    narrator "게임 이야기."
    # SOURCE CH07 L894
    narrator "사진과 설계 이야기."
    # SOURCE CH07 L896
    narrator "처음에는 전부 축제와 관련된 일이었다."
    # SOURCE CH07 L898
    narrator "그러다 어느 순간부터는 그렇지 않은 메시지가 늘어났다."
    # SOURCE CH07 L900
    narrator "'오늘 뭐 하세요?'"
    # SOURCE CH07 L902
    narrator "'다음에 같이 갈래요?'"
    # SOURCE CH07 L904
    narrator "'이거 보여주고 싶어요.'"
    # SOURCE CH07 L906
    narrator "정말 별것 아닌 말들이다."
    # SOURCE CH07 L908
    narrator "하지만 누군가에게는 그런 말 한마디를 꺼내는 것도 용기가 필요한 일일 것이다."
    # SOURCE CH07 L910
    narrator "나도 지금 그렇다."
    # SOURCE CH07 L913 주인공 · 혼잣말
    mc "……먼저 연락해볼까."
    # SOURCE CH07 L917
    narrator "그런데 누구에게?"
    # SOURCE CH07 L919
    narrator "나는 잠시 화면을 바라봤다."
    # SOURCE CH07 L921
    narrator "다섯 사람 모두 소중하다."
    # SOURCE CH07 L923
    narrator "함께 준비했던 시간도, 서로 장난치던 순간도 즐거웠다."
    # SOURCE CH07 L925
    narrator "하지만 그중에서도 유독 기다려지는 사람이 있었다."
    # SOURCE CH07 L927
    narrator "그 사람과는 앞으로 무슨 일이 생길까."
    # SOURCE CH07 L929
    narrator "어떤 모습까지 알게 될까."
    # SOURCE CH07 L931
    narrator "그 생각만으로도 조금 설렜다."
    # SOURCE CH07 L933
    narrator "이제는 그 마음을 모른 척하지 않아도 될 것 같다."
    # CONTI SOURCE CH07 L935 [UI] 회상 기록 표시
    # SOURCE CH07 L937 [CONDITION] `ch06_festival_partner`에 따라 짧은 회상 하나를 출력
    if story_id(ch06_festival_partner) == "roman":
        # SOURCE CH07 L939 로만
        # SOURCE CH07 L942
        narrator "로만이 직접 만든 책갈피를 건네던 순간이 떠올랐다."
        # SOURCE CH07 L944
        narrator "다른 사람에게는 주지 않았다는 말."
        # SOURCE CH07 L946
        narrator "그리고 언젠가 자신의 글을 읽어달라고 했던 약속."
    elif story_id(ch06_festival_partner) == "sia":
        # SOURCE CH07 L948 시아
        # SOURCE CH07 L951
        narrator "시아가 자기 작품의 마지막 장면을 설명하던 순간이 떠올랐다."
        # SOURCE CH07 L953
        narrator "늘 장난을 치지만, 자신이 좋아하는 일에는 누구보다 진지한 사람이었다."
    elif story_id(ch06_festival_partner) == "darim":
        # SOURCE CH07 L955 다림
        # SOURCE CH07 L958
        narrator "다림 선배와 협동 게임을 하던 순간이 떠올랐다."
        # SOURCE CH07 L960
        narrator "평소 차분한 선배가 승부욕을 드러내며 웃던 모습."
        # SOURCE CH07 L962
        narrator "그 모습을 다시 보고 싶었다."
    elif story_id(ch06_festival_partner) == "omu":
        # SOURCE CH07 L964 오므
        # SOURCE CH07 L967
        narrator "오므와 함께 사진을 찍었던 순간이 떠올랐다."
        # SOURCE CH07 L969
        narrator "늘 카메라 뒤에 있던 사람이 그날만큼은 나와 같은 사진 속에 있었다."
    elif story_id(ch06_festival_partner) == "lumi":
        # SOURCE CH07 L971 하린
        # SOURCE CH07 L974
        narrator "하린 선배와 완성된 부스를 둘러보던 아침이 떠올랐다."
        # SOURCE CH07 L976
        narrator "늘 여유롭던 사람이 아무렇지 않은 말에 잠시 시선을 피하던 모습."
    # SOURCE CH07 L982
    narrator "그런 순간이 있었다."
    # SOURCE CH07 L984
    narrator "그리고 아직 경험하지 못한 순간도 많을 것이다."
    # SOURCE CH07 L986
    narrator "……그래."
    # SOURCE CH07 L988
    narrator "이번에는 내가 먼저 연락해보자."
    # SOURCE CH07 L990
    narrator "축제 준비가 아니라."
    # SOURCE CH07 L992
    narrator "그냥 그 사람이 보고 싶어서."
    # SOURCE CH07 L994 [BGM] 서서히 밝아지는 피아노
    $ story_draft_bgm("서서히 밝아지는 피아노")

label ch07_final_choice:
    # SOURCE CH07 L996 ### [FINAL CHOICE] 누구와 조금 더 가까워지고 싶을까?
    menu:
        # SOURCE CH07 L998 최종 선택 후보
        "로만 씨와 더 많은 이야기를 나누고 싶다.":
            $ ch07_route_candidate = "roman"
            jump ch07_final_confirmation
        # SOURCE CH07 L1000 최종 선택 후보
        "시아 씨의 새로운 모습을 더 알고 싶다.":
            $ ch07_route_candidate = "sia"
            jump ch07_final_confirmation
        # SOURCE CH07 L1002 최종 선택 후보
        "다림 선배와 일상적인 시간을 함께하고 싶다.":
            $ ch07_route_candidate = "darim"
            jump ch07_final_confirmation
        # SOURCE CH07 L1004 최종 선택 후보
        "오므 씨와 새로운 풍경을 보러 가고 싶다.":
            $ ch07_route_candidate = "omu"
            jump ch07_final_confirmation
        # SOURCE CH07 L1006 최종 선택 후보
        "하린 선배와 앞으로도 함께하고 싶다.":
            $ ch07_route_candidate = "lumi"
            jump ch07_final_confirmation

label ch07_final_confirmation:
    # SOURCE CH07 L1016
    narrator "「이 선택 이후에는 선택한 인물의 이야기가 시작됩니다.」"
    # SOURCE CH07 L1018
    narrator "「진행하시겠습니까?」"
    menu:
        "네, 이 사람의 이야기를 시작한다.":
            $ story_apply("ch07_final_route_" + ch07_route_candidate, values={"selected_route": ch07_route_candidate, "route_locked": True})
            jump ch07_sc05_confirmed
        "아직 결정하지 않는다. (선택 화면으로 돌아간다.)":
            jump ch07_final_choice
    # CONTI SOURCE CH07 L1008 [FLAG] `selected_route`에 선택한 히로인 ID 저장
    # CONTI SOURCE CH07 L1010 [FLAG] `route_locked = True`
    # CONTI SOURCE CH07 L1012 [중요] CH07의 유일한 개별 루트 확정 선택. 이전 호감도와 개인 이벤트는 이후 추가 대사에 반영하지만, 기본적으로 다섯 히로인 모두 선택 가능.
    # CONTI SOURCE CH07 L1014 [시스템 연출]
    # CONTI SOURCE CH07 L1020 - 네, 이 사람의 이야기를 시작한다.
    # CONTI SOURCE CH07 L1021 - 아직 결정하지 않는다. (선택 화면으로 돌아간다.)

label ch07_sc05_confirmed:
    $ phone_timeline_enter("CH07", "ch07_sc05_confirmed")
    # SOURCE CH07 L1027
    narrator "나는 연락처 목록에서 한 사람의 이름을 눌렀다."
    # SOURCE CH07 L1029
    narrator "이제는 내가 먼저 그 사람의 다음 이야기를 찾아가려고 한다."
    # CONTI SOURCE CH07 L1031 [선택한 히로인의 SC06 이벤트로 이동]
    # CONTI SOURCE CH07 L1033 [SCENE 05 END]
    if story_id(selected_route) == "roman":
        jump ch07_sc06_roman
    elif story_id(selected_route) == "sia":
        jump ch07_sc06_sia
    elif story_id(selected_route) == "darim":
        jump ch07_sc06_darim
    elif story_id(selected_route) == "omu":
        jump ch07_sc06_omu
    elif story_id(selected_route) == "lumi":
        jump ch07_sc06_lumi
    else:
        # Old/malformed saves do not select another person automatically.
        jump ch07_sc07

label ch07_sc06_roman:
    $ phone_timeline_enter("CH07", "ch07_sc06_roman")
    # SOURCE CH07 L1035 로만: 그 문장, 아직 기억하세요?
    # SOURCE CH07 L1037 [BG] 캠퍼스 벤치 · 노을
    $ story_draft_scene("캠퍼스 벤치 · 노을")
    # SOURCE CH07 L1039 [BGM] Gentle Decision
    $ story_draft_bgm("Gentle Decision")
    # SOURCE CH07 L1043
    narrator "연락처에서 로만의 이름을 눌렀다."
    # SOURCE CH07 L1045
    narrator "메시지를 적었다가 잠시 지웠다."
    # SOURCE CH07 L1047
    narrator "뭐라고 시작해야 하지."
    # SOURCE CH07 L1049
    narrator "그냥 책을 읽으러 가자고 하면 되나?"
    # SOURCE CH07 L1051
    narrator "……아니다."
    # SOURCE CH07 L1053
    narrator "괜히 핑계를 만들 필요는 없겠지."
    # CONTI SOURCE CH07 L1055 [UI] 로만 개인 메시지
    $ story_chat(True, title="로만")
    # SOURCE CH07 L1058 주인공 · 메시지
    mc "로만 씨, 혹시 오늘 도서관에 계세요?"
    # SOURCE CH07 L1061 로만
    roman "앗,,, 네……!"
    # SOURCE CH07 L1063 로만
    roman "책 반납하고 있었어요."
    # SOURCE CH07 L1066 주인공 · 메시지
    mc "괜찮으시면 잠깐 만날 수 있을까요? 같이 이야기하고 싶어서요."
    # CONTI SOURCE CH07 L1068 [SFX] 메시지 도착
    # SOURCE CH07 L1071 로만
    roman "……!"
    # SOURCE CH07 L1073 로만
    roman "네! 좋아요."
    # SOURCE CH07 L1075 로만
    roman "그럼 도서관 입구에서 기다릴게요……!"
    # CONTI SOURCE CH07 L1077 [TRANSITION] 도서관 앞 · 오후 5:45
    $ phone_timeline_cue("CH07", "CH07_L1077")
    $ story_chat(False)
    # SOURCE CH07 L1079 [BG] 도서관 입구
    $ story_draft_scene("도서관 입구", cast=["roman"], standing=True)
    # COMMON STANDING BEGIN CH07 L1079
    $ story_stage_fade_in(["roman"])
    # COMMON STANDING END CH07 L1079
    # CONTI SOURCE CH07 L1081 [ANIM] 로만 · 눈 깜빡임, 잔잔한 머리카락 움직임
    # SOURCE CH07 L1085
    narrator "도서관 앞에 도착하자 로만이 손을 흔들었다."
    # SOURCE CH07 L1088 로만
    # COMMON STANDING BEGIN CH07 L1088
    $ story_stage(faces={"roman": "happy"})
    # COMMON STANDING END CH07 L1088
    roman "앗,,, [player_name] 씨!"
    # SOURCE CH07 L1091 주인공
    mc "많이 기다리셨어요?"
    # SOURCE CH07 L1094 로만
    roman "아니에요……! 저도 방금 나왔어요."
    # SOURCE CH07 L1098
    narrator "로만은 작은 책 한 권을 들고 있었다."
    # SOURCE CH07 L1101 주인공
    mc "무슨 책이에요?"
    # SOURCE CH07 L1104 로만
    roman "아…… 전에 말씀드렸던 책이에요."
    # SOURCE CH07 L1107 주인공
    mc "같이 읽고 싶다고 하셨던 책이요?"
    # SOURCE CH07 L1110 로만
    roman "……네."
    # SOURCE CH07 L1113 로만
    roman "기억하고 계셨네요."
    # SOURCE CH07 L1116 주인공
    mc "그럼요."
    # SOURCE CH07 L1120
    narrator "로만은 책을 조금 더 꼭 쥐었다."
    # SOURCE CH07 L1123 로만
    roman "그런데 오늘은 무슨 일이세요……?"
    # SOURCE CH07 L1126 주인공
    mc "그냥 로만 씨랑 이야기하고 싶었어요."
    # SOURCE CH07 L1129 로만
    roman "……."
    # CONTI SOURCE CH07 L1131 [ANIM] 로만의 눈 깜빡임 후 미세한 홍조 표정 전환
    # SOURCE CH07 L1134 로만
    # COMMON STANDING BEGIN CH07 L1134
    $ story_stage(faces={"roman": "surprised"})
    # COMMON STANDING END CH07 L1134
    roman "……저랑요?"
    # SOURCE CH07 L1137 주인공
    mc "네. 축제도 끝났고, 이제는 따로 만날 일이 별로 없잖아요."
    # SOURCE CH07 L1140 로만
    roman "……그렇죠."
    # SOURCE CH07 L1143 주인공
    mc "그래서 앞으로도 가끔 같이 만나고 싶어요."
    # SOURCE CH07 L1146 로만
    roman "……."
    # SOURCE CH07 L1150
    narrator "로만은 잠시 아무 말도 하지 않았다."
    # SOURCE CH07 L1152
    narrator "나는 괜히 말을 너무 갑작스럽게 꺼냈나 싶었다."
    # SOURCE CH07 L1154
    narrator "그러나 로만은 곧 작게 웃었다."
    # SOURCE CH07 L1157 로만
    # COMMON STANDING BEGIN CH07 L1157
    $ story_stage(faces={"roman": "happy"})
    # COMMON STANDING END CH07 L1157
    roman "앗,,, 저도 그랬어요."
    # SOURCE CH07 L1160 주인공
    mc "네?"
    # SOURCE CH07 L1163 로만
    roman "축제 끝나고 조금 아쉬웠거든요."
    # SOURCE CH07 L1165 로만
    roman "이제 매일 같이 볼 이유가 없으니까……."
    # SOURCE CH07 L1168 로만
    roman "그래서 다음에 어떻게 연락드려야 할지 고민했어요."
    # SOURCE CH07 L1171 주인공
    mc "그냥 연락하셔도 되는데요."
    # SOURCE CH07 L1174 로만
    roman "……."
    # SOURCE CH07 L1177 로만
    # COMMON STANDING BEGIN CH07 L1177
    $ story_stage(faces={"roman": "embarrassed"})
    # COMMON STANDING END CH07 L1177
    roman "그렇게 말씀하셔도…… 조금 부끄럽잖아요."
    # SOURCE CH07 L1181
    narrator "로만은 조심스럽게 웃었다."
    # SOURCE CH07 L1183
    narrator "그러더니 책을 내밀었다."
    # SOURCE CH07 L1186 로만
    roman "그럼…… 오늘은 이것부터 같이 읽으실래요?"
    # SOURCE CH07 L1189 주인공
    mc "좋아요."
    # SOURCE CH07 L1191 [BG] 도서관 열람 공간 · 저녁
    $ story_draft_scene("도서관 열람 공간 · 저녁", cast=["roman"], standing=True)
    # COMMON STANDING BEGIN CH07 L1191
    $ story_stage_fade_in(["roman"])
    # COMMON STANDING END CH07 L1191
    # SOURCE CH07 L1195
    # CH07 VISUAL 0611 BEGIN ch07_private_roman-start
    $ cg_start("ch07_private_roman", transition=0.35)
    # CH07 VISUAL 0611 END ch07_private_roman-start
    narrator "우리는 창가에 나란히 앉았다."
    # SOURCE CH07 L1197
    narrator "밖에서는 해가 천천히 지고 있었다."
    # SOURCE CH07 L1199
    narrator "로만은 책갈피를 꺼내 책 사이에 끼웠다."
    # SOURCE CH07 L1201
    narrator "CH06에서 직접 만들어줬던 것과 같은 작은 파란 꽃이 그려져 있었다."
    # SOURCE CH07 L1204 주인공
    mc "그 책갈피 아직 사용하고 계시네요."
    # SOURCE CH07 L1207 로만
    # COMMON STANDING BEGIN CH07 L1207
    $ story_stage(faces={"roman": "happy"})
    # COMMON STANDING END CH07 L1207
    roman "후후…… 네."
    # SOURCE CH07 L1209 로만
    roman "같이 만들었던 날이 생각나서요."
    # SOURCE CH07 L1213
    narrator "로만은 잠시 책을 바라봤다."
    # SOURCE CH07 L1216 로만
    roman "저기……."
    # SOURCE CH07 L1219 주인공
    mc "네?"
    # SOURCE CH07 L1222 로만
    roman "오늘 먼저 연락해 주셔서 고마워요."
    # SOURCE CH07 L1225 주인공
    mc "저도 만나서 좋아요."
    # SOURCE CH07 L1228 로만
    roman "……후후."
    # SOURCE CH07 L1231 로만
    roman "그럼 다음에는 제가 먼저 연락드릴게요."
    # SOURCE CH07 L1234 주인공
    mc "기다릴게요."
    # SOURCE CH07 L1238
    narrator "로만은 책장을 넘겼다."
    # SOURCE CH07 L1240
    narrator "나는 그 옆에서 조용히 앉아 있었다."
    # SOURCE CH07 L1242
    narrator "아직 서로에게 어떤 사람인지 정확히 정의할 수는 없다."
    # SOURCE CH07 L1244
    narrator "하지만 지금은 그걸 서두르고 싶지 않았다."
    # SOURCE CH07 L1246
    narrator "이 사람과 나눌 이야기가 아직 많이 남아 있으니까."
    # SOURCE CH07 L1248 [CONDITION] `ch04_partner == "roman"`
    if story_id(ch04_partner) == "roman":
        # SOURCE CH07 L1251 로만
        roman "아, 그리고…… 그때 말씀드린 글도 조금 더 썼어요."
        # SOURCE CH07 L1254 주인공
        mc "언젠가 보여주신다고 하셨죠."
        # SOURCE CH07 L1257 로만
        # COMMON STANDING BEGIN CH07 L1257
        $ story_stage(faces={"roman": "embarrassed"})
        # COMMON STANDING END CH07 L1257
        roman "네……."
        # SOURCE CH07 L1259 로만
        roman "조금만 더 기다려주세요."
        # SOURCE CH07 L1262 주인공
        mc "그럴게요."
    # SOURCE CH07 L1267 로만
    roman "오늘은…… 책을 어디부터 읽을까요?"
    # SOURCE CH07 L1270 주인공
    mc "로만 씨가 가장 좋아하시는 부분부터요."
    # SOURCE CH07 L1273 로만
    roman "앗,,, 그럼……."
    # SOURCE CH07 L1275 로만
    roman "제가 먼저 읽어드릴까요?"
    # SOURCE CH07 L1278 주인공
    mc "네. 듣고 싶어요."
    # SOURCE CH07 L1282
    narrator "로만은 수줍게 웃으며 첫 장을 펼쳤다."
    # SOURCE CH07 L1284
    narrator "그렇게 새로운 이야기가 시작됐다."
    # CH07 VISUAL 0611 BEGIN ch07_private_roman-end
    $ cg_end(transition=0.35)
    # CH07 VISUAL 0611 END ch07_private_roman-end
    # SOURCE CH07 L1286 [FLAG] `selected_route = roman`
    $ story_flag("selected_route", 'roman')
    # SOURCE CH07 L1288 [FLAG] `roman_route_unlocked = True`
    $ story_flag("roman_route_unlocked", True)
    # CONTI SOURCE CH07 L1290 [RETURN TO SC07]
    jump ch07_sc07

label ch07_sc06_sia:
    $ phone_timeline_enter("CH07", "ch07_sc06_sia")
    # SOURCE CH07 L1293 시아: 장난 아닌 약속
    # SOURCE CH07 L1295 [BG] 캠퍼스 벤치 · 노을
    $ story_draft_scene("캠퍼스 벤치 · 노을")
    # SOURCE CH07 L1297 [BGM] Light Romantic
    $ story_draft_bgm("Light Romantic")
    # SOURCE CH07 L1301
    narrator "시아의 개인 채팅창을 열었다."
    # SOURCE CH07 L1303
    narrator "마지막 메시지는 며칠 전이었다."
    # SOURCE CH07 L1305
    narrator "자기가 만든 이상한 표정의 캐릭터를 보내면서 나를 닮았다고 놀리는 내용이었다."
    # SOURCE CH07 L1307
    narrator "……지금 생각해도 전혀 닮지 않았다."
    # SOURCE CH07 L1309
    narrator "나는 메시지를 입력했다."
    # CONTI SOURCE CH07 L1311 [UI] 시아 개인 메시지
    $ story_chat(True, title="시아")
    # SOURCE CH07 L1314 주인공 · 메시지
    mc "시아 씨, 전에 말씀하신 개인 웹툰 아직 볼 수 있나요?"
    # SOURCE CH07 L1317 시아
    sia "오"
    # SOURCE CH07 L1319 시아
    sia "드디어 감상 담당 출근하는 거냐ㅋㅋ"
    # SOURCE CH07 L1322 주인공 · 메시지
    mc "네. 그런데 웹툰만 보러 가는 건 아니에요."
    # SOURCE CH07 L1325 시아
    sia "?"
    # SOURCE CH07 L1328 주인공 · 메시지
    mc "시아 씨랑도 이야기하고 싶어서요."
    # CONTI SOURCE CH07 L1330 [SFX] 메시지 읽음
    # SOURCE CH07 L1334
    narrator "답장이 바로 오지 않았다."
    # SOURCE CH07 L1336
    narrator "평소 시아라면 이미 이상한 농담을 세 개쯤 보냈을 텐데."
    # CONTI SOURCE CH07 L1338 [SFX] 메시지 도착
    # SOURCE CH07 L1341 시아
    sia "……야"
    # SOURCE CH07 L1343 시아
    sia "그런 말은 예고하고 해라ㅋㅋ"
    # SOURCE CH07 L1345 시아
    sia "아무튼 와"
    # SOURCE CH07 L1347 시아
    sia "작업실에 있음"
    # SOURCE CH07 L1351
    narrator "나도 모르게 웃음이 났다."
    # CONTI SOURCE CH07 L1353 [TRANSITION] 애니메이션학과 작업실 · 오후 6:00
    $ phone_timeline_cue("CH07", "CH07_L1353")
    $ story_chat(False)
    # SOURCE CH07 L1355 [BG] 애니메이션학과 작업실
    $ story_draft_scene("애니메이션학과 작업실", cast=["sia"], standing=True)
    # COMMON STANDING BEGIN CH07 L1355
    $ story_stage_fade_in(["sia"])
    # COMMON STANDING END CH07 L1355
    # SOURCE CH07 L1357 [BGM] Creative Evening
    $ story_draft_bgm("Creative Evening")
    # SOURCE CH07 L1361
    narrator "작업실 문을 열자 시아가 태블릿 앞에 앉아 있었다."
    # SOURCE CH07 L1364 시아
    # COMMON STANDING BEGIN CH07 L1364
    $ story_stage(faces={"sia": "happy"})
    # COMMON STANDING END CH07 L1364
    sia "오, 왔냐?"
    # SOURCE CH07 L1367 주인공
    mc "안녕하세요."
    # SOURCE CH07 L1370 시아
    # COMMON STANDING BEGIN CH07 L1370
    $ story_stage(faces={"sia": "smug"})
    # COMMON STANDING END CH07 L1370
    sia "자, 오늘은 천재 작가님의 특별 시사회다."
    # SOURCE CH07 L1373 주인공
    mc "드디어 보여주시는군요."
    # SOURCE CH07 L1376 시아
    sia "그렇지."
    # SOURCE CH07 L1378 시아
    sia "영광인 줄 알아라."
    # SOURCE CH07 L1381 주인공
    mc "그럼 감상료는 얼마인가요?"
    # SOURCE CH07 L1384 시아
    # COMMON STANDING BEGIN CH07 L1384
    $ story_stage(faces={"sia": "confused"})
    # COMMON STANDING END CH07 L1384
    sia "……."
    # SOURCE CH07 L1386 시아
    sia "야, 그건 내가 너한테 줘야 하는 거 아니냐?"
    # SOURCE CH07 L1389 주인공
    mc "그러네요."
    # SOURCE CH07 L1392 시아
    # COMMON STANDING BEGIN CH07 L1392
    $ story_stage(faces={"sia": "happy"})
    # COMMON STANDING END CH07 L1392
    sia "ㅋㅋㅋ 진짜."
    # SOURCE CH07 L1396
    narrator "시아는 화면을 돌렸다."
    # SOURCE CH07 L1398
    narrator "거기에는 아직 완성되지 않은 짧은 웹툰이 있었다."
    # SOURCE CH07 L1400
    narrator "축제 때 전시했던 작품과는 조금 달랐다."
    # SOURCE CH07 L1402
    narrator "좀 더 긴 이야기였고, 캐릭터들의 표정도 다양했다."
    # SOURCE CH07 L1405 주인공
    mc "오…… 이건 분위기가 조금 다르네요."
    # SOURCE CH07 L1408 시아
    sia "그치?"
    # SOURCE CH07 L1411 시아
    sia "내가 원래 이런 것도 그릴 줄 알거든."
    # SOURCE CH07 L1414 주인공
    mc "캐릭터들이 재미있어요."
    # SOURCE CH07 L1417 시아
    sia "어떤 부분?"
    # SOURCE CH07 L1420 주인공
    mc "둘이 계속 다투는데, 서로가 없으면 이야기가 진행되지 않는다는 점이요."
    # SOURCE CH07 L1423 시아
    sia "……."
    # SOURCE CH07 L1426 시아
    sia "그거 잘 봤네."
    # SOURCE CH07 L1430
    narrator "시아는 잠시 화면을 바라봤다."
    # SOURCE CH07 L1433 시아
    # COMMON STANDING BEGIN CH07 L1433
    $ story_stage(faces={"sia": "serious"})
    # COMMON STANDING END CH07 L1433
    sia "원래 두 캐릭터가 혼자서 다 해결하는 걸로 그리려고 했거든."
    # SOURCE CH07 L1436 주인공
    mc "그런데요?"
    # SOURCE CH07 L1439 시아
    sia "그럼 좀 재미없더라."
    # SOURCE CH07 L1441 시아
    sia "서로 다른 애들이 같이 움직이니까 더 좋았어."
    # SOURCE CH07 L1444 주인공
    mc "저도 그런 이야기가 좋아요."
    # SOURCE CH07 L1447 시아
    sia "……."
    # SOURCE CH07 L1450 시아
    sia "야."
    # SOURCE CH07 L1453 주인공
    mc "네?"
    # SOURCE CH07 L1456 시아
    sia "너는 왜 내가 좋아하는 부분을 잘 알아보냐?"
    # SOURCE CH07 L1459 주인공
    mc "시아 씨가 설명을 잘해주시니까요."
    # SOURCE CH07 L1462 시아
    # COMMON STANDING BEGIN CH07 L1462
    $ story_stage(faces={"sia": "embarrassed"})
    # COMMON STANDING END CH07 L1462
    sia "……아니, 그렇게 말하면 내가 좀……."
    # SOURCE CH07 L1465 주인공
    mc "좀요?"
    # SOURCE CH07 L1468 시아
    sia "……됐다."
    # SOURCE CH07 L1472
    narrator "시아가 시선을 돌렸다."
    # CONTI SOURCE CH07 L1474 [ANIM] 시아의 미소가 작아지며 한 번 눈을 깜빡이는 표정 전환
    # CONTI SOURCE CH07 L1476 [시간 경과 · 오후 6:35]
    $ phone_timeline_cue("CH07", "CH07_L1476")
    # SOURCE CH07 L1480
    narrator "우리는 작업실에 앉아 이런저런 이야기를 나눴다."
    # SOURCE CH07 L1482
    narrator "시아는 요즘 그리고 싶은 작품이 많다고 했다."
    # SOURCE CH07 L1484
    narrator "하지만 실제로 완성하려면 생각보다 시간이 오래 걸린다고도 했다."
    # SOURCE CH07 L1487 시아
    # COMMON STANDING BEGIN CH07 L1487
    $ story_stage(faces={"sia": "serious"})
    # COMMON STANDING END CH07 L1487
    sia "야, 근데 진짜."
    # SOURCE CH07 L1489 시아
    sia "너 없었으면 이 만화 계속 그리고 있었을까?"
    # SOURCE CH07 L1492 주인공
    mc "왜 그렇게 생각하세요?"
    # SOURCE CH07 L1495 시아
    sia "그냥."
    # SOURCE CH07 L1497 시아
    sia "전에 네가 내 그림 좋다고 해준 거 있잖아."
    # SOURCE CH07 L1499 시아
    sia "그때 좀 힘이 났거든."
    # SOURCE CH07 L1502 주인공
    mc "저는 그냥 제가 좋았던 부분을 말씀드린 건데요."
    # SOURCE CH07 L1505 시아
    sia "알아."
    # SOURCE CH07 L1508 시아
    # COMMON STANDING BEGIN CH07 L1508
    $ story_stage(faces={"sia": "happy"})
    # COMMON STANDING END CH07 L1508
    sia "그래서 더 좋았어."
    # SOURCE CH07 L1512
    narrator "시아는 잠시 웃었다."
    # SOURCE CH07 L1515 시아
    sia "근데 너 오늘 진짜 웹툰 보려고 온 거 맞냐?"
    # SOURCE CH07 L1518 주인공
    mc "네. 그것도 맞아요."
    # SOURCE CH07 L1521 시아
    sia "그것도?"
    # SOURCE CH07 L1524 주인공
    mc "시아 씨 보고 싶어서 온 것도 맞고요."
    # SOURCE CH07 L1527 시아
    sia "……."
    # SOURCE CH07 L1531
    # CH07 VISUAL 0611 BEGIN ch07_private_sia-start
    $ cg_start("ch07_private_sia", transition=0.35)
    # CH07 VISUAL 0611 END ch07_private_sia-start
    narrator "시아의 펜이 멈췄다."
    # SOURCE CH07 L1534 시아
    sia "야."
    # SOURCE CH07 L1537 주인공
    mc "네?"
    # SOURCE CH07 L1540 시아
    # COMMON STANDING BEGIN CH07 L1540
    $ story_stage(faces={"sia": "embarrassed"})
    # COMMON STANDING END CH07 L1540
    sia "너 그런 말 자꾸 하면……."
    # SOURCE CH07 L1543 주인공
    mc "하면요?"
    # SOURCE CH07 L1546 시아
    sia "……."
    # SOURCE CH07 L1549 시아
    sia "내가 장난을 못 치잖아."
    # SOURCE CH07 L1552 주인공
    mc "안 치셔도 괜찮아요."
    # SOURCE CH07 L1555 시아
    sia "……그게 더 문제거든."
    # SOURCE CH07 L1559
    narrator "시아는 조용히 웃었다."
    # SOURCE CH07 L1561
    narrator "그런데 이번에는 평소처럼 크게 웃지는 않았다."
    # CH07 VISUAL 0611 BEGIN ch07_private_sia-end
    $ cg_end(transition=0.35)
    # CH07 VISUAL 0611 END ch07_private_sia-end
    # SOURCE CH07 L1564 시아
    sia "야, 다음에도 와라."
    # SOURCE CH07 L1567 주인공
    mc "작업실에요?"
    # SOURCE CH07 L1570 시아
    sia "응."
    # SOURCE CH07 L1572 시아
    sia "아니, 꼭 작업실 아니어도 되고."
    # SOURCE CH07 L1574 시아
    sia "밥 먹어도 되고, 그냥 놀아도 되고."
    # SOURCE CH07 L1577 시아
    sia "……."
    # SOURCE CH07 L1579 시아
    sia "그냥 너랑 있으면 재미있거든."
    # SOURCE CH07 L1582 주인공
    mc "저도 그래요."
    # SOURCE CH07 L1585 시아
    sia "……."
    # SOURCE CH07 L1587 시아
    sia "그럼 약속이다."
    # SOURCE CH07 L1590 주인공
    mc "네. 약속할게요."
    # SOURCE CH07 L1592 [CONDITION] `ch04_partner == "sia"`
    if story_id(ch04_partner) == "sia":
        # SOURCE CH07 L1595 시아
        sia "근데 너 기억하냐?"
        # SOURCE CH07 L1597 시아
        sia "내가 전에 장난으로 하지 말라고 했던 거."
        # SOURCE CH07 L1600 주인공
        mc "네. 기억해요."
        # SOURCE CH07 L1603 시아
        # COMMON STANDING BEGIN CH07 L1603
        $ story_stage(faces={"sia": "serious"})
        # COMMON STANDING END CH07 L1603
        sia "……오늘은 나도 장난 아니야."
    # SOURCE CH07 L1609
    narrator "시아는 다시 태블릿을 켰다."
    # SOURCE CH07 L1612 시아
    # COMMON STANDING BEGIN CH07 L1612
    $ story_stage(faces={"sia": "happy"})
    # COMMON STANDING END CH07 L1612
    sia "자, 그럼 다음 장면도 보여줄까?"
    # SOURCE CH07 L1615 주인공
    mc "좋아요."
    # SOURCE CH07 L1618 시아
    sia "대신 이번에도 솔직하게 감상해라."
    # SOURCE CH07 L1621 주인공
    mc "그럼요. 감상 담당이잖아요."
    # SOURCE CH07 L1624 시아
    sia "ㅋㅋㅋ 맞네."
    # SOURCE CH07 L1628
    narrator "나는 시아의 옆에 앉았다."
    # SOURCE CH07 L1630
    narrator "그림 속 이야기는 아직 끝나지 않았다."
    # SOURCE CH07 L1632
    narrator "우리 사이의 이야기도 마찬가지였다."
    # SOURCE CH07 L1634 [FLAG] `selected_route = sia`
    $ story_flag("selected_route", 'sia')
    # SOURCE CH07 L1636 [FLAG] `sia_route_unlocked = True`
    $ story_flag("sia_route_unlocked", True)
    # CONTI SOURCE CH07 L1638 [RETURN TO SC07]
    jump ch07_sc07

label ch07_sc06_darim:
    $ phone_timeline_enter("CH07", "ch07_sc06_darim")
    # SOURCE CH07 L1640 다림: 선배, 이번에는 제가 먼저요
    # SOURCE CH07 L1642 [BG] 캠퍼스 벤치 · 노을
    $ story_draft_scene("캠퍼스 벤치 · 노을")
    # SOURCE CH07 L1644 [BGM] Gentle Afternoon
    $ story_draft_bgm("Gentle Afternoon")
    # SOURCE CH07 L1648
    narrator "다림 선배에게 메시지를 보내기로 했다."
    # SOURCE CH07 L1650
    narrator "축제 기간에는 항상 선배가 일정을 정리하고 먼저 연락하는 경우가 많았다."
    # SOURCE CH07 L1652
    narrator "이번에는 내가 먼저 약속을 잡아보고 싶었다."
    # CONTI SOURCE CH07 L1654 [UI] 다림 개인 메시지
    $ story_chat(True, title="다림")
    # SOURCE CH07 L1657 주인공 · 메시지
    mc "선배, 혹시 오늘 저녁 시간 괜찮으세요?"
    # SOURCE CH07 L1660 다림
    darim "네. 오늘은 조금 여유 있어요."
    # SOURCE CH07 L1662 다림
    darim "무슨 일이세요?"
    # SOURCE CH07 L1665 주인공 · 메시지
    mc "전에 말씀하신 게임 카페 같이 가실래요?"
    # SOURCE CH07 L1668 다림
    darim "어머."
    # SOURCE CH07 L1670 다림
    darim "후후. 드디어 승부 신청이 들어왔네요."
    # SOURCE CH07 L1673 주인공 · 메시지
    mc "이번에는 제가 먼저 신청해보고 싶었어요."
    # SOURCE CH07 L1676 다림
    darim "좋아요. 그럼 저도 준비할게요."
    # SOURCE CH07 L1680
    narrator "예상대로였다."
    # SOURCE CH07 L1682
    narrator "선배는 역시 승부를 피하지 않는다."
    # CONTI SOURCE CH07 L1684 [TRANSITION] 학교 근처 게임 카페 · 오후 6:10
    $ phone_timeline_cue("CH07", "CH07_L1684")
    $ story_chat(False)
    # SOURCE CH07 L1686 [BG] 게임 카페
    $ story_draft_scene("게임 카페", cast=["darim"], standing=True)
    # COMMON STANDING BEGIN CH07 L1686
    $ story_stage_fade_in(["darim"])
    # COMMON STANDING END CH07 L1686
    # SOURCE CH07 L1688 [BGM] Playful Game
    $ story_draft_bgm("Playful Game")
    # SOURCE CH07 L1692
    narrator "다림 선배는 이미 게임 목록을 살펴보고 있었다."
    # SOURCE CH07 L1695 다림
    # COMMON STANDING BEGIN CH07 L1695
    $ story_stage(faces={"darim": "happy"})
    # COMMON STANDING END CH07 L1695
    darim "[player_name] 씨, 여기예요."
    # SOURCE CH07 L1698 주인공
    mc "많이 기다리셨어요?"
    # SOURCE CH07 L1701 다림
    darim "아니에요. 어떤 게임 할지 보고 있었어요."
    # SOURCE CH07 L1704 주인공
    mc "오늘도 진지하시네요."
    # SOURCE CH07 L1707 다림
    darim "후후. 그럼요."
    # SOURCE CH07 L1709 다림
    # COMMON STANDING BEGIN CH07 L1709
    $ story_stage(faces={"darim": "smug"})
    # COMMON STANDING END CH07 L1709
    darim "오늘은 제가 질 생각이 없거든요."
    # SOURCE CH07 L1712 주인공
    mc "저도요."
    # SOURCE CH07 L1716
    narrator "우리는 대결 게임 하나를 선택했다."
    # SOURCE CH07 L1718
    narrator "처음에는 서로 규칙을 설명해주며 느긋하게 시작했는데."
    # SOURCE CH07 L1720
    narrator "몇 분 뒤에는 분위기가 완전히 달라졌다."
    # CONTI SOURCE CH07 L1722 [SFX] 게임 승리 효과음
    # SOURCE CH07 L1725 다림
    # COMMON STANDING BEGIN CH07 L1725
    $ story_stage(faces={"darim": "surprised"})
    # COMMON STANDING END CH07 L1725
    darim "……어?"
    # SOURCE CH07 L1728 주인공
    mc "제가 이겼네요."
    # SOURCE CH07 L1731 다림
    darim "……."
    # SOURCE CH07 L1733 다림
    # COMMON STANDING BEGIN CH07 L1733
    $ story_stage(faces={"darim": "serious"})
    # COMMON STANDING END CH07 L1733
    darim "한 판만 더 할까요?"
    # SOURCE CH07 L1736 주인공
    mc "선배, 벌써 세 번째인데요?"
    # SOURCE CH07 L1739 다림
    darim "네."
    # SOURCE CH07 L1741 다림
    darim "그러니까 네 번째는 이겨야죠."
    # SOURCE CH07 L1745
    narrator "……정말 승부욕이 대단하다."
    # SOURCE CH07 L1747
    narrator "결국 나도 웃음을 터뜨렸다."
    # CONTI SOURCE CH07 L1749 [시간 경과 · 오후 6:45]
    $ phone_timeline_cue("CH07", "CH07_L1749")
    # SOURCE CH07 L1751 [BG] 게임 카페 테이블
    $ story_draft_scene("게임 카페 테이블", cast=["darim"], standing=True)
    # COMMON STANDING BEGIN CH07 L1751
    $ story_stage_fade_in(["darim"])
    # COMMON STANDING END CH07 L1751
    # SOURCE CH07 L1755
    narrator "몇 번의 승부 끝에 우리는 음료를 마시며 쉬었다."
    # SOURCE CH07 L1758 다림
    # COMMON STANDING BEGIN CH07 L1758
    $ story_stage(faces={"darim": "happy"})
    # COMMON STANDING END CH07 L1758
    # CH07 VISUAL 0611 BEGIN ch07_private_darim-start
    $ cg_start("ch07_private_darim", transition=0.35)
    # CH07 VISUAL 0611 END ch07_private_darim-start
    darim "후후. 재미있었어요."
    # SOURCE CH07 L1761 주인공
    mc "저도요."
    # SOURCE CH07 L1764 다림
    darim "그런데 오늘은 무슨 바람이 불어서 먼저 연락하셨어요?"
    # SOURCE CH07 L1767 주인공
    mc "그냥 선배랑 같이 놀고 싶었어요."
    # SOURCE CH07 L1770 다림
    darim "……."
    # SOURCE CH07 L1773 다림
    # COMMON STANDING BEGIN CH07 L1773
    $ story_stage(faces={"darim": "surprised"})
    # COMMON STANDING END CH07 L1773
    darim "……아."
    # SOURCE CH07 L1777
    narrator "다림 선배가 살짝 놀란 표정을 지었다."
    # SOURCE CH07 L1780 주인공
    mc "축제 준비할 때는 늘 할 일이 있었잖아요."
    # SOURCE CH07 L1783 다림
    darim "그렇죠."
    # SOURCE CH07 L1786 주인공
    mc "이제는 그런 이유가 없어도 선배랑 만나고 싶어서요."
    # SOURCE CH07 L1789 다림
    darim "……."
    # CONTI SOURCE CH07 L1791 [ANIM] 다림의 눈 깜빡임 후 부드러운 미소
    # SOURCE CH07 L1794 다림
    # COMMON STANDING BEGIN CH07 L1794
    $ story_stage(faces={"darim": "happy"})
    # COMMON STANDING END CH07 L1794
    darim "……후후."
    # SOURCE CH07 L1796 다림
    darim "그런 말씀을 들으니까 기분이 좋네요."
    # SOURCE CH07 L1799 주인공
    mc "저도 만나니까 좋네요."
    # SOURCE CH07 L1802 다림
    darim "……."
    # SOURCE CH07 L1805 다림
    darim "사실 저도 비슷한 생각을 했어요."
    # SOURCE CH07 L1808 주인공
    mc "어떤 생각이요?"
    # SOURCE CH07 L1811 다림
    darim "축제 때는 다 같이 모일 이유가 있었는데."
    # SOURCE CH07 L1813 다림
    # COMMON STANDING BEGIN CH07 L1813
    $ story_stage(faces={"darim": "sad"})
    # COMMON STANDING END CH07 L1813
    darim "끝나고 나니까 조금 아쉽더라고요."
    # SOURCE CH07 L1816 다림
    darim "그런데 오늘 먼저 연락해 주셔서……."
    # SOURCE CH07 L1818 다림
    # COMMON STANDING BEGIN CH07 L1818
    $ story_stage(faces={"darim": "happy"})
    # COMMON STANDING END CH07 L1818
    darim "조금 기뻤어요."
    # SOURCE CH07 L1822
    narrator "다림 선배는 웃었다."
    # SOURCE CH07 L1824
    narrator "그 미소가 평소보다 조금 더 편안해 보였다."
    # SOURCE CH07 L1827 다림
    darim "앞으로도 가끔 이렇게 만나면 좋겠어요."
    # SOURCE CH07 L1830 주인공
    mc "좋아요."
    # SOURCE CH07 L1833 다림
    darim "다음에는 게임 말고 다른 것도 해봐요."
    # SOURCE CH07 L1836 주인공
    mc "선배가 하고 싶은 걸로요?"
    # SOURCE CH07 L1839 다림
    darim "후후. 같이 정해봐요."
    # SOURCE CH07 L1843
    narrator "같이 정하자는 말이 마음에 남았다."
    # SOURCE CH07 L1845
    narrator "선배는 늘 다른 사람을 챙기는 사람이었다."
    # SOURCE CH07 L1847
    narrator "그런데 이제는 내가 선배의 시간 속에 조금 더 자연스럽게 들어가는 기분이었다."
    # SOURCE CH07 L1849 [CONDITION] `ch04_partner == "darim"`
    if story_id(ch04_partner) == "darim":
        # SOURCE CH07 L1852 다림
        darim "기억하세요?"
        # SOURCE CH07 L1854 다림
        darim "예전에 제가 가끔은 도움을 받아도 괜찮겠다고 했던 거."
        # SOURCE CH07 L1857 주인공
        mc "네. 기억해요."
        # SOURCE CH07 L1860 다림
        darim "오늘은……."
        # SOURCE CH07 L1862 다림
        # COMMON STANDING BEGIN CH07 L1862
        $ story_stage(faces={"darim": "embarrassed"})
        # COMMON STANDING END CH07 L1862
        darim "먼저 만나자고 말씀해주신 게 정말 좋았어요."
        # SOURCE CH07 L1865 다림
        darim "가끔은 누가 저를 먼저 찾아주는 것도 좋네요."
    # SOURCE CH07 L1870 주인공
    mc "그럼 다음에도 제가 먼저 연락드릴게요."
    # SOURCE CH07 L1873 다림
    # COMMON STANDING BEGIN CH07 L1873
    $ story_stage(faces={"darim": "happy"})
    # COMMON STANDING END CH07 L1873
    darim "후후. 좋아요."
    # SOURCE CH07 L1875 다림
    darim "하지만 저도 먼저 연락할 거예요."
    # SOURCE CH07 L1878 주인공
    mc "그럼 누가 먼저 연락하나 승부인가요?"
    # SOURCE CH07 L1881 다림
    darim "……어머."
    # SOURCE CH07 L1883 다림
    darim "그것도 재미있겠네요."
    # SOURCE CH07 L1887
    narrator "나는 웃었다."
    # SOURCE CH07 L1889
    narrator "선배와 있으면 평범한 대화도 어느새 작은 게임이 된다."
    # SOURCE CH07 L1891
    narrator "그런 시간을 앞으로도 더 보내고 싶었다."
    # CH07 VISUAL 0611 BEGIN ch07_private_darim-end
    $ cg_end(transition=0.35)
    # CH07 VISUAL 0611 END ch07_private_darim-end
    # SOURCE CH07 L1893 [FLAG] `selected_route = darim`
    $ story_flag("selected_route", 'darim')
    # SOURCE CH07 L1895 [FLAG] `darim_route_unlocked = True`
    $ story_flag("darim_route_unlocked", True)
    # CONTI SOURCE CH07 L1897 [RETURN TO SC07]
    jump ch07_sc07

label ch07_sc06_omu:
    $ phone_timeline_enter("CH07", "ch07_sc06_omu")
    # SOURCE CH07 L1899 오므: 사진 밖에서도 함께
    # SOURCE CH07 L1901 [BG] 캠퍼스 벤치 · 노을
    $ story_draft_scene("캠퍼스 벤치 · 노을")
    # SOURCE CH07 L1903 [BGM] Soft Photography
    $ story_draft_bgm("Soft Photography")
    # SOURCE CH07 L1907
    narrator "오므의 채팅창을 열었다."
    # SOURCE CH07 L1909
    narrator "마지막으로 받은 건 축제 때 함께 찍었던 사진이었다."
    # SOURCE CH07 L1911
    narrator "사진 아래에는 짧은 메시지가 남아 있었다."
    # SOURCE CH07 L1913
    narrator "「잘 나왔네ㅋㅋ」"
    # SOURCE CH07 L1915
    narrator "나는 사진을 다시 바라봤다."
    # SOURCE CH07 L1917
    narrator "그러고는 메시지를 입력했다."
    # CONTI SOURCE CH07 L1919 [UI] 오므 개인 메시지
    $ story_chat(True, title="오므")
    # SOURCE CH07 L1922 주인공 · 메시지
    mc "오므 씨, 오늘 시간 괜찮으세요?"
    # SOURCE CH07 L1925 오므
    omu "어 왜?"
    # SOURCE CH07 L1928 주인공 · 메시지
    mc "전에 말씀하신 학교 밖 사진 촬영, 오늘 가볼까요?"
    # SOURCE CH07 L1931 오므
    omu "오"
    # SOURCE CH07 L1933 오므
    omu "니가 먼저 연락했네"
    # SOURCE CH07 L1936 주인공 · 메시지
    mc "네. 같이 가고 싶어서요."
    # SOURCE CH07 L1939 오므
    omu "……."
    # SOURCE CH07 L1941 오므
    omu "좋지"
    # SOURCE CH07 L1943 오므
    omu "오늘 날씨도 괜찮고"
    # SOURCE CH07 L1946 오므
    omu "그럼 강변 쪽에서 보자"
    # SOURCE CH07 L1950
    narrator "약속을 잡자마자 기분이 조금 좋아졌다."
    # CONTI SOURCE CH07 L1952 [TRANSITION] 강변 산책로 · 오후 6:00
    $ phone_timeline_cue("CH07", "CH07_L1952")
    $ story_chat(False)
    # SOURCE CH07 L1954 [BG] 강변 산책로 · 저녁
    $ story_draft_scene("강변 산책로 · 저녁", cast=["omu"], standing=True)
    # COMMON STANDING BEGIN CH07 L1954
    $ story_stage_fade_in(["omu"])
    # COMMON STANDING END CH07 L1954
    # SOURCE CH07 L1956 [BGM] Gentle Sunset
    $ story_draft_bgm("Gentle Sunset")
    # SOURCE CH07 L1960
    narrator "강변에 도착하자 오므가 카메라를 들고 서 있었다."
    # SOURCE CH07 L1963 오므
    # COMMON STANDING BEGIN CH07 L1963
    $ story_stage(faces={"omu": "happy"})
    # COMMON STANDING END CH07 L1963
    omu "어. 왔나?"
    # SOURCE CH07 L1966 주인공
    mc "네. 많이 기다리셨어요?"
    # SOURCE CH07 L1969 오므
    omu "아니다. 나도 방금 왔다."
    # SOURCE CH07 L1972 주인공
    mc "오늘은 어떤 사진 찍으실 거예요?"
    # SOURCE CH07 L1975 오므
    omu "글쎄."
    # SOURCE CH07 L1977 오므
    omu "일단 걸어보자."
    # SOURCE CH07 L1981
    narrator "우리는 천천히 강변을 걸었다."
    # SOURCE CH07 L1983
    narrator "물 위로 해가 비치고 있었고, 길가에는 가을빛이 조금 남아 있었다."
    # SOURCE CH07 L1986 주인공
    mc "오므 씨는 이런 곳을 어떻게 찾으세요?"
    # SOURCE CH07 L1989 오므
    omu "그냥 돌아다니다 보니까."
    # SOURCE CH07 L1991 오므
    omu "사진 찍을 만한 데 찾아보는 게 재미있잖아."
    # SOURCE CH07 L1994 주인공
    mc "그렇군요."
    # SOURCE CH07 L1997 오므
    omu "근데 오늘은 사진만 찍으러 온 건 아이다."
    # SOURCE CH07 L2000 주인공
    mc "네?"
    # SOURCE CH07 L2003 오므
    omu "……."
    # SOURCE CH07 L2005 오므
    # COMMON STANDING BEGIN CH07 L2005
    $ story_stage(faces={"omu": "embarrassed"})
    # COMMON STANDING END CH07 L2005
    omu "아니, 뭐."
    # SOURCE CH07 L2007 오므
    omu "그냥 같이 걸어도 괜찮잖아."
    # SOURCE CH07 L2011
    narrator "오므는 카메라를 고쳐 멨다."
    # SOURCE CH07 L2014 주인공
    mc "그렇죠. 저도 오므 씨랑 같이 걷고 싶어서 왔어요."
    # SOURCE CH07 L2017 오므
    omu "……."
    # SOURCE CH07 L2020 오므
    omu "니 그런 말 참 아무렇지도 않게 한다."
    # SOURCE CH07 L2023 주인공
    mc "아닌가요?"
    # SOURCE CH07 L2026 오므
    omu "아니다."
    # SOURCE CH07 L2028 오므
    # COMMON STANDING BEGIN CH07 L2028
    $ story_stage(faces={"omu": "happy"})
    # COMMON STANDING END CH07 L2028
    omu "……좋다."
    # CONTI SOURCE CH07 L2030 [ANIM] 오므가 살짝 시선을 피했다가 다시 바라보는 표정 전환
    # CONTI SOURCE CH07 L2032 [시간 경과 · 오후 6:35]
    $ phone_timeline_cue("CH07", "CH07_L2032")
    # SOURCE CH07 L2034 [BG] 강변 벤치 · 노을
    $ story_draft_scene("강변 벤치 · 노을", cast=["omu"], standing=True)
    # COMMON STANDING BEGIN CH07 L2034
    $ story_stage_fade_in(["omu"])
    # COMMON STANDING END CH07 L2034
    # SOURCE CH07 L2038
    # CH07 VISUAL 0611 BEGIN ch07_private_omu-start
    $ cg_start("ch07_private_omu", transition=0.35)
    # CH07 VISUAL 0611 END ch07_private_omu-start
    narrator "우리는 벤치에 앉았다."
    # SOURCE CH07 L2040
    narrator "오므는 그동안 찍은 사진을 몇 장 보여줬다."
    # SOURCE CH07 L2042
    narrator "축제 당일 사진도 있었고, 처음 준비하던 시절의 사진도 있었다."
    # SOURCE CH07 L2045 오므
    omu "이거 기억하나?"
    # SOURCE CH07 L2048 주인공
    mc "네. CH04 때 같이 골랐던 사진이네요."
    # SOURCE CH07 L2051 오므
    omu "어."
    # SOURCE CH07 L2053 오므
    omu "그때 니랑 의견 달랐잖아."
    # SOURCE CH07 L2056 주인공
    mc "그랬죠."
    # SOURCE CH07 L2059 오므
    # COMMON STANDING BEGIN CH07 L2059
    $ story_stage(faces={"omu": "happy"})
    # COMMON STANDING END CH07 L2059
    omu "근데 생각해보면 그런 것도 재미있었다."
    # SOURCE CH07 L2062 주인공
    mc "왜요?"
    # SOURCE CH07 L2065 오므
    omu "그냥."
    # SOURCE CH07 L2067 오므
    omu "니랑 이야기하면 내가 못 봤던 것도 보이거든."
    # SOURCE CH07 L2071
    narrator "오므는 사진을 넘겼다."
    # SOURCE CH07 L2074 오므
    omu "그리고 이건 축제 때 같이 찍은 거."
    # SOURCE CH07 L2077 주인공
    mc "잘 나왔네요."
    # SOURCE CH07 L2080 오므
    omu "어."
    # SOURCE CH07 L2083 오므
    omu "이거 내가 되게 좋아한다."
    # SOURCE CH07 L2086 주인공
    mc "어떤 점이요?"
    # SOURCE CH07 L2089 오므
    omu "……."
    # SOURCE CH07 L2091 오므
    omu "내가 사진 안에 있잖아."
    # SOURCE CH07 L2095
    narrator "오므는 조용히 웃었다."
    # SOURCE CH07 L2098 오므
    omu "평소에는 찍는 쪽이라서."
    # SOURCE CH07 L2100 오므
    # COMMON STANDING BEGIN CH07 L2100
    $ story_stage(faces={"omu": "embarrassed"})
    # COMMON STANDING END CH07 L2100
    omu "누가 나랑 같이 사진 찍자고 하면 좀 어색하거든."
    # SOURCE CH07 L2103 주인공
    mc "그런데 그때는 같이 찍자고 하셨잖아요."
    # SOURCE CH07 L2106 오므
    omu "그랬지."
    # SOURCE CH07 L2109 오므
    omu "……니랑은 같이 찍고 싶었거든."
    # SOURCE CH07 L2113
    narrator "잠깐 바람이 불었다."
    # SOURCE CH07 L2115
    narrator "오므는 머리카락을 귀 뒤로 넘겼다."
    # SOURCE CH07 L2118 주인공
    mc "저도 그 사진 좋아해요."
    # SOURCE CH07 L2121 오므
    omu "……어."
    # SOURCE CH07 L2124 오므
    # COMMON STANDING BEGIN CH07 L2124
    $ story_stage(faces={"omu": "happy"})
    # COMMON STANDING END CH07 L2124
    omu "그럼 다행이네."
    # SOURCE CH07 L2128
    narrator "우리는 잠시 말없이 강변을 바라봤다."
    # SOURCE CH07 L2130
    narrator "카메라 셔터 소리는 들리지 않았다."
    # SOURCE CH07 L2132
    narrator "그런데 조금도 어색하지 않았다."
    # CH07 VISUAL 0611 BEGIN ch07_private_omu-end
    $ cg_end(transition=0.35)
    # CH07 VISUAL 0611 END ch07_private_omu-end
    # SOURCE CH07 L2135 오므
    omu "야."
    # SOURCE CH07 L2138 주인공
    mc "네?"
    # SOURCE CH07 L2141 오므
    omu "다음에도 같이 올래?"
    # SOURCE CH07 L2144 주인공
    mc "사진 찍으러요?"
    # SOURCE CH07 L2147 오므
    omu "그것도 좋고."
    # SOURCE CH07 L2149 오므
    omu "그냥 걸어도 좋고."
    # SOURCE CH07 L2152 오므
    omu "영화 봐도 되고."
    # SOURCE CH07 L2155 주인공
    mc "좋아요. 저도 그러고 싶어요."
    # SOURCE CH07 L2158 오므
    omu "……."
    # SOURCE CH07 L2160 오므
    omu "그럼 약속이다."
    # SOURCE CH07 L2162 [CONDITION] `ch04_partner == "omu"`
    if story_id(ch04_partner) == "omu":
        # SOURCE CH07 L2165 주인공
        mc "지난번에도 학교 밖에서 같이 찍자고 하셨잖아요."
        # SOURCE CH07 L2168 오므
        omu "어. 오늘 지켰네."
        # SOURCE CH07 L2171 주인공
        mc "그러게요."
        # SOURCE CH07 L2174 오므
        omu "근데……."
        # SOURCE CH07 L2176 오므
        omu "한 번으로 끝내기는 좀 아쉽다."
    # SOURCE CH07 L2182
    narrator "오므는 다시 카메라를 들었다."
    # SOURCE CH07 L2185 오므
    omu "자, 오늘 마지막으로 하나만 찍자."
    # SOURCE CH07 L2188 주인공
    mc "좋아요."
    # SOURCE CH07 L2191 오므
    # COMMON STANDING BEGIN CH07 L2191
    $ story_stage(faces={"omu": "embarrassed"})
    # COMMON STANDING END CH07 L2191
    omu "근데 이번에는……."
    # SOURCE CH07 L2193 오므
    omu "니도 같이."
    # SOURCE CH07 L2197
    narrator "나는 오므의 옆으로 다가갔다."
    # SOURCE CH07 L2199
    narrator "두 사람의 그림자가 강변 바닥에 길게 드리워졌다."
    # CONTI SOURCE CH07 L2201 [SFX] 카메라 셔터
    # SOURCE CH07 L2205
    narrator "사진 한 장이 더 남았다."
    # SOURCE CH07 L2207
    narrator "하지만 오늘 가장 기억에 남을 건 사진 속 풍경만은 아닐 것 같았다."
    # SOURCE CH07 L2209 [FLAG] `selected_route = omu`
    $ story_flag("selected_route", 'omu')
    # SOURCE CH07 L2211 [FLAG] `omu_route_unlocked = True`
    $ story_flag("omu_route_unlocked", True)
    # CONTI SOURCE CH07 L2213 [RETURN TO SC07]
    jump ch07_sc07

label ch07_sc06_lumi:
    $ phone_timeline_enter("CH07", "ch07_sc06_lumi")
    # SOURCE CH07 L2216 하린: 계획에 없던 다음 약속
    # SOURCE CH07 L2218 [BG] 캠퍼스 벤치 · 노을
    $ story_draft_scene("캠퍼스 벤치 · 노을")
    # SOURCE CH07 L2220 [BGM] Calm Romance
    $ story_draft_bgm("Calm Romance")
    # SOURCE CH07 L2224
    narrator "하린 선배의 채팅창을 열었다."
    # SOURCE CH07 L2226
    narrator "축제 준비가 끝난 뒤에도 선배는 가끔 작업실 사진을 보내줬다."
    # SOURCE CH07 L2228
    narrator "새로 만드는 모형이나 설계도 이야기였다."
    # SOURCE CH07 L2230
    narrator "그런데 요즘은 그 사진보다도 선배가 무슨 일을 하고 있는지 궁금했다."
    # SOURCE CH07 L2232
    narrator "나는 메시지를 입력했다."
    # CONTI SOURCE CH07 L2234 [UI] 하린 개인 메시지
    $ story_chat(True, title="하린")
    # SOURCE CH07 L2237 주인공 · 메시지
    mc "하린 선배, 혹시 오늘 작업실에 계세요?"
    # SOURCE CH07 L2240 하린
    lumi "네. 아직 작업하고 있어요."
    # SOURCE CH07 L2242 하린
    lumi "무슨 일이에요?"
    # SOURCE CH07 L2245 주인공 · 메시지
    mc "잠깐 찾아가도 될까요?"
    # SOURCE CH07 L2248 하린
    lumi "후후. 무슨 일이길래요?"
    # SOURCE CH07 L2251 주인공 · 메시지
    mc "그냥 선배 보고 싶어서요."
    # CONTI SOURCE CH07 L2253 [SFX] 읽음 표시
    # SOURCE CH07 L2257
    narrator "답장이 바로 오지 않았다."
    # SOURCE CH07 L2259
    narrator "……너무 갑작스러웠나?"
    # CONTI SOURCE CH07 L2261 [SFX] 메시지 도착
    # SOURCE CH07 L2264 하린
    lumi "……."
    # SOURCE CH07 L2266 하린
    lumi "그런 말은 조금 예고하고 하시면 안 될까요?"
    # SOURCE CH07 L2269 주인공 · 메시지
    mc "혹시 지금 바쁘세요?"
    # SOURCE CH07 L2272 하린
    lumi "아니에요."
    # SOURCE CH07 L2274 하린
    lumi "와도 돼요."
    # SOURCE CH07 L2276 하린
    lumi "……나도 보고 싶었으니까."
    # SOURCE CH07 L2280
    narrator "나는 잠시 화면을 바라봤다."
    # SOURCE CH07 L2282
    narrator "마지막 문장을 두 번쯤 읽었다."
    # SOURCE CH07 L2284
    narrator "……선배도?"
    # CONTI SOURCE CH07 L2286 [TRANSITION] 건축학과 작업실 · 오후 6:10
    $ phone_timeline_cue("CH07", "CH07_L2286")
    $ story_chat(False)
    # SOURCE CH07 L2288 [BG] 건축학과 작업실
    $ story_draft_scene("건축학과 작업실", cast=["lumi"], standing=True)
    # COMMON STANDING BEGIN CH07 L2288
    $ story_stage_fade_in(["lumi"])
    # COMMON STANDING END CH07 L2288
    # SOURCE CH07 L2290 [BGM] Warm Workshop
    $ story_draft_bgm("Warm Workshop")
    # CONTI SOURCE CH07 L2292 [ANIM] 하린 · 눈 깜빡임, 미세 호흡
    # SOURCE CH07 L2296
    narrator "작업실 문을 열자 하린 선배가 책상 앞에 앉아 있었다."
    # SOURCE CH07 L2298
    narrator "책상에는 새로운 설계도와 작은 모형이 놓여 있었다."
    # SOURCE CH07 L2301 하린
    # COMMON STANDING BEGIN CH07 L2301
    $ story_stage(faces={"lumi": "happy"})
    # COMMON STANDING END CH07 L2301
    lumi "왔어요?"
    # SOURCE CH07 L2304 주인공
    mc "네. 안녕하세요, 선배."
    # SOURCE CH07 L2307 하린
    lumi "후후. 오늘은 축제 자료도 없는데."
    # SOURCE CH07 L2309 하린
    lumi "여기까지 오신 이유가 정말 그거예요?"
    # SOURCE CH07 L2312 주인공
    mc "어떤 거요?"
    # SOURCE CH07 L2315 하린
    # COMMON STANDING BEGIN CH07 L2315
    $ story_stage(faces={"lumi": "embarrassed"})
    # COMMON STANDING END CH07 L2315
    lumi "……저 보고 싶어서 왔다고 하신 거."
    # SOURCE CH07 L2318 주인공
    mc "네. 맞아요."
    # SOURCE CH07 L2321 하린
    lumi "……."
    # SOURCE CH07 L2325
    narrator "하린 선배가 잠시 말을 멈췄다."
    # SOURCE CH07 L2328 하린
    lumi "……진짜."
    # SOURCE CH07 L2330 하린
    lumi "당신은 가끔 너무 예측이 안 돼."
    # SOURCE CH07 L2333 주인공
    mc "제가요?"
    # SOURCE CH07 L2336 하린
    lumi "네."
    # SOURCE CH07 L2338 하린
    lumi "그런 말을 아무렇지도 않게 하니까."
    # SOURCE CH07 L2341 주인공
    mc "그런데 선배도 보고 싶으셨다고 하셨잖아요."
    # SOURCE CH07 L2344 하린
    lumi "……."
    # SOURCE CH07 L2347 하린
    lumi "그건……."
    # SOURCE CH07 L2351
    narrator "하린 선배는 시선을 돌렸다."
    # CONTI SOURCE CH07 L2353 [ANIM] 하린의 시선 회피, 옅은 홍조 표정
    # SOURCE CH07 L2356 하린
    lumi "……맞아요."
    # SOURCE CH07 L2359 주인공
    mc "그럼 다행이네요."
    # SOURCE CH07 L2362 하린
    lumi "……다행이요?"
    # SOURCE CH07 L2365 주인공
    mc "저만 보고 싶었던 건 아니라서요."
    # SOURCE CH07 L2368 하린
    lumi "……."
    # SOURCE CH07 L2371 하린
    # COMMON STANDING BEGIN CH07 L2371
    $ story_stage(faces={"lumi": "happy"})
    # COMMON STANDING END CH07 L2371
    lumi "후후."
    # SOURCE CH07 L2373 하린
    lumi "정말 못 이기겠네."
    # CONTI SOURCE CH07 L2375 [시간 경과 · 오후 6:30]
    $ phone_timeline_cue("CH07", "CH07_L2375")
    # SOURCE CH07 L2377 [BG] 건축학과 작업실 · 창가
    $ story_draft_scene("건축학과 작업실 · 창가", cast=["lumi"], standing=True)
    # COMMON STANDING BEGIN CH07 L2377
    $ story_stage_fade_in(["lumi"])
    # COMMON STANDING END CH07 L2377
    # SOURCE CH07 L2381
    # CH07 VISUAL 0611 BEGIN ch07_private_lumi-start
    $ cg_start("ch07_private_lumi", transition=0.35)
    # CH07 VISUAL 0611 END ch07_private_lumi-start
    narrator "하린 선배는 새로 만드는 모형을 보여줬다."
    # SOURCE CH07 L2383
    narrator "축제 때 만들었던 부스와는 조금 달랐다."
    # SOURCE CH07 L2385
    narrator "좀 더 개인적인 작품처럼 보였다."
    # SOURCE CH07 L2388 주인공
    mc "이번에는 어떤 공간이에요?"
    # SOURCE CH07 L2391 하린
    # COMMON STANDING BEGIN CH07 L2391
    $ story_stage(faces={"lumi": "serious"})
    # COMMON STANDING END CH07 L2391
    lumi "사람이 편하게 머무를 수 있는 곳이요."
    # SOURCE CH07 L2394 주인공
    mc "좋네요."
    # SOURCE CH07 L2397 하린
    lumi "아직 구상 중이에요."
    # SOURCE CH07 L2399 하린
    lumi "그런데 이번에는 조금 다른 방식으로 해보려고요."
    # SOURCE CH07 L2402 주인공
    mc "어떤 방식이요?"
    # SOURCE CH07 L2405 하린
    lumi "처음부터 모든 걸 정해놓기보다는……."
    # SOURCE CH07 L2407 하린
    lumi "실제로 사람이 어떻게 쓰는지 생각하면서 만들어보려고요."
    # SOURCE CH07 L2410 주인공
    mc "축제 때 경험이 도움이 됐나 봐요."
    # SOURCE CH07 L2413 하린
    lumi "네."
    # SOURCE CH07 L2415 하린
    lumi "생각보다 많이요."
    # SOURCE CH07 L2419
    narrator "하린 선배는 모형을 바라봤다."
    # SOURCE CH07 L2422 하린
    lumi "그리고……."
    # SOURCE CH07 L2424 하린
    lumi "오늘도 조금 그런 것 같아요."
    # SOURCE CH07 L2427 주인공
    mc "네?"
    # SOURCE CH07 L2430 하린
    lumi "원래는 오늘 저녁까지 모형만 만들 생각이었거든요."
    # SOURCE CH07 L2432 하린
    lumi "그런데 당신이 온다고 하니까……."
    # SOURCE CH07 L2434 하린
    lumi "계획이 바뀌었어요."
    # SOURCE CH07 L2437 주인공
    mc "방해가 된 건 아니죠?"
    # SOURCE CH07 L2440 하린
    lumi "……아니에요."
    # SOURCE CH07 L2443 하린
    # COMMON STANDING BEGIN CH07 L2443
    $ story_stage(faces={"lumi": "happy"})
    # COMMON STANDING END CH07 L2443
    lumi "오히려 좋았어."
    # SOURCE CH07 L2447
    narrator "하린 선배가 부드럽게 웃었다."
    # SOURCE CH07 L2450 하린
    lumi "그래서 조금 신기해요."
    # SOURCE CH07 L2452 하린
    lumi "전에는 계획이 바뀌면 불편했는데."
    # SOURCE CH07 L2454 하린
    lumi "요즘은 꼭 그렇지만은 않네."
    # SOURCE CH07 L2457 주인공
    mc "좋은 변화인가요?"
    # SOURCE CH07 L2460 하린
    lumi "……."
    # SOURCE CH07 L2462 하린
    lumi "그런 것 같아요."
    # CH07 VISUAL 0611 BEGIN ch07_private_lumi-end
    $ cg_end(transition=0.35)
    # CH07 VISUAL 0611 END ch07_private_lumi-end
    # SOURCE CH07 L2464 [BG] 작업실 밖 복도 · 저녁
    $ story_draft_scene("작업실 밖 복도 · 저녁", cast=["lumi"], standing=True)
    # COMMON STANDING BEGIN CH07 L2464
    $ story_stage_fade_in(["lumi"])
    # COMMON STANDING END CH07 L2464
    # SOURCE CH07 L2468
    narrator "작업실을 나서자 복도에는 사람이 거의 없었다."
    # SOURCE CH07 L2470
    narrator "하린 선배는 문을 잠그고 내 옆으로 걸어왔다."
    # SOURCE CH07 L2473 하린
    lumi "이제 어디 가세요?"
    # SOURCE CH07 L2476 주인공
    mc "아직 정한 건 없어요."
    # SOURCE CH07 L2479 하린
    # COMMON STANDING BEGIN CH07 L2479
    $ story_stage(faces={"lumi": "happy"})
    # COMMON STANDING END CH07 L2479
    lumi "그럼 저녁 먹을래요?"
    # SOURCE CH07 L2482 주인공
    mc "좋아요. 같이 가요."
    # SOURCE CH07 L2485 하린
    lumi "……후후."
    # SOURCE CH07 L2488 하린
    lumi "오늘은 제가 먼저 약속 잡았네요."
    # SOURCE CH07 L2491 주인공
    mc "그러네요."
    # SOURCE CH07 L2494 하린
    lumi "다음에는……."
    # SOURCE CH07 L2496 하린
    # COMMON STANDING BEGIN CH07 L2496
    $ story_stage(faces={"lumi": "embarrassed"})
    # COMMON STANDING END CH07 L2496
    lumi "그냥 보고 싶어서 연락하셔도 돼요."
    # SOURCE CH07 L2499 주인공
    mc "선배도 그러셔도 돼요."
    # SOURCE CH07 L2502 하린
    lumi "……."
    # SOURCE CH07 L2505 하린
    # COMMON STANDING BEGIN CH07 L2505
    $ story_stage(faces={"lumi": "happy"})
    # COMMON STANDING END CH07 L2505
    lumi "그럼 앞으로 자주 연락할지도 몰라요."
    # SOURCE CH07 L2508 주인공
    mc "기다릴게요."
    # SOURCE CH07 L2512
    narrator "하린 선배가 잠시 웃었다."
    # SOURCE CH07 L2514
    narrator "그러더니 조용히 말했다."
    # SOURCE CH07 L2517 하린
    lumi "……응."
    # SOURCE CH07 L2519 하린
    lumi "나도 기다릴게."
    # SOURCE CH07 L2521 [CONDITION] `ch04_partner == "harin"`
    if story_id(ch04_partner) == "lumi":
        # SOURCE CH07 L2524 하린
        lumi "지난번에 모형 고칠 때 기억하세요?"
        # SOURCE CH07 L2527 주인공
        mc "네. 같이 고쳤잖아요."
        # SOURCE CH07 L2530 하린
        lumi "그때도 계획에 없던 일이 생겼었죠."
        # SOURCE CH07 L2533 주인공
        mc "그랬죠."
        # SOURCE CH07 L2536 하린
        lumi "그런데 지금 생각하면……."
        # SOURCE CH07 L2538 하린
        lumi "그날이 꽤 좋았어요."
    # SOURCE CH07 L2544
    narrator "우리는 함께 복도를 걸었다."
    # SOURCE CH07 L2546
    narrator "처음에는 축제 부스를 설계하던 선배였다."
    # SOURCE CH07 L2548
    narrator "그런데 지금은 그 사람의 다음 작품과 다음 하루까지 궁금해졌다."
    # SOURCE CH07 L2550
    narrator "앞으로 어떤 일이 생길까."
    # SOURCE CH07 L2552
    narrator "아직은 모르겠다."
    # SOURCE CH07 L2554
    narrator "하지만 조금 기대됐다."
    # SOURCE CH07 L2556 [FLAG] `selected_route = harin`
    $ story_flag("selected_route", 'lumi')
    # SOURCE CH07 L2558 [FLAG] `harin_route_unlocked = True`
    $ story_flag("harin_route_unlocked", True)
    # CONTI SOURCE CH07 L2560 [RETURN TO SC07]
    jump ch07_sc07

label ch07_sc07:
    $ phone_timeline_enter("CH07", "ch07_sc07")
    # SOURCE CH07 L2562 그 이상의 시작
    # SOURCE CH07 L2564 [BG] 주인공 방 · 밤
    $ story_draft_scene("주인공 방 · 밤")
    # SOURCE CH07 L2566 [BGM] Common Route Ending · 잔잔한 피아노
    $ story_draft_bgm("Common Route Ending · 잔잔한 피아노")
    # CONTI SOURCE CH07 L2568 [FADE IN]
    # SOURCE CH07 L2572
    narrator "오늘 하루는 생각보다 길었다."
    # SOURCE CH07 L2574
    narrator "아침에는 아무 일정도 없는 것이 조금 허전했는데."
    # SOURCE CH07 L2576
    narrator "저녁이 된 지금은 이상하게 마음이 가벼웠다."
    # SOURCE CH07 L2578
    narrator "오랜만에 모두와 만나서 즐거웠다."
    # SOURCE CH07 L2580
    narrator "축제 이야기를 하면서 웃었고, 각자의 근황을 들었다."
    # SOURCE CH07 L2582
    narrator "그리고……"
    # SOURCE CH07 L2584
    narrator "오늘은 내가 먼저 한 사람을 찾아갔다."
    # SOURCE CH07 L2586
    narrator "축제 준비 때문도 아니고."
    # SOURCE CH07 L2588
    narrator "해야 할 일이 있어서도 아니었다."
    # SOURCE CH07 L2590
    narrator "그냥 만나고 싶었다."
    # SOURCE CH07 L2592
    narrator "그 이유만으로 충분했다."
    # CONTI SOURCE CH07 L2594 [UI] 스마트폰 화면
    $ story_chat(True, title="우리 사이")
    $ phone_threads["campus_group"]["title"] = "우리 사이"
    # SOURCE CH07 L2596
    narrator "「우리 사이 (6)」"
    # SOURCE CH07 L2599 시아
    sia "야 오늘 재밌었다"
    # SOURCE CH07 L2602 오므
    omu "니가 제일 시끄러웠다"
    # SOURCE CH07 L2605 시아
    sia "그게 재미있는 거거든"
    # SOURCE CH07 L2608 다림
    darim "후후. 다음에는 조금 더 여유 있게 만나봐요."
    # SOURCE CH07 L2611 로만
    roman "앗,,, 저도 오늘 즐거웠어요……!"
    # SOURCE CH07 L2614 하린
    lumi "다들 오늘도 수고했어요. 이번에는 정말 노느라 수고했네요."
    # SOURCE CH07 L2617 시아
    sia "야 그건 무슨 말이야ㅋㅋ"
    # SOURCE CH07 L2621
    narrator "나는 웃으면서 메시지를 읽었다."
    # SOURCE CH07 L2623
    narrator "처음 이 사람들을 만났을 때는 이런 날이 올 거라고 생각하지 못했다."
    # SOURCE CH07 L2625
    narrator "이제는 서로 장난을 치고, 약속을 만들고, 각자의 이야기를 나누는 사람들이 됐다."
    # SOURCE CH07 L2627
    narrator "축제는 끝났다."
    # SOURCE CH07 L2629
    narrator "하지만 우리 사이가 끝난 건 아니다."
    # SOURCE CH07 L2631
    narrator "오히려 이제부터 시작되는 이야기도 있을 것이다."
    # CONTI SOURCE CH07 L2633 [SFX] 개인 메시지 알림
    # SOURCE CH07 L2635 [CONDITION] `selected_route`에 따른 마지막 메시지
    if story_id(selected_route) == "roman":
        # SOURCE CH07 L2637 로만
        $ story_chat(False)
        $ story_chat(True, title="로만")
        # SOURCE CH07 L2640 로만
        roman "앗,,, 오늘 같이 있어주셔서 고마웠어요."
        # SOURCE CH07 L2642 로만
        roman "다음에 읽을 책도 골라둘게요."
        # SOURCE CH07 L2645 주인공 · 메시지
        mc "네. 다음에도 같이 읽어요."
        # SOURCE CH07 L2648 로만
        roman "……후후. 약속이에요."
        # SOURCE CH07 L2652
        narrator "함께 읽을 책."
        # SOURCE CH07 L2654
        narrator "그리고 언젠가 보여주겠다고 했던 문장."
        # SOURCE CH07 L2656
        narrator "로만과는 아직 나누지 못한 이야기가 많다."
        $ story_chat(False)
    elif story_id(selected_route) == "sia":
        # SOURCE CH07 L2658 시아
        $ story_chat(True, title="시아")
        # SOURCE CH07 L2661 시아
        sia "야 오늘 내 웹툰 본 거"
        # SOURCE CH07 L2663 시아
        sia "다른 데 가서 스포하면 안 된다?"
        # SOURCE CH07 L2666 주인공 · 메시지
        mc "알겠어요. 첫 독자의 비밀로 해둘게요."
        # SOURCE CH07 L2669 시아
        sia "ㅋㅋㅋ 좋아"
        # SOURCE CH07 L2671 시아
        sia "다음에도 와라"
        # SOURCE CH07 L2675
        narrator "시아가 만들고 있는 이야기는 아직 완성되지 않았다."
        # SOURCE CH07 L2677
        narrator "그런데 다음 장면이 벌써 궁금하다."
        $ story_chat(False)
    elif story_id(selected_route) == "darim":
        # SOURCE CH07 L2679 다림
        $ story_chat(True, title="다림")
        # SOURCE CH07 L2682 다림
        darim "오늘 정말 재미있었어요."
        # SOURCE CH07 L2684 다림
        darim "다음 게임도 기대하고 있을게요. 후후."
        # SOURCE CH07 L2687 주인공 · 메시지
        mc "저도요. 이번에도 지지 않을게요."
        # SOURCE CH07 L2690 다림
        darim "그럼 저도 열심히 준비해야겠네요."
        # SOURCE CH07 L2694
        narrator "다림 선배와는 다음에 어떤 승부를 하게 될까."
        # SOURCE CH07 L2696
        narrator "생각만 해도 웃음이 났다."
        $ story_chat(False)
    elif story_id(selected_route) == "omu":
        # SOURCE CH07 L2698 오므
        $ story_chat(True, title="오므")
        # SOURCE CH07 L2701 오므
        omu "오늘 사진 정리했다"
        # SOURCE CH07 L2703 오므
        omu "같이 찍은 거 잘 나왔네"
        # SOURCE CH07 L2706 주인공 · 메시지
        mc "저도 보고 싶어요. 다음에 보여주세요."
        # SOURCE CH07 L2709 오므
        omu "어"
        # SOURCE CH07 L2711 오므
        omu "다음에 또 같이 찍으러 가자"
        # SOURCE CH07 L2715
        narrator "오므와는 아직 가보지 못한 장소가 많다."
        # SOURCE CH07 L2717
        narrator "앞으로 어떤 풍경을 함께 보게 될까."
        $ story_chat(False)
    elif story_id(selected_route) == "lumi":
        # SOURCE CH07 L2719 하린
        $ story_chat(True, title="하린")
        # SOURCE CH07 L2722 하린
        lumi "오늘 와줘서 고마웠어요."
        # SOURCE CH07 L2724 하린
        lumi "계획에 없던 저녁이었는데 생각보다 좋았어."
        # SOURCE CH07 L2727 주인공 · 메시지
        mc "저도 좋았어요. 다음에도 같이 밥 먹어요."
        # SOURCE CH07 L2730 하린
        lumi "후후."
        # SOURCE CH07 L2732 하린
        lumi "그럼 다음 약속은 제가 잡을게요."
        # SOURCE CH07 L2736
        narrator "하린 선배는 늘 계획을 세우는 사람이었다."
        # SOURCE CH07 L2738
        narrator "그런데 이번에는 그 계획 안에 나와의 약속도 생겼다."
        $ story_chat(False)
    # CONTI SOURCE CH07 L2742 [UI] 스마트폰 화면 종료
    # SOURCE CH07 L2746
    narrator "나는 휴대전화를 내려놓았다."
    # SOURCE CH07 L2748
    narrator "오늘은 조금 다른 기분으로 잠들 수 있을 것 같았다."
    # SOURCE CH07 L2750
    narrator "누군가를 좋아한다는 감정이 정확히 어떤 것인지는 아직 잘 모르겠다."
    # SOURCE CH07 L2752
    narrator "하지만 이제는 그걸 알아가고 싶다."
    # SOURCE CH07 L2754
    narrator "함께 시간을 보내면서."
    # SOURCE CH07 L2756
    narrator "사소한 이야기를 나누면서."
    # SOURCE CH07 L2758
    narrator "때로는 서로 다른 생각 때문에 다투기도 하겠지만."
    # SOURCE CH07 L2760
    narrator "그 과정까지 함께 겪으면서."
    # SOURCE CH07 L2763 주인공 · 혼잣말
    mc "……앞으로도 만나고 싶네."
    # SOURCE CH07 L2767
    narrator "처음에는 그저 축제를 준비하는 사람들이었다."
    # SOURCE CH07 L2769
    narrator "그러다 친구가 되었고."
    # SOURCE CH07 L2771
    narrator "이제는 그중 한 사람과 조금 더 특별한 관계가 되고 싶어졌다."
    # SOURCE CH07 L2773
    narrator "이 마음이 어디로 이어질지는 아직 알 수 없다."
    # SOURCE CH07 L2775
    narrator "그래도 괜찮다."
    # SOURCE CH07 L2777
    narrator "오늘은 내가 먼저 한 걸음을 내디뎠으니까."
    # SOURCE CH07 L2779 [BGM] 천천히 고조
    $ story_draft_bgm("천천히 고조")
    # CONTI SOURCE CH07 L2781 [FADE TO BLACK]
    # CONTI SOURCE CH07 L2783 [TEXT]
    # CONTI SOURCE CH07 L2785 [TEXT/PLAN] 「우연히 만난 다섯 사람.」
    # CONTI SOURCE CH07 L2787 [TEXT/PLAN] 「함께 보낸 평범하고 특별한 날들.」
    # CONTI SOURCE CH07 L2789 [TEXT/PLAN] 「그리고 이제, 한 사람과 시작되는 새로운 이야기.」
    # CONTI SOURCE CH07 L2791 [화면 전환] 공통 루트 완료 연출
    # SOURCE CH07 L2793 [FLAG] `chapter07_complete = True`
    $ story_complete_chapter(7)
    # SOURCE CH07 L2795 [FLAG] `common_route_complete = True`
    $ story_flag("common_route_complete", True)
    # CONTI SOURCE CH07 L2797 [CONDITION] `selected_route`에 따라 다음 타이틀 표시
    # CONTI SOURCE CH07 L2799 [TEXT/PLAN] - `roman` → ROMAN ROUTE 「말하지 못한 문장」
    # CONTI SOURCE CH07 L2800 [TEXT/PLAN] - `sia` → SIA ROUTE 「장난 아니거든?」
    # CONTI SOURCE CH07 L2801 [TEXT/PLAN] - `darim` → DARIM ROUTE 「선배도 기대고 싶어요」
    # CONTI SOURCE CH07 L2802 [TEXT/PLAN] - `omu` → OMU ROUTE 「네가 찍힌 풍경」
    # CONTI SOURCE CH07 L2803 [TEXT/PLAN] - `harin` → HARIN ROUTE 「완벽하지 않은 설계도」
    # CONTI SOURCE CH07 L2805 [UI]
    # CONTI SOURCE CH07 L2807 [TEXT/PLAN] 「COMMON ROUTE COMPLETE」
    # CONTI SOURCE CH07 L2809 [TEXT/PLAN] 「우리 사이, 그 이상의 시작」
    # SOURCE CH07 L2811 [BGM STOP]
    $ story_draft_bgm("STOP")
    # CONTI SOURCE CH07 L2813 [FADE IN TO SELECTED ROUTE TITLE]
    # CONTI SOURCE CH07 L2815 [NEXT] 선택한 히로인의 개별 루트 R01로 이동
    # CONTI SOURCE CH07 L2817 [CHAPTER 07 END]
    jump common_route_dispatch
