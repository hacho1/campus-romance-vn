# -*- coding: utf-8 -*-
# Official CH02, converted without dialogue rewriting.
# Source: ch2 스토리.txt; source comments use original one-based line numbers.


label chapter02:
    $ phone_timeline_enter("CH02", "chapter02")
    $ story_begin_chapter(2, "우리 옆 부스가 수상하다")
    # source L2
    narrator "세상에는 두 종류의 사람이 있다. 자신감이 넘치는 사람과, 그 자신감이 왜 넘치는지 도저히 이해할 수 없는 사람."
    jump ch02_sc01

label ch02_sc01:
    $ phone_timeline_enter("CH02", "ch02_sc01")
    # source L20: **[BG] 주인공 방 · 아침**
    $ story_scene("room", mode="normal", cast=[], light="day", location="주인공 방 · 아침")
    # source L22: **[BGM] Daily Campus**
    $ play_bgm("campus_day")
    # 장소 전환은 story_scene에서 처리합니다.

    # source L28
    narrator "아침이다."
    # source L30
    narrator "정확히 말하자면, 아무런 일정도 없는 아침이어야 했다."
    # source L32
    narrator "오늘은 강의가 없는 날."
    # source L34
    narrator "어제까지만 해도 오랜만에 늦잠을 잘 수 있다는 사실에 제법 기분이 좋았다."
    # source L36: **[SFX] 휴대전화 진동**
    $ story_sfx("message")
    # source L40
    mc "……."
    # source L42: **[SFX] 연속 메시지 알림**
    # 두 번째 알림음은 휴대폰 이벤트 시작에 재생.
    # source L46
    mc "……누구야."
    # source L48: **[UI] 스마트폰 화면**
    $ story_chat(True, title="축제 준비팀")
    # source L50
    system_note "「축제 준비팀」"
    # source L54
    sia "야 다들 일어났냐"
    # source L56
    sia "일어났으면 대답해라"
    # source L58
    sia "아니 읽었으면 대답을 해야지ㅋㅋ"
    # source L62
    omu "니는 아침부터 와 이래 시끄럽노"
    # source L66
    sia "지금 9시인데?"
    # source L70
    omu "내 기준으론 새벽이다"
    # source L74
    darim "다들 좋은 아침이에요."
    # source L76
    darim "오늘 공지 확인하셔야 해요."
    # source L80
    roman "앗,,, 좋은 아침이에요……!"
    # source L84
    lumi "좋은 아침. 저는 작업실 가는 중이에요."
    # source L88
    sia "하린아 너는 아침부터 부지런하네"
    # source L92
    lumi "시아 씨는 아침부터 채팅할 힘이 넘치시네요."
    # source L96
    sia "응 아니야~ 사실 누워있음"
    # source L100
    omu "그럴 줄 알았다"
    $ story_chat(False)
    # source L104
    narrator "나는 휴대전화를 내려놓았다."
    # source L106
    narrator "그리고 이불을 다시 덮었다."
    # source L108: **[SFX] 개인 메시지 알림**
    # 알림음은 휴대폰 이벤트 시작에 재생.
    # source L112
    mc "……."
    # source L114
    mc "제발."
    if first_task_partner == "roman":
        $ story_chat(True, title="로만")
        # source L122
        roman "앗,,, [player_name] 씨……."
        # source L124
        roman "어제 같이 찾아본 문구를 조금 수정해 봤어요."
        # source L126
        roman "혹시 오늘 시간 괜찮으시면 보여드려도 될까요……?"
        $ story_chat(False)
    elif first_task_partner == "sia":
        $ story_chat(True, title="시아")
        # source L132
        sia "야ㅋㅋ 어제 그린 콘티 수정함"
        # source L134
        sia "너한테 제일 먼저 보여줄게"
        # source L136
        sia "아 그리고 오늘 늦으면 안 됨"
        # source L138
        sia "내가 늦는 건 괜찮고"
        $ story_chat(False)
    elif first_task_partner == "darim":
        $ story_chat(True, title="다림")
        # source L144
        darim "좋은 아침이에요."
        # source L146
        darim "어제 정리한 일정표에 변경 사항이 생겼어요."
        # source L148
        darim "오늘 회의에서 같이 확인해 주실 수 있을까요?"
        $ story_chat(False)
    elif first_task_partner == "omu":
        $ story_chat(True, title="오므")
        # source L154
        omu "니 오늘 학교 오나?"
        # source L156
        omu "어제 사진 정리하다가 쓸 만한 거 찾았다"
        # source L158
        omu "오면 보여줄게"
        $ story_chat(False)
    elif first_task_partner in ("lumi", "rumi"):
        $ story_chat(True, title="하린")
        # source L164
        lumi "어제 공간 배치도를 다시 봤는데요."
        # source L166
        lumi "수정할 부분이 좀 생겼어요."
        # source L168
        lumi "오늘 시간 되면 같이 확인해 줄래?"
        $ story_chat(False)
    # source L170: **[공통 복귀]**
    # source L174
    narrator "그래."
    # source L176
    narrator "내 공강은 어제 끝났구나."
    # source L180
    mc "……대학생활이 이렇게 부지런한 거였나."
    # source L182: **[SFX] 새로운 공지 알림**
    # 알림음은 휴대폰 이벤트 시작에 재생.
    $ story_chat(True, title="축제 운영위원회")  # source L184
    system_note "「축제 운영위원회」"
    # source L186
    narrator "축제 부스 공간 재배정 안내"
    # source L188
    narrator "동일 구역을 신청한 팀이 확인되어 기획 평가를 진행할 예정입니다."
    # source L190
    narrator "참가팀은 오전 11시까지 학생회관 안내 게시판의 세부 공지를 확인해 주시기 바랍니다."
    $ story_chat(False)  # source L194
    mc "동일 구역 신청 팀……."
    # source L198
    narrator "어제 마지막에 봤던 공지와 같은 내용이었다."
    # source L200
    narrator "설마 경쟁이라도 해야 한다는 걸까."
    # source L204
    mc "……일단 가보자."
    # source L206: **[FADE OUT]**
    # 다음 장소로 바로 연결합니다.
    # 이전 장면이 왼쪽으로 밀립니다.

    # source L208: **[SCENE 01 END]**
    jump ch02_sc02

label ch02_sc02:
    $ phone_timeline_enter("CH02", "ch02_sc02")
    # source L212: **[BG] 학생회관 복도 · 낮**
    $ story_scene("corridor", mode="normal", cast=['roman', 'sia', 'darim', 'omu', 'lumi'], light="day", location="학생회관 복도 · 낮")
    # source L214: **[BGM] Daily Campus**
    $ play_bgm("campus_day")
    # source L218
    narrator "학생회관에 도착했을 때는 이미 몇몇 팀원이 게시판 앞에 모여 있었다."
    # source L222
    sia "아니, 그러니까 우리 자리 뺏긴 거냐고!"
    # source L226
    darim "아직 뺏긴 건 아니라니까요."
    # source L230
    sia "근데 왜 발표를 또 해야 하는데!"
    # source L234
    omu "니 일단 공지 좀 읽어봐라."
    # source L238
    sia "읽었어!"
    # source L242
    omu "그럼 이해를 해라."
    # source L246
    sia "아."
    # source L248
    sia "그건 좀 어려운데."
    # source L252
    mc "무슨 일이에요?"
    # source L256
    roman "앗,,, 오셨어요……!"
    # source L260
    darim "공지 내용이 조금 복잡해서 설명해 드릴게요."
    # source L264
    narrator "게시판에는 새로운 안내문이 붙어 있었다."
    # source L266
    system_note "「축제 인기 구역 중복 신청에 따른 우선 배정 심사」"
    # source L268
    system_note "「동일 구역 신청 팀은 중간 기획 발표 및 시범 운영 평가를 진행합니다.」"
    # source L270
    system_note "「최종 우선 배정 결과는 평가 완료 후 발표됩니다.」"
    # source L274
    mc "……그럼 우리가 신청한 구역에 다른 팀도 신청한 거예요?"
    # source L278
    darim "네. 그래서 누가 우선 배정을 받을지 평가한다고 하네요."
    # source L282
    lumi "공간도 줄었는데 경쟁까지 하게 됐네."
    $ story_stage(faces={"sia": "angry"})  # source L286
    sia "아니, 난 그냥 축제 준비하러 온 건데 왜 갑자기 오디션 프로그램이 됐냐고."
    # source L290
    omu "니가 발표 잘하면 되는 거 아인가."
    # source L294
    sia "그럼 나 1위 할 자신은 있음."
    # source L298
    lumi "벌써 우승 소감도 준비했어요?"
    # source L302
    sia "당연하지."
    # source L304
    sia "먼저 이 영광을 저 자신에게……."
    # source L308
    darim "아직 발표 일정도 안 나왔어요."
    # source L312
    sia "아, 분위기 좀 맞춰줘!"
    # source L316
    roman "앗,,, 그런데 경쟁팀은 어떤 분들이실까요……?"
    # source L320
    mc "그러게요. 어느 팀일까요?"
    # source L324
    narrator "그때 등 뒤에서 낯선 목소리가 들려왔다."
    # source L328
    unknown_voice "혹시 저희를 찾고 계신 건가요?"
    # source L330: **[BGM] 정지**
    stop music fadeout 0.5
    # source L334
    narrator "나는 뒤를 돌아봤다."
    # source L336
    narrator "네 사람이 서 있었다."
    # source L338
    narrator "그중 가장 앞에 있던 사람은 어째서인지 벌써부터 승리한 사람처럼 웃고 있었다."
    # source L340: **[SCENE 02 END]**
    jump ch02_sc03

