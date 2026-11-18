# CH05 · 원본 design_docs/story_sources/chapter05.txt
# SHA256: 78c071ae87b63b3913dee545bd9b164f0ac3efb55f07eaf248c713d9e5b9101b
# 이미지와 스탠딩의 연출 위치는 원본 행 번호가 붙은 콘티로 남깁니다.

label chapter05:
    $ phone_timeline_enter("CH05", "chapter05")
    $ story_begin_chapter(5, "축제까지 앞으로 일주일")
    jump ch05_sc01

# CH05 공식 대본 SC01–SC04. SOURCE 주석은 원고 행 번호를 가리킵니다.
# 시연 영상과 전용 배경은 콘티 주석으로 남겼습니다.

label ch05_sc01:
    $ phone_timeline_enter("CH05", "ch05_sc01")
    # SOURCE CH05 L27 SCENE 01. D-7, 이제 진짜 시작이다
    # SOURCE CH05 L28 오전 8:40 · 주인공 방 · 최종 평가 당일
    $ phone_timeline_cue("CH05", "CH05_L28")
    # SOURCE CH05 L29 SC01 · D-7, 이제 진짜 시작이다
    # SOURCE CH05 L30 [BG] 주인공 방 · 아침
    $ story_scene("room", light="day", location="주인공 방 · 아침", standing=False)
    # SOURCE CH05 L32 [BGM] Daily Campus
    $ play_bgm("campus_day")
    # SOURCE CH05 L34 [FADE IN]
    # SOURCE CH05 L38
    narrator "축제까지 일주일."
    # SOURCE CH05 L40
    narrator "처음 준비팀에 들어왔을 때는 축제가 한참 멀게만 느껴졌다."
    # SOURCE CH05 L42
    narrator "그동안 별일이 다 있었다."
    # SOURCE CH05 L44
    narrator "시아와 오므가 복도에서 티격태격하던 날."
    # SOURCE CH05 L46
    narrator "로만이 떨어뜨린 책을 함께 주웠던 날."
    # SOURCE CH05 L48
    narrator "하린 선배가 합류하고, 다림 선배가 정신없는 회의를 정리하던 날."
    # SOURCE CH05 L50
    narrator "그리고 옆 부스의 스키가 등장한 뒤로는……"
    # SOURCE CH05 L52
    narrator "……생각만 해도 조금 시끄럽다."
    # SOURCE CH05 L54 [SFX] 스마트폰 진동
    # SOURCE CH05 L56 [UI] 축제 준비팀 (6)
    $ story_chat(True, title="축제 준비팀")
    # SOURCE CH05 L59
    darim "좋은 아침이에요."
    # SOURCE CH05 L61
    darim "다들 오늘 최종 평가 있는 거 기억하시죠?"
    # SOURCE CH05 L64
    sia "기억함"
    # SOURCE CH05 L66
    sia "완전 기억함"
    # SOURCE CH05 L68
    sia "꿈에서도 발표함"
    # SOURCE CH05 L71
    omu "니 꿈에서도 말 많나"
    # SOURCE CH05 L74
    sia "야 꿈에서까지 조용해야 되냐"
    # SOURCE CH05 L77
    lumi "그럼 깨어 있을 때만이라도 조금 조용히 해주세요."
    # SOURCE CH05 L80
    sia "너까지 그러기냐"
    # SOURCE CH05 L83
    roman "앗,,, 다들 좋은 아침이에요……!"
    # SOURCE CH05 L85
    roman "저는 발표 문구 다시 확인하고 있어요."
    # SOURCE CH05 L88
    darim "로만 씨는 너무 긴장하지 않으셔도 돼요."
    # SOURCE CH05 L90
    darim "어제 다 같이 확인했으니까요."
    # SOURCE CH05 L93
    roman "네……!"
    # SOURCE CH05 L96
    sia "아 근데"
    # SOURCE CH05 L98
    sia "발표 잘못하면 우리 부스 없어지는 건 아니지?"
    # SOURCE CH05 L101
    darim "부스가 없어지는 건 아니에요."
    # SOURCE CH05 L103
    darim "우선 배정 구역을 결정하는 평가예요."
    # SOURCE CH05 L106
    omu "그 얘기 어제도 했잖아"
    # SOURCE CH05 L109
    sia "중요하니까 다시 묻는 거지"
    # SOURCE CH05 L112
    lumi "시아 씨가 설명 담당이 아니라 다행이네요."
    # SOURCE CH05 L115
    sia "야ㅋㅋㅋ"
    $ story_chat(False)
    # SOURCE CH05 L119
    narrator "화면을 보며 웃음이 나왔다."
    # SOURCE CH05 L121
    narrator "예전 같았으면 이런 채팅방을 무음으로 해뒀을지도 모른다."
    # SOURCE CH05 L123
    narrator "이제는 아침마다 확인하는 게 습관이 됐다."
    # SOURCE CH05 L125 [UI] 개인 메시지 알림
    # SOURCE CH05 L127 [CONDITION] ch04_partner에 해당하는 메시지만 표시
    # SOURCE CH05 L128 로만
    if ch04_partner == "roman":
        $ story_chat(True, title="로만")
        # SOURCE CH05 L130
        roman "앗,,, 오늘 발표 잘 끝났으면 좋겠어요."
        # SOURCE CH05 L132
        roman "끝나면 전에 말씀드린 책도 같이 찾아볼까요……?"
        # SOURCE CH05 L135
        mc "좋아요. 발표부터 잘 마치고 같이 찾아봐요."
        $ story_chat(False)
    # SOURCE CH05 L136 시아
    elif ch04_partner == "sia":
        $ story_chat(True, title="시아")
        # SOURCE CH05 L138
        sia "야 감상 담당"
        # SOURCE CH05 L140
        sia "오늘도 내 영상 보고 감탄할 준비 됐냐"
        # SOURCE CH05 L143
        mc "일단 발표가 무사히 끝나면 감탄해 드릴게요."
        # SOURCE CH05 L146
        sia "와 조건부 칭찬이네ㅋㅋ"
        $ story_chat(False)
    # SOURCE CH05 L147 다림
    elif ch04_partner == "darim":
        $ story_chat(True, title="다림")
        # SOURCE CH05 L149
        darim "어제 자료 다시 봤는데 큰 문제는 없더라고요."
        # SOURCE CH05 L151
        darim "오늘도 잘 부탁드릴게요."
        # SOURCE CH05 L154
        mc "네. 선배도 너무 혼자 부담 갖지 마세요."
        # SOURCE CH05 L157
        darim "후후. 이제는 같이 하고 있으니까 괜찮아요."
        $ story_chat(False)
    # SOURCE CH05 L158 오므
    elif ch04_partner == "omu":
        $ story_chat(True, title="오므")
        # SOURCE CH05 L160
        omu "오늘 촬영한 사진도 필요할 수 있겠다"
        # SOURCE CH05 L162
        omu "카메라 챙겨갈게"
        # SOURCE CH05 L165
        mc "좋아요. 오늘도 멋진 사진 기대할게요."
        # SOURCE CH05 L168
        omu "기대 너무 많이 하진 마라ㅋㅋ"
        $ story_chat(False)
    # SOURCE CH05 L169 하린
    elif ch04_partner == "lumi":
        $ story_chat(True, title="하린")
        # SOURCE CH05 L171
        lumi "오늘 배치 모형도 가져갈 거예요."
        # SOURCE CH05 L173
        lumi "지난번에 같이 고친 부분도 잘 붙어 있어요."
        # SOURCE CH05 L176
        mc "다행이네요. 오늘 직접 보는 게 기대돼요."
        # SOURCE CH05 L179
        lumi "후후. 그럼 실망시키지 않아야겠네."
        $ story_chat(False)
    # SOURCE CH05 L181 [공통 복귀]
    # SOURCE CH05 L185
    narrator "모두 각자의 방식으로 오늘을 준비하고 있다."
    # SOURCE CH05 L187
    narrator "나도 가만히 있을 수는 없겠지."
    # SOURCE CH05 L189
    narrator "가방을 챙기고 문을 나섰다."
    # SOURCE CH05 L191 [주인공 · 혼잣말]
    # SOURCE CH05 L192
    mc "좋아. 오늘만 잘 넘기면……."
    # SOURCE CH05 L196
    narrator "……끝나는 건가?"
    # SOURCE CH05 L198
    narrator "아니다."
    # SOURCE CH05 L200
    narrator "축제까지 아직 일주일이나 남았다."
    # SOURCE CH05 L202
    narrator "그런데 왠지."
    # SOURCE CH05 L204
    narrator "일주일밖에 남지 않은 것 같기도 했다."
    # SOURCE CH05 L206 [FADE OUT]
    # SOURCE CH05 L208 [SCENE 01 END]
    jump ch05_sc02


label ch05_sc02:
    $ phone_timeline_enter("CH05", "ch05_sc02")
    # SOURCE CH05 L214 SCENE 02. 마지막 준비는 왜 이렇게 바쁜데
    # SOURCE CH05 L215 오전 10:10 · 공동 동아리실 · 단체 SD 이벤트
    $ phone_timeline_cue("CH05", "CH05_L215")
    # SOURCE CH05 L216 SC02 · 마지막 준비는 왜 이렇게 바쁜데
    # SOURCE CH05 L217 [BG] 공동 동아리실 · 오전
    $ story_scene("clubroom307", cast=STORY_HEROES, light="day", location="공동 동아리실 · 오전", standing=False)
    # SOURCE CH05 L219 [BGM] Light Comedy
    $ play_bgm("comedy_light")
    # SOURCE CH05 L221 [SD EVENT] ch05_final_prep_01
    # SOURCE CH05 L225
    narrator "동아리실에 들어오자 모두 바쁘게 움직이고 있었다."
    # SOURCE CH05 L227
    narrator "시아는 노트북을 붙잡고 있었고, 오므는 사진을 정리하고 있었다."
    # SOURCE CH05 L229
    narrator "로만은 발표 문구를 확인했고, 다림 선배는 제출 자료와 일정을 대조하고 있었다."
    # SOURCE CH05 L231
    narrator "하린 선배의 앞에는 완성된 부스 모형이 놓여 있었다."
    # 네 준비 독백을 모두 읽고 넘긴 뒤, 같은 단체 일러스트를 장면 끝까지 유지한다.
    $ sd_event_start("ch05_final_prep_01", transition=0.30)
    $ story_stage(faces={"sia": "confused"})
    # SOURCE CH05 L234
    sia "……아아아."
    # SOURCE CH05 L237
    omu "와 그라는데."
    # SOURCE CH05 L240
    sia "나 방금 영상 다시 봤는데."
    $ story_stage(faces={"sia": "smug"})
    # SOURCE CH05 L242
    sia "진짜 잘 만든 것 같아."
    # SOURCE CH05 L245
    omu "그 말을 왜 그렇게 고통스럽게 하노."
    # SOURCE CH05 L248
    sia "내 재능이 너무 무서워서."
    $ story_stage(faces={"lumi": "smug"})
    # SOURCE CH05 L251
    lumi "저도 조금 무섭긴 하네요."
    # SOURCE CH05 L254
    sia "그치?"
    # SOURCE CH05 L257
    lumi "네. 자화자찬이 끝나지 않을 것 같아서."
    $ story_stage(faces={"sia": "surprised"})
    # SOURCE CH05 L260
    sia "야!"
    $ story_stage(faces={"darim": "serious"})
    # SOURCE CH05 L262 [SD EVENT] ch05_final_prep_02
    # SOURCE CH05 L265
    darim "다들 자료 확인 부탁드릴게요."
    # SOURCE CH05 L267
    darim "최종 제출본하고 지금 발표할 자료가 같은 버전인지 봐야 해요."
    # SOURCE CH05 L270
    mc "안녕하세요. 저도 도울게요."
    $ story_stage(faces={"roman": "happy", "sia": "happy"})
    # SOURCE CH05 L273
    roman "앗,,, 오셨어요!"
    # SOURCE CH05 L276
    sia "야, 마침 잘 왔다."
    # SOURCE CH05 L278
    sia "이거 봐봐."
    # SOURCE CH05 L282
    narrator "시아가 영상을 재생했다."
    # SOURCE CH05 L284
    narrator "작은 캐릭터가 전시 부스를 소개하고, 로만의 질문 카드와 오므의 사진이 차례로 등장했다."
    # SOURCE CH05 L286
    narrator "화면이 전환되며 하린 선배의 공간 배치와 다림 선배의 참여 절차가 자연스럽게 연결됐다."
    # SOURCE CH05 L289
    mc "오, 확실히 처음보다 이해하기 쉬워졌네요."
    $ story_stage(faces={"sia": "happy"})
    # SOURCE CH05 L292
    sia "그치!"
    # SOURCE CH05 L295
    omu "중간에 니 캐릭터가 넘어지는 장면은 왜 아직 있는데?"
    # SOURCE CH05 L298
    sia "그건 핵심 개그거든."
    $ story_stage(faces={"darim": "smug"})
    # SOURCE CH05 L301
    darim "설명에는 지장 없으니까 남겨두기로 했죠."
    # SOURCE CH05 L304
    roman "앗,,, 저도 그 부분은 조금 귀여운 것 같아요……."
    # SOURCE CH05 L307
    sia "봐봐! 로만도 인정했어!"
    $ story_stage(faces={"lumi": "serious"})
    # SOURCE CH05 L310
    lumi "영상 전체는 58초예요. 두 초 남았네요."
    # SOURCE CH05 L313
    sia "그럼 두 초 더 웃길 수 있는데?"
    # SOURCE CH05 L316
    mc "이번에는 그냥 두 초 남겨두는 게 좋지 않을까요?"
    $ story_stage(faces={"sia": "embarrassed"})
    # SOURCE CH05 L319
    sia "……."
    # SOURCE CH05 L321
    sia "너 요즘 내 개그를 너무 엄격하게 평가한다?"
    # SOURCE CH05 L324
    mc "감상 담당이라면서요."
    # SOURCE CH05 L327
    sia "아."
    # SOURCE CH05 L329
    sia "그건 그렇네."
    $ story_stage(faces={"roman": "happy", "sia": "happy", "darim": "happy", "omu": "happy", "lumi": "happy"})
    # SOURCE CH05 L331 [SD EVENT] ch05_final_prep_03
    # SOURCE CH05 L335
    narrator "다들 웃었다."
    # SOURCE CH05 L337
    narrator "나는 발표용 자료를 살펴봤다."
    # SOURCE CH05 L339
    narrator "CH03 시범 운영에서 방문객이 헷갈려 하던 참여 과정이 크게 단순해져 있었다."
    # SOURCE CH05 L341
    narrator "개인 기록을 전시하기 전에 확인하는 절차와, 공개를 원하지 않을 때 철회하는 방법도 한눈에 보였다."
    # SOURCE CH05 L344
    mc "지난번에 문제 있었던 부분도 정리가 잘됐네요."
    $ story_stage(faces={"darim": "serious", "roman": "normal", "omu": "normal", "lumi": "normal"})
    # SOURCE CH05 L347
    darim "네. 그때 의견을 듣고 운영 방식을 다시 만들었어요."
    # SOURCE CH05 L350
    roman "질문 카드도 부담 없이 고를 수 있게 바꿨어요."
    # SOURCE CH05 L353
    omu "사진은 공개 가능한 것만 남겨놨다."
    # SOURCE CH05 L356
    lumi "통로도 넓혔어요. 그냥 둘러보는 사람도 편하게 지나갈 수 있도록요."
    $ story_stage(faces={"sia": "smug"})
    # SOURCE CH05 L359
    sia "그리고 내 영상이 대박이잖아."
    # SOURCE CH05 L362
    omu "그 얘기는 이미 했다."
    # SOURCE CH05 L365
    sia "중요해서 또 하는 거야."
    # SOURCE CH05 L369
    narrator "처음에는 하나의 부스를 만들기 위해 모인 사람들이었다."
    # SOURCE CH05 L371
    narrator "지금은 서로가 무엇을 중요하게 생각하는지 알고, 그걸 하나의 결과물로 만들어내고 있었다."
    $ story_stage(faces={"darim": "happy"})
    # SOURCE CH05 L374
    darim "좋아요. 자료는 문제없네요."
    # SOURCE CH05 L376
    darim "이제 발표 장소로 이동할까요?"
    # SOURCE CH05 L379
    sia "가자!"
    $ story_stage(faces={"roman": "embarrassed"})
    # SOURCE CH05 L382
    roman "앗,,, 저 조금 떨려요……."
    # SOURCE CH05 L385
    mc "괜찮아요. 같이 준비한 만큼 보여드리면 되죠."
    # SOURCE CH05 L388
    lumi "그러게요. 혼자 발표하는 것도 아니니까."
    # SOURCE CH05 L391
    omu "가보자."
    # SOURCE CH05 L393 [SD EVENT] ch05_team_departure
    # SOURCE CH05 L397
    narrator "우리는 자료를 챙겨 동아리실을 나섰다."
    # SOURCE CH05 L399
    narrator "오늘은 정말 중요한 날이었다."
    # SOURCE CH05 L401 [SCENE 02 END]
    $ sd_event_end(restore=False, transition=0)
    jump ch05_sc03


