# Roman R01 · dialogue-only storyboard import
# SOURCE: design_docs/story_sources/roman_r01.txt
# SHA256: 4a290045ffefbae93ca78501a833d9953585cef0fa6d5f72b1262658d7e17eca
# Rebuild: tools/import_roman_first.py --write
# CONTI markers intentionally do not load standing, SD, or LD artwork.

default roman_r01_book_choice = None
default roman_mutual_understanding = 0
default roman_shared_reading = 0
default roman_reading_event_goal_known = False
default roman_mutual_respect = 0
default roman_first_reader_promise = False
default roman_r01_complete = False

label roman_r01:
    $ phone_timeline_enter("R01", "roman_r01")
    $ roman_begin_episode("R01", "책갈피에 남겨둔 약속")
    jump roman_r01_sc01

label roman_r01_sc01:
    $ phone_timeline_enter("R01", "roman_r01_sc01")
    # SOURCE R01 L31 SCENE 01. 다음 페이지를 넘기기 전에
    # CONTI SOURCE R01 L32 [TIME] CH07 종료 사흘 후 · 오후 12:40 · 주인공 방
    $ phone_timeline_cue("R01", "R01_L32")
    # SOURCE R01 L34 [BG] 주인공 방 · 낮
    $ story_draft_scene("주인공 방 · 낮")
    # SOURCE R01 L36 [BGM] Ordinary Afternoon
    $ story_draft_bgm("Ordinary Afternoon")
    # CONTI SOURCE R01 L38 [FADE IN]
    # SOURCE R01 L42
    narrator "책장을 넘겼다."
    # SOURCE R01 L44
    narrator "그리고 다시 앞장으로 돌아갔다."
    # SOURCE R01 L46
    narrator "……이상하다."
    # SOURCE R01 L48
    narrator "같은 문장을 세 번째 읽고 있는데도 좀처럼 집중이 되지 않는다."
    # SOURCE R01 L50
    narrator "책이 어려운 건 아니다."
    # SOURCE R01 L52
    narrator "그냥 다른 생각이 자꾸 떠오를 뿐이다."
    # SOURCE R01 L54
    narrator "며칠 전 도서관에서 로만 씨와 함께 읽었던 책."
    # SOURCE R01 L56
    narrator "그리고 헤어질 때 나눴던 짧은 약속."
    # CONTI SOURCE R01 L58 [FLASHBACK · CH07 SC06-A]
    $ story_flashback_set(True)
    # SOURCE R01 L60 (로만)
    roman "그럼 다음에는 제가 먼저 연락드릴게요."
    # SOURCE R01 L62 (주인공)
    mc "기다릴게요."
    # CONTI SOURCE R01 L64 [FLASHBACK END]
    $ story_flashback_set(False)
    # SOURCE R01 L68
    narrator "그렇게 말하고 헤어졌는데."
    # SOURCE R01 L70
    narrator "그 이후로 로만 씨에게서 별다른 연락은 없었다."
    # SOURCE R01 L72
    narrator "물론 이상할 일은 아니다."
    # SOURCE R01 L74
    narrator "서로 수업도 있고 과제도 있으니까."
    # SOURCE R01 L76
    narrator "……그렇긴 한데."
    # CONTI SOURCE R01 L78 [SFX] 휴대전화 진동
    # SOURCE R01 L82 (주인공 · 혼잣말)
    mc "……어?"
    # CONTI SOURCE R01 L84 [UI] 스마트폰 화면 · 로만 개인 메시지
    $ story_chat(True, title="로만")
    # SOURCE R01 L86 (로만)
    roman "앗,,, 안녕하세요……!"
    # SOURCE R01 L88 (로만)
    roman "혹시 오늘 바쁘세요……?"
    # SOURCE R01 L92
    narrator "……정말 연락이 왔다."
    # SOURCE R01 L94
    narrator "타이밍이 조금 놀라울 정도다."
    # SOURCE R01 L96 (주인공 · 메시지)
    mc "안녕하세요, 로만 씨. 오늘은 오후에 시간이 있어요."
    # SOURCE R01 L98 (로만)
    roman "앗, 다행이에요……!"
    # SOURCE R01 L100 (로만)
    roman "그럼 혹시……."
    # SOURCE R01 L102 (로만)
    roman "같이 서점에 가실래요?"
    # SOURCE R01 L104 (주인공 · 메시지)
    mc "좋아요. 어떤 책 찾으세요?"
    # SOURCE R01 L106 (로만)
    roman "읽어보고 싶은 책이 몇 권 있어서요."
    # SOURCE R01 L108 (로만)
    roman "그런데 혼자 고르려니까 조금 고민돼서……."
    # SOURCE R01 L110 (주인공 · 메시지)
    mc "그럼 같이 골라봐요."
    # SOURCE R01 L112 (로만)
    roman "……네!"
    # SOURCE R01 L114 (로만)
    roman "그럼 두 시에 학교 앞 서점에서 뵐게요……!"
    $ story_chat(False)
    # SOURCE R01 L118
    narrator "휴대전화를 내려놓았다."
    # SOURCE R01 L120
    narrator "그렇게 기다리던 연락이 왔는데."
    # SOURCE R01 L122
    narrator "막상 약속이 잡히고 나니 조금 이상했다."
    # SOURCE R01 L124
    narrator "그냥 서점에 같이 가는 것뿐이다."
    # SOURCE R01 L126
    narrator "그런데 왜 괜히 시계를 확인하게 되는 걸까."
    # SOURCE R01 L130 (주인공 · 혼잣말)
    mc "……아직 한 시간이나 남았는데."
    # SOURCE R01 L134
    narrator "나는 책을 덮었다."
    # SOURCE R01 L136
    narrator "어차피 지금은 글자가 눈에 들어올 것 같지 않았다."
    # CONTI SOURCE R01 L138 [TRANSITION] 오후 1:55 · 학교 앞 거리
    $ phone_timeline_cue("R01", "R01_L138")
    # SOURCE R01 L140 [BG] 학교 앞 거리 · 맑은 오후
    $ story_draft_scene("학교 앞 거리 · 맑은 오후")
    # SOURCE R01 L142 [BGM] Light Campus
    $ story_draft_bgm("Light Campus")
    # SOURCE R01 L146
    narrator "서점으로 향하는 길."
    # SOURCE R01 L148
    narrator "손에는 작은 가방 하나만 들려 있었다."
    # SOURCE R01 L150
    narrator "축제 준비 때처럼 자료를 챙길 필요도, 물품 목록을 확인할 필요도 없었다."
    # SOURCE R01 L152
    narrator "이제는 정말 개인적인 약속이다."
    # SOURCE R01 L154
    narrator "그 사실이 조금 새롭게 느껴졌다."
    # CONTI SOURCE R01 L156 [SFX] 휴대전화 알림
    $ story_chat(True, title="로만")
    # SOURCE R01 L158 (로만)
    roman "앗,,, 저 도착했어요!"
    # SOURCE R01 L160 (로만)
    roman "급하게 오시지 않으셔도 돼요……!"
    # SOURCE R01 L162 (주인공 · 메시지)
    mc "저도 거의 도착했어요. 금방 뵐게요."
    $ story_chat(False)
    # SOURCE R01 L166
    narrator "발걸음이 조금 빨라졌다."
    # SOURCE R01 L168
    narrator "……급하게 오지 않아도 된다면서."
    # SOURCE R01 L170
    narrator "왜 나는 이렇게 빨리 가고 있는 거지?"
    # CONTI SOURCE R01 L172 [SCENE 01 END]
    jump roman_r01_sc02