label ch02_sc03:
    $ phone_timeline_enter("CH02", "ch02_sc03")
    # source L344: **[BG] 축제 준비실**
    $ story_scene("prep_room", mode="normal", cast=["sia", "omu"], light="day", location="축제 준비실")
    # source L346: **[BGM] Comedy Battle**
    $ play_bgm("rivalry_comedy")
    # 라이벌 팀원은 첫 대사 직전에 한 명씩 들어옵니다.
    $ story_enter("ski", side="right", face="happy")
    # source L352
    ski "반가워, 다들!"
    # source L354
    ski "이번 축제에서 가장 주목받을 팀의 핵심 인물, 스키야!"
    # source L358
    narrator "……자기소개가 조금 길다."
    # source L362
    sia "……누구?"
    # source L366
    ski "스키라고 해."
    # source L370
    sia "아니, 이름 말고."
    # source L372
    sia "왜 혼자 시상식 수상 소감 하는 사람처럼 말하냐고."
    # source L376
    ski "아, 내 자신감에 놀랐구나."
    # source L380
    sia "응 아니야~"
    # source L384
    ski "부끄러워할 거 없어."
    # source L388
    sia "뭐래ㅋㅋㅋㅋ"
    # source L392
    omu "와, 저 사람 자신감 장난 아니네."
    # source L396
    ski "고마워. 내 장점 중 하나야."
    # source L400
    omu "칭찬 아닌데."
    # source L404
    ski "칭찬으로 받아들일게."
    # source L408
    narrator "엄청난 사람이다."
    # source L410
    narrator "다른 사람이 하는 말을 전부 자기에게 유리하게 해석하고 있다."
    $ story_enter("hyeophap", side="right", face="serious")  # source L414
    hyeophap "스키, 인사 끝났으면 옆으로 좀 비켜."
    # source L418
    ski "협합, 지금 중요한 첫인상 만드는 중인데?"
    # source L422
    hyeophap "첫인상은 이미 충분해."
    # source L426
    ski "좋은 쪽으로?"
    # source L430
    hyeophap "기억에는 남겠네."
    # source L434
    ski "역시!"
    # source L438
    hyeophap "좋다는 뜻은 아니야."
    # 상대 팀이 처음 만나는 장면은 스탠딩을 유지합니다.
    $ story_stage(faces={"ski": "embarrassed"})
    # source L444
    sia "푸하하하!"
    # source L448
    ski "……전략적으로 넘어갈게."
    # source L452
    narrator "두 번째로 말을 건 사람은 협합이라고 자신을 소개했다."
    # source L454
    narrator "스키와 같은 제과제빵과 3학년이며, 같은 제과제빵 동아리 소속이라고 했다."
    # source L458
    hyeophap "우리는 축제 체험 부스를 준비하고 있어."
    # source L460
    hyeophap "같은 구역을 신청했다고 들었는데, 서로 잘 준비해 보자."
    # source L464
    darim "네. 저희도 잘 부탁드려요."
    # source L468
    ski "물론 승리는 우리가 가져가겠지만!"
    # source L472
    hyeophap "그건 아직 모르지."
    # source L476
    ski "왜 자꾸 내 기세를 꺾는 거야?"
    # source L480
    hyeophap "기세만으로 평가받는 게 아니니까."
    # source L484
    ski "……맞는 말이라 더 화나네."
    # source L488
    narrator "그 뒤에는 조금 조용해 보이는 두 사람이 있었다."
    $ story_enter("bambam", side="right", face="happy")  # source L492
    bambam "안녕하세요. 저는 밤밤이에요."
    # source L494
    bambam "심리학과 2학년이에요."
    # source L498
    narrator "밤밤은 눈을 가늘게 뜬 채 느긋하게 웃었다."
    # source L500
    narrator "처음에는 눈을 감고 있는 건가 싶었지만, 주변 상황을 꽤 잘 보고 있는 것 같았다."
    $ story_enter("hess", side="right", face="normal")  # source L504
    hess "헤스입니다."
    # source L506
    hess "심리학과 1학년이고요."
    # source L510
    narrator "……끝?"
    # source L514
    sia "끝이야?"
    # source L518
    hess "네."
    # source L522
    sia "뭔가 더 없어?"
    # source L526
    hess "뭐가요?"
    # source L530
    sia "취미라든가 각오라든가."
    # source L534
    hess "축제 준비 잘하겠습니다."
    # source L538
    sia "……."
    # source L542
    hess "이 정도면 됐나요?"
    # source L546
    bambam "헤스는 원래 말이 좀 짧아요."
    # source L550
    hess "필요한 말은 했잖아요."
    # source L554
    bambam "그렇긴 하지."
    # source L558
    roman "앗,,, 안녕하세요……."
    # source L562
    hess "안녕하세요."
    # source L566
    roman "……."
    # source L570
    hess "……."
    # source L572: **[SD] 두 사람 사이에 정적을 표현하는 점 세 개가 떠오른다.**
    # source L576
    sia "야, 둘 다 왜 멈췄어ㅋㅋㅋ"
    # source L580
    roman "앗,,, 아니에요……!"
    # source L584
    hess "인사는 끝났으니까요."
    # source L588
    omu "맞는 말이긴 하네."
    # source L592
    lumi "독특한 팀이네요."
    # source L596
    hyeophap "우리도 그렇게 생각해."
    # source L600
    ski "물론 내 매력이 제일 큰 비중을 차지하겠지만!"
    # source L604
    hyeophap "그건 아닐 거야."
    # source L608
    ski "잠깐만. 이번엔 이유라도……."
    # source L612
    hyeophap "설명할 시간이 아까워."
    # source L614: 스키의 당황한 표정과 시아의 웃음.
    $ story_stage(faces={"ski": "embarrassed", "sia": "happy"})
    # source L618
    narrator "어제까지만 해도 우리 팀이 가장 시끄러운 조합이라고 생각했다."
    # source L620
    narrator "……착각이었다."
    $ story_stage(mode="normal")  # 예전 저장에서 남아 있는 SD 연출도 여기서 닫습니다.

    menu:
        # source L624
        "그 자신감이면 부스도 혼자 만들겠네요.":
            # source L634
            mc "그 자신감이면 부스도 혼자 만들겠네요."
            # source L638
            ski "오, 좋은 아이디어네!"
            # source L642
            ski "하지만 내 재능을 독점하면 다른 팀원들이 서운해하지 않겠어?"
            # source L646
            sia "아, 너 진짜 웃기다ㅋㅋㅋ"
            # source L650
            hyeophap "혼자 하라고 하면 10분 만에 도움 요청할 사람이야."
            # source L654
            ski "……30분은 버틸 수 있어."
            # source L658
            sia "인정은 하네?"
            # source L660: **[FLAG] affection.sia +1, rival_attitude = playful**
            $ story_apply("ch02_sc03_a", affection={'sia': 1}, values={'rival_attitude': 'playful'})
        # source L626
        "서로 열심히 준비해 봐요.":
            # source L666
            mc "서로 열심히 준비해 봐요."
            # source L670
            hyeophap "좋은 생각이야."
            # source L672
            hyeophap "경쟁하는 건 맞지만 불필요하게 감정 상할 이유는 없으니까."
            # source L676
            darim "저도 그렇게 생각해요."
            # source L680
            ski "정정당당한 승부, 아주 좋아!"
            # source L684
            ski "물론 내가 이기는 것도 정정당당한 결과겠지."
            # source L688
            hess "아직 시작도 안 했는데요."
            # source L690: **[FLAG] trust.darim +1, rival_attitude = respectful**
            $ story_apply("ch02_sc03_b", trust={'darim': 1}, values={'rival_attitude': 'respectful'})
        # source L628
        "어떤 부스를 준비하고 있어요?":
            # source L696
            mc "어떤 부스를 준비하고 있어요?"
            # source L700
            hess "간단한 질문을 통해 기분에 맞는 디저트를 고르는 부스예요."
            # source L704
            bambam "너무 어렵지 않게 만들고 있어요."
            # source L708
            ski "그리고 그 디저트는 바로 이 천재적인 내가……."
            # source L712
            hyeophap "디저트는 같이 만드는 거지."
            # source L716
            ski "……내가 아주 중요한 역할을 맡아."
            # source L720
            lumi "그건 조금 기대되네요."
            # source L722: **[FLAG] rival_project_known = True**
            $ story_apply("ch02_sc03_c", values={'rival_project_known': True})
    # source L724: **[공통 복귀]**
    # source L728
    sia "근데 너희 네 명은 어떻게 모인 거야?"
    # source L732
    bambam "아, 그거요?"
    # source L736
    ski "내가 설명할게."
    # source L740
    hyeophap "짧게 해."
    # source L744
    ski "물론이지. 아주 감동적인 이야기야."
    # source L748
    hess "……감동적이었나요?"
    # source L752
    bambam "저는 재밌긴 했어요."
    # source L754: **[FADE TO WHITE]**
    # 회상 장소는 배경 슬라이드로 전환합니다.
    # source L756: **[SCENE 03 END]**
    jump ch02_sc04

label ch02_sc04:
    $ phone_timeline_enter("CH02", "ch02_sc04")
    # source L760: **[BG] 제과제빵 동아리실 · 회상**
    $ story_scene("clubroom", mode="normal", cast=['ski', 'hyeophap', 'hess', 'bambam'], light="day", location="제과제빵 동아리실 · 회상")
    $ story_flashback_set(True)
    # source L762: **[BGM] Mischief Comedy**
    $ play_bgm("comedy_light")
    # 면접 회상은 네 사람이 탁자 앞에 모인 컷 하나로 유지합니다.
    $ sd_event_start("ch02_interview_flashback", variant="02")
    # source L768
    narrator "스키의 설명에 따르면, 모든 일은 약 2주 전에 시작됐다고 한다."
    # source L770
    narrator "정확히는 스키가 자기 자신을 팀의 대표로 임명한 날이었다."
    # source L774
    ski "다들 들어봐. 난 이번 축제에서 역사에 남을 부스를 만들기로 했어."
    # source L778
    hyeophap "그러니까 팀원부터 모집하자고 했잖아."
    # source L782
    ski "물론이지."
    # source L784
    ski "그래서 내가 직접 모집 공고를 썼어."
    # source L786: **[UI] 당시 모집 공고 표시**
    # source L788
    system_note "「축제 체험 부스 팀원 모집」"
    # source L790
    system_note "「제과제빵과 × 심리학과 협업 프로젝트」"
    # source L792
    system_note "「모집 인원: 2명」"
    # source L794
    system_note "「조건: 일정 조율 가능, 공동 작업 참여 가능」"
    # source L798
    narrator "여기까지만 보면 평범한 모집 공고였다."
    # source L800
    narrator "문제는 스키가 그다음에 준비한 것이었다."
    # source L802: **[SFX] 종이 뭉치 내려놓는 소리**
    $ story_sfx("paper")
    # source L806
    ski "자, 지원자 평가표야."
    # source L810
    hyeophap "……이게 다 뭐야?"
    # source L814
    ski "면접 질문이야."
    # source L818
    hyeophap "지원자 두 명 뽑는데 질문이 스무 개나 필요해?"
    # source L822
    ski "인재를 뽑을 때는 신중해야 해."
    # source L826
    hyeophap "질문 마지막 항목이 '팀장의 매력에 대해 자유롭게 서술'인데?"
    # source L830
    ski "중요한 질문이야."
    # source L834
    hyeophap "삭제."
    # source L836: **[SD] 협합이 평가표에 커다란 X 표시**
    # source L840
    ski "아니, 잠깐만!"
    # source L842: **[SFX] 문 열리는 소리**
    $ story_sfx("door_open")
    # source L846
    bambam "안녕하세요. 여기 축제팀 모집하는 곳 맞나요?"
    # source L850
    hess "공고 보고 왔습니다."
    # source L854
    ski "드디어 왔구나!"
    # source L856
    ski "환영해. 앞으로 너희 역량을 평가할 면접관 스키야."
    # source L860
    hess "면접이요?"
    # source L864
    bambam "공고에는 없었는데요."
    # source L868
    ski "걱정 마. 어려운 질문은……."
    # source L872
    hyeophap "두 분 다 축제 기간 일정 괜찮으세요?"
    # source L876
    bambam "네. 미리 조정해 뒀어요."
    # source L880
    hess "저도 가능합니다."
    # source L884
    hyeophap "방문객 안내랑 체험 질문 제작에 참여할 수 있고요?"
    # source L888
    hess "네."
    # source L892
    bambam "저도요."
    # source L896
    hyeophap "그럼 두 분 다 합격이에요."
    # source L900
    ski "……."
    # 회상은 같은 SD 컷을 유지합니다.

    # source L906
    ski "잠깐만."
    # source L910
    hyeophap "왜?"
    # source L914
    ski "아직 면접 시작도 안 했는데?"
    # source L918
    hyeophap "지금 필요한 사항 확인했잖아."
    # source L922
    ski "지원 동기와 열정, 그리고 나에 대한 존경심을……."
    # source L926
    hess "존경심이 필수 조건인가요?"
    # source L930
    ski "그건……."
    # source L934
    bambam "공고에는 없던데."
    # source L938
    hyeophap "응. 없지."
    # source L942
    ski "……."
    # source L946
    hyeophap "모집 인원도 맞고, 역할도 맞고, 일정도 문제없어."
    # source L948
    hyeophap "더 확인할 이유가 있으면 말해봐."
    # source L952
    ski "내 면접 진행 실력을 보여줄 기회가……."
    # source L956
    hyeophap "그건 팀원 선발과 관계없어."
    # source L958: **[SD] 스키의 캐릭터가 점점 작아진다.**
    # source L962
    ski "……내 권위가 3초 만에 사라졌는데?"
    # source L966
    hess "원래 없던 것 아닌가요?"
    # source L970
    ski "……!"
    # source L974
    bambam "그래도 팀은 빨리 만들어졌네요."
    # source L978
    hyeophap "그러게. 잘 부탁해."
    # source L982
    hess "잘 부탁드립니다."
    # source L986
    bambam "저도요."
    # source L990
    ski "……."
    # source L994
    ski "좋아. 오늘은 특별히 내 넓은 아량으로 면접을 생략할게!"
    # source L998
    hyeophap "네가 생략한 게 아니잖아."
    # source L1002
    ski "그냥 그렇게 해줘!"
    $ sd_event_end(mode="normal", cast=[])
    # source L1004: **[FADE TO WHITE]**
    # 현재 장소로 슬라이드합니다.
    # source L1006: **[BG] 현재 · 축제 준비실**
    $ story_scene("prep_room", mode="normal", cast=['roman', 'sia', 'darim', 'omu', 'lumi', 'ski', 'hyeophap', 'hess', 'bambam'], light="day", location="현재 · 축제 준비실")
    $ story_flashback_set(False)
    # source L1008: **[BGM] Light Comedy**
    $ play_bgm("comedy_light")
    # source L1012
    sia "푸하하하하!"
    # source L1016
    sia "야, 너 면접관인데 면접을 못 봤어?"
    # source L1020
    ski "정확히는 효율적인 인재 선발을 위해 권한을 위임한 거야."
    # source L1024
    hyeophap "위임받은 적 없어."
    # source L1028
    omu "와, 끝까지 안 지네."
    # source L1032
    hess "저때 질문 스무 개 안 받아서 다행이었어요."
    # source L1036
    bambam "저는 조금 궁금하긴 했어요."
    # source L1040
    ski "봤지? 밤밤은 내 면접의 가치를 알아준다니까!"
    # source L1044
    bambam "아뇨. 어떤 이상한 질문이 나올지 궁금했어요."
    # source L1048
    ski "……."
    # source L1052
    lumi "팀워크가 꽤 좋아 보이네요."
    # source L1056
    hyeophap "일할 때는 잘 맞아."
    # source L1060
    darim "네 분이 같이 준비하는 부스가 궁금해지네요."
    # source L1064
    ski "후후. 드디어 보여줄 때가 왔군."
    # source L1068
    hess "발표 자료는 협합 선배한테 있죠?"
    # source L1072
    hyeophap "응. 가져왔어."
    # source L1076
    ski "……내 극적인 소개 타이밍이 또."
    # source L1078: **[SCENE 04 END]**
    jump ch02_sc05

