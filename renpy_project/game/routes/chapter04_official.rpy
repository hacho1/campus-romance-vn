# CH04 · 원본 design_docs/story_sources/chapter04.txt
# SHA256: 5a73371c2ee5d24d89fbc8ec98313dba5812b8024e089260f51c96d5bcdd1460
# 원본 행 번호는 대사와 연출 위치를 가리킵니다.

label chapter04:
    $ phone_timeline_enter("CH04", "chapter04")
    $ story_begin_chapter(4, "장난이었는데, 왜 신경 쓰이지?")
    jump ch04_sc01

# CH04 SC01–SC05 · 대사와 콘티
# 원본: ch4 스토리.txt / SHA256 5a73371c2ee5d24d89fbc8ec98313dba5812b8024e089260f51c96d5bcdd1460
# SOURCE CH04 L 번호는 원고의 행 번호입니다. 콘티 표시는 화면에 표시하지 않습니다.

label ch04_sc01:
    $ phone_timeline_enter("CH04", "ch04_sc01")
    # SOURCE CH04 L29 ## SCENE 01. 평소랑 똑같은데?
    # SOURCE CH04 L31 오전 9:35 · 주인공 방 · 스마트폰
    $ phone_timeline_cue("CH04", "CH04_L31")
    # SOURCE CH04 L33 [BG] 주인공 방 · 아침
    $ story_scene("room", mode="normal", cast=[], light="day", location="주인공 방 · 아침", standing=False)
    # SOURCE CH04 L35 [BGM] Daily Campus
    $ play_bgm("campus_day")
    # SOURCE CH04 L37 [FADE IN]
    # SOURCE CH04 L39 [독백]
    # SOURCE CH04 L41
    narrator "축제 시범 운영을 마친 지 사흘이 지났다."
    # SOURCE CH04 L43
    narrator "그동안 특별한 일이 있었느냐고 묻는다면, 딱히 그렇지는 않았다."
    # SOURCE CH04 L45
    narrator "강의를 듣고, 과제를 정리하고, 팀원들과 메시지를 주고받았다."
    # SOURCE CH04 L47
    narrator "평범한 대학생활."
    # SOURCE CH04 L49
    narrator "……이라고 생각했는데."
    # SOURCE CH04 L51 [SFX] 휴대전화 진동
    # SOURCE CH04 L53 [주인공 · 혼잣말]
    # SOURCE CH04 L55
    mc "……또 단톡방인가."
    # SOURCE CH04 L57 [UI] 스마트폰 · 축제 준비팀 (6)
    $ story_chat(True, title="축제 준비팀")
    $ phone_clock = "09:35"
    # SOURCE CH04 L59
    sia "야 다들"
    # SOURCE CH04 L61
    sia "오늘 회의 기억하지?"
    # SOURCE CH04 L63
    omu "니부터 기억하면 된다"
    # SOURCE CH04 L65
    sia "나 오늘 안 늦음"
    # SOURCE CH04 L67
    lumi "아직 출발도 안 하셨잖아요."
    # SOURCE CH04 L69
    sia "너 감시하냐?"
    # SOURCE CH04 L71
    lumi "굳이요? 예상이 어렵지 않은데."
    # SOURCE CH04 L73
    darim "다들 오늘 세 시에 모이는 거 맞죠?"
    # SOURCE CH04 L75
    darim "최종 평가 자료를 정리해야 해요."
    # SOURCE CH04 L77
    roman "앗,,, 저는 오후 수업 끝나면 갈게요……!"
    # SOURCE CH04 L79
    omu "내도 그쯤 가면 된다"
    # SOURCE CH04 L81
    sia "좋아. 오늘 내가 1등으로 간다"
    # SOURCE CH04 L83
    lumi "그럼 인증사진 부탁드릴게요."
    # SOURCE CH04 L85
    sia "응 아니야~"
    $ story_chat(False)
    # SOURCE CH04 L87 [독백]
    # SOURCE CH04 L89
    narrator "이제는 익숙하다."
    # SOURCE CH04 L91
    narrator "누가 먼저 말을 걸고, 누가 태클을 걸고, 누가 마지막에 정리하는지까지."
    # SOURCE CH04 L93
    narrator "처음 이 사람들을 만났을 때는 이렇게 친해질 줄 몰랐다."
    # SOURCE CH04 L95
    narrator "나는 채팅창을 닫으려다가 잠시 멈췄다."
    # SOURCE CH04 L97
    narrator "며칠 전 받았던 개인 메시지가 눈에 들어왔기 때문이다."
    # SOURCE CH04 L99 [CONDITION] CH03에서 함께한 상대의 메시지만 표시
    # SOURCE CH04 L101 로만
    if story_id(ch03_evening_event) == "roman":
        # SOURCE CH04 L102 로만 · 이전 메시지
        # SOURCE CH04 L104
        roman "앗,,, 다음에 같이 읽고 싶은 책이 생겼어요. 나중에 보여드릴게요……!"
        # SOURCE CH04 L106
        narrator "같이 읽고 싶은 책. 무슨 책이길래 굳이 나한테 보여주겠다고 했을까. 이상하게 궁금하다."
    # SOURCE CH04 L108 시아
    elif story_id(ch03_evening_event) == "sia":
        # SOURCE CH04 L109 시아 · 이전 메시지
        # SOURCE CH04 L111
        sia "야 오늘 해준 말 기억한다? ㅋㅋ 다음 작품도 기대해라"
        # SOURCE CH04 L113
        narrator "시아는 원래 농담이 많은 사람이다. 그런데 그날 진지하게 고맙다고 했던 목소리가 자꾸 생각난다."
    # SOURCE CH04 L115 다림
    elif story_id(ch03_evening_event) == "darim":
        # SOURCE CH04 L116 다림 · 이전 메시지
        # SOURCE CH04 L118
        darim "오늘 같이 이야기해서 좋았어요. 게임 약속도 잊지 마세요. 후후."
        # SOURCE CH04 L120
        narrator "선배는 늘 차분하다. 하지만 가끔 장난칠 때는 표정부터 달라진다. 그런 모습이 꽤 재미있었다."
    # SOURCE CH04 L122 오므
    elif story_id(ch03_evening_event) == "omu":
        # SOURCE CH04 L123 오므 · 이전 메시지
        # SOURCE CH04 L125
        omu "아까 말한 사진 정리했다. 다음에 보면 보여줄게."
        # SOURCE CH04 L127
        narrator "오므가 보여준 사진이 떠오른다. 별것 아닌 풍경인데도 오므가 설명하면 어쩐지 달라 보였다."
    # SOURCE CH04 L129 하린
    elif story_id(ch03_evening_event) == "lumi":
        # SOURCE CH04 L130 하린 · 이전 메시지
        # SOURCE CH04 L132
        lumi "오늘은 조금 예상 밖이었네요. 그래도 재미있었어. 좋은 밤 보내요."
        # SOURCE CH04 L134
        narrator "늘 여유롭던 하린 선배가 잠깐 시선을 피했던 순간. 왜 그 모습이 아직도 생각나는 걸까."
    # SOURCE CH04 L138 [공통 복귀]
    # SOURCE CH04 L140 [주인공 · 혼잣말]
    # SOURCE CH04 L142
    mc "……내가 왜 이걸 또 읽고 있지?"
    # SOURCE CH04 L144 [독백]
    # SOURCE CH04 L146
    narrator "친해졌으니까."
    # SOURCE CH04 L148
    narrator "같이 보낸 시간이 많으니까."
    # SOURCE CH04 L150
    narrator "그냥 그런 이유겠지."
    # SOURCE CH04 L152
    narrator "굳이 복잡하게 생각할 필요는 없다."
    # SOURCE CH04 L154 [SFX] 새로운 공지 알림
    # SOURCE CH04 L156 [UI] 축제 운영위원회 공지
    $ story_chat(True, title="축제 운영위원회")
    $ phone_clock = "09:35"
    # SOURCE CH04 L158
    system_note "「최종 평가 준비 안내」"
    # SOURCE CH04 L160
    system_note "- 수정 기획안 제출"
    # SOURCE CH04 L161
    system_note "- 1분 이내 체험 시연 영상 제출"
    # SOURCE CH04 L162
    system_note "- 예산 및 공간 배치 최종 확인"
    # SOURCE CH04 L163
    system_note "- 제출 기한: 이틀 후 오후 6시"
    $ story_chat(False)
    # SOURCE CH04 L165 [주인공 · 혼잣말]
    # SOURCE CH04 L167
    mc "……이틀?"
    # SOURCE CH04 L169 [독백]
    # SOURCE CH04 L171
    narrator "잠깐만."
    # SOURCE CH04 L173
    narrator "시연 영상?"
    # SOURCE CH04 L175
    narrator "그건 누가 만들지?"
    # SOURCE CH04 L177 [SFX] 단체 채팅 알림
    $ story_chat(True, title="축제 준비팀")
    $ phone_clock = "09:35"
    # SOURCE CH04 L179
    sia "야 시연 영상은 내가 만들게"
    # SOURCE CH04 L181
    sia "대신 촬영이랑 편집 도와줄 사람 구함"
    # SOURCE CH04 L183
    omu "니가 만든다더니 결국 다 같이 하네"
    # SOURCE CH04 L185
    sia "원래 협업이 중요한 거거든"
    # SOURCE CH04 L187
    darim "오늘 회의에서 역할을 나눠봐요."
    # SOURCE CH04 L189
    lumi "공간 자료는 제가 정리해 둘게요."
    # SOURCE CH04 L191
    roman "앗,,, 설명 문구도 필요하겠죠……?"
    $ story_chat(False)
    # SOURCE CH04 L193 [주인공 · 혼잣말]
    # SOURCE CH04 L195
    mc "……또 바빠지겠네."
    # SOURCE CH04 L197 [독백]
    # SOURCE CH04 L199
    narrator "이쯤 되면 공강이란 게 원래 존재했는지도 의심스럽다."
    # SOURCE CH04 L201
    narrator "그래도 싫지는 않았다."
    # SOURCE CH04 L203
    narrator "그 사실이 조금 이상할 뿐."
    # SOURCE CH04 L205 [FADE OUT]
    # SOURCE CH04 L207 [SCENE 01 END]
    jump ch04_sc02

label ch04_sc02:
    $ phone_timeline_enter("CH04", "ch04_sc02")
    # SOURCE CH04 L209 ## SCENE 02. 우리는 정말 친한 사이일까?
    # SOURCE CH04 L211 오후 3:05 · 공동 동아리실 · SD 단체 코미디
    $ phone_timeline_cue("CH04", "CH04_L211")
    # SOURCE CH04 L213 [BG] 공동 동아리실
    $ story_scene("clubroom307", mode="normal", cast=STORY_HEROES, light="day", location="공동 동아리실 · 오후")
    # SOURCE CH04 L215 [BGM] Light Comedy
    $ play_bgm("comedy_light")
    # SOURCE CH04 L217 [SD EVENT] `ch04_meeting_comedy_01`
    # 콘티: 회의 중인 다섯 사람과 시아의 1분 구성 제안. 전체 단체 SD 컷.
    # SOURCE CH04 L219 [독백]
    # SOURCE CH04 L221
    narrator "동아리실 문을 열자마자 익숙한 목소리가 들렸다."
    # SOURCE CH04 L223
    $ story_stage(faces={"sia": "smug"})
    sia "야, 내 말 좀 들어봐."
    # SOURCE CH04 L225
    omu "듣고 있다."
    # SOURCE CH04 L227
    sia "영상이 딱 1분이잖아?"
    # SOURCE CH04 L229
    darim "네."
    # SOURCE CH04 L231
    $ sd_event_start("ch04_meeting_comedy_01")
    sia "첫 10초는 개그!"
    # SOURCE CH04 L233
    sia "다음 20초는 설명!"
    # SOURCE CH04 L235
    sia "마지막 30초는 감동!"
    $ sd_event_end()
    # SOURCE CH04 L237
    $ story_stage(faces={"lumi": "confused"})
    lumi "그걸 전부 1분에 넣겠다고요?"
    # SOURCE CH04 L239
    sia "가능하지."
    # SOURCE CH04 L241
    $ story_stage(faces={"lumi": "smug"})
    lumi "시간을 늘리는 설계라도 하셨나 봐요."
    # SOURCE CH04 L243
    sia "아니, 편집하면 되잖아!"
    # SOURCE CH04 L245
    omu "니가 10초 동안 조용히 있는 것부터 해봐라."
    # SOURCE CH04 L247
    $ story_stage(faces={"sia": "angry"})
    sia "야!"
    # SOURCE CH04 L249 [SD EVENT] `ch04_meeting_comedy_02`
    # 콘티: 로만의 조심스러운 동의와 뒤이은 반론, 시아의 리액션. 전체 단체 SD 컷.
    # SOURCE CH04 L251
    $ story_stage(faces={"roman": "embarrassed"})
    roman "앗,,, 저는 재미있을 것 같아요……."
    # SOURCE CH04 L253
    $ sd_event_start("ch04_meeting_comedy_02")
    sia "로만아! 역시 너밖에 없다!"
    # SOURCE CH04 L255
    roman "그런데…… 1분이면 조금 짧지 않을까요……?"
    # SOURCE CH04 L257
    sia "……너까지?"
    $ sd_event_end()
    # SOURCE CH04 L259
    $ story_stage(faces={"darim": "serious"})
    darim "먼저 꼭 필요한 내용부터 정해볼까요?"
    # SOURCE CH04 L261 [주인공]
    # SOURCE CH04 L263
    mc "안녕하세요. 저 왔어요."
    # SOURCE CH04 L265
    $ story_stage(faces={"sia": "happy", "roman": "normal"})
    sia "오, [player_name]!"
    # SOURCE CH04 L267
    sia "드디어 감상 담당 왔다!"
    # SOURCE CH04 L269 [주인공]
    # SOURCE CH04 L271
    mc "제가 정식 감상 담당이 된 건가요?"
    # SOURCE CH04 L273
    sia "응. 방금."
    # SOURCE CH04 L275 [주인공]
    # SOURCE CH04 L277
    mc "그럼 업무 내용부터 알려주세요."
    # SOURCE CH04 L279
    sia "와, 까다로운 직원이네."
    # SOURCE CH04 L281
    omu "니가 멋대로 임명했잖아."
    # SOURCE CH04 L283
    $ story_stage(faces={"lumi": "smug"})
    lumi "계약서도 없는데 일을 시키시네요."
    # SOURCE CH04 L285
    sia "너희 오늘 왜 다 나한테 이래?"
    # SOURCE CH04 L287 [독백]
    # SOURCE CH04 L289
    narrator "나는 웃으며 빈자리에 앉았다."
    # SOURCE CH04 L291
    narrator "처음 이 방에 들어왔을 때는 어디에 앉아야 할지도 몰랐다."
    # SOURCE CH04 L293
    narrator "이제는 다들 자연스럽게 자리를 비켜준다."
    # SOURCE CH04 L295
    darim "오늘은 영상 구성과 제출할 자료를 정리하려고 해요."
    # SOURCE CH04 L297
    roman "설명 문구는 제가 맡아볼게요."
    # SOURCE CH04 L299
    omu "촬영은 내가 할게."
    # SOURCE CH04 L301
    lumi "저는 부스 모형이랑 동선을 다시 확인할게요."
    # SOURCE CH04 L303
    sia "좋아. 역시 내 영상이 중심이네."
    # SOURCE CH04 L305 [주인공]
    # SOURCE CH04 L307
    mc "아직 그렇게 정한 건 아니지 않나요?"
    # SOURCE CH04 L309
    sia "……너도 내 편 아니냐?"
    # SOURCE CH04 L311 [주인공]
    # SOURCE CH04 L313
    mc "저는 일단 영상 편인데요."
    # SOURCE CH04 L315
    $ story_stage(faces={"omu": "happy"})
    omu "ㅋㅋㅋ 맞는 말이네."
    # SOURCE CH04 L317
    lumi "이제 장난을 제법 잘 받아치시네."
    # SOURCE CH04 L319
    sia "아, 점점 만만하지 않아지는데?"
    # SOURCE CH04 L321 [독백]
    # SOURCE CH04 L323
    $ story_stage(faces={actor: "happy" for actor in STORY_HEROES})
    narrator "다들 웃었다."
    # SOURCE CH04 L325
    narrator "그런데 시아가 갑자기 고개를 들었다."
    # SOURCE CH04 L327
    $ story_stage(faces={"sia": "normal"})
    sia "야, 근데 우리 진짜 많이 친해지지 않았냐?"
    # SOURCE CH04 L329
    darim "그렇죠. 함께 준비한 시간이 있으니까요."
    # SOURCE CH04 L331
    roman "앗,,, 저도 처음보다 많이 편해졌어요."
    # SOURCE CH04 L333
    omu "이제 누가 뭔 말 할지 대충 알겠다."
    # SOURCE CH04 L335
    lumi "특히 시아 씨는 참 예상하기 쉽죠."
    # SOURCE CH04 L337
    sia "왜?"
    # SOURCE CH04 L339
    lumi "말씀하시기 전에 표정에 다 나오거든요."
    # SOURCE CH04 L341
    sia "……."
    # SOURCE CH04 L343
    sia "그거 칭찬이냐?"
    # SOURCE CH04 L345
    lumi "어떻게 받아들이고 싶어요?"
    # SOURCE CH04 L347 [주인공]
    # SOURCE CH04 L349
    mc "저도 이제 조금 알 것 같아요."
    # SOURCE CH04 L351
    omu "뭘?"
    # SOURCE CH04 L353 [주인공]
    # SOURCE CH04 L355
    mc "다들 어떤 사람인지요."
    # SOURCE CH04 L357
    lumi "벌써 다 안다고 생각하시는 건 아니죠?"
    # SOURCE CH04 L359 [주인공]
    # SOURCE CH04 L361
    mc "아직 멀었죠."
    # SOURCE CH04 L363
    darim "후후. 앞으로 알아갈 시간이 더 있으니까요."
    # SOURCE CH04 L365
    roman "……네."
    # SOURCE CH04 L367
    sia "좋아! 그럼 친목 확인 끝!"
    # SOURCE CH04 L369 [주인공]
    # SOURCE CH04 L371
    mc "그걸 확인하고 있었나요?"
    # SOURCE CH04 L373
    $ sd_event_start("ch04_meeting_comedy_03")
    sia "응. 다음 안건은 밥 메뉴."
    # SOURCE CH04 L375
    darim "영상부터 정해야 해요."
    # SOURCE CH04 L377
    sia "……아, 진짜."
    # SOURCE CH04 L379 [SD EVENT] `ch04_meeting_comedy_03`
    # 콘티: 밥 메뉴를 내미는 시아와 영상이 먼저라고 하는 다림의 반응. 전체 단체 SD 컷.
    $ sd_event_end()
    # SOURCE CH04 L381 [독백]
    # SOURCE CH04 L383
    narrator "늘 이런 식이다."
    # SOURCE CH04 L385
    narrator "시끄럽게 웃고, 누군가는 장난을 치고, 누군가는 그걸 받아친다."
    # SOURCE CH04 L387
    narrator "그런데 이제는 그런 시간이 조금 편하다."
    # SOURCE CH04 L389
    narrator "어쩌면 처음 생각했던 것보다 훨씬 많이 친해진 걸지도 모르겠다."
    # SOURCE CH04 L391 [SCENE 02 END]
    jump ch04_sc03