label roman_r01_sc02:
    $ phone_timeline_enter("R01", "roman_r01_sc02")
    # SOURCE R01 L175 SCENE 02. 책을 고르는 방식
    # CONTI SOURCE R01 L176 [TIME] 오후 2:00 · 학교 앞 독립서점 · 개인적인 첫 외출
    $ phone_timeline_cue("R01", "R01_L176")
    # SOURCE R01 L178 [BG] 작은 독립서점 · 오후
    $ story_draft_scene("작은 독립서점 · 오후")
    # SOURCE R01 L180 [BGM] Cozy Bookstore
    $ story_draft_bgm("Cozy Bookstore")
    # CONTI SOURCE R01 L182 [LD] 로만 · 기본 미소
    # SOURCE R01 L186
    narrator "서점 앞에 도착하자 로만 씨가 책 한 권을 들고 서 있었다."
    # SOURCE R01 L188
    narrator "내가 다가가자 로만 씨는 고개를 들었다."
    # SOURCE R01 L190 (로만)
    roman "앗,,, [player_name] 씨!"
    # SOURCE R01 L192 (주인공)
    mc "안녕하세요. 많이 기다리셨어요?"
    # SOURCE R01 L194 (로만)
    roman "아니에요……! 저도 방금 왔어요."
    # SOURCE R01 L198
    narrator "로만 씨는 책을 조금 더 꼭 쥐었다."
    # SOURCE R01 L200 (주인공)
    mc "오늘은 어떤 책을 찾으세요?"
    # SOURCE R01 L202 (로만)
    roman "음……."
    # SOURCE R01 L204 (로만)
    roman "사실은 아직 정확히 정하지 못했어요."
    # SOURCE R01 L206 (주인공)
    mc "그럼 천천히 둘러볼까요?"
    # SOURCE R01 L208 (로만)
    roman "네……!"
    # SOURCE R01 L210 [BG] 서점 내부 · 문학 코너
    $ story_draft_scene("서점 내부 · 문학 코너")
    # SOURCE R01 L214
    narrator "서점은 생각보다 조용했다."
    # SOURCE R01 L216
    narrator "오래된 나무 책장 사이로 오후 햇살이 들어오고 있었다."
    # SOURCE R01 L218
    narrator "로만 씨는 익숙한 듯 문학 코너로 향했다."
    # SOURCE R01 L220 (로만)
    roman "여기 서점이 좋아요."
    # SOURCE R01 L222 (주인공)
    mc "자주 오세요?"
    # SOURCE R01 L224 (로만)
    roman "네. 가끔 수업 끝나고 들러요."
    # SOURCE R01 L226 (로만)
    roman "책이 아주 많지는 않은데……."
    # SOURCE R01 L228 (로만)
    roman "직접 고른 책들이 많아서 구경하는 재미가 있거든요."
    # SOURCE R01 L230 (주인공)
    mc "로만 씨 취향에 잘 맞는 곳이네요."
    # SOURCE R01 L232 (로만)
    roman "후후…… 그런가요?"
    # SOURCE R01 L236
    narrator "로만 씨는 책장 앞에서 잠시 멈췄다."
    # SOURCE R01 L238
    narrator "그러더니 서로 다른 두 권의 책을 꺼냈다."
    # SOURCE R01 L240 (로만)
    roman "둘 중에 뭐가 더 재미있을 것 같으세요?"
    # SOURCE R01 L242 (주인공)
    mc "음……."
    # SOURCE R01 L246
    narrator "한 권은 잔잔한 일상 소설이었다."
    # SOURCE R01 L248
    narrator "다른 한 권은 표지부터 조금 기묘한 분위기의 단편집이었다."
    # SOURCE R01 L249 [CHOICE 01 · 책 고르기]
    menu:
        # SOURCE R01 L250 선택지
        "저는 일상 소설이 끌리네요.":
            # SOURCE R01 L252 (주인공)
            mc "평범한 이야기인데 오히려 오래 기억에 남을 것 같아요."
            # SOURCE R01 L254 (로만)
            roman "앗,,, 저도 그런 이야기 좋아해요."
            # SOURCE R01 L256 (로만)
            roman "작은 장면 하나가 마음에 남는 책들이 있거든요."
            # SOURCE R01 L258 [FLAG] roman_r01_book_choice = daily
            $ story_apply("roman_r01_choice01_a", values={'roman_r01_book_choice': 'daily'})
        # SOURCE R01 L260 선택지
        "이 단편집도 재미있어 보이는데요?":
            # SOURCE R01 L262 (주인공)
            mc "표지가 조금 신비롭네요."
            # SOURCE R01 L264 (로만)
            roman "……앗."
            # SOURCE R01 L266 (로만)
            roman "그, 그건 조금 무서울 수도 있는데……."
            # SOURCE R01 L268 (주인공)
            mc "로만 씨는 무서운 책은 잘 안 읽으세요?"
            # SOURCE R01 L270 (로만)
            roman "……네."
            # SOURCE R01 L272 (로만)
            roman "궁금하기는 한데…… 읽고 나면 잠이 안 와서요."
            # SOURCE R01 L274 [FLAG] roman_r01_book_choice = mystery
            $ story_apply("roman_r01_choice01_b", values={'roman_r01_book_choice': 'mystery'})
        # SOURCE R01 L276 선택지
        "로만 씨가 좋아하시는 책을 같이 읽고 싶어요.":
            # SOURCE R01 L278 (주인공)
            mc "오늘은 로만 씨 추천을 들어보고 싶어요."
            # SOURCE R01 L280 (로만)
            roman "……!"
            # SOURCE R01 L282 (로만)
            roman "앗,,, 제 추천이요?"
            # SOURCE R01 L284 (로만)
            roman "그럼…… 조금 신중하게 골라야겠네요."
            # SOURCE R01 L286 [FLAG] roman_r01_book_choice = recommendation
            $ story_apply("roman_r01_choice01_c", values={'roman_r01_book_choice': 'recommendation'})
    # SOURCE R01 L292
    narrator "로만 씨는 두 권의 책을 다시 살펴봤다."
    # SOURCE R01 L294
    narrator "한참 고민하더니 결국 일상 소설을 책장에 되돌려 놓았다."
    # SOURCE R01 L296 (주인공)
    mc "그 책은 안 사세요?"
    # SOURCE R01 L298 (로만)
    roman "아…… 이건 이미 읽었거든요."
    # SOURCE R01 L300 (주인공)
    mc "그런데 왜 꺼내셨어요?"
    # SOURCE R01 L302 (로만)
    roman "좋아하는 책이라서요."
    # SOURCE R01 L304 (로만)
    roman "누군가에게 추천하고 싶으면 자꾸 꺼내게 돼요."
    # SOURCE R01 L306 (주인공)
    mc "그럼 저한테 추천해 주신 거네요?"
    # SOURCE R01 L308 (로만)
    roman "……."
    # CONTI SOURCE R01 L310 [LD] 로만 · 당황
    # SOURCE R01 L312 (로만)
    roman "앗,,, 그렇게 되는 건가요?"
    # SOURCE R01 L316
    narrator "로만 씨가 조금 당황했다."
    # SOURCE R01 L318
    narrator "나는 웃음을 참았다."
    # SOURCE R01 L320 (주인공)
    mc "그런 것 같은데요."
    # SOURCE R01 L322 (로만)
    roman "……그럼."
    # SOURCE R01 L324 (로만)
    roman "다음에 읽어보실래요?"
    # SOURCE R01 L326 (주인공)
    mc "네. 로만 씨가 좋아하시는 책이라니까 궁금해요."
    # SOURCE R01 L328 (로만)
    roman "……후후."
    # SOURCE R01 L332
    narrator "로만 씨는 수줍게 웃었다."
    # SOURCE R01 L334
    narrator "그러더니 조금 작은 목소리로 말했다."
    # SOURCE R01 L336 (로만)
    roman "그럼 다음에 읽고…… 감상도 같이 나눠요."
    # SOURCE R01 L338 (주인공)
    mc "좋아요."
    # SOURCE R01 L342
    narrator "책을 한 권 고르는 데 생각보다 오래 걸렸다."
    # SOURCE R01 L344
    narrator "그런데 이상하게도 지루하지 않았다."
    # SOURCE R01 L346
    narrator "로만 씨는 책마다 좋아하는 이유가 있었고, 어떤 부분이 마음에 들었는지 자세히 설명해 줬다."
    # SOURCE R01 L348
    narrator "평소에는 조용한 사람이지만."
    # SOURCE R01 L350
    narrator "좋아하는 이야기를 할 때는 말이 조금 많아지는 모양이다."
    # SOURCE R01 L352
    narrator "그걸 알게 된 게 재미있었다."
    # CONTI SOURCE R01 L354 [SCENE 02 END]
    jump roman_r01_sc03

