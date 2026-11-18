# 공식 CH01 원문 전체를 정적 Ren'Py 문장으로 옮긴 신규 진입 경로.
# 재생 중 원문 파일이나 Python 변환기에 의존하지 않습니다.
# 기존 routes/ch01.rpy는 레거시 세이브를 위해 그대로 유지합니다.

label chapter01:
    $ phone_timeline_enter("CH01", "chapter01")
    $ story_begin_chapter(1, "이 조합으로 축제가 가능해?")
    jump ch01_sc01

# SC01 · 모집 공고 / 원문 29행
label ch01_sc01:
    $ phone_timeline_enter("CH01", "ch01_sc01")
    # 원문 연출: [BG] 캠퍼스 산책로 · 맑은 낮
    $ sd_event_end(mode="normal", cast=[])
    scene black
    with None
    $ story_scene("campus", mode="normal", cast=[], light="day", location="캠퍼스 산책로 · 맑은 낮")
    # 원문 연출: [BGM] Daily Campus · 밝고 편안한 피아노
    $ play_bgm("campus_day")
    # 새 게임에서는 첫 대사 전에 검은 화면 뒤로 캠퍼스가 밝아진다.
    with Fade(0.0, 0.04, 0.46)
    # 원문 39행
    narrator "평범한 대학생활."
    # 원문 41행
    narrator "아침에 일어나 강의실에 들어가고, 교수님의 말씀을 듣고, 과제를 제출한다."
    # 원문 43행
    narrator "그러다 배가 고프면 밥을 먹고, 피곤해지면 카페에 들르고, 다시 강의실로 돌아간다."
    # 원문 45행
    narrator "놀랍게도 이 모든 일은 매일 반복된다."
    # 원문 49행
    mc "……재미없네."
    # 원문 53행
    narrator "물론 특별히 불만이 있는 건 아니다."
    # 원문 55행
    narrator "그저 오늘이 어제와 별다를 바 없고, 내일도 오늘과 크게 다르지 않을 것 같을 뿐."
    # 원문 59행
    mc "이러다 졸업할 때까지 학교랑 기숙사만 왔다 갔다 하겠는데."
    # 원문 연출: [SFX] 휴대전화 진동
    # 알림음은 휴대폰 이벤트 시작에 재생.
    # 원문 65행
    $ story_chat(True, title="학사 알림")
    system_note "「오늘 예정된 강의가 모두 종료되었습니다.」"
    $ story_chat(False)
    # 원문 69행
    mc "……오."
    # 원문 73행
    narrator "좋은 소식이다."
    # 원문 75행
    narrator "오늘은 예상보다 빨리 자유의 몸이 되었다."
    # 원문 77행
    narrator "문제는 자유로워진 다음에 뭘 해야 할지 모르겠다는 점이지만."
    # 원문 81행
    mc "그냥 돌아갈까."
    # 원문 연출: [BG] 학생회관 앞 게시판
    $ sd_event_end(mode="normal", cast=[])
    $ story_scene("board", mode="normal", cast=[], light="day", location="학생회관 앞 게시판")
    # 원문 87행
    narrator "그렇게 발길을 돌리려던 순간, 게시판에 붙은 종이 한 장이 눈에 들어왔다."
    # 원문 89행
    narrator "커다란 글씨로 쓰여 있는 문구."
    # 원문 91행
    narrator "「축제 연합 프로젝트 추가 팀원 모집!」"
    # 원문 93행
    show screen campus_recruitment_notice
    narrator "「전공 무관! 경험 무관!」"
    # 원문 95행
    narrator "「새로운 사람 환영!」"
    # 원문 97행
    narrator "「함께 대학 축제를 만들어 갈 분을 찾습니다!」"
    hide screen campus_recruitment_notice
    # 원문 101행
    mc "축제……?"
    # 원문 105행
    narrator "그러고 보니 얼마 전부터 학교 곳곳에 축제 포스터가 붙기 시작했다."
    # 원문 107행
    narrator "아직 한참 남았다고 생각했는데 벌써 준비 기간인가 보다."
    # 원문 111행
    mc "전공도 상관없고, 경험도 상관없다라……."
    # 원문 115행
    narrator "공지 아래쪽에는 작은 글씨가 하나 더 적혀 있었다."
    # 원문 117행
    narrator "「※ 정상적인 소통이 가능한 분을 찾습니다.」"
    # 원문 121행
    mc "……?"
    # 원문 123행
    mc "굳이 저걸 적어야 할 이유가 있나?"
    # 원문 127행
    # 기존 저장에서 작은 글씨까지 표시 중이었다면 이 지점에서 닫는다.
    hide screen campus_recruitment_notice
    narrator "뭔가 이상하다."
    # 원문 129행
    narrator "그런데 왜인지 조금 궁금해졌다."
    # 원문 133행
    mc "뭐, 해봐서 나쁠 건 없겠지."
    # 원문 선택지: 참여 동기
    menu:
        "새로운 사람도 좀 만나보고 싶고.":
            # 원문 147행
            mc "맨날 똑같은 사람들만 만나니까."
            # 원문 149행
            mc "가끔은 새로운 사람들이랑 어울리는 것도 괜찮겠지."
            $ story_apply("ch01_sc01_motivation_a")
        "대학생활에 추억 하나쯤은 있어야지.":
            # 원문 155행
            mc "나중에 대학생활에서 기억나는 게 시험이랑 과제뿐이면 좀 억울하잖아."
            $ story_apply("ch01_sc01_motivation_b")
        "재미있는 일이 생길지도 모르잖아.":
            # 원문 161행
            mc "어차피 할 일도 없는데."
            # 원문 163행
            mc "설마 축제 준비가 그렇게 힘들겠어?"
            $ story_apply("ch01_sc01_motivation_c")

    # 원문 169행
    narrator "나는 모집 공고에 적힌 QR 코드를 스캔했다."
    # 원문 171행
    narrator "화면에는 간단한 참가 신청서가 나타났다."
    # 원문 연출: [UI] 이름 입력 화면
    # 원문 연출: [INPUT] player_name
    call application_name_input
    $ player_name = _return
    # 원문 181행
    system_note "「신청이 완료되었습니다.」"
    # 원문 연출: [SFX] 메시지 알림
    # 알림음은 휴대폰 이벤트 시작에 재생.
    $ story_chat(True, title="축제 연합 프로젝트")  # 원문 187행
    system_note "안녕하세요! 축제 연합 프로젝트에 지원해 주셔서 감사합니다."
    # 원문 189행
    system_note "오늘 오후 2시, 학생회관 3층 공동 동아리실에서 첫 모임이 진행됩니다."
    # 원문 191행
    system_note "늦지 않게 참석해 주세요!"
    $ story_chat(False)  # 원문 195행
    mc "……오늘?"
    # 원문 199행
    narrator "신청하자마자 모임이라니."
    # 원문 201행
    narrator "일 처리가 굉장히 빠른 팀인가 보다."
    # 원문 205행
    mc "뭐, 시간은 충분하니까."
    # 원문 209행
    narrator "나는 휴대전화를 주머니에 넣었다."
    # 원문 211행
    narrator "이때까지만 해도 몰랐다."
    # 원문 213행
    narrator "앞으로의 대학생활이 얼마나 시끄러워질지."
    # 복도로 이동할 때 이전 장소와 바로 이어서 슬라이드한다.



    # 원문 연출: [SCENE 01 END]
    jump ch01_sc02