label ch05_sc03:
    $ phone_timeline_enter("CH05", "ch05_sc03")
    # SOURCE CH05 L407 SCENE 03. 우리도 쉽게 질 생각 없거든
    # SOURCE CH05 L408 오전 11:00 · 평가 장소 앞 복도 · 라이벌 팀
    $ phone_timeline_cue("CH05", "CH05_L408")
    # SOURCE CH05 L409 SC03 · 우리도 쉽게 질 생각 없거든
    # SOURCE CH05 L410 [BG] 학생회관 평가실 앞 복도
    $ story_scene("corridor", cast=STORY_HEROES, light="day", location="학생회관 평가실 앞 복도")
    # SOURCE CH05 L412 [BGM] Rival Comedy
    $ play_bgm("rivalry_comedy")
    # SOURCE CH05 L416
    narrator "평가실 앞에는 이미 다른 참가팀 몇 명이 모여 있었다."
    # SOURCE CH05 L418
    narrator "그중에서 가장 눈에 띄는 사람은……"
    $ story_stage(cast=STORY_HEROES + ["hyeophap", "hess", "bambam"], faces={"hyeophap": "serious", "hess": "normal"})
    $ story_enter("ski", side="right", face="smug")
    # SOURCE CH05 L421
    ski "후후후."
    # SOURCE CH05 L425
    narrator "……설명할 필요도 없다."
    # SOURCE CH05 L428
    ski "드디어 결전의 날이군!"
    $ story_stage(faces={"sia": "confused"})
    # SOURCE CH05 L431
    sia "와, 너 아침부터 그러고 있었냐?"
    $ story_stage(faces={"ski": "smug"})
    # SOURCE CH05 L434
    ski "당연하지. 오늘은 내 천재성을 증명하는 날이니까."
    # SOURCE CH05 L437
    hyeophap "아까부터 저러고 있어."
    # SOURCE CH05 L440
    bambam "저희도 이제 익숙해졌어요."
    # SOURCE CH05 L443
    hess "조용할 때가 더 수상해요."
    # SOURCE CH05 L446
    ski "야, 너희는 왜 날 그렇게 평가하는데?"
    $ story_stage(faces={"hyeophap": "serious"})
    # SOURCE CH05 L449
    hyeophap "오늘은 우리가 평가받는 날이니까 그만해."
    # SOURCE CH05 L451 [SD EVENT] ch05_rival_hallway_01
    $ sd_event_start("ch05_rival_hallway_01")
    # SOURCE CH05 L454
    mc "안녕하세요. 준비는 잘되셨어요?"
    # SOURCE CH05 L457
    hyeophap "응. 거의 끝났어."
    # SOURCE CH05 L460
    ski "거의가 아니라 완벽하지."
    $ sd_event_end()
    # SOURCE CH05 L463
    hess "시식용 디저트 수량이랑 운영 시간까지 정리했어요."
    # SOURCE CH05 L466
    bambam "대기 안내 카드도 새로 만들었고요."
    $ story_stage(faces={"darim": "serious"})
    # SOURCE CH05 L469
    darim "지난번 시범 운영 문제를 많이 보완하셨네요."
    # SOURCE CH05 L472
    hyeophap "그때 서로 도와준 덕분이지."
    # SOURCE CH05 L475
    omu "동선 겹쳤던 거?"
    # SOURCE CH05 L478
    hyeophap "응. 오늘 자료에도 반영했어."
    $ story_stage(faces={"sia": "smug"})
    # SOURCE CH05 L481
    sia "그렇게 들으니까 우리가 도와준 건데?"
    # SOURCE CH05 L484
    ski "아니지. 우리도 너희 도와줬잖아."
    # SOURCE CH05 L487
    sia "응 아니야~"
    # SOURCE CH05 L490
    ski "이번에는 그 말 안 통한다."
    # SOURCE CH05 L494
    narrator "스키는 당당하게 작은 상자를 꺼냈다."
    # SOURCE CH05 L496
    narrator "안에는 여러 모양의 쿠키가 들어 있었다."
    $ story_stage(faces={"roman": "surprised"})
    # SOURCE CH05 L499
    roman "앗,,, 예쁘네요……!"
    # SOURCE CH05 L502
    ski "먹어봐. 오늘 시식용으로 준비한 거야."
    # SOURCE CH05 L505
    sia "……수상한데."
    # SOURCE CH05 L508
    ski "왜?"
    # SOURCE CH05 L511
    sia "경쟁 상대에게 쿠키를 준다니."
    # SOURCE CH05 L514
    ski "내 실력을 보여주는 거지."
    # SOURCE CH05 L517
    hyeophap "평가용으로 만든 시제품 중 여분이야."
    # SOURCE CH05 L520
    hyeophap "먹어보고 의견 주면 우리도 참고할 수 있고."
    # SOURCE CH05 L523
    mc "그럼 하나 먹어봐도 될까요?"
    # SOURCE CH05 L526
    ski "당연하지. 대신 감탄은 크게 해."
    # SOURCE CH05 L530
    narrator "쿠키를 한 입 베어 물었다."
    # SOURCE CH05 L532
    narrator "바삭한 식감 뒤로 부드러운 향이 퍼졌다."
    $ story_stage(faces={"ski": "happy"})
    # SOURCE CH05 L535
    mc "……맛있네요."
    # SOURCE CH05 L538
    ski "그렇지?"
    # SOURCE CH05 L541
    mc "정말 잘 만드셨어요."
    # SOURCE CH05 L544
    ski "하하! 역시 알아보는 사람이 있구나!"
    # SOURCE CH05 L547
    sia "아, 맛있는 건 맞는데 반응 때문에 주기 싫어진다."
    # SOURCE CH05 L550
    omu "니가 먼저 감탄하라 했잖아."
    $ story_stage(faces={"hess": "smug"})
    # SOURCE CH05 L553
    hess "실력과 말수가 반비례하면 좋겠네요."
    $ story_icon("ski", "exclamation")
    # SOURCE CH05 L556
    ski "헤스야!"
    # SOURCE CH05 L558 [SD EVENT] ch05_rival_hallway_02
    $ sd_event_start("ch05_rival_hallway_02")
    # SOURCE CH05 L562
    narrator "웃음소리가 복도에 퍼졌다."
    # SOURCE CH05 L564
    narrator "그러다 협합이 발표 자료를 다시 확인하며 말했다."
    # SOURCE CH05 L567
    hyeophap "장난은 여기까지."
    $ sd_event_end()
    # SOURCE CH05 L569
    hyeophap "오늘은 제대로 해보자."
    # SOURCE CH05 L572
    ski "……."
    # SOURCE CH05 L574
    ski "당연하지."
    $ story_stage(faces={"ski": "serious"})
    # SOURCE CH05 L578
    narrator "스키의 표정이 조금 진지해졌다."
    # SOURCE CH05 L581
    ski "우리도 준비한 게 많거든."
    # SOURCE CH05 L583
    ski "쉽게 질 생각 없어."
    $ story_stage(faces={"sia": "serious"})
    # SOURCE CH05 L586
    sia "우리도 마찬가지야."
    # SOURCE CH05 L589
    ski "그럼 결과로 보자."
    # SOURCE CH05 L592
    sia "좋아."
    # SOURCE CH05 L595
    mc "두 팀 다 후회 없이 발표했으면 좋겠네요."
    # SOURCE CH05 L598
    hyeophap "그러자."
    # SOURCE CH05 L602
    narrator "처음 만났을 때는 서로 이상한 팀이라고 생각했다."
    # SOURCE CH05 L604
    narrator "그런데 이제는 알 것 같았다."
    # SOURCE CH05 L606
    narrator "저 사람들도 우리만큼 이 축제를 진지하게 준비했다는 걸."
    # SOURCE CH05 L608 [SFX] 평가실 문 열리는 소리
    $ story_sfx("door")
    # SOURCE CH05 L611
    staff "다음 팀, 입장해주세요."
    $ story_stage(faces={"darim": "serious"})
    # SOURCE CH05 L614
    darim "저희 차례네요."
    # SOURCE CH05 L617
    sia "가자!"
    # SOURCE CH05 L619 [FADE OUT]
    # SOURCE CH05 L621 [SCENE 03 END]
    jump ch05_sc04


label ch05_sc04:
    $ phone_timeline_enter("CH05", "ch05_sc04")
    # SOURCE CH05 L627 SCENE 04. 마지막 평가
    # SOURCE CH05 L628 오전 11:30 · 학생회관 평가실 · CH02~CH04 사건 회수
    $ phone_timeline_cue("CH05", "CH05_L628")
    # SOURCE CH05 L629 SC04 · 마지막 평가
    # SOURCE CH05 L630 [BG] 학생회관 평가실
    $ story_scene("presentation", cast=STORY_HEROES, light="day", location="학생회관 평가실")
    # SOURCE CH05 L632 [BGM] Quiet Tension
    $ play_bgm("light_tension")
    # SOURCE CH05 L634 [FADE IN]
    # SOURCE CH05 L638
    narrator "평가실 안은 생각보다 조용했다."
    # SOURCE CH05 L640
    narrator "앞쪽에는 운영위원들이 앉아 있었고, 옆에는 준비해 온 자료를 보여줄 화면이 설치되어 있었다."
    # SOURCE CH05 L642
    narrator "우리는 나란히 앉아 마지막 순서를 기다렸다."
    # SOURCE CH05 L644 [시아 · 작은 목소리]
    $ story_stage(faces={"sia": "embarrassed"})
    # SOURCE CH05 L645
    sia "야."
    # SOURCE CH05 L648
    mc "네?"
    # SOURCE CH05 L651
    sia "나 지금 좀 떨리는 것 같은데."
    # SOURCE CH05 L654
    mc "시아 씨도 긴장하시는군요."
    $ story_stage(faces={"sia": "surprised", "lumi": "smug"})
    # SOURCE CH05 L657
    sia "뭐? 나도 사람이거든?"
    # SOURCE CH05 L660
    lumi "그건 오늘 처음 알았네요."
    # SOURCE CH05 L663
    sia "하린아."
    # SOURCE CH05 L666
    lumi "응?"
    # SOURCE CH05 L669
    sia "너 진짜 조금 있다 보자."
    # SOURCE CH05 L672
    lumi "발표부터 잘하고요."
    # SOURCE CH05 L676
    narrator "피식 웃음이 나왔다."
    # SOURCE CH05 L678
    narrator "잠깐이지만 긴장이 조금 풀렸다."
    # SOURCE CH05 L680 [SFX] 마이크 켜지는 소리
    # SOURCE CH05 L683
    staff "다음은 공동 체험 전시팀입니다."
    # SOURCE CH05 L685
    staff "준비하신 내용 발표해 주세요."
    $ story_stage(faces={"darim": "serious"})
    # SOURCE CH05 L688
    darim "네. 시작하겠습니다."
    # SOURCE CH05 L690 [BG] 발표 화면 · 전시 기획안
    # SOURCE CH05 L692 [BGM] Hopeful Presentation
    $ play_bgm("hopeful_teamwork")
    # SOURCE CH05 L695
    darim "저희는 대학생활에서 경험한 하루를 글과 사진, 그림으로 기록할 수 있는 참여형 전시를 준비했습니다."
    # SOURCE CH05 L697
    darim "방문객이 자신의 경험을 직접 남겨도 되고, 다른 사람의 기록을 둘러보는 것만으로도 참여할 수 있습니다."
    # SOURCE CH05 L701
    narrator "다림 선배의 목소리는 차분했다."
    # SOURCE CH05 L703
    narrator "지난 몇 주 동안 수없이 확인한 내용이었다."
    # SOURCE CH05 L705
    narrator "그런데 발표실에서 들으니 조금 새롭게 느껴졌다."
    # SOURCE CH05 L708
    staff "시범 운영에서 방문객이 참여 방법을 어려워했다는 의견이 있었죠?"
    # SOURCE CH05 L711
    darim "네. 그래서 진행 과정을 단순화했습니다."
    $ story_stage(faces={"sia": "serious"})
    # SOURCE CH05 L714
    sia "먼저 짧은 영상을 보여드리겠습니다."
    # SOURCE CH05 L716 [VIDEO EVENT] ch05_final_promo_video
    # SOURCE CH05 L718 [연출] 1분 이내 시연 영상의 주요 화면을 순서대로 표시. 실제 영상 에셋이 없다면 정지 프레임과 대사로 대체.
    # SOURCE CH05 L722
    narrator "화면 속 만화 캐릭터가 전시 부스로 들어갔다."
    # SOURCE CH05 L724
    narrator "질문 카드를 고르고, 종이에 짧은 글을 적고, 공개 여부를 선택했다."
    # SOURCE CH05 L726
    narrator "그다음에는 완성된 기록들이 모인 전시 공간이 나타났다."
    # SOURCE CH05 L728
    narrator "영상 마지막에는 한 문장이 떠올랐다."
    # SOURCE CH05 L730
    narrator "「누군가의 평범한 하루가, 다른 사람에게는 특별한 이야기가 될 수 있습니다.」"
    # SOURCE CH05 L734
    narrator "로만이 오래 고민했던 문장이었다."
    # SOURCE CH05 L736
    narrator "짧아졌지만, 처음 담고 싶어 했던 의미는 남아 있었다."
    # SOURCE CH05 L739
    sia "이렇게 처음 방문한 사람도 진행 과정을 쉽게 이해할 수 있도록 구성했습니다."
    # SOURCE CH05 L742
    staff "좋습니다. 그럼 실제로 사람이 몰렸을 때는 어떻게 운영할 예정인가요?"
    $ story_stage(faces={"lumi": "serious"})
    # SOURCE CH05 L745
    lumi "제가 설명드릴게요."
    # SOURCE CH05 L747 [BG] 부스 평면 배치도
    # SOURCE CH05 L750
    lumi "입구에서는 전시 소개를 볼 수 있고, 안쪽에 선택형 체험 공간을 배치했습니다."
    # SOURCE CH05 L752
    lumi "체험하지 않는 방문객도 관람할 수 있도록 이동 통로를 분리했어요."
    # SOURCE CH05 L755
    lumi "시범 운영에서는 통행이 겹치는 문제가 있었기 때문에, 이번에는 공용 통로까지 고려해 배치를 수정했습니다."
    # SOURCE CH05 L758
    staff "참여 인원이 많아지면 동선이 다시 복잡해질 가능성은 없을까요?"
    # SOURCE CH05 L761
    lumi "그래서 대기할 수 있는 위치를 별도로 표시했습니다."
    # SOURCE CH05 L763
    lumi "혼잡할 때는 체험을 잠시 조정하고 관람 중심으로 운영할 예정입니다."
    # SOURCE CH05 L767
    narrator "하린 선배는 모형을 돌려 보여줬다."
    # SOURCE CH05 L769
    narrator "CH04에서 함께 고쳤던 부분도 잘 보였다."
    # SOURCE CH05 L772
    staff "기록을 남긴 방문객이 나중에 공개를 원하지 않으면 어떻게 하나요?"
    # SOURCE CH05 L776
    narrator "잠깐 정적이 흘렀다."
    # SOURCE CH05 L778
    narrator "CH03에서 실제로 겪었던 문제였다."
    $ story_stage(faces={"roman": "serious"})
    # SOURCE CH05 L781
    roman "앗,,, 제가 설명드릴게요."
    # SOURCE CH05 L783
    roman "저희는 기록 작성과 공개 동의를 따로 확인하도록 바꿨어요."
    # SOURCE CH05 L785
    roman "공개를 원하지 않으면 전시하지 않고, 이미 전시한 기록도 철회를 요청하실 수 있어요."
    # SOURCE CH05 L788
    darim "접수된 요청은 운영 담당자가 확인한 뒤 해당 기록을 회수하도록 절차를 정리했습니다."
    # SOURCE CH05 L791
    staff "좋네요. 참여하지 않는 사람도 관람할 수 있다는 점은 특히 강조해 주세요."
    # SOURCE CH05 L794
    roman "네……!"
    # SOURCE CH05 L798
    narrator "로만은 고개를 끄덕였다."
    # SOURCE CH05 L800
    narrator "처음에는 작은 질문에도 당황하곤 했는데."
    # SOURCE CH05 L802
    narrator "오늘은 자신의 역할을 끝까지 설명했다."
    # SOURCE CH05 L805
    staff "사진 자료는 어떤 기준으로 선택하셨나요?"
    $ story_stage(faces={"omu": "serious"})
    # SOURCE CH05 L808
    omu "제가 말씀드릴게요."
    # SOURCE CH05 L810
    omu "공개해도 되는 자료만 사용했고, 사람이 식별되는 사진은 허락을 확인하거나 제외했습니다."
    # SOURCE CH05 L813
    omu "완성된 모습만 보여주기보다는 준비하는 과정도 일부 넣었어요."
    # SOURCE CH05 L815
    omu "이 부스가 어떻게 만들어졌는지도 보여주고 싶었거든요."
    # SOURCE CH05 L818
    mc "저도 그 사진들이 좋았어요. 준비하는 과정이 자연스럽게 느껴졌거든요."
    # SOURCE CH05 L821
    omu "……."
    # SOURCE CH05 L824
    omu "어. 그 부분을 보여주려고 했어요."
    # SOURCE CH05 L828
    narrator "오므가 짧게 웃었다."
    # SOURCE CH05 L830
    narrator "CH04에서는 사진 한 장을 두고 의견이 달랐는데."
    # SOURCE CH05 L832
    narrator "이제는 왜 그 사진을 남기고 싶었는지 조금 이해할 수 있었다."
    # SOURCE CH05 L835
    staff "알겠습니다. 마지막으로 한 가지 질문하겠습니다."
    # SOURCE CH05 L837
    staff "이 부스가 다른 체험 부스와 구별되는 가장 중요한 점은 무엇인가요?"
    # SOURCE CH05 L839 [BGM] 조용해짐
    # SOURCE CH05 L843
    narrator "모두 잠시 서로를 바라봤다."
    # SOURCE CH05 L845
    narrator "좋은 질문이었다."
    # SOURCE CH05 L847
    narrator "그런데 한 문장으로 답하려니 쉽지 않았다."
    # SOURCE CH05 L850
    darim "[player_name] 씨. 함께 준비하면서 느끼신 점을 말씀해 주실래요?"
    # SOURCE CH05 L854
    narrator "갑자기 시선이 나에게 향했다."
    # SOURCE CH05 L856
    narrator "……아니, 여기서 나한테?"
    # SOURCE CH05 L858
    narrator "하지만 생각해 보면 대답은 그렇게 어렵지 않았다."
    # SOURCE CH05 L859 [CHOICE] CH05 주요 발표 선택
    menu:
        # SOURCE CH05 L860
        "방문객의 선택을 존중하는 체험이라는 점을 강조한다.":
            # SOURCE CH05 L863
            mc "저희는 방문객이 꼭 기록을 남겨야 한다고 생각하지 않아요."
            # SOURCE CH05 L865
            mc "그냥 다른 사람의 이야기를 읽고 돌아가셔도 괜찮고, 본인의 이야기를 남기셔도 괜찮아요."
            # SOURCE CH05 L867
            mc "참여하는 방법을 스스로 선택할 수 있다는 점이 가장 중요하다고 생각합니다."
            # SOURCE CH05 L869 [FLAG] ch05_final_answer = autonomy
            $ story_apply("ch05_sc04_a", values={"ch05_final_answer": "autonomy"})
        # SOURCE CH05 L871
        "평범한 경험도 특별한 이야기가 될 수 있다는 점을 강조한다.":
            # SOURCE CH05 L874
            mc "특별한 경험을 한 사람만 이야기를 남길 수 있는 건 아니잖아요."
            # SOURCE CH05 L876
            mc "오늘 먹은 점심이나 친구와 나눈 대화도 누군가에게는 기억에 남는 순간일 수 있어요."
            # SOURCE CH05 L878
            mc "그런 평범한 하루를 서로 나눌 수 있다는 점이 저희 전시의 장점입니다."
            # SOURCE CH05 L880 [FLAG] ch05_final_answer = everyday
            $ story_apply("ch05_sc04_b", values={"ch05_final_answer": "everyday"})
        # SOURCE CH05 L882
        "여러 학과 학생이 함께 만들었다는 점을 강조한다.":
            # SOURCE CH05 L885
            mc "저희 팀은 전공도 다르고 생각하는 방식도 달라요."
            # SOURCE CH05 L887
            mc "처음에는 의견을 맞추는 게 어려웠지만, 각자의 장점을 살려 하나의 전시를 만들었습니다."
            # SOURCE CH05 L889
            mc "방문객도 서로 다른 방식으로 참여할 수 있다는 점이 저희 부스와 닮았다고 생각해요."
            # SOURCE CH05 L891 [FLAG] ch05_final_answer = teamwork
            $ story_apply("ch05_sc04_c", values={"ch05_final_answer": "teamwork"})
    # SOURCE CH05 L893 [공통 복귀]
    # SOURCE CH05 L896
    staff "좋은 설명 감사합니다."
    # SOURCE CH05 L898
    staff "준비하신 내용은 여기까지 확인하겠습니다."
    $ story_stage(faces={"darim": "happy"})
    # SOURCE CH05 L901
    darim "감사합니다."
    $ story_stage(faces={"sia": "happy"})
    # SOURCE CH05 L904
    sia "감사합니다!"
    $ story_stage(faces={"roman": "happy"})
    # SOURCE CH05 L907
    roman "감사합니다……!"
    # SOURCE CH05 L909 [SFX] 의자 움직이는 소리
    # SOURCE CH05 L911 [FADE TO] 평가실 밖 복도
    $ story_scene("corridor", cast=STORY_HEROES, light="day", location="평가실 밖 복도")
    # SOURCE CH05 L915
    narrator "문을 나서자마자 시아가 벽에 기대섰다."
    $ story_stage(faces={"sia": "sad", "omu": "normal"})
    # SOURCE CH05 L918
    sia "……아."
    # SOURCE CH05 L920
    sia "끝났다."
    # SOURCE CH05 L923
    omu "왜 니가 제일 힘들어하노."
    # SOURCE CH05 L926
    sia "영상 담당의 고충을 몰라서 그래."
    $ story_stage(faces={"lumi": "smug"})
    # SOURCE CH05 L929
    lumi "발표할 때는 그래도 멀쩡하셨네요."
    $ story_stage(faces={"sia": "smug"})
    # SOURCE CH05 L932
    sia "그래. 나 사실 프로거든."
    # SOURCE CH05 L935
    darim "후후. 모두 잘하셨어요."
    $ story_stage(faces={"roman": "embarrassed"})
    # SOURCE CH05 L938
    roman "앗,,, 질문이 어려울까 봐 걱정했는데……."
    # SOURCE CH05 L941
    mc "로만 씨 설명 잘하셨어요."
    $ story_stage(faces={"roman": "happy"})
    # SOURCE CH05 L944
    roman "……고마워요."
    # SOURCE CH05 L948
    narrator "끝났다."
    # SOURCE CH05 L950
    narrator "몇 주 동안 준비했던 자료를 마침내 보여줬다."
    # SOURCE CH05 L952
    narrator "이제 남은 건 결과였다."
    # SOURCE CH05 L954 [장면 전환]
    # SOURCE CH05 L956 [BG] 라이벌 팀 발표 대기 구역
    $ story_scene("corridor", cast=STORY_HEROES + ["ski", "hyeophap", "hess", "bambam"], light="day", location="라이벌 팀 발표 대기 구역")
    $ story_stage(faces={"ski": "happy"})
    # SOURCE CH05 L959
    ski "어땠어?"
    $ story_stage(faces={"sia": "smug"})
    # SOURCE CH05 L962
    sia "완벽했지."
    # SOURCE CH05 L965
    ski "그럼 우리가 더 완벽하게 해야겠네."
    $ story_stage(faces={"hyeophap": "serious"})
    # SOURCE CH05 L968
    hyeophap "그만 떠들고 들어갈 준비해."
    # SOURCE CH05 L971
    bambam "시식용 접시는 제가 가져갈게요."
    # SOURCE CH05 L974
    hess "설문 카드도 준비됐어요."
    # SOURCE CH05 L978
    narrator "라이벌 팀도 각자 자기 자리에서 움직였다."
    # SOURCE CH05 L981
    mc "스키 씨, 잘하고 오세요."
    $ story_stage(faces={"ski": "smug"})
    # SOURCE CH05 L984
    ski "당연하지."
    # SOURCE CH05 L986
    ski "끝나고 결과 보자!"
    # SOURCE CH05 L988 [SFX] 평가실 문 열림
    $ story_sfx("door")
    $ story_exit("ski")
    $ story_exit("hyeophap")
    $ story_exit("hess")
    $ story_exit("bambam")
    # SOURCE CH05 L992
    narrator "네 사람은 평가실 안으로 들어갔다."
    # SOURCE CH05 L994
    narrator "우리는 잠시 문을 바라봤다."
    # SOURCE CH05 L997
    sia "……야."
    # SOURCE CH05 L1000
    mc "네?"
    $ story_stage(faces={"sia": "serious"})
    # SOURCE CH05 L1003
    sia "쟤네도 진짜 열심히 했네."
    # SOURCE CH05 L1006
    mc "그러게요."
    # SOURCE CH05 L1010
    narrator "시끄럽고 이상한 라이벌이었다."
    # SOURCE CH05 L1012
    narrator "그래도 이번에는 조금 응원하고 싶었다."
    # SOURCE CH05 L1014 [FLAG] ch05_presentation_complete = True
    $ story_flag("ch05_presentation_complete", True)
    # SOURCE CH05 L1016 [SCENE 04 END]
    jump ch05_sc05