label ch04_sc03:
    $ phone_timeline_enter("CH04", "ch04_sc03")
    # SOURCE CH04 L393 ## SCENE 03. 상대 팀도 만만치 않다
    # SOURCE CH04 L395 오후 3:45 · 축제 준비 구역 · 라이벌 재등장
    $ phone_timeline_cue("CH04", "CH04_L395")
    # SOURCE CH04 L397 [BG] 축제 준비 구역
    $ story_scene("booth", mode="normal", cast=STORY_HEROES, light="day", location="축제 준비 구역 · 오후")
    # SOURCE CH04 L399 [BGM] Comedy Battle
    $ play_bgm("rivalry_comedy")
    # SOURCE CH04 L401 [독백]
    # SOURCE CH04 L403
    narrator "시연 영상에 넣을 부스 장면을 확인하려고 광장으로 나왔다."
    # SOURCE CH04 L405
    narrator "그런데 옆 부스에서 고소한 냄새가 풍겨왔다."
    # SOURCE CH04 L407
    $ story_stage(faces={"sia": "confused"})
    sia "……뭐야. 맛있는 냄새 나는데?"
    # SOURCE CH04 L409
    omu "쿠키 냄새 아이가?"
    # SOURCE CH04 L411
    $ story_stage(faces={"roman": "happy"})
    roman "앗,,, 정말 좋은 냄새예요……!"
    # SOURCE CH04 L413
    $ story_stage(cast=STORY_HEROES + ["hyeophap", "hess", "bambam"])
    $ story_enter("ski", side="right", face="happy")
    ski "후후."
    # SOURCE CH04 L415
    ski "드디어 알아본 거야?"
    # SOURCE CH04 L417 [SD EVENT] `ch04_ski_baking_01`
    # 콘티: 시제품 쿠키 접시를 내보이는 스키와 두 팀의 반응. 전체 단체 SD 컷.
    # SOURCE CH04 L419
    ski "오늘은 내 진짜 실력을 보여주지!"
    # SOURCE CH04 L421
    sia "네가 숨겨진 실력이 있었어?"
    # SOURCE CH04 L423
    ski "숨겨진 게 너무 많아서 문제야."
    # SOURCE CH04 L425
    hyeophap "스키, 말 그만하고 시제품부터 보여줘."
    # SOURCE CH04 L427
    ski "알았어, 알았어."
    # SOURCE CH04 L429 [독백]
    # SOURCE CH04 L431
    $ sd_event_start("ch04_ski_baking_01")
    narrator "스키는 접시 위에 쿠키 몇 개를 올려놓았다."
    # SOURCE CH04 L433
    narrator "크기도 일정했고, 장식도 제법 깔끔했다."
    # SOURCE CH04 L435
    narrator "처음에는 또 자랑만 할 줄 알았는데."
    $ sd_event_end()
    # SOURCE CH04 L437
    $ story_stage(faces={"darim": "surprised"})
    darim "와, 정말 잘 만드셨네요."
    # SOURCE CH04 L439
    ski "그렇지? 이제야 내 진가를 알아보는구나!"
    # SOURCE CH04 L441
    $ story_stage(faces={"sia": "surprised"})
    sia "……잠깐."
    # SOURCE CH04 L443
    sia "진짜 잘 만들었는데?"
    # SOURCE CH04 L445
    ski "그 반응을 기다렸어."
    # SOURCE CH04 L447
    lumi "모양이 상당히 일정하네요."
    # SOURCE CH04 L449
    omu "생각보다 제대로 하네."
    # SOURCE CH04 L451
    ski "그 '생각보다'는 빼주면 안 되냐?"
    # SOURCE CH04 L453
    hess "실력은 있으시네요."
    # SOURCE CH04 L455
    ski "역시 헤스! 넌 보는 눈이 있어."
    # SOURCE CH04 L457
    hess "말이 많아서 그렇지."
    # SOURCE CH04 L459
    ski "……그 말은 꼭 해야 했냐?"
    # SOURCE CH04 L461
    bambam "그래도 만들 때는 되게 집중하시던데요."
    # SOURCE CH04 L463
    ski "봐! 밤밤도 인정했잖아."
    # SOURCE CH04 L465
    hyeophap "인정받았으면 이제 재료 설명해."
    # SOURCE CH04 L467 [전환] 일반 스탠딩
    # SOURCE CH04 L469 [독백]
    # SOURCE CH04 L471
    narrator "스키는 디저트의 제작 과정과 재료 관리 방법을 설명하기 시작했다."
    # SOURCE CH04 L473
    narrator "의외였다."
    # SOURCE CH04 L475
    $ story_stage(faces={"ski": "serious", "sia": "serious"})
    narrator "평소의 뻔뻔한 태도와 달리, 제과제빵에 대해서는 제법 진지했다."
    # SOURCE CH04 L477
    ski "쿠키는 크기가 일정해야 굽는 정도도 비슷해져."
    # SOURCE CH04 L479
    ski "온도랑 시간만 맞춘다고 끝나는 게 아니거든."
    # SOURCE CH04 L481
    sia "……."
    # SOURCE CH04 L483
    ski "왜 그렇게 봐?"
    # SOURCE CH04 L485
    sia "아니. 잠깐 멋있어서."
    # SOURCE CH04 L487
    $ story_stage(faces={"ski": "surprised"})
    $ story_effect("surprise", "ski")
    ski "……!"
    # SOURCE CH04 L489
    $ story_stage(faces={"ski": "happy"})
    ski "드디어 내 매력을……!"
    # SOURCE CH04 L491
    $ story_stage(faces={"sia": "smug"})
    sia "응 아니야~ 딱 3초."
    # SOURCE CH04 L493
    hyeophap "그럼 이미 지났네."
    # SOURCE CH04 L495
    $ story_stage(faces={"omu": "happy"})
    omu "ㅋㅋㅋㅋㅋ"
    # SOURCE CH04 L497 [독백]
    # SOURCE CH04 L499
    $ story_stage(faces={"hyeophap": "serious", "hess": "serious"})
    narrator "협합은 운영표를 펼쳤다."
    # SOURCE CH04 L501
    hyeophap "우리는 최종 평가에서 실제 운영 가능성을 보여주려고 해."
    # SOURCE CH04 L503
    hyeophap "스키가 만든 시제품을 기준으로 제작 시간과 재료 소요량도 다시 계산했고."
    # SOURCE CH04 L505
    hess "질문 카드도 지난 시범 운영 결과에 맞춰 줄였어요."
    # SOURCE CH04 L507
    $ story_stage(faces={"bambam": "happy"})
    bambam "기다리는 분들이 편하게 읽을 안내 카드도 만들었고요."
    # SOURCE CH04 L509
    lumi "각자 꽤 많이 준비하셨네요."
    # SOURCE CH04 L511
    hyeophap "너희도 그렇잖아."
    # SOURCE CH04 L513
    darim "저희도 마지막까지 보완하려고요."
    # SOURCE CH04 L515
    ski "좋아. 그럼 정정당당하게 승부하자!"
    # SOURCE CH04 L517
    sia "이번엔 우리가 이긴다."
    # SOURCE CH04 L519
    ski "그건 좀 어려울걸?"
    # SOURCE CH04 L521
    sia "응 아니야~"
    # SOURCE CH04 L523
    ski "나도 아니라고 해줄게."
    # SOURCE CH04 L525
    omu "니들 둘이 진짜 똑같다."
    # SOURCE CH04 L527 [주인공]
    # SOURCE CH04 L529
    mc "두 분은 경쟁하는 것보다 말싸움하는 게 더 즐거워 보이는데요."
    # SOURCE CH04 L531
    sia "이것도 경쟁이거든?"
    # SOURCE CH04 L533
    ski "맞아! 그리고 지금은 내가 이기고 있어."
    # SOURCE CH04 L535
    hyeophap "아무도 점수 안 매겼어."
    # SOURCE CH04 L537
    hess "그럼 무승부네요."
    # SOURCE CH04 L539
    bambam "평화롭네요."
    # SOURCE CH04 L541 [독백]
    # SOURCE CH04 L543
    narrator "……평화로운 건가, 이게?"
    # SOURCE CH04 L545 [FLAG] `rival_skill_recognized = True`
    $ story_flag("rival_skill_recognized")
    # SOURCE CH04 L547 [SCENE 03 END]
    jump ch04_sc04

label ch04_sc04:
    $ phone_timeline_enter("CH04", "ch04_sc04")
    # SOURCE CH04 L549 ## SCENE 04. 친하다는 건 어디까지?
    # SOURCE CH04 L551 오후 4:20 · 공동 동아리실 · 단체 장난에서 감정 전환
    $ phone_timeline_cue("CH04", "CH04_L551")
    # SOURCE CH04 L553 [BG] 공동 동아리실
    $ story_scene("clubroom307", mode="normal", cast=STORY_HEROES, light="day", location="공동 동아리실 · 오후")
    # SOURCE CH04 L555 [BGM] Warm Daily
    $ play_bgm("warm_workshop")
    # SOURCE CH04 L557 [독백]
    # SOURCE CH04 L559
    narrator "동아리실로 돌아온 우리는 시연 영상에 들어갈 내용을 다시 확인했다."
    # SOURCE CH04 L561
    narrator "다림은 일정표를 펼쳤고, 시아는 태블릿에 콘티를 띄웠다."
    # SOURCE CH04 L563
    darim "이틀 뒤가 제출이니까 오늘은 촬영할 장면을 확정하면 좋겠어요."
    # SOURCE CH04 L565
    sia "좋아. 일단 만화로 설명하고 실제 부스 보여주는 거지?"
    # SOURCE CH04 L567
    lumi "네. 그런데 화면에 보이는 동선이 실제 배치와 맞아야 해요."
    # SOURCE CH04 L569
    omu "영상 찍을 때는 내가 확인해 볼게."
    # SOURCE CH04 L571
    roman "앗,,, 설명 문구도 조금 더 줄여볼게요."
    # SOURCE CH04 L573 [주인공]
    # SOURCE CH04 L575
    mc "그럼 저는 필요한 자료를 같이 정리할게요."
    # SOURCE CH04 L577
    $ story_stage(faces={"sia": "smug"})
    sia "역시. 우리 팀 공식 만능 담당."
    # SOURCE CH04 L579 [주인공]
    # SOURCE CH04 L581
    mc "그 직책은 그만 만들어주시면 안 될까요?"
    # SOURCE CH04 L583
    sia "싫은데?"
    # SOURCE CH04 L585 [독백]
    # SOURCE CH04 L587
    $ story_stage(faces={actor: "happy" for actor in STORY_HEROES})
    narrator "우리는 웃으면서 작업을 시작했다."
    # SOURCE CH04 L589
    narrator "그러다 시아가 갑자기 물었다."
    # SOURCE CH04 L591
    sia "근데 [player_name]."
    # SOURCE CH04 L593 [주인공]
    # SOURCE CH04 L595
    mc "네?"
    # SOURCE CH04 L597
    $ story_stage(faces={"sia": "smug"})
    sia "너 우리 중에 누구랑 제일 친하냐?"
    # SOURCE CH04 L599 [주인공]
    # SOURCE CH04 L601
    mc "……네?"
    # SOURCE CH04 L603
    $ story_stage(faces={"omu": "serious"})
    omu "니는 또 뭔 질문을 하노."
    # SOURCE CH04 L605
    sia "아니, 다 친해졌잖아."
    # SOURCE CH04 L607
    sia "그럼 특히 편한 사람도 있을 거 아니야."
    # SOURCE CH04 L609
    darim "굳이 순위를 정할 필요는 없지 않을까요?"
    # SOURCE CH04 L611
    $ story_stage(faces={"lumi": "smug"})
    lumi "흐음, 그래도 조금 궁금하긴 하네요."
    # SOURCE CH04 L613
    $ story_stage(faces={"roman": "embarrassed"})
    roman "앗,,, 저도……."
    # SOURCE CH04 L615 [독백]
    # SOURCE CH04 L617
    $ sd_event_start("ch04_friendship_teasing_01")
    narrator "갑자기 모두의 시선이 나에게 향했다."
    # SOURCE CH04 L619
    narrator "아니, 그냥 축제 준비 회의 아니었나?"
    # SOURCE CH04 L621 [SD EVENT] `ch04_friendship_teasing_01`
    # 콘티: 주인공에게 한꺼번에 시선을 돌리는 팀원들과 가장 친한 사람을 묻는 장난. 전체 단체 SD 컷.
    # SOURCE CH04 L623 [주인공]
    # SOURCE CH04 L625
    mc "저는 다들 편한데요."
    $ sd_event_end()
    # SOURCE CH04 L627
    sia "와, 모범 답안."
    # SOURCE CH04 L629
    omu "틀린 말은 아니지."
    # SOURCE CH04 L631
    lumi "정말 다 똑같이 편하세요?"
    # SOURCE CH04 L633 [주인공]
    # SOURCE CH04 L635
    mc "……왜 이렇게 어려운 질문을 하시는 거예요?"
    # SOURCE CH04 L637
    lumi "후후. 그냥 궁금해서요."
    # SOURCE CH04 L639
    darim "놀리시는 건 이쯤 하세요."
    # SOURCE CH04 L641
    sia "알았어, 알았어."
    # SOURCE CH04 L643 [독백]
    # SOURCE CH04 L645
    narrator "겨우 넘어간 줄 알았는데, 시아가 또 입을 열었다."
    # SOURCE CH04 L647 [CONDITION] CH03 저녁 이벤트 상대에 따른 추가 대사
    # SOURCE CH04 L649 로만
    if story_id(ch03_evening_event) == "roman":
        # SOURCE CH04 L650
        sia "아, 맞다. 로만이랑 저번에 같이 갔다며?"
        # SOURCE CH04 L650
        $ story_stage(faces={"roman": "embarrassed"})
        roman "앗,,, 네…… 가는 방향이 같아서요."
        # SOURCE CH04 L650
        sia "아니, 그냥 물어본 건데ㅋㅋ"
    # SOURCE CH04 L652 시아
    elif story_id(ch03_evening_event) == "sia":
        # SOURCE CH04 L653
        omu "니도 저번에 [player_name]이랑 같이 갔잖아."
        # SOURCE CH04 L653
        $ story_stage(faces={"sia": "embarrassed"})
        sia "어? 그건 그냥 같이 간 거지."
        # SOURCE CH04 L653
        omu "내도 그냥 말했다."
    # SOURCE CH04 L655 다림
    elif story_id(ch03_evening_event) == "darim":
        # SOURCE CH04 L656
        lumi "다림 씨도 저번에 같이 걸어가셨죠?"
        # SOURCE CH04 L656
        darim "네. 이런저런 이야기했어요."
        # SOURCE CH04 L656
        sia "오, 무슨 얘기?"
        # SOURCE CH04 L656
        $ story_stage(faces={"darim": "smug"})
        darim "후후. 비밀이에요."
    # SOURCE CH04 L658 오므
    elif story_id(ch03_evening_event) == "omu":
        # SOURCE CH04 L659
        sia "오므야, 너도 저번에 같이 갔잖아."
        # SOURCE CH04 L659
        omu "우연히 길이 같아서 그랬다."
        # SOURCE CH04 L659
        sia "응 아니야~ 수상한데?"
        # SOURCE CH04 L659
        $ story_stage(faces={"omu": "smug"})
        omu "니가 더 수상하다."
    # SOURCE CH04 L661 하린
    elif story_id(ch03_evening_event) == "lumi":
        # SOURCE CH04 L662
        sia "하린도 저번에 같이 갔다며?"
        # SOURCE CH04 L662
        lumi "네. 방향이 같았거든요."
        # SOURCE CH04 L662
        sia "둘이 무슨 얘기했는데?"
        # SOURCE CH04 L662
        $ story_stage(faces={"lumi": "smug"})
        lumi "시아 씨 이야기요."
        # SOURCE CH04 L662
        sia "야!"
    # SOURCE CH04 L664 [공통 복귀]
    # SOURCE CH04 L666 [SD EVENT] `ch04_friendship_teasing_02`
    # 콘티: CH03 저녁 상대 이야기를 마친 뒤 다시 터지는 웃음. 전체 단체 SD 컷.
    # SOURCE CH04 L668 [독백]
    # SOURCE CH04 L670
    $ sd_event_start("ch04_friendship_teasing_02")
    narrator "또 웃음소리가 터졌다."
    # SOURCE CH04 L672
    narrator "분명 평소와 똑같은 장난이었다."
    $ sd_event_end()
    # SOURCE CH04 L674
    narrator "그런데 이번에는 조금 달랐다."
    # SOURCE CH04 L676
    narrator "내가 누구와 같이 있었는지, 누구에게 더 관심이 있는지."
    # SOURCE CH04 L678
    narrator "그런 걸 다른 사람들이 이야기하는 게 묘하게 신경 쓰였다."
    # SOURCE CH04 L680 [주인공]
    # SOURCE CH04 L682
    mc "……그냥 같이 걸어간 것뿐인데요."
    # SOURCE CH04 L684
    sia "알았어ㅋㅋ 우리가 뭐라고 했냐?"
    # SOURCE CH04 L686
    $ story_stage(faces={actor: "normal" for actor in STORY_HEROES})
    darim "자, 이제 다시 작업할까요?"
    # SOURCE CH04 L688
    lumi "그래야겠네요. 시간이 얼마 없으니까."
    # SOURCE CH04 L690
    omu "영상부터 찍자."
    # SOURCE CH04 L692
    roman "앗,,, 저도 준비할게요."
    # SOURCE CH04 L694 [전환] 일반 대화
    # SOURCE CH04 L696 [독백]
    # SOURCE CH04 L698
    narrator "다들 다시 자기 일에 집중했다."
    # SOURCE CH04 L700
    narrator "나는 잠깐 그 모습을 바라봤다."
    # SOURCE CH04 L702
    narrator "분명 친구끼리 충분히 할 수 있는 장난이다."
    # SOURCE CH04 L704
    narrator "그런데……"
    # SOURCE CH04 L706
    narrator "정말 그게 전부일까?"
    # SOURCE CH04 L708
    narrator "아니다. 지금은 일부터 하자."
    # SOURCE CH04 L710 ### 선택지 1. 누구의 작업을 도울까?
    menu:
        "누구의 작업을 도울까?"
        # SOURCE CH04 L712
        "로만과 영상 문구 정리":
            $ story_apply("ch04_sc04_partner_roman", values={"ch04_partner": "roman"})
        # SOURCE CH04 L714
        "시아와 콘티 수정":
            $ story_apply("ch04_sc04_partner_sia", values={"ch04_partner": "sia"})
        # SOURCE CH04 L716
        "다림과 운영 자료 정리":
            $ story_apply("ch04_sc04_partner_darim", values={"ch04_partner": "darim"})
        # SOURCE CH04 L718
        "오므와 촬영 자료 선별":
            $ story_apply("ch04_sc04_partner_omu", values={"ch04_partner": "omu"})
        # SOURCE CH04 L720
        "하린과 부스 모형 수정":
            $ story_apply("ch04_sc04_partner_lumi", values={"ch04_partner": "lumi"})
    # SOURCE CH04 L722 `ch04_partner = "{work}"` · SC05\~06의 해당 개인 분기로 진행
    # SOURCE CH04 L724 [독백]
    # SOURCE CH04 L726
    narrator "나는 먼저 한 사람의 작업부터 돕기로 했다."
    # SOURCE CH04 L728
    narrator "일이 잘 풀리길 바랐는데, 생각보다 간단하지는 않았다."
    # SOURCE CH04 L730 [SCENE 04 END]
    jump ch04_sc05