# SC02 · 처음 온 사람 / 원문 219행
label ch01_sc02:
    $ phone_timeline_enter("CH01", "ch01_sc02")
    # 원문 연출: [BG] 학생회관 3층 복도
    $ sd_event_end(mode="normal", cast=[])
    $ story_scene("corridor", mode="normal", cast=[], light="day", location="학생회관 3층 복도")
    # 원문 연출: [BGM] Light Comedy
    $ play_bgm("comedy_light")
    # 원문 227행
    narrator "학생회관 3층."
    # 원문 229행
    narrator "안내 메시지에는 공동 동아리실이라고 적혀 있었지만, 막상 와보니 비슷한 문이 여러 개였다."
    # 원문 233행
    mc "301호…… 302호……."
    # 원문 235행
    mc "근데 왜 여긴 305호 다음이 307호야?"
    # 원문 239행
    narrator "건물 구조부터 정상이 아닌 것 같다."
    # 원문 241행
    narrator "그때 복도 끝에서 누군가의 목소리가 들렸다."
    # 시아의 첫 대사와 함께 복도 끝에 두 사람이 보인다.
    $ story_stage_fade_in(["sia", "omu"])
    # 원문 247행
    sia "아니, 내가 언제 그랬는데?"
    # 원문 연출: [SPRITE] 오므 등장 · 무표정
    $ story_stage(faces={"omu": "normal"})
    # 원문 253행
    omu "니 어제 그랬다 아이가."
    # 원문 257행
    $ story_stage(faces={"sia": "smug"})
    sia "응 아니야~ 증거 있어?"
    # 원문 261행
    omu "단톡방에 니가 직접 썼다."
    # 원문 265행
    $ story_stage(faces={"sia": "embarrassed"})
    sia "……."
    # 원문 267행
    sia "그건 어제의 나잖아."
    # 원문 271행
    $ story_stage(faces={"omu": "confused"})
    omu "뭐?"
    # 원문 275행
    $ story_stage(faces={"sia": "smug"})
    sia "오늘의 나는 새로운 사람이거든."
    # 원문 279행
    omu "아, 진짜 뭔 소리고."
    # 원문 연출: [SD] 시아가 자신만만하게 팔짱을 끼고, 오므가 어이없다는 표정을 짓는다.
    $ sd_event_start("ch01_sia_omu_argument", variant="01")
    # 원문 285행
    narrator "복도 한복판에서 이상한 논쟁을 벌이는 두 사람."
    # 원문 287행
    narrator "한 사람은 지나치게 당당했고, 다른 한 사람은 이미 익숙하다는 듯 받아치고 있었다."
    # 원문 289행
    narrator "아마 오래 알고 지낸 사이겠지."
    # 원문 291행
    narrator "나는 조심스럽게 말을 걸었다."
    # 원문 295행
    mc "저기, 혹시 축제 프로젝트 모임이 여기인가요?"
    # 원문 299행
    sia "어?"
    # 원문 연출: [SPRITE] 시아 · 흥미
    # 복도의 SD는 첫 컷을 계속 사용한다.
    # 원문 305행
    sia "야, 오므야. 신입이다."
    # 원문 309행
    omu "신입은 무슨. 니도 이번에 들어왔잖아."
    # 원문 313행
    sia "내가 5분 먼저 왔으니까 선배지."
    # 원문 317행
    omu "5분 선배님, 그럼 문이나 좀 열어보이소."
    # 원문 321행
    sia "말투 왜 이렇게 공격적이야?"
    # 원문 325행
    omu "내 서울말 쓰는데?"
    # 원문 329행
    mc "……서울말이요?"
    # 원문 333행
    sia "ㅋㅋㅋㅋ 너도 이상하지?"
    # 원문 337행
    omu "뭐가 이상한데."
    # 원문 341행
    sia "아냐. 그래. 네가 서울말 쓰면 서울말이지."
    # 원문 345행
    narrator "시아라고 불린 사람은 고개를 돌려 나를 바라봤다."
    # 원문 349행
    sia "근데 넌 누구야? 오늘 새로 오는 사람?"
    # 원문 353행
    mc "네. 모집 공고 보고 신청했어요."
    # 원문 357행
    sia "오, 잘 왔다."
    # 원문 359행
    sia "너 혹시 그림 좀 그려?"
    # 원문 363행
    mc "잘 못 그리는데요."
    # 원문 367행
    sia "영상 편집은?"
    # 원문 371행
    mc "그것도 별로요."
    # 원문 375행
    sia "웹툰은?"
    # 원문 379행
    mc "읽는 건 잘해요."
    # 원문 연출: [SD] 시아의 머리 위에 전구 아이콘 등장

    # 원문 385행
    sia "합격."
    # 원문 389행
    mc "……뭐가요?"
    # 원문 393행
    sia "내 작품 감상 담당."
    # 원문 397행
    omu "니 또 사람 이상한 데 쓰지 마라."
    # 원문 401행
    sia "왜. 감상평도 창작에 중요하거든?"
    # 원문 405행
    omu "아직 작품도 없잖아."
    # 원문 409행
    sia "그건 앞으로 만들면 되지."
    # 원문 413행
    mc "잠깐만요. 전 아직 뭘 하는지도 못 들었는데요?"
    # 원문 417행
    sia "그럼 지금부터 알면 되겠네."
    # 원문 421행
    omu "일단 들어가자. 여기서 계속 떠들 끼가?"
    # 원문 425행
    sia "아, 재미있었는데."
    # 원문 선택지: 첫인상
    menu:
        "그럼 감상료는 얼마 주는데요?":
            # 원문 439행
            mc "그럼 감상료는 얼마 주는데요?"
            # 원문 443행
            sia "……뭐?"
            # 원문 447행
            mc "제가 작품을 봐주면 돈은 줘야 하는 거 아니에요?"
            # 원문 451행
            sia "푸하하! 너도 좀 치네?"
            # 원문 453행
            sia "좋아. 감상료는……."
            # 원문 457행
            sia "내가 그린 그림을 제일 먼저 볼 수 있는 영광!"
            # 원문 461행
            mc "그게 무슨 감상료예요."
            # 원문 465행
            omu "둘이 잘 맞네."
            $ story_apply("ch01_sc02_a", affection={'sia': 1})
        "원래 다들 이런 분위기예요?":
            # 원문 473행
            mc "원래 다들 이런 분위기예요?"
            # 원문 477행
            omu "아이다. 쟤만 저런다."
            # 원문 481행
            sia "야, 배신하냐?"
            # 원문 485행
            omu "팩트잖아."
            # 원문 489행
            sia "너 고등학교 때부터 나한테 왜 이러냐?"
            # 원문 493행
            omu "니가 고등학교 때부터 저랬으니까."
            # 원문 497행
            mc "아, 두 분 고등학교 친구예요?"
            # 원문 501행
            sia "응. 무려 나의 흑역사를 전부 알고 있는 위험인물."
            # 원문 505행
            omu "아직 안 푼 거 많다."
            # 원문 509행
            sia "……야, 잠깐."
            $ story_apply("ch01_sc02_b", affection={'omu': 1})
        "그래서 모임 장소는 어디예요?":
            # 원문 517행
            mc "그래서 모임 장소는 어디예요?"
            # 원문 521행
            omu "아, 저기 안쪽이다. 같이 가자."
            # 원문 525행
            sia "뭐야. 너무 정상적인 반응인데?"
            # 원문 529행
            mc "회의하러 왔으니까요."
            # 원문 533행
            sia "……이 사람, 생각보다 쉽지 않겠는데."
            # 원문 537행
            omu "니 장난이 안 먹히는 거겠지."
            $ story_apply("ch01_sc02_c", trust={'omu': 1})

    # 원문 연출: [BG] 동아리실 앞 복도
    $ sd_event_end(mode="normal", cast=["sia", "omu"])
    $ story_scene("corridor", mode="normal", cast=["sia", "omu"], light="day", location="동아리실 앞 복도")
    # 원문 547행
    $ story_stage(faces={"sia": "happy", "omu": "normal"})
    sia "아무튼 잘 부탁해. 난 시아."
    # 원문 549행
    sia "애니메이션과 2학년."
    # 원문 553행
    omu "나는 오므. 사회복지학과 2학년."
    # 원문 557행
    mc "저는 [player_name]이에요. 잘 부탁해요."
    # 원문 561행
    sia "오케이, [player_name]."
    # 원문 565행
    omu "들어가자. 다른 사람들 기다리겠다."
    # 원문 569행
    narrator "두 사람을 따라 문 앞에 섰다."
    # 원문 571행
    narrator "그때는 아직 몰랐다."
    # 원문 573행
    narrator "이 둘은 앞으로도 자주 이런 식으로 대화할 거라는 사실을."
    # 원문 연출: [SCENE 02 END]
    jump ch01_sc03

# SC03 · 앗,,, 여기 맞나요? / 원문 577행
label ch01_sc03:
    $ phone_timeline_enter("CH01", "ch01_sc03")
    # 원문 연출: [BG] 공동 동아리실 · 오후 햇살
    $ sd_event_end(mode="normal", cast=[])
    $ story_scene("clubroom307", mode="normal", cast=[], light="day", location="동아리실 307호 · 오후")
    # 원문 연출: [BGM] Warm Daily
    $ play_bgm("campus_day")
    # 원문 연출: [SFX] 문 열리는 소리
    $ story_sfx("door_open")
    # 원문 587행

    narrator "문을 열자 조용한 동아리실이 나타났다."
    # 원문 589행
    narrator "책상 위에는 노트와 필기구가 정리되어 있었고, 창가 쪽에는 두 사람이 앉아 있었다."
    # 원문 591행
    narrator "그중 한 사람이 우리를 보고 자리에서 일어났다."
    # 로만이 인사하는 순간 두 사람을 함께 보여준다.
    $ story_stage_fade_in(["roman", "darim"])
    # 원문 597행
    roman "앗,,, 오셨어요……!"
    # 원문 연출: [SFX] 책 떨어지는 소리
    $ story_sfx("paper")
    # 원문 603행
    $ story_stage(faces={"roman": "surprised"})
    roman "아……!"
    # 원문 607행
    narrator "자리에서 급하게 일어나는 바람에 책 한 권이 바닥으로 떨어졌다."
    # 원문 609행
    narrator "나는 발밑에 떨어진 책을 주워 건넸다."
    # 원문 613행
    mc "여기요."
    # 원문 617행
    $ story_stage(faces={"roman": "embarrassed"})
    roman "앗,,, 가, 감사합니다……."
    # 원문 621행
    mc "괜찮아요. 다친 데는 없어요?"
    # 원문 625행
    roman "네……! 저는 괜찮아요."
    # 원문 627행
    roman "책도…… 아마 괜찮을 거예요."
    $ story_enter("sia", side="left", face="smug")
    # 원문 631행
    sia "로만아, 책이랑 싸웠어?"
    # 원문 635행
    roman "아, 아니에요……."
    $ story_enter("omu", side="right", face="serious")
    # 원문 639행
    omu "시아야, 니는 좀 가만히 있어라."
    # 원문 연출: [SPRITE] 다림 · 부드러운 웃음
    $ story_stage(faces={"darim": "happy"})
    # 원문 645행
    darim "로만 씨, 그거 아까 교양 시간에 읽던 책이죠?"
    # 원문 649행
    roman "네…… 맞아요."
    # 원문 653행
    darim "다음 주에도 가져오실 거면 가방에 먼저 넣어두세요."
    # 원문 657행
    roman "아, 네……."
    # 원문 661행
    darim "또 떨어뜨리면 책이 서운해할지도 몰라요."
    # 원문 665행
    roman "앗,,, 책도 서운해하나요……?"
    # 원문 669행
    darim "후후. 농담이에요."
    # 원문 673행
    sia "어? 다림 언니도 농담을 하네?"
    # 원문 677행
    darim "저도 농담할 줄 알아요."
    # 원문 681행
    sia "와, 의외다."
    # 원문 685행
    darim "시아 씨한테만 안 한 거 아닐까요?"
    # 원문 689행
    $ story_stage(faces={"sia": "confused"})
    sia "……어라?"
    # 원문 693행
    narrator "차분한 인상이었지만, 생각보다 만만한 사람은 아닌 모양이다."
    # 원문 697행
    darim "안녕하세요. 저는 다림이에요. 철학과 3학년이고요."
    # 원문 701행
    mc "안녕하세요. [player_name]입니다."
    # 원문 705행
    darim "오늘 새로 오신 분이군요. 잘 부탁드려요."
    # 원문 709행
    roman "저, 저는 로만이에요……."
    # 원문 711행
    roman "영문학과 1학년이고……."
    # 원문 713행
    roman "잘 부탁드립니다……!"
    # 원문 717행
    mc "저도 잘 부탁해요."
    # 원문 721행
    narrator "로만은 작은 목소리로 인사를 마친 뒤 다시 책을 품에 안았다."
    # 원문 723행
    narrator "낯선 사람을 대하는 일이 조금 어려운 걸까."
    # 원문 선택지: 로만과 대화
    menu:
        "책 좋아하시나 봐요?":
            # 원문 737행
            mc "책 좋아하시나 봐요?"
            # 원문 741행
            roman "아, 네……!"
            # 원문 743행
            roman "많이 읽는 편은 아닐 수도 있지만…… 좋아해요."
            # 원문 747행
            mc "어떤 책 좋아하세요?"
            # 원문 751행
            roman "음…… 소설이요. 특히 읽고 나서 오래 생각하게 되는 이야기요."
            # 원문 755행
            mc "그런 책을 읽으면 기분이 복잡해지지 않아요?"
            # 원문 759행
            roman "맞아요……."
            # 원문 761행
            roman "그런데 그게 또 재미있어서요."
            # 원문 765행
            $ story_stage(faces={"roman": "embarrassed"})
            roman "앗,,, 제가 혼자 너무 떠들었죠……?"
            # 원문 769행
            mc "아뇨. 재미있는데요?"
            # 원문 773행
            $ story_stage(faces={"roman": "happy"})
            roman "……다행이에요."
            $ story_apply("ch01_sc03_a", affection={'roman': 1})
        "많이 놀랐죠? 괜찮아요?":
            # 원문 781행
            mc "많이 놀랐죠? 괜찮아요?"
            # 원문 785행
            roman "앗,,, 네……."
            # 원문 787행
            roman "사실 사람이 갑자기 많이 들어와서 조금 놀랐어요."
            # 원문 791행
            mc "그럴 수 있죠."
            # 원문 795행
            roman "……고마워요."
            # 원문 799행
            darim "로만 씨는 조금 천천히 친해지는 편이세요."
            # 원문 803행
            roman "다림 선배……."
            # 원문 807행
            darim "칭찬이에요."
            # 원문 811행
            mc "그럼 저도 천천히 친해지면 되겠네요."
            # 원문 815행
            $ story_stage(faces={"roman": "happy"})
            roman "……네."
            $ story_apply("ch01_sc03_b", trust={'roman': 1})
        "그 책 재미있어요?":
            # 원문 823행
            mc "그 책 재미있어요?"
            # 원문 827행
            roman "앗,,, 네! 저는 재미있게 읽고 있어요."
            # 원문 831행
            mc "어떤 내용인데요?"
            # 원문 835행
            roman "음…… 설명하기가 조금 어려운데요."
            # 원문 837행
            roman "같은 문장을 읽어도 사람마다 다른 장면을 떠올릴 수 있는 이야기예요."
            # 원문 841행
            mc "신기하네요."
            # 원문 845행
            roman "혹시 관심 있으시면…… 나중에 빌려드릴까요?"
            # 원문 849행
            mc "그래도 돼요?"
            # 원문 853행
            roman "네……!"
            # 원문 855행
            roman "대신……."
            # 원문 859행
            mc "대신이요?"
            # 원문 863행
            $ story_stage(faces={"roman": "happy"})
            roman "읽고 나서 감상 한 줄은 꼭 알려주세요."
            # 원문 867행
            narrator "로만은 말끝에 아주 작게 웃었다."
            $ story_apply("ch01_sc03_c")
            $ story_flag("roman_book_event", True)

    # 원문 875행
    darim "두 분은 벌써 친해지셨네요."
    # 원문 879행
    $ story_stage(faces={"roman": "embarrassed"})
    roman "앗,,, 아, 아직……."
    # 원문 883행
    sia "그럼 이제 다 모인 거야?"
    # 원문 887행
    darim "한 분 더 오신다고 했어요."
    # 원문 891행
    omu "누고?"
    # 원문 895행
    darim "하린 씨요."
    # 원문 899행
    roman "아, 하린 선배……!"
    # 원문 903행
    mc "아는 분이에요?"
    # 원문 907행
    roman "네. 같은 동아리예요."
    # 원문 911행
    sia "아."
    # 원문 915행
    sia "그럼 오늘도 그 얘기 듣겠네."
    # 원문 919행
    omu "뭔 얘긴데?"
    # 원문 923행
    $ story_stage(faces={"sia": "embarrassed"})
    sia "……음료수."
    # 원문 927행
    narrator "음료수?"
    # 원문 929행
    narrator "어쩐지 시아의 표정이 조금 굳었다."
    # 원문 연출: [SCENE 03 END]
    jump ch01_sc04