# CH05 SC05–SC06 · 대사와 콘티
# CH05 원고 SHA256 78c071ae87b63b3913dee545bd9b164f0ac3efb55f07eaf248c713d9e5b9101b
# SOURCE CH05 L 번호는 원고의 행 번호입니다. 콘티 표시는 화면에 표시하지 않습니다.

label ch05_sc05:
    $ phone_timeline_enter("CH05", "ch05_sc05")
    # SOURCE CH05 L1022 SCENE 05. 결과보다 중요한 것
    # SOURCE CH05 L1023 오후 2:20 · 학생회관 앞 · 최종 배정 결과
    $ phone_timeline_cue("CH05", "CH05_L1023")
    # SOURCE CH05 L1025 이번에는 CH01~CH04의 플레이 결과를 반영할 수 있도록 두 가지 배정 결과를 준비하자.
    # SOURCE CH05 L1027 단, 여기서 발표를 잘못했다고 부스가 취소되거나 히로인 루트가 잠기는 구조는 사용하지 않아.
    # SOURCE CH05 L1028 SC05 · 결과보다 중요한 것
    # SOURCE CH05 L1029 [BG] 학생회관 앞 휴게 공간 · 오후
    $ story_scene("board", cast=STORY_HEROES, light="day", location="학생회관 앞 휴게 공간 · 오후")
    # SOURCE CH05 L1031 [BGM] Waiting
    $ play_bgm("light_tension")
    # SOURCE CH05 L1033 [독백]
    # SOURCE CH05 L1035
    narrator "라이벌 팀의 발표도 끝났다."
    # SOURCE CH05 L1037
    narrator "운영위원회에서는 잠시 후 우선 배정 결과를 안내하겠다고 했다."
    # SOURCE CH05 L1039
    narrator "우리는 학생회관 앞에 모여 결과를 기다렸다."
    # SOURCE CH05 L1041 [시아]
    $ story_stage(faces={"sia": "embarrassed", "omu": "embarrassed"})
    # SOURCE CH05 L1042
    sia "야."
    # SOURCE CH05 L1044 [오므]
    # SOURCE CH05 L1045
    omu "왜."
    # SOURCE CH05 L1047 [시아]
    # SOURCE CH05 L1048
    sia "너도 떨리냐?"
    # SOURCE CH05 L1050 [오므]
    # SOURCE CH05 L1051
    omu "조금."
    # SOURCE CH05 L1053 [시아]
    # SOURCE CH05 L1054
    sia "나도."
    # SOURCE CH05 L1056 [오므]
    # SOURCE CH05 L1057
    omu "니 아까부터 떨린다 했잖아."
    # SOURCE CH05 L1059 [시아]
    # SOURCE CH05 L1060
    sia "그때랑 지금이랑 다르거든."
    # SOURCE CH05 L1062 [하린]
    $ story_stage(faces={"lumi": "smug"})
    # SOURCE CH05 L1063
    lumi "긴장에도 종류가 있었네요."
    # SOURCE CH05 L1065 [시아]
    # SOURCE CH05 L1066
    sia "당연하지."
    # SOURCE CH05 L1068 [다림]
    $ story_stage(faces={"darim": "happy"})
    # SOURCE CH05 L1069
    darim "후후. 이제 결과를 기다리는 일만 남았어요."
    # SOURCE CH05 L1071 [로만]
    $ story_stage(faces={"roman": "embarrassed"})
    # SOURCE CH05 L1072
    roman "앗,,, 잘됐으면 좋겠어요……."
    # SOURCE CH05 L1074 [주인공]
    # SOURCE CH05 L1075
    mc "네. 다들 열심히 준비했으니까요."
    $ story_sfx("message")
    # SOURCE CH05 L1077 [SFX] 스마트폰 진동
    # SOURCE CH05 L1079 [다림]
    $ story_stage(faces={"darim": "surprised"})
    # SOURCE CH05 L1080
    darim "……어?"
    # SOURCE CH05 L1082 [시아]
    $ story_stage(faces={"sia": "surprised"})
    # SOURCE CH05 L1083
    sia "왔다?"
    # SOURCE CH05 L1085 [다림]
    $ story_stage(faces={"darim": "serious"})
    # SOURCE CH05 L1086
    darim "네. 결과 안내가 왔어요."
    # SOURCE CH05 L1088 [UI] 축제 운영위원회 결과 안내
    $ story_chat(True, title="축제 운영위원회")
    $ phone_clock = "14:20"
    # SOURCE CH05 L1090 [CONDITION] team_preparation 및 최종 평가 결과에 따라 다음 중 하나를 표시. 정확한 판정 기준은 구현 단계에서 확정.
    # 임시 판정: 준비도 2 이상이고 발표를 마쳤다면 우선 배정. 두 결과 모두 축제 참가를 이어간다.
    # SOURCE CH05 L1092 [RESULT A] 우선 배정 성공
    if team_preparation >= 2 and ch05_presentation_complete:
        # SOURCE CH05 L1093
        system_note "「공동 체험 전시팀」"
        # SOURCE CH05 L1095
        system_note "「축제 부스 우선 배정 구역 선정」"
        $ story_chat(False)
        $ story_stage(cast=STORY_HEROES)
        # SOURCE CH05 L1097 [다림]
        $ story_stage(faces={"darim": "surprised"})
        # SOURCE CH05 L1098
        darim "……선정됐어요."
        # SOURCE CH05 L1100 [시아]
        $ story_stage(faces={"sia": "surprised"})
        # SOURCE CH05 L1101
        sia "……뭐?"
        # SOURCE CH05 L1103 [다림]
        $ story_stage(faces={"darim": "happy"})
        $ story_icon("darim", "exclamation")
        # SOURCE CH05 L1104
        darim "저희 우선 배정 구역이에요!"
        $ story_stage(faces={"roman": "surprised", "sia": "happy", "omu": "happy", "lumi": "happy"})
        # SOURCE CH05 L1106 [SD EVENT] ch05_result_success
        $ sd_event_start("ch05_result_success")
        # 콘티: 우선 배정 결과를 확인한 다섯 명의 환호와 안도. 완성형 단체 SD 컷.
        # SOURCE CH05 L1108 [시아]
        # SOURCE CH05 L1109
        sia "으아아아!"
        # SOURCE CH05 L1111 [로만]
        # SOURCE CH05 L1112
        roman "앗,,, 정말요?!"
        # SOURCE CH05 L1114 [오므]
        # SOURCE CH05 L1115
        omu "와, 진짜 됐네!"
        $ sd_event_end()
        # SOURCE CH05 L1117 [하린]
        # SOURCE CH05 L1118
        lumi "후후. 다들 고생한 보람이 있네요."
        # SOURCE CH05 L1120 [주인공]
        # SOURCE CH05 L1121
        mc "와…… 정말 다행이에요."
        # SOURCE CH05 L1123 [시아]
        # SOURCE CH05 L1124
        sia "야, 우리 진짜 해냈다!"
        # SOURCE CH05 L1126 [독백]
        $ story_effect("bounce", "sia")
        # SOURCE CH05 L1128
        narrator "시아가 양팔을 번쩍 들었다."
        # SOURCE CH05 L1130
        narrator "오므가 옆에서 웃었고, 로만은 믿기지 않는다는 듯 화면을 다시 확인했다."
        # SOURCE CH05 L1132
        narrator "다림 선배는 겨우 안도의 한숨을 내쉬었다."
        # SOURCE CH05 L1134 [다림]
        # SOURCE CH05 L1135
        darim "모두가 잘 준비해 준 덕분이에요."
        # SOURCE CH05 L1137 [하린]
        # SOURCE CH05 L1138
        lumi "부스 설치도 계획대로 할 수 있겠네요."
        # SOURCE CH05 L1140 [독백]
        # SOURCE CH05 L1142
        narrator "처음에는 다들 자기 의견만 내느라 정신이 없었는데."
        # SOURCE CH05 L1144
        narrator "그렇게 만든 부스가 실제로 좋은 평가를 받았다."
        # SOURCE CH05 L1146 [FLAG] ch05_booth_priority = True
        $ story_flag("ch05_booth_priority", True)
    # SOURCE CH05 L1148 [RESULT B] 일반 구역 배정
    else:
        # SOURCE CH05 L1149
        system_note "「공동 체험 전시팀」"
        # SOURCE CH05 L1151
        system_note "「축제 일반 부스 구역 배정」"
        $ story_chat(False)
        $ story_stage(cast=STORY_HEROES)
        # SOURCE CH05 L1153 [다림]
        $ story_stage(faces={"darim": "sad"})
        # SOURCE CH05 L1154
        darim "……일반 구역이네요."
        # SOURCE CH05 L1156 [시아]
        $ story_stage(faces={"sia": "surprised"})
        # SOURCE CH05 L1157
        sia "아."
        # SOURCE CH05 L1159 [로만]
        $ story_stage(faces={"roman": "sad"})
        # SOURCE CH05 L1160
        roman "앗,,, 아쉽네요……."
        # SOURCE CH05 L1162 [오므]
        $ story_stage(faces={"omu": "serious"})
        # SOURCE CH05 L1163
        omu "그래도 부스 운영은 하는 거지?"
        # SOURCE CH05 L1165 [다림]
        # SOURCE CH05 L1166
        darim "네. 참가에는 문제없어요."
        # SOURCE CH05 L1168 [하린]
        # SOURCE CH05 L1169
        lumi "다만 공간 크기가 조금 다르겠네요."
        # SOURCE CH05 L1171 [시아]
        $ story_stage(faces={"sia": "sad"})
        # SOURCE CH05 L1172
        sia "……."
        # SOURCE CH05 L1174 [시아]
        # SOURCE CH05 L1175
        sia "아, 진짜 아깝다."
        # SOURCE CH05 L1177 [독백]
        # SOURCE CH05 L1179
        narrator "시아가 입술을 삐죽 내밀었다."
        # SOURCE CH05 L1181
        narrator "나도 조금 아쉬웠다."
        # SOURCE CH05 L1183
        narrator "몇 주 동안 열심히 준비했으니까."
        # SOURCE CH05 L1185 [주인공]
        # SOURCE CH05 L1186
        mc "아쉽기는 하지만, 저희 전시를 못 하는 건 아니잖아요."
        # SOURCE CH05 L1188 [다림]
        $ story_stage(faces={"darim": "serious"})
        # SOURCE CH05 L1189
        darim "맞아요."
        # SOURCE CH05 L1191 [주인공]
        # SOURCE CH05 L1192
        mc "장소에 맞춰서 조금 수정하면 될 것 같아요."
        # SOURCE CH05 L1194 [하린]
        $ story_stage(faces={"lumi": "serious"})
        # SOURCE CH05 L1195
        lumi "네. 그 정도는 충분히 조정할 수 있어요."
        # SOURCE CH05 L1197 [오므]
        # SOURCE CH05 L1198
        omu "사진 배치도 다시 보면 되고."
        # SOURCE CH05 L1200 [로만]
        # SOURCE CH05 L1201
        roman "앗,,, 질문 카드 수량도 조정할게요."
        # SOURCE CH05 L1203 [시아]
        $ story_stage(faces={"sia": "happy"})
        # SOURCE CH05 L1204
        sia "……좋아."
        # SOURCE CH05 L1206
        sia "그럼 우리 일반 구역에서 제일 인기 많은 부스 만들자."
        # SOURCE CH05 L1208 [오므]
        # SOURCE CH05 L1209
        omu "갑자기 목표 커지네."
        # SOURCE CH05 L1211 [시아]
        # SOURCE CH05 L1212
        sia "원래 목표는 크게 잡는 거야."
        # SOURCE CH05 L1214 [독백]
        # SOURCE CH05 L1216
        narrator "기대했던 결과는 아니었다."
        # SOURCE CH05 L1218
        narrator "그래도 우리가 만든 게 사라진 건 아니다."
        # SOURCE CH05 L1220
        narrator "축제는 아직 시작도 하지 않았다."
        # SOURCE CH05 L1222 [FLAG] ch05_booth_priority = False
        $ story_flag("ch05_booth_priority", False)
    # SOURCE CH05 L1224 [공통 복귀]
    # SOURCE CH05 L1226 [SFX] 복도에서 다가오는 발소리
    # 발소리 뒤 라이벌 팀이 합류하고 스키가 오른쪽에서 등장한다.
    # SOURCE CH05 L1228 [스키]
    $ story_stage(cast=STORY_HEROES + ["hyeophap", "hess", "bambam"])
    $ story_enter("ski", side="right", face="happy")
    # SOURCE CH05 L1229
    ski "야!"
    # SOURCE CH05 L1231
    ski "너희 결과 나왔어?"
    # SOURCE CH05 L1233 [시아]
    $ story_stage(faces={"sia": "smug"})
    # SOURCE CH05 L1234
    sia "나왔지."
    # SOURCE CH05 L1236 [스키]
    # SOURCE CH05 L1237
    ski "우리도 나왔어."
    # SOURCE CH05 L1239 [협합]
    $ story_stage(faces={"hyeophap": "serious"})
    # SOURCE CH05 L1240
    hyeophap "스키, 목소리부터 좀 낮춰."
    # SOURCE CH05 L1242 [스키]
    # SOURCE CH05 L1243
    ski "이런 순간에 어떻게 조용히 해?"
    # SOURCE CH05 L1245 [헤스]
    # SOURCE CH05 L1246
    hess "결과는 이미 확인했는데요."
    # SOURCE CH05 L1248 [밤밤]
    $ story_stage(faces={"bambam": "happy"})
    # SOURCE CH05 L1249
    bambam "다들 고생 많으셨어요."
    # SOURCE CH05 L1251 [독백]
    # SOURCE CH05 L1253
    narrator "라이벌 팀도 결과를 확인한 모양이었다."
    # SOURCE CH05 L1255
    narrator "스키는 여전히 들떠 있었지만, 협합은 발표 자료가 든 파일을 차분하게 정리하고 있었다."
    # SOURCE CH05 L1257 [조건부 대사: 두 팀의 실제 배정 결과에 맞게 출력]
    # SOURCE CH05 L1258 - 우리가 우선 배정에 성공한 경우
    if ch05_booth_priority:
        # SOURCE CH05 L1259 [협합]
        # SOURCE CH05 L1260
        hyeophap "축하해. 이번에는 너희가 좋은 구역을 받았네."
        # SOURCE CH05 L1262 [스키]
        # SOURCE CH05 L1263
        ski "아쉽다. 다음에는 우리가 이길 거야."
        # SOURCE CH05 L1265 [시아]
        # SOURCE CH05 L1266
        sia "이번에는 우리가 이겼지롱."
        # SOURCE CH05 L1268 [스키]
        # SOURCE CH05 L1269
        ski "야, 아직 축제 당일이 남았거든?"
        # SOURCE CH05 L1271 [협합]
        # SOURCE CH05 L1272
        hyeophap "이제 구역 경쟁은 끝났어."
        # SOURCE CH05 L1274 [스키]
        # SOURCE CH05 L1275
        ski "……아, 그러네."
    # SOURCE CH05 L1276 - 우리가 일반 구역을 받은 경우
    else:
        # SOURCE CH05 L1277 [협합]
        # SOURCE CH05 L1278
        hyeophap "우리 쪽이 우선 배정을 받았어."
        # SOURCE CH05 L1280 [시아]
        # SOURCE CH05 L1281
        sia "……아, 부럽다."
        # SOURCE CH05 L1283 [스키]
        # SOURCE CH05 L1284
        ski "후후. 역시 내 실력이지."
        # SOURCE CH05 L1286 [헤스]
        # SOURCE CH05 L1287
        hess "네 명이 같이 준비한 결과죠."
        # SOURCE CH05 L1289 [밤밤]
        # SOURCE CH05 L1290
        bambam "그리고 부스 운영은 다 같이 하잖아요."
        # SOURCE CH05 L1292 [스키]
        # SOURCE CH05 L1293
        ski "……맞아, 맞아."
        # SOURCE CH05 L1295 [주인공]
        # SOURCE CH05 L1296
        mc "축하드려요. 정말 준비 많이 하셨잖아요."
        # SOURCE CH05 L1298 [협합]
        # SOURCE CH05 L1299
        hyeophap "고마워."
    # SOURCE CH05 L1301 [공통 복귀]
    # SOURCE CH05 L1303 [독백]
    # SOURCE CH05 L1305
    narrator "승부는 끝났다."
    # SOURCE CH05 L1307
    narrator "그런데 생각했던 것과는 조금 달랐다."
    # SOURCE CH05 L1309
    narrator "처음에는 서로를 이겨야만 한다고 생각했는데."
    # SOURCE CH05 L1311
    narrator "지금은 누가 이겼든 축제가 잘됐으면 좋겠다는 마음이 더 컸다."
    # SOURCE CH05 L1313 [협합]
    # SOURCE CH05 L1314
    hyeophap "축제 당일에는 방문객 동선이 또 겹칠 수도 있으니까."
    # SOURCE CH05 L1316
    hyeophap "그때는 서로 연락하자."
    # SOURCE CH05 L1318 [다림]
    # SOURCE CH05 L1319
    darim "네. 저희도 현장에서 협조할게요."
    # SOURCE CH05 L1321 [스키]
    # SOURCE CH05 L1322
    ski "그리고 우리 부스에도 놀러 와."
    # SOURCE CH05 L1324 [시아]
    $ story_stage(faces={"sia": "smug"})
    # SOURCE CH05 L1325
    sia "공짜 쿠키 주냐?"
    # SOURCE CH05 L1327 [스키]
    # SOURCE CH05 L1328
    ski "네가 오면 두 배 받아야겠다."
    # SOURCE CH05 L1330 [시아]
    $ story_stage(faces={"sia": "surprised"})
    # SOURCE CH05 L1331
    sia "야!"
    # SOURCE CH05 L1333 [오므]
    $ story_stage(faces={"omu": "happy"})
    # SOURCE CH05 L1334
    omu "ㅋㅋㅋㅋ"
    # SOURCE CH05 L1336 [하린]
    $ story_stage(faces={"lumi": "smug"})
    # SOURCE CH05 L1337
    lumi "끝까지 사이좋으시네요."
    # SOURCE CH05 L1339 [헤스]
    # SOURCE CH05 L1340
    hess "저게 사이좋은 거였군요."
    # SOURCE CH05 L1342 [밤밤]
    # SOURCE CH05 L1343
    bambam "저는 이제 그렇게 생각하기로 했어요."
    # SOURCE CH05 L1345 [SD EVENT] ch05_rival_after_result
    $ sd_event_start("ch05_rival_after_result")
    # 콘티: 결과를 공유한 두 팀이 다음 준비로 흩어지는 장면. 완성형 단체 SD 컷.
    # SOURCE CH05 L1347 [독백]
    # SOURCE CH05 L1349
    narrator "잠시 뒤 라이벌 팀은 다음 준비를 하러 떠났다."
    $ sd_event_end()
    $ story_exit("ski")
    $ story_exit("hyeophap")
    $ story_exit("hess")
    $ story_exit("bambam")
    # SOURCE CH05 L1351
    narrator "우리도 다시 모형과 운영표를 펼쳤다."
    # SOURCE CH05 L1353 [다림]
    $ story_stage(faces={"darim": "serious"})
    # SOURCE CH05 L1354
    darim "이제 최종 설치만 남았네요."
    # SOURCE CH05 L1356 [로만]
    $ story_stage(faces={"roman": "surprised"})
    # SOURCE CH05 L1357
    roman "앗,,, 벌써 여기까지 왔네요."
    # SOURCE CH05 L1359 [시아]
    # SOURCE CH05 L1360
    sia "그러게."
    # SOURCE CH05 L1362 [오므]
    # SOURCE CH05 L1363
    omu "처음에는 다들 뭐가 뭔지도 몰랐는데."
    # SOURCE CH05 L1365 [하린]
    $ story_stage(faces={"lumi": "happy"})
    # SOURCE CH05 L1366
    lumi "후후. 지금은 제법 팀 같죠?"
    # SOURCE CH05 L1368 [주인공]
    # SOURCE CH05 L1369
    mc "처음부터 팀은 맞았잖아요."
    # SOURCE CH05 L1371 [시아]
    # SOURCE CH05 L1372
    sia "아니, 그때는 그냥 시끄러운 사람들 모임이었지."
    # SOURCE CH05 L1374 [주인공]
    # SOURCE CH05 L1375
    mc "지금도 조금 그런 것 같은데요?"
    # SOURCE CH05 L1377 [시아]
    # SOURCE CH05 L1378
    sia "야ㅋㅋㅋ"
    # SOURCE CH05 L1380 [독백]
    # SOURCE CH05 L1382
    narrator "또 웃음이 터졌다."
    # SOURCE CH05 L1384
    narrator "결과도 중요했다."
    # SOURCE CH05 L1386
    narrator "하지만 그보다 더 기억에 남을 일이 이미 많이 생긴 것 같았다."
    # SOURCE CH05 L1388 [SCENE 05 END]
    jump ch05_sc06