label ch02_sc05:
    $ phone_timeline_enter("CH02", "ch02_sc05")
    # source L1082: **[BG] 축제 부스 예정 구역 · 낮**
    $ story_scene("booth", mode="normal", cast=['roman', 'sia', 'darim', 'omu', 'lumi', 'ski', 'hyeophap', 'hess', 'bambam'], light="day", location="축제 부스 예정 구역 · 낮")
    # source L1084: **[BGM] Curious Campus**
    $ play_bgm("campus_day")
    # source L1088
    narrator "점심을 먹고 난 뒤, 두 팀은 실제 부스가 설치될 구역으로 이동했다."
    # source L1090
    narrator "학생회관 옆에 위치한 광장."
    # source L1092
    narrator "평소에는 학생들이 지나가는 길이지만 축제 기간에는 여러 체험 부스가 들어서는 공간이라고 한다."
    # source L1096
    lumi "여기면 유동 인구는 꽤 많겠네요."
    # source L1100
    darim "강의실이랑 학생회관 사이니까요."
    # source L1104
    omu "사진도 잘 나오겠다. 햇빛도 괜찮고."
    # source L1108
    sia "좋아. 여기서 우리 부스가 제일 유명해지는 거다."
    $ story_stage(faces={"ski": "happy"})  # source L1112
    ski "그건 좀 어려울 것 같은데?"
    # source L1116
    sia "왜?"
    # source L1120
    ski "이미 내가 있으니까."
    # source L1124
    sia "……아, 맞다. 저 인간 있었지."
    # source L1128
    hyeophap "스키, 준비한 거 보여주자."
    # source L1132
    ski "알았어."
    # source L1134: **[SFX] 상자 여는 소리**
    $ story_sfx("message")
    # source L1138
    narrator "스키는 테이블 위에 작은 상자 몇 개를 올려놓았다."
    # source L1140
    narrator "그 안에는 개별 포장된 쿠키와 손바닥만 한 카드들이 들어 있었다."
    show screen story_prop_insert("rival_samples")  # source L1144
    roman "앗,,, 귀여워요……!"
    # source L1148
    bambam "시제품이에요. 아직 맛이랑 종류는 조정 중이에요."
    # source L1152
    ski "프로젝트의 이름은 바로……."
    hide screen story_prop_insert  # source L1154: 라이벌 프로젝트 카드 등장
    # source L1156
    system_note "「오늘의 기분을 굽습니다」"
    # source L1160
    ski "어때?"
    # source L1164
    sia "어…… 이름은 괜찮네."
    # source L1168
    ski "고마워. 나의 천재적인 작명 실력이……."
    # source L1172
    hyeophap "네 명이 같이 골랐어."
    # source L1176
    ski "내가 후보 냈잖아!"
    # source L1180
    bambam "저도 후보 냈는데요."
    # source L1184
    hess "전 투표했어요."
    $ story_stage(faces={"ski": "embarrassed"})  # source L1188
    ski "……팀워크의 결과라고 할게."
    # source L1192
    narrator "헤스가 카드 한 장을 내밀었다."
    # source L1196
    hess "간단히 체험해 보실래요?"
    # source L1200
    mc "네? 지금요?"
    # source L1204
    hess "네. 시제품 테스트라서요."
    # source L1208
    hess "아래 질문 중 하나를 골라주세요."
    # source L1210: **[UI] 체험 카드 표시**
    # source L1212
    system_note "「오늘 하루를 한 단어로 표현한다면?」"
    menu:
        # source L1214
        "정신없는 하루":
            $ story_apply("ch02_sc05_a")
            # source L1226
            mc "정신없는 하루."
            # source L1230
            hess "그럼 이쪽 카드예요."
            # source L1234
            bambam "달콤한 쿠키랑 잠깐 쉬어가라는 메시지예요."
            # source L1238
            sia "야, 이거 완전 우리 팀 이야기 아니냐?"
        # source L1216
        "평범하고 편안한 하루":
            $ story_apply("ch02_sc05_b")
            # source L1244
            mc "평범하고 편안한 하루."
            # source L1248
            bambam "오, 좋네요."
            # source L1250
            bambam "이건 고소한 쿠키랑 작은 응원 카드예요."
            # source L1254
            omu "평범한 하루도 괜찮지."
        # source L1218
        "무언가 기대되는 하루":
            $ story_apply("ch02_sc05_c")
            # source L1260
            mc "무언가 기대되는 하루."
            # source L1264
            hess "그럼 이 카드가 어울리겠네요."
            # source L1268
            bambam "새로운 걸 시작하는 날이라는 느낌으로 준비했어요."
            # source L1272
            roman "앗,,, 문구가 예쁘네요……."
    # source L1274: **[공통 복귀]**
    # source L1278
    hess "실제 심리검사 같은 건 아니고, 방문객이 재미있게 고르는 방식이에요."
    # source L1282
    darim "기분에 맞는 체험이라니 재미있네요."
    # source L1286
    bambam "꼭 정확한 결과가 나와야 한다기보다, 잠깐 쉬어가는 느낌으로 만들었어요."
    # source L1290
    hyeophap "체험한 사람에게는 포장된 디저트를 제공할 거야."
    # source L1292
    hyeophap "식품 보관이나 알레르기 안내도 준비하고 있고."
    # source L1296
    lumi "대기 공간도 작게 나눠 놓으셨네요."
    # source L1300
    hyeophap "응. 사람이 몰리면 줄이 길어질 수 있으니까."
    # source L1304
    omu "사진 찍기도 좋겠네. 색깔도 잘 맞춰놨고."
    # source L1308
    ski "후후. 이제 우리 팀의 위대함을 알겠지?"
    # source L1312
    sia "……."
    # source L1316
    sia "인정하기 싫은데."
    # source L1320
    sia "솔직히 좀 괜찮다."
    # source L1324
    ski "아, 드디어!"
    # source L1328
    ski "이 순간을 얼마나 기다렸는지 몰라!"
    # source L1332
    hyeophap "칭찬받는 게 목적이었어?"
    # source L1336
    ski "승리는 그다음이야."
    # source L1340
    narrator "처음 만났을 때는 그저 시끄러운 사람들이라고 생각했다."
    # source L1342
    narrator "그런데 막상 준비한 내용을 보니 이야기가 달랐다."
    # source L1344
    narrator "헤스가 만든 질문, 밤밤이 준비한 메시지, 협합의 운영 계획."
    # source L1346
    narrator "그리고 스키의 홍보 방식까지."
    # source L1348
    narrator "농담은 많았지만 결과물은 생각보다 탄탄했다."
    # source L1350: **[BG] 잠시 후 · 주인공 팀의 부스 구역**
    $ story_scene("booth", mode="normal", cast=['roman', 'sia', 'darim', 'omu', 'lumi'], light="day", location="잠시 후 · 주인공 팀의 부스 구역")
    # source L1354
    darim "저희도 한번 점검해 봐야겠어요."
    # source L1358
    lumi "공간 배치 자체는 괜찮은데, 방문객이 어디서부터 참여하는지 조금 애매하네요."
    # source L1362
    omu "사진 구경부터 하고 싶은 사람도 있을 거고."
    # source L1366
    roman "글부터 읽고 싶은 분도 계실 것 같아요……."
    # source L1370
    sia "그러면 만화로 순서 설명하면 되지 않나?"
    # source L1374
    mc "그런데 그 순서가 아직 안 정해진 것 같은데요."
    # source L1378
    sia "……."
    # source L1382
    sia "아."
    # source L1386
    darim "맞네요. 저희는 만들 콘텐츠만 먼저 정했어요."
    # source L1390
    lumi "방문객 입장에서 어떻게 움직일지 다시 생각해야겠네."
    # source L1394
    narrator "그때 로만이 조심스럽게 입을 열었다."
    # source L1398
    roman "저……."
    # source L1402
    roman "그럼 지금부터 잘 만들어 보면 되지 않을까요……?"
    # source L1406
    sia "……오?"
    # source L1410
    omu "맞는 말이네."
    # source L1414
    roman "앗,,, 아니, 그냥……."
    # source L1418
    darim "로만 씨 말이 맞아요."
    # source L1422
    lumi "응. 아직 시간 있으니까."
    # source L1426
    sia "좋아! 그럼 우리도 제대로 해보자."
    # source L1430
    mc "일단 뭘 고쳐야 하는지부터 정리해요."
    # source L1432: **[FLAG] rival_project_observed = True**
    $ story_flag("rival_project_observed", True)
    # source L1434: **[SCENE 05 END]**
    jump ch02_sc06

label ch02_sc06:
    $ phone_timeline_enter("CH02", "ch02_sc06")
    # source L1438: **[BG] 공동 동아리실 · 오후**
    $ story_scene("clubroom307", mode="normal", cast=["roman", "sia", "darim", "omu", "lumi"], light="day", location="동아리실 307호 · 오후")
    # source L1440: **[BGM] Hopeful Campus**
    $ play_bgm("hopeful_teamwork")
    $ sd_event_start("ch02_whiteboard_huddle", variant="01")
    # source L1444
    narrator "동아리실로 돌아오자마자 다림이 화이트보드 앞에 섰다."
    # source L1448
    darim "아까 확인한 문제를 먼저 정리해 볼까요?"
    # source L1452
    sia "우리도 잘하고 있는 거 아니었어?"
    # source L1456
    lumi "잘하고 있죠. 다만 방문객이 어떻게 참여하는지는 아직 부족해요."
    # source L1460
    omu "사진이랑 글이랑 그림이 각각 따로 노는 느낌도 있긴 하지."
    # source L1464
    roman "앗,,, 그럼 하나의 질문으로 연결하면 어떨까요……?"
    # source L1468
    mc "하나의 질문이요?"
    # source L1472
    roman "네…… 예를 들면 '오늘 기억하고 싶은 순간' 같은 거요."
    # source L1476
    roman "그걸 글로 적어도 되고, 사진이나 그림으로 남겨도 되고요."
    # source L1480
    sia "오, 그럼 내 안내 만화도 그 질문부터 시작하면 되겠네."
    # source L1484
    darim "참여 방식도 더 간단하게 정리할 수 있겠어요."
    # source L1488
    lumi "공간도 그 흐름에 맞춰 바꿔볼게요."
    # source L1492
    omu "난 전시에 넣을 사진을 좀 더 찍어올게."
    $ sd_event_end()
    # source L1496
    narrator "회의는 빠르게 정리됐다."
    # source L1498
    narrator "각자 해야 할 일도 정해졌다."
    # source L1500
    narrator "그런데 문득 한 가지를 깨달았다."
    # source L1504
    mc "……저 또 여기저기 다 도와야 하는 거죠?"
    # source L1508
    sia "당연하지."
    # source L1512
    darim "너무 부담되시면 한 분부터 도와주셔도 돼요."
    # source L1516
    lumi "오늘은 먼저 하고 싶은 것부터 골라보세요."
    # source L1520
    narrator "좋아."
    # source L1522
    narrator "그럼 어디부터 시작하지?"
    menu:
        # source L1526
        "로만과 질문 카드를 만든다.":
            $ story_apply("ch02_sc06_roman", values={'ch02_partner': 'roman'})
            jump ch02_sc06_roman
        # source L1528
        "시아와 안내 만화를 수정한다.":
            $ story_apply("ch02_sc06_sia", values={'ch02_partner': 'sia'})
            jump ch02_sc06_sia
        # source L1530
        "다림과 운영 계획을 정리한다.":
            $ story_apply("ch02_sc06_darim", values={'ch02_partner': 'darim'})
            jump ch02_sc06_darim
        # source L1532
        "오므와 전시용 사진을 찍는다.":
            $ story_apply("ch02_sc06_omu", values={'ch02_partner': 'omu'})
            jump ch02_sc06_omu
        # source L1534
        "하린과 부스 모형을 만든다.":
            $ story_apply("ch02_sc06_lumi", values={'ch02_partner': 'lumi'})
            jump ch02_sc06_lumi