label ch04_sc05:
    $ phone_timeline_enter("CH04", "ch04_sc05")
    # SOURCE CH04 L732 ## SCENE 05. 장난으로 넘길 수 없는 말
    # SOURCE CH04 L734 오후 4:40 · 선택 히로인의 작업 공간 · 개인 갈등 시작
    $ phone_timeline_cue("CH04", "CH04_L734")
    # SOURCE CH04 L736 ### SC05-A. 로만 「지워진 문장」
    if ch04_partner == "roman":
        # 콘티: 로만 스탠딩 / 문장을 제안할 때 → 원고에서 삭제 제안을 듣고 시선을 노트에 둠.
        # SOURCE CH04 L738 [BG] 도서관 스터디 공간
        $ story_scene("library", mode="emotion", cast=["roman"], light="day", location="도서관 스터디 공간 · 오후")
        # SOURCE CH04 L740 [BGM] Quiet Library
        $ play_bgm("quiet_library")
        # SOURCE CH04 L742 [독백]
        # SOURCE CH04 L744
        narrator "로만과 함께 시연 영상의 마지막 문구를 검토하고 있었다."
        # SOURCE CH04 L746
        narrator "노트에는 여러 후보가 적혀 있었다."
        # SOURCE CH04 L748
        roman "앗,,, 이 문장은 어떠세요?"
        # SOURCE CH04 L750 [주인공]
        # SOURCE CH04 L752
        mc "좋은데요. 그런데 영상에는 조금 길지 않을까요?"
        # SOURCE CH04 L754
        roman "아…… 그렇죠."
        # SOURCE CH04 L756
        roman "그럼 조금 줄여볼까요……?"
        # SOURCE CH04 L758 [독백]
        # SOURCE CH04 L760
        narrator "나는 문장들을 하나씩 확인했다."
        # SOURCE CH04 L762
        narrator "그중에는 유독 여러 번 고쳐 쓴 흔적이 남은 문장도 있었다."
        # SOURCE CH04 L764 [주인공]
        # SOURCE CH04 L766
        mc "여기는 아예 빼도 될 것 같은데요."
        # SOURCE CH04 L768
        $ story_stage(faces={"roman": "surprised"})
        roman "……네?"
        # SOURCE CH04 L770 [주인공]
        # SOURCE CH04 L772
        mc "영상이 1분이라서요. 다른 문장으로도 충분히 설명할 수 있을 것 같아요."
        # SOURCE CH04 L774
        $ story_stage(faces={"roman": "sad"})
        roman "아……."
        # SOURCE CH04 L776 [독백]
        # SOURCE CH04 L778
        narrator "로만의 시선이 노트에 머물렀다."
        # SOURCE CH04 L780
        roman "그렇네요……."
        # SOURCE CH04 L782 [주인공]
        # SOURCE CH04 L784
        mc "혹시 마음에 안 드세요?"
        # SOURCE CH04 L786
        roman "아, 아니에요."
        # SOURCE CH04 L788
        roman "그냥…… 조금만 더 생각해 봐도 될까요?"
        # SOURCE CH04 L790 [주인공]
        # SOURCE CH04 L792
        mc "네, 물론이죠."
        # SOURCE CH04 L794 [독백]
        # SOURCE CH04 L796
        narrator "로만은 고개를 끄덕였다."
        # SOURCE CH04 L798
        narrator "하지만 아까까지 자연스럽게 이어지던 대화가 잠시 멈췄다."
        # SOURCE CH04 L800
        narrator "혹시 저 문장에 내가 모르는 의미가 있었던 걸까."
        # SOURCE CH04 L802 [FLAG] `ch04_conflict = roman_wording`
        $ story_flag("ch04_conflict", "roman_wording")
    # SOURCE CH04 L804 ### SC05-B. 시아 「웃기기만 하면 되는 건 아니야」
    elif ch04_partner == "sia":
        # 콘티: 시아 스탠딩 / 콘티를 보여줄 때 → 장난 장면을 덜자는 말에 펜을 멈춤.
        # SOURCE CH04 L806 [BG] 애니메이션과 작업실
        $ story_scene("animation", mode="emotion", cast=["sia"], light="day", location="애니메이션과 작업실 · 오후")
        # SOURCE CH04 L808
        $ story_stage(faces={"sia": "smug"})
        sia "자, 이 장면 봐봐."
        # SOURCE CH04 L810 [독백]
        # SOURCE CH04 L812
        narrator "시아는 시연 영상에 사용할 콘티를 보여줬다."
        # SOURCE CH04 L814
        narrator "캐릭터의 표정과 화면 전환까지 제법 세밀하게 그려져 있었다."
        # SOURCE CH04 L816 [주인공]
        # SOURCE CH04 L818
        mc "재미있네요. 그런데 이 부분은 조금 복잡한 것 같아요."
        # SOURCE CH04 L820
        sia "어디?"
        # SOURCE CH04 L822 [주인공]
        # SOURCE CH04 L824
        mc "여기요. 장난치는 장면이 길어서 체험 방법이 잘 안 보여요."
        # SOURCE CH04 L826
        sia "……아."
        # SOURCE CH04 L828
        sia "그럼 이 부분 줄이면 되겠네."
        # SOURCE CH04 L830 [주인공]
        # SOURCE CH04 L832
        mc "아예 웃긴 장면을 조금 덜 넣는 게 어떨까요?"
        # SOURCE CH04 L834
        $ story_stage(faces={"sia": "serious"})
        sia "……."
        # SOURCE CH04 L836 [독백]
        # SOURCE CH04 L838
        narrator "시아가 펜을 멈췄다."
        # SOURCE CH04 L840
        sia "뭐, 그럴 수도 있지."
        # SOURCE CH04 L842 [주인공]
        # SOURCE CH04 L844
        mc "시아 씨?"
        # SOURCE CH04 L846
        sia "아냐. 수정하면 돼."
        # SOURCE CH04 L848 [주인공]
        # SOURCE CH04 L850
        mc "꼭 전부 빼자는 뜻은 아니었는데요."
        # SOURCE CH04 L852
        sia "알아."
        # SOURCE CH04 L854
        sia "그냥 설명만 남기면 되잖아."
        # SOURCE CH04 L856 [독백]
        # SOURCE CH04 L858
        narrator "시아는 태블릿을 다시 바라봤다."
        # SOURCE CH04 L860
        narrator "평소 같으면 농담으로 받아쳤을 말이었다."
        # SOURCE CH04 L862
        narrator "그런데 지금은 뭔가 다르다."
        # SOURCE CH04 L864
        narrator "내가 너무 쉽게 말한 걸까."
        # SOURCE CH04 L866 [FLAG] `ch04_conflict = sia_creativity`
        $ story_flag("ch04_conflict", "sia_creativity")
    # SOURCE CH04 L868 ### SC05-C. 다림 「괜찮다는 말의 의미」
    elif ch04_partner == "darim":
        # 콘티: 다림 스탠딩 / 차분한 업무 설명 → 조심스러운 웃음.
        # SOURCE CH04 L870 [BG] 스터디룸
        $ story_scene("study", mode="emotion", cast=["darim"], light="day", location="스터디룸 · 오후")
        $ story_stage(faces={"darim": "serious"})
        # SOURCE CH04 L872
        darim "제출 자료는 거의 끝났는데, 확인할 게 몇 가지 남았어요."
        # SOURCE CH04 L874 [주인공]
        # SOURCE CH04 L876
        mc "어떤 건가요?"
        # SOURCE CH04 L878
        darim "최종 파일명도 맞춰야 하고, 촬영 자료도 정리해야 하고……."
        # SOURCE CH04 L880 [독백]
        # SOURCE CH04 L882
        narrator "다림은 해야 할 일을 하나씩 이야기했다."
        # SOURCE CH04 L884
        narrator "목록이 끝날 기미가 보이지 않았다."
        # SOURCE CH04 L886 [주인공]
        # SOURCE CH04 L888
        mc "선배, 그걸 전부 혼자 하시려고요?"
        # SOURCE CH04 L890
        darim "아, 괜찮아요. 제가 정리하는 게 편해서요."
        # SOURCE CH04 L892 [주인공]
        # SOURCE CH04 L894
        mc "그래도 너무 많잖아요."
        # SOURCE CH04 L896
        darim "금방 끝나요."
        # SOURCE CH04 L898 [주인공]
        # SOURCE CH04 L900
        mc "……선배는 항상 괜찮다고만 하시네요."
        # SOURCE CH04 L902
        $ story_stage(faces={"darim": "surprised"})
        darim "……."
        # SOURCE CH04 L904 [독백]
        # SOURCE CH04 L906
        narrator "다림이 노트북에서 눈을 뗐다."
        # SOURCE CH04 L908
        darim "그런가요?"
        # SOURCE CH04 L910 [주인공]
        # SOURCE CH04 L912
        mc "힘들어 보이셔서요. 제가 도와드려도 되는데……."
        # SOURCE CH04 L914
        darim "제가 그렇게 힘들어 보여요?"
        # SOURCE CH04 L916 [주인공]
        # SOURCE CH04 L918
        mc "아니, 그런 뜻은 아니고요."
        # SOURCE CH04 L920
        $ story_stage(faces={"darim": "happy"})
        darim "……후후. 무슨 말씀인지는 알겠어요."
        # SOURCE CH04 L922 [독백]
        # SOURCE CH04 L924
        narrator "다림은 웃었다."
        # SOURCE CH04 L926
        narrator "그런데 평소보다 조금 조심스러운 웃음이었다."
        # SOURCE CH04 L928
        darim "일단 이 부분까지만 정리할게요."
        # SOURCE CH04 L930 [주인공]
        # SOURCE CH04 L932
        mc "……네."
        # SOURCE CH04 L934 [독백]
        # SOURCE CH04 L936
        narrator "걱정해서 한 말이었는데."
        # SOURCE CH04 L938
        narrator "다림에게는 자신이 일을 못하고 있다는 지적처럼 들렸을지도 모른다."
        # SOURCE CH04 L940 [FLAG] `ch04_conflict = darim_workload`
        $ story_flag("ch04_conflict", "darim_workload")
    # SOURCE CH04 L942 ### SC05-D. 오므 「좋은 사진만 남기면 될까?」
    elif ch04_partner == "omu":
        # 콘티: 오므 스탠딩 / 사진을 보여줄 때 → 홍보 사진 선별 기준에서 의견이 갈림.
        # SOURCE CH04 L944 [BG] 사진 작업 공간
        # 콘티: 전용 사진 작업 공간을 배치할 위치. 지금은 기존 스터디룸 배경.
        $ story_scene("study", mode="emotion", cast=["omu"], light="day", location="사진 작업 공간 · 오후")
        # SOURCE CH04 L946
        omu "이거 봐라. 어때?"
        # SOURCE CH04 L948 [독백]
        # SOURCE CH04 L950
        narrator "오므가 시범 운영에서 찍은 사진들을 보여줬다."
        # SOURCE CH04 L952
        narrator "완성된 부스와 팀원들이 작업하던 모습이 섞여 있었다."
        # SOURCE CH04 L954 [주인공]
        # SOURCE CH04 L956
        mc "좋네요. 그런데 이 사진은 빼도 되지 않을까요?"
        # SOURCE CH04 L958
        omu "어느 거?"
        # SOURCE CH04 L960 [주인공]
        # SOURCE CH04 L962
        mc "여기요. 테이블이 조금 어수선해 보여서요."
        # SOURCE CH04 L964
        mc "홍보 영상이니까 깔끔한 사진 위주로 넣으면 어떨까요?"
        # SOURCE CH04 L966
        $ story_stage(faces={"omu": "serious"})
        omu "……."
        # SOURCE CH04 L968
        omu "니는 그렇게 생각하나?"
        # SOURCE CH04 L970 [주인공]
        # SOURCE CH04 L972
        mc "네. 아무래도 홍보용이니까요."
        # SOURCE CH04 L974
        omu "그것도 맞는 말인데……."
        # SOURCE CH04 L976 [독백]
        # SOURCE CH04 L978
        narrator "오므가 사진을 다시 바라봤다."
        # SOURCE CH04 L980
        omu "내는 이런 모습도 좋거든."
        # SOURCE CH04 L982 [주인공]
        # SOURCE CH04 L984
        mc "어떤 점이요?"
        # SOURCE CH04 L986
        omu "준비하는 과정이 보이잖아."
        # SOURCE CH04 L988
        omu "완성된 것만 보여주면 너무 꾸민 것 같기도 하고."
        # SOURCE CH04 L990 [주인공]
        # SOURCE CH04 L992
        mc "……그렇게 볼 수도 있겠네요."
        # SOURCE CH04 L994
        omu "뭐, 니 생각도 이해는 한다."
        # SOURCE CH04 L996 [독백]
        # SOURCE CH04 L998
        narrator "오므는 더 말하지 않고 사진을 넘겼다."
        # SOURCE CH04 L1000
        narrator "말이 강하게 들린 건 평소와 다를 바 없었다."
        # SOURCE CH04 L1002
        narrator "그런데 왜인지 내가 무언가 놓친 기분이었다."
        # SOURCE CH04 L1004 [FLAG] `ch04_conflict = omu_photo`
        $ story_flag("ch04_conflict", "omu_photo")
    # SOURCE CH04 L1006 ### SC05-E. 하린 「반듯하지 않은 계획」
    elif ch04_partner == "lumi":
        # 콘티: 하린 스탠딩 / 모형 설명 → 공간을 채우자는 말에 여유로운 기색이 사라짐.
        # SOURCE CH04 L1008 [BG] 건축학과 작업실
        $ story_scene("architecture", mode="emotion", cast=["lumi"], light="day", location="건축학과 작업실 · 오후")
        # SOURCE CH04 L1010
        lumi "여기까지 수정하면 될 것 같아요."
        # SOURCE CH04 L1012 [독백]
        # SOURCE CH04 L1014
        narrator "하린이 새로 만든 부스 모형을 보여줬다."
        # SOURCE CH04 L1016
        narrator "이전보다 전시 공간이 잘 정리되어 있었다."
        # SOURCE CH04 L1018 [주인공]
        # SOURCE CH04 L1020
        mc "좋네요. 그런데 이쪽에 전시물을 하나 더 넣으면 안 될까요?"
        # SOURCE CH04 L1022
        $ story_stage(faces={"lumi": "confused"})
        lumi "……여기요?"
        # SOURCE CH04 L1024 [주인공]
        # SOURCE CH04 L1026
        mc "네. 조금 비어 있는 것 같아서요."
        # SOURCE CH04 L1028
        $ story_stage(faces={"lumi": "serious"})
        lumi "남는 공간은 아니에요."
        # SOURCE CH04 L1030 [주인공]
        # SOURCE CH04 L1032
        mc "조금만 조정하면 될 것 같은데……."
        # SOURCE CH04 L1034
        lumi "……."
        # SOURCE CH04 L1036 [독백]
        # SOURCE CH04 L1038
        narrator "하린이 모형을 잠시 바라봤다."
        # SOURCE CH04 L1040
        lumi "그렇게 간단한 문제는 아니거든요."
        # SOURCE CH04 L1042 [주인공]
        # SOURCE CH04 L1044
        mc "아……."
        # SOURCE CH04 L1046
        lumi "방문객이 이동할 공간이라 일부러 비워둔 거예요."
        # SOURCE CH04 L1048 [주인공]
        # SOURCE CH04 L1050
        mc "제가 그 부분까지는 생각 못 했네요."
        # SOURCE CH04 L1052
        lumi "……."
        # SOURCE CH04 L1054
        lumi "아니에요. 설명을 안 한 제 잘못도 있죠."
        # SOURCE CH04 L1056 [독백]
        # SOURCE CH04 L1058
        $ story_stage(faces={"lumi": "happy"})
        narrator "하린은 작게 웃었다."
        # SOURCE CH04 L1060
        narrator "그런데 조금 전까지의 능글맞은 분위기는 사라져 있었다."
        # SOURCE CH04 L1062
        $ story_stage(faces={"lumi": "serious"})
        lumi "잠시만요. 이 부분부터 다시 확인할게요."
        # SOURCE CH04 L1064 [주인공]
        # SOURCE CH04 L1066
        mc "네."
        # SOURCE CH04 L1068 [독백]
        # SOURCE CH04 L1070
        narrator "도움이 될 거라고 생각했다."
        # SOURCE CH04 L1072
        narrator "그런데 내가 생각한 것보다 하린은 훨씬 많은 걸 고민해 둔 모양이다."
        # SOURCE CH04 L1074 [FLAG] `ch04_conflict = harin_design`
        $ story_flag("ch04_conflict", "harin_design")
    # SOURCE CH04 L1076 ### SC05 공통 마무리
    # SOURCE CH04 L1078 [BGM] Quiet Emotional
    $ play_bgm("emotional_warm")
    # SOURCE CH04 L1080 [독백]
    # SOURCE CH04 L1082
    narrator "별것 아닌 말이라고 생각했다."
    # SOURCE CH04 L1084
    narrator "도움이 됐으면 좋겠다는 마음도 있었다."
    # SOURCE CH04 L1086
    narrator "그런데 가까워졌다는 이유로 상대를 너무 잘 안다고 생각했던 걸까."
    # SOURCE CH04 L1088
    narrator "조금 더 이야기를 나눠야겠다."
    # SOURCE CH04 L1090 [SCENE 05 END → 선택한 개인 이벤트로 이동]
    jump ch04_sc06