label ch05_sc06:
    $ phone_timeline_enter("CH05", "ch05_sc06")
    # SOURCE CH05 L1394 SCENE 06. 다섯 개의 초대
    # SOURCE CH05 L1395 오후 3:30 · 캠퍼스 · 개인 이벤트 5종
    $ phone_timeline_cue("CH05", "CH05_L1395")
    # SOURCE CH05 L1397 이 장면은 이번 CH05의 로맨스 중심이야. 다만 CH04와 달리 다섯 명이 전부 주인공에게 고백에 가까운 초대를 하는 식으로 만들지는 않을 거야.
    # SOURCE CH05 L1399 각자의 목표나 취미에 맞는 약속을 제안하고, CH04에서 이미 함께했던 상대라면 추가 대사가 나오는 방식이야.
    # SOURCE CH05 L1401 CH05에서는 5개 초대를 모두 짧게 경험할 수 있도록 구성하고, SC07에서 축제 당일 동행할 상대를 선택하도록 하자.
    # SOURCE CH05 L1402 SC06 · 다섯 개의 초대
    # SOURCE CH05 L1403 [BG] 캠퍼스 중앙 광장 · 오후
    $ story_scene("campus", mode="normal", cast=[], light="day", location="캠퍼스 중앙 광장 · 오후", standing=False)
    # SOURCE CH05 L1405 [BGM] Warm Afternoon
    $ play_bgm("warm_workshop")
    # SOURCE CH05 L1407 [독백]
    # SOURCE CH05 L1409
    narrator "최종 평가가 끝난 뒤, 우리는 각자 남은 준비를 확인하고 잠시 흩어졌다."
    # SOURCE CH05 L1411
    narrator "그런데 축제 준비팀으로 함께할 시간이 얼마 남지 않았다는 생각 때문일까."
    # SOURCE CH05 L1413
    narrator "평소에는 별일 아니라고 넘겼을 대화가 조금 특별하게 느껴졌다."
    # SOURCE CH05 L1415 SC06-A. 로만 「조금만 들어주실래요?」
    # SOURCE CH05 L1416 [BG] 도서관 앞 벤치
    $ story_scene("campus", light="day", location="도서관 앞 벤치 · 오후")
    # SOURCE CH05 L1418 [ANIM] 로만 · 눈 깜빡임, 머리카락의 미세한 움직임
    # 콘티: 노트를 든 로만이 도서관 앞에서 조심스레 말을 거는 스탠딩.
    # SOURCE CH05 L1420 [독백]
    # SOURCE CH05 L1422
    narrator "도서관 앞을 지나가는데 익숙한 목소리가 들렸다."
    # SOURCE CH05 L1424 [로만]
    $ story_enter("roman", side="left", face="surprised")
    # SOURCE CH05 L1425
    roman "앗,,, [player_name] 씨!"
    # SOURCE CH05 L1427 [주인공]
    # SOURCE CH05 L1428
    mc "로만 씨. 여기서 뭐 하고 계세요?"
    # SOURCE CH05 L1430 [로만]
    $ story_stage(faces={"roman": "embarrassed"})
    # SOURCE CH05 L1431
    roman "아…… 자료를 반납하러 왔어요."
    # SOURCE CH05 L1433
    roman "그리고……."
    # SOURCE CH05 L1435 [독백]
    # SOURCE CH05 L1437
    narrator "로만은 손에 든 노트를 조금 들어 보였다."
    # SOURCE CH05 L1439 [주인공]
    # SOURCE CH05 L1440
    mc "또 글 쓰고 계셨어요?"
    # SOURCE CH05 L1442 [로만]
    $ story_stage(faces={"roman": "happy"})
    $ cg_start("ch05_private_roman")
    # SOURCE CH05 L1443
    roman "후후…… 네."
    # SOURCE CH05 L1445 [로만]
    # SOURCE CH05 L1446
    roman "축제 때 작은 낭독 행사도 있다고 해서요."
    # SOURCE CH05 L1448 [주인공]
    # SOURCE CH05 L1449
    mc "로만 씨도 참여하세요?"
    # SOURCE CH05 L1451 [로만]
    $ story_stage(faces={"roman": "embarrassed"})
    # SOURCE CH05 L1452
    roman "아, 아직은 아니에요……!"
    # SOURCE CH05 L1454
    roman "그냥 구경만 할까 생각 중이에요."
    # SOURCE CH05 L1456 [독백]
    # SOURCE CH05 L1458
    narrator "로만은 잠시 노트를 바라봤다."
    # SOURCE CH05 L1460 [로만]
    # SOURCE CH05 L1461
    roman "그런데……."
    # SOURCE CH05 L1463
    roman "혹시 축제 때 시간 있으시면 같이 가실래요?"
    # SOURCE CH05 L1465 [주인공]
    # SOURCE CH05 L1466
    mc "낭독 행사요?"
    # SOURCE CH05 L1468 [로만]
    # SOURCE CH05 L1469
    roman "네……!"
    # SOURCE CH05 L1471
    roman "혼자 가면 조금 긴장될 것 같아서요."
    # SOURCE CH05 L1473 [주인공]
    # SOURCE CH05 L1474
    mc "좋아요. 같이 가면 재미있겠네요."
    # SOURCE CH05 L1476 [로만]
    $ story_stage(faces={"roman": "happy"})
    # SOURCE CH05 L1477
    roman "……후후."
    # SOURCE CH05 L1479
    roman "그럼 저도 기대할게요."
    # SOURCE CH05 L1481 [CONDITION] ch04_partner == "roman"
    if story_id(ch04_partner) == "roman":
        # SOURCE CH05 L1483 [로만]
        # SOURCE CH05 L1484
        roman "아, 그리고 전에 말씀드린 글도 조금 더 썼어요."
        # SOURCE CH05 L1486 [주인공]
        # SOURCE CH05 L1487
        mc "정말요? 나중에 보여주시기로 했잖아요."
        # SOURCE CH05 L1489 [로만]
        # SOURCE CH05 L1490
        roman "앗,,, 기억하고 계셨네요……."
        # SOURCE CH05 L1492 [주인공]
        # SOURCE CH05 L1493
        mc "그럼요."
        # SOURCE CH05 L1495 [로만]
        # SOURCE CH05 L1496
        roman "……고마워요."
        # SOURCE CH05 L1498 [독백]
        # SOURCE CH05 L1500
        narrator "로만은 조심스럽게 웃었다."
        # SOURCE CH05 L1502
        narrator "CH04에서 보여주지 않겠다고 했던 문장까지 억지로 묻지는 않았다."
        # SOURCE CH05 L1504
        narrator "다만 로만이 언젠가 먼저 보여줄 날이 조금 기다려졌다."
    # SOURCE CH05 L1506 [공통 복귀]
    # SOURCE CH05 L1508 [로만]
    # SOURCE CH05 L1509
    roman "그럼 축제 때 연락드릴게요."
    # SOURCE CH05 L1511 [주인공]
    # SOURCE CH05 L1512
    mc "네. 조심히 들어가세요."
    # SOURCE CH05 L1514 [독백]
    # SOURCE CH05 L1516
    narrator "로만은 몇 걸음 걷다가 뒤돌아봤다."
    # SOURCE CH05 L1518 [로만]
    # SOURCE CH05 L1519
    roman "앗,,, 오늘 발표도 수고 많으셨어요!"
    # SOURCE CH05 L1521 [주인공]
    # SOURCE CH05 L1522
    mc "로만 씨도요!"
    # SOURCE CH05 L1524 [FLAG] ch05_invitation_seen["roman"] = True
    $ ch05_invitation_seen["roman"] = True
    $ cg_end()
    # SOURCE CH05 L1526 SC06-B. 시아 「내가 만든 거 보러 와」
    # SOURCE CH05 L1527 [BG] 애니메이션과 복도
    $ story_scene("corridor", cast=["sia"], light="day", location="애니메이션과 복도 · 오후")
    # SOURCE CH05 L1529 [BGM] Light Comedy
    $ play_bgm("comedy_light")
    # SOURCE CH05 L1531 [ANIM] 시아 · 눈 깜빡임, 가벼운 호흡
    # 콘티: 시아가 태블릿을 들어 보여주는 스탠딩.
    # SOURCE CH05 L1533 [독백]
    # SOURCE CH05 L1535
    narrator "강의동을 지나는데 복도 한쪽에서 시아가 손을 흔들었다."
    # SOURCE CH05 L1537 [시아]
    $ story_stage(faces={"sia": "happy"})
    $ story_effect("bounce", "sia")
    # SOURCE CH05 L1538
    sia "야! [player_name]!"
    # SOURCE CH05 L1540 [주인공]
    # SOURCE CH05 L1541
    mc "시아 씨, 여기 계셨네요."
    # SOURCE CH05 L1543 [시아]
    $ story_stage(faces={"sia": "normal"})
    # SOURCE CH05 L1544
    sia "응. 교수님한테 자료 내고 오는 길."
    # SOURCE CH05 L1546 [주인공]
    # SOURCE CH05 L1547
    mc "축제 준비도 끝나가는데 바쁘시네요."
    $ cg_start("ch05_private_sia")
    # SOURCE CH05 L1549 [시아]
    # SOURCE CH05 L1550
    sia "그러게."
    # SOURCE CH05 L1552
    sia "이쯤 되면 애니메이션학과가 아니라 밤샘학과야."
    # SOURCE CH05 L1554 [주인공]
    # SOURCE CH05 L1555
    mc "그건 조금 걱정되는데요."
    # SOURCE CH05 L1557 [시아]
    $ story_stage(faces={"sia": "smug"})
    # SOURCE CH05 L1558
    sia "농담이거든ㅋㅋ"
    # SOURCE CH05 L1560 [독백]
    # SOURCE CH05 L1562
    narrator "시아는 태블릿을 꺼내 화면을 보여줬다."
    # SOURCE CH05 L1564 [시아]
    # SOURCE CH05 L1565
    sia "이거 봐봐."
    # SOURCE CH05 L1567 [주인공]
    # SOURCE CH05 L1568
    mc "새로운 그림이에요?"
    # SOURCE CH05 L1570 [시아]
    # SOURCE CH05 L1571
    sia "응. 축제 때 전시할 수도 있대."
    # SOURCE CH05 L1573
    sia "우리 학과 작품 전시 코너 있거든."
    # SOURCE CH05 L1575 [독백]
    # SOURCE CH05 L1577
    narrator "화면에는 짧은 만화의 일부가 보였다."
    # SOURCE CH05 L1579 [주인공]
    # SOURCE CH05 L1580
    mc "오, 이거 재미있겠는데요?"
    # SOURCE CH05 L1582 [시아]
    # SOURCE CH05 L1583
    sia "그치?"
    # SOURCE CH05 L1585
    sia "근데 아직 완성은 아니야."
    # SOURCE CH05 L1587 [주인공]
    # SOURCE CH05 L1588
    mc "시아 씨는 늘 뭔가 만들고 계시네요."
    # SOURCE CH05 L1590 [시아]
    # SOURCE CH05 L1591
    sia "왜, 멋있냐?"
    # SOURCE CH05 L1593 [주인공]
    # SOURCE CH05 L1594
    mc "네. 좋아하는 걸 계속 만드는 건 멋있죠."
    # SOURCE CH05 L1596 [시아]
    $ story_stage(faces={"sia": "embarrassed"})
    # SOURCE CH05 L1597
    sia "……."
    # SOURCE CH05 L1599 [독백]
    # SOURCE CH05 L1601
    narrator "시아가 잠깐 말을 멈췄다."
    # SOURCE CH05 L1603 [시아]
    # SOURCE CH05 L1604
    sia "……야."
    # SOURCE CH05 L1606 [주인공]
    # SOURCE CH05 L1607
    mc "네?"
    # SOURCE CH05 L1609 [시아]
    # SOURCE CH05 L1610
    sia "너 진짜 가끔 사람 당황하게 한다."
    # SOURCE CH05 L1612 [주인공]
    # SOURCE CH05 L1613
    mc "제가요?"
    # SOURCE CH05 L1615 [시아]
    # SOURCE CH05 L1616
    sia "응."
    # SOURCE CH05 L1618
    sia "아무튼."
    # SOURCE CH05 L1620 [시아]
    $ story_stage(faces={"sia": "happy"})
    # SOURCE CH05 L1621
    sia "축제 때 우리 학과 전시도 보러 와."
    # SOURCE CH05 L1623 [주인공]
    # SOURCE CH05 L1624
    mc "좋아요. 시아 씨 작품도 있나요?"
    # SOURCE CH05 L1626 [시아]
    # SOURCE CH05 L1627
    sia "그럴 예정."
    # SOURCE CH05 L1629
    sia "그러니까 꼭 와라."
    # SOURCE CH05 L1631 [CONDITION] ch04_partner == "sia"
    if story_id(ch04_partner) == "sia":
        # SOURCE CH05 L1633 [시아]
        # SOURCE CH05 L1634
        sia "그리고 전에 말한 개인 웹툰도 기억하지?"
        # SOURCE CH05 L1636 [주인공]
        # SOURCE CH05 L1637
        mc "그럼요. 보여주시기로 하셨잖아요."
        # SOURCE CH05 L1639 [시아]
        # SOURCE CH05 L1640
        sia "오, 안 잊었네."
        # SOURCE CH05 L1642 [시아]
        # SOURCE CH05 L1643
        sia "그거는…… 축제 끝나고 따로 보여줄게."
        # SOURCE CH05 L1645 [주인공]
        # SOURCE CH05 L1646
        mc "왜 따로요?"
        # SOURCE CH05 L1648 [시아]
        # SOURCE CH05 L1649
        sia "……."
        # SOURCE CH05 L1651
        sia "그냥."
        # SOURCE CH05 L1653
        sia "첫 감상은 너한테 받고 싶어서."
        # SOURCE CH05 L1655 [독백]
        # SOURCE CH05 L1657
        narrator "시아는 아무렇지 않은 척했지만 시선을 조금 피했다."
        # SOURCE CH05 L1659 [시아]
        # SOURCE CH05 L1660
        sia "아, 뭐야. 왜 그렇게 봐?"
        # SOURCE CH05 L1662 [주인공]
        # SOURCE CH05 L1663
        mc "아무 말도 안 했는데요?"
        # SOURCE CH05 L1665 [시아]
        # SOURCE CH05 L1666
        sia "……응 아니야~"
    # SOURCE CH05 L1668 [공통 복귀]
    # SOURCE CH05 L1670 [시아]
    # SOURCE CH05 L1671
    sia "그럼 축제 때 봐."
    # SOURCE CH05 L1673
    sia "내 작품 보고 울지 마라?"
    # SOURCE CH05 L1675 [주인공]
    # SOURCE CH05 L1676
    mc "우는 장면도 있나요?"
    # SOURCE CH05 L1678 [시아]
    # SOURCE CH05 L1679
    sia "……아직 안 정했는데?"
    # SOURCE CH05 L1681 [주인공]
    # SOURCE CH05 L1682
    mc "그럼 일단 기대할게요."
    # SOURCE CH05 L1684 [시아]
    # SOURCE CH05 L1685
    sia "ㅋㅋㅋ 그래."
    # SOURCE CH05 L1687 [FLAG] ch05_invitation_seen["sia"] = True
    $ ch05_invitation_seen["sia"] = True
    $ cg_end()
    # SOURCE CH05 L1689 SC06-C. 다림 「일 말고 다른 약속」
    # SOURCE CH05 L1690 [BG] 캠퍼스 카페 앞 · 오후
    $ story_scene("cafe", cast=["darim"], light="day", location="캠퍼스 카페 앞 · 오후")
    # SOURCE CH05 L1692 [BGM] Gentle Daily
    $ play_bgm("gentle_walk")
    # SOURCE CH05 L1694 [ANIM] 다림 · 자연스러운 눈 깜빡임
    # 콘티: 음료 두 잔을 든 다림과 캠퍼스 카페 앞 스탠딩.
    # SOURCE CH05 L1696 [독백]
    # SOURCE CH05 L1698
    narrator "학생회관으로 돌아오는 길에 다림 선배를 만났다."
    # SOURCE CH05 L1700
    narrator "선배는 카페에서 음료 두 잔을 받아 나오고 있었다."
    # SOURCE CH05 L1702 [주인공]
    # SOURCE CH05 L1703
    mc "선배, 안녕하세요."
    # SOURCE CH05 L1705 [다림]
    $ story_stage(faces={"darim": "surprised"})
    # SOURCE CH05 L1706
    darim "어머, [player_name] 씨."
    # SOURCE CH05 L1708 [주인공]
    # SOURCE CH05 L1709
    mc "음료 많이 사셨네요."
    # SOURCE CH05 L1711 [다림]
    $ story_stage(faces={"darim": "happy"})
    # SOURCE CH05 L1712
    darim "하나는 로만 씨 거예요."
    $ cg_start("ch05_private_darim")
    # SOURCE CH05 L1714
    darim "발표 준비할 때 많이 긴장하셨잖아요."
    # SOURCE CH05 L1716 [독백]
    # SOURCE CH05 L1718
    narrator "역시 다림 선배답다."
    # SOURCE CH05 L1720
    narrator "그런데 오늘은 조금 다른 이야기를 하고 싶었다."
    # SOURCE CH05 L1722 [주인공]
    # SOURCE CH05 L1723
    mc "선배도 오늘 고생 많으셨어요."
    # SOURCE CH05 L1725 [다림]
    # SOURCE CH05 L1726
    darim "후후. 감사해요."
    # SOURCE CH05 L1728 [다림]
    # SOURCE CH05 L1729
    darim "그래도 다 같이 준비해서 생각보다 덜 힘들었어요."
    # SOURCE CH05 L1731 [주인공]
    # SOURCE CH05 L1732
    mc "지난번에 같이 일정 정리했던 게 도움이 됐나 봐요."
    # SOURCE CH05 L1734 [다림]
    $ story_stage(faces={"darim": "normal"})
    # SOURCE CH05 L1735
    darim "맞아요."
    # SOURCE CH05 L1737
    darim "그때 덕분에 생각이 조금 바뀌었거든요."
    # SOURCE CH05 L1739 [다림]
    # SOURCE CH05 L1740
    darim "다른 사람에게 부탁하는 것도 나쁘지 않더라고요."
    # SOURCE CH05 L1742 [주인공]
    # SOURCE CH05 L1743
    mc "그럼 다행이네요."
    # SOURCE CH05 L1745 [독백]
    $ story_stage(faces={"darim": "happy"})
    # SOURCE CH05 L1747
    narrator "다림은 작게 웃었다."
    # SOURCE CH05 L1749 [다림]
    # SOURCE CH05 L1750
    darim "그런데 축제 끝나면 다들 조금 한가해지겠죠?"
    # SOURCE CH05 L1752 [주인공]
    # SOURCE CH05 L1753
    mc "그렇겠죠."
    # SOURCE CH05 L1755 [다림]
    # SOURCE CH05 L1756
    darim "그럼……."
    # SOURCE CH05 L1758
    darim "전에 이야기했던 게임 약속, 기억하세요?"
    # SOURCE CH05 L1760 [주인공]
    # SOURCE CH05 L1761
    mc "네. 기억하죠."
    # SOURCE CH05 L1763 [다림]
    # SOURCE CH05 L1764
    darim "후후. 다행이네요."
    # SOURCE CH05 L1766 [다림]
    # SOURCE CH05 L1767
    darim "축제 때 게임 체험 부스도 있다고 하던데, 잠깐 구경할래요?"
    # SOURCE CH05 L1769 [주인공]
    # SOURCE CH05 L1770
    mc "좋아요."
    # SOURCE CH05 L1772 [다림]
    $ story_stage(faces={"darim": "smug"})
    # SOURCE CH05 L1773
    darim "물론 승부는 제가 이길 거예요."
    # SOURCE CH05 L1775 [주인공]
    # SOURCE CH05 L1776
    mc "아직 시작도 안 했는데요?"
    # SOURCE CH05 L1778 [다림]
    # SOURCE CH05 L1779
    darim "미리 알려드리는 거죠."
    # SOURCE CH05 L1781 [CONDITION] ch04_partner == "darim"
    if story_id(ch04_partner) == "darim":
        # SOURCE CH05 L1783 [다림]
        # SOURCE CH05 L1784
        darim "그리고 축제 끝나고는 진짜로 일 이야기 없이 만나봐요."
        # SOURCE CH05 L1786 [주인공]
        # SOURCE CH05 L1787
        mc "네. 저도 그러고 싶어요."
        # SOURCE CH05 L1789 [다림]
        # SOURCE CH05 L1790
        darim "……."
        # SOURCE CH05 L1792 [다림]
        # SOURCE CH05 L1793
        darim "후후. 그럼 약속이에요."
        # SOURCE CH05 L1795 [독백]
        # SOURCE CH05 L1797
        narrator "선배가 평소보다 조금 기분 좋게 웃었다."
    # SOURCE CH05 L1799 [공통 복귀]
    # SOURCE CH05 L1801 [다림]
    # SOURCE CH05 L1802
    darim "그럼 저는 로만 씨 음료 가져다드려야겠네요."
    # SOURCE CH05 L1804 [주인공]
    # SOURCE CH05 L1805
    mc "네. 조심히 가세요."
    # SOURCE CH05 L1807 [다림]
    # SOURCE CH05 L1808
    darim "다음에 봬요."
    # SOURCE CH05 L1810 [FLAG] ch05_invitation_seen["darim"] = True
    $ ch05_invitation_seen["darim"] = True
    $ cg_end()
    # SOURCE CH05 L1812 SC06-D. 오므 「마지막 풍경」
    # SOURCE CH05 L1813 [BG] 캠퍼스 중앙 광장 · 오후
    $ story_scene("campus", cast=["omu"], light="day", location="캠퍼스 중앙 광장 · 오후")
    # SOURCE CH05 L1815 [BGM] Warm Photography
    $ play_bgm("warm_workshop")
    # SOURCE CH05 L1817 [ANIM] 오므 · 눈 깜빡임, 머리카락 끝 미세 움직임
    # 콘티: 카메라를 든 오므와 광장 스탠딩.
    # SOURCE CH05 L1819 [독백]
    # SOURCE CH05 L1821
    narrator "광장에 나오자 카메라를 들고 있는 오므가 보였다."
    # SOURCE CH05 L1823 [주인공]
    # SOURCE CH05 L1824
    mc "오므 씨!"
    # SOURCE CH05 L1826 [오므]
    $ story_stage(faces={"omu": "normal"})
    # SOURCE CH05 L1827
    omu "어. 와?"
    # SOURCE CH05 L1829 [주인공]
    # SOURCE CH05 L1830
    mc "사진 찍고 계셨어요?"
    # SOURCE CH05 L1832 [오므]
    $ story_stage(faces={"omu": "happy"})
    # SOURCE CH05 L1833
    omu "어. 축제 준비하는 모습 좀 찍으려고."
    # SOURCE CH05 L1835 [주인공]
    # SOURCE CH05 L1836
    mc "아직 축제도 시작 안 했는데요?"
    # SOURCE CH05 L1838 [오므]
    $ cg_start("ch05_private_omu")
    # SOURCE CH05 L1839
    omu "준비하는 것도 축제잖아."
    # SOURCE CH05 L1841 [독백]
    # SOURCE CH05 L1843
    narrator "오므가 화면을 보여줬다."
    # SOURCE CH05 L1845
    narrator "축제 현수막을 설치하는 학생들."
    # SOURCE CH05 L1847
    narrator "종이 장식을 붙이는 사람들."
    # SOURCE CH05 L1849
    narrator "부스 앞에 쌓인 상자들."
    # SOURCE CH05 L1851 [주인공]
    # SOURCE CH05 L1852
    mc "이런 장면도 나중에 보면 재미있겠네요."
    # SOURCE CH05 L1854 [오므]
    # SOURCE CH05 L1855
    omu "그렇지?"
    # SOURCE CH05 L1857 [오므]
    # SOURCE CH05 L1858
    omu "축제 당일에는 사람도 많고 정신없을 것 같아서."
    # SOURCE CH05 L1860
    omu "지금 모습도 남겨놓으려고."
    # SOURCE CH05 L1862 [주인공]
    # SOURCE CH05 L1863
    mc "역시 오므 씨답네요."
    # SOURCE CH05 L1865 [오므]
    $ story_stage(faces={"omu": "confused"})
    # SOURCE CH05 L1866
    omu "그건 무슨 뜻인데."
    # SOURCE CH05 L1868 [주인공]
    # SOURCE CH05 L1869
    mc "사람들이 그냥 지나칠 장면도 잘 찾아내신다는 뜻이요."
    # SOURCE CH05 L1871 [오므]
    $ story_stage(faces={"omu": "embarrassed"})
    # SOURCE CH05 L1872
    omu "……."
    # SOURCE CH05 L1874
    omu "뭐, 칭찬으로 듣는다."
    # SOURCE CH05 L1876 [독백]
    # SOURCE CH05 L1878
    narrator "오므는 카메라를 다시 들었다."
    # SOURCE CH05 L1880 [오므]
    # SOURCE CH05 L1881
    omu "야, 니 축제 때 시간 있나?"
    # SOURCE CH05 L1883 [주인공]
    # SOURCE CH05 L1884
    mc "어느 시간대요?"
    # SOURCE CH05 L1886 [오므]
    $ story_stage(faces={"omu": "happy"})
    # SOURCE CH05 L1887
    omu "부스 교대하고 나서."
    # SOURCE CH05 L1889
    omu "같이 좀 돌아다니면서 사진 찍자."
    # SOURCE CH05 L1891 [주인공]
    # SOURCE CH05 L1892
    mc "좋아요. 재미있겠네요."
    # SOURCE CH05 L1894 [오므]
    # SOURCE CH05 L1895
    omu "어."
    # SOURCE CH05 L1897
    omu "해 질 때도 괜찮을 것 같은데."
    # SOURCE CH05 L1899 [CONDITION] ch04_partner == "omu"
    if story_id(ch04_partner) == "omu":
        # SOURCE CH05 L1901 [주인공]
        # SOURCE CH05 L1902
        mc "전에 학교 밖에도 같이 사진 찍으러 가자고 하셨잖아요."
        # SOURCE CH05 L1904 [오므]
        # SOURCE CH05 L1905
        omu "어. 기억하네?"
        # SOURCE CH05 L1907 [주인공]
        # SOURCE CH05 L1908
        mc "그럼요."
        # SOURCE CH05 L1910 [오므]
        # SOURCE CH05 L1911
        omu "그건 축제 끝나고 가자."
        # SOURCE CH05 L1913
        omu "이번에는 축제 사진부터 찍고."
        # SOURCE CH05 L1915 [주인공]
        # SOURCE CH05 L1916
        mc "좋아요."
        # SOURCE CH05 L1918 [오므]
        # SOURCE CH05 L1919
        omu "……어."
        # SOURCE CH05 L1921 [독백]
        # SOURCE CH05 L1923
        narrator "오므가 카메라를 고쳐 쥐었다."
    # SOURCE CH05 L1925 [공통 복귀]
    # SOURCE CH05 L1927 [오므]
    # SOURCE CH05 L1928
    omu "그리고 니 사진도 하나 찍어줄까?"
    # SOURCE CH05 L1930 [주인공]
    # SOURCE CH05 L1931
    mc "제 사진이요?"
    # SOURCE CH05 L1933 [오므]
    # SOURCE CH05 L1934
    omu "어. 추억으로 남기게."
    # SOURCE CH05 L1936 [주인공]
    # SOURCE CH05 L1937
    mc "그럼 그때 생각해볼게요."
    # SOURCE CH05 L1939 [오므]
    # SOURCE CH05 L1940
    omu "ㅋㅋㅋ 알았다."
    # SOURCE CH05 L1942 [독백]
    # SOURCE CH05 L1944
    narrator "나는 웃으면서 손을 흔들었다."
    $ cg_end()
    $ story_exit("omu")
    # SOURCE CH05 L1946
    narrator "오므는 다시 카메라를 들고 광장 쪽으로 걸어갔다."
    # SOURCE CH05 L1948 [FLAG] ch05_invitation_seen["omu"] = True
    $ ch05_invitation_seen["omu"] = True
    # SOURCE CH05 L1950 SC06-E. 하린 「완성된 공간」
    # SOURCE CH05 L1951 [BG] 건축학과 작업실 · 늦은 오후
    $ story_scene("architecture", light="evening", location="건축학과 작업실 · 늦은 오후")
    # SOURCE CH05 L1953 [BGM] Soft Evening
    $ play_bgm("evening_warm")
    # SOURCE CH05 L1955 [ANIM] 하린 · 미세 호흡, 자연스러운 눈 깜빡임
    # 콘티: 모형 앞에서 이야기하는 하린 스탠딩.
    # SOURCE CH05 L1957 [독백]
    # SOURCE CH05 L1959
    narrator "마지막으로 하린 선배에게 부스 배치에 관해 확인할 것이 있어 작업실로 향했다."
    $ story_sfx("door")
    $ story_stage_fade_in(["lumi"])
    # SOURCE CH05 L1961
    narrator "문을 열자 선배는 모형 앞에 앉아 있었다."
    # SOURCE CH05 L1963 [주인공]
    # SOURCE CH05 L1964
    mc "하린 선배, 잠깐 괜찮으세요?"
    # SOURCE CH05 L1966 [하린]
    $ story_stage(faces={"lumi": "normal"})
    # SOURCE CH05 L1967
    lumi "네. 들어오세요."
    # SOURCE CH05 L1969 [주인공]
    # SOURCE CH05 L1970
    mc "최종 설치할 때 필요한 물품 목록을 확인하려고요."
    # SOURCE CH05 L1972 [하린]
    $ story_stage(faces={"lumi": "happy"})
    # SOURCE CH05 L1973
    lumi "아, 여기 정리해뒀어요."
    # SOURCE CH05 L1975 [독백]
    # SOURCE CH05 L1977
    narrator "하린이 노트를 내밀었다."
    # SOURCE CH05 L1979
    narrator "작은 부품 하나까지 정리된 목록이었다."
    # SOURCE CH05 L1981 [주인공]
    # SOURCE CH05 L1982
    mc "정말 꼼꼼하시네요."
    # SOURCE CH05 L1984 [하린]
    $ story_stage(faces={"lumi": "smug"})
    $ cg_start("ch05_private_lumi")
    # SOURCE CH05 L1985
    lumi "후후. 그 정도는 해야죠."
    # SOURCE CH05 L1987 [하린]
    # SOURCE CH05 L1988
    lumi "지난번처럼 벽이 떨어지면 곤란하니까."
    # SOURCE CH05 L1990 [주인공]
    # SOURCE CH05 L1991
    mc "그때는 조금 놀랐어요."
    # SOURCE CH05 L1993 [하린]
    # SOURCE CH05 L1994
    lumi "저도요."
    # SOURCE CH05 L1996 [독백]
    # SOURCE CH05 L1998
    narrator "하린은 모형을 바라봤다."
    # SOURCE CH05 L2000 [하린]
    $ story_stage(faces={"lumi": "normal"})
    # SOURCE CH05 L2001
    lumi "그런데……."
    # SOURCE CH05 L2003
    lumi "그날 같이 고쳤던 부분이 지금은 제일 마음에 들어요."
    # SOURCE CH05 L2005 [주인공]
    # SOURCE CH05 L2006
    mc "정말요?"
    # SOURCE CH05 L2008 [하린]
    # SOURCE CH05 L2009
    lumi "네."
    # SOURCE CH05 L2011
    lumi "처음에는 조금 거슬렸는데."
    # SOURCE CH05 L2013
    lumi "지금 보니까 꼭 처음 생각한 모양이 아니어도 괜찮은 것 같아서."
    # SOURCE CH05 L2015 [독백]
    $ story_stage(faces={"lumi": "happy"})
    # SOURCE CH05 L2017
    narrator "선배는 그렇게 말하며 작게 웃었다."
    # SOURCE CH05 L2019 [하린]
    # SOURCE CH05 L2020
    lumi "축제 시작하면 실제 공간도 완성되겠네요."
    # SOURCE CH05 L2022 [주인공]
    # SOURCE CH05 L2023
    mc "네. 이제 얼마 안 남았어요."
    # SOURCE CH05 L2025 [하린]
    # SOURCE CH05 L2026
    lumi "……그러게요."
    # SOURCE CH05 L2028 [주인공]
    # SOURCE CH05 L2029
    mc "아쉬우세요?"
    # SOURCE CH05 L2031 [하린]
    # SOURCE CH05 L2032
    lumi "조금?"
    # SOURCE CH05 L2034
    lumi "맨날 부스 만들면서 정신없었잖아요."
    # SOURCE CH05 L2036 [하린]
    # SOURCE CH05 L2037
    lumi "끝나면 편할 줄 알았는데, 막상 끝난다고 생각하니까 좀 이상하네."
    # SOURCE CH05 L2039 [독백]
    # SOURCE CH05 L2041
    narrator "그 말에 나도 모르게 고개가 끄덕여졌다."
    # SOURCE CH05 L2043 [주인공]
    # SOURCE CH05 L2044
    mc "저도 그래요."
    # SOURCE CH05 L2046 [하린]
    $ story_stage(faces={"lumi": "embarrassed"})
    # SOURCE CH05 L2047
    lumi "……."
    # SOURCE CH05 L2049 [하린]
    # SOURCE CH05 L2050
    lumi "그럼 축제 시작하기 전에, 완성된 부스를 같이 한 번 둘러볼래요?"
    # SOURCE CH05 L2052 [주인공]
    # SOURCE CH05 L2053
    mc "좋아요."
    # SOURCE CH05 L2055 [하린]
    # SOURCE CH05 L2056
    lumi "다른 사람들 오기 전에 잠깐이면 돼요."
    # SOURCE CH05 L2058 [주인공]
    # SOURCE CH05 L2059
    mc "네. 저도 직접 보고 싶어요."
    # SOURCE CH05 L2061 [CONDITION] ch04_partner == "harin"
    if story_id(ch04_partner) == "lumi":
        # SOURCE CH05 L2063 [하린]
        # SOURCE CH05 L2064
        lumi "지난번에 약속했던 거 기억하고 계셨네요."
        # SOURCE CH05 L2066 [주인공]
        # SOURCE CH05 L2067
        mc "네. 선배가 마지막도 같이 봐달라고 하셨잖아요."
        # SOURCE CH05 L2069 [하린]
        # SOURCE CH05 L2070
        lumi "……."
        # SOURCE CH05 L2072 [하린]
        # SOURCE CH05 L2073
        lumi "그런 건 또 잘 기억하시네."
        # SOURCE CH05 L2075 [주인공]
        # SOURCE CH05 L2076
        mc "중요한 약속이니까요."
        # SOURCE CH05 L2078 [ANIM] 하린이 눈을 깜빡인 뒤 잠시 시선을 피한다.
        # 콘티: 약속을 중요하게 기억하는 주인공의 말을 듣고 잠시 시선을 피하는 하린 표정 전환.
        # SOURCE CH05 L2080 [하린]
        # SOURCE CH05 L2081
        lumi "……진짜."
        # SOURCE CH05 L2083
        lumi "그런 말을 아무렇지도 않게 하시네요."
    # SOURCE CH05 L2085 [공통 복귀]
    # SOURCE CH05 L2087 [독백]
    # SOURCE CH05 L2089
    narrator "하린은 모형을 다시 바라봤다."
    # SOURCE CH05 L2091
    narrator "그런데 조금 전보다 표정이 부드러워 보였다."
    # SOURCE CH05 L2093 [하린]
    # SOURCE CH05 L2094
    lumi "그럼 축제 때 봬요."
    # SOURCE CH05 L2096 [주인공]
    # SOURCE CH05 L2097
    mc "네. 오늘도 고생 많으셨어요."
    # SOURCE CH05 L2099 [FLAG] ch05_invitation_seen["harin"] = True
    $ ch05_invitation_seen["lumi"] = True
    # SOURCE CH05 L2101 SC06 공통 마무리
    $ cg_end()
    # SOURCE CH05 L2102 [BG] 캠퍼스 산책로 · 저녁
    $ story_scene("campus", mode="normal", cast=[], light="evening", location="캠퍼스 산책로 · 저녁", standing=False)
    # SOURCE CH05 L2104 [BGM] Sunset Campus
    $ play_bgm("evening_warm")
    # SOURCE CH05 L2106 [독백]
    # SOURCE CH05 L2108
    narrator "어느새 해가 지고 있었다."
    # SOURCE CH05 L2110
    narrator "오늘은 발표 때문에 정신없을 줄 알았는데, 생각보다 여러 사람과 이야기를 나눴다."
    # SOURCE CH05 L2112
    narrator "로만은 낭독 행사를 함께 구경하자고 했다."
    # SOURCE CH05 L2114
    narrator "시아는 자신이 만든 그림을 보러 오라고 했다."
    # SOURCE CH05 L2116
    narrator "다림 선배는 게임 체험 부스를 이야기했고."
    # SOURCE CH05 L2118
    narrator "오므는 함께 사진을 찍자고 했다."
    # SOURCE CH05 L2120
    narrator "하린 선배는 완성된 부스를 같이 둘러보자고 했다."
    # SOURCE CH05 L2122
    narrator "모두 평범한 제안이었다."
    # SOURCE CH05 L2124
    narrator "친구끼리도 충분히 할 수 있는 약속."
    # SOURCE CH05 L2126
    narrator "그런데 이상하게도 누구와 시간을 보낼지 생각하는 것만으로 조금 설렜다."
    # SOURCE CH05 L2128 [주인공 · 혼잣말]
    # SOURCE CH05 L2129
    mc "……이거 참."
    # SOURCE CH05 L2131 [독백]
    # SOURCE CH05 L2133
    narrator "축제를 준비하면서 사람을 이렇게 많이 알게 될 줄은 몰랐다."
    # SOURCE CH05 L2135
    narrator "그리고 그중 누군가와 더 가까워지고 싶다는 생각을 하게 될 줄도."
    # SOURCE CH05 L2137 [SCENE 06 END]
    jump ch05_sc07