# SC04 · 음료수 사건의 전말 / 원문 933행
label ch01_sc04:
    $ phone_timeline_enter("CH01", "ch01_sc04")
    # 원문 연출: [BG] 공동 동아리실
    $ sd_event_end(mode="normal", cast=["sia", "roman", "darim", "omu"])
    $ story_scene("clubroom307", mode="normal", cast=["sia", "roman", "darim", "omu"], light="day", location="동아리실 307호")
    # 원문 연출: [SFX] 문 열리는 소리
    $ story_sfx("door_open")
    # 원문 연출: [SPRITE] 하린 · 기본 표정
    $ story_enter("lumi", side="right", face="normal")
    # 원문 941행
    lumi "다들 먼저 와 있었네요."
    # 원문 947행
    narrator "문을 열고 들어온 사람은 커다란 파일을 들고 있었다."
    # 원문 949행
    narrator "안쪽으로는 정리된 도면과 여러 장의 종이가 보였다."
    # 하린의 첫 인사는 스탠딩으로 이어간다. (원문 953행)
    darim "하린 씨, 어서 오세요."
    # 원문 957행
    roman "앗,,, 하린 선배!"
    # 원문 961행
    lumi "로만 씨도 왔네. 오늘 교양은 어땠어요?"
    # 원문 965행
    roman "아, 괜찮았어요……!"
    $ story_stage(mode="normal", cast=["sia", "roman", "darim", "omu", "lumi"], faces={"sia": "angry"})
    # 원문 969행
    sia "야, 하린아. 나한텐 인사 안 하냐?"
    $ story_stage(faces={"lumi": "smug"})
    # 원문 973행
    lumi "시아 씨도 오셨네."
    # 원문 977행
    sia "왜 그렇게 영혼이 없냐?"
    # 원문 981행
    lumi "아뇨. 오늘은 음료수를 안 들고 계셔서 다행이라고 생각했어요."
    # 원문 연출: [BGM] Comedy Mischief
    $ play_bgm("comedy_light")
    # 원문 연출: [SD] 하린과 시아 등장. 하린이는 미소, 시아는 충격.
    $ sd_event_start("ch01_drink_incident", variant="01")
    # 원문 989행
    sia "야아아! 그 얘기 언제까지 할 건데!"
    # 원문 993행
    lumi "글쎄요. 올해 축제까지는 기억할 것 같은데."
    # 원문 997행
    sia "작년 일이잖아!"
    # 원문 1001행
    lumi "네. 작년 축제였죠."
    # 원문 1005행
    lumi "제가 새 옷을 입고 있었던 날이기도 하고."
    # 원문 1009행
    sia "아, 진짜 미안하다고 했잖아!"
    # 원문 1013행
    omu "무슨 일 있었는데?"
    # 원문 1017행
    sia "아니, 그게……."
    # 원문 1021행
    lumi "시아 씨가 제 옷에 음료수를 한 컵 쏟았거든요."
    # 원문 1025행
    mc "한 컵이나요?"
    # 원문 1029행
    sia "정확히는 반 컵 정도였거든?"
    # 원문 1033행
    lumi "나머지 반 컵은 바닥이 마셨겠네요."
    # 원문 1037행
    sia "ㅋㅋㅋ 아 진짜!"
    # 원문 1041행
    darim "많이 놀라셨겠어요."
    # 원문 1045행
    lumi "그때는 조금요."
    # 원문 1047행
    lumi "그런데 덕분에 시아 씨랑 친해졌으니까, 나쁘지만은 않았죠."
    # 원문 1051행
    sia "오…… 감동인데?"
    # 원문 1055행
    lumi "그래도 옷은 다시 사주셨어야 했지만요."
    # 원문 1059행
    sia "감동 취소!"
    # 원문 연출: [SD] 시아가 뒤로 넘어지고, 오므가 옆에서 웃는다.
    # 음료수 사건은 첫 SD 컷을 계속 사용한다.
    # 원문 1065행
    roman "앗,,, 저는 음료수 조심해서 마실게요……."
    # 원문 1069행
    lumi "로만 씨는 괜찮아요. 믿고 있거든."
    # 원문 1073행
    sia "차별이다!"
    # 원문 1077행
    lumi "이제 아셨네."
    # 원문 1081행
    narrator "이쯤 되니 둘이 얼마나 친한 사이인지 알 것 같았다."
    # 원문 1083행
    narrator "한쪽은 놀리고, 다른 한쪽은 억울해하면서도 계속 받아친다."
    # 원문 1087행
    mc "그런데 두 분은 같은 학과예요?"
    # 원문 1091행
    lumi "아뇨. 저는 건축학과 3학년이에요."
    # 원문 1095행
    sia "난 애니메이션과고."
    # 원문 1099행
    lumi "작년 축제에서 우연히 알게 됐어요. 아주 인상적인 방법으로요."
    # 원문 1103행
    sia "이제 그만!"
    # 원문 1107행
    omu "와, 니 진짜 평생 놀림당하겠다."
    # 원문 1111행

    sia "너까지 그러지 마!"
    # 원문 연출: [SD] 화면에 '음료수 사건 · 현재도 진행 중'이라는 코미디 자막을 짧게 표시.
    # 원문 연출: [전환] 일반 대화 모드
    $ sd_event_end(mode="normal", cast=["sia", "roman", "darim", "omu", "lumi"])
    $ story_stage(faces={"lumi": "normal"})
    # 원문 1119행
    lumi "아, 그러고 보니 처음 뵙는 분이 계시네요."
    # 원문 1123행
    mc "안녕하세요. 오늘 새로 들어왔어요. [player_name]입니다."
    # 원문 1127행
    lumi "하린이에요. 잘 부탁해요."
    # 원문 1131행
    mc "저도 잘 부탁해요."
    # 원문 1135행
    lumi "분위기에 놀라셨죠?"
    # 원문 1139행
    mc "조금요."
    # 원문 1143행
    lumi "걱정하지 마세요."
    # 원문 1147행
    lumi "평소에도 이 정도니까."
    # 원문 1151행
    mc "……그게 더 걱정되는데요."
    # 원문 1155행
    $ story_stage(faces={"lumi": "happy"})
    lumi "후후. 적응하시면 괜찮을 거예요."
    $ story_stage(faces={"sia": "normal", "roman": "normal", "darim": "happy", "omu": "normal"})
    # 원문 1159행
    darim "그러면 이제 회의를 시작할까요?"
    # 원문 1163행
    omu "아, 맞다. 다림 선배."
    # 원문 1167행
    darim "네?"
    # 원문 1171행
    omu "작년에 같이 듣던 교양 기억나세요? 그때 조별 발표도 이런 식으로 했잖아요."
    # 원문 1175행
    darim "기억하죠. 그때도 시간 맞추기가 어려웠어요."
    # 원문 1179행
    omu "맞아요. 그때 진짜 고생했는데."
    # 원문 1183행
    $ story_stage(faces={"sia": "confused"})
    sia "어? 둘도 아는 사이였어?"
    # 원문 1187행
    omu "작년에 같은 교양 들었다."
    # 원문 1191행
    darim "그때 몇 번 같이 이야기했어요."
    # 원문 1195행
    sia "이 학교 인간관계 생각보다 좁네."
    # 원문 1199행
    $ story_stage(faces={"lumi": "smug"})
    lumi "시아 씨가 사람을 많이 만나고 다녀서 그런 건 아닐까요?"
    # 원문 1203행
    sia "그것도 맞긴 해."
    # 원문 1207행
    narrator "그렇게 예상보다 복잡한 관계를 가진 여섯 사람이 한 테이블에 모였다."
    # 원문 1209행
    narrator "아니, 내가 들어왔으니까 여섯 사람이다."
    # 원문 1211행
    narrator "이제부터 무슨 일이 시작되는 걸까."
    # 원문 연출: [SCENE 04 END]
    jump ch01_sc05