# CH04 · SC06 개인 이벤트 / 대사와 콘티
# 원고 SHA256: 5a73371c2ee5d24d89fbc8ec98313dba5812b8024e089260f51c96d5bcdd1460
# [ANIM] 주석은 별도 미세 애니메이션의 원고 연출을 기록한다.

# 원고 L1092 SCENE 06. 너는 원래 그런 사람이었어?
# 원고 L1094 오후 5:10 · 히로인별 개인 이벤트 · 미세 애니메이션 도입
label ch04_sc06:
    $ phone_timeline_enter("CH04", "ch04_sc06")
    if ch04_partner == "roman":
        call ch04_sc06_roman from ch04_sc06_return_roman
    elif ch04_partner == "sia":
        call ch04_sc06_sia from ch04_sc06_return_sia
    elif ch04_partner == "darim":
        call ch04_sc06_darim from ch04_sc06_return_darim
    elif ch04_partner == "omu":
        call ch04_sc06_omu from ch04_sc06_return_omu
    elif ch04_partner == "lumi":
        call ch04_sc06_lumi from ch04_sc06_return_lumi
    jump ch04_sc07

# 원고 L1100 SC06-A. 로만 「읽지 않아도 되는 문장」
label ch04_sc06_roman:
    $ phone_timeline_enter("CH04", "ch04_sc06_roman")
    # 원고 L1102: [BG] 도서관 창가 · 늦은 오후
    $ story_scene("library", mode="emotion", cast=["roman"], light="evening", location="도서관 창가 · 늦은 오후")
    # 원고 L1104: [BGM] Gentle Emotional
    $ play_bgm("quiet_library")
    # 원고 L1106: [ANIM] 로만 · 느린 눈 깜빡임, 머리카락 끝의 미세한 움직임
    # 원고 L1110
    narrator "로만은 노트를 펼친 채 무언가를 고민하고 있었다."
    # 원고 L1112
    narrator "나는 잠시 망설이다 말을 걸었다."
    # 원고 L1116
    mc "로만 씨."
    # 원고 L1118
    $ story_stage(faces={"roman": "surprised"})
    roman "앗,,, 네?"
    # 원고 L1122
    mc "아까는 제가 너무 쉽게 말한 것 같아요."
    # 원고 L1124
    $ story_stage(faces={"roman": "embarrassed"})
    roman "……."
    # 원고 L1128
    mc "그 문장, 여러 번 고쳐 쓰신 거죠?"
    # 원고 L1130
    $ cg_start("ch04_private_roman")
    roman "아…… 네."
    # 원고 L1132
    roman "사실 조금 오래 생각한 문장이었어요."
    # 원고 L1136
    mc "그랬군요."
    # 원고 L1138
    roman "근데 영상에는 확실히 길 것 같아서……."
    # 원고 L1142
    mc "줄이자는 의견은 여전히 맞을 수도 있어요."
    # 원고 L1144
    mc "그런데 왜 그 문장을 쓰셨는지 먼저 여쭤봤어야 했는데."
    # 원고 L1148
    narrator "로만은 펜을 내려놓았다."
    # 원고 L1150
    roman "제가 좋아하는 문장이 있거든요."
    # 원고 L1154
    mc "어떤 문장인가요?"
    # 원고 L1156
    roman "음…… 같은 글을 읽어도 사람마다 다르게 받아들이는 이야기요."
    # 원고 L1158
    roman "어떤 사람은 슬프다고 하고…… 어떤 사람은 따뜻하다고 할 수도 있고요."
    # 원고 L1162
    mc "그래서 그런 느낌을 넣고 싶으셨군요."
    # 원고 L1164
    roman "……네."
    # 원고 L1168
    mc "그럼 영상에서는 짧게 소개하고, 원래 문장은 전시에 남겨두면 어떨까요?"
    # 원고 L1170
    roman "……!"
    # 원고 L1172
    roman "그렇게 해도 될까요?"
    # 원고 L1176
    mc "물론이죠. 문장을 전부 없앨 필요는 없으니까요."
    # 원고 L1180
    narrator "로만은 노트를 다시 바라봤다."
    # 원고 L1182
    roman "앗,,, 고마워요."
    # 원고 L1184
    roman "사실…… 제가 쓴 글을 다른 사람이 읽는 게 조금 부끄럽거든요."
    # 원고 L1188
    mc "그럴 수 있죠."
    # 원고 L1190
    $ cg_start("ch04_private_roman_shy", transition=0.38)
    roman "그래도 [player_name] 씨에게는 보여드리고 싶었어요."
    # 원고 L1194
    mc "저한테요?"
    # 원고 L1196
    roman "네……."
    # 원고 L1198
    roman "제가 쓴 걸 항상 재미있게 읽어주시니까요."
    # 원고 L1200
    roman "가끔 장난도 받아주시고……."
    # 원고 L1204
    narrator "예상하지 못한 말이었다."
    # 원고 L1206
    narrator "로만은 노트의 다음 장을 조심스럽게 넘겼다."
    # 원고 L1208
    roman "그런데 여기는……."
    # 원고 L1212
    narrator "로만이 손으로 한쪽 페이지를 가렸다."
    # 원고 L1214
    roman "아직 안 보여드리고 싶어요."
    # 원고 L1218
    mc "그럼 안 보여주셔도 돼요."
    # 원고 L1220
    roman "……네?"
    # 원고 L1224
    mc "나중에 보여주고 싶으실 때 보여주세요."
    # 원고 L1228
    narrator "로만은 잠시 나를 바라봤다."
    # 원고 L1230
    narrator "그러고는 작은 목소리로 물었다."
    # 원고 L1232
    roman "그럼…… 기다려주실래요?"
    # 원고 L1234: ### 선택지 · 로만의 부탁
    menu:
        # 원고 L1236
        "네. 천천히 하셔도 괜찮아요.":
            # 원고 L1238
            roman "……고마워요."
            # 원고 L1240
            roman "그렇게 말씀해 주시니까 마음이 조금 편해져요."
            # 원고 L1242: 로만 신뢰도 +2
            $ story_apply("ch04_sc06_roman_a", trust={"roman": 2})
        # 원고 L1244
        "언젠가 읽어볼 수 있으면 좋겠네요.":
            # 원고 L1245
            roman "앗,,, 그럼 저도 조금 더 열심히 써볼게요."
            # 원고 L1247
            roman "나중에 꼭 읽어주세요."
            # 원고 L1249: 로만 호감도 +1
            $ story_apply("ch04_sc06_roman_b", affection={"roman": 1})
        # 원고 L1251
        "그럼 나중에 보여주시는 걸로 약속할까요?":
            # 원고 L1252
            roman "후후……."
            # 원고 L1254
            roman "약속이에요. 대신 재촉하시면 벌칙이에요."
            # 원고 L1256
            mc "제가 벌칙을 받는 건가요?"
            # 원고 L1258
            roman "네. 제가 정한 규칙이거든요."
            # 원고 L1260: 로만 장난 이벤트 플래그
            $ story_apply("ch04_sc06_roman_c", values={"ch04_roman_playful_event": True})
    # 원고 L1263: [공통 복귀]
    # 원고 L1267
    narrator "로만은 다시 글을 고치기 시작했다."
    # 원고 L1269
    narrator "아까보다 펜을 움직이는 속도가 조금 빨라진 것 같았다."
    # 원고 L1271
    roman "저기……."
    # 원고 L1275
    mc "네?"
    # 원고 L1277
    roman "다음에 도서관 오실 때……."
    # 원고 L1279
    roman "같이 책도 읽으실래요?"
    # 원고 L1283
    mc "좋아요. 시간 맞춰봐요."
    # 원고 L1285
    roman "……후후."
    # 원고 L1289
    narrator "로만은 작게 웃었다."
    # 원고 L1291
    narrator "처음 만났을 때는 말 한마디 건네는 것도 조심스러워했던 사람이다."
    # 원고 L1293
    narrator "그런데 이제는 먼저 약속을 제안한다."
    # 원고 L1295
    narrator "그 변화가 조금 기뻤다."
    # 원고 L1297: [FLAG] `ch04_personal_promise["roman"] = True`
    $ ch04_personal_promise["roman"] = True
    $ secret_note_unlock("roman", 2)
    # 원고 L1299: [SCENE 06-A END]
    $ cg_end(restore=False)
    return