# CH05 · SC07–SC09 축제 동행, 부스 설치, 축제 전날 / 대사와 콘티
# 원고 SHA256: 78c071ae87b63b3913dee545bd9b164f0ac3efb55f07eaf248c713d9e5b9101b
# SD·CG·촬영·전환 지시는 해당 대사 옆 원고 주석으로 보존한다.

# SOURCE CH05 L2143 SCENE 07. 누구와 축제를 즐길까?
# SOURCE CH05 L2144 오후 7:20 · 주인공 방 · CH06 동행 상대 선택
# SOURCE CH05 L2145 SC07 · 누구와 축제를 즐길까?
label ch05_sc07:
    $ phone_timeline_enter("CH05", "ch05_sc07")
    # SOURCE CH05 L2146 [BG] 주인공 방 · 저녁
    $ story_scene("room", cast=[], standing=False, light="evening", location="주인공 방 · 저녁")
    # SOURCE CH05 L2148 [BGM] Romantic Daily
    $ play_bgm("romantic")
    # SOURCE CH05 L2152
    narrator "방으로 돌아와 책상에 앉았다."
    # SOURCE CH05 L2154
    narrator "축제 일정표를 열어봤다."
    # SOURCE CH05 L2156
    narrator "생각보다 행사가 많았다."
    # SOURCE CH05 L2158
    narrator "공연도 있고, 작품 전시도 있고, 체험 부스도 있었다."
    # SOURCE CH05 L2160
    narrator "그런데 가장 먼저 눈에 들어온 건 오늘 들었던 약속들이었다."
    # SOURCE CH05 L2162
    narrator "누구와 먼저 시간을 보내면 좋을까."
    # SOURCE CH05 L2164 [SFX] 스마트폰 진동
    # SOURCE CH05 L2166 [UI] 축제 준비팀 (6)
    $ story_chat(True, title="축제 준비팀")
    $ phone_clock = "19:20"
    # SOURCE CH05 L2169
    darim "다들 최종 평가 수고 많으셨어요."
    # SOURCE CH05 L2171
    darim "축제 당일에는 교대 시간을 정해서 쉴 수 있도록 할게요."
    # SOURCE CH05 L2174
    sia "드디어 놀 시간 생기냐"
    # SOURCE CH05 L2177
    omu "일단 일부터 해라"
    # SOURCE CH05 L2180
    sia "아 축제인데 놀아야지"
    # SOURCE CH05 L2183
    lumi "놀 시간도 일정에 포함해둘게요."
    # SOURCE CH05 L2186
    roman "앗,,, 그럼 조금 구경할 수 있겠네요……!"
    # SOURCE CH05 L2189
    darim "네. 모두 한 번씩은 쉴 수 있게 조정해 봐요."
    # SOURCE CH05 L2192
    mc "저도 교대 시간 정하는 거 도울게요."
    # SOURCE CH05 L2195
    darim "감사해요."
    # SOURCE CH05 L2199
    narrator "곧 교대 일정이 정리되어 올라왔다."
    # SOURCE CH05 L2201
    narrator "다섯 명 모두와 종일 함께 다닐 수는 없겠지만, 쉬는 시간에 한 사람과 조금 더 오래 시간을 보낼 수는 있을 것 같았다."
    # SOURCE CH05 L2203 [UI] 개인적인 약속 확인
    # SOURCE CH05 L2207
    narrator "이상하다."
    # SOURCE CH05 L2209
    narrator "누구와 가든 재미있을 것 같다."
    # SOURCE CH05 L2211
    narrator "그런데 오늘은 조금 더 특별하게 시간을 보내고 싶은 사람이 있었다."
    # SOURCE CH05 L2212 [CHOICE] 축제 때 누구와 함께할까?
    menu:
        "축제 때 누구와 함께할까?"
        # SOURCE CH05 L2213
        "로만 씨와 낭독 행사 구경하기":
            $ story_apply("ch05_sc07_partner_roman", values={"ch06_festival_partner": "roman"})
        # SOURCE CH05 L2215
        "시아 씨와 애니메이션 작품 전시 구경하기":
            $ story_apply("ch05_sc07_partner_sia", values={"ch06_festival_partner": "sia"})
        # SOURCE CH05 L2217
        "다림 선배와 게임 체험 부스 가보기":
            $ story_apply("ch05_sc07_partner_darim", values={"ch06_festival_partner": "darim"})
        # SOURCE CH05 L2219
        "오므 씨와 축제 사진 찍으러 가기":
            $ story_apply("ch05_sc07_partner_omu", values={"ch06_festival_partner": "omu"})
        # SOURCE CH05 L2221
        "하린 선배와 완성된 공간 둘러보기":
            $ story_apply("ch05_sc07_partner_lumi", values={"ch06_festival_partner": "lumi"})
    # SOURCE CH05 L2223 [FLAG] ch06_festival_partner에 선택한 캐릭터 ID 저장
    # SOURCE CH05 L2225 [중요] 이 선택은 CH06의 개인 이벤트를 정할 뿐, 개별 루트 진입을 확정하지 않음.
    # SOURCE CH05 L2227 [CONDITION] 선택한 히로인의 답장만 표시
    # SOURCE CH05 L2228 로만 선택
    if ch06_festival_partner == "roman":
        $ story_chat(True, title="로만")
        $ phone_clock = "19:20"
        # SOURCE CH05 L2230
        mc "로만 씨, 축제 때 말씀하신 낭독 행사 같이 보러 갈까요?"
        # SOURCE CH05 L2233
        roman "앗,,, 정말요……?"
        # SOURCE CH05 L2235
        roman "네! 좋아요."
        # SOURCE CH05 L2237
        roman "그럼 시간 확인해서 연락드릴게요……!"
        # SOURCE CH05 L2241
        narrator "로만은 기쁜 마음을 숨기지 못하는 것 같았다."
        # SOURCE CH05 L2243
        narrator "나도 모르게 웃음이 나왔다."
    # SOURCE CH05 L2244 시아 선택
    elif ch06_festival_partner == "sia":
        $ story_chat(True, title="시아")
        $ phone_clock = "19:20"
        # SOURCE CH05 L2246
        mc "시아 씨, 축제 때 작품 전시 보러 갈게요. 같이 구경할까요?"
        # SOURCE CH05 L2249
        sia "오ㅋㅋ"
        # SOURCE CH05 L2251
        sia "내 작품을 그렇게 보고 싶었냐"
        # SOURCE CH05 L2254
        mc "네. 직접 설명도 듣고 싶어요."
        # SOURCE CH05 L2257
        sia "……."
        # SOURCE CH05 L2259
        sia "좋아. 특별 해설해준다"
        # SOURCE CH05 L2261
        sia "대신 칭찬 많이 해라"
        # SOURCE CH05 L2265
        narrator "여전히 시아답다."
        # SOURCE CH05 L2267
        narrator "그런데 작품을 보여주겠다는 말이 조금 기대됐다."
    # SOURCE CH05 L2268 다림 선택
    elif ch06_festival_partner == "darim":
        $ story_chat(True, title="다림")
        $ phone_clock = "19:20"
        # SOURCE CH05 L2270
        mc "선배, 축제 때 게임 체험 부스 같이 가실래요?"
        # SOURCE CH05 L2273
        darim "후후. 좋아요."
        # SOURCE CH05 L2275
        darim "그런데 이번에는 정말 승부예요."
        # SOURCE CH05 L2278
        mc "저도 제대로 준비할게요."
        # SOURCE CH05 L2281
        darim "기대하고 있을게요."
        # SOURCE CH05 L2285
        narrator "선배와 게임을 하게 되면 또 무슨 일이 벌어질까."
        # SOURCE CH05 L2287
        narrator "조금 걱정되면서도 재미있을 것 같았다."
    # SOURCE CH05 L2288 오므 선택
    elif ch06_festival_partner == "omu":
        $ story_chat(True, title="오므")
        $ phone_clock = "19:20"
        # SOURCE CH05 L2290
        mc "오므 씨, 축제 때 같이 사진 찍으러 가요."
        # SOURCE CH05 L2293
        omu "오. 니가 먼저 연락하네"
        # SOURCE CH05 L2295
        omu "좋지"
        # SOURCE CH05 L2297
        omu "해 질 때쯤 괜찮겠나?"
        # SOURCE CH05 L2300
        mc "네. 그때 시간 비워둘게요."
        # SOURCE CH05 L2303
        omu "어. 그럼 그때 보자"
        # SOURCE CH05 L2307
        narrator "오므와 함께 보는 축제의 풍경은 조금 다르게 보일지도 모르겠다."
    # SOURCE CH05 L2308 하린 선택
    elif ch06_festival_partner == "lumi":
        $ story_chat(True, title="하린")
        $ phone_clock = "19:20"
        # SOURCE CH05 L2310
        mc "하린 선배, 축제 때 완성된 부스 같이 둘러보기로 한 거 기억하시죠?"
        # SOURCE CH05 L2313
        lumi "네. 기억하죠."
        # SOURCE CH05 L2315
        lumi "그런데 먼저 연락하실 줄은 몰랐네요."
        # SOURCE CH05 L2318
        mc "약속했으니까요."
        # SOURCE CH05 L2321
        lumi "……후후."
        # SOURCE CH05 L2323
        lumi "그럼 축제 시작 전에 잠깐 만나요."
        # SOURCE CH05 L2327
        narrator "하린 선배의 대답이 평소보다 조금 부드럽게 느껴졌다."
    # SOURCE CH05 L2329 [공통 복귀]
    # SOURCE CH05 L2331 [UI] 스마트폰 화면 종료
    $ story_chat(False)
    # SOURCE CH05 L2335
    narrator "약속을 정하고 나니 축제가 조금 더 기다려졌다."
    # SOURCE CH05 L2337
    narrator "부스가 잘 운영되는 것도 중요하지만."
    # SOURCE CH05 L2339
    narrator "이제는 다른 이유로도 그날이 기대됐다."
    # SOURCE CH05 L2341 [SCENE 07 END]
    jump ch05_sc08