# SC05 · 첫 회의부터 난장판 / 원문 1215행
label ch01_sc05:
    $ phone_timeline_enter("CH01", "ch01_sc05")
    # 원문 연출: [BG] 공동 동아리실
    $ sd_event_end(mode="normal", cast=[])
    $ story_scene("clubroom307", mode="normal", cast=[], light="day", location="동아리실 307호")
    # 원문 연출: [BGM] Meeting Comedy
    $ play_bgm("comedy_light")
    # 원문 연출: [SD] 회의 테이블을 중심으로 다섯 히로인 배치.
    $ sd_event_start("ch01_group_meeting", variant="01")
    # 원문 1225행
    darim "그럼 시작해 볼까요?"
    # 원문 1229행
    sia "좋아!"
    # 원문 1233행
    darim "일단 저희가 무엇을 만들 건지부터 정해야 할 것 같아요."
    # 원문 1237행
    sia "웹툰 전시."
    # 원문 1241행
    omu "너무 빠른 거 아이가."
    # 원문 1245행
    sia "이미 결정됐는데?"
    # 원문 1249행
    lumi "누가요?"
    # 원문 1253행
    sia "나."
    # 원문 1257행
    lumi "그럼 기각할게요."
    # 원문 1261행
    sia "야!"
    # 원문 1265행
    roman "앗,,, 저는…… 짧은 글을 전시해도 좋을 것 같아요."
    # 원문 1269행
    darim "좋은 생각이에요. 축제에 온 사람들이 직접 글을 남길 수도 있고요."
    # 원문 1273행
    omu "사진도 같이 넣으면 괜찮겠다."
    # 원문 1277행
    sia "그럼 그림이랑 글이랑 사진이잖아."
    # 원문 1281행
    mc "다 같이 전시하면 안 돼요?"
    # 원문 1285행
    lumi "가능은 한데, 그냥 나란히 붙여두는 것보다는 연결되는 방식이 좋겠네요."
    # 원문 1289행
    sia "오, 그럼 전시관처럼?"
    # 원문 1293행
    lumi "공간이 얼마나 배정되느냐에 따라 다르겠지만요."
    # 원문 1297행
    omu "사진은 너무 빽빽하면 보기 힘들긴 하지."
    # 원문 1301행
    roman "글도…… 너무 많으면 읽기 힘들 것 같아요."
    # 원문 1305행
    darim "그럼 관람객이 직접 참여하는 형식으로 만들면 어떨까요?"
    # 원문 1309행
    mc "직접 참여한다는 건요?"
    # 원문 1313행
    darim "예를 들면 자기 대학생활에서 기억에 남는 순간을 적는 거예요."
    # 원문 1317행
    omu "사진으로도 남길 수 있겠네."
    # 원문 1321행
    roman "짧은 문장으로도요……!"
    # 원문 1325행
    sia "난 그림으로 그려줄 수 있는데."
    # 원문 1329행
    lumi "그럼 참여 방식에 따라 공간을 나누면 되겠네요."
    # 원문 1333행
    narrator "방금 전까지는 다들 제각각 이야기하는 것처럼 보였다."
    # 원문 1335행
    narrator "그런데 조금씩 같은 방향을 바라보기 시작했다."
    # 원문 1339행
    mc "그럼 주제를 하나로 묶어보면 어떨까요?"
    # 원문 1343행
    darim "어떤 식으로요?"
    # 원문 1347행
    mc "우리 대학에서 보내는 하루를 기록하는 거예요."
    # 원문 1349행
    mc "누군가는 글로, 누군가는 그림으로, 또 누군가는 사진으로."
    # 원문 1353행
    roman "……좋은 것 같아요."
    # 원문 1357행
    omu "오, 그거 괜찮네."
    # 원문 1361행
    sia "그럼 이름도 있어야지."
    # 원문 1365행
    lumi "전시 제목이요?"
    # 원문 1369행
    sia "응."
    # 원문 1373행
    sia "대학 생활 생존기!"
    # 원문 1377행
    omu "무슨 재난 영화 제목 같노."
    # 원문 1381행
    sia "그럼 대학에서 살아남는 법!"
    # 원문 1385행
    darim "점점 생존이 목적이 되고 있네요."
    # 원문 1389행
    roman "앗,,, '우리 대학의 하루'는 어떨까요……?"
    # 원문 1393행
    sia "오."
    # 원문 1397행
    omu "그게 더 낫다."
    # 원문 1401행
    lumi "간결하고 좋아요."
    # 원문 1405행
    darim "그럼 '우리 대학의 하루를 기록하는 체험 전시'로 정할까요?"
    # 원문 1409행
    sia "뭔가 길어졌는데?"
    # 원문 1413행
    mc "공식 기획명으로 쓰고, 부스 이름은 나중에 짧게 정해요."
    # 원문 1417행
    sia "오케이. 그러면 내 4컷 만화도 들어가는 거지?"
    # 원문 1421행
    lumi "4컷으로 끝낼 수 있어요?"
    # 원문 1425행
    sia "……."
    # 원문 1429행
    lumi "왜 대답이 없지?"
    # 원문 1433행
    sia "6컷 정도는 괜찮지 않아?"
    # 원문 1437행
    omu "시작됐다."
    # 원문 1441행
    darim "일단 네 컷부터 만들어 보세요."
    # 원문 1445행
    sia "아, 알았어!"
    # 원문 연출: [SD] 시아가 책상 위에 엎드리고, 오므가 팔짱을 낀 채 바라본다.
    # 회의는 첫 SD 컷을 계속 사용한다.
    # 원문 1451행
    narrator "이상한 점이 있었다."
    # 원문 1453행
    narrator "어쩐지 전부 제멋대로인 것 같은데, 회의는 생각보다 잘 진행되고 있었다."
    # 원문 1457행
    darim "그럼 역할을 나누면 좋겠네요."
    # 원문 1461행
    lumi "저는 공간 배치 쪽을 맡아볼게요. 건축학과니까 익숙하긴 해요."
    # 원문 1465행
    omu "사진은 내가 해볼게."
    # 원문 1469행
    sia "그림은 나!"
    # 원문 1473행
    roman "앗,,, 저는 글 쪽을 해볼게요……."
    # 원문 1477행
    darim "그럼 저는 일정과 운영 계획을 정리할게요."
    # 원문 1481행
    mc "저는 필요한 일을 도우면서 같이 정리하면 되겠네요."
    # 원문 1485행
    sia "만능 심부름꾼 탄생."
    # 원문 1489행
    mc "그런 직책은 없거든요."
    # 원문 1493행
    lumi "이름은 조금 그렇지만, 여러 작업을 연결해 주는 역할이 필요하긴 해요."
    # 원문 1497행
    darim "그럼 [player_name] 씨는 각 작업을 함께 보면서 도와주시는 걸로 할까요?"
    # 원문 1501행
    mc "좋아요."
    # 원문 1505행
    omu "니 고생 좀 하겠다."
    # 원문 1509행
    sia "환영한다, 프로젝트의 세계에."
    # 원문 1513행
    mc "……지금 나갈 수는 없나요?"
    # 원문 1517행

    sia "응 아니야~"
    # 원문 연출: [SD] 시아가 주인공 쪽을 향해 손가락으로 X를 만드는 코미디 연출.
    # 원문 연출: [SCENE 05 END]
    $ sd_event_end(mode="normal", cast=[])
    jump ch01_sc06

# SC06 · 첫 번째 선택 / 원문 1523행
label ch01_sc06:
    $ phone_timeline_enter("CH01", "ch01_sc06")
    # 원문 연출: [BG] 공동 동아리실
    $ sd_event_end(mode="normal", cast=[])
    $ story_scene("clubroom307", mode="normal", cast=[], light="day", location="동아리실 307호")
    # 원문 연출: [BGM] Warm Daily
    $ play_bgm("campus_day")
    $ sd_event_start("ch01_group_meeting", variant="01")
    # 원문 1531행
    darim "그럼 오늘은 각자 기본 자료를 조금씩 준비해 볼까요?"
    # 원문 1535행
    lumi "좋아요. 저는 공간을 대략 그려볼게요."
    # 원문 1539행
    sia "난 만화 콘티!"
    # 원문 1543행
    omu "사진 찍으러 나갈까."
    # 원문 1547행
    roman "저는 자료를 찾아봐야겠네요……."
    # 원문 1551행
    darim "저도 일정표를 정리할게요."
    # 원문 1555행
    narrator "다섯 사람이 자연스럽게 각자의 작업을 시작했다."
    # 원문 1557행
    narrator "나는 잠깐 고민했다."
    # 원문 1559행
    narrator "어느 쪽을 먼저 도와주면 좋을까."
    # 원문 선택지: 함께할 작업 선택
    menu:
        "로만: 전시 문구부터 같이 찾아볼까요?":
            # 원문 1577행
            roman "앗,,, 저랑요?"
            # 원문 1579행
            roman "아, 좋아요……! 그럼 도서관에 잠깐 가도 괜찮으세요?"
            # 원문 1583행
            mc "네, 좋아요."
            $ story_apply("ch01_sc06_a", affection={'roman': 1}, values={'first_task_partner': 'roman'})
        "시아: 웹툰 콘티 만드는 거 도와드릴게요.":
            # 원문 1591행
            sia "오, 진짜?"
            # 원문 1593행
            sia "좋아. 대신 내가 시키는 대로 해야 돼."
            # 원문 1597행
            mc "뭔데 벌써 불안하죠?"
            # 원문 1601행
            sia "걱정 마. 아직은 안 위험해."
            $ story_apply("ch01_sc06_b", affection={'sia': 1}, values={'first_task_partner': 'sia'})
        "다림: 일정표 정리부터 해요.":
            # 원문 1609행
            darim "도와주시게요?"
            # 원문 1611행
            darim "좋아요. 일정이 조금 복잡했는데 같이 정리하면 금방 끝나겠네요."
            # 원문 1615행
            mc "잘 부탁해요."
            # 원문 1619행
            darim "저야말로요."
            $ story_apply("ch01_sc06_c", trust={'darim': 1}, values={'first_task_partner': 'darim'})
        "오므: 사진 찍으러 같이 가도 돼요?":
            # 원문 1627행
            omu "어? 같이 갈라꼬?"
            # 원문 1631행
            mc "네. 저도 도와드릴 일이 있을 것 같아서요."
            # 원문 1635행
            omu "그럼 카메라 가방 좀 들어줄래?"
            # 원문 1639행
            mc "역시 그거였군요."
            # 원문 1643행
            omu "하하, 장난이다. 가자."
            $ story_apply("ch01_sc06_d", affection={'omu': 1}, values={'first_task_partner': 'omu'})
        "하린: 부스 배치도 만드는 거 같이 볼까요?":
            # 원문 1651행
            lumi "저랑요?"
            # 원문 1653행
            lumi "좋아요. 다만 이쪽은 생각보다 재미없을 수도 있는데."
            # 원문 1657행
            mc "괜찮아요. 궁금하거든요."
            # 원문 1661행
            lumi "……그럼 특별히 구경시켜 드릴게요."
            $ story_apply("ch01_sc06_e", affection={'lumi': 1}, values={'first_task_partner': 'lumi'})

    # 원문 연출: [SCENE 06 END]
    $ sd_event_end(mode="normal", cast=[])
    jump ch01_sc07

label ch01_sc07:
    $ phone_timeline_enter("CH01", "ch01_sc07")
    if first_task_partner == "roman":
        jump ch01_sc07_roman
    elif first_task_partner == "sia":
        jump ch01_sc07_sia
    elif first_task_partner == "darim":
        jump ch01_sc07_darim
    elif first_task_partner == "omu":
        jump ch01_sc07_omu
    elif first_task_partner == "lumi":
        jump ch01_sc07_lumi
    else:
        jump ch01_sc07_lumi