label ch02_sc06_roman:
    $ phone_timeline_enter("CH02", "ch02_sc06_roman")
    # source L1542: **[BG] 도서관 스터디 공간**
    $ story_scene("library", mode="emotion", cast=['roman'], light="day", location="도서관 스터디 공간")
    # source L1544: **[BGM] Quiet Library**
    $ play_bgm("quiet_library")
    # source L1548
    narrator "로만과 함께 도서관 한쪽에 자리를 잡았다."
    # source L1550
    narrator "책상 위에는 색색의 카드와 몇 장의 메모지가 놓여 있었다."
    # source L1554
    roman "앗,,, 이 정도면 될까요……?"
    # source L1558
    mc "카드가 꽤 많네요."
    $ story_stage(faces={"roman": "embarrassed"})  # source L1562
    roman "아…… 혹시 너무 많이 만들었나요?"
    # source L1566
    mc "아뇨. 어떤 질문인지 궁금해서요."
    # source L1570
    roman "그럼 하나 읽어보실래요?"
    # source L1574
    narrator "나는 가장 위에 있던 카드를 집어 들었다."
    # source L1576
    system_note "「오늘 가장 기억하고 싶은 순간은 무엇인가요?」"
    # source L1580
    mc "괜찮네요."
    # source L1584
    roman "정말요……?"
    # source L1588
    mc "네. 어렵지도 않고, 누구나 대답할 수 있을 것 같아요."
    $ story_stage(faces={"roman": "happy"})  # source L1592
    roman "앗,,, 다행이에요."
    # source L1596
    roman "사실 처음에는 질문을 조금 어렵게 썼거든요."
    # source L1600
    mc "예를 들면요?"
    # source L1604
    roman "음……."
    # source L1608
    roman "'당신의 삶을 구성하는 가장 의미 있는 기억의 본질은 무엇인가요?'……."
    # source L1612
    mc "……."
    # source L1616
    $ story_stage(faces={"roman": "embarrassed"})
    roman "앗,,, 너무 어려웠죠……?"
    # source L1620
    mc "이건 축제 부스가 아니라 철학 시험 아니에요?"
    # source L1624
    roman "후후…… 다림 선배한테 물어봐야 할까요?"
    # source L1628
    mc "다림 선배도 잠깐 고민하실 것 같은데요."
    # source L1632
    roman "그, 그렇겠네요……."
    $ story_stage(faces={"roman": "happy"})  # source L1636
    $ story_effect("bounce", "roman")  # source L1636
    narrator "로만은 웃으며 어려운 문장이 적힌 카드를 한쪽으로 치웠다."
    # source L1640
    roman "그런데 질문은 쉬워도…… 대답은 사람마다 다를 것 같아요."
    # source L1644
    mc "그게 좋은 점이죠."
    # source L1648
    roman "네. 저도 그렇게 생각해요."
    # source L1652
    narrator "잠깐의 침묵이 흘렀다."
    # source L1654
    narrator "로만은 펜 끝으로 카드의 가장자리를 톡톡 두드렸다."
    # source L1658
    roman "[player_name] 씨."
    # source L1662
    mc "네?"
    # source L1666
    roman "만약 오늘 하루를 한 문장으로 남긴다면…… 뭐라고 쓰실 거예요?"
    menu:
        # source L1670
        "생각보다 재미있는 사람들을 만난 날.":
            $ story_apply("ch02_roman_a")
            # source L1680
            roman "앗,,, 재미있는 사람들이요……?"
            # source L1684
            mc "네. 특히 시아랑 스키요."
            # source L1688
            roman "후후…… 그건 정말 인정해요."
            # source L1692
            roman "그럼 저도 재미있는 사람에 포함되나요?"
            # source L1696
            mc "당연하죠."
            # source L1700
            roman "……앗."
        # source L1672
        "조금씩 새로운 걸 배우는 날.":
            $ story_apply("ch02_roman_b")
            # source L1706
            roman "좋은 문장이네요."
            # source L1708
            roman "오늘은 저도 배운 게 많아요."
            # source L1712
            mc "어떤 거요?"
            # source L1716
            roman "글을 잘 쓰는 것보다…… 읽는 사람이 이해하기 쉬운 게 중요하다는 거요."
        # source L1674
        "아직 어떻게 끝날지 모르는 날.":
            $ story_apply("ch02_roman_c")
            # source L1722
            roman "조금 두근거리는 문장이네요."
            # source L1726
            mc "그래요?"
            # source L1730
            roman "네. 다음에 어떤 일이 생길지 모른다는 느낌이어서요."
    # source L1732: **[공통 복귀]**
    # source L1736
    roman "그럼 이 문장들도 따로 적어둘게요."
    # source L1740
    mc "왜요?"
    # source L1744
    roman "방문객 질문을 만드는 데 도움이 될 것 같아서요."
    # source L1748
    roman "아, 물론…… [player_name] 씨가 싫으시면 안 적을게요."
    # source L1752
    mc "괜찮아요. 같이 만든 거잖아요."
    # source L1756
    roman "……네."
    $ story_icon("roman", "heart")  # source L1760
    narrator "로만은 작게 웃으며 메모장에 문장을 적었다."
    # source L1762
    narrator "그리고 잠시 뒤, 자신이 써 놓은 질문 하나를 내밀었다."
    # source L1764
    system_note "「오늘 가장 웃겼던 사람은 누구인가요?」"
    # source L1768
    mc "……이건 뭐예요?"
    # source L1772
    roman "후후……."
    # source L1776
    roman "시아 선배랑 스키 선배 중에 고르시라고요."
    # source L1780
    mc "로만 씨도 은근히 장난치네요?"
    # source L1784
    roman "앗,,, 들켰네요……!"
    # source L1786: **[FLAG] ch02_partner = roman / affection.roman +1 / roman_question_event = True**
    $ story_apply("ch02_sc06_roman_complete", affection={'roman': 1}, values={'ch02_partner': 'roman', 'roman_question_event': True})
    $ secret_note_unlock("roman", 1)
    # source L1788: **[공통 SC07로 복귀]**
    jump ch02_sc07

label ch02_sc06_sia:
    $ phone_timeline_enter("CH02", "ch02_sc06_sia")
    # source L1792: **[BG] 애니메이션과 작업실**
    $ story_scene("animation", mode="emotion", cast=['sia'], light="day", location="애니메이션과 작업실")
    # source L1794: **[BGM] Playful Workshop**
    $ play_bgm("comedy_light")
    $ story_stage(faces={"sia": "smug"})  # source L1798
    sia "좋아. 이번에는 진짜 완벽하게 만들 거야."
    # source L1802
    mc "지난번에도 그렇게 말하지 않았어요?"
    # source L1806
    sia "응 아니야~ 그때는 연습."
    # source L1810
    mc "몇 번까지 연습인데요?"
    # source L1814
    sia "완성할 때까지."
    # source L1818
    narrator "시아는 태블릿 화면을 확대했다."
    # source L1820
    narrator "그 안에는 축제 부스를 소개하는 만화가 있었다."
    # source L1824
    mc "그런데 그림은 이미 괜찮지 않아요?"
    # source L1828
    sia "그림은 괜찮지."
    # source L1832
    sia "문제는 이걸 처음 보는 사람이 이해하느냐인데……."
    # source L1836
    mc "네."
    $ story_stage(faces={"sia": "serious"})  # source L1840
    sia "……솔직히 좀 애매하긴 해."
    # source L1844
    narrator "시아는 펜을 잠시 내려놓았다."
    # source L1846
    narrator "평소처럼 장난스럽게 넘길 줄 알았는데, 생각보다 진지한 얼굴이었다."
    # source L1850
    mc "그럼 처음부터 다시 봐볼까요?"
    $ story_stage(faces={"sia": "smug"})  # source L1854
    sia "오, 감상 담당님이 드디어 일하실 생각이 드셨나?"
    # source L1858
    mc "돈도 안 받는데 너무 부려먹는 거 아니에요?"
    # source L1862
    sia "경력 쌓아준다 생각해."
    # source L1866
    mc "무슨 경력이요?"
    # source L1870
    sia "천재 작가 시아의 첫 번째 독자."
    # source L1874
    mc "그렇게 대단한 직책이었어요?"
    # source L1878
    sia "당연하지."
    # source L1882
    narrator "우리는 첫 컷부터 천천히 확인했다."
    # source L1884
    narrator "그런데 세 번째 컷에서 문제가 생겼다."
    # source L1888
    mc "잠깐만요. 여기서는 왜 갑자기 강아지가 나와요?"
    # source L1892
    sia "귀여우니까."
    # source L1896
    mc "부스 소개잖아요."
    # source L1900
    sia "강아지가 부스 안내해 주는 거지."
    # source L1904
    mc "그런데 강아지가 갑자기 우주로 날아가는데요?"
    # source L1908
    sia "장면 전환."
    # source L1912
    mc "……."
    # source L1916
    sia "왜."
    # source L1920
    mc "그림은 잘 그리는데 이야기가 너무 자유로운 거 아니에요?"
    $ story_stage(faces={"sia": "happy"})  # source L1924
    $ story_effect("bounce", "sia")  # source L1924
    sia "ㅋㅋㅋㅋ 그건 맞아."
    # source L1928
    narrator "시아는 웃다가 다시 펜을 들었다."
    # source L1932
    sia "그러면 제대로 해보자."
    menu:
        # source L1936
        "강아지는 남기고 내용을 단순화해요.":
            $ story_apply("ch02_sia_a")
            # source L1946
            sia "오. 강아지는 살려주는 거야?"
            # source L1950
            mc "로만도 좋아할 것 같은데요?"
            # source L1954
            sia "좋아. 강아지의 우주 진출은 다음 작품으로 미룬다."
        # source L1938
        "사람이 직접 설명하는 방식으로 바꿔요.":
            $ story_apply("ch02_sia_b")
            # source L1960
            sia "정석적인 방식이네."
            # source L1964
            mc "이해하기는 쉬울 것 같아서요."
            # source L1968
            sia "좋아. 그럼 표정을 좀 웃기게 그리면 되겠다."
        # source L1940
        "설명은 간단하게, 마지막에 개그를 넣어요.":
            $ story_apply("ch02_sia_c")
            # source L1974
            sia "야, 그거다!"
            # source L1976
            sia "설명은 먼저 끝내고 마지막에 웃기는 거지."
            # source L1980
            mc "네. 너무 복잡하지 않게요."
            # source L1984
            sia "오케이. 이번엔 네 말 듣는다."
    # source L1986: **[공통 복귀]**
    # source L1990
    narrator "시아는 새 컷을 그리기 시작했다."
    # source L1992
    narrator "평소의 수다스러운 모습과 달리, 작업에 집중할 때는 말수가 줄어들었다."
    # source L1994
    narrator "한참이 지난 뒤였다."
    # source L1998
    sia "……됐어."
    # source L2002
    mc "볼게요."
    # source L2006
    narrator "처음보다 훨씬 간단하고 읽기 쉬운 만화가 완성되어 있었다."
    # source L2010
    mc "이번 건 진짜 좋네요."
    # source L2014
    sia "그치?"
    # source L2018
    mc "네. 그림도 잘 그렸는데, 읽는 사람 입장도 잘 생각한 것 같아요."
    # source L2022
    sia "……."
    # source L2026
    mc "왜요?"
    # source L2030
    sia "아니."
    # source L2034
    sia "너 칭찬할 때 되게 진지하게 한다?"
    # source L2038
    mc "좋으니까 좋다고 하는 거죠."
    # source L2042
    sia "……흐음."
    # source L2046
    narrator "시아는 다시 그림을 바라봤다."
    # source L2050
    sia "야."
    # source L2054
    mc "네?"
    $ story_stage(faces={"sia": "embarrassed"})  # source L2058
    sia "고맙다."
    # source L2062
    mc "뭐가요?"
    $ story_icon("sia", "heart")  # source L2066
    sia "그냥. 같이 봐줘서."
    # source L2070
    narrator "평소보다 목소리가 조금 작았다."
    # source L2072
    narrator "그런데 내가 대답하기도 전에 시아가 다시 씩 웃었다."
    $ story_stage(faces={"sia": "happy"})  # source L2076
    sia "자, 그럼 다음 것도 해보자!"
    # source L2080
    mc "……다음 것도 있어요?"
    # source L2084
    sia "당연하지."
    # source L2086
    sia "콘티 지옥은 아직 안 끝났거든."
    # source L2088: **[FLAG] ch02_partner = sia / affection.sia +1 / sia_webtoon_revision = True**
    $ story_apply("ch02_sc06_sia_complete", affection={'sia': 1}, values={'ch02_partner': 'sia', 'sia_webtoon_revision': True})
    $ secret_note_unlock("sia", 1)
    # source L2090: **[공통 SC07로 복귀]**
    jump ch02_sc07