# SOURCE CH05 L2347 SCENE 08. 우리의 축제가 시작된다
# SOURCE CH05 L2348 축제 전날 D-1 · 오후 4:00 · 부스 설치 및 마지막 단체 이벤트
label ch05_sc08:
    $ phone_timeline_enter("CH05", "ch05_sc08")
    # SOURCE CH05 L2350 [연출] SC07 이후 며칠 경과. 날짜가 바뀌는 몽타주를 넣고, 축제 전날로 이동한다.
    # SOURCE CH05 L2351 SC08 · 우리의 축제가 시작된다
    # SOURCE CH05 L2352 [TRANSITION] 날짜가 넘어가는 몽타주
    # SOURCE CH05 L2356 [BG] 동아리실
    $ story_scene("clubroom307", cast=[], standing=False, light="day", location="공동 동아리실")
    # SOURCE CH05 L2354
    narrator "축제까지 D-5"
    # SOURCE CH05 L2360
    narrator "며칠 동안 우리는 최종 배정된 장소에 맞춰 설치 자재를 정리했다."
    # SOURCE CH05 L2362
    narrator "하린 선배는 공간을 다시 확인했고, 다림 선배는 운영 시간을 조정했다."
    # SOURCE CH05 L2366 [BG] 캠퍼스 광장
    $ story_scene("campus", cast=[], standing=False, light="day", location="캠퍼스 광장")
    # SOURCE CH05 L2364
    narrator "축제까지 D-3"
    # SOURCE CH05 L2370
    narrator "시아와 로만은 안내 자료를 마지막으로 수정했다."
    # SOURCE CH05 L2372
    narrator "오므는 실제 설치 공간을 촬영했다."
    # SOURCE CH05 L2374
    narrator "라이벌 팀도 옆에서 분주하게 움직였다."
    # SOURCE CH05 L2378 [BG] 축제 부스 설치 구역 · 오후
    $ story_scene("booth", cast=STORY_HEROES, light="day", location="축제 부스 설치 구역 · 오후")
    # SOURCE CH05 L2380 [BGM] Exciting Preparation
    $ play_bgm("hopeful_teamwork")
    # SOURCE CH05 L2382 [FADE IN]
    # SOURCE CH05 L2376
    narrator "축제까지 D-1"
    # SOURCE CH05 L2386
    narrator "드디어 축제 전날이 됐다."
    # SOURCE CH05 L2388
    narrator "광장에는 여러 부스가 설치되고 있었고, 학생들은 현수막을 붙이거나 물품을 옮기느라 바빴다."
    # SOURCE CH05 L2390
    narrator "며칠 전까지 모형으로만 보던 공간이 이제 실제 크기로 눈앞에 있었다."
    $ story_stage(faces={"sia": "surprised"})
    # SOURCE CH05 L2393
    sia "……야."
    # SOURCE CH05 L2396
    omu "왜."
    $ story_stage(faces={"sia": "happy"})
    # SOURCE CH05 L2399
    sia "우리 부스 진짜 생겼다."
    # SOURCE CH05 L2402
    omu "당연하지. 지금 만들고 있잖아."
    # SOURCE CH05 L2405
    sia "아니, 그게 아니라."
    # SOURCE CH05 L2407
    sia "진짜로 사람들이 여기 와서 놀 거 아니야."
    $ story_stage(faces={"roman": "happy"})
    # SOURCE CH05 L2410
    roman "앗,,, 그러게요……!"
    $ story_stage(faces={"darim": "happy"})
    # SOURCE CH05 L2413
    darim "후후. 이제 실감이 나네요."
    # SOURCE CH05 L2416
    lumi "저도요."
    # SOURCE CH05 L2419
    lumi "모형으로만 보다가 실제로 보니까 조금 다르네요."
    # SOURCE CH05 L2422
    mc "선배가 설계하신 대로 잘 만들어지고 있네요."
    $ story_stage(faces={"lumi": "smug"})
    # SOURCE CH05 L2425
    lumi "아직 끝난 건 아니니까요."
    $ story_stage(faces={"lumi": "happy"})
    # SOURCE CH05 L2429
    narrator "하린 선배는 그렇게 말했지만 조금 기분이 좋아 보였다."
    # SOURCE CH05 L2431 [SD EVENT] ch05_booth_install_01
    $ sd_event_start("ch05_booth_install_01")
    # SOURCE CH05 L2434
    sia "좋아! 그럼 마지막 설치 시작!"
    # SOURCE CH05 L2437
    omu "니는 일단 그 상자부터 들어라."
    # SOURCE CH05 L2440
    sia "나 감독인데?"
    $ story_stage(faces={"darim": "smug"})
    # SOURCE CH05 L2443
    darim "오늘은 감독도 상자를 들어야 해요."
    $ story_stage(faces={"sia": "embarrassed"})
    # SOURCE CH05 L2446
    sia "……아."
    # SOURCE CH05 L2449
    sia "노동의 현장이구나."
    # SOURCE CH05 L2452
    mc "저도 같이 옮길게요."
    # SOURCE CH05 L2455
    roman "앗,,, 저도 할 수 있어요!"
    $ story_stage(faces={"lumi": "serious"})
    # SOURCE CH05 L2458
    lumi "그럼 무거운 건 나눠서 들고, 작은 전시물부터 먼저 배치해요."
    # SOURCE CH05 L2460 [SD EVENT] ch05_booth_install_02
    $ sd_event_start("ch05_booth_install_02")
    # SOURCE CH05 L2464
    narrator "우리는 각자의 일을 시작했다."
    # SOURCE CH05 L2466
    narrator "다림 선배는 물품 목록을 확인했고, 하린 선배는 설치 위치를 조정했다."
    # SOURCE CH05 L2468
    narrator "로만은 질문 카드와 문장을 전시했고, 오므는 사진을 순서대로 배치했다."
    # SOURCE CH05 L2470
    narrator "시아는 안내 만화를 붙인 뒤 멀리서 전체 모습을 확인했다."
    # SOURCE CH05 L2472
    narrator "나도 부족한 물품을 옮기고, 안내판을 세우는 일을 도왔다."
    # SOURCE CH05 L2474 [시간 경과 · 오후 5:10]
    $ phone_timeline_cue("CH05", "CH05_L2474")
    # SOURCE CH05 L2477
    darim "이제 거의 끝났네요."
    $ story_stage(faces={"roman": "surprised"})
    # SOURCE CH05 L2480
    roman "앗,,, 생각보다 예뻐요……!"
    # SOURCE CH05 L2483
    omu "사진으로 찍어도 괜찮겠다."
    # SOURCE CH05 L2486
    sia "야, 잠깐."
    # SOURCE CH05 L2488
    sia "여기 내 만화 너무 잘 보이지 않냐?"
    $ story_stage(faces={"lumi": "smug"})
    # SOURCE CH05 L2491
    lumi "네. 안내판이니까 잘 보여야죠."
    # SOURCE CH05 L2494
    sia "아니, 그게 아니라."
    # SOURCE CH05 L2496
    sia "내 작품이 너무 뛰어나서."
    # SOURCE CH05 L2499
    omu "또 시작이네."
    # SOURCE CH05 L2502
    mc "그래도 실제로 보니까 잘 어울리네요."
    $ story_stage(faces={"sia": "happy"})
    # SOURCE CH05 L2505
    sia "그치?"
    # SOURCE CH05 L2508
    sia "역시 내 감상 담당."
    # SOURCE CH05 L2512
    narrator "나는 완성된 부스를 천천히 둘러봤다."
    # SOURCE CH05 L2514
    narrator "질문 카드가 놓인 테이블."
    # SOURCE CH05 L2516
    narrator "사진과 글이 걸린 전시 공간."
    # SOURCE CH05 L2518
    narrator "누구나 편하게 둘러볼 수 있도록 비워둔 통로."
    # SOURCE CH05 L2520
    narrator "처음 회의에서 상상했던 것보다 훨씬 그럴듯했다."
    # SOURCE CH05 L2523
    mc "……정말 완성됐네요."
    $ story_stage(faces={"darim": "happy", "roman": "happy", "omu": "happy", "lumi": "happy"})
    # SOURCE CH05 L2526
    darim "그러네요."
    # SOURCE CH05 L2529
    roman "조금 신기해요……."
    # SOURCE CH05 L2532
    omu "그때 우리가 이런 거 만들 줄 알았나."
    # SOURCE CH05 L2535
    lumi "후후. 그때는 회의만 제대로 끝나도 다행이었죠."
    $ story_stage(faces={"sia": "surprised"})
    # SOURCE CH05 L2538
    sia "야, 그렇게까지 심각했냐?"
    # SOURCE CH05 L2541
    omu "니가 제일 심각했지."
    $ story_stage(faces={"sia": "angry"})
    # SOURCE CH05 L2544
    sia "아니거든?"
    # SOURCE CH05 L2546 [SFX] 옆 부스에서 들리는 소란
    $ story_stage(cast=STORY_HEROES + ["ski", "hyeophap", "hess", "bambam"], faces={"ski": "confused", "hyeophap": "serious"})
    # SOURCE CH05 L2549
    ski "야! 그거 거기 아니야!"
    # SOURCE CH05 L2552
    hyeophap "스키, 네가 아까 저기 두라고 했잖아."
    $ story_stage(faces={"ski": "confused"})
    # SOURCE CH05 L2555
    ski "……그랬나?"
    # SOURCE CH05 L2558
    hess "네."
    # SOURCE CH05 L2561
    bambam "저도 들었어요."
    $ story_stage(faces={"ski": "embarrassed"})
    # SOURCE CH05 L2564
    ski "아, 내 완벽한 기억력에 이런 일이……."
    $ story_stage(faces={"hyeophap": "serious"})
    # SOURCE CH05 L2567
    hyeophap "완벽하다는 말부터 다시 생각해."
    # SOURCE CH05 L2569 [SD EVENT] ch05_rival_install_comedy
    $ sd_event_start("ch05_rival_install_comedy")
    # SOURCE CH05 L2573
    narrator "우리는 동시에 옆 부스를 바라봤다."
    # SOURCE CH05 L2576
    sia "……쟤네도 똑같네."
    # SOURCE CH05 L2579
    omu "우리랑 뭐가 다르겠노."
    # SOURCE CH05 L2582
    ski "야! 들리거든?"
    $ story_stage(faces={"sia": "smug"})
    # SOURCE CH05 L2585
    sia "들으라고 한 건데?"
    # SOURCE CH05 L2588
    hyeophap "시아, 신경 쓰지 말고 너희 설치 마무리해."
    $ story_stage(faces={"darim": "happy"})
    # SOURCE CH05 L2591
    darim "네. 그쪽도 수고 많으세요."
    # SOURCE CH05 L2594
    bambam "내일 봬요."
    # SOURCE CH05 L2597
    hess "내일은 통로 안 막히게 해요."
    # SOURCE CH05 L2600
    lumi "네. 그 부분은 저희도 확인했어요."
    # SOURCE CH05 L2604
    narrator "잠시 뒤 협합이 우리 부스 앞에 섰다."
    $ story_stage(faces={"hyeophap": "serious"})
    # SOURCE CH05 L2607
    hyeophap "아까 동선 확인하다 봤는데."
    # SOURCE CH05 L2609
    hyeophap "여기 안내판은 조금 더 안쪽에 놓는 게 좋겠어."
    $ story_stage(faces={"lumi": "serious"})
    # SOURCE CH05 L2612
    lumi "아, 통로 때문에요?"
    # SOURCE CH05 L2615
    hyeophap "응. 내일 사람 많아지면 서로 부딪힐 수 있으니까."
    # SOURCE CH05 L2618
    darim "좋은 의견이네요."
    # SOURCE CH05 L2621
    mc "그럼 같이 조금 옮길까요?"
    # SOURCE CH05 L2624
    hyeophap "그래."
    # SOURCE CH05 L2628
    narrator "우리와 협합은 안내판을 조금 옮겼다."
    # SOURCE CH05 L2630
    narrator "스키도 옆에서 상자를 들어줬다."
    $ story_stage(faces={"ski": "happy"})
    # SOURCE CH05 L2633
    ski "자, 됐지?"
    $ story_stage(faces={"sia": "smug"})
    # SOURCE CH05 L2636
    sia "오, 오늘은 일도 하네."
    # SOURCE CH05 L2639
    ski "야, 나 원래 일 잘하거든."
    # SOURCE CH05 L2642
    hyeophap "그건 맞아."
    $ story_stage(faces={"ski": "surprised"})
    # SOURCE CH05 L2645
    ski "……!"
    $ story_effect("bounce", "ski")
    $ story_icon("ski", "exclamation")
    # SOURCE CH05 L2648
    ski "협합이 나 칭찬했다!"
    $ story_stage(faces={"hyeophap": "smug"})
    # SOURCE CH05 L2651
    hyeophap "칭찬 취소."
    $ story_stage(faces={"ski": "surprised"})
    # SOURCE CH05 L2654
    ski "왜!"
    # SOURCE CH05 L2656 [SD EVENT] ch05_joint_install_final
    # SOURCE CH05 L2660
    narrator "또 웃음이 퍼졌다."
    # SOURCE CH05 L2662
    narrator "처음에는 경쟁하는 사이였는데."
    # SOURCE CH05 L2664
    narrator "이제는 서로의 부스를 도와주고 있었다."
    $ story_stage(cast=STORY_HEROES)
    # SOURCE CH05 L2666
    narrator "그것도 조금 신기했다."
    # SOURCE CH05 L2668 [시간 경과 · 오후 6:20]
    $ phone_timeline_cue("CH05", "CH05_L2668")
    # 설치 컷 3장은 연속 유지하고, 노을 배경으로 바뀔 때 명시적으로 스탠딩에 복귀한다.
    $ sd_event_end(restore=False, transition=0)
    # SOURCE CH05 L2670 [BG] 완성된 축제 부스 · 노을
    $ story_scene("booth", cast=STORY_HEROES, light="evening", location="완성된 축제 부스 · 노을")
    # SOURCE CH05 L2672 [BGM] Warm Memories
    $ play_bgm("evening_warm")
    # SOURCE CH05 L2676
    narrator "설치가 모두 끝났다."
    # SOURCE CH05 L2678
    narrator "우리 부스에는 전시할 사진과 글이 걸렸고, 작은 안내 카드까지 제자리를 찾았다."
    # SOURCE CH05 L2680
    narrator "뒤돌아보니 다섯 명이 나란히 서 있었다."
    $ story_stage(faces={"darim": "happy", "roman": "happy", "omu": "happy", "lumi": "happy", "sia": "happy"})
    # SOURCE CH05 L2683
    darim "……다들 정말 고생 많으셨어요."
    # SOURCE CH05 L2686
    roman "앗,,, 저도 이렇게 될 줄은 몰랐어요."
    # SOURCE CH05 L2689
    omu "내도."
    # SOURCE CH05 L2692
    sia "야, 우리 좀 멋있지 않냐?"
    $ story_stage(faces={"lumi": "smug"})
    # SOURCE CH05 L2695
    lumi "조금요?"
    $ story_stage(faces={"sia": "angry"})
    # SOURCE CH05 L2698
    sia "아, 그냥 멋있다고 해줘!"
    # SOURCE CH05 L2701
    mc "저는 정말 멋있다고 생각해요."
    $ story_stage(faces={"sia": "embarrassed"})
    # SOURCE CH05 L2704
    sia "……."
    # SOURCE CH05 L2707
    sia "뭐야."
    # SOURCE CH05 L2709
    sia "갑자기 그렇게 진지하게 말하면."
    # SOURCE CH05 L2712
    mc "진심인데요."
    # SOURCE CH05 L2716
    narrator "시아는 잠시 말이 없었다."
    # SOURCE CH05 L2718
    narrator "그러다 어깨를 으쓱했다."
    # SOURCE CH05 L2721
    sia "……알았어."
    # SOURCE CH05 L2723
    sia "그럼 인정."
    # SOURCE CH05 L2726
    darim "후후. 저도 모두가 자랑스러워요."
    # SOURCE CH05 L2729
    omu "와, 선배 그렇게 말하니까 좀 뭉클한데."
    # SOURCE CH05 L2732
    roman "……저도요."
    # SOURCE CH05 L2735
    lumi "아직 축제 시작도 안 했잖아요."
    # SOURCE CH05 L2738
    lumi "감동은 내일 아껴둬요."
    # SOURCE CH05 L2742
    narrator "하린 선배는 웃으며 말했다."
    # SOURCE CH05 L2744
    narrator "그러나 그 목소리에도 조금은 아쉬운 마음이 묻어 있었다."
    # SOURCE CH05 L2746 [UI] 사진 촬영 연출
    # SOURCE CH05 L2749
    omu "야, 다들 잠깐 모여봐라."
    $ story_stage(faces={"sia": "confused"})
    # SOURCE CH05 L2752
    sia "왜?"
    # SOURCE CH05 L2755
    omu "사진 하나 찍자."
    # SOURCE CH05 L2758
    darim "좋아요."
    $ story_stage(faces={"roman": "embarrassed"})
    # SOURCE CH05 L2761
    roman "앗,,, 저도 같이 찍어도 되나요?"
    # SOURCE CH05 L2764
    omu "당연하지."
    # SOURCE CH05 L2767
    mc "저도 같이 있어도 될까요?"
    # SOURCE CH05 L2770
    omu "니는 당연히 있어야지."
    $ story_stage(faces={"sia": "happy"})
    # SOURCE CH05 L2773
    sia "야, [player_name] 빠지면 안 되지."
    $ story_stage(faces={"lumi": "happy"})
    # SOURCE CH05 L2776
    lumi "처음부터 같이 준비했잖아요."
    # SOURCE CH05 L2780
    narrator "나는 모두와 함께 자리를 잡았다."
    # SOURCE CH05 L2782
    narrator "오므가 카메라를 설치하고 타이머를 맞췄다."
    $ story_stage(faces={"omu": "happy"})
    # SOURCE CH05 L2785
    omu "자, 찍는다."
    # SOURCE CH05 L2788
    sia "야, 스키 표정 따라 해볼까?"
    $ story_stage(faces={"darim": "serious"})
    # SOURCE CH05 L2791
    darim "시아 씨, 제발 그냥 찍어요."
    # SOURCE CH05 L2794
    lumi "후후. 그러다 또 이상하게 나오겠네요."
    $ story_stage(faces={"roman": "happy"})
    # SOURCE CH05 L2797
    roman "앗,,, 저 준비됐어요……!"
    # SOURCE CH05 L2800
    omu "하나, 둘……."
    $ story_sfx("shutter")
    # SOURCE CH05 L2802 [SFX] 카메라 셔터
    # SOURCE CH05 L2804 [CG EVENT] ch05_team_memory_photo
    $ cg_start("ch05_team_memory_photo")
    # SOURCE CH05 L2806 [연출] 주인공 외형을 직접 보여주지 않는 구도 사용. 단체 사진의 구체적인 구성은 아트 제작 단계에서 결정.
    # SOURCE CH05 L2810
    narrator "찰칵."
    # SOURCE CH05 L2812
    narrator "짧은 소리가 났다."
    # SOURCE CH05 L2814
    narrator "오므는 화면을 확인했다."
    $ cg_end()
    # SOURCE CH05 L2817
    omu "……오."
    # SOURCE CH05 L2819
    omu "잘 나왔네."
    $ story_stage(faces={"sia": "surprised"})
    # SOURCE CH05 L2822
    sia "보여줘!"
    # SOURCE CH05 L2825
    darim "저도 볼래요."
    # SOURCE CH05 L2828
    roman "앗,,, 저도요……!"
    $ story_stage(faces={"lumi": "happy"})
    # SOURCE CH05 L2831
    lumi "후후. 다들 표정이 재미있네요."
    # SOURCE CH05 L2835
    narrator "사진 속에서 모두 웃고 있었다."
    # SOURCE CH05 L2837
    narrator "완벽하게 정돈된 사진은 아니었다."
    # SOURCE CH05 L2839
    narrator "누군가는 웃다가 눈을 감았고, 누군가는 옆을 바라보고 있었다."
    # SOURCE CH05 L2841
    narrator "그래도 마음에 들었다."
    # SOURCE CH05 L2844
    mc "……좋네."
    # SOURCE CH05 L2848
    narrator "내일이면 이곳에 사람들이 찾아올 것이다."
    # SOURCE CH05 L2850
    narrator "그리고 얼마 지나지 않아 축제도 끝나겠지."
    # SOURCE CH05 L2852
    narrator "하지만 적어도 이 순간만큼은 오래 기억하고 싶었다."
    # SOURCE CH05 L2854 [FLAG] ch05_booth_install_complete = True
    $ story_flag("ch05_booth_install_complete")
    # SOURCE CH05 L2856 [FLAG] ch05_group_photo_taken = True
    $ story_flag("ch05_group_photo_taken")
    # SOURCE CH05 L2858 [SCENE 08 END]
    jump ch05_sc09