# SC07-A · 로만: 책갈피에 적힌 말 / 원문 1669행
label ch01_sc07_roman:
    $ phone_timeline_enter("CH01", "ch01_sc07_roman")
    # 원문 연출: [BG] 대학교 도서관
    $ sd_event_end(mode="normal", cast=["roman"])
    $ story_scene("library", mode="normal", cast=["roman"], light="day", location="대학교 도서관")
    # 원문 연출: [BGM] Quiet Library
    $ play_bgm("quiet_library")
    # 원문 연출: [SPRITE] 로만 · 기본 표정
    $ story_stage(mode="normal", cast=["roman"], faces={'roman': 'normal'})
    # 원문 1679행
    narrator "도서관은 동아리실과 완전히 다른 분위기였다."
    # 원문 1681행
    narrator "시끄럽게 떠드는 사람도 없고, 갑자기 장난을 치는 사람도 없었다."
    # 원문 1683행
    narrator "무엇보다 시아가 없었다."
    # 원문 1687행
    mc "……조용하네요."
    # 원문 1691행
    roman "앗,,, 네……."
    # 원문 1693행
    roman "도서관이니까요……."
    # 원문 1697행
    mc "그러게요. 너무 당연한 말을 했네요."
    # 원문 1701행
    roman "후후……."
    # 원문 1705행
    narrator "로만은 작게 웃으며 책장으로 걸어갔다."
    # 원문 1709행
    roman "전시 문구에 사용할 만한 글을 조금 찾아보려고요."
    # 원문 1713행
    mc "어떤 문구가 좋을까요?"
    # 원문 1717행
    roman "음…… 저는 너무 멋있는 말보다는……."
    # 원문 1719행
    roman "읽는 사람이 자기 이야기를 떠올릴 수 있는 말이 좋을 것 같아요."
    # 원문 1723행
    mc "자기 이야기요?"
    # 원문 1727행
    roman "네. 같은 하루여도 사람마다 기억하는 건 다르잖아요."
    # 원문 1729행
    roman "누군가는 친구랑 밥 먹은 게 기억날 수도 있고……."
    # 원문 1731행
    roman "누군가는 집에 가는 길에 본 강아지가 기억날 수도 있고요."
    # 원문 1735행
    mc "강아지 좋아하세요?"
    # 원문 1739행
    roman "앗,,, 네!"
    # 원문 연출: [SPRITE] 로만 · 밝은 웃음
    $ story_stage(mode="normal", cast=["roman"], faces={'roman': 'happy'})
    $ story_effect("bounce", "roman")  # 원문 1745행
    roman "진짜 좋아해요."
    # 원문 1747행
    roman "강아지 사진만 봐도 기분이 좋아져서……."
    # 원문 1749행
    roman "아, 저번에 길에서 정말 귀여운 강아지를 봤거든요."
    # 원문 1753행
    mc "어땠는데요?"
    # 원문 1757행
    roman "작고…… 털이 복슬복슬하고……."
    # 원문 1759행
    roman "눈이 엄청 동그랬어요."
    # 원문 1763행
    mc "표현이 꽤 구체적이네요."
    # 원문 1767행
    roman "앗,,, 너무 신났나요?"
    # 원문 1771행
    mc "아뇨. 뭘 좋아하시는지 확실히 알겠어요."
    # 원문 1775행
    $ story_stage(faces={"roman": "embarrassed"})
    narrator "로만은 조금 부끄러운 듯 책 표지를 만지작거렸다."
    # 원문 1779행
    roman "……그럼 [player_name] 씨는 어떤 하루를 기억하고 싶으세요?"
    # 원문 1783행
    mc "음……."
    # 원문 선택지: 로만의 질문
    menu:
        "재미있게 웃었던 날.":
            # 원문 1797행
            roman "후후…… 그럼 오늘도 기억에 남을 것 같네요."
            # 원문 1801행
            mc "왜요?"
            # 원문 1805행
            roman "시아 선배 때문에 많이 웃으셨잖아요."
            $ story_apply("ch01_sc07_roman_a")
        "조용하고 편안했던 날.":
            # 원문 1811행
            roman "저도 그런 날 좋아해요."
            # 원문 1813행
            roman "특별한 일이 없어도 편안하게 지나간 날이요."
            $ story_apply("ch01_sc07_roman_b")
        "평소와 달랐던 날.":
            # 원문 1819행
            roman "그럼 오늘이 그런 날일 수도 있겠네요."
            # 원문 1821행
            roman "새로운 사람들을 많이 만나셨으니까요."
            $ story_apply("ch01_sc07_roman_c")

    # 원문 1827행
    narrator "잠시 후 로만이 책 한 권을 꺼냈다."
    # 원문 1829행
    narrator "그런데 책 사이에서 작은 종이가 떨어졌다."
    # 원문 1833행
    mc "어? 책갈피 떨어졌어요."
    # 원문 1837행
    $ story_stage(faces={"roman": "surprised"})
    roman "앗,,,!"
    # 원문 1841행
    narrator "종이에는 손글씨로 짧은 문장이 적혀 있었다."
    # 원문 1843행
    narrator "「평범한 하루에도, 오래 기억하고 싶은 순간이 있다.」"
    # 원문 1847행
    mc "이거 직접 쓰신 거예요?"
    # 원문 1851행
    $ story_stage(faces={"roman": "embarrassed"})
    roman "아…… 네."
    # 원문 1853행
    roman "그냥 읽다가 생각나서 적어둔 거예요."
    # 원문 1857행
    mc "좋은 문장인데요?"
    # 원문 1861행
    roman "……정말요?"
    # 원문 1865행
    mc "네. 우리 전시에도 어울릴 것 같아요."
    # 원문 1869행
    roman "앗,,, 그러면……."
    # 원문 1871행
    roman "전시 문구로 써볼까요?"
    # 원문 1875행
    mc "좋죠."
    # 원문 1879행
    narrator "로만은 조심스럽게 책갈피를 집어 들었다."
    $ story_stage(faces={"roman": "happy"})  # 원문 1881행
    $ story_icon("roman", "heart")
    narrator "그리고 조금 전보다 환하게 웃었다."
    # 원문 1885행
    roman "오늘 같이 와주셔서 감사해요."
    # 원문 1889행
    mc "저도 재미있었어요."
    # 원문 1893행
    roman "……그럼 다음에도 같이 와주실래요?"
    # 원문 1897행
    mc "자료 찾으러요?"
    # 원문 1901행
    roman "네……."
    # 원문 1905행
    roman "자료 찾으러요."
    # 원문 1909행
    narrator "어쩐지 마지막 말이 조금 작게 들렸다."
    # 원문 연출: [FLAG] roman_library_visit = True
    $ story_flag("roman_library_visit", True)
    $ secret_note_unlock("roman", 1)
    jump ch01_sc08

# SC07-B · 시아: 콘티 지옥에 오신 걸 환영합니다 / 원문 1915행
label ch01_sc07_sia:
    $ phone_timeline_enter("CH01", "ch01_sc07_sia")
    # 원문 연출: [BG] 애니메이션과 작업실
    $ sd_event_end(mode="normal", cast=["sia"])
    $ story_scene("animation", mode="normal", cast=["sia"], light="day", location="애니메이션과 작업실")
    # 원문 연출: [BGM] Playful Workshop
    $ play_bgm("comedy_light")
    # 원문 연출: [SPRITE] 시아 · 자신만만
    $ story_stage(mode="normal", cast=["sia"], faces={'sia': 'smug'})
    # 원문 1925행
    sia "자, 환영한다."
    # 원문 1929행
    mc "어디에요?"
    # 원문 1933행
    sia "콘티 지옥에."
    # 원문 1937행
    mc "저 지금 돌아가도 돼요?"
    # 원문 1941행
    sia "응 아니야~ 이미 늦었어."
    # 원문 1945행
    narrator "책상 위에는 태블릿과 스케치북, 몇 장의 낙서가 놓여 있었다."
    # 원문 1947행
    narrator "시아는 태블릿을 켜더니 자신 있게 화면을 보여줬다."
    # 원문 1951행
    sia "어때?"
    # 원문 1955행
    mc "……이게 뭐예요?"
    # 원문 1959행
    sia "우리 축제 부스 안내 만화."
    # 원문 1963행
    mc "그건 알겠는데, 왜 주인공 얼굴이 이렇게 생겼어요?"
    # 원문 1967행
    sia "일단 사람이긴 하잖아."
    # 원문 1971행
    mc "눈이 네 개잖아요."
    # 원문 1975행
    sia "감정 표현이 풍부한 캐릭터야."
    # 원문 1979행
    mc "그런 이유였어요?"
    # 원문 1983행
    sia "예술을 너무 논리적으로 이해하려 하지 마."
    # 원문 1987행
    narrator "시아는 뻔뻔하게 말하더니 곧바로 그림을 수정하기 시작했다."
    # 원문 1989행
    $ story_stage(faces={"sia": "serious"})
    narrator "방금까지 장난을 치던 모습과 달리 작업할 때는 제법 집중하는 얼굴이었다."
    # 원문 1993행
    mc "근데 시아 씨, 진짜 빠르게 그리네요."
    # 원문 1997행
    sia "그치? 내가 좀 잘해."
    # 원문 2001행
    mc "농담이 아니라 진짜로요."
    # 원문 2005행
    $ story_stage(faces={"sia": "embarrassed"})
    sia "……."
    # 원문 2009행
    sia "아, 뭐야. 갑자기 진지하게 칭찬하지 마."
    # 원문 2013행
    mc "왜요? 잘 그렸는데요."
    # 원문 2017행
    $ story_stage(faces={"sia": "smug"})
    sia "……응 아니야~ 더 칭찬해도 됨."
    # 원문 2021행
    mc "역시 괜한 걱정이었네요."
    # 원문 2025행
    narrator "시아는 씩 웃더니 새로운 레이어를 만들었다."
    # 원문 2029행
    sia "그럼 감상 담당님. 하나 골라봐."
    # 원문 선택지: 만화 방향
    menu:
        "웃긴 장면을 먼저 넣어요.":
            # 원문 2043행
            sia "오, 너 좀 아는데?"
            # 원문 2045행
            sia "사람을 웃겨야 일단 관심을 가지지."
            $ story_apply("ch01_sc07_sia_a")
        "참여 방법을 쉽게 알려줘요.":
            # 원문 2051행
            sia "음, 그것도 맞지."
            # 원문 2053행
            sia "만화가 아무리 웃겨도 설명이 안 되면 소용없긴 해."
            $ story_apply("ch01_sc07_sia_b")
        "둘 다 할 수 있지 않아요?":
            # 원문 2059행
            sia "……야."
            # 원문 2063행
            mc "왜요?"
            # 원문 2067행
            sia "그게 제일 어렵거든?"
            # 원문 2071행
            mc "그럼 못 해요?"
            # 원문 2075행
            sia "누가 못 한다고 했냐?"
            # 원문 2077행
            sia "기다려 봐."
            $ story_apply("ch01_sc07_sia_c")

    # 원문 2083행
    $ story_stage(faces={"sia": "serious"})
    narrator "시아는 잠시 말없이 그림을 그렸다."
    # 원문 2085행
    narrator "조금 전까지 정신없이 움직이던 입이 멈추자 작업실이 이상하게 조용해졌다."
    # 원문 2089행
    mc "원래 작업할 때 이렇게 조용해요?"
    # 원문 2093행
    sia "집중하면 좀 그래."
    # 원문 2097행
    mc "의외네요."
    # 원문 2101행
    sia "야, 그럼 평소의 나는 뭐냐?"
    # 원문 2105행
    mc "시끄러운 사람이요?"
    # 원문 2109행
    sia "……."
    # 원문 2113행
    sia "반박할 수가 없네."
    # 원문 2117행
    narrator "완성된 콘티에는 주인공이 말한 의견도 반영되어 있었다."
    # 원문 2121행
    mc "오, 아까보다 훨씬 보기 좋아요."
    # 원문 2125행
    sia "그치?"
    # 원문 2129행
    mc "네. 진짜 잘 만들었어요."
    # 원문 2133행
    $ story_stage(faces={"sia": "embarrassed"})
    sia "……."
    # 원문 2137행
    sia "야, 근데 너."
    # 원문 2141행
    mc "네?"
    # 원문 2145행
    sia "칭찬 좀 잘한다?"
    # 원문 2149행
    mc "그냥 사실대로 말하는 건데요."
    # 원문 2153행
    sia "……그게 더 문제인데."
    # 원문 2157행
    mc "뭐라고요?"
    # 원문 2161행
    sia "아무것도 아냐."
    $ story_stage(faces={"sia": "happy"})  # 원문 2163행
    $ story_effect("bounce", "sia")
    sia "자, 다음 컷도 만들자!"
    # 원문 2167행
    narrator "시아는 다시 평소처럼 웃었다."
    # 원문 2169행
    narrator "그래도 방금 전의 진지한 표정은 조금 의외였다."
    # 원문 연출: [FLAG] sia_concept_event = True
    $ story_flag("sia_concept_event", True)
    $ secret_note_unlock("sia", 1)
    jump ch01_sc08