# 원고 L1301 SC06-B. 시아 「농담으로 하지 마」
label ch04_sc06_sia:
    $ phone_timeline_enter("CH04", "ch04_sc06_sia")
    # 원고 L1303: [BG] 애니메이션과 작업실 · 저녁
    $ story_scene("animation", mode="emotion", cast=["sia"], light="evening", location="애니메이션과 작업실 · 저녁")
    # 원고 L1305: [BGM] Calm Workshop
    $ play_bgm("warm_workshop")
    # 원고 L1307: [ANIM] 시아 · 눈 깜빡임, 머리카락의 미세한 움직임
    # 원고 L1311
    narrator "시아는 태블릿 앞에 앉아 있었다."
    # 원고 L1313
    narrator "평소 같으면 내가 들어오자마자 장난을 쳤을 텐데, 이번에는 화면만 바라보고 있었다."
    # 원고 L1317
    mc "시아 씨."
    # 원고 L1319
    sia "어."
    # 원고 L1323
    mc "아까 말씀드린 콘티 이야기, 조금 더 해도 될까요?"
    # 원고 L1325
    sia "……왜?"
    # 원고 L1329
    mc "제가 너무 쉽게 말한 것 같아서요."
    # 원고 L1331
    $ cg_start("ch04_private_sia_tablet")
    sia "아, 그거?"
    # 원고 L1333
    sia "괜찮아. 수정하면 되지."
    # 원고 L1337
    mc "그래도 시아 씨가 왜 그런 장면을 넣었는지 먼저 들어봤어야 했는데요."
    # 원고 L1339
    sia "……."
    # 원고 L1343
    narrator "시아가 펜을 내려놓았다."
    # 원고 L1345
    $ cg_start("ch04_private_sia", transition=0.38)
    sia "솔직히 말하면……."
    # 원고 L1347
    sia "사람들이 우리 부스 보고 좀 웃었으면 좋겠거든."
    # 원고 L1351
    mc "네."
    # 원고 L1353
    sia "다들 축제 와서 즐기고 싶은 거잖아."
    # 원고 L1355
    sia "그냥 설명만 보고 가면 재미없을 것 같아서."
    # 원고 L1359
    mc "그렇죠."
    # 원고 L1361
    sia "그래서 웃긴 부분을 넣은 거야."
    # 원고 L1363
    sia "근데 네가 그거 줄여도 되지 않냐고 하니까……."
    # 원고 L1365
    sia "내가 괜히 쓸데없는 걸 만들었나 싶더라."
    # 원고 L1369
    narrator "시아가 이런 말을 하는 건 처음이었다."
    # 원고 L1371
    narrator "평소라면 말장난으로 넘겼을 사람인데."
    # 원고 L1375
    mc "그렇게 생각하지 않으셨으면 좋겠어요."
    # 원고 L1377
    sia "……."
    # 원고 L1381
    mc "제가 말한 건 재미있는 부분이 필요 없다는 뜻이 아니었어요."
    # 원고 L1383
    mc "설명할 내용이랑 웃긴 부분을 조금 나눠보자는 뜻이었어요."
    # 원고 L1385
    sia "……그럼 웃긴 건 남겨도 돼?"
    # 원고 L1389
    mc "당연하죠."
    # 원고 L1391
    mc "그게 시아 씨가 잘하는 거잖아요."
    # 원고 L1395
    narrator "시아는 잠시 나를 바라봤다."
    # 원고 L1397
    sia "……야."
    # 원고 L1401
    mc "네?"
    # 원고 L1403
    sia "너 그런 말 되게 자연스럽게 한다?"
    # 원고 L1407
    mc "어떤 말이요?"
    # 원고 L1409
    sia "장점이니 뭐니."
    # 원고 L1413
    mc "그냥 사실대로 말씀드리는 건데요."
    # 원고 L1415
    sia "……."
    # 원고 L1417: [ANIM] 시아가 잠시 눈을 깜빡인 뒤 시선을 피한다.
    # 원고 L1419
    sia "……아, 진짜."
    # 원고 L1423
    mc "왜 그러세요?"
    # 원고 L1425
    sia "아니야."
    # 원고 L1427
    sia "그냥……."
    # 원고 L1429
    sia "그런 말은 장난으로 하지 마."
    # 원고 L1433
    mc "장난 아닌데요."
    # 원고 L1435
    sia "……."
    # 원고 L1439
    narrator "시아의 손이 멈췄다."
    # 원고 L1441
    narrator "잠깐 정적이 흘렀다."
    # 원고 L1443
    sia "응 아니야~"
    # 원고 L1445
    sia "……."
    # 원고 L1447
    sia "아, 이건 좀 아니네."
    # 원고 L1451
    mc "뭐가요?"
    # 원고 L1453
    sia "내가 지금 장난치고 싶은 게 아닌데 자꾸 장난치려고 해서."
    # 원고 L1457
    narrator "처음 듣는 말이었다."
    # 원고 L1461
    mc "그럼 장난 안 치셔도 돼요."
    # 원고 L1463
    sia "……."
    # 원고 L1465
    sia "그래."
    # 원고 L1467
    sia "고맙다."
    # 원고 L1469: ### 선택지 · 시아의 진심
    menu:
        # 원고 L1471
        "진지하게 작업하시는 모습도 멋있어요.":
            # 원고 L1472
            sia "……."
            # 원고 L1474
            sia "너 진짜 사람 당황하게 하는 재주 있다."
            # 원고 L1476: 시아 호감도 +2
            $ story_apply("ch04_sc06_sia_a", affection={"sia": 2})
        # 원고 L1478
        "다음 콘티도 같이 고민해볼까요?":
            # 원고 L1479
            sia "오케이."
            # 원고 L1481
            sia "그럼 앞으로도 감상 담당 계속해라."
            # 원고 L1483
            mc "급여 협상은 안 되는 건가요?"
            # 원고 L1485
            sia "응 아니야~"
            # 원고 L1487: 시아 신뢰도 +2
            $ story_apply("ch04_sc06_sia_b", trust={"sia": 2})
        # 원고 L1489
        "그럼 이번엔 제가 먼저 장난쳐볼까요?":
            # 원고 L1490
            sia "오?"
            # 원고 L1492
            sia "드디어 제자가 스승한테 도전하는 건가?"
            # 원고 L1494
            mc "제가 언제 제자가 됐나요?"
            # 원고 L1496
            sia "방금."
            # 원고 L1498: 시아 특별 장난 이벤트
            $ story_apply("ch04_sc06_sia_c", values={"ch04_sia_special_prank": True})
    # 원고 L1502: [공통 복귀]
    # 원고 L1506
    narrator "시아는 다시 태블릿을 켰다."
    # 원고 L1508
    sia "야, 그러면."
    # 원고 L1512
    mc "네?"
    # 원고 L1514
    sia "축제 끝나고……."
    # 원고 L1516
    sia "내가 개인적으로 그리는 웹툰도 한번 볼래?"
    # 원고 L1520
    mc "좋죠. 보여주시면 재미있게 읽을게요."
    # 원고 L1522
    sia "……좋아."
    # 원고 L1524
    sia "그럼 약속이다."
    # 원고 L1528
    narrator "이번에는 농담을 덧붙이지 않았다."
    # 원고 L1530
    narrator "평소와 다른 모습이었다."
    # 원고 L1532
    narrator "그런데 이상하게 싫지 않았다."
    # 원고 L1534: [FLAG] `ch04_personal_promise["sia"] = True`
    $ ch04_personal_promise["sia"] = True
    $ secret_note_unlock("sia", 2)
    # 원고 L1536: [SCENE 06-B END]
    $ cg_end(restore=False)
    return

# 원고 L1538 SC06-C. 다림 「괜찮다고 말하지 않아도」
label ch04_sc06_darim:
    $ phone_timeline_enter("CH04", "ch04_sc06_darim")
    # 원고 L1540: [BG] 스터디룸 · 저녁
    $ story_scene("study", mode="emotion", cast=["darim"], light="evening", location="스터디룸 · 저녁")
    # 원고 L1542: [BGM] Emotional Warm
    $ play_bgm("emotional_warm")
    # 원고 L1544: [ANIM] 다림 · 부드러운 눈 깜빡임과 미세 호흡
    # 원고 L1548
    narrator "다림은 노트북 앞에 앉아 있었다."
    # 원고 L1550
    narrator "화면에는 제출 자료와 일정표가 가득했다."
    # 원고 L1554
    mc "선배."
    # 원고 L1556
    darim "네?"
    # 원고 L1560
    mc "아까 제가 한 말 때문에 기분 상하셨어요?"
    # 원고 L1562
    $ story_stage(faces={"darim": "serious"})
    darim "……."
    # 원고 L1564
    $ cg_start("ch04_private_darim")
    darim "조금 놀라기는 했어요."
    # 원고 L1568
    mc "역시 그랬군요."
    # 원고 L1570
    darim "그렇지만 틀린 말은 아니었죠."
    # 원고 L1574
    narrator "다림은 노트북을 덮었다."
    # 원고 L1576
    darim "저도 가끔 제가 할 수 있는 일을 너무 많이 적어놓을 때가 있어요."
    # 원고 L1580
    mc "네."
    # 원고 L1582
    darim "그런데 누가 갑자기 그걸 지적하면……."
    # 원고 L1584
    darim "제가 일을 못하고 있는 것처럼 느껴질 때도 있거든요."
    # 원고 L1588
    mc "아……."
    # 원고 L1590
    darim "물론 그런 뜻으로 말씀하신 건 아니라는 건 알아요."
    # 원고 L1594
    mc "그냥 선배가 너무 바빠 보이셔서요."
    # 원고 L1596
    darim "네. 알고 있어요."
    # 원고 L1600
    narrator "다림은 작게 웃었다."
    $ cg_start("ch04_private_darim_smile", transition=0.38)
    # 원고 L1602
    darim "조금 이상하죠?"
    # 원고 L1606
    mc "뭐가요?"
    # 원고 L1608
    darim "도와준다고 하면 고마우면서도……."
    # 원고 L1610
    darim "제가 맡은 일은 잘하고 싶은 마음도 있으니까요."
    # 원고 L1614
    mc "이상하지 않아요."
    # 원고 L1616
    mc "자기가 맡은 일을 잘하고 싶은 건 당연하죠."
    # 원고 L1618
    darim "……."
    # 원고 L1622
    mc "그런데 같이 하는 프로젝트잖아요."
    # 원고 L1624
    mc "일을 나눈다고 선배가 잘하신 게 없어지는 건 아니잖아요."
    # 원고 L1628
    narrator "다림은 잠시 말이 없었다."
    # 원고 L1630
    darim "……그러네요."
    # 원고 L1632
    darim "생각해보니 그렇죠."
    # 원고 L1636
    mc "그럼 저도 같이 정리해도 될까요?"
    # 원고 L1638
    darim "……좋아요."
    # 원고 L1642
    narrator "우리는 일정표를 다시 살펴봤다."
    # 원고 L1644
    narrator "다림이 맡아둔 일 중 일부는 내가 도울 수 있었고, 다른 팀원들에게 분담할 수 있는 일도 있었다."
    # 원고 L1646
    darim "이건 제가 계속 맡고……."
    # 원고 L1650
    mc "이 부분은 제가 도울게요."
    # 원고 L1652
    darim "그럼 부탁드릴게요."
    # 원고 L1656
    narrator "몇 분 뒤 복잡했던 표가 조금 정리됐다."
    # 원고 L1658
    darim "……후우."
    # 원고 L1662
    mc "이제 좀 괜찮으세요?"
    # 원고 L1664
    darim "네."
    # 원고 L1666
    darim "이번에는 정말 괜찮아요."
    # 원고 L1670
    narrator "다림이 부드럽게 웃었다."
    # 원고 L1672
    darim "그런데 [player_name] 씨."
    # 원고 L1676
    mc "네?"
    # 원고 L1678
    darim "저 이렇게 도움받아도 괜찮은 걸까요?"
    # 원고 L1682
    mc "오늘 선배도 하실 일을 많이 하셨잖아요."
    # 원고 L1684
    darim "후후."
    # 원고 L1686
    darim "그럼 다음에는 제가 도와드릴게요."
    # 원고 L1690
    mc "좋아요."
    # 원고 L1692
    darim "……아."
    # 원고 L1694
    darim "그런데 다음에는 일 말고 다른 것도 하고 싶네요."
    # 원고 L1698
    mc "예를 들면요?"
    # 원고 L1700
    darim "게임이라든가."
    # 원고 L1702
    darim "카페에서 그냥 이야기하는 것도 좋고요."
    # 원고 L1704: ### 선택지 · 다림의 제안
    menu:
        # 원고 L1706
        "선배랑 있으면 편해서 좋아요.":
            # 원고 L1707
            darim "……저도 그래요."
            # 원고 L1709
            darim "그래서 그런 시간을 조금 더 보내고 싶었어요."
            # 원고 L1711: 다림 호감도 +2
            $ story_apply("ch04_sc06_darim_a", affection={"darim": 2})
        # 원고 L1713
        "다음에는 편하게 쉬는 시간을 만들어봐요.":
            # 원고 L1714
            darim "후후. 그럼 다음에는 진짜 쉬는 시간으로 잡아봐요."
            # 원고 L1716: 다림 신뢰도 +2
            $ story_apply("ch04_sc06_darim_b", trust={"darim": 2})
        # 원고 L1718
        "게임 약속은 아직 유효하죠?":
            # 원고 L1719
            darim "물론이죠."
            # 원고 L1721
            darim "다만 이번에도 제가 이길 거예요."
            # 원고 L1723
            mc "벌써 승리 선언하시는 건가요?"
            # 원고 L1725
            darim "준비된 자신감이죠. 후후."
            # 원고 L1727: 다림 게임 약속 이벤트
            $ story_apply("ch04_sc06_darim_c", values={"ch04_darim_game_promise": True})
    # 원고 L1731: [공통 복귀]
    # 원고 L1735
    narrator "다림은 노트북을 가방에 넣었다."
    # 원고 L1737
    darim "오늘은 여기까지 할까요?"
    # 원고 L1741
    mc "네. 오늘도 고생 많으셨어요."
    # 원고 L1743
    darim "……고마워요."
    # 원고 L1747
    mc "저야말로요."
    # 원고 L1751
    narrator "평소보다 조금 더 솔직한 모습이었다."
    # 원고 L1753
    narrator "차분하고 믿음직한 선배라고만 생각했는데."
    # 원고 L1755
    narrator "그 선배도 가끔은 누군가에게 기대고 싶은 모양이다."
    # 원고 L1757
    narrator "그걸 알게 된 게 이상하게 기뻤다."
    # 원고 L1759: [FLAG] `ch04_personal_promise["darim"] = True`
    $ ch04_personal_promise["darim"] = True
    $ secret_note_unlock("darim", 2)
    # 원고 L1761: [SCENE 06-C END]
    $ cg_end(restore=False)
    return

# 원고 L1763 SC06-D. 오므 「사진에서 지우지 않은 것」
label ch04_sc06_omu:
    $ phone_timeline_enter("CH04", "ch04_sc06_omu")
    # 원고 L1765: [BG] 사진 작업 공간 · 저녁
    # 콘티 임시 배경: 사진 작업 공간은 기존 스터디룸 배경을 사용한다.
    $ story_scene("study", mode="emotion", cast=["omu"], light="evening", location="사진 작업 공간 · 저녁")
    # 원고 L1767: [BGM] Gentle Evening
    $ play_bgm("evening_warm")
    # 원고 L1769: [ANIM] 오므 · 눈 깜빡임, 머리카락 끝 미세 움직임
    # 원고 L1773
    narrator "오므는 노트북으로 사진을 정리하고 있었다."
    # 원고 L1775
    narrator "화면에는 지난 시범 운영 당시 찍은 사진이 나란히 떠 있었다."
    # 원고 L1779
    mc "오므 씨."
    # 원고 L1781
    omu "어. 와?"
    # 원고 L1785
    mc "아까 사진 이야기 때문에요."
    # 원고 L1787
    $ story_stage(faces={"omu": "serious"})
    omu "사진 빼자는 거?"
    # 원고 L1791
    mc "네. 제가 너무 쉽게 말한 것 같아서요."
    # 원고 L1793
    $ cg_start("ch04_private_omu")
    omu "뭐, 그럴 수도 있지."
    # 원고 L1797
    mc "홍보 영상이니까 예쁜 사진만 넣으면 된다고 생각했거든요."
    # 원고 L1799
    omu "그것도 맞는 말이다."
    # 원고 L1801
    omu "근데 나는 사진이 꼭 예뻐야 좋은 건 아니라고 생각하거든."
    # 원고 L1805
    mc "어떤 의미예요?"
    # 원고 L1807
    omu "이것 좀 봐라."
    # 원고 L1811
    narrator "오므는 작업 도중 찍었던 사진을 확대했다."
    # 원고 L1813
    narrator "테이블 위에는 구겨진 종이가 있었고, 의자는 조금 비뚤어져 있었다."
    # 원고 L1815
    omu "이거 좀 지저분하지?"
    # 원고 L1819
    mc "조금요."
    # 원고 L1821
    omu "근데 그날 우리가 뭘 했는지 다 보이잖아."
    # 원고 L1823
    omu "준비하다 실수도 하고, 다시 고치고."
    # 원고 L1825
    omu "그런 게 좋은 거지."
    # 원고 L1829
    mc "……."
    # 원고 L1833
    narrator "사진을 다시 바라봤다."
    # 원고 L1835
    narrator "처음에는 그냥 어수선해 보였던 테이블이었다."
    # 원고 L1837
    narrator "그런데 자세히 보니 누가 어디에 앉았는지, 어떤 작업을 하고 있었는지 떠올랐다."
    # 원고 L1841
    mc "그러네요. 이때 진짜 정신없었는데."
    # 원고 L1843
    omu "그렇지?"
    # 원고 L1845
    omu "시아는 종이 떨어뜨리고, 로만이는 질문 카드 정리하고."
    # 원고 L1849
    mc "다림 선배는 일정표 정리하셨죠."
    # 원고 L1851
    omu "하린 선배는 부스 모형 고치고."
    # 원고 L1855
    mc "오므 씨는 사진 찍고요."
    # 원고 L1857
    omu "어."
    # 원고 L1861
    mc "그럼 저는 뭘 하고 있었죠?"
    # 원고 L1863
    omu "니?"
    # 원고 L1865
    omu "……여기저기 왔다 갔다 하면서 도와줬잖아."
    # 원고 L1869
    mc "그랬나요?"
    # 원고 L1871
    omu "어."
    # 원고 L1873
    omu "그러니까 그때 분위기가 기억에 남는 거지."
    # 원고 L1877
    narrator "오므는 다른 사진을 열었다."
    # 원고 L1879
    narrator "그 사진에는 CH03에서 보여준 빈 의자가 담겨 있었다."
    # 원고 L1881
    omu "이것도 마음에 들었는데."
    # 원고 L1883
    omu "오늘 다시 보니까 아까 사진도 괜찮네."
    # 원고 L1887
    mc "어느 쪽이 더 좋아요?"
    # 원고 L1889
    omu "음……."
    # 원고 L1891
    omu "못 고르겠다."
    # 원고 L1895
    mc "오므 씨도 못 고르는 게 있네요."
    # 원고 L1897
    omu "와, 니 나를 뭘로 보는데."
    # 원고 L1901
    mc "사진은 바로 고르실 줄 알았죠."
    # 원고 L1903
    omu "좋아하는 거라 더 고민되는 것도 있다."
    # 원고 L1907
    narrator "오므는 아무렇지도 않게 말했다."
    # 원고 L1909
    narrator "그런데 그 말이 이상하게 오래 남았다."
    # 원고 L1911: ### 선택지 · 오므의 사진
    menu:
        # 원고 L1913
        "완성된 모습만큼 과정도 중요하겠네요.":
            # 어떤 답을 골라도 선택 직후 미소 컷으로 부드럽게 전환한다.
            $ cg_start("ch04_private_omu_smile", transition=0.38)
            # 원고 L1914
            omu "어. 내가 하고 싶었던 말이 그거다."
            # 원고 L1916: 오므 신뢰도 +2
            $ story_apply("ch04_sc06_omu_a", trust={"omu": 2})
        # 원고 L1918
        "사진을 좋아하시는 이유를 조금 알 것 같아요.":
            $ cg_start("ch04_private_omu_smile", transition=0.38)
            # 원고 L1919
            omu "……그라나?"
            # 원고 L1921
            omu "그럼 좀 다행이네."
            # 원고 L1923: 오므 호감도 +2
            $ story_apply("ch04_sc06_omu_b", affection={"omu": 2})
        # 원고 L1925
        "그럼 두 사진 다 넣을 방법을 찾아볼까요?":
            $ cg_start("ch04_private_omu_smile", transition=0.38)
            # 원고 L1926
            omu "오, 그거 괜찮네."
            # 원고 L1928
            omu "과정이랑 완성된 모습으로 나눠도 되겠다."
            # 원고 L1930: 오므 전시 아이디어 플래그
            $ story_apply("ch04_sc06_omu_c", values={"ch04_omu_exhibition_idea": True})
    # 원고 L1933: [공통 복귀]
    # 원고 L1937
    narrator "우리는 사진을 다시 정리했다."
    # 원고 L1939
    narrator "완성된 부스 사진뿐 아니라, 함께 준비하던 순간도 영상에 일부 넣기로 했다."
    # 원고 L1941
    omu "오늘 같이 봐줘서 고맙다."
    # 원고 L1945
    mc "저도 재미있었어요."
    # 원고 L1947
    omu "……."
    # 원고 L1949
    omu "야, 니 다음에 시간 되나?"
    # 원고 L1953
    mc "왜요?"
    # 원고 L1955
    omu "사진 찍으러 갈 건데."
    # 원고 L1957
    omu "이번에는 학교 말고 다른 데도 가볼까 싶어서."
    # 원고 L1961
    mc "좋아요. 같이 가요."
    # 원고 L1963
    omu "……어."
    # 원고 L1965
    omu "그럼 나중에 연락할게."
    # 원고 L1969
    narrator "오므는 다시 화면을 바라봤다."
    # 원고 L1971
    narrator "그런데 아까보다 조금 기분이 좋아 보였다."
    # 원고 L1973: [FLAG] `ch04_personal_promise["omu"] = True`
    $ ch04_personal_promise["omu"] = True
    $ secret_note_unlock("omu", 2)
    # 원고 L1975: [SCENE 06-D END]
    $ cg_end(restore=False)
    return