# SOURCE CH05 L2864 SCENE 09. 내일이면 정말 축제다
# SOURCE CH05 L2865 오후 11:30 · 주인공 방 · CH05 마지막 장면
# SOURCE CH05 L2866 SC09 · 내일이면 정말 축제다
label ch05_sc09:
    $ phone_timeline_enter("CH05", "ch05_sc09")
    # SOURCE CH05 L2867 [BG] 주인공 방 · 밤
    $ story_scene("room", cast=[], standing=False, light="night", location="주인공 방 · 밤")
    # SOURCE CH05 L2869 [BGM] Night Campus
    $ play_bgm("night_campus")
    # SOURCE CH05 L2871 [FADE IN]
    # SOURCE CH05 L2875
    narrator "방에 돌아오니 몸이 조금 무거웠다."
    # SOURCE CH05 L2877
    narrator "며칠 동안 계속 부스 준비를 했으니 당연했다."
    # SOURCE CH05 L2879
    narrator "그래도 오늘은 기분이 나쁘지 않았다."
    # SOURCE CH05 L2881
    narrator "침대에 누워 휴대전화를 열었다."
    # SOURCE CH05 L2883 [UI] 갤러리 · 오늘의 사진
    # SOURCE CH05 L2887
    narrator "오므가 조금 전 공유한 단체 사진이 있었다."
    # SOURCE CH05 L2889
    narrator "시아는 웃고 있었고, 다림 선배는 작은 미소를 짓고 있었다."
    # SOURCE CH05 L2891
    narrator "로만은 손을 모은 채 카메라를 바라봤고, 하린 선배는 평소처럼 여유롭게 웃고 있었다."
    # SOURCE CH05 L2893
    narrator "……그러고 보니 이 사람들이랑 참 많은 일을 했다."
    # SOURCE CH05 L2895
    narrator "처음에는 같이 축제를 준비한다는 것 말고는 공통점도 별로 없었는데."
    # SOURCE CH05 L2897
    narrator "이제는 각자의 목소리와 표정이 익숙하다."
    # SOURCE CH05 L2899 [SFX] 스마트폰 알림
    # SOURCE CH05 L2901 [UI] 축제 준비팀 (6)
    $ story_chat(True, title="축제 준비팀")
    $ phone_clock = "23:30"
    $ phone_date = "축제 전날"
    # SOURCE CH05 L2904
    darim "다들 오늘 정말 고생 많으셨어요."
    # SOURCE CH05 L2906
    darim "내일 오전에는 조금 일찍 모여서 마지막 점검만 할게요."
    # SOURCE CH05 L2909
    sia "드디어 내일이다아아"
    # SOURCE CH05 L2912
    omu "니 오늘도 그 말 열 번은 했다"
    # SOURCE CH05 L2915
    sia "열한 번 할 건데"
    # SOURCE CH05 L2918
    roman "앗,,, 저 벌써 조금 긴장돼요……!"
    # SOURCE CH05 L2921
    lumi "오늘은 너무 늦게까지 깨어 있지 마세요."
    # SOURCE CH05 L2924
    sia "너도 자라"
    # SOURCE CH05 L2927
    lumi "후후. 네."
    # SOURCE CH05 L2930
    darim "내일은 다들 즐겁게 해봐요."
    # SOURCE CH05 L2933
    mc "네. 다들 푹 쉬세요. 내일 봬요."
    # SOURCE CH05 L2937
    narrator "단체 채팅방에는 하나둘 잘 자라는 메시지가 올라왔다."
    $ story_chat(False)
    # SOURCE CH05 L2939
    narrator "나는 웃으며 화면을 닫았다."
    # SOURCE CH05 L2941
    narrator "그때 개인 메시지가 도착했다."
    # SOURCE CH05 L2943 [CONDITION] ch06_festival_partner에 해당하는 메시지만 출력
    # SOURCE CH05 L2945 로만과 축제를 구경하기로 한 경우
    if ch06_festival_partner == "roman":
        $ story_chat(True, title="로만")
        $ phone_clock = "23:30"
        $ phone_date = "축제 전날"
        # SOURCE CH05 L2947
        roman "앗,,, 혹시 아직 안 주무세요……?"
        # SOURCE CH05 L2950
        mc "네. 아직 안 자요. 무슨 일이세요?"
        # SOURCE CH05 L2953
        roman "그냥……."
        # SOURCE CH05 L2955
        roman "내일 같이 낭독 행사 보기로 한 거요."
        # SOURCE CH05 L2957
        roman "잊지 않으셨죠……?"
        # SOURCE CH05 L2960
        mc "그럼요. 기대하고 있어요."
        # SOURCE CH05 L2963
        roman "……후후."
        # SOURCE CH05 L2965
        roman "저도요."
        # SOURCE CH05 L2967
        roman "그럼 내일 뵐게요. 좋은 밤 보내세요……!"
        # SOURCE CH05 L2971
        narrator "로만은 약속을 다시 확인하고 싶었던 모양이다."
        # SOURCE CH05 L2973
        narrator "그런 작은 메시지가 조금 귀여웠다."
    # SOURCE CH05 L2975 시아와 축제를 구경하기로 한 경우
    elif ch06_festival_partner == "sia":
        $ story_chat(True, title="시아")
        $ phone_clock = "23:30"
        $ phone_date = "축제 전날"
        # SOURCE CH05 L2977
        sia "야"
        # SOURCE CH05 L2979
        sia "내일 꼭 와라"
        # SOURCE CH05 L2982
        mc "네. 시아 씨 작품 보러 갈게요."
        # SOURCE CH05 L2985
        sia "좋아"
        # SOURCE CH05 L2987
        sia "그리고 내일 내 작품 보고 엄청 놀라지 마"
        # SOURCE CH05 L2990
        mc "왜요? 무슨 비밀이라도 있나요?"
        # SOURCE CH05 L2993
        sia "비밀은 무슨ㅋㅋ"
        # SOURCE CH05 L2995
        sia "그냥 너무 잘 만들어서"
        # SOURCE CH05 L2998
        mc "그럼 기대를 많이 해도 되겠네요."
        # SOURCE CH05 L3001
        sia "……."
        # SOURCE CH05 L3003
        sia "야 그럼 나도 긴장되잖아"
        # SOURCE CH05 L3007
        narrator "시아가 긴장한다고 말하는 건 아직도 조금 의외다."
        # SOURCE CH05 L3009
        narrator "하지만 이제는 그 말이 농담만은 아니라는 걸 안다."
    # SOURCE CH05 L3011 다림과 축제를 구경하기로 한 경우
    elif ch06_festival_partner == "darim":
        $ story_chat(True, title="다림")
        $ phone_clock = "23:30"
        $ phone_date = "축제 전날"
        # SOURCE CH05 L3013
        darim "[player_name] 씨, 내일 게임 체험 부스도 잊지 않으셨죠?"
        # SOURCE CH05 L3016
        mc "네. 선배와의 승부를 기대하고 있어요."
        # SOURCE CH05 L3019
        darim "후후."
        # SOURCE CH05 L3021
        darim "그럼 준비 단단히 하고 오세요."
        # SOURCE CH05 L3024
        mc "선배야말로 방심하시면 안 돼요."
        # SOURCE CH05 L3027
        darim "어머. 벌써 그렇게 자신만만하시면 곤란한데요?"
        # SOURCE CH05 L3030
        darim "그럼 내일 봬요. 푹 쉬세요."
        # SOURCE CH05 L3034
        narrator "게임 하나를 두고 이렇게 진지하게 장난칠 수 있는 사람이었다니."
        # SOURCE CH05 L3036
        narrator "처음의 다림 선배를 떠올리면 조금 웃음이 났다."
    # SOURCE CH05 L3038 오므와 축제를 구경하기로 한 경우
    elif ch06_festival_partner == "omu":
        $ story_chat(True, title="오므")
        $ phone_clock = "23:30"
        $ phone_date = "축제 전날"
        # SOURCE CH05 L3040
        omu "야"
        # SOURCE CH05 L3042
        omu "내일 날씨 괜찮으면 해 질 때 사진 찍자"
        # SOURCE CH05 L3045
        mc "좋아요. 저도 기대하고 있어요."
        # SOURCE CH05 L3048
        omu "어"
        # SOURCE CH05 L3050
        omu "카메라 배터리도 다 충전했다"
        # SOURCE CH05 L3053
        mc "준비가 철저하시네요."
        # SOURCE CH05 L3056
        omu "중요한 날이니까"
        # SOURCE CH05 L3059
        mc "그렇죠. 내일 재미있게 보내요."
        # SOURCE CH05 L3062
        omu "어. 내일 보자"
        # SOURCE CH05 L3066
        narrator "중요한 날."
        # SOURCE CH05 L3068
        narrator "오므가 그런 표현을 쓰니까 조금 다르게 들렸다."
        # SOURCE CH05 L3070
        narrator "나도 내일이 중요하다고 생각하고 있었다."
    # SOURCE CH05 L3072 하린과 축제를 구경하기로 한 경우
    elif ch06_festival_partner == "lumi":
        $ story_chat(True, title="하린")
        $ phone_clock = "23:30"
        $ phone_date = "축제 전날"
        # SOURCE CH05 L3074
        lumi "내일 약속 기억하고 계시죠?"
        # SOURCE CH05 L3077
        mc "네. 완성된 부스 같이 보기로 했잖아요."
        # SOURCE CH05 L3080
        lumi "후후. 맞아요."
        # SOURCE CH05 L3082
        lumi "그런데 오늘 보니까 생각보다 잘 만들어졌더라고요."
        # SOURCE CH05 L3085
        mc "선배가 열심히 설계하셨으니까요."
        # SOURCE CH05 L3088
        lumi "……."
        # SOURCE CH05 L3090
        lumi "오늘은 그런 말씀 많이 하시네요."
        # SOURCE CH05 L3093
        mc "그냥 사실대로 말씀드리는 건데요."
        # SOURCE CH05 L3096
        lumi "……그러니까요."
        # SOURCE CH05 L3098
        lumi "아무튼 내일 봬요."
        # SOURCE CH05 L3102
        narrator "하린 선배는 마지막 메시지를 보낸 뒤 더 이상 말을 하지 않았다."
        # SOURCE CH05 L3104
        narrator "그런데 왠지 조금 부끄러워하는 모습이 떠올랐다."
    # SOURCE CH05 L3106 [공통 복귀]
    # SOURCE CH05 L3108 [UI] 스마트폰 화면 종료
    $ story_chat(False)
    # SOURCE CH05 L3112
    narrator "휴대전화를 내려놓았다."
    # SOURCE CH05 L3114
    narrator "내일이면 축제가 시작된다."
    # SOURCE CH05 L3116
    narrator "수많은 사람들이 캠퍼스로 찾아오고, 우리가 만든 부스에도 방문객이 올 것이다."
    # SOURCE CH05 L3118
    narrator "처음에는 잘할 수 있을지 걱정했다."
    # SOURCE CH05 L3120
    narrator "서로 다른 사람들이 모여서 정말 하나의 결과물을 만들 수 있을까 싶었다."
    # SOURCE CH05 L3122
    narrator "그런데 이제는 그 답을 조금 알 것 같다."
    # SOURCE CH05 L3124
    narrator "완벽하지 않아도 괜찮았다."
    # SOURCE CH05 L3126
    narrator "의견이 다를 때도 있었고, 실수도 했고, 마음이 상한 적도 있었다."
    # SOURCE CH05 L3128
    narrator "그래도 이야기하면서 하나씩 해결해 왔다."
    # SOURCE CH05 L3130
    narrator "그리고 그 과정에서……"
    # SOURCE CH05 L3132
    narrator "나는 이 사람들을 조금씩 좋아하게 된 것 같다."
    # SOURCE CH05 L3135
    mc "……좋아한다라."
    # SOURCE CH05 L3139
    narrator "그냥 친구로서 좋아하는 걸까."
    # SOURCE CH05 L3141
    narrator "아니면 조금 다른 의미일까."
    # SOURCE CH05 L3143
    narrator "아직은 모르겠다."
    # SOURCE CH05 L3145
    narrator "하지만 한 가지는 분명하다."
    # SOURCE CH05 L3147
    narrator "내일이 기다려진다."
    # SOURCE CH05 L3149
    narrator "축제 때문이기도 하고."
    # SOURCE CH05 L3151
    narrator "누군가와 함께 시간을 보낼 수 있기 때문이기도 하다."
    # SOURCE CH05 L3153 [SFX] 스마트폰 화면 켜지는 소리
    # SOURCE CH05 L3155 [UI] 오늘 촬영한 단체 사진
    # SOURCE CH05 L3159
    narrator "나는 사진을 한 번 더 바라봤다."
    # SOURCE CH05 L3161
    narrator "처음의 우리는 모두 조금 어색했다."
    # SOURCE CH05 L3163
    narrator "이제는 한 사진 안에서 자연스럽게 웃고 있다."
    # SOURCE CH05 L3165
    narrator "문득 생각했다."
    # SOURCE CH05 L3167
    narrator "축제가 끝나도."
    # SOURCE CH05 L3169
    narrator "우리는 이렇게 만날 수 있을까."
    # SOURCE CH05 L3172
    mc "……끝나고도 또 만나면 되지."
    # SOURCE CH05 L3176
    narrator "그런데 그건 누가 먼저 말해야 하는 걸까."
    # SOURCE CH05 L3178
    narrator "……뭐."
    # SOURCE CH05 L3180
    narrator "그건 축제가 끝난 뒤에 생각하자."
    # SOURCE CH05 L3182
    narrator "지금은 내일을 즐길 차례다."
    # SOURCE CH05 L3184 [BGM] 천천히 고조
    $ play_bgm("chapter_ending_reprise")
    # SOURCE CH05 L3186 [FADE TO BLACK]
    $ story_fade_out()
    scene expression Solid("#080d16") with fade
    # SOURCE CH05 L3188
    narrator "「CHAPTER 05 COMPLETE」"
    # SOURCE CH05 L3190
    narrator "「다음 이야기」"
    # SOURCE CH05 L3192
    narrator "「오늘만큼은, 조금 특별하게」"
    # SOURCE CH05 L3194 [FLAG] chapter05_complete = True
    # SOURCE CH05 L3196 [NEXT] CHAPTER 06 · 축제 당일과 프로젝트 마무리
    # SOURCE CH05 L3198 [SCENE 09 END]
    $ story_complete_chapter(5)
    jump chapter06