label roman_r01_sc03:
    $ phone_timeline_enter("R01", "roman_r01_sc03")
    # SOURCE R01 L356 SCENE 03. 무서운 건 딱 질색이에요
    # CONTI SOURCE R01 L357 [TIME] 오후 2:35 · 서점 · R01 유일한 SD 코미디
    $ phone_timeline_cue("R01", "R01_L357")
    # SOURCE R01 L359 [BG] 독립서점 · 추천 도서 코너
    $ story_draft_scene("독립서점 · 추천 도서 코너")
    # SOURCE R01 L361 [BGM] Playful Bookstore
    $ story_draft_bgm("Playful Bookstore")
    # SOURCE R01 L365
    narrator "서점 안쪽에는 직원이 직접 고른 추천 도서들이 놓여 있었다."
    # SOURCE R01 L367
    narrator "로만 씨는 그중 한 권을 발견하더니 반가운 표정을 지었다."
    # SOURCE R01 L369 (로만)
    roman "앗,,, 이 작가님 책도 있네요!"
    # SOURCE R01 L371 (주인공)
    mc "좋아하시는 작가인가요?"
    # SOURCE R01 L373 (로만)
    roman "네! 문장이 정말 예뻐요."
    # SOURCE R01 L375 (로만)
    roman "특히 등장인물의 마음을 표현하는 방식이 좋아서……."
    # SOURCE R01 L379
    narrator "로만 씨는 책을 꺼내 표지를 바라봤다."
    # SOURCE R01 L381
    narrator "그런데 다음 순간."
    # SOURCE R01 L383 (로만)
    roman "……."
    # CONTI SOURCE R01 L385 [LD] 로만 · 굳은 표정
    # SOURCE R01 L387 (주인공)
    mc "로만 씨?"
    # SOURCE R01 L389 (로만)
    roman "……어."
    # SOURCE R01 L393
    narrator "책 표지에는 어두운 복도와 희미한 사람 그림자가 그려져 있었다."
    # SOURCE R01 L395
    narrator "제목 아래에는 작은 글씨가 적혀 있었다."
    # SOURCE R01 L397
    narrator "「기묘한 밤의 이야기」"
    # SOURCE R01 L399 (로만)
    roman "……."
    # SOURCE R01 L401 (주인공)
    mc "왜 그러세요?"
    # SOURCE R01 L403 (로만)
    roman "이, 이 작가님이……."
    # SOURCE R01 L405 (로만)
    roman "이번에는 공포 소설을 쓰셨나 봐요……."
    # SOURCE R01 L407 (주인공)
    mc "아, 그러네요."
    # SOURCE R01 L409 (로만)
    roman "……."
    # SOURCE R01 L413
    narrator "로만 씨는 책을 조용히 내려놓았다."
    # SOURCE R01 L415
    narrator "손끝이 조금 빨라졌다."
    # SOURCE R01 L417 (주인공)
    mc "안 읽으세요?"
    # SOURCE R01 L419 (로만)
    roman "아, 아니……."
    # SOURCE R01 L421 (로만)
    roman "그냥…… 오늘은 다른 책을 먼저 읽으려고요."
    # SOURCE R01 L423 (주인공)
    mc "무서우셔서요?"
    # SOURCE R01 L425 (로만)
    roman "……."
    # SOURCE R01 L427 (로만)
    roman "쪼, 조금요."
    # SOURCE R01 L431
    narrator "로만 씨는 부끄러운 듯 고개를 숙였다."
    # SOURCE R01 L433
    narrator "그 순간 서점의 안내 스피커에서 음성이 나왔다."
    # CONTI SOURCE R01 L435 [SFX] 서점 안내 방송 시작
    # SOURCE R01 L437 (안내 음성)
    narrator "안내 음성: 이번 주 추천 도서는……."
    # CONTI SOURCE R01 L439 [SFX] 스피커 잡음
    # SOURCE R01 L441 (로만)
    roman "앗?!"
    # CONTI SOURCE R01 L443 [SD EVENT] roman_r01_ghost_book_comedy
    # CONTI SOURCE R01 L445 [연출] 로만이 공포 소설을 들고 놀란 표정으로 굳어 있고, 주변에는 평범한 서점 책장과 스피커가 있는 완성형 SD 일러스트 1장. 주인공은 화면 밖에 존재.
    # SOURCE R01 L447 [BGM] Comical Panic
    $ story_draft_bgm("Comical Panic")
    # SOURCE R01 L449 (로만)
    roman "……!"
    # SOURCE R01 L451 (주인공)
    mc "로만 씨, 괜찮으세요?"
    # SOURCE R01 L453 (로만)
    roman "네, 네……!"
    # SOURCE R01 L455 (로만)
    roman "그냥 소리가 조금 커서……."
    # SOURCE R01 L459
    narrator "로만 씨는 애써 태연한 척했다."
    # SOURCE R01 L461
    narrator "하지만 방금 책을 떨어뜨릴 뻔한 건 나도 봤다."
    # SOURCE R01 L463 (주인공)
    mc "많이 놀라셨나 봐요."
    # SOURCE R01 L465 (로만)
    roman "……."
    # SOURCE R01 L467 (로만)
    roman "앗,,, 너무 놀리시면……."
    # SOURCE R01 L471
    narrator "로만 씨가 입술을 조금 내밀었다."
    # SOURCE R01 L473 (주인공)
    mc "아니에요. 놀리려던 건 아니었어요."
    # SOURCE R01 L475 (로만)
    roman "……정말요?"
    # SOURCE R01 L477 (주인공)
    mc "네. 그 대신 다른 책을 같이 찾아볼까요?"
    # SOURCE R01 L479 (로만)
    roman "……후후."
    # SOURCE R01 L481 (로만)
    roman "그건 좋아요."
    # CONTI SOURCE R01 L483 [전환] 일반 LD
    # SOURCE R01 L485 [BGM] Cozy Bookstore
    $ story_draft_bgm("Cozy Bookstore")
    # SOURCE R01 L489
    narrator "로만 씨는 공포 소설을 원래 자리에 돌려놓았다."
    # SOURCE R01 L491
    narrator "그러다가 문득 고개를 들었다."
    # SOURCE R01 L493 (로만)
    roman "그런데 [player_name] 씨."
    # SOURCE R01 L495 (주인공)
    mc "네?"
    # SOURCE R01 L497 (로만)
    roman "혹시 무서운 거 잘 보세요?"
    # SOURCE R01 L499 (주인공)
    mc "음, 아주 잘 보는 편은 아니에요."
    # SOURCE R01 L501 (로만)
    roman "……그럼 다행이에요."
    # SOURCE R01 L503 (주인공)
    mc "왜요?"
    # SOURCE R01 L505 (로만)
    roman "저만 무서워하는 건 아닌 것 같아서요."
    # SOURCE R01 L509
    narrator "로만 씨가 조금 장난스럽게 웃었다."
    # SOURCE R01 L511 (주인공)
    mc "그렇다고 제가 무서워한다고 말씀드린 건 아닌데요?"
    # SOURCE R01 L513 (로만)
    roman "앗,,, 그러셨어요?"
    # SOURCE R01 L515 (로만)
    roman "그럼 다음에 같이 읽어볼까요?"
    # SOURCE R01 L517 (주인공)
    mc "방금 그렇게 놀라셨는데요?"
    # SOURCE R01 L519 (로만)
    roman "……."
    # SOURCE R01 L521 (로만)
    roman "아, 아니에요. 역시 안 될 것 같아요……!"
    # SOURCE R01 L525
    narrator "이번에는 내가 웃음을 참지 못했다."
    # SOURCE R01 L527
    narrator "로만 씨도 결국 같이 웃었다."
    # SOURCE R01 L529
    narrator "처음에는 로만 씨가 이렇게 장난칠 수 있는 사람인 줄 몰랐다."
    # SOURCE R01 L531
    narrator "함께 있는 시간이 늘어날수록 조금씩 새로운 모습을 발견하게 된다."
    # CONTI SOURCE R01 L533 [SCENE 03 END]
    jump roman_r01_sc04