label ch02_sc06_darim:
    $ phone_timeline_enter("CH02", "ch02_sc06_darim")
    # source L2094: **[BG] 캠퍼스 스터디룸**
    $ story_scene("study", mode="emotion", cast=['darim'], light="day", location="캠퍼스 스터디룸")
    # source L2096: **[BGM] Warm Study**
    $ play_bgm("warm_workshop")
    # source L2100
    darim "일단 지금까지 정리된 작업부터 확인할까요?"
    # source L2104
    mc "네."
    # source L2108
    narrator "다림은 노트북에 정리한 작업 목록을 보여줬다."
    # source L2110
    narrator "그런데 목록이 생각보다 길었다."
    # source L2114
    mc "……이거 언제 다 해요?"
    # source L2118
    darim "하나씩 하면 되죠."
    # source L2122
    mc "되게 침착하시네요."
    # source L2126
    darim "음……."
    # source L2128
    darim "침착한 척하고 있는 걸 수도 있어요."
    # source L2132
    mc "진짜요?"
    $ story_stage(faces={"darim": "smug"})  # source L2136
    darim "후후. 농담이에요."
    # source L2140
    narrator "우리는 작업별 마감일과 담당자를 정리하기 시작했다."
    $ story_stage(faces={"darim": "normal"})  # source L2144
    darim "여기 안내문은 로만 씨랑 시아 씨가 같이 보면 좋겠네요."
    # source L2148
    mc "글이랑 그림을 연결하는 거니까요."
    # source L2152
    darim "네. 그리고 방문객이 참여하는 과정은 제가 한번 확인할게요."
    # source L2156
    mc "그럼 선배가 할 일이 너무 많아지는 거 아니에요?"
    # source L2160
    darim "……그러네요."
    # source L2164
    narrator "다림은 잠시 화면을 바라봤다."
    # source L2168
    darim "원래 이런 걸 정리하다 보면 자연스럽게 제가 할 일을 많이 적게 되더라고요."
    # source L2172
    mc "그럼 나눠요."
    $ story_stage(faces={"darim": "surprised"})  # source L2176
    darim "네?"
    # source L2180
    mc "일정표 정리랑 안내문 점검은 제가 도울 수 있잖아요."
    # source L2184
    darim "……괜찮으시겠어요?"
    # source L2188
    mc "같이 하는 프로젝트니까요."
    # source L2192
    darim "그렇죠."
    $ story_stage(faces={"darim": "happy"})  # source L2196
    darim "그럼 정말 부탁드릴게요."
    menu:
        # source L2200
        "제가 안내문 점검을 맡을게요.":
            $ story_apply("ch02_darim_a")
            # source L2210
            darim "좋아요. 그럼 제가 전체 운영 계획을 볼게요."
            # source L2214
            mc "네."
            # source L2218
            darim "생각보다 일이 빨리 끝나겠네요."
        # source L2202
        "작업별 마감일을 같이 확인해요.":
            $ story_apply("ch02_darim_b")
            # source L2224
            darim "좋은 생각이에요."
            # source L2226
            darim "마감일이 겹치는 것부터 조정하면 훨씬 편할 거예요."
        # source L2204
        "다른 팀원들 의견도 먼저 들어보죠.":
            $ story_apply("ch02_darim_c")
            # source L2232
            darim "맞아요. 혼자 정하면 오히려 문제가 생길 수 있으니까요."
            # source L2234
            darim "다들 가능한 일정을 확인해 볼게요."
    # source L2236: **[공통 복귀]**
    # source L2240
    narrator "한동안 작업을 정리하고 나자, 복잡했던 표가 조금씩 깔끔해졌다."
    # source L2244
    mc "오. 이제 할 만해 보이네요."
    # source L2248
    darim "그러게요. 혼자 할 때보다 훨씬 빠르네요."
    # source L2252
    mc "그럼 잠깐 쉴까요?"
    # source L2256
    darim "좋아요."
    # source L2258: **[SFX] 휴대전화 알림**
    $ story_sfx("message")
    # source L2262
    narrator "다림의 휴대전화에 게임 알림이 떴다."
    # source L2266
    mc "어? 그거 아직 하세요?"
    # source L2270
    darim "그럼요."
    # source L2274
    mc "전에 한 판 하자고 하셨잖아요."
    # source L2278
    darim "……기억하고 계셨네요?"
    # source L2282
    mc "당연하죠."
    $ story_icon("darim", "heart")  # source L2286
    darim "후후. 그럼 나중에 꼭 한 판 해요."
    # source L2290
    mc "선배가 이길 자신 있으세요?"
    # source L2294
    darim "있죠."
    # source L2298
    mc "오."
    # source L2302
    darim "물론 제가 이길 수 있는 게임으로 할 거예요."
    # source L2306
    mc "그건 반칙 아니에요?"
    $ story_stage(faces={"darim": "smug"})  # source L2310
    $ story_effect("bounce", "darim")  # source L2310
    darim "후후. 전략이에요."
    # source L2314
    narrator "다림은 웃으며 다시 노트북을 켰다."
    # source L2316
    narrator "차분하게 대화하던 사람에게서 의외로 장난스러운 면이 조금씩 보이기 시작했다."
    # source L2318: **[FLAG] ch02_partner = darim / trust.darim +1 / darim_schedule_event = True**
    $ story_apply("ch02_sc06_darim_complete", trust={'darim': 1}, values={'ch02_partner': 'darim', 'darim_schedule_event': True})
    $ secret_note_unlock("darim", 1)
    # source L2320: **[공통 SC07로 복귀]**
    jump ch02_sc07

label ch02_sc06_omu:
    $ phone_timeline_enter("CH02", "ch02_sc06_omu")
    # source L2324: **[BG] 캠퍼스 산책로 · 오후**
    $ story_scene("campus", mode="emotion", cast=['omu'], light="day", location="캠퍼스 산책로 · 오후")
    # source L2326: **[BGM] Gentle Walk**
    $ play_bgm("gentle_walk")
    # source L2330
    narrator "오므와 함께 캠퍼스를 돌아다니기 시작했다."
    # source L2332
    narrator "지난번에 왔던 길이었지만, 오늘은 목적이 조금 달랐다."
    # source L2336
    omu "오늘은 전시에 쓸 만한 사진을 좀 찍어보자."
    # source L2340
    mc "어떤 사진이 좋은데요?"
    # source L2344
    omu "너무 꾸민 거 말고."
    # source L2346
    omu "진짜 학교생활 같은 거."
    # source L2350
    mc "진짜 학교생활이요?"
    # source L2354
    omu "어. 예를 들면 저기 봐라."
    # source L2358
    narrator "오므가 가리킨 곳에는 학생 몇 명이 벤치에 앉아 이야기하고 있었다."
    # source L2360
    narrator "그 옆에는 떨어진 낙엽과 커피잔이 놓여 있었다."
    # source L2364
    omu "저런 분위기."
    # source L2366
    omu "막 특별한 건 아닌데, 나중에 보면 기억날 것 같은 거."
    # source L2370
    mc "사진에 사람이 들어가도 돼요?"
    # source L2374
    omu "허락받고 찍어야지."
    # source L2376
    omu "안 그러면 풍경만 찍으면 되고."
    # source L2380
    mc "그렇네요."
    # source L2384
    narrator "오므는 사람들의 얼굴이 나오지 않는 각도에서 벤치와 낙엽을 찍었다."
    # source L2386: **[SFX] 카메라 셔터**
    $ story_sfx("shutter")
    $ story_stage(faces={"omu": "happy"})  # source L2390
    omu "오, 괜찮네."
    # source L2394
    mc "보여 주세요."
    # source L2398
    narrator "사진 속에는 평범한 벤치와 나무가 담겨 있었다."
    # source L2400
    narrator "그런데 이상하게도 실제로 보는 것과 분위기가 달랐다."
    # source L2404
    mc "신기하네요."
    # source L2408
    omu "뭐가?"
    # source L2412
    mc "그냥 지나가던 곳인데 사진으로 보니까 다르게 보이네요."
    $ story_effect("bounce", "omu")  # source L2416
    omu "그런 게 재밌는 거지."
    # source L2420
    narrator "잠시 후 우리는 학생회관 앞에 도착했다."
    # source L2424
    mc "여기는 어때요?"
    # source L2428
    omu "음……."
    # source L2432
    narrator "오므는 카메라를 들었다가 다시 내렸다."
    # source L2436
    mc "왜요?"
    $ story_stage(faces={"omu": "angry"})  # source L2440
    omu "저기 쓰레기 봐라."
    # source L2444
    narrator "화단 옆에 빈 음료수 컵이 버려져 있었다."
    # source L2448
    omu "멀쩡한 쓰레기통이 바로 옆에 있는데 와 저기 버리노."
    # source L2452
    mc "그러게요."
    # source L2456
    omu "진짜 이해 안 된다."
    # source L2460
    narrator "오므는 잠시 카메라를 내려놓았다."
    # source L2462
    narrator "나는 주변을 살펴봤다."
    menu:
        # source L2466
        "같이 치워요.":
            $ story_apply("ch02_omu_a")
            # source L2476
            mc "같이 치워요."
            # source L2480
            omu "어, 좋지."
            # source L2484
            narrator "우리는 주변에 떨어진 컵을 정리했다."
            # source L2488
            omu "이렇게 금방 치울 수 있는 걸."
            # source L2492
            mc "그러게요."
        # source L2468
        "관리하시는 분께 알려드려요.":
            $ story_apply("ch02_omu_b")
            # source L2498
            mc "관리하시는 분께 알려드려요."
            # source L2502
            omu "그것도 괜찮겠다."
            # source L2504
            omu "괜히 위험한 쓰레기가 있을 수도 있으니까."
            # source L2508
            narrator "우리는 건물 안내 데스크에 상황을 알렸다."
        # source L2470
        "저런 사람들은 왜 그러는 걸까요?":
            $ story_apply("ch02_omu_c")
            # source L2514
            mc "저런 사람들은 왜 그러는 걸까요?"
            # source L2518
            omu "몰라."
            # source L2520
            omu "근데 귀찮다고 아무 데나 버리는 건 좀 그렇지 않나."
            # source L2524
            mc "맞아요."
            # source L2528
            omu "남이 치워야 하는 건데."
    # source L2530: **[공통 복귀]**
    # source L2534
    narrator "잠시 뒤 우리는 다시 사진을 찍으러 이동했다."
    # source L2538
    mc "오므 씨는 이런 거 보면 그냥 못 지나치는군요."
    # source L2542
    omu "뭐…… 그렇지."
    # source L2546
    mc "확실히 자기 기준이 있네요."
    # source L2550
    omu "기준이라기보단 그냥 기본적인 거 아이가?"
    # source L2554
    mc "그렇긴 해요."
    # source L2558
    narrator "오므는 카메라를 다시 들었다."
    # source L2562
    omu "야, 저기 서 봐라."
    # source L2566
    mc "저요?"
    # source L2570
    omu "어. 뒷모습은 안 찍을 거니까 그냥 저쪽 풍경 좀 봐줘."
    # source L2574
    mc "왜요?"
    # source L2578
    omu "니가 보던 쪽 구도가 괜찮아 보여서."
    # source L2582
    narrator "오므는 내가 가리켰던 방향을 촬영했다."
    # source L2584: **[SFX] 셔터**
    $ story_sfx("shutter")
    # source L2588
    $ story_stage(faces={"omu": "happy"})
    omu "오. 잘 나왔다."
    # source L2592
    mc "보여 주세요."
    # source L2596
    omu "잠깐. 이것도 찍고."
    # source L2600
    mc "생각보다 엄청 진지하네요."
    # source L2604
    $ story_stage(faces={"omu": "serious"})
    omu "좋아하는 거니까."
    # source L2608
    narrator "오므는 사진을 몇 장 더 찍었다."
    # source L2612
    omu "오늘 사진은 나중에 정리해서 보내줄게."
    # source L2616
    mc "고마워요."
    # source L2620
    omu "다음엔 니가 직접 한번 찍어봐라."
    # source L2624
    mc "또 구도 이상하다고 할 거잖아요."
    # source L2628
    omu "그건 니가 이상하게 찍으면 그렇겠지."
    # source L2632
    mc "……."
    # source L2636
    $ story_stage(faces={"omu": "smug"})
    omu "ㅋㅋㅋ 농담이다."
    # source L2638: **[FLAG] ch02_partner = omu / affection.omu +1 / omu_campus_photo_event = True**
    $ story_apply("ch02_sc06_omu_complete", affection={'omu': 1}, values={'ch02_partner': 'omu', 'omu_campus_photo_event': True})
    $ secret_note_unlock("omu", 1)
    # source L2640: **[공통 SC07로 복귀]**
    jump ch02_sc07