# SC07-C · 다림: 선배의 승부욕 / 원문 2175행
label ch01_sc07_darim:
    $ phone_timeline_enter("CH01", "ch01_sc07_darim")
    # 원문 연출: [BG] 캠퍼스 스터디룸
    $ sd_event_end(mode="normal", cast=["darim"])
    $ story_scene("study", mode="normal", cast=["darim"], light="day", location="캠퍼스 스터디룸")
    # 원문 연출: [BGM] Warm Afternoon
    $ play_bgm("warm_workshop")
    # 원문 연출: [SPRITE] 다림 · 기본 표정
    $ story_stage(mode="normal", cast=["darim"], faces={'darim': 'normal'})
    # 원문 2185행
    darim "그럼 먼저 가능한 날짜부터 정리할까요?"
    # 원문 2189행
    mc "네."
    # 원문 2193행
    darim "축제까지 시간이 조금 남았으니까, 급한 것과 나중에 해도 되는 걸 구분해 두면 좋겠어요."
    # 원문 2197행
    mc "생각보다 할 일이 많네요."
    # 원문 2201행
    darim "그러게요."
    # 원문 2205행
    narrator "다림은 노트북 화면에 표를 만들기 시작했다."
    # 원문 2207행
    narrator "날짜, 작업, 담당자."
    # 원문 2209행
    narrator "하나씩 정리되자 복잡했던 준비 과정이 조금은 명확해졌다."
    # 원문 2213행
    mc "선배는 이런 거 잘하시네요."
    # 원문 2217행
    darim "그냥 정리하는 걸 좋아해요."
    # 원문 2221행
    mc "이런 거 혼자 하면 힘들지 않아요?"
    # 원문 2225행
    darim "그렇죠. 혼자 하면 아무래도 시간이 오래 걸려요."
    # 원문 2229행
    darim "그래서 같이 해주셔서 고마워요."
    # 원문 2233행
    narrator "잠시 후 일정표의 기본 틀이 완성됐다."
    # 원문 2235행
    narrator "나는 의자에 등을 기대고 숨을 돌렸다."
    # 원문 2239행
    mc "휴…… 잠깐 쉬어도 되겠죠?"
    # 원문 2243행
    darim "물론이죠."
    # 원문 연출: [SFX] 휴대전화 알림
    $ story_sfx("message")
    # 원문 2249행
    narrator "마침 휴대전화에 게임 관련 알림이 떠 있었다."
    # 원문 2253행
    $ story_stage(faces={"darim": "surprised"})
    darim "어? 그 게임 하세요?"
    # 원문 2257행
    mc "이거요?"
    # 원문 2261행
    darim "네. 저도 해봤는데."
    # 원문 2265행
    mc "오, 선배도 게임 좋아하세요?"
    # 원문 2269행
    $ story_stage(faces={"darim": "happy"})
    darim "좋아하죠."
    # 원문 2273행
    darim "그런데 혹시 어느 캐릭터 사용하세요?"
    # 원문 2277행
    mc "음……."
    # 원문 선택지: 게임 취향
    menu:
        "공격적으로 플레이하는 편이에요.":
            # 원문 2291행
            darim "아, 저랑 비슷하시네요."
            # 원문 2293행
            darim "저도 가끔은 먼저 들어가는 게 좋더라고요."
            $ story_apply("ch01_sc07_darim_a")
        "안전하게 운영하는 편이에요.":
            # 원문 2299행
            darim "좋은 방식이죠."
            # 원문 2301행
            darim "그런데 너무 안전하게만 하면 기회를 놓칠 때도 있더라고요."
            $ story_apply("ch01_sc07_darim_b")
        "그때그때 달라요.":
            # 원문 2307행
            darim "상황에 맞춰서 바꾸는 게 제일 어렵죠."
            # 원문 2309행
            darim "생각보다 게임을 많이 하셨나 봐요."
            $ story_apply("ch01_sc07_darim_c")

    # 원문 2315행
    mc "선배는 게임할 때도 이렇게 차분해요?"
    # 원문 2319행
    darim "음……."
    # 원문 2323행
    darim "아마 그럴걸요?"
    # 원문 2327행
    mc "아마요?"
    # 원문 2331행
    darim "……가끔은 조금 달라질 수도 있죠."
    # 원문 2335행
    mc "예를 들면요?"
    # 원문 2339행
    darim "지고 있을 때요."
    # 원문 2343행
    mc "화내세요?"
    # 원문 2347행
    darim "화는 안 내요."
    # 원문 2349행
    darim "그냥……."
    # 원문 2353행
    darim "한 판만 더 하자고 하죠."
    # 원문 2357행
    mc "그게 승부욕 아닌가요?"
    # 원문 2361행
    darim "후후, 그런가요?"
    # 원문 2365행
    mc "완전 의외네요."
    # 원문 2369행
    darim "사람이 한 가지 모습만 있는 건 아니잖아요."
    # 원문 2373행
    $ story_stage(faces={"darim": "happy"})
    narrator "다림은 미소를 지으며 노트북을 닫았다."
    # 원문 2377행
    darim "다음에 시간 되시면 게임 한 판 하실래요?"
    # 원문 2381행
    mc "좋죠."
    # 원문 2385행
    darim "좋아요."
    $ story_stage(faces={"darim": "smug"})  # 원문 2389행
    $ story_effect("bounce", "darim")
    darim "그때는 제가 이길게요."
    # 원문 2393행
    mc "벌써 이길 생각부터 하시는 거예요?"
    # 원문 2397행
    darim "후후. 이기면 좋잖아요."
    # 원문 2401행
    narrator "차분한 선배라는 첫인상이 조금 달라졌다."
    # 원문 2403행
    narrator "생각보다 장난기가 있는 사람인 것 같다."
    # 원문 연출: [FLAG] darim_game_event = True
    $ story_flag("darim_game_event", True)
    $ secret_note_unlock("darim", 1)
    jump ch01_sc08

# SC07-D · 오므: 사진 한 장의 차이 / 원문 2409행
label ch01_sc07_omu:
    $ phone_timeline_enter("CH01", "ch01_sc07_omu")
    # 원문 연출: [BG] 캠퍼스 산책로
    $ sd_event_end(mode="normal", cast=["omu"])
    $ story_scene("campus", mode="normal", cast=["omu"], light="day", location="캠퍼스 산책로")
    # 원문 연출: [BGM] Gentle Walk
    $ play_bgm("gentle_walk")
    # 원문 연출: [SPRITE] 오므 · 기본 표정
    $ story_stage(mode="normal", cast=["omu"], faces={'omu': 'normal'})
    # 원문 2419행
    omu "여기서부터 찍어보자."
    # 원문 2423행
    mc "생각보다 학교에 예쁜 곳이 많네요."
    # 원문 2427행
    omu "평소엔 바빠가 잘 못 보는 거지."
    # 원문 2431행
    narrator "오므는 카메라를 들고 천천히 주변을 둘러봤다."
    # 원문 2433행
    narrator "학교 건물과 나무, 길가의 벤치."
    # 원문 2435행
    narrator "평범한 풍경인데도 오므는 꽤 신중하게 구도를 잡았다."
    # 원문 2439행
    mc "뭘 그렇게 보고 있어요?"
    # 원문 2443행
    omu "빛."
    # 원문 2447행
    mc "빛이요?"
    # 원문 2451행
    omu "저기 봐라. 나뭇잎 사이로 들어오는 거."
    # 원문 2455행
    mc "아……."
    # 원문 2459행
    omu "저런 거 잘 찍으면 분위기 괜찮거든."
    # 원문 2463행
    mc "신기하네요. 전 그냥 나무인 줄 알았는데요."
    # 원문 2467행
    omu "그냥 나무 맞다."
    # 원문 2471행
    mc "……그렇네요."
    # 원문 2475행
    omu "ㅋㅋㅋ"
    # 원문 2479행
    narrator "오므가 카메라를 내게 건넸다."
    # 원문 2483행
    omu "니도 한 장 찍어볼래?"
    # 원문 2487행
    mc "제가요?"
    # 원문 2491행
    omu "어렵게 생각하지 말고 찍어봐."
    # 원문 연출: [SFX] 카메라 셔터
    $ story_sfx("shutter")
    # 원문 2497행
    omu "……."
    # 원문 2501행
    mc "어때요?"
    # 원문 2505행
    $ story_stage(faces={"omu": "confused"})
    omu "니 이거 와 이래 찍었노."
    # 원문 2509행
    mc "……많이 이상해요?"
    # 원문 2513행
    omu "하늘이 반이고 건물이 반인데, 정작 찍으려던 나무는 어디 갔노?"
    # 원문 2517행
    mc "하늘이 예뻐서요."
    # 원문 2521행
    omu "그건 인정."
    # 원문 2523행
    omu "근데 주제가 나무라며."
    # 원문 2527행
    mc "……."
    $ story_stage(faces={"omu": "happy"})  # 원문 2531행
    $ story_effect("bounce", "omu")
    omu "하하, 괜찮다. 처음엔 그럴 수도 있지."
    # 원문 2535행
    omu "자, 여기 봐봐라."
    # 원문 2539행
    narrator "오므는 카메라를 다시 들고 구도를 잡았다."
    # 원문 2541행
    narrator "같은 장소였지만 화면 안에 보이는 풍경은 완전히 달랐다."
    # 원문 2545행
    mc "오, 진짜 다르네요."
    # 원문 2549행
    omu "그렇지?"
    # 원문 2553행
    mc "오므 씨, 사진 잘 찍네요."
    # 원문 2557행
    omu "뭐, 좋아하니까 자주 찍는 거지."
    # 원문 2561행
    mc "영화도 좋아한다고 했죠?"
    # 원문 2565행
    omu "어. 영화 볼 때도 화면 구도 같은 거 자꾸 보게 되더라."
    # 원문 2569행
    mc "그럼 영화 보는 게 힘들지 않아요?"
    # 원문 2573행
    omu "아이다. 오히려 재밌다."
    # 원문 선택지: 사진에 대한 생각
    menu:
        "사진에는 찍는 사람의 취향이 보이는 것 같아요.":
            # 원문 2587행
            omu "그 말 좀 괜찮네."
            # 원문 2589행
            omu "맞다. 사람마다 보는 게 다르니까."
            $ story_apply("ch01_sc07_omu_a")
        "전 그냥 잘 나온 사진이 좋던데요.":
            # 원문 2595행
            omu "그것도 맞지."
            # 원문 2597행
            omu "결국 마음에 드는 사진이면 되는 거 아이가."
            $ story_apply("ch01_sc07_omu_b")
        "저도 사진 좀 배워볼까요?":
            # 원문 2603행
            omu "배워보게?"
            # 원문 2605행
            omu "그럼 다음에 내가 좀 알려줄게."
            # 원문 2609행
            mc "진짜요?"
            # 원문 2613행
            omu "어. 대신 아까처럼 찍으면 다시 찍는다."
            $ story_apply("ch01_sc07_omu_c")

    # 원문 2619행
    narrator "우리는 몇 장의 사진을 더 찍었다."
    # 원문 2621행
    narrator "돌아가는 길에 오므는 마지막으로 카메라 화면을 확인했다."
    # 원문 2625행
    omu "오늘 찍은 건 나중에 보내줄게."
    # 원문 2629행
    mc "고마워요."
    # 원문 2633행
    omu "뭐, 같이 찍었으니까."
    # 원문 2637행
    mc "그런데 진짜 서울말 쓴다고 생각해요?"
    # 원문 2641행
    omu "내 서울말 쓰는데?"
    # 원문 2645행
    mc "……그렇군요."
    # 원문 2649행
    $ story_stage(faces={"omu": "smug"})
    omu "니 그 표정 뭔데."
    # 원문 2653행
    mc "아무것도 아니에요."
    # 원문 2657행
    omu "말해봐라."
    # 원문 2661행
    $ story_stage(faces={"omu": "happy"})
    narrator "오므는 웃으며 내 쪽을 바라봤다."
    # 원문 2663행
    narrator "조금 강하게 들리는 말투였지만, 함께 지내다 보니 생각보다 편하게 느껴졌다."
    # 원문 연출: [FLAG] omu_photo_event = True
    $ story_flag("omu_photo_event", True)
    $ secret_note_unlock("omu", 1)
    jump ch01_sc08