label roman_r01_sc04:
    $ phone_timeline_enter("R01", "roman_r01_sc04")
    # SOURCE R01 L536 SCENE 04. 같은 문장을 다르게 읽는 우리
    # CONTI SOURCE R01 L537 [TIME] 오후 3:20 · 서점 옆 카페 · 깊어지는 대화
    $ phone_timeline_cue("R01", "R01_L537")
    # SOURCE R01 L539 [BG] 작은 북카페 · 창가
    $ story_draft_scene("작은 북카페 · 창가")
    # SOURCE R01 L541 [BGM] Afternoon Conversation
    $ story_draft_bgm("Afternoon Conversation")
    # SOURCE R01 L545
    narrator "책을 고른 뒤 우리는 서점 옆 카페로 이동했다."
    # SOURCE R01 L547
    narrator "로만 씨는 따뜻한 음료를 주문했고, 나는 창가 자리에 앉았다."
    # SOURCE R01 L549
    narrator "테이블에는 오늘 고른 책 두 권이 놓여 있었다."
    # SOURCE R01 L551 (로만)
    roman "오늘 생각보다 책을 많이 봤네요."
    # SOURCE R01 L553 (주인공)
    mc "그러게요. 로만 씨가 설명을 잘해 주셔서 재미있었어요."
    # SOURCE R01 L555 (로만)
    roman "앗,,, 제가 너무 많이 이야기한 건 아니죠……?"
    # SOURCE R01 L557 (주인공)
    mc "아니요. 더 들어보고 싶은데요."
    # SOURCE R01 L559 (로만)
    roman "……."
    # CONTI SOURCE R01 L561 [LD] 로만 · 옅은 홍조
    # SOURCE R01 L563 (로만)
    roman "……후후."
    # SOURCE R01 L565 (로만)
    roman "그럼 조금만 더 이야기해 볼까요?"
    # SOURCE R01 L569
    narrator "로만 씨는 책을 한 권 펼쳤다."
    # SOURCE R01 L571
    narrator "아까 서점에서 둘이 함께 골랐던 일상 소설이었다."
    # SOURCE R01 L573 (로만)
    roman "이 책에서 제가 좋아하는 부분이 있어요."
    # SOURCE R01 L575 (주인공)
    mc "어떤 부분인데요?"
    # SOURCE R01 L577 (로만)
    roman "주인공이 다른 사람을 기다리는 장면이요."
    # SOURCE R01 L579 (로만)
    roman "그런데 그 기다림을 슬프게만 표현하지 않거든요."
    # SOURCE R01 L581 (주인공)
    mc "기다리는 게 기쁠 수도 있다는 건가요?"
    # SOURCE R01 L583 (로만)
    roman "네."
    # SOURCE R01 L585 (로만)
    roman "누군가를 다시 만날 수 있다는 사실이 기쁠 때도 있으니까요."
    # SOURCE R01 L589
    narrator "로만 씨는 책장을 넘기며 이야기했다."
    # SOURCE R01 L591 (로만)
    roman "그런데 읽는 사람에 따라 다르게 느낄 수도 있겠죠."
    # SOURCE R01 L593 (주인공)
    mc "저는 조금 외로운 장면처럼 느껴져요."
    # SOURCE R01 L595 (로만)
    roman "……외롭게요?"
    # SOURCE R01 L597 (주인공)
    mc "네. 다시 만날 수 있다는 걸 알아도 기다리는 동안은 혼자잖아요."
    # SOURCE R01 L601
    narrator "로만 씨는 잠시 생각했다."
    # SOURCE R01 L603 (로만)
    roman "……그렇게 생각할 수도 있겠네요."
    # SOURCE R01 L605 (주인공)
    mc "로만 씨는 다르게 느끼셨고요?"
    # SOURCE R01 L607 (로만)
    roman "네."
    # SOURCE R01 L609 (로만)
    roman "저는 누군가를 기다릴 수 있다는 게 조금 따뜻하게 느껴졌어요."
    # SOURCE R01 L613 (주인공)
    mc "어느 쪽이 맞는 해석일까요?"
    # SOURCE R01 L615 (로만)
    roman "후후……."
    # SOURCE R01 L617 (로만)
    roman "꼭 하나만 맞아야 할까요?"
    # SOURCE R01 L621
    narrator "로만 씨가 웃었다."
    # SOURCE R01 L623 (로만)
    roman "같은 글을 읽어도 사람마다 다르게 생각할 수 있잖아요."
    # SOURCE R01 L625 (로만)
    roman "그래서 책 이야기를 나누는 게 좋아요."
    # SOURCE R01 L627 (주인공)
    mc "그렇네요."
    # SOURCE R01 L631
    narrator "로만 씨는 다시 책장을 넘겼다."
    # SOURCE R01 L633
    narrator "그렇게 좋아하는 책을 설명하는 표정에는 평소의 망설임이 거의 없었다."
    # SOURCE R01 L635 (로만)
    roman "……아."
    # SOURCE R01 L637 (주인공)
    mc "왜 그러세요?"
    # SOURCE R01 L639 (로만)
    roman "제가 너무 진지하게 이야기했네요……."
    # SOURCE R01 L641 (주인공)
    mc "아니에요. 재미있었어요."
    # SOURCE R01 L643 (로만)
    roman "……정말요?"
    # SOURCE R01 L645 (주인공)
    mc "네. 로만 씨가 어떤 생각을 하시는지 알 수 있어서 좋았어요."
    # SOURCE R01 L649
    narrator "로만 씨는 잠시 나를 바라봤다."
    # SOURCE R01 L651
    narrator "그리고 조금 웃었다."
    # SOURCE R01 L653 (로만)
    roman "그럼……."
    # SOURCE R01 L655 (로만)
    roman "다음에도 저랑 다른 생각이 드시면 말씀해 주세요."
    # SOURCE R01 L657 (주인공)
    mc "당연하죠."
    # SOURCE R01 L659 (로만)
    roman "후후. 약속이에요."
    # SOURCE R01 L663
    narrator "이 사람과 함께 책을 읽으면 앞으로도 의견이 다를 때가 있겠지."
    # SOURCE R01 L665
    narrator "그런데 그게 나쁘게 느껴지지는 않았다."
    # SOURCE R01 L667
    narrator "오히려 로만 씨가 세상을 바라보는 방식을 조금씩 알게 될 것 같아서 기대됐다."
    # SOURCE R01 L668 [CHOICE 02 · 서로 다른 생각]
    menu:
        # SOURCE R01 L669 선택지
        "다른 해석을 듣는 게 재미있어요.":
            # SOURCE R01 L671 (주인공)
            mc "같은 책인데 서로 다른 장면이 기억에 남는 것도 재미있네요."
            # SOURCE R01 L673 (로만)
            roman "……맞아요."
            # SOURCE R01 L675 (로만)
            roman "저도 그래서 같이 읽는 게 좋아요."
            # SOURCE R01 L677 [FLAG] roman_mutual_understanding += 1
            $ story_apply("roman_r01_choice02_a", counters={'roman_mutual_understanding': 1})
        # SOURCE R01 L679 선택지
        "로만 씨는 생각을 깊이 하시는 것 같아요.":
            # SOURCE R01 L681 (주인공)
            mc "저는 그냥 지나쳤을 장면을 로만 씨는 다르게 보셨네요."
            # SOURCE R01 L683 (로만)
            roman "앗,,, 그렇게 말씀하시면 부끄러운데……."
            # SOURCE R01 L685 (로만)
            roman "그래도 고마워요."
            # SOURCE R01 L687 [FLAG] roman_affection += 1
            $ story_apply("roman_r01_choice02_b", affection={'roman': 1})
        # SOURCE R01 L689 선택지
        "로만 씨가 좋아하시는 해석을 더 듣고 싶어요.":
            # SOURCE R01 L691 (주인공)
            mc "제가 놓친 부분이 있을 수도 있으니까요."
            # SOURCE R01 L693 (로만)
            roman "후후. 그럼 저도 [player_name] 씨 생각을 더 들어볼래요."
            # SOURCE R01 L695 [FLAG] roman_shared_reading += 1
            $ story_apply("roman_r01_choice02_c", counters={'roman_shared_reading': 1})
    # SOURCE R01 L701
    narrator "로만 씨는 음료를 한 모금 마셨다."
    # SOURCE R01 L703
    narrator "그런데 아까부터 무릎 위에 놓인 작은 노트를 신경 쓰는 것 같았다."
    # SOURCE R01 L705
    narrator "나는 그걸 보고 물었다."
    # SOURCE R01 L707 (주인공)
    mc "그 노트도 읽으시는 책인가요?"
    # SOURCE R01 L709 (로만)
    roman "아……."
    # SOURCE R01 L713
    narrator "로만 씨의 손이 노트 위에서 멈췄다."
    # SOURCE R01 L715 (로만)
    roman "그건……."
    # SOURCE R01 L717 (로만)
    roman "제가 쓰는 글이에요."
    # SOURCE R01 L719 [BGM] 조금 차분하게 전환
    $ story_draft_bgm("조금 차분하게 전환")
    # CONTI SOURCE R01 L721 [SCENE 04 END]
    jump roman_r01_sc05