label ch02_sc06_lumi:
    $ phone_timeline_enter("CH02", "ch02_sc06_lumi")
    # source L2644: **[BG] 건축학과 작업실**
    $ story_scene("architecture", mode="emotion", cast=['lumi'], light="day", location="건축학과 작업실")
    # source L2646: **[BGM] Calm Workshop**
    $ play_bgm("warm_workshop")
    # source L2650
    narrator "하린이는 책상 위에 작은 부스 모형을 올려놓았다."
    # source L2652
    narrator "종이와 폼보드로 만든 간단한 모형이었다."
    # source L2656
    lumi "일단 지금 생각한 배치는 이거예요."
    # source L2660
    mc "오, 진짜 부스처럼 보이네요."
    # source L2664
    lumi "아직은 대충 만든 거지만요."
    # source L2668
    mc "대충 만든 것치고는 엄청 깔끔한데요?"
    $ story_stage(faces={"lumi": "smug"})  # source L2672
    lumi "후후. 그런 말은 자주 해주셔도 되는데."
    # source L2676
    mc "칭찬에 익숙하네요."
    # source L2680
    lumi "좋은 말은 많이 들을수록 좋잖아요."
    # source L2684
    narrator "나는 모형을 자세히 살펴봤다."
    # source L2686
    narrator "글을 남기는 공간, 사진을 전시하는 벽, 안내 테이블."
    # source L2688
    narrator "전체적으로 잘 정리되어 있었다."
    # source L2692
    mc "그런데 여기서 사진 보고 나오려면 조금 돌아가야 하지 않아요?"
    $ story_stage(faces={"lumi": "serious"})  # source L2696
    lumi "……."
    # source L2700
    narrator "하린이가 모형을 돌려봤다."
    # source L2704
    lumi "그러네."
    # source L2708
    mc "네?"
    # source L2712
    lumi "맞아요. 이쪽으로 사람이 몰리면 돌아가야겠네요."
    # source L2716
    mc "그냥 생각난 건데요."
    # source L2720
    lumi "그 생각이 필요한 거죠."
    # source L2724
    narrator "하린이는 펜을 꺼내 모형 옆의 종이에 선을 그었다."
    # source L2728
    lumi "그럼 여기 통로를 조금 넓히고……."
    # source L2732
    mc "사진 전시를 반대쪽으로 옮기면 어떨까요?"
    # source L2736
    lumi "나쁘지 않겠네요."
    # source L2740
    lumi "다만 글을 쓰는 공간이 좁아질 수 있어요."
    # source L2744
    mc "어렵네요."
    # source L2748
    lumi "공간이란 게 그래요."
    # source L2750
    lumi "하나를 늘리면 다른 쪽에서 줄여야 하니까."
    # source L2754
    mc "좀 철학적인 말인데요?"
    # source L2758
    lumi "건축학과도 가끔 철학적인 말을 합니다."
    # source L2762
    mc "다림 선배한테 들려줘야겠어요."
    # source L2766
    lumi "그러면 제 논리가 검증당할지도 모르겠네요."
    menu:
        # source L2770
        "관람객이 움직이기 편한 게 우선이죠.":
            $ story_apply("ch02_lumi_a")
            # source L2780
            lumi "동의해요."
            # source L2782
            lumi "아무리 예뻐도 불편하면 좋은 공간이라고 하기 어렵죠."
        # source L2772
        "전시물이 잘 보이는 것도 중요하지 않을까요?":
            $ story_apply("ch02_lumi_b")
            # source L2788
            lumi "맞아요. 보여주는 방식도 중요하니까."
            # source L2790
            lumi "그럼 높이와 간격을 조금 조정해볼까요?"
        # source L2774
        "잠깐 쉴 수 있는 공간은 없어요?":
            $ story_apply("ch02_lumi_c")
            # source L2796
            lumi "쉬는 공간……."
            # source L2800
            lumi "생각보다 괜찮은데?"
            # source L2802
            lumi "잠깐 머물러서 기록을 읽는 자리도 있으면 좋겠네요."
    # source L2804: **[공통 복귀]**
    # source L2808
    narrator "하린이는 모형의 작은 벽 하나를 떼어내 다른 위치에 붙였다."
    # source L2812
    mc "그렇게 금방 바꿔도 돼요?"
    # source L2816
    lumi "모형이니까요."
    # source L2818
    lumi "지금 바꿔봐야 실제로 만들 때 덜 고생하죠."
    # source L2822
    mc "전 하린 씨가 계획 바뀌는 거 싫어할 줄 알았는데요."
    # source L2826
    lumi "왜요?"
    # source L2830
    mc "깔끔하고 반듯한 거 좋아하시잖아요."
    # source L2834
    lumi "그건 맞아요."
    # source L2838
    lumi "그런데 좋은 계획은 고칠 수 있어야 한다고 생각해요."
    # source L2842
    mc "의외네요."
    $ story_stage(faces={"lumi": "smug"})  # source L2846
    lumi "저에 대해 벌써 많이 안다고 생각하셨나 봐요?"
    # source L2850
    mc "조금요?"
    # source L2854
    lumi "흐음."
    # source L2858
    lumi "그럼 앞으로 더 알아보셔야겠네."
    $ story_effect("bounce", "lumi")  # source L2862
    narrator "하린이는 능글맞게 웃었다."
    # source L2866
    mc "그렇게 말하니까 뭔가 시험 보는 것 같은데요."
    # source L2870
    lumi "시험은 아니에요."
    # source L2872
    lumi "다만 정답이 있다고 보장할 수는 없죠."
    # source L2876
    mc "……그건 더 어렵잖아요."
    # source L2880
    $ story_stage(faces={"lumi": "happy"})
    lumi "후후."
    # source L2884
    narrator "하린이는 수정한 모형을 바라보며 고개를 끄덕였다."
    # source L2888
    lumi "오늘 같이 봐줘서 고마워."
    # source L2892
    mc "저도 재미있었어요."
    # source L2896
    lumi "그럼 다음에도 같이 작업하실래요?"
    # source L2900
    mc "네."
    $ story_icon("lumi", "heart")  # source L2904
    lumi "좋아요. 기대할게."
    # source L2906: **[FLAG] ch02_partner = rumi / affection.rumi +1 / rumi_model_event = True**
    $ story_apply("ch02_sc06_lumi_complete", affection={'lumi': 1}, values={'ch02_partner': 'lumi', 'rumi_model_event': True})
    $ secret_note_unlock("lumi", 1)
    # source L2908: **[공통 SC07로 복귀]**
    jump ch02_sc07

label ch02_sc07:
    $ phone_timeline_enter("CH02", "ch02_sc07")
    # source L2912: **[BG] 축제 준비실 복도**
    $ story_scene("corridor", mode="normal", cast=[], light="day", location="축제 준비실 복도")
    # source L2914: **[BGM] Light Comedy**
    $ play_bgm("comedy_light")
    # source L2918
    narrator "개인 작업을 마치고 동아리실로 돌아가는 길이었다."
    # source L2920
    narrator "복도 끝에서 익숙한 목소리가 들렸다."
    $ story_enter("ski", side="right", face="happy")  # source L2924
    ski "걱정 마! 내가 완벽하게 옮길게!"
    $ story_enter("hyeophap", side="right", face="serious")  # source L2928
    hyeophap "스키, 한 번에 다 옮기지 말고 나눠서……."
    # source L2930: **[SFX] 상자 부딪히는 소리**
    $ story_sfx("impact")
    $ story_stage(faces={"ski": "surprised"})  # source L2934
    ski "……어?"
    $ story_stage_fall("ski", side="right")

    $ story_sfx("paper")  # source L2936: 카드가 바닥에 흩어지는 소리
    $ sd_event_start("ch02_ski_accident", variant="01")
    # source L2942
    narrator "상자 하나가 문턱에 걸렸다."
    # source L2944
    narrator "다행히 크게 다친 사람은 없었지만, 안에 있던 자료들이 복도 바닥에 흩어졌다."
    # source L2948
    ski "아, 괜찮아!"
    # source L2950
    ski "이 정도는 내 완벽한 계산 범위 안에……."

    # source L2954
    hyeophap "완벽한 계산에 상자 떨어뜨리는 것도 포함돼?"
    # source L2958
    ski "……오차가 좀 있었어."
    # source L2962
    hess "꽤 큰 오차네요."
    # source L2966
    bambam "저쪽까지 날아갔어요."
    # source L2970
    ski "다들 너무 냉정한 거 아니야?"
    # source L2974
    hyeophap "말할 시간에 주워."
    # source L2978
    ski "응……."
    # source L2982
    narrator "바닥에 흩어진 카드 몇 장이 우리 쪽까지 굴러왔다."
    # source L2986
    sia "어? 뭐야. 사고 났네?"
    # source L2990
    omu "니는 왜 웃고 있노."
    # source L2994
    sia "아니, 아까 완벽하게 운반한다더니ㅋㅋ"
    # source L2998
    darim "카드가 밟히기 전에 정리해야겠네요."
    # source L3002
    roman "앗,,, 많이 떨어졌어요……."
    # source L3006
    lumi "자료가 손상되면 다시 만들어야 할 수도 있겠네요."
    # source L3010
    mc "어떻게 하지?"
    menu:
        # source L3014
        "일단 같이 주워요.":
            $ sd_event_change("03")
            # source L3024
            mc "일단 같이 주워요."
            # source L3028
            darim "좋아요."
            # source L3032
            narrator "나는 근처에 떨어진 카드를 주웠다."
            # source L3036
            bambam "아, 감사합니다."
            # source L3040
            hess "저쪽은 제가 정리할게요."
            # source L3044
            ski "다들……!"
            # source L3048
            ski "경쟁 상대에게 이렇게 친절하다니!"
            # source L3052
            sia "야, 감동할 시간에 주워ㅋㅋ"
            # source L3056
            ski "이 은혜는 안 잊을게."
            # source L3060
            ski "물론 승부는 별개지만!"
            # source L3064
            hyeophap "그건 다 알고 있어."
            # source L3066: **[FLAG] rival_attitude = cooperative / rival_helped = True / trust.darim +1**
            $ story_apply("ch02_sc07_a", trust={'darim': 1}, values={'rival_attitude': 'cooperative', 'rival_helped': True})
        # source L3016
        "필요한 게 있는지 물어보자.":

            # source L3072
            mc "도와드릴 일 있어요?"
            # source L3076
            hyeophap "아, 고마워."
            # source L3078
            hyeophap "저기 문 앞에 있는 카드 몇 장만 집어주면 될 것 같아."
            # source L3082
            mc "알았어요."
            # source L3086
            hess "자료가 다른 상자랑 섞이지 않게 조심해 주세요."
            # source L3090
            mc "네."
            # source L3094
            bambam "정리가 생각보다 빨리 끝나겠네요."
            # source L3098
            ski "역시 우리 인덕이……."
            # source L3102
            hyeophap "스키, 네가 떨어뜨렸어."
            # source L3106
            ski "……그렇지."
            # source L3108: **[FLAG] rival_attitude = respectful / rival_helped = True**
            $ story_apply("ch02_sc07_b", values={'rival_attitude': 'respectful', 'rival_helped': True})
        # source L3018
        "저쪽에서 정리하는 것 같으니 우리 준비를 계속해요.":
            # source L3114
            mc "저쪽에서 정리하는 것 같으니 우리 준비를 계속해요."
            # source L3118
            sia "그래. 우리도 아직 할 거 많지."
            # source L3122
            lumi "네 명이 있으니까 금방 정리하겠네요."
            # source L3126
            narrator "우리는 복도 가장자리를 비켜 지나갔다."
            # source L3130
            ski "아, 경쟁팀 왔어!"
            # source L3134
            mc "네?"
            # source L3138
            ski "방금 본 건 잊어주면 좋겠는데!"
            # source L3142
            sia "응 아니야~ 평생 기억함!"
            # source L3146
            ski "아니, 그건 좀 곤란한데!"
            # source L3148: **[FLAG] rival_attitude = neutral / team_preparation +1**
            $ story_apply("ch02_sc07_c", values={'rival_attitude': 'neutral'}, counters={'team_preparation': 1})
    # source L3150: **[공통 복귀]**
    # source L3154
    narrator "조금 뒤 라이벌 팀의 자료 정리가 끝났다."
    $ sd_event_end(mode="normal", cast=STORY_HEROES + ["ski", "hyeophap", "hess", "bambam"])
    $ story_stage(faces={"ski": "normal"})
    # source L3156
    narrator "우연히 두 팀이 같은 복도에 모이게 됐다."
    # source L3160
    hyeophap "어쨌든 내일 발표니까 다들 준비 잘해."
    # source L3164
    darim "네. 그쪽도 잘 준비하세요."
    # source L3168
    $ story_stage(faces={"ski": "happy"})
    ski "내일은 우리 팀의 진짜 실력을 보여줄게."
    # source L3172
    sia "그래, 기대할게."
    # source L3176
    ski "어? 이렇게 쉽게 인정해 주는 거야?"
    # source L3180
    sia "응. 기대한다고 했지, 이길 거라곤 안 했거든."
    # source L3184
    ski "……말을 참 잘하네."
    # source L3188
    omu "둘이 아주 죽이 잘 맞네."
    # source L3192
    hess "말이 너무 많아서 피곤하네요."
    # source L3196
    bambam "저는 재밌는데요."
    # source L3200
    lumi "내일 발표에서도 이런 분위기면 꽤 볼 만하겠네요."
    # source L3204
    hyeophap "발표할 때는 좀 조용히 시킬게."
    # source L3208
    ski "왜 날 보는 거야?"
    # source L3210: **[SD] 모두의 시선이 스키에게 향한다.**
    # source L3214
    ski "……."
    # source L3218
    ski "알았어."
    # source L3220: **[BGM] 서서히 페이드아웃**
    stop music fadeout 0.5
    $ story_stage(cast=[])
    # source L3224
    narrator "우리는 각자의 준비실로 돌아갔다."
    # source L3226
    narrator "경쟁팀이라고 해서 무조건 불편한 사이가 되는 건 아닌 모양이다."
    # source L3228
    narrator "하지만 내일은 달랐다."
    # source L3230
    narrator "처음으로 두 팀의 기획을 공식적인 자리에서 평가받는 날이었다."
    # source L3232: **[SCENE 07 END]**
    $ sd_event_end(mode="normal", cast=[])
    jump ch02_sc08