# SC07-E · 하린: 설계도에 없는 변수 / 원문 2669행
label ch01_sc07_lumi:
    $ phone_timeline_enter("CH01", "ch01_sc07_lumi")
    # 원문 연출: [BG] 건축학과 작업실
    $ sd_event_end(mode="normal", cast=["lumi"])
    $ story_scene("architecture", mode="normal", cast=["lumi"], light="day", location="건축학과 작업실")
    # 원문 연출: [BGM] Calm Workshop
    $ play_bgm("warm_workshop")
    # 원문 연출: [SPRITE] 하린 · 기본 표정
    $ story_stage(mode="normal", cast=["lumi"], faces={'lumi': 'normal'})
    $ story_enter("lumi", side="right")
    # 원문 2679행
    narrator "하린이가 안내한 작업실에는 책상마다 도면과 모형이 놓여 있었다."
    # 원문 2681행
    narrator "깔끔하게 정리된 책상도 있었고, 작업 중인 재료로 가득한 책상도 있었다."
    # 원문 2685행
    lumi "여기 앉아요."
    # 원문 2689행
    mc "모형 만드는 거 처음 봐요."
    # 원문 2693행
    lumi "생각보다 별거 없어요."
    # 원문 2695행
    lumi "자르고, 붙이고, 다시 고치고."
    # 원문 2699행
    mc "듣기만 하면 쉬워 보이네요."
    # 원문 2703행
    lumi "그렇죠?"
    # 원문 2705행
    lumi "막상 하면 쉽지 않지만."
    # 원문 2709행
    narrator "하린이는 자와 종이를 꺼내 책상 위에 올려놓았다."
    # 원문 2713행
    lumi "일단 부스 공간을 대략적으로 나눠보려고요."
    # 원문 2717행
    mc "저기 사진 전시 공간이 있고……."
    # 원문 2721행
    lumi "네. 그리고 이쪽은 글을 남기는 공간."
    # 원문 2725행
    mc "그럼 이 가운데는요?"
    # 원문 2729행
    lumi "관람객이 이동하는 길이죠."
    # 원문 2733행
    mc "근데 여기 들어왔다가 나가려면 조금 돌아가야 하지 않아요?"
    # 원문 2737행
    $ story_stage(faces={"lumi": "serious"})
    lumi "……."
    # 원문 2741행
    narrator "하린이는 내가 가리킨 곳을 잠시 바라봤다."
    # 원문 2743행
    narrator "그리고 다시 도면을 확인했다."
    # 원문 2747행
    lumi "그러네."
    # 원문 2751행
    mc "어, 진짜요?"
    # 원문 2755행
    lumi "응. 내가 그 부분을 놓쳤네."
    # 원문 2759행
    mc "별생각 없이 말한 건데요."
    # 원문 2763행
    lumi "별생각 없이 발견하기엔 꽤 중요한 부분인데요?"
    # 원문 2767행
    lumi "눈썰미가 좋네."
    # 원문 2771행
    mc "칭찬이에요?"
    # 원문 2775행
    lumi "그럼요."
    # 원문 2777행
    lumi "혹시 의심하시는 건가?"
    # 원문 2781행
    mc "평소에 사람 놀리는 걸 좋아하는 것 같아서요."
    # 원문 2785행
    $ story_stage(faces={"lumi": "smug"})
    lumi "……벌써 들켰어요?"
    # 원문 2789행
    narrator "하린이는 조금도 당황하지 않고 웃었다."
    # 원문 2793행
    lumi "그럼 하나 더 물어볼까요?"
    # 원문 선택지: 공간 개선
    menu:
        "동선을 조금 더 단순하게 만들어요.":
            # 원문 2807행
            lumi "좋아요. 그게 제일 현실적인 방향일 수도 있겠네요."
            $ story_apply("ch01_sc07_lumi_a")
        "사진 공간을 더 넓히면 좋겠어요.":
            # 원문 2813행
            lumi "사진에 집중하게 만드는 것도 괜찮죠."
            # 원문 2815행
            lumi "다만 다른 공간이 조금 좁아질 수 있겠어요."
            $ story_apply("ch01_sc07_lumi_b")
        "앉아서 쉴 공간도 있으면 좋겠는데요.":
            # 원문 2821행
            lumi "쉬는 공간이라……."
            # 원문 2823행
            $ story_icon("lumi", "lightbulb")
            lumi "그거 좋은 생각인데?"
            # 원문 2825행
            lumi "잠시 머물러도 되는 전시라면 더 편하겠네요."
            $ story_apply("ch01_sc07_lumi_c")

    # 원문 2831행
    narrator "하린이는 도면에 몇 개의 선을 더 그었다."
    # 원문 2833행
    narrator "그리고 불필요한 선 하나를 지웠다."
    # 원문 2837행
    mc "이렇게 바꿔도 괜찮아요?"
    # 원문 2841행
    lumi "그럼요. 원래 계획은 수정하라고 있는 거니까."
    # 원문 2845행
    mc "하린 씨는 이런 거 엄청 깔끔하게 해야 직성이 풀리는 분인 줄 알았어요."
    # 원문 2849행
    lumi "깔끔한 건 좋아해요."
    # 원문 2851행
    lumi "특히 각진 건 더 좋고."
    # 원문 2855행
    mc "각진 거요?"
    # 원문 2859행
    lumi "네. 반듯하게 맞아떨어지는 게 보기 좋잖아요."
    # 원문 2863행
    mc "그렇다고 모든 걸 네모로 만들 순 없잖아요."
    # 원문 2867행
    lumi "그래서 세상이 어려운 거죠."
    # 원문 2871행
    mc "……농담이죠?"
    # 원문 2875행
    lumi "반쯤은요."
    # 원문 2879행
    $ story_stage(faces={"lumi": "happy"})
    narrator "하린이는 다시 웃었다."
    # 원문 2881행
    narrator "말투는 여유로웠지만 작업할 때만큼은 상당히 집중하는 사람이었다."
    $ story_icon("lumi", "heart")  # 원문 2885행
    lumi "오늘 도와줘서 고마워요."
    # 원문 2889행
    mc "별로 한 것도 없는데요."
    # 원문 2893행
    lumi "아뇨. 혼자 했으면 못 봤을 수도 있는 부분이었으니까."
    # 원문 2897행
    lumi "다음에도 같이 봐주실래요?"
    # 원문 2901행
    mc "네, 좋아요."
    # 원문 2905행
    lumi "후후. 그럼 잘 부탁할게."
    # 원문 연출: [FLAG] rumi_design_event = True
    $ story_flag("rumi_design_event", True)
    $ secret_note_unlock("lumi", 1)
    $ story_exit("lumi", side="right")
    if _preferences.transitions:
        $ renpy.pause(0.26)
    jump ch01_sc08

# SC08 · 계획에 없던 문제 / 원문 2911행
label ch01_sc08:
    $ phone_timeline_enter("CH01", "ch01_sc08")
    # 원문 연출: [BG] 공동 동아리실 · 저녁
    $ sd_event_end(mode="normal", cast=["sia", "roman", "darim", "omu", "lumi"])
    $ story_scene("clubroom307", mode="normal", cast=["sia", "roman", "darim", "omu", "lumi"], light="evening", location="동아리실 307호 · 저녁")
    # 원문 연출: [BGM] Calm Evening
    $ play_bgm("evening_warm")
    # 원문 2919행
    narrator "각자의 작업을 마치고 다시 동아리실에 모였다."
    # 원문 2921행
    narrator "아침보다 책상 위의 종이가 많아졌고, 화이트보드에는 할 일이 빼곡히 적혀 있었다."
    # 원문 2925행
    sia "아……."
    # 원문 2929행
    sia "나 진짜 열심히 했다."
    # 원문 2933행
    omu "니 아직 콘티만 그린 거 아이가?"
    # 원문 2937행
    sia "콘티가 제일 중요하거든?"
    # 원문 2941행
    lumi "그건 맞는 말이에요."
    # 원문 2945행
    sia "오? 하린이가 내 편을?"
    # 원문 2949행
    lumi "완성까지 얼마나 걸릴지는 모르겠지만요."
    # 원문 2953행
    $ story_stage(faces={"sia": "angry"})
    $ story_effect("shake", "sia")
    sia "……취소. 내 편 아니네."
    # 원문 2957행
    $ story_stage(faces={"darim": "happy"})
    darim "다들 오늘 수고 많으셨어요."
    # 원문 2961행
    $ story_stage(faces={"roman": "surprised"})
    $ story_effect("jump", "roman")
    $ story_icon("roman", "exclamation")
    roman "앗,,, 생각보다 많이 했네요……!"
    # 원문 2965행
    $ story_stage(faces={"roman": "happy"})
    mc "그러게요. 처음에는 무슨 프로젝트인지도 잘 몰랐는데요."
    # 원문 2969행
    omu "이제 좀 감이 잡히지?"
    # 원문 2973행
    mc "네. 생각보다 재미있어요."
    # 원문 2977행
    $ story_stage(faces={"sia": "smug"})
    sia "그치? 내가 있으니까."
    # 원문 2981행
    omu "니는 안 빠지는 데가 없네."
    # 원문 연출: [SFX] 메시지 알림
    $ story_sfx("message")
    # 원문 2987행
    darim "어? 축제 운영위원회에서 연락이 왔네요."
    # 원문 2991행
    narrator "다림이 휴대전화를 확인하고, 우리도 볼 수 있게 화면을 돌려 주었다."
    # 원문 2993행
    $ story_stage(faces={"darim": "serious"})
    narrator "조금 전까지 부드럽던 표정이 진지해졌다."
    # 원문 2997행
    darim "……잠깐만요."
    # 원문 3001행
    sia "왜? 무슨 일인데?"
    # 원문 연출: [BGM] 음악 페이드아웃 후 Light Tension
    $ play_bgm("light_tension")
    show screen campus_space_notice
    # 원문 3007행
    darim "부스 공간 배정이 변경됐대요."
    # 원문 3011행
    $ story_stage(faces={"lumi": "surprised"})
    lumi "변경이요?"
    # 원문 3015행
    darim "네. 신청한 구역의 사용 가능한 공간이 줄어들었다고 해요."
    hide screen campus_space_notice  # 원문 3019행
    omu "얼마나 줄었는데요?"
    # 원문 3023행
    darim "정확한 도면은 추가로 보내준다고 하는데……."
    # 원문 3027행
    darim "지금 계획보다는 작아질 것 같아요."
    # 원문 3031행
    sia "……."
    # 원문 3035행
    sia "야, 잠깐."
    # 원문 3039행
    sia "그럼 내 웹툰 30컷짜리 대작은?"
    # 원문 3043행
    omu "니 언제 30컷 됐는데?"
    # 원문 3047행
    sia "방금."
    # 원문 3051행
    $ story_stage(faces={"lumi": "serious"})
    lumi "일단 공간부터 다시 확인해야겠네요."
    # 원문 3055행
    roman "앗,,, 글도 조금 줄여야 할까요……?"
    # 원문 3059행
    darim "아직 결정된 건 아니니까요. 구체적인 내용을 먼저 확인해 보죠."
    # 원문 3063행
    mc "그래도 우리가 지금까지 한 게 다 소용없어지는 건 아니잖아요."
    # 원문 3067행
    lumi "맞아. 배치를 바꾸면 되는 부분도 있을 거예요."
    # 원문 3071행
    omu "사진 크기도 조정하면 되고."
    # 원문 3075행
    sia "……만화도 줄이면 되긴 하지."
    # 원문 3079행
    omu "아까는 30컷 포기 못 한다며."
    # 원문 3083행
    sia "그건 창작자의 자존심이었고."
    # 원문 3087행
    sia "지금은 생존의 문제야."
    # 원문 연출: [SD] 시아가 두 손을 머리에 올리고 절망한다.
    $ story_stage(faces={"sia": "embarrassed"})
    # 원문 3093행
    roman "저도 문구를 조금 더 짧게 만들어 볼게요."
    # 원문 3097행
    darim "그럼 수정할 부분을 정리해 둘게요."
    # 원문 3101행
    mc "좋아요. 내일 다시 모여서 맞춰봐요."
    # 원문 3105행
    narrator "예상하지 못한 일이었지만, 모두 생각보다 빠르게 다시 움직이기 시작했다."
    # 원문 3107행
    narrator "회의가 처음 시작됐을 때와는 조금 달랐다."
    # 원문 3111행
    lumi "……그런데 한 가지 걸리는 게 있어요."
    # 원문 3115행
    mc "뭔데요?"
    # 원문 3119행
    lumi "공간이 줄어든 이유가 정확하게 안 적혀 있네요."
    # 원문 3123행
    darim "내일 추가 공지가 나온다고 하니까 그때 확인해 봐요."
    # 원문 3127행
    sia "설마 다른 팀이랑 같이 쓰는 건 아니겠지?"
    # 원문 3131행
    omu "그럼 진짜 좁아질 것 같은데."
    # 원문 3135행
    lumi "아직은 모르죠."
    # 원문 3139행
    narrator "그 말에 모두 잠시 조용해졌다."
    # 원문 3141행
    narrator "하지만 오래가지는 않았다."
    # 원문 3145행
    sia "뭐, 어떻게든 되겠지!"
    # 원문 3149행
    darim "그렇게 낙관적으로만 생각하시면 안 되지만……."
    # 원문 3153행
    sia "아, 알았어. 내일 열심히 할게!"
    # 원문 3157행
    omu "그 말 녹음해둘걸."
    # 원문 3161행
    sia "야!"
    # 원문 3165행
    narrator "다시 시끌벅적한 목소리가 동아리실을 채웠다."
    # 원문 3167행
    narrator "나는 그 모습을 바라보다가 피식 웃었다."
    # 원문 3171행
    mc "……내일도 재미있겠네."
    # 주인공 방으로 이동할 때 공통 배경 슬라이드를 사용한다.
    $ sd_event_end(mode="normal", cast=[])



    # 원문 연출: [FLAG] space_issue_discovered = True
    $ story_flag("space_issue_discovered", True)
    # 원문 연출: [SCENE 08 END]
    jump ch01_sc09