label roman_r01_sc05:
    $ phone_timeline_enter("R01", "roman_r01_sc05")
    # SOURCE R01 L724 SCENE 05. 아직은 보여드릴 수 없는 글
    # CONTI SOURCE R01 L725 [TIME] 오후 4:00 · 북카페 · 로만의 창작 목표 공개
    $ phone_timeline_cue("R01", "R01_L725")
    # SOURCE R01 L727 [BG] 북카페 · 오후
    $ story_draft_scene("북카페 · 오후")
    # SOURCE R01 L729 [BGM] Soft Piano
    $ story_draft_bgm("Soft Piano")
    # CONTI SOURCE R01 L731 [ANIM] 로만 · 부드러운 눈 깜빡임과 미세 호흡
    # SOURCE R01 L735
    narrator "로만 씨는 노트 표지를 손가락으로 쓸었다."
    # SOURCE R01 L737
    narrator "처음에는 그냥 독서 기록을 적는 노트라고 생각했다."
    # SOURCE R01 L739
    narrator "그런데 직접 글을 쓰고 있었다니."
    # SOURCE R01 L741 (주인공)
    mc "소설을 쓰시는 거예요?"
    # SOURCE R01 L743 (로만)
    roman "네……."
    # SOURCE R01 L745 (로만)
    roman "아직은 완성하지 못했지만요."
    # SOURCE R01 L747 (주인공)
    mc "언제부터 쓰셨어요?"
    # SOURCE R01 L749 (로만)
    roman "음…… 꽤 오래됐어요."
    # SOURCE R01 L751 (로만)
    roman "처음에는 그냥 생각나는 문장을 적어두는 정도였는데."
    # SOURCE R01 L753 (로만)
    roman "조금씩 이야기가 생기더라고요."
    # SOURCE R01 L757
    narrator "로만 씨는 노트를 살짝 펼쳤다."
    # SOURCE R01 L759
    narrator "작은 글씨가 빼곡하게 적혀 있었다."
    # SOURCE R01 L761
    narrator "문장 옆에는 지우고 다시 쓴 흔적도 많았다."
    # SOURCE R01 L763 (주인공)
    mc "정말 많이 쓰셨네요."
    # SOURCE R01 L765 (로만)
    roman "앗,,, 아직 별거 아니에요……."
    # SOURCE R01 L767 (주인공)
    mc "그래도 꾸준히 쓰셨잖아요."
    # SOURCE R01 L769 (로만)
    roman "……."
    # SOURCE R01 L771 (로만)
    roman "후후. 그렇기는 하네요."
    # SOURCE R01 L775
    narrator "로만 씨는 페이지를 몇 장 넘겼다."
    # SOURCE R01 L777
    narrator "그러다가 어느 지점에서 손을 멈췄다."
    # SOURCE R01 L779 (로만)
    roman "여기는……."
    # SOURCE R01 L783
    narrator "노트가 천천히 닫혔다."
    # SOURCE R01 L785 (로만)
    roman "아직 보여드리기 조금 부끄러워요."
    # SOURCE R01 L787 (주인공)
    mc "그럼 안 보여주셔도 돼요."
    # SOURCE R01 L789 (로만)
    roman "……."
    # SOURCE R01 L793
    narrator "로만 씨는 잠시 나를 바라봤다."
    # SOURCE R01 L795 (로만)
    roman "CH04 때도……."
    # SOURCE R01 L799
    narrator "로만 씨는 말을 멈췄다."
    # SOURCE R01 L801
    narrator "그때 시연 영상에 넣을 문장을 두고 이야기했던 일이 떠올랐다."
    # SOURCE R01 L803 (로만)
    roman "아니, 축제 영상 준비할 때도 그렇게 말씀하셨잖아요."
    # SOURCE R01 L805 (주인공)
    mc "기억해요."
    # SOURCE R01 L807 (로만)
    roman "그때…… 조금 기뻤어요."
    # SOURCE R01 L809 (로만)
    roman "제가 아직 보여드리고 싶지 않은 부분도 기다려주셔서요."
    # SOURCE R01 L811 (주인공)
    mc "로만 씨가 직접 쓰신 글이니까요."
    # SOURCE R01 L813 (주인공)
    mc "보여주실지 결정하는 것도 로만 씨 마음이죠."
    # SOURCE R01 L817
    narrator "로만 씨는 노트를 내려다봤다."
    # SOURCE R01 L819
    narrator "그리고 천천히 웃었다."
    # SOURCE R01 L821 (로만)
    roman "……고마워요."
    # SOURCE R01 L825
    narrator "잠시 조용해졌다."
    # SOURCE R01 L827
    narrator "그러다 로만 씨가 새로운 이야기를 꺼냈다."
    # SOURCE R01 L829 (로만)
    roman "사실은 다음 달에 교내 문학 낭독 행사가 있거든요."
    # SOURCE R01 L831 (주인공)
    mc "축제 때 봤던 행사처럼요?"
    # SOURCE R01 L833 (로만)
    roman "네. 그런데 이번에는 조금 더 긴 글도 읽을 수 있대요."
    # SOURCE R01 L835 (로만)
    roman "그래서……."
    # SOURCE R01 L839
    narrator "로만 씨는 문장을 고르듯 잠시 말을 멈췄다."
    # SOURCE R01 L841 (로만)
    roman "제가 쓴 글을 직접 읽어볼까 고민하고 있어요."
    # SOURCE R01 L843 (주인공)
    mc "좋은데요?"
    # SOURCE R01 L845 (로만)
    roman "앗,,, 그렇게 바로요?"
    # SOURCE R01 L847 (주인공)
    mc "네. 해보고 싶으셨던 거잖아요."
    # SOURCE R01 L849 (로만)
    roman "……."
    # SOURCE R01 L851 (로만)
    roman "그렇기는 한데……."
    # SOURCE R01 L853 (로만)
    roman "아직 자신은 없어요."
    # SOURCE R01 L857
    narrator "로만 씨는 옅게 웃었다."
    # SOURCE R01 L859 (로만)
    roman "제가 쓰는 글이 재미있는지도 모르겠고."
    # SOURCE R01 L861 (로만)
    roman "사람들 앞에서 읽다가 실수할까 봐 걱정되고……."
    # SOURCE R01 L863 (주인공)
    mc "그런 걱정이 드실 수 있죠."
    # SOURCE R01 L865 (로만)
    roman "……네."
    # SOURCE R01 L867 (주인공)
    mc "그래도 로만 씨가 해보고 싶으시면, 준비하실 때 도와드릴게요."
    # SOURCE R01 L869 (로만)
    roman "……!"
    # SOURCE R01 L871 (로만)
    roman "정말요?"
    # SOURCE R01 L873 (주인공)
    mc "네. 제가 글을 대신 쓸 수는 없지만, 연습 상대는 되어드릴 수 있잖아요."
    # SOURCE R01 L877
    narrator "로만 씨는 노트를 꼭 끌어안았다."
    # SOURCE R01 L879 (로만)
    roman "……후후."
    # SOURCE R01 L881 (로만)
    roman "그것만으로도 많이 도움이 될 것 같아요."
    # SOURCE R01 L885
    narrator "나는 조금 궁금해졌다."
    # SOURCE R01 L887
    narrator "로만 씨가 어떤 이야기를 쓰고 있을까."
    # SOURCE R01 L889
    narrator "어떤 문장에 마음을 담았을까."
    # SOURCE R01 L891
    narrator "그리고 언젠가 그 이야기를 직접 읽어줄 날이 올까."
    # SOURCE R01 L893
    narrator "……기다려 보고 싶었다."
    # SOURCE R01 L895 [FLAG] roman_reading_event_goal_known = True
    $ story_flag("roman_reading_event_goal_known", True)
    # CONTI SOURCE R01 L897 [SCENE 05 END]
    jump roman_r01_sc06