# 원고 L1977 SC06-E. 하린 「틀어진 선 하나」
label ch04_sc06_lumi:
    $ phone_timeline_enter("CH04", "ch04_sc06_lumi")
    # 원고 L1979: [BG] 건축학과 작업실 · 저녁
    $ story_scene("architecture", mode="emotion", cast=["lumi"], light="evening", location="건축학과 작업실 · 저녁")
    # 원고 L1981: [BGM] Calm Emotional
    $ play_bgm("emotional_warm")
    # 원고 L1983: [ANIM] 하린 · 자연스러운 눈 깜빡임, 미세한 호흡
    # 원고 L1987
    narrator "하린은 모형 앞에 앉아 있었다."
    # 원고 L1989
    narrator "책상에는 자와 작은 종이 조각들이 놓여 있었다."
    # 원고 L1993
    mc "하린 선배."
    # 원고 L1995
    lumi "왔어요?"
    # 원고 L1999
    mc "네. 아까 말씀드린 것 때문에요."
    # 원고 L2001
    $ story_stage(faces={"lumi": "serious"})
    lumi "……아."
    # 원고 L2003
    $ cg_start("ch04_private_lumi")
    lumi "그거요?"
    # 원고 L2007
    mc "제가 너무 쉽게 말한 것 같아서요."
    # 원고 L2009
    lumi "……."
    # 원고 L2013
    mc "그 공간을 왜 비워두셨는지 제대로 들어보지도 않았잖아요."
    # 원고 L2015
    lumi "……그랬죠."
    # 원고 L2019
    narrator "하린은 모형을 조금 돌렸다."
    # 원고 L2021
    lumi "사실 그 부분은 몇 번이나 수정한 곳이었어요."
    # 원고 L2023
    lumi "방문객이 지나가야 하니까 일부러 넓게 비워둔 거거든."
    # 원고 L2027
    mc "네."
    # 원고 L2029
    lumi "근데 설명을 안 했으니 남는 공간처럼 보였을 수도 있겠네요."
    # 원고 L2033
    mc "그래도 먼저 여쭤봤어야 했는데요."
    # 원고 L2035
    lumi "그렇게까지 신경 쓰실 필요는 없어요."
    # 원고 L2039
    mc "그래도 신경 쓰이네요."
    # 원고 L2041
    lumi "……왜요?"
    # 원고 L2045
    mc "선배가 열심히 만드신 거잖아요."
    # 원고 L2049
    narrator "하린은 잠시 말이 없었다."
    # 원고 L2051
    lumi "……그렇죠."
    # 원고 L2053
    lumi "열심히 만들기는 했어요."
    # 원고 L2057
    narrator "하린은 모형의 작은 벽을 손끝으로 눌렀다."
    # 원고 L2059
    narrator "그 순간 접착이 약해졌던 부분이 떨어졌다."
    # 원고 L2061: [SFX] 종이 조각 떨어지는 소리
    $ story_sfx("paper")
    # 원고 L2065
    mc "어?"
    # 원고 L2067
    lumi "……아."
    # 원고 L2071
    narrator "모형의 벽 하나가 옆으로 기울었다."
    # 원고 L2075
    mc "괜찮으세요?"
    # 원고 L2077
    lumi "……괜찮아요."
    # 원고 L2079
    lumi "다시 붙이면 되니까."
    # 원고 L2083
    narrator "하린은 떨어진 부분을 집어 들었다."
    # 원고 L2085
    narrator "평소 같으면 바로 농담 한마디쯤 했을 텐데."
    # 원고 L2087
    narrator "이번에는 조용했다."
    # 원고 L2091
    mc "제가 도와드릴까요?"
    # 원고 L2093
    lumi "……."
    # 원고 L2095
    lumi "조금만 기다려줄래요?"
    # 원고 L2099
    mc "네."
    # 원고 L2103
    narrator "나는 옆에 앉아 하린이 모형을 확인하는 모습을 지켜봤다."
    # 원고 L2105
    narrator "잠시 뒤 하린이 입을 열었다."
    # 원고 L2107
    lumi "있잖아요."
    # 원고 L2111
    mc "네?"
    # 원고 L2113
    lumi "저는 이런 게 조금 신경 쓰여요."
    # 원고 L2115
    lumi "작은 부분 하나가 어긋난 건데."
    # 원고 L2117
    lumi "다른 건 다 괜찮아도 자꾸 그쪽에 눈이 가거든."
    # 원고 L2121
    mc "그럴 수 있죠."
    # 원고 L2123
    lumi "……."
    # 원고 L2125
    lumi "평소에는 별것 아닌 척하는 게 편한데."
    # 원고 L2127
    lumi "막상 제가 만든 것에서는 잘 안 되네."
    # 원고 L2131
    narrator "하린은 작게 웃었다."
    # 원고 L2133
    lumi "좀 의외죠?"
    # 원고 L2137
    mc "조금요."
    # 원고 L2139
    mc "그런데 그것도 선배 모습이잖아요."
    # 원고 L2141
    lumi "……."
    # 원고 L2145
    mc "항상 여유로우실 필요는 없죠."
    # 원고 L2149
    narrator "하린이 나를 바라봤다."
    # 원고 L2151: [ANIM] 하린이 잠시 눈을 깜빡인 뒤, 평소의 능글맞은 미소가 조금 사라진다.
    # 원고 L2153
    $ cg_start("ch04_private_lumi_shy", transition=0.38)
    lumi "……당신은 참."
    # 원고 L2157
    mc "네?"
    # 원고 L2159
    lumi "가끔 예상 못 한 말을 하네."
    # 원고 L2163
    mc "그런가요?"
    # 원고 L2165
    lumi "응."
    # 원고 L2167
    lumi "그래서……."
    # 원고 L2169
    lumi "조금 당황스럽기도 하고."
    # 원고 L2173
    narrator "하린은 시선을 내렸다."
    # 원고 L2175: ### 선택지 · 하린의 진심
    menu:
        # 원고 L2177
        "가끔은 당황하셔도 괜찮잖아요.":
            # 원고 L2178
            lumi "……."
            # 원고 L2180
            lumi "그런 말은 또 왜 이렇게 자연스럽게 하는 거야."
            # 원고 L2182: 하린 호감도 +2
            $ story_apply("ch04_sc06_lumi_a", affection={"lumi": 2})
        # 원고 L2184
        "다 고치실 때까지 옆에 있을게요.":
            # 원고 L2185
            lumi "……좋아요."
            # 원고 L2187
            lumi "그럼 조금만 같이 있어줘."
            # 원고 L2189: 하린 신뢰도 +2
            $ story_apply("ch04_sc06_lumi_b", trust={"lumi": 2})
        # 원고 L2191
        "완벽하지 않아도 충분히 멋있어요.":
            # 원고 L2192
            lumi "……."
            # 원고 L2194
            lumi "그렇게 봐주는 사람도 있구나."
            # 원고 L2196: 하린 특별 감정 플래그
            $ story_apply("ch04_sc06_lumi_c", values={"ch04_harin_special_emotion": True})
    # 원고 L2200: [공통 복귀]
    # 원고 L2204
    narrator "잠시 뒤 작은 벽을 다시 붙였다."
    # 원고 L2206
    narrator "완벽한 모형은 아니었지만, 충분히 괜찮아 보였다."
    # 원고 L2208
    lumi "……고마워요."
    # 원고 L2212
    mc "별거 안 했는데요."
    # 원고 L2214
    lumi "그냥."
    # 원고 L2216
    lumi "같이 있어줘서."
    # 원고 L2220
    narrator "하린은 조용히 웃었다."
    # 원고 L2222
    lumi "축제 시작 전에……."
    # 원고 L2224
    lumi "완성된 공간을 같이 한번 둘러볼래요?"
    # 원고 L2228
    mc "네. 좋아요."
    # 원고 L2230
    lumi "……응."
    # 원고 L2232
    lumi "그럼 약속이에요."
    # 원고 L2236
    narrator "평소의 능글맞은 말투가 잠시 사라졌다."
    # 원고 L2238
    narrator "그 모습을 처음 보는 것은 아니었다."
    # 원고 L2240
    narrator "그런데 오늘은 그 이유를 조금 알 것 같았다."
    # 원고 L2242: [FLAG] `ch04_personal_promise["harin"] = True`
    $ ch04_personal_promise["lumi"] = True
    $ secret_note_unlock("lumi", 2)
    # 원고 L2244: [SCENE 06-E END]
    $ cg_end(restore=False)
    return

# CH04 SC07–SC09. Original line numbers link dialogue to the script.
# 원고에 있는 미세 애니메이션과 전용 화면의 연출 위치를 주석으로 남긴다.

label ch04_sc07:
    $ phone_timeline_enter("CH04", "ch04_sc07")