# SC09 · 단체 채팅방이 만들어졌다 / 원문 3179행
label ch01_sc09:
    $ phone_timeline_enter("CH01", "ch01_sc09")
    # 원문 연출: [BG] 주인공 방 · 밤
    $ sd_event_end(mode="normal", cast=[])
    $ story_scene("room", mode="normal", cast=[], light="night", location="주인공 방 · 밤")
    # 원문 연출: [BGM] Night Campus
    $ play_bgm("night_campus")
    # 원문 3187행
    $ cg_start("ld_03")
    narrator "길었던 하루가 끝났다."
    # 원문 3189행
    narrator "방으로 돌아와 짐을 내려놓고 침대에 누웠다."
    # 원문 3193행
    mc "아…… 피곤해."
    # 원문 3197행
    narrator "오늘 있었던 일을 하나씩 떠올려 보았다."
    # 원문 3199행
    narrator "처음 만난 사람들."
    # 원문 3201행
    narrator "시끄러운 회의."
    # 원문 3203행
    narrator "예상보다 재미있었던 작업."
    # 원문 3205행
    narrator "그리고 갑자기 생긴 문제까지."
    # 원문 3209행
    mc "……하루 만에 별일이 다 있었네."
    # 원문 연출: [SFX] 휴대전화 알림
    # 알림음은 휴대폰 이벤트 시작에 재생.
    # 원문 연출: [UI] 스마트폰 채팅 화면 표시
    $ story_chat(True, title="축제 준비팀")
    # 원문 3215행
    system_note "「시아 님이 '축제 준비팀' 채팅방을 만들었습니다.」"
    # 원문 3217행
    system_note "「시아 님이 다림, 오므, 로만, 하린, [player_name] 님을 초대했습니다.」"
    # 원문 3221행
    sia "야 다들 살아있냐"
    # 원문 3225행
    omu "니만 시끄럽다"
    # 원문 3229행
    sia "아니 다들 집 잘 갔냐고ㅋㅋ"
    # 원문 3233행
    darim "네. 저도 방금 도착했어요."
    # 원문 3237행
    roman "앗,,, 저도 잘 도착했어요……!"
    # 원문 3241행
    lumi "저도요. 오늘 수고 많으셨어요."
    # 원문 3245행
    sia "내일도 이 시간에 모이는 거?"
    # 원문 3249행
    darim "아뇨. 내일은 각자 수업이 있으니까 오후에 일정 맞춰보죠."
    # 원문 3253행
    sia "오케이"
    # 원문 3257행
    omu "내일은 안 늦을 거지?"
    # 원문 3261행
    sia "당연하지"
    # 원문 3265행
    omu "니 오늘도 늦었잖아"
    # 원문 3269행
    sia "응 아니야~ 5분은 지각 아님"
    # 원문 3273행
    lumi "그럼 음료수 쏟은 것도 실수 아니라고 해드릴까요?"
    # 원문 3277행
    sia "아 진짜 그만해ㅋㅋㅋㅋ"
    # 원문 3281행
    roman "앗,,, 저 내일 음료수 안 가져갈게요……."
    # 원문 3285행
    darim "로만 씨까지 그러실 필요는 없어요."
    # 원문 3289행
    omu "ㅋㅋㅋㅋㅋㅋ"
    # 원문 3293행
    mc "다들 진짜 친하네요."
    # 원문 3297행
    sia "어 당연하지"
    # 원문 3301행
    lumi "그렇죠. 특히 시아 씨가 저를 많이 기억해 주셔서요."
    # 원문 3305행
    sia "아니 그 기억은 좀 지워줘!!!"
    # 원문 3309행
    narrator "나는 채팅창을 바라보며 웃었다."
    # 원문 3311행
    narrator "정말 이상한 사람들이다."
    # 원문 3313행
    narrator "하지만 이상하게도 낯설지는 않았다."
    # 원문 연출: [SFX] 개인 메시지 알림
    # 알림음은 휴대폰 이벤트 시작에 재생.
    # 원문 연출: [UI] 단체 채팅에서 개인 메시지 화면으로 전환
    if first_task_partner == "roman":
        $ story_chat(True, title="로만 · 개인 메시지")
        # 원문 3325행
        roman "앗,,, 늦은 시간에 연락드려서 괜찮을까요……?"
        # 원문 3327행
        roman "오늘 같이 책 찾아주셔서 감사했어요."
        # 원문 3329행
        roman "덕분에 생각보다 좋은 문구를 찾은 것 같아요."
        # 원문 3333행
        mc "저도 재미있었어요. 내일 봐요."
        # 원문 3337행
        roman "네……! 내일 뵐게요."
        # 원문 3339행
        roman "좋은 밤 보내세요……!"
    elif first_task_partner == "sia":
        $ story_chat(True, title="시아 · 개인 메시지")
        # 원문 3345행
        sia "야ㅋㅋ 오늘 그 콘티 다시 봤는데"
        # 원문 3347행
        sia "생각보다 잘 나옴"
        # 원문 3351행
        mc "그렇게 열심히 그렸는데 당연하죠."
        # 원문 3355행
        sia "오 칭찬?"
        # 원문 3357행
        sia "좋아 내일도 감상 담당 예약이다"
        # 원문 3361행
        mc "감상료부터 주세요."
        # 원문 3365행
        sia "응 아니야~"
    elif first_task_partner == "darim":
        $ story_chat(True, title="다림 · 개인 메시지")
        # 원문 3371행
        darim "오늘 일정표 정리 도와주셔서 감사했어요."
        # 원문 3373행
        darim "덕분에 생각보다 빨리 끝났네요."
        # 원문 3377행
        mc "선배가 거의 다 하셨잖아요."
        # 원문 3381행
        darim "후후. 같이 해서 더 빨랐던 거죠."
        # 원문 3383행
        darim "다음에도 잘 부탁드려요."
    elif first_task_partner == "omu":
        $ story_chat(True, title="오므 · 개인 메시지")
        # 원문 3389행
        omu "야 오늘 사진 정리했는데"
        # 원문 3391행
        omu "생각보다 괜찮게 나왔다"
        # 원문 3395행
        mc "제가 찍은 것도요?"
        # 원문 3399행
        omu "……"
        # 원문 3401행
        omu "그건 좀 더 연습해야겠다ㅋㅋ"
        # 원문 3405행
        mc "역시 그렇군요."
        # 원문 3409행
        omu "다음에 또 찍으러 가자."
    elif first_task_partner == "lumi":
        $ story_chat(True, title="하린 · 개인 메시지")
        # 원문 3415행
        lumi "오늘 같이 봤던 부스 배치도 수정해 봤어요."
        # 원문 3417행
        lumi "내일 한번 보여드릴게요."
        # 원문 3421행
        mc "벌써 수정했어요?"
        # 원문 3425행
        lumi "네. 마음에 걸리면 계속 보게 되더라고."
        # 원문 3427행
        lumi "그래도 오늘은 덕분에 도움이 많이 됐어요."
        # 원문 3431행
        mc "저도 재미있었어요."
        # 원문 3435행
        lumi "후후. 다음에도 잘 부탁할게."

    # 원문 연출: [개인 메시지 종료]
    $ story_chat(False)
    # 원문 연출: [BG] 주인공 방 · 밤
    $ sd_event_end(mode="normal", cast=[])
    $ story_scene("room", mode="normal", cast=[], light="night", location="주인공 방 · 밤")
    # 원문 연출: [BGM] 잔잔한 엔딩 테마
    $ play_bgm("chapter_ending_reprise")
    # 원문 3445행
    narrator "휴대전화를 내려놓고 천장을 바라봤다."
    # 원문 3447행
    narrator "처음에는 그저 새로운 사람들을 만나보고 싶었다."
    # 원문 3449행
    narrator "반복되는 대학생활에서 조금은 색다른 일을 해보고 싶었을 뿐이다."
    # 원문 3451행
    narrator "그런데 막상 참여하고 나니 예상했던 것과는 전혀 다른 하루가 되어 있었다."
    # 원문 3453행
    narrator "시끄럽고."
    # 원문 3455행
    narrator "정신없고."
    # 원문 3457행
    narrator "가끔은 이해할 수 없는 말이 오가기도 하고."
    # 원문 3461행
    mc "……다들 조금씩 이상해."
    # 원문 3465행
    narrator "그래도 나쁘지는 않았다."
    # 원문 3467행
    narrator "오히려 내일이 조금 기다려졌다."
    # 원문 3471행
    mc "축제 준비…… 생각보다 재미있을지도."
    # 원문 연출: [SFX] 새로운 메시지 도착
    # 알림음은 휴대폰 이벤트 시작에 재생.
    # 원문 연출: [UI] 운영위원회 공지
    $ story_chat(True, title="축제 운영위원회")  # 원문 3477행
    system_note "「축제 부스 공간 배정 관련 추가 안내」"
    # 원문 3479행
    system_note "「동일 구역 신청 팀이 확인되어 일부 부스의 배정 절차가 변경될 예정입니다.」"
    # 원문 3481행
    system_note "「자세한 내용은 내일 공지하겠습니다.」"
    $ story_chat(False)  # 원문 3485행
    mc "……동일 구역 신청 팀?"
    # 원문 3489행
    narrator "설마, 다른 팀이랑 경쟁해야 한다는 건 아니겠지."
    # 원문 3491행
    narrator "……아니겠지?"
    # 원문 연출: [BGM] 정지
    stop music fadeout 0.5
    # 원문 연출: [FADE TO BLACK]
    $ story_fade_out()
    scene black
    with fade
    # 원문 3497행
    system_note "「CH01 완료」"
    # 원문 3499행
    system_note "「다음 이야기」"
    # 원문 3501행
    system_note "「우리 옆 부스가 수상하다」"
    # 원문 연출: [FLAG] chapter01_complete = True
    $ story_complete_chapter(1)
    # 원문 연출: [CHAPTER 01 END]
    jump chapter02