label roman_r01_sc06:
    $ phone_timeline_enter("R01", "roman_r01_sc06")
    # SOURCE R01 L899 SCENE 06. 첫 번째 독자가 되어주세요
    # CONTI SOURCE R01 L900 [TIME] 오후 4:25 · 북카페 · 신뢰와 관계의 경계
    $ phone_timeline_cue("R01", "R01_L900")
    # SOURCE R01 L902 [BG] 북카페 · 창가
    $ story_draft_scene("북카페 · 창가")
    # SOURCE R01 L904 [BGM] Gentle Emotional
    $ story_draft_bgm("Gentle Emotional")
    # SOURCE R01 L908
    narrator "카페 밖으로 노을빛이 들어왔다."
    # SOURCE R01 L910
    narrator "로만 씨는 노트를 펼쳐 놓고 조용히 페이지를 넘겼다."
    # SOURCE R01 L912
    narrator "그러다가 무언가를 결심한 듯 고개를 들었다."
    # SOURCE R01 L914 (로만)
    roman "저기……."
    # SOURCE R01 L916 (주인공)
    mc "네?"
    # SOURCE R01 L918 (로만)
    roman "혹시……."
    # SOURCE R01 L920 (로만)
    roman "제가 쓴 글 중에 짧은 부분 하나만 읽어보실래요?"
    # SOURCE R01 L922 (주인공)
    mc "정말 괜찮으시겠어요?"
    # SOURCE R01 L924 (로만)
    roman "……네."
    # SOURCE R01 L926 (로만)
    roman "오늘 이야기 나누면서 조금 용기가 생겼거든요."
    # SOURCE R01 L930
    narrator "로만 씨는 노트를 조심스럽게 내밀었다."
    # SOURCE R01 L932
    narrator "한 페이지에는 짧은 글이 적혀 있었다."
    # SOURCE R01 L934
    narrator "오래된 정류장에서 누군가를 기다리는 인물에 관한 이야기였다."
    # SOURCE R01 L936
    narrator "주인공은 매일 같은 시간에 정류장을 찾는다."
    # SOURCE R01 L938
    narrator "하지만 그 사람은 기다리는 상대를 만나기 위해서만 그곳에 가는 것은 아니었다."
    # SOURCE R01 L940
    narrator "기다리는 동안 지나가는 사람들을 보고, 계절이 바뀌는 것을 느끼고, 자신의 시간을 살아가고 있었다."
    # SOURCE R01 L944
    narrator "마지막 문장은 유독 눈에 들어왔다."
    # SOURCE R01 L946
    narrator "기다리는 동안에도, 내 하루는 계속되고 있었다."
    # SOURCE R01 L948
    narrator "나는 노트에서 시선을 들었다."
    # SOURCE R01 L950 (로만)
    roman "……."
    # SOURCE R01 L952 (주인공)
    mc "좋았어요."
    # SOURCE R01 L954 (로만)
    roman "앗,,, 정말요?"
    # SOURCE R01 L956 (주인공)
    mc "네. 특히 마지막 문장이 좋았어요."
    # SOURCE R01 L958 (로만)
    roman "……!"
    # SOURCE R01 L960 (로만)
    roman "그 부분이요?"
    # SOURCE R01 L962 (주인공)
    mc "기다림을 이야기하면서도 그 사람 자신의 시간이 중요하다고 말하는 것 같았거든요."
    # SOURCE R01 L966
    narrator "로만 씨는 잠시 아무 말도 하지 않았다."
    # SOURCE R01 L968
    narrator "그러더니 작게 웃었다."
    # SOURCE R01 L970 (로만)
    roman "……그렇게 읽으셨군요."
    # SOURCE R01 L972 (주인공)
    mc "제가 생각하신 의미와는 다른가요?"
    # SOURCE R01 L974 (로만)
    roman "아니에요."
    # SOURCE R01 L976 (로만)
    roman "조금 다르기는 한데……."
    # SOURCE R01 L978 (로만)
    roman "그래서 더 재미있어요."
    # SOURCE R01 L982
    narrator "로만 씨는 노트를 다시 펼쳤다."
    # SOURCE R01 L984 (로만)
    roman "사실 저는 그 인물이 조금 더 외로운 사람이라고 생각했거든요."
    # SOURCE R01 L986 (로만)
    roman "그런데 [player_name] 씨는 그 사람이 자기 시간을 보내고 있다고 읽으셨네요."
    # SOURCE R01 L988 (주인공)
    mc "그럼 두 해석을 다 살릴 수도 있겠네요."
    # SOURCE R01 L990 (로만)
    roman "……후후."
    # SOURCE R01 L992 (로만)
    roman "맞아요."
    # SOURCE R01 L996
    narrator "로만 씨는 펜을 들었다."
    # SOURCE R01 L998
    narrator "그러다가 다시 내려놓았다."
    # SOURCE R01 L1000 (로만)
    roman "저…… 한 가지 부탁드려도 될까요?"
    # SOURCE R01 L1002 (주인공)
    mc "네. 말씀하세요."
    # SOURCE R01 L1004 (로만)
    roman "앞으로 글을 쓰다가 고민이 생기면……."
    # SOURCE R01 L1006 (로만)
    roman "가끔 읽어주실 수 있을까요?"
    # SOURCE R01 L1008 (주인공)
    mc "좋아요."
    # SOURCE R01 L1010 (로만)
    roman "……그런데."
    # SOURCE R01 L1012 (로만)
    roman "제가 쓴 문장이 이상해도 솔직하게 말씀해 주세요."
    # SOURCE R01 L1014 (주인공)
    mc "알겠어요."
    # SOURCE R01 L1016 (로만)
    roman "후후……."
    # SOURCE R01 L1018 (로만)
    roman "그럼 저도 조금 더 열심히 써볼게요."
    # SOURCE R01 L1019 [CHOICE 03 · 첫 독자의 약속]
    menu:
        # SOURCE R01 L1021 선택지
        "서로 다른 생각도 편하게 이야기해요.":
            # SOURCE R01 L1023 (주인공)
            mc "의견이 다르더라도 편하게 이야기해요."
            # SOURCE R01 L1025 (로만)
            roman "……네. 저도 그게 좋아요."
            # SOURCE R01 L1027 (로만)
            roman "그럼 제가 마음에 안 드는 부분이 있으면 그것도 말씀드릴게요."
            # SOURCE R01 L1022 신뢰 +2 · roman_mutual_respect += 1
            $ story_apply("roman_r01_choice03_a", trust={'roman': 2}, counters={'roman_mutual_respect': 1})
        # SOURCE R01 L1030 선택지
        "로만 씨 글을 앞으로도 읽고 싶어요.":
            # SOURCE R01 L1031 (주인공)
            mc "다음 글도 기대할게요. 로만 씨가 어떤 이야기를 쓰실지 궁금해요."
            # SOURCE R01 L1033 (로만)
            roman "앗,,, 그러면 조금 더 열심히 써야겠네요."
            # SOURCE R01 L1035 호감 +2 · roman_affection += 2
            $ story_apply("roman_r01_choice03_b", affection={'roman': 2})
        # SOURCE R01 L1038 선택지
        "다른 사람보다 제가 먼저 읽어드릴게요.":
            # SOURCE R01 L1039 (주인공)
            mc "새로 쓰신 글은 제가 먼저 읽어드릴게요."
            # SOURCE R01 L1041 (로만)
            roman "……정말요?"
            # SOURCE R01 L1043 (로만)
            roman "후후…… 왠지 조금 특별한 기분이에요."
            # SOURCE R01 L1045 둘만의 약속 · roman_first_reader_promise = True
            $ story_apply("roman_r01_choice03_c", values={'roman_first_reader_promise': True})
    # SOURCE R01 L1053
    narrator "로만 씨는 노트를 다시 가방에 넣었다."
    # SOURCE R01 L1055
    narrator "그리고 조금 머뭇거리다가 말을 꺼냈다."
    # SOURCE R01 L1057 (로만)
    roman "그런데……."
    # SOURCE R01 L1059 (주인공)
    mc "네?"
    # SOURCE R01 L1061 (로만)
    roman "제가 가끔 연락드려도 괜찮으실까요?"
    # SOURCE R01 L1063 (주인공)
    mc "그럼요."
    # SOURCE R01 L1065 (로만)
    roman "책 이야기나…… 글 이야기 말고도요."
    # SOURCE R01 L1069
    narrator "……책이나 글 말고도?"
    # SOURCE R01 L1071 (주인공)
    mc "물론이죠. 그냥 일상 이야기하셔도 좋아요."
    # SOURCE R01 L1073 (로만)
    roman "……."
    # CONTI SOURCE R01 L1075 [LD] 로만 · 붉어진 얼굴
    # SOURCE R01 L1077 (로만)
    roman "앗,,, 다행이에요."
    # SOURCE R01 L1079 (로만)
    roman "그런 이야기도 하고 싶었거든요."
    # SOURCE R01 L1083
    narrator "로만 씨는 웃었다."
    # SOURCE R01 L1085
    narrator "평소의 조용한 미소와는 조금 달랐다."
    # SOURCE R01 L1087
    narrator "마음이 놓인 사람의 표정이었다."
    # SOURCE R01 L1089
    narrator "나도 그 모습이 좋았다."
    # CONTI SOURCE R01 L1091 [SCENE 06 END]
    jump roman_r01_sc07