# SOURCE CH04 L2246 # SCENE 07. 누구의 의견을 먼저 들어야 하지?
    # SOURCE CH04 L2248 오후 7:00 · 공동 동아리실 · 최종 영상 구성 결정
    $ phone_timeline_cue("CH04", "CH04_L2248")
    # SOURCE CH04 L2250 [BG] 공동 동아리실 · 저녁
    $ story_scene("clubroom307", cast=STORY_HEROES, light="evening", location="공동 동아리실 · 저녁")
    # SOURCE CH04 L2252 [BGM] Hopeful Campus
    $ play_bgm("hopeful_teamwork")
    # SOURCE CH04 L2254 [독백]
    # SOURCE CH04 L2256
    narrator "각자의 작업을 마치고 다시 동아리실에 모였다."
    # SOURCE CH04 L2258
    narrator "시연 영상의 초안은 어느 정도 완성돼 있었다."
    # SOURCE CH04 L2260
    narrator "이제 남은 건 1분이라는 제한된 시간 안에 무엇을 먼저 보여줄지 정하는 일이었다."
    # SOURCE CH04 L2262
    $ story_stage(faces={"darim": "serious"})
    darim "제출까지 이틀 남았어요."
    # SOURCE CH04 L2264
    darim "오늘 방향을 확실하게 정하면 좋겠네요."
    # SOURCE CH04 L2266
    $ story_stage(faces={"sia": "smug"})
    sia "좋아. 일단 내 영상부터 봐."
    # SOURCE CH04 L2268 [SFX] 영상 재생 버튼
    $ story_sfx("click")
    # SOURCE CH04 L2270 [독백]
    # SOURCE CH04 L2272
    narrator "화면에는 우리 팀의 전시가 차례로 나타났다."
    # SOURCE CH04 L2274
    narrator "로만의 질문 카드, 시아의 안내 만화, 오므의 사진."
    # SOURCE CH04 L2276
    narrator "하린의 공간 배치와 다림의 운영 절차까지."
    # SOURCE CH04 L2278
    narrator "처음 회의할 때는 제각각이었던 아이디어들이 하나의 영상으로 이어져 있었다."
    # SOURCE CH04 L2280 [주인공]
    # SOURCE CH04 L2282
    mc "오…… 생각보다 잘 나왔네요."
    # SOURCE CH04 L2284
    $ story_stage(faces={"sia": "happy", "omu": "happy", "lumi": "happy", "roman": "happy"})
    sia "그치?"
    # SOURCE CH04 L2286
    omu "사진도 괜찮게 들어갔네."
    # SOURCE CH04 L2288
    lumi "공간 동선도 잘 보이네요."
    # SOURCE CH04 L2290
    roman "앗,,, 제 문장도 잘 보여요……!"
    # SOURCE CH04 L2292
    darim "다만 마지막 부분을 조금 더 정리하면 좋겠어요."
    # SOURCE CH04 L2294
    $ story_stage(faces={"sia": "confused"})
    sia "아, 또 수정?"
    # SOURCE CH04 L2296
    darim "조금만요."
    # SOURCE CH04 L2298 [독백]
    # SOURCE CH04 L2300
    narrator "다림은 발표 자료를 펼쳤다."
    # SOURCE CH04 L2302
    darim "운영위원회에서는 체험이 실제로 어떻게 진행되는지 보여주길 원하잖아요."
    # SOURCE CH04 L2304
    lumi "그럼 동선을 설명하는 장면이 조금 더 필요하겠네요."
    # SOURCE CH04 L2306
    omu "근데 영상이 1분밖에 안 되잖아."
    # SOURCE CH04 L2308
    roman "글도 너무 많으면 읽기 어려울 것 같아요."
    # SOURCE CH04 L2310
    sia "그럼 설명만 하다가 끝나는 거 아니야?"
    # SOURCE CH04 L2312 [독백]
    # SOURCE CH04 L2314
    narrator "모두의 말에는 이유가 있었다."
    # SOURCE CH04 L2316
    narrator "하지만 영상 시간은 정해져 있었다."
    # SOURCE CH04 L2318
    $ story_stage(faces={actor: "serious" for actor in STORY_HEROES})
    narrator "무엇을 가장 먼저 보여줄지 결정해야 했다."
    # SOURCE CH04 L2320
    darim "그럼 우선순위를 정해볼까요?"
    # SOURCE CH04 L2322
    lumi "좋아요."
    # SOURCE CH04 L2324
    sia "나는 재미가 있어야 한다고 생각하는데."
    # SOURCE CH04 L2326
    omu "보는 사람이 무슨 부스인지 이해하는 게 먼저 아이가?"
    # SOURCE CH04 L2328
    roman "앗,,, 저는 분위기도 중요할 것 같아요."
    # SOURCE CH04 L2330
    darim "[player_name] 씨는 어떻게 생각하세요?"
    # SOURCE CH04 L2332 ### 선택지 2. 최종 시연 영상의 방향
    menu:
        # SOURCE CH04 L2334 "체험 과정을 명확하게 보여주는 게 우선 같아요."
        "체험 과정을 명확하게 보여주는 게 우선 같아요.":
            # SOURCE CH04 L2335
            $ story_stage(faces={"darim": "happy", "lumi": "happy"})
            darim "좋아요. 방문객이 어떻게 참여하는지 먼저 보여주면 되겠네요."
            # SOURCE CH04 L2337
            lumi "그럼 공간 동선도 자연스럽게 설명할 수 있겠어요."
            # SOURCE CH04 L2339 `ch04_video_priority = experience` / 팀 준비도 +1
            $ story_apply("ch04_sc07_video_experience", values={"ch04_video_priority": "experience"}, counters={"team_preparation": 1})
        # SOURCE CH04 L2341 "우리 전시만의 분위기를 보여주면 좋겠어요."
        "우리 전시만의 분위기를 보여주면 좋겠어요.":
            # SOURCE CH04 L2342
            $ story_stage(faces={"roman": "happy", "omu": "happy"})
            roman "앗,,, 그럼 질문 카드에 적힌 문장으로 시작하면 어떨까요?"
            # SOURCE CH04 L2344
            omu "사진이랑 연결하면 분위기 괜찮겠다."
            # SOURCE CH04 L2346 ch04_video_priority = emotion / 전시 완성도 +1
            $ story_apply("ch04_sc07_video_emotion", values={"ch04_video_priority": "emotion"}, counters={"exhibition_quality": 1})
        # SOURCE CH04 L2348 "짧지만 재미있고 기억에 남게 만들어요."
        "짧지만 재미있고 기억에 남게 만들어요.":
            # SOURCE CH04 L2349
            $ story_stage(faces={"sia": "happy"})
            sia "오, 그거야! 짧게 웃기고 바로 설명하는 거지."
            # SOURCE CH04 L2351
            $ story_stage(faces={"lumi": "smug"})
            lumi "이번에는 강아지가 우주로 가지는 않겠죠?"
            # SOURCE CH04 L2353
            $ story_stage(faces={"sia": "angry"})
            sia "아, 그건 다음 작품이라니까!"
            # SOURCE CH04 L2355 ch04_video_priority = fun / 홍보 완성도 +1
            $ story_apply("ch04_sc07_video_fun", values={"ch04_video_priority": "fun"}, counters={"promotion_quality": 1})
    # SOURCE CH04 L2358 [공통 복귀]
    # SOURCE CH04 L2360
    darim "그럼 정한 방향을 중심으로 다시 조정해봐요."
    # SOURCE CH04 L2362
    lumi "다른 요소를 전부 없앨 필요는 없으니까."
    # SOURCE CH04 L2364
    sia "그렇지. 1분 안에서 최대한 살리는 거야."
    # SOURCE CH04 L2366
    omu "사진 길이는 내가 조정할게."
    # SOURCE CH04 L2368
    roman "앗,,, 문장도 조금 줄여볼게요."
    # SOURCE CH04 L2370 [주인공]
    # SOURCE CH04 L2372
    mc "좋아요. 그럼 조금만 더 해봐요."
    # SOURCE CH04 L2374 [독백]
    # SOURCE CH04 L2376
    $ story_stage(faces={actor: "normal" for actor in STORY_HEROES})
    narrator "다시 작업이 시작됐다."
    # SOURCE CH04 L2378
    narrator "이번에는 한 사람이 모든 의견을 밀어붙이지 않았다."
    # SOURCE CH04 L2380
    narrator "서로 의견이 달라도 이유를 설명하고, 중요한 부분은 지키면서 조금씩 조정했다."
    # SOURCE CH04 L2382
    narrator "조금 전 개인적으로 겪었던 일들이 떠올랐다."
    # SOURCE CH04 L2384
    narrator "상대방을 이해한다는 건, 상대에게 무조건 맞춰주는 것도 아니고 내 의견을 버리는 것도 아니다."
    # SOURCE CH04 L2386
    narrator "이제야 그걸 조금 알 것 같았다."
    # SOURCE CH04 L2388 [시간 경과 · 오후 7:45]
    $ phone_timeline_cue("CH04", "CH04_L2388")
    # SOURCE CH04 L2390
    $ story_stage(faces={"sia": "happy"})
    $ story_effect("bounce", "sia")
    sia "……됐다!"
    # SOURCE CH04 L2392
    sia "야, 이번엔 진짜 끝났어."
    # SOURCE CH04 L2394
    omu "니 그 말 오늘만 세 번째다."
    # SOURCE CH04 L2396
    sia "이번엔 진짜라니까!"
    # SOURCE CH04 L2398
    darim "마지막으로 파일만 확인할게요."
    # SOURCE CH04 L2400
    lumi "화면 비율은 문제없네요."
    # SOURCE CH04 L2402
    roman "자막도…… 괜찮아요."
    # SOURCE CH04 L2404 [주인공]
    # SOURCE CH04 L2406
    mc "그럼 제출해도 되겠네요."
    # SOURCE CH04 L2408
    darim "네. 제가 올릴게요."
    # SOURCE CH04 L2410 [SFX] 마우스 클릭
    $ story_sfx("click")
    # SOURCE CH04 L2412 [UI] 축제 운영위원회 제출 시스템
    # SOURCE CH04 L2414
    system_note "「수정 기획안 업로드 완료」"
    # SOURCE CH04 L2416
    system_note "「시연 영상 업로드 완료」"
    # SOURCE CH04 L2418
    system_note "「제출이 정상적으로 접수되었습니다.」"
    # SOURCE CH04 L2420
    $ story_stage(faces={"darim": "happy"})
    darim "됐어요. 제출 확인됐어요."
    # SOURCE CH04 L2422
    sia "와아아아!"
    # SOURCE CH04 L2424 [SD EVENT] `ch04_submission_success`
    $ sd_event_start("ch04_submission_success")
    # SOURCE CH04 L2426
    omu "진짜 끝났네."
    # SOURCE CH04 L2428
    lumi "일단 오늘 할 일은 끝났죠."
    # SOURCE CH04 L2430
    roman "앗,,, 다들 수고하셨어요……!"
    $ sd_event_end()
    $ story_stage(faces={actor: "happy" for actor in STORY_HEROES})
    # SOURCE CH04 L2432
    sia "그럼 이제 밥 먹자!"
    # SOURCE CH04 L2434 [주인공]
    # SOURCE CH04 L2436
    mc "그 말만 기다리고 계셨던 거예요?"
    # SOURCE CH04 L2438
    sia "당연하지."
    # SOURCE CH04 L2440
    darim "후후. 저도 배고프네요."
    # SOURCE CH04 L2442
    lumi "그럼 오늘은 다 같이 먹어요."
    # SOURCE CH04 L2444 [독백]
    # SOURCE CH04 L2446
    narrator "누군가의 말에 또 웃음이 터졌다."
    # SOURCE CH04 L2448
    narrator "늘 그렇듯 정신없는 하루였다."
    # SOURCE CH04 L2450
    narrator "그런데 이상하게도, 이런 하루가 조금씩 소중해지고 있었다."
    # SOURCE CH04 L2452 [FLAG] `ch04_team_decision_complete = True`
    $ story_flag("ch04_team_decision_complete")
    # SOURCE CH04 L2454 [FLAG] `ch04_submission_complete = True`
    $ story_flag("ch04_submission_complete")
    # SOURCE CH04 L2456 [SCENE 07 END]
    jump ch04_sc08

label ch04_sc08:
    $ phone_timeline_enter("CH04", "ch04_sc08")
# SOURCE CH04 L2458 # SCENE 08. 조금 달라진 우리
    # SOURCE CH04 L2460 오후 8:45 · 캠퍼스 산책로 · 개인 감정 이벤트
    $ phone_timeline_cue("CH04", "CH04_L2460")
    # SOURCE CH04 L2462 [BG] 캠퍼스 야간 산책로
    $ story_scene("campus", cast=STORY_HEROES, light="night", location="캠퍼스 산책로 · 밤")
    # SOURCE CH04 L2464 [BGM] Romantic Night
    $ play_bgm("romantic_night")
    # SOURCE CH04 L2466 [독백]
    # SOURCE CH04 L2468
    narrator "저녁 식사를 마친 뒤, 우리는 학생회관 앞에서 헤어졌다."
    # SOURCE CH04 L2470
    $ story_stage(faces={"sia": "smug"})
    sia "야, 내일은 진짜 쉰다."
    # SOURCE CH04 L2472
    omu "니가 쉰다 해놓고 또 뭐 하자 할 것 같은데."
    # SOURCE CH04 L2474
    sia "응 아니야~"
    # SOURCE CH04 L2476
    $ story_stage(faces={"darim": "happy", "roman": "happy", "lumi": "happy"})
    darim "다들 오늘 수고 많으셨어요."
    # SOURCE CH04 L2478
    roman "앗,,, 조심히 들어가세요……!"
    # SOURCE CH04 L2480
    lumi "내일은 조금 여유 있게 보내요."
    # SOURCE CH04 L2482 [주인공]
    # SOURCE CH04 L2484
    mc "다들 조심히 들어가세요. 오늘 고생 많으셨어요."
    # SOURCE CH04 L2486 [독백]
    # SOURCE CH04 L2488
    $ story_exit("roman", side="left")
    $ story_exit("sia", side="left")
    $ story_exit("darim", side="right")
    $ story_exit("omu", side="right")
    $ story_exit("lumi", side="right")
    narrator "하나둘 각자의 방향으로 걸어갔다."
    # SOURCE CH04 L2490
    $ story_stage(mode="emotion", cast=[])
    narrator "나는 가방을 고쳐 메고 천천히 걷기 시작했다."
    # SOURCE CH04 L2492
    narrator "그때 누군가가 나를 불렀다."
    # SOURCE CH04 L2494 [CONDITION] `ch04_partner`에 따라 하나만 재생
    # SOURCE CH04 L2496 ### SC08-A. 로만
    if ch04_partner == "roman":
        # SOURCE CH04 L2498 [ANIM] 로만 · 부드러운 눈 깜빡임
        $ story_enter("roman", side="left", face="normal")
        # SOURCE CH04 L2500
        roman "[player_name] 씨……!"
        # 부르는 대사를 읽고 넘긴 뒤, 다음 응답부터 저녁 개인 CG를 표시한다.
        $ cg_start("ch04_evening_roman", transition=0.38)
        # SOURCE CH04 L2502 [주인공]
        # SOURCE CH04 L2504
        mc "로만 씨? 아직 안 가셨어요?"
        # SOURCE CH04 L2506
        roman "앗,,, 네. 잠깐 말씀드리고 싶은 게 있어서요."
        # SOURCE CH04 L2508 [주인공]
        # SOURCE CH04 L2510
        mc "무슨 일이에요?"
        # SOURCE CH04 L2512
        roman "아까 이야기한 문장 있잖아요."
        # SOURCE CH04 L2514
        roman "그거…… 조금 더 써봤어요."
        # SOURCE CH04 L2516 [주인공]
        # SOURCE CH04 L2518
        mc "벌써요?"
        # SOURCE CH04 L2520
        $ story_stage(faces={"roman": "happy"})
        roman "후후…… 생각이 나서요."
        # SOURCE CH04 L2522 [주인공]
        # SOURCE CH04 L2524
        mc "완성되면 꼭 읽어보고 싶네요."
        # SOURCE CH04 L2526
        $ story_stage(faces={"roman": "embarrassed"})
        roman "……네."
        # SOURCE CH04 L2528
        roman "그러니까 조금만 더 기다려주세요."
        # SOURCE CH04 L2530 [주인공]
        # SOURCE CH04 L2532
        mc "기다릴게요."
        # SOURCE CH04 L2534 [독백]
        # SOURCE CH04 L2536
        $ story_stage(faces={"roman": "happy"})
        narrator "로만은 작은 미소를 남겼다."
        # SOURCE CH04 L2538
        narrator "기다려달라는 말이 이상하게 따뜻했다."
        $ cg_end()
    # SOURCE CH04 L2540 ### SC08-B. 시아
    elif ch04_partner == "sia":
        # SOURCE CH04 L2542 [ANIM] 시아 · 눈 깜빡임, 평소보다 차분한 표정
        $ story_enter("sia", side="right", face="serious")
        # SOURCE CH04 L2544
        sia "야, [player_name]."
        # 부르는 첫 대사를 넘긴 뒤 저녁 개인 CG를 부드럽게 겹쳐 표시한다.
        $ cg_start("ch04_evening_sia", transition=0.38)
        # SOURCE CH04 L2546 [주인공]
        # SOURCE CH04 L2548
        mc "네?"
        # SOURCE CH04 L2550
        sia "오늘 진지한 이야기한 거."
        # SOURCE CH04 L2552
        sia "다른 애들한테 놀리지 마라?"
        # SOURCE CH04 L2554 [주인공]
        # SOURCE CH04 L2556
        mc "왜 제가 놀리겠어요?"
        # SOURCE CH04 L2558
        sia "……아, 그러네."
        # SOURCE CH04 L2560
        $ story_stage(faces={"sia": "embarrassed"})
        sia "그냥 좀 쑥스러워서."
        # SOURCE CH04 L2562 [주인공]
        # SOURCE CH04 L2564
        mc "걱정 안 하셔도 돼요."
        # SOURCE CH04 L2566
        sia "……."
        # SOURCE CH04 L2568
        sia "너 진짜 이상한 애다."
        # SOURCE CH04 L2570 [주인공]
        # SOURCE CH04 L2572
        mc "제가요?"
        # SOURCE CH04 L2574
        sia "응."
        # SOURCE CH04 L2576
        sia "좋은 뜻으로."
        # SOURCE CH04 L2578 [독백]
        # SOURCE CH04 L2580
        $ story_stage(faces={"sia": "happy"})
        narrator "시아는 웃었지만, 이번에는 장난을 덧붙이지 않았다."
        $ cg_end()
    # SOURCE CH04 L2582 ### SC08-C. 다림
    elif ch04_partner == "darim":
        # SOURCE CH04 L2584 [ANIM] 다림 · 잔잔한 미소, 자연스러운 깜빡임
        $ story_enter("darim", side="left", face="happy")
        # SOURCE CH04 L2586
        darim "[player_name] 씨."
        # 부르는 첫 대사를 넘긴 뒤 저녁 개인 CG를 부드럽게 겹쳐 표시한다.
        $ cg_start("ch04_evening_darim", transition=0.38)
        # SOURCE CH04 L2588 [주인공]
        # SOURCE CH04 L2590
        mc "네, 선배."
        # SOURCE CH04 L2592
        darim "오늘은 생각보다 많은 이야기를 했네요."
        # SOURCE CH04 L2594 [주인공]
        # SOURCE CH04 L2596
        mc "그러게요."
        # SOURCE CH04 L2598
        darim "그런데 이상하게 마음이 좀 편해졌어요."
        # SOURCE CH04 L2600 [주인공]
        # SOURCE CH04 L2602
        mc "저도 선배랑 이야기해서 좋았어요."
        # SOURCE CH04 L2604
        darim "……후후."
        # SOURCE CH04 L2606
        darim "그럼 다음에는 일 말고 다른 이야기로도 이렇게 같이 있어요."
        # SOURCE CH04 L2608 [주인공]
        # SOURCE CH04 L2610
        mc "좋아요. 저도 그러고 싶어요."
        # SOURCE CH04 L2612
        darim "……기대할게요."
        # SOURCE CH04 L2614 [독백]
        # SOURCE CH04 L2616
        narrator "선배와 후배라는 거리감이 조금 줄어든 것 같았다."
        $ cg_end()
    # SOURCE CH04 L2618 ### SC08-D. 오므
    elif ch04_partner == "omu":
        # SOURCE CH04 L2620 [ANIM] 오므 · 머리카락 끝의 미세 움직임
        $ story_enter("omu", side="right", face="normal")
        # SOURCE CH04 L2622
        omu "야."
        # 부르는 첫 대사를 넘긴 뒤 저녁 개인 CG를 부드럽게 겹쳐 표시한다.
        $ cg_start("ch04_evening_omu", transition=0.38)
        # SOURCE CH04 L2624 [주인공]
        # SOURCE CH04 L2626
        mc "네?"
        # SOURCE CH04 L2628
        omu "아까 그 사진 있잖아."
        # SOURCE CH04 L2630
        omu "니랑 이야기하고 나니까 좀 다르게 보이더라."
        # SOURCE CH04 L2632 [주인공]
        # SOURCE CH04 L2634
        mc "좋은 쪽으로요?"
        # SOURCE CH04 L2636
        omu "어."
        # SOURCE CH04 L2638
        omu "좋은 쪽으로."
        # SOURCE CH04 L2640 [주인공]
        # SOURCE CH04 L2642
        mc "그럼 다행이네요."
        # SOURCE CH04 L2644
        $ story_stage(faces={"omu": "embarrassed"})
        omu "……."
        # SOURCE CH04 L2646
        omu "다음에 시간 되면 다른 데도 같이 찍으러 가자."
        # SOURCE CH04 L2648 [주인공]
        # SOURCE CH04 L2650
        mc "좋아요. 연락 주세요."
        # SOURCE CH04 L2652
        $ story_stage(faces={"omu": "normal"})
        omu "어. 꼭."
        # SOURCE CH04 L2654 [독백]
        # SOURCE CH04 L2656
        narrator "오므는 담담하게 말했다."
        # SOURCE CH04 L2658
        narrator "그런데 그 약속이 이상하게 기다려졌다."
        $ cg_end()
    # SOURCE CH04 L2660 ### SC08-E. 하린
    elif ch04_partner == "lumi":
        # SOURCE CH04 L2662 [ANIM] 하린 · 미세 호흡, 시선 변화
        $ story_enter("lumi", side="left", face="normal")
        # SOURCE CH04 L2664
        lumi "[player_name] 씨."
        # 부르는 첫 대사를 넘긴 뒤 저녁 개인 CG를 부드럽게 겹쳐 표시한다.
        $ cg_start("ch04_evening_lumi", transition=0.38)
        # SOURCE CH04 L2666 [주인공]
        # SOURCE CH04 L2668
        mc "네, 선배?"
        # SOURCE CH04 L2670
        lumi "오늘은 조금…… 예상 밖이었네요."
        # SOURCE CH04 L2672 [주인공]
        # SOURCE CH04 L2674
        mc "어떤 점이요?"
        # SOURCE CH04 L2676
        lumi "그냥 여러 가지로요."
        # SOURCE CH04 L2678
        lumi "생각보다 계획이 많이 바뀌었고."
        # SOURCE CH04 L2680
        lumi "또……."
        # SOURCE CH04 L2682 [주인공]
        # SOURCE CH04 L2684
        mc "또요?"
        # SOURCE CH04 L2686
        lumi "……."
        # SOURCE CH04 L2688
        lumi "아니에요."
        # SOURCE CH04 L2690 [주인공]
        # SOURCE CH04 L2692
        mc "그래도 나쁘지는 않았죠?"
        # SOURCE CH04 L2694
        lumi "……응."
        # SOURCE CH04 L2696
        lumi "사실은 좋았어."
        # SOURCE CH04 L2698 [독백]
        # SOURCE CH04 L2700
        $ story_stage(faces={"lumi": "embarrassed"})
        narrator "하린이 잠시 시선을 내렸다."
        # SOURCE CH04 L2702
        lumi "같이 있어줘서."
        # SOURCE CH04 L2704 [주인공]
        # SOURCE CH04 L2706
        mc "저도 좋았어요."
        # SOURCE CH04 L2708
        lumi "……."
        # SOURCE CH04 L2710
        lumi "그런 말씀은 정말 아무렇지 않게 하시네요."
        # SOURCE CH04 L2712 [주인공]
        # SOURCE CH04 L2714
        mc "진심인데요."
        # SOURCE CH04 L2716
        lumi "……그러니까."
        # SOURCE CH04 L2718 [독백]
        # SOURCE CH04 L2720
        $ story_stage(faces={"lumi": "happy"})
        narrator "하린은 작게 웃더니 먼저 고개를 돌렸다."
        # SOURCE CH04 L2722
        narrator "평소 같으면 분명 나를 놀렸을 텐데."
        # SOURCE CH04 L2724
        narrator "이번에는 내가 조금 더 오래 바라보게 됐다."
        $ cg_end()
    # SOURCE CH04 L2726 [공통 복귀]
    # SOURCE CH04 L2728 [독백]
    # SOURCE CH04 L2730
    $ story_exit(ch04_partner, side="right")
    narrator "돌아가는 길이 조금 짧게 느껴졌다."
    # SOURCE CH04 L2732
    narrator "별것 아닌 대화였다고 생각하면 될 텐데."
    # SOURCE CH04 L2734
    narrator "오늘은 그렇게 넘기기가 어려웠다."
    # SOURCE CH04 L2736 [주인공 · 혼잣말]
    # SOURCE CH04 L2738
    mc "……정말 친해서 그런 걸까."
    # SOURCE CH04 L2740 [FADE OUT]
    # SOURCE CH04 L2742 [FLAG] `ch04_evening_event = ch04_partner`
    $ ch04_evening_event = ch04_partner
    # SOURCE CH04 L2744 [SCENE 08 END]
    jump ch04_sc09