label ch02_sc08:
    $ phone_timeline_enter("CH02", "ch02_sc08")
    # source L3236: **[BG] 교내 발표실 · 오후**
    $ story_scene("presentation", mode="normal", cast=['roman', 'sia', 'darim', 'omu', 'lumi'], light="day", location="교내 발표실 · 오후")
    # source L3238: **[BGM] Light Tension**
    $ play_bgm("light_tension")
    # source L3242
    $ cg_start("ld_05")
    narrator "다음 날."
    # source L3244
    narrator "우리는 발표 시작 시간보다 조금 일찍 발표실에 도착했다."
    # source L3246
    narrator "앞쪽에는 운영위원들이 앉아 있었고, 스크린에는 축제 부스 기획 평가라는 문구가 떠 있었다."
    # source L3250
    sia "……야."
    # source L3254
    mc "네?"
    # source L3258
    sia "나 갑자기 긴장되는데."
    # source L3262
    omu "니 어제는 1등 한다며."
    # source L3266
    sia "그건 어제의 나였고."
    # source L3270
    omu "그 논리 또 쓰네."
    # source L3274
    darim "긴장할 수 있죠. 그래도 준비한 내용만 잘 설명하면 돼요."
    # source L3278
    roman "앗,,, 저도 조금 떨려요……."
    # source L3282
    lumi "괜찮아요. 연습한 대로 하면 되니까."
    # source L3286
    mc "우리 다 같이 준비했잖아요."
    # source L3290
    sia "오. 방금 좀 주인공 같은 말 했다."
    # source L3294
    mc "……제가 주인공이 아니면 누가 주인공인데요?"
    # source L3298
    sia "내 인생의 주인공은 나지."
    # source L3302
    omu "갑자기 좋은 말이네."
    # source L3306
    sia "그치?"
    # source L3310
    narrator "긴장이 조금 풀렸다."
    $ story_sfx("door_open")  # source L3312
    narrator "그때 발표실 문이 열렸다."
    $ story_stage(mode="normal", cast=["roman", "sia", "darim", "omu", "lumi"])  # source L3316
    ski "안녕!"
    # source L3318
    ski "오늘의 주인공이 왔어!"
    # source L3322
    sia "아, 또 한 명 왔네."
    # source L3326
    hyeophap "스키, 발표실에서는 조용히 해."
    # source L3330
    ski "응. 오늘은 진지하게 할게."
    # source L3334
    hess "그 말이 제일 안 믿기네요."
    # source L3338
    bambam "그래도 연습 많이 했잖아요."
    # source L3342
    ski "역시 밤밤밖에 없어!"
    # source L3346
    hyeophap "발표 자료부터 열어."
    # source L3348: **[SFX] 마이크 켜지는 소리**
    $ story_sfx("message")
    # source L3352
    staff "그럼 첫 번째 팀의 발표를 시작하겠습니다."
    # source L3354: **[BGM] Presentation Tension**
    $ play_bgm("light_tension")
    # source L3358: 라이벌 팀 발표.
    $ story_scene("presentation", mode="normal", cast=["ski", "hyeophap", "hess", "bambam"], light="day", location="교내 발표실 · 라이벌 팀 발표")
    $ story_stage(faces={"ski": "happy", "hess": "serious", "hyeophap": "serious"})  # source L3362
    ski "안녕!"
    # source L3364
    ski "다들 하루를 달콤하게 바꿔줄 스키야!"
    # source L3368
    narrator "스키는 시작부터 지나치게 당당했다."
    # source L3372
    ski "다들, 행복이 뭘까?"
    # source L3376
    hess "……발표 주제는 디저트 부스예요."
    # source L3380
    ski "잠깐만. 지금 분위기 잡는 중인데."
    # source L3384
    hyeophap "제한시간 5분."
    $ story_stage(faces={"ski": "embarrassed"})  # source L3388
    ski "……그럼 바로 본론으로 갈게."
    # source L3392
    narrator "청중 사이에서 웃음이 흘러나왔다."
    # source L3394
    narrator "하지만 발표가 시작되자 내용은 생각보다 진지했다."
    # source L3398
    hess "저희는 방문객이 간단한 질문에 답하며 자신의 기분을 돌아볼 수 있는 체험을 준비했습니다."
    # source L3400
    hess "다만 전문적인 심리검사나 진단은 아닙니다."
    # source L3404
    bambam "선택한 카드에 맞춰 디저트와 짧은 메시지를 제공할 예정이에요."
    # source L3406
    bambam "오래 머물지 않아도 편하게 즐길 수 있도록 구성했습니다."
    # source L3410
    hyeophap "운영 측면에서는 예상 대기시간과 재료 소요량을 고려했습니다."
    # source L3412
    hyeophap "알레르기 안내와 보관 조건도 함께 준비하고 있습니다."
    $ story_stage(faces={"ski": "happy"})  # source L3416
    ski "그리고 그 모든 경험을 완성할 디저트!"
    # source L3418
    ski "그건 바로 우리가 직접……."
    # source L3422
    hyeophap "스키, 마지막 슬라이드."
    # source L3426
    ski "응!"
    # source L3430
    ski "……우리 팀이 정성껏 준비할게!"
    # source L3434
    narrator "웃기는 장면도 있었지만 기획 자체는 꽤 탄탄했다."
    # source L3436
    narrator "운영위원들도 몇 가지 질문을 한 뒤 고개를 끄덕였다."
    # source L3440
    staff "수고하셨습니다. 다음 팀 준비해 주세요."
    # 같은 발표실에서 우리 팀의 발표를 시작합니다.
    $ story_scene("presentation", mode="normal", cast=["roman", "sia", "darim", "omu", "lumi"], light="day", location="교내 발표실 · 우리 팀 발표")
    # source L3446: **[BGM] Hopeful Presentation**
    $ play_bgm("hopeful_teamwork")
    # source L3450
    narrator "우리 차례였다."
    # source L3452
    narrator "나는 준비한 자료를 다시 한번 확인했다."
    # source L3456
    darim "준비됐죠?"
    # source L3460
    mc "네."
    # source L3464
    darim "그럼 시작해 봐요."
    # source L3468
    narrator "나는 마이크 앞에 섰다."
    # source L3472
    mc "안녕하세요."
    # source L3474
    mc "저희는 '우리 대학의 하루를 기록하는 체험 전시'를 준비하고 있습니다."
    # source L3476
    mc "대학생활에는 특별한 순간도 있지만, 평범해서 그냥 지나치는 순간도 많다고 생각합니다."
    # source L3478
    mc "저희는 그런 순간을 여러 방식으로 남길 수 있는 공간을 만들고 싶었습니다."
    # source L3482
    roman "앗,,, 방문객은 준비된 질문 중 하나를 고르고……."
    # source L3484
    roman "그 질문에 대한 자신의 이야기를 짧은 문장으로 남길 수 있어요."
    # source L3488
    sia "글로 쓰는 게 어렵다면 그림으로 남겨도 됩니다."
    # source L3490
    sia "참여 방법은 제가 만든 안내 만화로 쉽게 확인할 수 있고요."
    # source L3494
    darim "참여 절차는 복잡하지 않도록 정리했습니다."
    # source L3496
    darim "짧은 시간에도 참여할 수 있는 방식으로 준비하고 있습니다."
    # source L3500
    omu "전시에는 캠퍼스 사진도 함께 넣을 예정입니다."
    # source L3502
    omu "평범한 장소도 사람마다 기억이 다르니까요."
    # source L3506
    lumi "공간은 동선을 따라 자연스럽게 이동할 수 있도록 구성했습니다."
    # source L3508
    lumi "작은 부스에서도 전시를 충분히 감상할 수 있도록 수정하고 있습니다."
    # source L3512
    narrator "우리는 준비한 내용을 차례대로 설명했다."
    # source L3514
    narrator "처음 회의할 때만 해도 각자 다른 이야기를 하던 사람들이었다."
    # source L3516
    narrator "그런데 지금은 서로의 말이 하나의 기획으로 이어지고 있었다."
    # source L3518: **[SFX] 발표 종료 안내음**
    $ story_sfx("message")
    # source L3522
    staff "발표 잘 들었습니다."
    # source L3524
    staff "한 가지 질문하겠습니다."
    # source L3528
    narrator "운영위원 한 사람이 자료를 내려다봤다."
    # source L3532
    staff "이 전시는 방문객의 직접 참여가 중요한 구조로 보이는데요."
    # source L3534
    staff "참여자가 적거나 글을 쓰고 싶어 하지 않는 경우에는 어떻게 운영할 계획인가요?"
    # source L3538
    narrator "순간 발표실이 조금 조용해졌다."
    # source L3540
    narrator "확실히 중요한 질문이었다."
    # source L3542
    narrator "나는 팀원들이 준비한 자료를 떠올렸다."
    menu:
        # source L3546
        "팀원들의 예시 작품을 먼저 전시하겠습니다.":
            # source L3556
            mc "팀원들이 직접 만든 예시 작품을 먼저 전시하겠습니다."
            # source L3558
            mc "참여자가 없어도 전시 자체를 감상할 수 있도록 준비하겠습니다."
            # source L3562
            roman "앗,,, 그리고 예시를 보시면 어떤 내용을 적어야 할지 조금 더 편하게 생각하실 수 있을 것 같아요."
            # source L3566
            staff "좋습니다. 관람만 하는 방식도 고려해 보세요."
            # source L3568: **[FLAG] pitch_strategy = sample / exhibition_quality +1**
            $ story_apply("ch02_sc08_a", values={'pitch_strategy': 'sample'}, counters={'exhibition_quality': 1})
        # source L3548
        "참여 절차를 더 간단하게 만들겠습니다.":
            # source L3574
            mc "참여 절차를 더 간단하게 만들겠습니다."
            # source L3576
            mc "긴 글 대신 짧은 단어나 스티커 선택으로도 참여할 수 있도록 하겠습니다."
            # source L3580
            darim "네. 부담 없이 참여할 수 있는 방식으로 운영 계획을 보완하겠습니다."
            # source L3584
            staff "그렇게 하면 접근성이 좋아지겠네요."
            # source L3586: **[FLAG] pitch_strategy = simple / team_preparation +1**
            $ story_apply("ch02_sc08_b", values={'pitch_strategy': 'simple'}, counters={'team_preparation': 1})
        # source L3550
        "방문객이 쉽게 이해할 안내물을 강화하겠습니다.":
            # source L3592
            mc "방문객이 체험 과정을 바로 이해할 수 있도록 안내물을 강화하겠습니다."
            # source L3594
            mc "입구에서 간단한 그림 안내를 볼 수 있게 준비하겠습니다."
            # source L3598
            sia "네! 제가 안내 만화를 더 간단하게 수정해 보겠습니다."
            # source L3602
            staff "좋습니다. 다만 안내물 자체가 너무 복잡하지 않도록 해주세요."
            # source L3604: **[FLAG] pitch_strategy = guide / promotion_quality +1**
            $ story_apply("ch02_sc08_c", values={'pitch_strategy': 'guide'}, counters={'promotion_quality': 1})
    # source L3606: **[공통 복귀]**
    # source L3610
    staff "두 팀 모두 흥미로운 기획을 준비해 주셨습니다."
    # source L3612
    staff "오늘 발표 결과만으로 최종 우선 배정팀을 결정하지는 않습니다."
    # source L3614
    staff "이후 시범 운영 결과까지 종합해 평가할 예정입니다."
    # source L3618
    narrator "아직 승패가 정해진 것은 아니었다."
    # source L3620
    narrator "하지만 적어도 오늘 발표를 망치지는 않은 것 같다."
    # source L3622: **[BG] 발표실 복도**
    $ story_scene("corridor", mode="normal", cast=["roman", "sia", "darim", "omu", "lumi"], light="day", location="발표실 복도")
    # source L3624: **[BGM] Relief**
    $ play_bgm("hopeful_teamwork")
    # source L3628
    $ sd_event_start("ch02_presentation_release")
    sia "와아아, 끝났다!"
    # source L3632
    omu "니 발표할 때 진짜 긴장했더라."
    # source L3636
    sia "응 아니야~ 나 완전 여유로웠는데?"
    # source L3640
    lumi "손에 쥔 종이가 조금 구겨졌던데요."
    # source L3644
    sia "그건 종이가 약한 거지."
    # source L3648
    darim "후후. 그래도 다들 잘했어요."
    # source L3652
    roman "앗,,, 저도 생각보다 덜 떨렸어요……!"
    # source L3656
    mc "다 같이 준비한 보람이 있네요."
    # source L3660
    narrator "아직 할 일은 많이 남았지만, 적어도 한 걸음은 앞으로 나아간 기분이었다."
    # source L3662: **[SCENE 08 END]**
    jump ch02_sc09