label roman_r01_sc07:
    $ phone_timeline_enter("R01", "roman_r01_sc07")
    # SOURCE R01 L1093 SCENE 07. 책갈피의 뒷면
    # CONTI SOURCE R01 L1094 [TIME] 오후 5:15 · 서점 앞 거리 · 첫 개인 데이트의 마무리
    $ phone_timeline_cue("R01", "R01_L1094")
    # SOURCE R01 L1096 [BG] 학교 앞 거리 · 노을
    $ story_draft_scene("학교 앞 거리 · 노을")
    # SOURCE R01 L1098 [BGM] Evening Walk
    $ story_draft_bgm("Evening Walk")
    # CONTI SOURCE R01 L1100 [ANIM] 로만 · 약한 머리카락 움직임, 자연스러운 눈 깜빡임
    # SOURCE R01 L1104
    narrator "서점 밖으로 나왔을 때는 해가 조금 기울어 있었다."
    # SOURCE R01 L1106
    narrator "생각보다 오랫동안 이야기를 나눴다."
    # SOURCE R01 L1108
    narrator "책 한 권을 고르고, 글을 읽고, 서로 다른 생각을 이야기했다."
    # SOURCE R01 L1110
    narrator "별다른 사건이 있었던 건 아니었다."
    # SOURCE R01 L1112
    narrator "그런데 오늘은 조금 특별한 하루로 기억될 것 같았다."
    # SOURCE R01 L1114 (로만)
    roman "오늘…… 정말 재미있었어요."
    # SOURCE R01 L1116 (주인공)
    mc "저도요."
    # SOURCE R01 L1118 (로만)
    roman "처음에는 책만 같이 고르려고 했는데……."
    # SOURCE R01 L1120 (로만)
    roman "생각보다 이야기를 많이 했네요."
    # SOURCE R01 L1122 (주인공)
    mc "그러게요. 로만 씨가 쓰시는 글 이야기도 들었고요."
    # SOURCE R01 L1124 (로만)
    roman "앗,,, 그건 조금 부끄러웠어요……."
    # SOURCE R01 L1126 (주인공)
    mc "그래도 보여주셔서 감사했어요."
    # SOURCE R01 L1128 (로만)
    roman "……후후."
    # SOURCE R01 L1132
    narrator "로만 씨는 손에 든 종이봉투를 내려다봤다."
    # SOURCE R01 L1134 (로만)
    roman "저기……."
    # SOURCE R01 L1136 (주인공)
    mc "네?"
    # SOURCE R01 L1138 (로만)
    roman "전에 제가 드린 책갈피, 아직 가지고 계세요?"
    # SOURCE R01 L1140 (주인공)
    mc "네. 잘 가지고 있어요."
    # SOURCE R01 L1142 (로만)
    roman "……정말요?"
    # SOURCE R01 L1144 (주인공)
    mc "물론이죠. 로만 씨가 직접 만들어주셨잖아요."
    # SOURCE R01 L1146 (로만)
    roman "앗,,, 그랬죠……."
    # SOURCE R01 L1150
    narrator "로만 씨는 작게 웃었다."
    # SOURCE R01 L1152 (로만)
    roman "그런데 사실……."
    # SOURCE R01 L1154 (로만)
    roman "그때 책갈피 뒷면에 문장을 하나 더 쓰려고 했어요."
    # SOURCE R01 L1156 (주인공)
    mc "다른 문장이요?"
    # SOURCE R01 L1158 (로만)
    roman "네."
    # SOURCE R01 L1160 (로만)
    roman "그런데 너무 부끄러워서 결국 못 썼어요."
    # SOURCE R01 L1164
    narrator "로만 씨는 잠시 하늘을 바라봤다."
    # SOURCE R01 L1166 (주인공)
    mc "어떤 문장이었는지 여쭤봐도 될까요?"
    # SOURCE R01 L1168 (로만)
    roman "……."
    # SOURCE R01 L1170 (로만)
    roman "아직은 비밀이에요."
    # SOURCE R01 L1172 (주인공)
    mc "그렇군요."
    # SOURCE R01 L1174 (로만)
    roman "……서운하세요?"
    # SOURCE R01 L1176 (주인공)
    mc "아니요. 언젠가 알려주실 수도 있잖아요."
    # SOURCE R01 L1180
    narrator "로만 씨가 웃음을 터뜨렸다."
    # SOURCE R01 L1182 (로만)
    roman "후후……."
    # SOURCE R01 L1184 (로만)
    roman "정말 기다리는 걸 잘하시네요."
    # SOURCE R01 L1186 (주인공)
    mc "그런가요?"
    # SOURCE R01 L1188 (로만)
    roman "네."
    # SOURCE R01 L1190 (로만)
    roman "그런데……."
    # SOURCE R01 L1192 (로만)
    roman "가끔은 저도 먼저 이야기해 보고 싶어요."
    # SOURCE R01 L1196
    narrator "로만 씨는 조금 쑥스러운 표정으로 말을 이었다."
    # SOURCE R01 L1198 (로만)
    roman "계속 기다리게만 하는 건 저도 싫으니까요."
    # SOURCE R01 L1202 (주인공)
    mc "그럼 다음에는 로만 씨가 먼저 이야기해 주세요."
    # SOURCE R01 L1204 (로만)
    roman "……네."
    # SOURCE R01 L1206 (로만)
    roman "연습해 볼게요."
    # SOURCE R01 L1210
    narrator "오늘은 처음 만났을 때보다 더 많은 걸 알게 됐다."
    # SOURCE R01 L1212
    narrator "로만 씨는 수줍어하지만, 하고 싶은 말이 없는 사람은 아니다."
    # SOURCE R01 L1214
    narrator "오히려 자신의 생각을 소중하게 여기기 때문에 조심스럽게 꺼내는 사람에 가깝다."
    # SOURCE R01 L1216
    narrator "그런 사람의 이야기를 앞으로도 더 듣고 싶었다."
    # CONTI SOURCE R01 L1218 [시간 경과 · 오후 5:35]
    $ phone_timeline_cue("R01", "R01_L1218")
    # SOURCE R01 L1220 [BG] 캠퍼스 갈림길
    $ story_draft_scene("캠퍼스 갈림길")
    # SOURCE R01 L1224
    narrator "어느새 서로 다른 길로 가야 하는 곳에 도착했다."
    # SOURCE R01 L1226 (로만)
    roman "저는 여기서 가면 돼요."
    # SOURCE R01 L1228 (주인공)
    mc "네. 오늘 정말 즐거웠어요."
    # SOURCE R01 L1230 (로만)
    roman "……저도요."
    # SOURCE R01 L1234
    narrator "잠시 조용해졌다."
    # SOURCE R01 L1236
    narrator "로만 씨는 한 걸음 물러났다가 다시 나를 바라봤다."
    # SOURCE R01 L1238 (로만)
    roman "저기……."
    # SOURCE R01 L1240 (주인공)
    mc "네?"
    # SOURCE R01 L1242 (로만)
    roman "다음에도……."
    # SOURCE R01 L1244 (로만)
    roman "오늘처럼 그냥 같이 책 보러 가도 될까요?"
    # SOURCE R01 L1246 (주인공)
    mc "좋아요."
    # SOURCE R01 L1248 (로만)
    roman "……후후."
    # SOURCE R01 L1250 (로만)
    roman "그럼 다음에는 제가 먼저 연락드릴게요."
    # SOURCE R01 L1252 (주인공)
    mc "기다리고 있을게요."
    # SOURCE R01 L1256
    narrator "로만 씨는 고개를 끄덕였다."
    # SOURCE R01 L1258
    narrator "그리고 조금 장난스럽게 웃었다."
    # SOURCE R01 L1260 (로만)
    roman "그런데 너무 오래 기다리시면 안 돼요."
    # SOURCE R01 L1262 (주인공)
    mc "왜요?"
    # SOURCE R01 L1264 (로만)
    roman "제가 생각보다 빨리 연락드릴 수도 있으니까요."
    # SOURCE R01 L1268
    narrator "……이런 장난도 할 줄 아는 사람이었나."
    # SOURCE R01 L1270 (주인공)
    mc "그럼 저도 준비하고 있을게요."
    # SOURCE R01 L1272 (로만)
    roman "후후…… 네!"
    # SOURCE R01 L1276
    narrator "로만 씨는 손을 흔들며 걸어갔다."
    # SOURCE R01 L1278
    narrator "나는 잠시 그 뒷모습을 바라봤다."
    # SOURCE R01 L1280
    narrator "아직 서로에 대해 모르는 게 많다."
    # SOURCE R01 L1282
    narrator "그래도 서두르지 않아도 괜찮을 것 같다."
    # SOURCE R01 L1284
    narrator "이 사람과는 천천히 가까워지는 과정 자체가 즐거우니까."
    # CONTI SOURCE R01 L1286 [SCENE 07 END]
    jump roman_r01_sc08