label ch04_sc09:
    $ phone_timeline_enter("CH04", "ch04_sc09")
# SOURCE CH04 L2746 # SCENE 09. 왜 하필 그 말이 기억나지?
    # SOURCE CH04 L2748 오후 11:20 · 주인공 방 · CH04 엔딩
    $ phone_timeline_cue("CH04", "CH04_L2748")
    # SOURCE CH04 L2750 [BG] 주인공 방 · 밤
    $ story_scene("room", light="night", location="주인공 방 · 밤", standing=False)
    # SOURCE CH04 L2752 [BGM] Night Campus
    $ play_bgm("night_campus")
    # SOURCE CH04 L2754 [독백]
    # SOURCE CH04 L2756
    narrator "방으로 돌아왔을 때는 이미 밤이 깊었다."
    # SOURCE CH04 L2758
    narrator "가방을 내려놓고 침대에 누웠다."
    # SOURCE CH04 L2760
    narrator "오늘 있었던 일들이 하나씩 떠올랐다."
    # SOURCE CH04 L2762
    narrator "스키가 진지하게 디저트를 만들던 모습."
    # SOURCE CH04 L2764
    narrator "시아와 오므가 서로 장난치던 모습."
    # SOURCE CH04 L2766
    narrator "로만이 조심스럽게 자신의 글에 관해 이야기하던 모습."
    # SOURCE CH04 L2768
    narrator "다림이 평소보다 솔직하게 마음을 표현하던 순간."
    # SOURCE CH04 L2770
    narrator "하린이 모형 앞에서 잠시 말을 멈췄던 모습."
    # SOURCE CH04 L2772
    narrator "……정말 많이 친해졌다."
    # SOURCE CH04 L2774
    narrator "그런데 오늘은 이상하게도 누군가의 말이 자꾸 기억에 남는다."
    # SOURCE CH04 L2776 [주인공 · 혼잣말]
    # SOURCE CH04 L2778
    mc "……뭐지, 이 기분."
    # SOURCE CH04 L2780 [독백]
    # SOURCE CH04 L2782
    narrator "처음에는 그저 궁금했다."
    # SOURCE CH04 L2784
    narrator "어떤 사람인지."
    # SOURCE CH04 L2786
    narrator "무엇을 좋아하는지."
    # SOURCE CH04 L2788
    narrator "어떤 상황에서 웃는지."
    # SOURCE CH04 L2790
    narrator "그런데 이제는 상대가 무슨 생각을 하는지도 알고 싶어졌다."
    # SOURCE CH04 L2792
    narrator "내가 모르는 모습도 더 보고 싶어졌다."
    # SOURCE CH04 L2794 [주인공 · 혼잣말]
    # SOURCE CH04 L2796
    mc "……이상하네."
    # SOURCE CH04 L2798 [SFX] 휴대전화 알림
    # SOURCE CH04 L2800 [UI] 축제 준비팀 (6)
    $ story_chat(True, title="축제 준비팀")
    $ phone_clock = "23:20"
    # SOURCE CH04 L2802
    darim "다들 오늘 정말 수고 많으셨어요."
    # SOURCE CH04 L2804
    darim "최종 자료도 잘 제출됐어요."
    # SOURCE CH04 L2806
    sia "와 드디어 끝"
    # SOURCE CH04 L2808
    sia "내일은 진짜 쉰다"
    # SOURCE CH04 L2810
    omu "니 그 말 오늘만 다섯 번째다"
    # SOURCE CH04 L2812
    sia "횟수 세고 있었냐ㅋㅋ"
    # SOURCE CH04 L2814
    roman "앗,,, 모두 편안한 밤 보내세요……!"
    # SOURCE CH04 L2816
    lumi "내일은 정말 조금 쉬어요."
    # SOURCE CH04 L2818
    sia "하린 너도 쉬어"
    # SOURCE CH04 L2820
    lumi "네. 저도 이제 쉬려고요."
    # SOURCE CH04 L2822
    omu "그 말 믿어도 되나"
    # SOURCE CH04 L2824
    lumi "시아 씨보다는 신뢰도가 높지 않을까요?"
    # SOURCE CH04 L2826
    sia "야ㅋㅋㅋ"
    $ story_chat(False)
    # SOURCE CH04 L2828 [독백]
    # SOURCE CH04 L2830
    narrator "나는 웃으면서 채팅창을 닫았다."
    # SOURCE CH04 L2832
    narrator "그 순간 개인 메시지가 하나 도착했다."
    # SOURCE CH04 L2834 [CONDITION] `ch04_partner`에 따라 하나만 표시
    # SOURCE CH04 L2836 로만
    if ch04_partner == "roman":
        # SOURCE CH04 L2837 로만 · 개인 메시지
        $ story_chat(True, title="로만")
        $ phone_clock = "23:20"
        # SOURCE CH04 L2839
        roman "앗,,, 늦은 시간에 연락드려서 괜찮을까요……?"
        # SOURCE CH04 L2841
        roman "아까 이야기한 문장 조금 더 써봤어요."
        # SOURCE CH04 L2843
        roman "완성되면 꼭 보여드릴게요."
        # SOURCE CH04 L2845
        roman "좋은 밤 보내세요……!"
        # SOURCE CH04 L2847
        mc "네. 기다릴게요. 로만 씨도 좋은 밤 보내세요."
        $ story_chat(False)
    # SOURCE CH04 L2849 시아
    elif ch04_partner == "sia":
        # SOURCE CH04 L2850 시아 · 개인 메시지
        $ story_chat(True, title="시아")
        $ phone_clock = "23:20"
        # SOURCE CH04 L2851
        sia "야 오늘 고마웠다"
        # SOURCE CH04 L2853
        sia "너랑 얘기하고 나니까 콘티 다시 손볼 생각 생김"
        # SOURCE CH04 L2855
        sia "다음에 내 개인 웹툰도 봐라"
        # SOURCE CH04 L2857
        sia "약속했으니까 도망가지 마ㅋㅋ"
        # SOURCE CH04 L2859
        mc "알겠어요. 꼭 보여주세요. 기대하고 있을게요."
        $ story_chat(False)
    # SOURCE CH04 L2861 다림
    elif ch04_partner == "darim":
        # SOURCE CH04 L2862 다림 · 개인 메시지
        $ story_chat(True, title="다림")
        $ phone_clock = "23:20"
        # SOURCE CH04 L2863
        darim "오늘 이야기 들어주셔서 감사했어요."
        # SOURCE CH04 L2865
        darim "생각보다 마음이 편해졌네요."
        # SOURCE CH04 L2867
        darim "다음에도 편하게 이야기해요."
        # SOURCE CH04 L2869
        darim "좋은 밤 보내세요."
        # SOURCE CH04 L2871
        mc "저도 좋았어요. 선배도 편히 쉬세요."
        $ story_chat(False)
    # SOURCE CH04 L2873 오므
    elif ch04_partner == "omu":
        # SOURCE CH04 L2874 오므 · 개인 메시지
        $ story_chat(True, title="오므")
        $ phone_clock = "23:20"
        # SOURCE CH04 L2875
        omu "아까 사진 다시 봤는데"
        # SOURCE CH04 L2877
        omu "니 말대로 두 장 다 넣는 것도 괜찮겠더라"
        # SOURCE CH04 L2879
        omu "다음에 사진 찍으러 갈 때 연락할게"
        # SOURCE CH04 L2881
        omu "오늘 고생했다"
        # SOURCE CH04 L2883
        mc "좋아요. 연락 주세요. 오므 씨도 고생 많으셨어요."
        $ story_chat(False)
    # SOURCE CH04 L2886 하린
    elif ch04_partner == "lumi":
        # SOURCE CH04 L2887 하린 · 개인 메시지
        $ story_chat(True, title="하린")
        $ phone_clock = "23:20"
        # SOURCE CH04 L2888
        lumi "오늘 같이 있어줘서 고마웠어요."
        # SOURCE CH04 L2890
        lumi "덕분에 모형도 잘 고쳤네."
        # SOURCE CH04 L2892
        lumi "그런 게 도움이 될 때도 있죠."
        # SOURCE CH04 L2894
        lumi "……좋은 밤 보내요."
        # SOURCE CH04 L2896
        mc "저도 같이 작업해서 좋았어요. 좋은 밤 보내세요, 선배."
        $ story_chat(False)
    # SOURCE CH04 L2900 [공통 복귀]
    # SOURCE CH04 L2902 [UI] 스마트폰 화면 종료
    # SOURCE CH04 L2904 [독백]
    # SOURCE CH04 L2906
    narrator "휴대전화를 내려놓았다."
    # SOURCE CH04 L2908
    narrator "별다를 것 없는 메시지였다."
    # SOURCE CH04 L2910
    narrator "그런데 오늘은 쉽게 잠이 오지 않았다."
    # SOURCE CH04 L2912
    narrator "누군가를 더 알고 싶어지는 마음."
    # SOURCE CH04 L2914
    narrator "함께 보내는 시간이 조금 더 길었으면 하는 마음."
    # SOURCE CH04 L2916
    narrator "그리고 헤어진 뒤에도 다시 만나고 싶어지는 마음."
    # SOURCE CH04 L2918
    narrator "이런 감정에 어떤 이름을 붙여야 할까."
    # SOURCE CH04 L2920 [주인공 · 혼잣말]
    # SOURCE CH04 L2922
    mc "……설마."
    # SOURCE CH04 L2924 [독백]
    # SOURCE CH04 L2926
    narrator "입 밖으로 내려고 했던 말을 멈췄다."
    # SOURCE CH04 L2928
    narrator "아직은 잘 모르겠다."
    # SOURCE CH04 L2930
    narrator "그런 감정이라고 단정하기에는 조금 이르다."
    # SOURCE CH04 L2932
    narrator "다만 확실한 건 하나 있었다."
    # SOURCE CH04 L2934
    narrator "나는 지금 이 사람들과 함께하는 시간이 좋다."
    # SOURCE CH04 L2936
    narrator "그리고……"
    # SOURCE CH04 L2938
    narrator "그중 누군가와는 조금 더 오래 함께하고 싶을지도 모르겠다."
    # SOURCE CH04 L2940 [SFX] 시스템 알림
    # SOURCE CH04 L2942 [UI] 축제 운영위원회
    $ story_chat(True, title="축제 운영위원회")
    $ phone_clock = "23:20"
    # SOURCE CH04 L2944
    system_note "「최종 부스 평가 일정 안내」"
    # SOURCE CH04 L2946
    system_note "「수정 기획안 및 시연 자료 제출이 확인되었습니다.」"
    # SOURCE CH04 L2948
    system_note "「최종 평가는 축제 시작 일주일 전 진행됩니다.」"
    # SOURCE CH04 L2950
    system_note "「평가 결과에 따라 부스 우선 배정 구역이 결정됩니다.」"
    $ story_chat(False)
    # SOURCE CH04 L2952 [주인공 · 혼잣말]
    # SOURCE CH04 L2954
    mc "……축제까지 일주일."
    # SOURCE CH04 L2956 [독백]
    # SOURCE CH04 L2958
    narrator "생각보다 얼마 남지 않았다."
    # SOURCE CH04 L2960
    narrator "축제가 끝나면 우리는 어떻게 될까."
    # SOURCE CH04 L2962
    narrator "지금처럼 매일 만나서 이야기하고, 장난치고, 함께 무언가를 만들까."
    # SOURCE CH04 L2964
    narrator "아니면 각자의 일상으로 돌아가게 될까."
    # SOURCE CH04 L2966 [주인공 · 혼잣말]
    # SOURCE CH04 L2968
    mc "……그건 좀 아쉬운데."
    # SOURCE CH04 L2970 [FADE TO BLACK]
    $ story_fade_out()
    scene expression Solid("#080d16") with fade
    # SOURCE CH04 L2972 [BGM] CH04 Ending Theme
    $ play_bgm("chapter_ending_reprise")
    # SOURCE CH04 L2974
    narrator "COMMON ROUTE"
    # SOURCE CH04 L2976
    narrator "「CHAPTER 04 COMPLETE」"
    # SOURCE CH04 L2978
    narrator "「다음 이야기」"
    # SOURCE CH04 L2980
    narrator "「축제까지 앞으로 일주일」"
    # SOURCE CH04 L2982 [FLAG] `chapter04_complete = True`
    $ story_complete_chapter(4)
    # SOURCE CH04 L2984 [CHAPTER 04 END]
    jump chapter05