label ch02_sc09:
    $ phone_timeline_enter("CH02", "ch02_sc09")
    # source L3666: **[BG] 캠퍼스 광장 · 저녁**
    $ story_scene("booth", mode="normal", cast=['roman', 'sia', 'darim', 'omu', 'lumi'], light="evening", location="캠퍼스 광장 · 저녁")
    # source L3668: **[BGM] Warm Evening**
    $ play_bgm("evening_warm")
    # source L3672
    narrator "발표를 마치고 학생회관 밖으로 나왔다."
    # source L3674
    narrator "늦은 오후의 햇빛이 건물 사이로 길게 드리워져 있었다."
    # source L3678
    sia "아, 배고파."
    # source L3682
    omu "니 아까도 먹었잖아."
    # source L3686
    sia "발표했잖아. 에너지 소모 심했다고."
    # source L3690
    darim "그럼 다 같이 저녁이라도 먹을까요?"
    # source L3694
    roman "앗,,, 좋아요……!"
    # source L3698
    lumi "저도 괜찮아요."
    # source L3702
    mc "그럼 어디로 갈까요?"
    # source L3706
    unknown_voice "잠깐만요!"
    # source L3710
    narrator "익숙한 목소리였다."
    # source L3712
    narrator "돌아보지 않아도 누군지 알 것 같았다."
    $ story_enter("ski", side="right", face="happy")
    # source L3716
    ski "다들! 발표 잘했어!"
    # source L3720
    sia "오, 웬일로 정상적인 말을 하네?"
    # source L3724
    ski "나 원래 정상적인 사람이야."
    # source L3728
    omu "그건 좀 아닌 것 같은데."
    # source L3732
    ski "……오늘 나한테 꽤 냉정하네."
    $ story_enter("hyeophap", side="right", face="serious")  # source L3736
    hyeophap "칭찬하려고 왔으면 제대로 해."
    # source L3740
    ski "알았어."
    # source L3744
    ski "솔직히 말할게."
    # source L3748
    narrator "스키는 잠시 우리를 둘러봤다."
    # source L3752
    ski "너희 발표, 생각보다 훨씬 괜찮았어."
    # source L3756
    sia "오."
    # source L3760
    ski "특히 여러 콘텐츠를 하나의 전시로 연결한 게 좋았어."
    # source L3764
    lumi "그건 고맙네요."
    # source L3768
    ski "물론 우리도 훌륭했지만."
    $ sd_event_start("ch02_rival_after_presentation", variant="02")  # source L3772
    sia "아, 결국 거기로 가네ㅋㅋ"
    # source L3776
    hyeophap "그래도 저쪽 기획도 장점이 분명하더라."
    # source L3780
    darim "저희도 라이벌 팀의 운영 계획에서 배울 점이 많았어요."
    # source L3784
    hess "양쪽 다 개선할 부분은 있어요."
    # source L3788
    sia "우리도?"
    # source L3792
    hess "네."
    # source L3796
    hess "저희도요."
    # source L3800
    bambam "그래도 재미있었어요. 다른 팀이랑 경쟁해 보니까."
    # source L3804
    roman "앗,,, 저도 조금 긴장됐지만…… 좋은 경험이었어요."
    # source L3808
    ski "좋아!"
    # source L3810
    ski "다음에는 우리가 압도적인 실력을 보여줄게!"
    # source L3814
    hyeophap "일단 오늘 받은 피드백부터 정리해."
    # source L3818
    ski "……응."
    # source L3822
    omu "와, 진짜 말 잘 듣네."
    # source L3826
    sia "스키야, 너 협합한테 약점 잡혔냐?"
    # source L3830
    ski "아니야!"
    # source L3832
    ski "이건 서로에 대한 깊은 신뢰를 바탕으로 한……."
    # source L3836
    hyeophap "내일 오전까지 수정안 보내."
    # source L3840
    ski "알았어!"
    # source L3844
    sia "ㅋㅋㅋㅋㅋㅋ"
    # source L3848
    narrator "결국 우리는 또 한참을 웃었다."
    # source L3850
    narrator "조금 전까지 경쟁 상대였다는 사실이 이상하게 느껴질 정도였다."
    # source L3852
    narrator "하지만 다음 평가에서는 다시 경쟁해야 한다."
    # source L3856
    hyeophap "그럼 다음에 봐."
    # source L3860
    darim "네. 수고하셨어요."
    # source L3864
    bambam "다음에 또 봬요."
    # source L3868
    hess "수고하셨습니다."
    # source L3872
    ski "그럼 다들, 오늘의 패배를 너무 슬퍼하지 말고……."
    # source L3876
    sia "아직 안 졌거든?"
    # source L3880
    ski "아, 그렇구나."
    # source L3882
    ski "그럼 미래의 패배를……."
    # source L3886
    hyeophap "가자."
    # source L3890

    ski "……응."
    # source L3892: **[SD] 협합이 스키를 데리고 화면 밖으로 퇴장. 시아는 웃음, 헤스는 무표정, 밤밤은 미소.**
    $ sd_event_end(mode="normal", cast=[])
    # 장소 전환은 story_scene에서 처리합니다.

    # source L3898: **[BG] 주인공 방 · 밤**
    $ story_scene("room", mode="normal", cast=[], light="night", location="주인공 방 · 밤")
    # source L3900: **[BGM] Night Campus**
    $ play_bgm("night_campus")
    # source L3904
    narrator "방으로 돌아와 짐을 내려놓았다."
    # source L3906
    narrator "하루 종일 움직였더니 몸이 무거웠다."
    # source L3910
    mc "……오늘도 길었다."
    # source L3914
    narrator "처음에는 그저 축제 준비를 조금 도와볼 생각이었다."
    # source L3916
    narrator "그런데 어느새 기획 발표에 경쟁팀까지 생겼다."
    # source L3918
    narrator "생각보다 일이 커졌다."
    # source L3920: **[SFX] 휴대전화 알림**
    # 알림음은 휴대폰 이벤트 시작에 재생.
    # source L3922: **[UI] 개인 메시지**
    if ch02_partner == "roman":
        $ story_chat(True, title="로만")
        # source L3930
        roman "앗,,, 오늘 발표할 때 조금 떨렸는데요……."
        # source L3932
        roman "같이 준비한 질문 카드가 도움이 된 것 같아요."
        # source L3936
        mc "로만이 만든 문구 좋았어요."
        # source L3940
        roman "정말요……?"
        # source L3942
        roman "그럼 다음에도 같이 만들어 주실래요?"
        # source L3946
        mc "좋아요."
        # source L3950
        roman "앗,,, 감사합니다……!"
        $ story_chat(False)
    elif ch02_partner == "sia":
        $ story_chat(True, title="시아")
        # source L3956
        sia "야ㅋㅋ 오늘 우리 발표 좀 잘하지 않았냐"
        # source L3960
        mc "네. 시아 씨 만화도 잘 나왔고요."
        # source L3964
        sia "그치?"
        # source L3966
        sia "역시 천재 작가 시아"
        # source L3970
        mc "그런데 다음 콘티는 언제 만들어요?"
        # source L3974
        sia "……"
        # source L3976
        sia "그건 내일의 시아가 해결할 문제다"
        # source L3980
        mc "그 논리 자주 쓰네요."
        # source L3984
        sia "응 아니야~"
        $ story_chat(False)
    elif ch02_partner == "darim":
        $ story_chat(True, title="다림")
        # source L3990
        darim "오늘 수고 많으셨어요."
        # source L3992
        darim "발표 준비할 때 같이 도와주셔서 감사했어요."
        # source L3996
        mc "저도 선배 덕분에 편하게 준비했어요."
        # source L4000
        darim "후후. 서로 도운 거네요."
        # source L4002
        darim "다음에는 일정도 조금 더 여유롭게 잡아봐요."
        # source L4006
        mc "좋아요."
        # source L4010
        darim "그럼 다음에 또 봬요. 좋은 밤 보내세요."
        $ story_chat(False)
    elif ch02_partner == "omu":
        $ story_chat(True, title="오므")
        # source L4016
        omu "오늘 사진 몇 장 찍었는데 잘 나왔다"
        # source L4020
        mc "발표 사진이요?"
        # source L4024
        omu "어"
        # source L4026
        omu "니도 나온 건 있는데 얼굴은 안 나오게 찍었다"
        # source L4030
        mc "잘 나왔어요?"
        # source L4034
        omu "그건 나중에 보여줄게ㅋㅋ"
        # source L4036
        omu "오늘 고생했다"
        # source L4040
        mc "오므 씨도요."
        $ story_chat(False)
    elif ch02_partner in ("lumi", "rumi"):
        $ story_chat(True, title="하린")
        # source L4046
        lumi "오늘 발표 나쁘지 않았어요."
        # source L4048
        lumi "특히 마지막 답변은 꽤 인상적이었네."
        # source L4052
        mc "다 같이 준비한 덕분이죠."
        # source L4056
        lumi "그건 맞죠."
        # source L4058
        lumi "그래도 본인이 잘한 건 인정하셔도 되는데."
        # source L4062
        mc "그럼 잘했다고 해둘게요."
        # source L4066
        lumi "후후. 그렇게 나와야죠."
        # source L4068
        lumi "내일 봐요."
        $ story_chat(False)
    # source L4070: **[공통 복귀]**
    # source L4072: **[UI] 스마트폰 화면 종료**
    $ story_chat(False)
    # source L4076
    narrator "휴대전화를 내려놓고 침대에 누웠다."
    # source L4078
    narrator "경쟁팀은 생각보다 잘 준비된 사람들이었다."
    # source L4080
    narrator "우리도 부족한 부분이 많았다."
    # source L4082
    narrator "그래도 이상하게 불안하기보다는 기대가 됐다."
    # source L4086
    mc "……다음에는 더 잘할 수 있겠지."
    # source L4088: **[SFX] 시스템 알림**
    # 알림음은 휴대폰 이벤트 시작에 재생.
    $ story_chat(True, title="축제 운영위원회")  # source L4090
    system_note "「축제 운영위원회 공지」"
    # source L4092
    system_note "「중간 기획 발표에 참여해 주셔서 감사합니다.」"
    # source L4094
    system_note "「최종 평가 전, 각 팀은 시범 운영을 진행해야 합니다.」"
    # source L4096
    system_note "「방문객의 체험 결과와 개선 사항을 제출해 주세요.」"
    $ story_chat(False)  # source L4100
    mc "……시범 운영?"
    # source L4104
    narrator "그렇다."
    # source L4106
    narrator "축제 준비는 아직 시작에 불과했다."
    # source L4110
    mc "……내 공강은 대체 어디로 간 거지?"
    # source L4112: **[FADE TO BLACK]**
    $ story_fade_out()
    scene black
    with fade
    # source L4114: **[BGM] CH02 Ending Theme**
    $ play_bgm("chapter_ending_reprise")
    # source L4116
    system_note "「CHAPTER 02 COMPLETE」"
    # source L4118
    system_note "「다음 이야기」"
    # source L4120
    system_note "「시범 운영부터 사고라고?」"
    # source L4122: **[FLAG] chapter02_complete = True**
    # source L4124: **[CHAPTER 02 END]**
    $ story_chat(False)
    $ story_complete_chapter(2)
    jump chapter03