label roman_r01_sc08:
    $ phone_timeline_enter("R01", "roman_r01_sc08")
    # SOURCE R01 L1288 SCENE 08. 다음에는 제가 먼저
    # CONTI SOURCE R01 L1289 [TIME] 오후 10:45 · 주인공 방 · R01 엔딩 및 R02 예고
    $ phone_timeline_cue("R01", "R01_L1289")
    # SOURCE R01 L1291 [BG] 주인공 방 · 밤
    $ story_draft_scene("주인공 방 · 밤")
    # SOURCE R01 L1293 [BGM] Quiet Reading
    $ story_draft_bgm("Quiet Reading")
    # CONTI SOURCE R01 L1295 [FADE IN]
    # SOURCE R01 L1299
    narrator "집으로 돌아온 뒤 책상에 앉았다."
    # SOURCE R01 L1301
    narrator "오늘 산 책을 펼쳐봤다."
    # SOURCE R01 L1303
    narrator "책 사이에는 로만 씨가 축제 때 직접 만들어줬던 책갈피가 끼워져 있었다."
    # SOURCE R01 L1305
    narrator "크림색 종이."
    # SOURCE R01 L1307
    narrator "작은 파란 꽃."
    # SOURCE R01 L1309
    narrator "그리고 손글씨로 적힌 문장."
    # SOURCE R01 L1311
    narrator "「함께 읽고 싶은 이야기가 생겼어요.」"
    # SOURCE R01 L1315
    narrator "처음 이 책갈피를 받았을 때는 그냥 예쁜 선물이라고 생각했다."
    # SOURCE R01 L1317
    narrator "그런데 지금은 조금 다르게 느껴진다."
    # SOURCE R01 L1319
    narrator "오늘 우리는 정말 함께 이야기를 읽었다."
    # SOURCE R01 L1321
    narrator "그리고 책에 적혀 있지 않은 이야기까지 많이 나눴다."
    # SOURCE R01 L1323
    narrator "로만 씨가 어떤 글을 쓰고 있는지."
    # SOURCE R01 L1325
    narrator "무엇을 좋아하고, 무엇을 어려워하는지."
    # SOURCE R01 L1327
    narrator "어떤 문장을 특별하게 생각하는지."
    # CONTI SOURCE R01 L1329 [SFX] 휴대전화 진동
    # CONTI SOURCE R01 L1331 [UI] 로만 개인 메시지
    $ story_chat(True, title="로만")
    # SOURCE R01 L1333 (로만)
    roman "앗,,, 오늘 집에는 잘 들어가셨어요?"
    # SOURCE R01 L1335 (주인공 · 메시지)
    mc "네. 로만 씨도 잘 들어가셨어요?"
    # SOURCE R01 L1337 (로만)
    roman "네……!"
    # SOURCE R01 L1339 (로만)
    roman "오늘 정말 즐거웠어요."
    # SOURCE R01 L1341 (주인공 · 메시지)
    mc "저도 즐거웠어요. 추천해 주신 책도 읽어볼게요."
    # SOURCE R01 L1343 (로만)
    roman "후후……."
    # SOURCE R01 L1345 (로만)
    roman "그런데 저 하나 여쭤봐도 될까요?"
    # SOURCE R01 L1347 (주인공 · 메시지)
    mc "네. 뭔데요?"
    # SOURCE R01 L1349 (로만)
    roman "제가 다음에 먼저 연락드리겠다고 했잖아요."
    # SOURCE R01 L1351 (주인공 · 메시지)
    mc "네. 기억해요."
    # SOURCE R01 L1353 (로만)
    roman "……그럼."
    # SOURCE R01 L1355 (로만)
    roman "지금 연락드리는 것도 괜찮은 거죠……?"
    # SOURCE R01 L1359
    narrator "……."
    # SOURCE R01 L1361
    narrator "나는 잠시 화면을 바라봤다."
    # SOURCE R01 L1363
    narrator "그러다 웃음이 터졌다."
    # SOURCE R01 L1365 (주인공 · 메시지)
    mc "당연하죠. 언제든 편하게 연락 주세요."
    # SOURCE R01 L1367 (로만)
    roman "앗,,, 다행이에요!"
    # SOURCE R01 L1369 (로만)
    roman "그럼 다음 주에 같이 점심 드실래요?"
    # SOURCE R01 L1371 (주인공 · 메시지)
    mc "좋아요. 어떤 메뉴 생각하세요?"
    # SOURCE R01 L1373 (로만)
    roman "음……."
    # SOURCE R01 L1375 (로만)
    roman "사실 이미 하나 생각해뒀어요."
    # SOURCE R01 L1377 (주인공 · 메시지)
    mc "어떤 건데요?"
    # SOURCE R01 L1379 (로만)
    roman "……비밀이에요."
    # SOURCE R01 L1381 (로만)
    roman "이번에는 제가 골라볼게요."
    # SOURCE R01 L1383 (주인공 · 메시지)
    mc "기대할게요."
    # SOURCE R01 L1385 (로만)
    roman "후후……."
    # SOURCE R01 L1387 (로만)
    roman "그럼 약속이에요."
    # SOURCE R01 L1391
    narrator "이번에는 로만 씨가 먼저 약속을 잡았다."
    # SOURCE R01 L1393
    narrator "책을 보여주는 것도, 글을 들려주는 것도 아닌 평범한 점심 약속."
    # SOURCE R01 L1395
    narrator "그런데 이상하게도 책을 추천받았을 때만큼 기뻤다."
    # CONTI SOURCE R01 L1397 [UI] 로만의 마지막 메시지
    # SOURCE R01 L1399 (로만)
    roman "아, 그리고……."
    # SOURCE R01 L1401 (로만)
    roman "오늘 보여드린 글 있잖아요."
    # SOURCE R01 L1403 (로만)
    roman "다음에는 조금 더 긴 부분을 읽어드리고 싶어요."
    # SOURCE R01 L1405 (로만)
    roman "제가 먼저 보여드릴 준비가 되면요."
    # SOURCE R01 L1407 (주인공 · 메시지)
    mc "좋아요. 천천히 기다릴게요."
    # SOURCE R01 L1409 (로만)
    roman "……네."
    # SOURCE R01 L1411 (로만)
    roman "좋은 밤 보내세요……!"
    # CONTI SOURCE R01 L1413 [UI] 메시지 종료
    $ story_chat(False)
    # SOURCE R01 L1417
    narrator "휴대전화를 내려놓았다."
    # SOURCE R01 L1419
    narrator "로만 씨가 쓰고 있는 이야기는 아직 끝나지 않았다."
    # SOURCE R01 L1421
    narrator "완성되려면 시간이 더 필요할 것이다."
    # SOURCE R01 L1423
    narrator "그런데 이상하게도 그게 아쉽지 않았다."
    # SOURCE R01 L1425
    narrator "앞으로 그 이야기가 어떻게 바뀔지 궁금했고."
    # SOURCE R01 L1427
    narrator "그 이야기를 쓰는 로만 씨도 더 알고 싶었다."
    # SOURCE R01 L1429
    narrator "어쩌면 오늘의 약속은 책을 함께 읽는 약속만이 아니었는지도 모르겠다."
    # CONTI SOURCE R01 L1431 [SFX] 책장 넘기는 소리
    # SOURCE R01 L1435
    narrator "나는 다시 책을 펼쳤다."
    # SOURCE R01 L1437
    narrator "하지만 이번에는 조금 다른 생각이 들었다."
    # SOURCE R01 L1439
    narrator "다음에 로만 씨를 만나면 무슨 이야기를 할까."
    # SOURCE R01 L1441
    narrator "어떤 책을 고를까."
    # SOURCE R01 L1443
    narrator "또 어떤 표정으로 웃을까."
    # SOURCE R01 L1447 (주인공 · 혼잣말)
    mc "……기대되네."
    # CONTI SOURCE R01 L1449 [FADE TO BLACK]
    # SOURCE R01 L1451 [BGM] R01 Ending Theme
    $ story_draft_bgm("R01 Ending Theme")
    # CONTI SOURCE R01 L1452 [TEXT] ROMAN ROUTE
    # CONTI SOURCE R01 L1453 [TEXT] R01 COMPLETE
    # CONTI SOURCE R01 L1454 [TEXT] 「책갈피에 남겨둔 약속」
    # CONTI SOURCE R01 L1456 [TEXT] NEXT CHAPTER
    # CONTI SOURCE R01 L1457 [TEXT] R02 「조금씩, 가까워지는 거리」
    # SOURCE R01 L1459 [FLAG] roman_r01_complete = True
    $ story_flag("roman_r01_complete", True)
    # CONTI SOURCE R01 L1461 [NEXT] ROMAN ROUTE R02
    # CONTI SOURCE R01 L1463 [CHAPTER R01 END]
    jump roman_r02
