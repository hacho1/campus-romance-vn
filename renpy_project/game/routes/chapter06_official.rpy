# CH06 · original manuscript dialogue-only import
# SOURCE: design_docs/story_sources/chapter06.txt
# SHA256: 42b48d4c793e4d1d7e39d90e64c2603a95945f2fe648a0f1b8ae3c8c5cccdfd3
# Rebuild: tools/import_ch06_ch07.py --write

define ch06_announcer = Character("안내 방송", callback=story_speaking("system"))
define ch06_staff = Character("운영본부 담당자", callback=story_speaking("system"))
define ch06_game_staff = Character("진행 요원", callback=story_speaking("system"))
define ch06_visitor_a = Character("방문객 A", callback=story_speaking("system"))
define ch06_visitor_b = Character("방문객 B", callback=story_speaking("system"))
define ch06_visitor_c = Character("방문객 C", callback=story_speaking("system"))
define ch06_visitor_d = Character("방문객 D", callback=story_speaking("system"))
define ch06_visitor_e = Character("방문객 E", callback=story_speaking("system"))

label chapter06:
    $ phone_timeline_enter("CH06", "chapter06")
    $ story_begin_chapter(6, "드디어 축제다!")
    jump ch06_sc01

label ch06_sc01:
    $ phone_timeline_enter("CH06", "ch06_sc01")
    # SOURCE CH06 L37 드디어 축제다!
    # SOURCE CH06 L39 [BG] 주인공 방 · 아침
    $ story_draft_scene("주인공 방 · 아침")
    # SOURCE CH06 L41 [BGM] Morning Campus
    $ story_draft_bgm("Morning Campus")
    # CONTI SOURCE CH06 L43 [FADE IN]
    # SOURCE CH06 L47
    narrator "아침부터 휴대전화가 시끄럽다."
    # SOURCE CH06 L49
    narrator "눈을 뜨기도 전에 알림이 세 번이나 울렸다."
    # SOURCE CH06 L51
    narrator "축제 당일."
    # SOURCE CH06 L53
    narrator "지난 몇 주 동안 그렇게 준비했던 날이 드디어 왔다."
    # CONTI SOURCE CH06 L55 [SFX] 휴대전화 진동
    # CONTI SOURCE CH06 L57 [UI] 축제 준비팀 (6)
    $ story_chat(True, title="축제 준비팀")
    $ phone_threads["campus_group"]["title"] = "축제 준비팀"
    # SOURCE CH06 L60 시아
    sia "야아아아아"
    # SOURCE CH06 L62 시아
    sia "축제다!!!!!!"
    # SOURCE CH06 L65 오므
    omu "아침부터 시끄럽다"
    # SOURCE CH06 L68 시아
    sia "오늘은 시끄러워도 되는 날이거든"
    # SOURCE CH06 L71 하린
    lumi "어제도 시끄러우셨잖아요."
    # SOURCE CH06 L74 시아
    sia "하린아 오늘만큼은 나 좀 봐줘"
    # SOURCE CH06 L77 다림
    darim "다들 아침은 드셨나요?"
    # SOURCE CH06 L79 다림
    darim "오전 아홉 시까지 부스에서 마지막 점검할게요."
    # SOURCE CH06 L82 로만
    roman "앗,,, 저 지금 출발해요……!"
    # SOURCE CH06 L85 시아
    sia "로만이 나보다 빠르네"
    # SOURCE CH06 L88 오므
    omu "니 아직 안 나왔나"
    # SOURCE CH06 L91 시아
    sia "……."
    # SOURCE CH06 L94 하린
    lumi "예상대로네요."
    # SOURCE CH06 L97 시아
    sia "아 나간다고ㅋㅋㅋ"
    # SOURCE CH06 L101
    narrator "채팅창을 보며 웃음이 나왔다."
    # SOURCE CH06 L103
    narrator "축제 당일에도 달라진 건 없다."
    # SOURCE CH06 L105
    narrator "이 사람들이랑 있으면 언제나 이런 식이다."
    # SOURCE CH06 L107
    narrator "나는 씻고 옷을 챙겨 입은 뒤 가방을 들었다."
    # SOURCE CH06 L110 주인공 · 혼잣말
    narrator "……오늘은 진짜 시작이네."
    # CONTI SOURCE CH06 L112 [TRANSITION] 캠퍼스 광장 · 오전 8:55
    $ phone_timeline_cue("CH06", "CH06_L112")
    $ story_chat(False)
    # SOURCE CH06 L114 [BG] 축제 광장 · 오전
    $ story_draft_scene("축제 광장 · 오전")
    # SOURCE CH06 L116 [BGM] Festival Morning
    $ story_draft_bgm("Festival Morning")
    # SOURCE CH06 L120
    narrator "학교 정문을 지나자 평소와 완전히 다른 풍경이 펼쳐졌다."
    # SOURCE CH06 L122
    narrator "건물 사이에는 축제 현수막이 걸려 있었고, 광장에는 형형색색의 부스가 줄지어 있었다."
    # SOURCE CH06 L124
    narrator "멀리서 음악을 점검하는 소리가 들렸다."
    # SOURCE CH06 L126
    narrator "아직 방문객이 많지는 않았지만, 모두가 분주했다."
    # SOURCE CH06 L128
    narrator "그리고 그 한쪽에 우리가 만든 부스가 있었다."
    # SOURCE CH06 L130 [BG] 공동 체험 전시 부스 · 개장 전
    $ story_draft_scene("공동 체험 전시 부스 · 개장 전", cast=["darim", "roman", "lumi"], standing=True)
    # COMMON STANDING BEGIN CH06 L130
    $ story_stage_fade_in(["darim", "roman", "lumi"])
    # COMMON STANDING END CH06 L130
    # SOURCE CH06 L134
    narrator "어제 설치를 마쳤을 때도 실감이 났는데."
    # SOURCE CH06 L136
    narrator "오늘은 조금 더 특별하게 느껴졌다."
    # SOURCE CH06 L138
    narrator "우리가 상상했던 공간이 진짜 축제의 일부가 되어 있었다."
    # SOURCE CH06 L141 다림
    # COMMON STANDING BEGIN CH06 L141
    $ story_stage(faces={"darim": "happy"})
    # COMMON STANDING END CH06 L141
    darim "[player_name] 씨, 오셨어요?"
    # SOURCE CH06 L144 주인공
    mc "안녕하세요, 선배. 제가 늦지는 않았죠?"
    # SOURCE CH06 L147 다림
    darim "아니에요. 아직 시간 있어요."
    # SOURCE CH06 L150 로만
    roman "앗,,, 좋은 아침이에요……!"
    # SOURCE CH06 L153 주인공
    mc "로만 씨도 일찍 오셨네요."
    # SOURCE CH06 L156 로만
    # COMMON STANDING BEGIN CH06 L156
    $ story_stage(faces={"roman": "embarrassed"})
    # COMMON STANDING END CH06 L156
    roman "조금 긴장돼서요……."
    # SOURCE CH06 L159 하린
    lumi "후후. 저도 아침부터 한 번 더 확인하러 왔어요."
    # SOURCE CH06 L162 주인공
    mc "선배, 어제도 충분히 확인하셨잖아요."
    # SOURCE CH06 L165 하린
    lumi "그러니까 오늘은 마지막으로 딱 한 번만요."
    # SOURCE CH06 L169
    narrator "하린 선배의 '마지막'이라는 말을 완전히 믿을 수는 없었다."
    # SOURCE CH06 L171
    narrator "부스 배치를 점검하는 선배의 눈은 이미 다음 수정할 곳을 찾고 있었으니까."
    # CONTI SOURCE CH06 L173 [SFX] 빠른 발소리
    # SOURCE CH06 L176 시아
    # COMMON STANDING BEGIN CH06 L176
    $ story_enter("sia", side="left", face="surprised")
    # COMMON STANDING END CH06 L176
    sia "잠깐! 나 안 늦었지?!"
    # SOURCE CH06 L179 오므
    # COMMON STANDING BEGIN CH06 L179
    $ story_enter("omu", side="right", face="normal")
    # COMMON STANDING END CH06 L179
    omu "니 또 뛰어왔나."
    # SOURCE CH06 L182 시아
    sia "당연하지. 오늘만큼은 지각할 수 없으니까."
    # SOURCE CH06 L185 다림
    darim "아직 괜찮아요."
    # SOURCE CH06 L188 시아
    # COMMON STANDING BEGIN CH06 L188
    $ story_stage(faces={"sia": "smug"})
    # COMMON STANDING END CH06 L188
    sia "봤지? 나 오늘 완벽함."
    # SOURCE CH06 L191 하린
    lumi "지각하지 않은 것만으로 완벽해지시는군요."
    # SOURCE CH06 L194 시아
    # COMMON STANDING BEGIN CH06 L194
    $ story_stage(faces={"sia": "angry"})
    # COMMON STANDING END CH06 L194
    sia "아, 좀!"
    # CONTI SOURCE CH06 L196 [SD EVENT] `ch06_festival_opening`
    # CH06 VISUAL 066 BEGIN opening-start
    $ sd_event_start("ch06_festival_opening", "01", transition=0.35)
    # CH06 VISUAL 066 END opening-start
    # CONTI SOURCE CH06 L198 [연출] 개장 직전 단체 코미디. 시아가 숨을 고르고, 오므는 카메라를 든 채 어이없어하며, 로만은 웃고, 다림과 하린은 준비물을 정리하는 완성형 SD 일러스트 1장. 별도의 SD 포즈 교체 없음.
    # SOURCE CH06 L201 주인공
    mc "다들 모였으니까 마지막으로 점검해볼까요?"
    # SOURCE CH06 L204 다림
    # COMMON STANDING BEGIN CH06 L204
    $ story_stage(faces={"darim": "serious", "sia": "normal", "roman": "normal"})
    # COMMON STANDING END CH06 L204
    darim "좋아요. 운영표부터 확인할게요."
    # CONTI SOURCE CH06 L206 [전환] 일반 LD 스탠딩
    # SOURCE CH06 L209 다림
    darim "처음에는 제가 방문객 안내를 맡고, 로만 씨가 질문 카드 쪽을 봐주세요."
    # SOURCE CH06 L212 로만
    roman "네……!"
    # SOURCE CH06 L215 시아
    sia "나는 만화 설명?"
    # SOURCE CH06 L218 다림
    darim "네. 오므 씨는 사진 전시 쪽 안내 부탁드려요."
    # SOURCE CH06 L221 오므
    omu "어. 알았다."
    # SOURCE CH06 L224 하린
    lumi "저는 입구랑 통로를 확인할게요."
    # SOURCE CH06 L227 주인공
    mc "그럼 저는 전체적으로 돌아보면서 필요한 부분을 도울게요."
    # SOURCE CH06 L230 다림
    darim "좋아요. 혹시 문제가 생기면 혼자 해결하려 하지 말고 바로 공유해 주세요."
    # SOURCE CH06 L233 시아
    sia "선배, 우리 이제 전문가 다 됐는데?"
    # SOURCE CH06 L236 다림
    darim "후후. 그럼 더 잘할 수 있겠네요."
    # CH06 VISUAL 066 BEGIN opening-end
    $ sd_event_end(transition=0.35)
    $ story_stage(faces={"darim": "happy", "sia": "normal", "roman": "normal"})
    # CH06 VISUAL 066 END opening-end
    # SOURCE CH06 L240
    narrator "모두 자기 자리로 향했다."
    # SOURCE CH06 L242
    narrator "나는 입구에 세워진 작은 안내판을 바라봤다."
    # SOURCE CH06 L244
    narrator "「우리 대학의 하루를 기록하는 체험 전시」"
    # SOURCE CH06 L246
    narrator "처음에는 말로만 존재하던 이름이었다."
    # SOURCE CH06 L248
    narrator "이제는 이곳에 서 있는 사람이라면 누구나 읽을 수 있었다."
    # SOURCE CH06 L251 주인공 · 혼잣말
    mc "……잘해보자."
    # CONTI SOURCE CH06 L253 [SFX] 축제 개장 안내 방송
    # SOURCE CH06 L256 안내 방송
    ch06_announcer "잠시 후 축제 부스 운영이 시작됩니다."
    # SOURCE CH06 L258 안내 방송
    ch06_announcer "참가팀은 최종 준비를 마쳐주시기 바랍니다."
    # SOURCE CH06 L261 시아
    # COMMON STANDING BEGIN CH06 L261
    $ story_stage(faces={"sia": "happy"})
    # COMMON STANDING END CH06 L261
    sia "야, 이제 진짜 시작이다!"
    # SOURCE CH06 L264 오므
    omu "준비됐다."
    # SOURCE CH06 L267 로만
    roman "앗,,, 저도요……!"
    # SOURCE CH06 L270 하린
    lumi "좋아요. 이제 방문객만 오면 되겠네요."
    # SOURCE CH06 L273 다림
    darim "다들 힘내봐요."
    # SOURCE CH06 L276 주인공
    mc "네. 오늘 잘해봐요!"
    # CONTI SOURCE CH06 L278 [FADE TO WHITE]
    # CONTI SOURCE CH06 L280 [TEXT] 축제 개장 · 오전 10:00
    $ phone_timeline_cue("CH06", "CH06_L280")
    # CONTI SOURCE CH06 L282 [SCENE 01 END]
    jump ch06_sc02

label ch06_sc02:
    $ phone_timeline_enter("CH06", "ch06_sc02")
    # SOURCE CH06 L284 옆 부스는 오늘도 시끄럽다
    # SOURCE CH06 L286 [BG] 축제 광장 · 오전
    $ story_draft_scene("축제 광장 · 오전", cast=["roman", "sia", "darim", "omu", "lumi", "ski", "hyeophap", "hess", "bambam"], standing=True)
    # COMMON STANDING BEGIN CH06 L286
    $ story_stage_fade_in(["roman", "sia", "darim", "omu", "lumi", "ski", "hyeophap", "hess", "bambam"])
    # COMMON STANDING END CH06 L286
    # SOURCE CH06 L288 [BGM] Festival Comedy
    $ story_draft_bgm("Festival Comedy")
    # SOURCE CH06 L292
    narrator "축제가 시작되자 광장이 조금씩 북적이기 시작했다."
    # SOURCE CH06 L294
    narrator "우리 부스에도 첫 방문객이 들어왔고, 다림 선배와 로만이 안내를 시작했다."
    # SOURCE CH06 L296
    narrator "나는 입구에 놓인 자료를 확인한 뒤 잠깐 옆 부스를 바라봤다."
    # SOURCE CH06 L298
    narrator "이상하게 사람들이 모여 있었다."
    # SOURCE CH06 L301 스키
    # COMMON STANDING BEGIN CH06 L301
    $ story_stage(faces={"ski": "smug"})
    # COMMON STANDING END CH06 L301
    ski "자, 여기 봐!"
    # SOURCE CH06 L303 스키
    ski "오늘의 기분을 굽습니다!"
    # SOURCE CH06 L305 스키
    ski "세상에서 제일 맛있는 기분을 맛볼 준비 됐어?"
    # SOURCE CH06 L308 시아
    # COMMON STANDING BEGIN CH06 L308
    $ story_stage(faces={"sia": "confused"})
    # COMMON STANDING END CH06 L308
    sia "……저 사람은 진짜 안 부끄럽나?"
    # SOURCE CH06 L311 주인공
    mc "그래도 홍보는 잘하시는데요?"
    # SOURCE CH06 L314 시아
    sia "그건 인정하기 싫은데."
    # SOURCE CH06 L316 [BG] 라이벌 팀 부스
    $ story_draft_scene("라이벌 팀 부스", cast=["roman", "sia", "darim", "omu", "lumi", "ski", "hyeophap", "hess", "bambam"], standing=True)
    # COMMON STANDING BEGIN CH06 L316
    $ story_stage_fade_in(["roman", "sia", "darim", "omu", "lumi", "ski", "hyeophap", "hess", "bambam"])
    # COMMON STANDING END CH06 L316
    # SOURCE CH06 L320
    narrator "스키가 작은 시식 접시를 들어 올렸다."
    # SOURCE CH06 L322
    narrator "협합은 뒤에서 재료와 운영표를 확인하고 있었고, 헤스와 밤밤은 방문객에게 간단한 체험 방법을 설명하고 있었다."
    # SOURCE CH06 L325 스키
    ski "자, 이 쿠키는 내가 직접 만들었어."
    # SOURCE CH06 L327 스키
    ski "모양만 봐도 맛있겠지?"
    # SOURCE CH06 L330 방문객 A
    ch06_visitor_a "와, 진짜 예뻐요!"
    # SOURCE CH06 L333 스키
    ski "그렇지?"
    # SOURCE CH06 L335 스키
    ski "근데 먹으면 더 놀랄걸?"
    # SOURCE CH06 L338 방문객 A
    ch06_visitor_a "……맛있다!"
    # SOURCE CH06 L341 스키
    ski "하하! 역시!"
    # SOURCE CH06 L344 협합
    # COMMON STANDING BEGIN CH06 L344
    $ story_stage(faces={"hyeophap": "serious"})
    # COMMON STANDING END CH06 L344
    hyeophap "스키, 다음 손님도 기다리고 있어."
    # SOURCE CH06 L347 스키
    ski "알았어. 나 지금 일 잘하고 있잖아."
    # SOURCE CH06 L350 협합
    hyeophap "그건 인정."
    # SOURCE CH06 L353 스키
    # COMMON STANDING BEGIN CH06 L353
    $ story_stage(faces={"ski": "surprised"})
    # COMMON STANDING END CH06 L353
    ski "……뭐?"
    # SOURCE CH06 L356 협합
    hyeophap "왜?"
    # SOURCE CH06 L359 스키
    ski "아니, 네가 또 칭찬할 줄은 몰라서."
    # SOURCE CH06 L362 헤스
    hess "칭찬받으면 멈추시는군요."
    # SOURCE CH06 L365 밤밤
    bambam "이제 방법을 알았네요."
    # CONTI SOURCE CH06 L367 [SD EVENT] `ch06_rival_comedy`
    # CONTI SOURCE CH06 L369 [연출] 스키가 칭찬받고 얼어붙은 순간, 협합은 무심하게 다음 손님을 가리키고, 헤스·밤밤은 태연한 표정인 SD 단체 일러스트 1장.
    # SOURCE CH06 L372 시아
    # COMMON STANDING BEGIN CH06 L372
    $ story_stage(faces={"sia": "happy"})
    # COMMON STANDING END CH06 L372
    sia "ㅋㅋㅋㅋㅋ"
    # SOURCE CH06 L374 시아
    sia "야, 스키!"
    # SOURCE CH06 L377 스키
    ski "왜!"
    # SOURCE CH06 L380 시아
    sia "오늘은 진짜 잘하네."
    # SOURCE CH06 L383 스키
    ski "……."
    # SOURCE CH06 L386 스키
    ski "너까지 왜 그래?"
    # SOURCE CH06 L389 시아
    sia "아니, 진심인데?"
    # SOURCE CH06 L392 스키
    ski "……이거 무슨 함정이냐?"
    # SOURCE CH06 L395 주인공
    mc "다들 진심으로 칭찬하는 것 같은데요."
    # SOURCE CH06 L398 스키
    ski "……."
    # SOURCE CH06 L400 스키
    ski "뭐, 당연한 결과긴 하지!"
    # SOURCE CH06 L403 협합
    hyeophap "이제 정상으로 돌아왔네."
    # CONTI SOURCE CH06 L405 [전환] 일반 LD 스탠딩
    # SOURCE CH06 L409
    narrator "그러다 한 방문객이 질문 카드를 집어 들었다."
    # SOURCE CH06 L412 방문객 B
    ch06_visitor_b "여기서 기분을 고르면 그걸 검사하는 건가요?"
    # SOURCE CH06 L415 밤밤
    bambam "아니에요. 심리검사나 진단은 아니고요."
    # SOURCE CH06 L417 밤밤
    bambam "오늘 기분을 재미있게 표현해보는 체험이에요."
    # SOURCE CH06 L420 헤스
    hess "결과를 기록하거나 제출하실 필요도 없어요."
    # SOURCE CH06 L423 방문객 B
    ch06_visitor_b "아, 그렇군요."
    # SOURCE CH06 L427
    narrator "설명은 간단하고 명확했다."
    # SOURCE CH06 L429
    narrator "CH03에서 두 부스가 함께 운영 문제를 해결한 경험이 반영된 모양이다."
    # SOURCE CH06 L432 협합
    hyeophap "우리도 시범 운영 후에 안내 방식을 많이 바꿨어."
    # SOURCE CH06 L435 다림
    darim "확실히 이해하기 쉬워졌네요."
    # SOURCE CH06 L438 스키
    ski "당연하지. 완벽한 팀이니까."
    # SOURCE CH06 L441 시아
    sia "너만 빼면?"
    # SOURCE CH06 L444 스키
    ski "야!"
    # SOURCE CH06 L448
    narrator "또 익숙한 말싸움이 시작됐다."
    # SOURCE CH06 L450
    narrator "그런데 이제는 그 모습이 불편하지 않았다."
    # SOURCE CH06 L452
    narrator "저 사람들도 오늘을 위해 많은 준비를 했다."
    # SOURCE CH06 L454
    narrator "우리처럼."
    # SOURCE CH06 L457 협합
    hyeophap "참, 오늘 사람 많아지면 통로 확인 좀 부탁해."
    # SOURCE CH06 L460 하린
    lumi "네. 저희 쪽도 계속 보고 있을게요."
    # SOURCE CH06 L463 다림
    darim "필요하면 서로 바로 연락해요."
    # SOURCE CH06 L466 협합
    hyeophap "좋아."
    # SOURCE CH06 L469 스키
    ski "야, 근데."
    # SOURCE CH06 L472 시아
    sia "왜."
    # SOURCE CH06 L475 스키
    ski "오늘 끝나면 우리 승부도 끝인 거냐?"
    # SOURCE CH06 L478 시아
    sia "뭐, 그렇겠지?"
    # SOURCE CH06 L481 스키
    ski "……아쉽네."
    # SOURCE CH06 L484 시아
    sia "……."
    # SOURCE CH06 L486 시아
    sia "야, 너 그런 말도 하냐?"
    # SOURCE CH06 L489 스키
    ski "왜. 재미있었잖아."
    # SOURCE CH06 L493
    narrator "시아가 잠깐 말을 멈췄다."
    # SOURCE CH06 L495
    narrator "그러더니 피식 웃었다."
    # SOURCE CH06 L498 시아
    sia "……그건 그렇지."
    # SOURCE CH06 L501 주인공
    mc "그럼 다음에 또 경쟁하셔도 되겠네요."
    # SOURCE CH06 L504 스키
    ski "좋지. 다음엔 내가 압승할 거야."
    # SOURCE CH06 L507 시아
    sia "응 아니야~"
    # SOURCE CH06 L510 협합
    hyeophap "다음 행사는 아직 정해진 것도 없어."
    # SOURCE CH06 L513 오므
    omu "벌써부터 시끄럽네."
    # SOURCE CH06 L517
    narrator "결국 마지막까지 이런 식이다."
    # SOURCE CH06 L519
    narrator "하지만 경쟁 상대가 있었다는 게 생각보다 좋은 일이었는지도 모르겠다."
    # SOURCE CH06 L521
    narrator "우리도 저 사람들 덕분에 조금 더 열심히 준비했으니까."
    # CONTI SOURCE CH06 L523 [SFX] 우리 부스 쪽 호출
    # SOURCE CH06 L526 로만
    roman "[player_name] 씨……! 잠깐 도와주실 수 있을까요?"
    # SOURCE CH06 L529 주인공
    mc "네, 금방 갈게요!"
    # SOURCE CH06 L532 시아
    sia "가자. 우리도 손님 받아야지."
    # SOURCE CH06 L535 스키
    ski "야! 오늘은 서로 제대로 해보자!"
    # SOURCE CH06 L538 시아
    sia "당연하지!"
    # CONTI SOURCE CH06 L540 [SCENE 02 END]
    jump ch06_sc03

label ch06_sc03:
    $ phone_timeline_enter("CH06", "ch06_sc03")
    # SOURCE CH06 L542 우리가 준비한 하루
    # SOURCE CH06 L544 [BG] 공동 체험 전시 부스 · 낮
    $ story_draft_scene("공동 체험 전시 부스 · 낮", cast=["roman", "darim"], standing=True)
    # COMMON STANDING BEGIN CH06 L544
    $ story_stage_fade_in(["roman", "darim"])
    # COMMON STANDING END CH06 L544
    # SOURCE CH06 L546 [BGM] Warm Festival
    $ story_draft_bgm("Warm Festival")
    # SOURCE CH06 L550
    narrator "부스로 돌아오니 예상보다 많은 사람이 안을 둘러보고 있었다."
    # SOURCE CH06 L552
    narrator "누군가는 벽에 걸린 사진을 바라봤고, 누군가는 질문 카드를 읽으며 고민하고 있었다."
    # SOURCE CH06 L554
    narrator "조금 긴장됐다."
    # SOURCE CH06 L556
    narrator "그동안은 우리가 준비한 것만 봤는데, 이제는 처음 보는 사람들이 이 공간을 경험하고 있었다."
    # SOURCE CH06 L559 로만
    # COMMON STANDING BEGIN CH06 L559
    $ story_stage(faces={"roman": "normal"})
    # COMMON STANDING END CH06 L559
    roman "앗,,, 여기 질문 카드를 하나 골라보시면 돼요."
    # SOURCE CH06 L562 방문객 A
    ch06_visitor_a "꼭 적어야 하나요?"
    # SOURCE CH06 L565 로만
    # COMMON STANDING BEGIN CH06 L565
    $ story_stage(faces={"roman": "surprised"})
    # COMMON STANDING END CH06 L565
    roman "아니에요……!"
    # SOURCE CH06 L567 로만
    roman "그냥 읽기만 하셔도 괜찮아요."
    # SOURCE CH06 L570 방문객 A
    ch06_visitor_a "그럼 먼저 구경해볼게요."
    # SOURCE CH06 L573 로만
    # COMMON STANDING BEGIN CH06 L573
    $ story_stage(faces={"roman": "happy"})
    # COMMON STANDING END CH06 L573
    roman "네. 편하게 둘러보세요."
    # SOURCE CH06 L577
    narrator "로만은 조심스럽게 웃었다."
    # SOURCE CH06 L579
    narrator "CH03에서 방문객이 참여 방법을 이해하지 못했던 일이 떠올랐다."
    # SOURCE CH06 L581
    narrator "이제는 굳이 누군가에게 설명을 떠넘기지 않아도 로만이 스스로 응대하고 있었다."
    # SOURCE CH06 L584 다림
    darim "[player_name] 씨, 이쪽 확인 부탁드려도 될까요?"
    # SOURCE CH06 L587 주인공
    mc "네. 무슨 일이에요?"
    # SOURCE CH06 L590 다림
    darim "잠깐 사람이 몰릴 것 같아서요. 관람 안내를 도와주세요."
    # SOURCE CH06 L593 주인공
    mc "알겠어요."
    # SOURCE CH06 L595 [BG] 전시 입구
    $ story_draft_scene("전시 입구", cast=["omu", "sia", "lumi"], standing=True)
    # COMMON STANDING BEGIN CH06 L595
    $ story_stage_fade_in(["omu", "sia", "lumi"])
    # COMMON STANDING END CH06 L595
    # SOURCE CH06 L598 주인공
    mc "안녕하세요. 이쪽으로 들어오시면 사진과 글을 먼저 보실 수 있어요."
    # SOURCE CH06 L601 방문객 B
    ch06_visitor_b "체험은 어디서 해요?"
    # SOURCE CH06 L604 주인공
    mc "안쪽 테이블에서 하실 수 있어요. 다만 원하지 않으시면 전시만 보고 가셔도 괜찮아요."
    # SOURCE CH06 L607 방문객 B
    ch06_visitor_b "아, 감사합니다."
    # SOURCE CH06 L611
    narrator "말이 자연스럽게 나왔다."
    # SOURCE CH06 L613
    narrator "몇 주 전이었다면 이런 설명을 하려고 원고부터 찾았을 텐데."
    # SOURCE CH06 L615
    narrator "이제는 어디에 무엇이 있는지 눈을 감고도 알 것 같았다."
    # CONTI SOURCE CH06 L617 [SFX] 전시 안내판을 넘기는 소리
    # SOURCE CH06 L620 방문객 C
    ch06_visitor_c "이 사진은 어디예요?"
    # SOURCE CH06 L623 오므
    omu "교내에서 준비하던 모습이에요."
    # SOURCE CH06 L625 오므
    omu "완성된 사진만 있는 게 아니라 만드는 과정도 같이 넣었어요."
    # SOURCE CH06 L628 방문객 C
    ch06_visitor_c "아, 그러니까 더 정겹네요."
    # SOURCE CH06 L631 오므
    omu "……어."
    # SOURCE CH06 L633 오므
    # COMMON STANDING BEGIN CH06 L633
    $ story_stage(faces={"omu": "happy"})
    # COMMON STANDING END CH06 L633
    omu "그렇게 봐주시면 좋죠."
    # SOURCE CH06 L637
    narrator "오므는 자신의 사진을 다시 바라봤다."
    # SOURCE CH06 L639
    narrator "CH04에서 굳이 남겨두고 싶다고 했던, 조금 어수선한 작업 공간의 사진이었다."
    # SOURCE CH06 L641
    narrator "지금은 그 사진 앞에 사람들이 멈춰 서 있었다."
    # SOURCE CH06 L644 시아
    sia "이쪽은 참여 방법을 만화로 만든 거야."
    # SOURCE CH06 L647 방문객 D
    ch06_visitor_d "아, 귀엽다."
    # SOURCE CH06 L650 시아
    # COMMON STANDING BEGIN CH06 L650
    $ story_stage(faces={"sia": "smug"})
    # COMMON STANDING END CH06 L650
    sia "그치?"
    # SOURCE CH06 L653 방문객 D
    ch06_visitor_d "이 캐릭터는 왜 넘어져 있어요?"
    # SOURCE CH06 L656 시아
    sia "……."
    # SOURCE CH06 L658 시아
    # COMMON STANDING BEGIN CH06 L658
    $ story_stage(faces={"sia": "embarrassed"})
    # COMMON STANDING END CH06 L658
    sia "그건 설명을 쉽게 하려고……."
    # SOURCE CH06 L661 하린
    # COMMON STANDING BEGIN CH06 L661
    $ story_stage(faces={"lumi": "smug"})
    # COMMON STANDING END CH06 L661
    lumi "시아 씨가 꼭 넣어야 한다고 주장하신 장면이에요."
    # SOURCE CH06 L664 시아
    sia "야, 그건 왜 설명하는데!"
    # SOURCE CH06 L667 방문객 D
    ch06_visitor_d "하하, 재미있네요."
    # SOURCE CH06 L671
    narrator "방문객이 웃었다."
    # SOURCE CH06 L673
    narrator "시아는 곧바로 어깨를 으쓱했다."
    # SOURCE CH06 L676 시아
    # COMMON STANDING BEGIN CH06 L676
    $ story_stage(faces={"sia": "happy"})
    # COMMON STANDING END CH06 L676
    sia "봤지? 내 개그 통한다니까."
    # SOURCE CH06 L679 주인공
    mc "이번에는 인정할게요."
    # SOURCE CH06 L682 시아
    sia "이번에는?"
    # SOURCE CH06 L685 주인공
    mc "네. 이번에는요."
    # SOURCE CH06 L688 시아
    sia "와, 진짜."
    # SOURCE CH06 L692
    narrator "이번에는 시아도 웃었다."
    # CONTI SOURCE CH06 L694 [시간 경과 · 오전 11:20]
    $ phone_timeline_cue("CH06", "CH06_L694")
    # SOURCE CH06 L696 [BG] 기록 참여 테이블
    $ story_draft_scene("기록 참여 테이블", cast=["darim"], standing=True)
    # COMMON STANDING BEGIN CH06 L696
    $ story_stage_fade_in(["darim"])
    # COMMON STANDING END CH06 L696
    # SOURCE CH06 L700
    narrator "잠시 후 한 방문객이 다림 선배에게 다가왔다."
    # SOURCE CH06 L703 방문객 E
    ch06_visitor_e "아까 제가 적었던 글 있잖아요."
    # SOURCE CH06 L706 다림
    # COMMON STANDING BEGIN CH06 L706
    $ story_stage(faces={"darim": "serious"})
    # COMMON STANDING END CH06 L706
    darim "네. 어떤 도움이 필요하세요?"
    # SOURCE CH06 L709 방문객 E
    ch06_visitor_e "생각이 바뀌어서요. 전시하지 않았으면 좋겠어요."
    # SOURCE CH06 L713
    narrator "CH03의 일이 떠올랐다."
    # SOURCE CH06 L715
    narrator "그때는 절차가 준비되어 있지 않아 모두가 당황했었다."
    # SOURCE CH06 L717
    narrator "하지만 이번에는 다림 선배가 바로 안내했다."
    # SOURCE CH06 L720 다림
    darim "네. 괜찮아요."
    # SOURCE CH06 L722 다림
    darim "기록을 확인해서 전시 대상에서 제외해드릴게요."
    # SOURCE CH06 L725 방문객 E
    ch06_visitor_e "이미 걸려 있으면 어떡하죠?"
    # SOURCE CH06 L728 다림
    darim "이미 전시 중이어도 회수할 수 있어요."
    # SOURCE CH06 L730 다림
    darim "지금 같이 확인해드릴게요."
    # SOURCE CH06 L733 주인공
    mc "선배, 제가 다른 방문객 안내를 맡을게요."
    # SOURCE CH06 L736 다림
    darim "감사해요."
    # SOURCE CH06 L740
    narrator "다림 선배는 해당 방문객과 기록을 확인했다."
    # SOURCE CH06 L742
    narrator "선배는 다른 사람에게 내용이 보이지 않도록 조심스럽게 처리했고, 요청을 마친 뒤에는 회수가 끝났다는 사실을 알려줬다."
    # SOURCE CH06 L745 방문객 E
    ch06_visitor_e "감사합니다. 괜히 번거롭게 한 건가 싶었는데……."
    # SOURCE CH06 L748 다림
    darim "아니에요. 원하실 때 바꾸실 수 있도록 준비한 거예요."
    # SOURCE CH06 L751 방문객 E
    ch06_visitor_e "그럼 조금 더 구경하고 갈게요."
    # SOURCE CH06 L754 다림
    # COMMON STANDING BEGIN CH06 L754
    $ story_stage(faces={"darim": "happy"})
    # COMMON STANDING END CH06 L754
    darim "네. 편하게 둘러보세요."
    # SOURCE CH06 L758
    narrator "방문객은 안심한 듯 미소 지었다."
    # SOURCE CH06 L760
    narrator "다림 선배가 나를 바라봤다."
    # SOURCE CH06 L763 다림
    darim "이번에는 잘 처리됐네요."
    # SOURCE CH06 L766 주인공
    mc "네. 지난번에 절차를 만들어둔 게 도움이 됐어요."
    # SOURCE CH06 L769 다림
    darim "그때는 정신없었는데……."
    # SOURCE CH06 L771 다림
    darim "지금 생각하면 필요한 경험이었어요."
    # SOURCE CH06 L775
    narrator "정말 그랬다."
    # SOURCE CH06 L777
    narrator "그날의 작은 문제를 그냥 넘겼다면 오늘도 똑같은 실수를 했을지 모른다."
    # CONTI SOURCE CH06 L779 [시간 경과 · 오후 12:15]
    $ phone_timeline_cue("CH06", "CH06_L779")
    # SOURCE CH06 L781 [BG] 부스 중앙 · 점심 무렵
    $ story_draft_scene("부스 중앙 · 점심 무렵", cast=["lumi"], standing=True)
    # COMMON STANDING BEGIN CH06 L781
    $ story_stage_fade_in(["lumi"])
    # COMMON STANDING END CH06 L781
    # SOURCE CH06 L784 하린
    # COMMON STANDING BEGIN CH06 L784
    $ story_stage(faces={"lumi": "serious"})
    # COMMON STANDING END CH06 L784
    lumi "입구 쪽 잠깐 확인할게요."
    # SOURCE CH06 L787 주인공
    mc "통로에 문제 있나요?"
    # SOURCE CH06 L790 하린
    lumi "아직은 없어요. 다만 사람이 늘어나서 안내판을 조금 옮기면 좋겠네요."
    # SOURCE CH06 L793 주인공
    mc "그럼 같이 옮길까요?"
    # SOURCE CH06 L796 하린
    lumi "네. 부탁드릴게요."
    # SOURCE CH06 L800
    narrator "하린 선배와 함께 안내판을 옮겼다."
    # SOURCE CH06 L802
    narrator "방문객들이 지나갈 공간이 조금 더 넓어졌다."
    # SOURCE CH06 L805 하린
    lumi "……좋네요."
    # SOURCE CH06 L808 주인공
    mc "이제 괜찮을까요?"
    # SOURCE CH06 L811 하린
    lumi "응. 처음 모형 만들었을 때보다 훨씬 나아졌어요."
    # SOURCE CH06 L814 주인공
    mc "선배가 계속 수정하신 덕분이죠."
    # SOURCE CH06 L817 하린
    lumi "……."
    # SOURCE CH06 L819 하린
    # COMMON STANDING BEGIN CH06 L819
    $ story_stage(faces={"lumi": "embarrassed"})
    # COMMON STANDING END CH06 L819
    lumi "오늘도 그런 말씀을 하시네."
    # SOURCE CH06 L822 주인공
    mc "사실이니까요."
    # SOURCE CH06 L825 하린
    # COMMON STANDING BEGIN CH06 L825
    $ story_stage(faces={"lumi": "happy"})
    # COMMON STANDING END CH06 L825
    lumi "후후. 알겠어요."
    # SOURCE CH06 L829
    narrator "하린 선배는 조금 웃으며 안내판을 바로 세웠다."
    # SOURCE CH06 L831
    narrator "우리가 만든 공간이 실제로 사람들에게 쓰이고 있었다."
    # SOURCE CH06 L833
    narrator "그 사실이 선배에게도 특별하게 느껴지는 것 같았다."
    # CONTI SOURCE CH06 L835 [시간 경과 · 오후 12:55]
    $ phone_timeline_cue("CH06", "CH06_L835")
    # SOURCE CH06 L837 [BG] 부스 뒤편 휴식 공간
    $ story_draft_scene("부스 뒤편 휴식 공간", cast=["roman", "sia", "darim", "omu", "lumi"], standing=True)
    # COMMON STANDING BEGIN CH06 L837
    $ story_stage_fade_in(["roman", "sia", "darim", "omu", "lumi"])
    # COMMON STANDING END CH06 L837
    # SOURCE CH06 L840 시아
    sia "아아아."
    # SOURCE CH06 L842 시아
    sia "배고파."
    # SOURCE CH06 L845 오므
    omu "도시락 먹었잖아."
    # SOURCE CH06 L848 시아
    sia "일하니까 다시 배고프다고."
    # SOURCE CH06 L851 로만
    # COMMON STANDING BEGIN CH06 L851
    $ story_stage(faces={"roman": "sad"})
    # COMMON STANDING END CH06 L851
    roman "앗,,, 저는 목이 조금 아파요……."
    # SOURCE CH06 L854 다림
    darim "로만 씨는 설명을 많이 하셨으니까요. 잠깐 쉬세요."
    # SOURCE CH06 L857 하린
    lumi "오후 교대 시간도 됐네요."
    # SOURCE CH06 L860 다림
    darim "네. 다들 돌아가면서 쉬어요."
    # SOURCE CH06 L864
    narrator "다림 선배는 운영표를 확인했다."
    # SOURCE CH06 L867 다림
    darim "[player_name] 씨는 먼저 쉬셔도 괜찮아요."
    # SOURCE CH06 L870 주인공
    mc "정말요? 아직 도울 일이 있을 것 같은데요."
    # SOURCE CH06 L873 다림
    darim "아까부터 계속 일하셨잖아요."
    # SOURCE CH06 L875 다림
    darim "지금은 쉬셔도 돼요."
    # SOURCE CH06 L878 시아
    # COMMON STANDING BEGIN CH06 L878
    $ story_stage(faces={"sia": "happy"})
    # COMMON STANDING END CH06 L878
    sia "맞아. 우리도 축제 좀 즐겨야지."
    # SOURCE CH06 L881 오므
    omu "니는 벌써 쉬고 싶은 거 아이가?"
    # SOURCE CH06 L884 시아
    sia "나는 언제나 쉬고 싶거든."
    # SOURCE CH06 L888
    narrator "나는 웃으며 고개를 끄덕였다."
    # SOURCE CH06 L890
    narrator "CH05에서 정했던 개인 약속이 떠올랐다."
    # SOURCE CH06 L892
    narrator "오늘은 부스 밖에서도 즐거운 일이 기다리고 있었다."
    # SOURCE CH06 L894 [FLAG] `ch06_booth_operation_complete = True`
    $ story_flag("ch06_booth_operation_complete", True)
    # CONTI SOURCE CH06 L896 [SCENE 03 END]
    # CONTI SOURCE CH06 L898 [SC04 DISPATCH PLAN] SCENE 04. 오늘만큼은 우리도 즐기자
    # CONTI SOURCE CH06 L899 [SC04 DISPATCH PLAN] 오후 1:30~3:00 · 히로인별 축제 데이트 · CH06 로맨스 핵심
    $ phone_timeline_cue("CH06", "CH06_L899")
    # CONTI SOURCE CH06 L901 [SC04 DISPATCH PLAN] 여기부터는 ch06_festival_partner에 따라 다섯 이벤트 중 하나만 재생돼.
    jump ch06_sc04

label ch06_sc04:
    $ phone_timeline_enter("CH06", "ch06_sc04")
    # SOURCE CH06 L903 CH05에서 선택한 축제 파트너 분기
    if story_id(ch06_festival_partner) == "roman":
        jump ch06_sc04_roman
    elif story_id(ch06_festival_partner) == "sia":
        jump ch06_sc04_sia
    elif story_id(ch06_festival_partner) == "darim":
        jump ch06_sc04_darim
    elif story_id(ch06_festival_partner) == "omu":
        jump ch06_sc04_omu
    elif story_id(ch06_festival_partner) == "lumi":
        jump ch06_sc04_lumi
    else:
        # Old/malformed saves do not select another person automatically.
        jump ch06_sc05

label ch06_sc04_darim:
    $ phone_timeline_enter("CH06", "ch06_sc04_darim")
    # SOURCE CH06_DARIM L2 다림 「선배의 승부는 아직 끝나지 않았다」
    # SOURCE SHA256: 70549a88cc7ec7582d5c7584b627ebf86ceefbbcf0e9a571d4cb427167b95d1c
    jump ch06_sc04_darim_01

label ch06_sc04_darim_01:
    $ phone_timeline_enter("CH06", "ch06_sc04_darim_01")
    # SOURCE CH06_DARIM L7 선배의 승부욕
    # SOURCE CH06_DARIM L8 [BG] 축제 게임 체험 구역 · 오후
    $ story_draft_scene("축제 게임 체험 구역 · 오후", cast=["darim"], standing=True)
    # COMMON STANDING BEGIN CH06_DARIM L8
    $ story_stage_fade_in(["darim"])
    # COMMON STANDING END CH06_DARIM L8
    # SOURCE CH06_DARIM L9 [BGM] Light Game
    $ story_draft_bgm("Light Game")
    # CONTI SOURCE CH06_DARIM L10 [LD] 다림 · 기본 미소
    # SOURCE CH06_DARIM L12
    narrator "게임 체험 부스 앞에는 사람들이 줄을 서 있었다."
    # SOURCE CH06_DARIM L13
    narrator "화면에는 두 명이 함께 플레이할 수 있는 간단한 협동 게임이 실행되어 있었다."
    # SOURCE CH06_DARIM L14
    narrator "다림 선배는 이미 안내판을 읽고 있었다."
    # SOURCE CH06_DARIM L16 주인공
    # CH06 VISUAL 0610 BEGIN darim-01-start
    $ cg_start("ch06_festival_darim_01", transition=0.35)
    # CH06 VISUAL 0610 END darim-01-start
    mc "선배, 많이 기다리셨어요?"
    # SOURCE CH06_DARIM L18 다림
    # COMMON STANDING BEGIN CH06_DARIM L18
    $ story_stage(faces={"darim": "happy"})
    # COMMON STANDING END CH06_DARIM L18
    darim "아니에요. 저도 방금 왔어요."
    # SOURCE CH06_DARIM L19 다림
    darim "그런데 생각보다 재미있어 보이네요."
    # SOURCE CH06_DARIM L21 주인공
    mc "벌써 규칙 다 읽으셨어요?"
    # SOURCE CH06_DARIM L23 다림
    darim "후후. 시작하기 전에 알아둬야죠."
    # SOURCE CH06_DARIM L25 주인공
    mc "오늘도 이길 준비부터 하시는군요."
    # SOURCE CH06_DARIM L27 다림
    # COMMON STANDING BEGIN CH06_DARIM L27
    $ story_stage(faces={"darim": "smug"})
    # COMMON STANDING END CH06_DARIM L27
    darim "당연하죠."
    # SOURCE CH06_DARIM L28 다림
    darim "대충 할 수는 없잖아요?"
    # SOURCE CH06_DARIM L30
    narrator "차분하게 웃는 모습과 달리 눈빛은 꽤 진지했다."
    # CH06 VISUAL 0610 BEGIN darim-01-end
    $ cg_end(transition=0.35)
    $ story_stage(faces={"darim": "smug"})
    # CH06 VISUAL 0610 END darim-01-end
    # SOURCE CH06_DARIM L32 진행 요원
    ch06_game_staff "다음 두 분, 들어오세요."
    # SOURCE CH06_DARIM L33 [BG] 게임 체험 테이블
    $ story_draft_scene("게임 체험 테이블", cast=["darim"], standing=True)
    # COMMON STANDING BEGIN CH06_DARIM L33
    $ story_stage_fade_in(["darim"])
    # COMMON STANDING END CH06_DARIM L33
    # SOURCE CH06_DARIM L35 진행 요원
    ch06_game_staff "제한 시간 안에 두 캐릭터가 함께 목표 지점에 도착하면 성공입니다."
    # SOURCE CH06_DARIM L37 다림
    darim "협동 게임이네요."
    # SOURCE CH06_DARIM L39 주인공
    mc "그럼 오늘은 경쟁하지 않아도 되겠네요."
    # SOURCE CH06_DARIM L41 다림
    darim "……그건 조금 아쉬운데요?"
    # SOURCE CH06_DARIM L43 주인공
    mc "선배?"
    # SOURCE CH06_DARIM L45 다림
    darim "후후. 농담이에요."
    # SOURCE CH06_DARIM L47
    narrator "……농담일까?"
    # CONTI SOURCE CH06_DARIM L48 [SFX] 게임 시작 효과음
    $ refresh_sfx("game_start")
    # SOURCE CH06_DARIM L50 다림
    # COMMON STANDING BEGIN CH06_DARIM L50
    $ story_stage(faces={"darim": "serious"})
    # COMMON STANDING END CH06_DARIM L50
    darim "오른쪽으로 가세요!"
    # SOURCE CH06_DARIM L52 주인공
    mc "오른쪽이요?"
    # SOURCE CH06_DARIM L54 다림
    # COMMON STANDING BEGIN CH06_DARIM L54
    $ story_stage(faces={"darim": "surprised"})
    # COMMON STANDING END CH06_DARIM L54
    darim "아니, 잠깐! 그쪽은 함정이에요!"
    # SOURCE CH06_DARIM L56 주인공
    mc "선배, 그럼 어느 쪽이에요?!"
    # SOURCE CH06_DARIM L58 다림
    darim "일단 멈추세요!"
    # CONTI SOURCE CH06_DARIM L59 [SFX] 게임 실패 효과음
    $ refresh_sfx("game_fail")
    # SOURCE CH06_DARIM L61 주인공
    mc "……."
    # SOURCE CH06_DARIM L63 다림
    darim "……."
    # SOURCE CH06_DARIM L65 다림
    # COMMON STANDING BEGIN CH06_DARIM L65
    $ story_stage(faces={"darim": "happy"})
    # COMMON STANDING END CH06_DARIM L65
    darim "후후."
    # SOURCE CH06_DARIM L67 주인공
    mc "지금 웃으시는 거예요?"
    # SOURCE CH06_DARIM L69 다림
    darim "아니에요."
    # SOURCE CH06_DARIM L70 다림
    darim "……조금요."
    # SOURCE CH06_DARIM L72
    narrator "결국 나도 웃었다."
    # SOURCE CH06_DARIM L73
    narrator "두 사람 다 게임을 좋아한다고 했는데."
    # SOURCE CH06_DARIM L74
    narrator "첫판부터 이렇게 실패할 줄이야."
    # SOURCE CH06_DARIM L76 다림
    # COMMON STANDING BEGIN CH06_DARIM L76
    $ story_stage(faces={"darim": "serious"})
    # COMMON STANDING END CH06_DARIM L76
    darim "이번에는 역할을 나눠봐요."
    # SOURCE CH06_DARIM L78 주인공
    mc "좋아요. 제가 앞쪽을 확인할게요."
    # SOURCE CH06_DARIM L80 다림
    darim "그럼 제가 뒤쪽 스위치를 맡을게요."
    # CONTI SOURCE CH06_DARIM L81 [SFX] 게임 재시작
    $ refresh_sfx("game_start")
    # SOURCE CH06_DARIM L83
    narrator "두 번째 시도에서는 훨씬 수월했다."
    # SOURCE CH06_DARIM L84
    narrator "서로가 맡은 역할을 지키면서 필요한 순간에만 도움을 요청했다."
    # SOURCE CH06_DARIM L86 다림
    darim "지금이에요!"
    # SOURCE CH06_DARIM L88 주인공
    mc "네!"
    # CONTI SOURCE CH06_DARIM L89 [SFX] 게임 클리어 효과음
    $ refresh_sfx("game_clear")
    # SOURCE CH06_DARIM L91 진행 요원
    ch06_game_staff "축하합니다! 성공하셨어요!"
    # SOURCE CH06_DARIM L93 다림
    # COMMON STANDING BEGIN CH06_DARIM L93
    $ story_stage(faces={"darim": "happy"})
    # COMMON STANDING END CH06_DARIM L93
    darim "……와!"
    # SOURCE CH06_DARIM L95 주인공
    mc "성공했네요!"
    # SOURCE CH06_DARIM L97
    narrator "다림 선배가 환하게 웃었다."
    # SOURCE CH06_DARIM L98
    narrator "평소에는 조용하고 차분한 선배였는데."
    # SOURCE CH06_DARIM L99
    narrator "게임 하나에 이렇게 즐거워하는 모습이 조금 새로웠다."
    # SOURCE CH06_DARIM L101 다림
    darim "후후. 역시 같이 하니까 잘되네요."
    # SOURCE CH06_DARIM L103 주인공
    mc "선배가 스위치를 잘 눌러주신 덕분이에요."
    # SOURCE CH06_DARIM L105 다림
    darim "아니에요. [player_name] 씨도 잘하셨어요."
    # SOURCE CH06_DARIM L107
    narrator "게임 부스에서 작은 고양이 모양 기념 스티커를 받았다."
    # SOURCE CH06_DARIM L108
    narrator "다림 선배는 그것을 보고 다시 웃었다."
    # SOURCE CH06_DARIM L110 다림
    darim "어머. 고양이네요."
    # SOURCE CH06_DARIM L112 주인공
    mc "선배 취향이네요."
    # SOURCE CH06_DARIM L114 다림
    darim "맞아요."
    # SOURCE CH06_DARIM L115 다림
    darim "이건 꽤 마음에 드는데요?"
    jump ch06_sc04_darim_02

label ch06_sc04_darim_02:
    $ phone_timeline_enter("CH06", "ch06_sc04_darim_02")
    # SOURCE CH06_DARIM L116 같이 하니까 좋은 것
    # CONTI SOURCE CH06_DARIM L117 [시간 경과 · 오후 2:15]
    $ phone_timeline_cue("CH06", "CH06_DARIM_L117")
    # SOURCE CH06_DARIM L118 [BG] 축제 카페 휴식 공간
    $ story_draft_scene("축제 카페 휴식 공간", cast=["darim"], standing=True)
    # COMMON STANDING BEGIN CH06_DARIM L118
    $ story_stage_fade_in(["darim"])
    # COMMON STANDING END CH06_DARIM L118
    # SOURCE CH06_DARIM L119 [BGM] Warm Festival Afternoon
    $ story_draft_bgm("Warm Festival Afternoon")
    # SOURCE CH06_DARIM L121
    narrator "우리는 작은 테이블에 앉아 음료를 마셨다."
    # SOURCE CH06_DARIM L123 다림
    # COMMON STANDING BEGIN CH06_DARIM L123
    $ story_stage(faces={"darim": "happy"})
    # COMMON STANDING END CH06_DARIM L123
    # CH06 VISUAL 0610 BEGIN darim-02-start
    $ cg_start("ch06_festival_darim_02", transition=0.35)
    # CH06 VISUAL 0610 END darim-02-start
    darim "생각보다 재미있었어요."
    # SOURCE CH06_DARIM L125 주인공
    mc "네. 처음에는 조금 당황했지만요."
    # SOURCE CH06_DARIM L127 다림
    darim "후후. 저도요."
    # SOURCE CH06_DARIM L128 다림
    darim "그런데 같이 하면서 역할을 나누니까 훨씬 쉬워졌죠?"
    # SOURCE CH06_DARIM L130 주인공
    mc "그러네요. 축제 준비할 때랑 비슷하네요."
    # SOURCE CH06_DARIM L132 다림
    darim "맞아요."
    # SOURCE CH06_DARIM L134
    narrator "다림 선배는 컵을 내려놓았다."
    # SOURCE CH06_DARIM L136 다림
    darim "있잖아요."
    # SOURCE CH06_DARIM L138 주인공
    mc "네?"
    # SOURCE CH06_DARIM L140 다림
    # COMMON STANDING BEGIN CH06_DARIM L140
    $ story_stage(faces={"darim": "serious"})
    # COMMON STANDING END CH06_DARIM L140
    darim "처음에는 제가 다른 사람을 잘 챙겨야 한다고 생각했거든요."
    # SOURCE CH06_DARIM L141 다림
    darim "선배이기도 하고, 팀에서 맡은 역할도 있었으니까요."
    # SOURCE CH06_DARIM L143 주인공
    mc "네."
    # SOURCE CH06_DARIM L145 다림
    darim "그런데 요즘은……."
    # SOURCE CH06_DARIM L146 다림
    darim "꼭 제가 다 해야 하는 건 아니라는 걸 알게 됐어요."
    # SOURCE CH06_DARIM L148 주인공
    mc "저도 그랬어요."
    # SOURCE CH06_DARIM L150 다림
    # COMMON STANDING BEGIN CH06_DARIM L150
    $ story_stage(faces={"darim": "happy"})
    # COMMON STANDING END CH06_DARIM L150
    darim "……후후."
    # SOURCE CH06_DARIM L151 다림
    darim "그래서 오늘처럼 아무 생각 없이 같이 노는 시간이 좋네요."
    # SOURCE CH06_DARIM L153
    narrator "다림 선배는 자연스럽게 웃었다."
    # SOURCE CH06_DARIM L154
    narrator "그 웃음에는 일을 잘 끝냈다는 안도감과는 조금 다른 편안함이 있었다."
    # SOURCE CH06_DARIM L156 주인공
    mc "저도 선배랑 이렇게 노니까 좋아요."
    # SOURCE CH06_DARIM L158 다림
    darim "……."
    # SOURCE CH06_DARIM L159 다림
    # COMMON STANDING BEGIN CH06_DARIM L159
    $ story_stage(faces={"darim": "embarrassed"})
    # COMMON STANDING END CH06_DARIM L159
    darim "그렇게 말씀하시니까 기분 좋네요."
    # CH06 VISUAL 0610 BEGIN darim-02-end
    $ cg_end(transition=0.35)
    $ story_stage(faces={"darim": "embarrassed"})
    # CH06 VISUAL 0610 END darim-02-end
    # SOURCE CH06_DARIM L160 [CONDITION] ch04_partner == "darim"
    if story_id(ch04_partner) == "darim":
        # SOURCE CH06_DARIM L162 다림
        darim "지난번에 일 말고 같이 놀자고 했던 약속, 기억하세요?"
        # SOURCE CH06_DARIM L164 주인공
        mc "네. 오늘 조금 지킨 것 같은데요?"
        # SOURCE CH06_DARIM L166 다림
        darim "후후. 그러네요."
        # SOURCE CH06_DARIM L167 다림
        darim "그런데 다음에는 조금 더 길게 놀고 싶어요."
    # SOURCE CH06_DARIM L170 다림
    darim "다음에 시간 되면 게임 카페도 같이 가실래요?"
    # SOURCE CH06_DARIM L172 주인공
    mc "좋아요."
    # SOURCE CH06_DARIM L174 다림
    # COMMON STANDING BEGIN CH06_DARIM L174
    $ story_stage(faces={"darim": "smug"})
    # COMMON STANDING END CH06_DARIM L174
    darim "이번에는 협동 말고 대결 게임도 해봐요."
    # SOURCE CH06_DARIM L176 주인공
    mc "선배, 결국 승부가 하고 싶으신 거죠?"
    # SOURCE CH06_DARIM L178 다림
    darim "……들켰네요."
    # SOURCE CH06_DARIM L180
    narrator "선배는 장난스럽게 웃었다."
    # SOURCE CH06_DARIM L181
    narrator "나도 웃었다."
    # SOURCE CH06_DARIM L182
    narrator "이 사람과는 앞으로도 이런 시간이 많았으면 좋겠다."
    jump ch06_sc04_darim_03

label ch06_sc04_darim_03:
    $ phone_timeline_enter("CH06", "ch06_sc04_darim_03")
    # SOURCE CH06_DARIM L183 다시 축제 현장으로
    # SOURCE CH06_DARIM L184 [BG] 축제 광장 · 오후
    $ story_draft_scene("축제 광장 · 오후", cast=["darim"], standing=True)
    # COMMON STANDING BEGIN CH06_DARIM L184
    $ story_stage_fade_in(["darim"])
    # COMMON STANDING END CH06_DARIM L184
    # SOURCE CH06_DARIM L185 [BGM] Festival Afternoon
    $ story_draft_bgm("Festival Afternoon")
    # SOURCE CH06_DARIM L187
    narrator "카페를 나와 다시 축제 광장으로 향했다."
    # SOURCE CH06_DARIM L188
    narrator "오후가 되자 사람들은 오전보다 더 많아져 있었다."
    # SOURCE CH06_DARIM L189
    narrator "멀리서 우리가 만든 부스가 보였다."
    # SOURCE CH06_DARIM L191 다림
    # COMMON STANDING BEGIN CH06_DARIM L191
    $ story_stage(faces={"darim": "happy"})
    # COMMON STANDING END CH06_DARIM L191
    darim "이제 돌아가야겠네요."
    # SOURCE CH06_DARIM L193 주인공
    mc "그러게요. 쉬는 시간이 금방 지나갔어요."
    # SOURCE CH06_DARIM L195 다림
    darim "후후. 재미있는 시간은 원래 빨리 가잖아요."
    # SOURCE CH06_DARIM L197 주인공
    mc "다음에는 조금 더 길게 놀아요."
    # SOURCE CH06_DARIM L199 다림
    darim "……."
    # SOURCE CH06_DARIM L201 다림
    darim "네. 저도 그러고 싶어요."
    # SOURCE CH06_DARIM L203
    narrator "다림 선배는 작은 고양이 스티커를 가방에 조심스럽게 넣었다."
    # SOURCE CH06_DARIM L205 다림
    darim "그럼 오늘 남은 시간도 같이 힘내봐요."
    # SOURCE CH06_DARIM L207 주인공
    mc "네, 선배."
    # SOURCE CH06_DARIM L209
    narrator "우리는 다시 부스로 걸어갔다."
    # SOURCE CH06_DARIM L210
    narrator "축제가 끝나도, 함께할 시간이 더 있었으면 좋겠다."
    # SOURCE CH06_DARIM L211 [FLAG] ch06_darim_festival_event = True
    $ story_flag("ch06_darim_festival_event", True)
    # SOURCE CH06_DARIM L212 [FLAG] ch06_special_memory = "darim_game"
    $ story_flag("ch06_special_memory", 'darim_game')
    # CONTI SOURCE CH06_DARIM L213 [RETURN] CH06 SC05 「마지막까지 사고라고?」
    jump ch06_sc05

label ch06_sc04_roman:
    $ phone_timeline_enter("CH06", "ch06_sc04_roman")
    # SOURCE CH06 L903 로만: 우리만 아는 책갈피
    # SOURCE CH06 L905 [BG] 축제 문학 행사장 입구
    $ story_draft_scene("축제 문학 행사장 입구", cast=["roman"], standing=True)
    # COMMON STANDING BEGIN CH06 L905
    $ story_stage_fade_in(["roman"])
    # COMMON STANDING END CH06 L905
    # SOURCE CH06 L907 [BGM] Gentle Festival
    $ story_draft_bgm("Gentle Festival")
    # CONTI SOURCE CH06 L909 [ANIM] 로만 기본 LD · 자연스러운 눈 깜빡임
    # SOURCE CH06 L913
    narrator "로만과 약속한 장소에 도착했다."
    # SOURCE CH06 L915
    narrator "행사장 입구에는 작은 책과 손글씨 엽서들이 전시되어 있었다."
    # SOURCE CH06 L917
    narrator "멀리서 로만이 나를 발견하고 손을 흔들었다."
    # SOURCE CH06 L920 로만
    # COMMON STANDING BEGIN CH06 L920
    $ story_stage(faces={"roman": "happy"})
    # COMMON STANDING END CH06 L920
    # CH06 VISUAL 066 BEGIN roman-01-start
    $ cg_start("ch06_festival_roman_01", transition=0.35)
    # CH06 VISUAL 066 END roman-01-start
    roman "앗,,, [player_name] 씨!"
    # SOURCE CH06 L923 주인공
    mc "많이 기다리셨어요?"
    # SOURCE CH06 L926 로만
    roman "아니에요……! 저도 방금 왔어요."
    # SOURCE CH06 L930
    narrator "로만은 평소보다 조금 들떠 보였다."
    # SOURCE CH06 L933 주인공
    mc "여기 분위기가 좋네요."
    # SOURCE CH06 L936 로만
    roman "네……!"
    # SOURCE CH06 L938 로만
    roman "책갈피도 직접 만들 수 있대요."
    # SOURCE CH06 L941 주인공
    mc "그럼 같이 만들어볼까요?"
    # SOURCE CH06 L944 로만
    roman "앗,,, 좋아요."
    # CH06 VISUAL 066 BEGIN roman-01-end
    $ cg_end(transition=0.35)
    # CH06 VISUAL 066 END roman-01-end
    # SOURCE CH06 L946 [BG] 문학 행사 체험 테이블
    $ story_draft_scene("문학 행사 체험 테이블", cast=["roman"], standing=True)
    # COMMON STANDING BEGIN CH06 L946
    $ story_stage_fade_in(["roman"])
    # COMMON STANDING END CH06 L946
    # SOURCE CH06 L950
    narrator "테이블 위에는 종이와 색연필, 리본 끈이 놓여 있었다."
    # SOURCE CH06 L952
    narrator "참가자는 원하는 문장을 적고 책갈피를 꾸밀 수 있었다."
    # SOURCE CH06 L954
    narrator "로만은 종이를 한 장 집어 들었다."
    # SOURCE CH06 L957 로만
    roman "음……."
    # SOURCE CH06 L960 주인공
    mc "무슨 문장 쓰실 거예요?"
    # SOURCE CH06 L963 로만
    roman "아직 고민 중이에요."
    # SOURCE CH06 L965 로만
    roman "좋아하는 문장이 너무 많아서……."
    # SOURCE CH06 L968 주인공
    mc "그럼 직접 쓰신 문장은 어때요?"
    # SOURCE CH06 L971 로만
    # COMMON STANDING BEGIN CH06 L971
    $ story_stage(faces={"roman": "surprised"})
    # COMMON STANDING END CH06 L971
    roman "……!"
    # SOURCE CH06 L973 로만
    roman "제 문장이요?"
    # SOURCE CH06 L976 주인공
    mc "네. 로만 씨가 쓰신 문장도 좋잖아요."
    # SOURCE CH06 L979 로만
    roman "……."
    # SOURCE CH06 L982 로만
    # COMMON STANDING BEGIN CH06 L982
    $ story_stage(faces={"roman": "embarrassed"})
    # COMMON STANDING END CH06 L982
    roman "그렇게 말씀해주시면 조금 부끄러운데요……."
    # SOURCE CH06 L986
    narrator "로만은 종이를 내려다봤다."
    # SOURCE CH06 L988
    narrator "잠시 고민하더니 조심스럽게 펜을 움직였다."
    # SOURCE CH06 L990
    narrator "나는 내 책갈피를 만들기 시작했다."
    # SOURCE CH06 L993 주인공
    mc "이런 건 처음 만들어보네요."
    # SOURCE CH06 L996 로만
    # COMMON STANDING BEGIN CH06 L996
    $ story_stage(faces={"roman": "happy"})
    # COMMON STANDING END CH06 L996
    roman "후후…… 저도 직접 만드는 건 오랜만이에요."
    # SOURCE CH06 L999 주인공
    mc "어렸을 때도 만들어보셨어요?"
    # SOURCE CH06 L1002 로만
    roman "네. 책 읽는 걸 좋아해서요."
    # SOURCE CH06 L1004 로만
    roman "그런데 예쁘게 만드는 건 잘 못했어요."
    # SOURCE CH06 L1007 주인공
    mc "지금은 잘하시는데요?"
    # SOURCE CH06 L1010 로만
    roman "……그, 그런가요?"
    # SOURCE CH06 L1014
    narrator "로만은 자신의 책갈피를 다시 바라봤다."
    # SOURCE CH06 L1016
    narrator "그리고 조금 자신 있는 표정으로 웃었다."
    # CONTI SOURCE CH06 L1018 [시간 경과 · 오후 1:55]
    $ phone_timeline_cue("CH06", "CH06_L1018")
    # SOURCE CH06 L1020 [BG] 문학 행사장 · 낭독 공간
    $ story_draft_scene("문학 행사장 · 낭독 공간", cast=["roman"], standing=True)
    # COMMON STANDING BEGIN CH06 L1020
    $ story_stage_fade_in(["roman"])
    # COMMON STANDING END CH06 L1020
    # SOURCE CH06 L1024
    narrator "작은 낭독 행사가 시작됐다."
    # SOURCE CH06 L1026
    narrator "학생 몇 명이 자신이 고른 글을 읽었고, 관객들은 조용히 귀를 기울였다."
    # SOURCE CH06 L1028
    narrator "로만은 무릎 위에 손을 모으고 앉아 있었다."
    # SOURCE CH06 L1031 주인공 · 작은 목소리
    mc "재미있으세요?"
    # SOURCE CH06 L1034 로만
    roman "네……."
    # SOURCE CH06 L1036 로만
    # COMMON STANDING BEGIN CH06 L1036
    $ story_stage(faces={"roman": "embarrassed"})
    # COMMON STANDING END CH06 L1036
    roman "그런데 조금 떨려요."
    # SOURCE CH06 L1039 주인공
    mc "로만 씨가 발표하시는 것도 아닌데요?"
    # SOURCE CH06 L1042 로만
    roman "그렇긴 한데……."
    # SOURCE CH06 L1044 로만
    roman "저도 저렇게 읽을 수 있을까 생각하니까요."
    # SOURCE CH06 L1048
    narrator "로만은 무대에서 시선을 떼지 않았다."
    # SOURCE CH06 L1051 주인공
    mc "해보고 싶으세요?"
    # SOURCE CH06 L1054 로만
    # COMMON STANDING BEGIN CH06 L1054
    $ story_stage(faces={"roman": "serious"})
    # COMMON STANDING END CH06 L1054
    roman "……언젠가는요."
    # SOURCE CH06 L1056 로만
    roman "제가 직접 쓴 글을 사람들 앞에서 읽어보고 싶어요."
    # SOURCE CH06 L1059 주인공
    mc "그럼 언젠가 듣고 싶네요."
    # SOURCE CH06 L1062 로만
    roman "……."
    # SOURCE CH06 L1064 로만
    roman "그렇게 말씀하시니까……."
    # SOURCE CH06 L1066 로만
    # COMMON STANDING BEGIN CH06 L1066
    $ story_stage(faces={"roman": "happy"})
    # COMMON STANDING END CH06 L1066
    roman "조금 더 해보고 싶어져요."
    # SOURCE CH06 L1070
    narrator "로만은 수줍게 웃었다."
    # SOURCE CH06 L1072
    narrator "그 모습이 왠지 오래 기억에 남을 것 같았다."
    # CONTI SOURCE CH06 L1074 [시간 경과 · 오후 2:20]
    $ phone_timeline_cue("CH06", "CH06_L1074")
    # SOURCE CH06 L1076 [BG] 행사장 밖 벤치
    $ story_draft_scene("행사장 밖 벤치", cast=["roman"], standing=True)
    # COMMON STANDING BEGIN CH06 L1076
    $ story_stage_fade_in(["roman"])
    # COMMON STANDING END CH06 L1076
    # SOURCE CH06 L1080
    narrator "행사를 모두 구경한 뒤 우리는 벤치에 앉았다."
    # SOURCE CH06 L1082
    narrator "로만은 작은 종이 봉투를 꺼냈다."
    # SOURCE CH06 L1085 로만
    roman "저기……."
    # SOURCE CH06 L1088 주인공
    mc "네?"
    # SOURCE CH06 L1091 로만
    roman "아까 만든 책갈피 있잖아요."
    # SOURCE CH06 L1094 주인공
    mc "네."
    # SOURCE CH06 L1097 로만
    roman "……이거."
    # SOURCE CH06 L1101
    # CH06 VISUAL 066 BEGIN roman-02-start
    $ cg_start("ch06_festival_roman_02", transition=0.35)
    # CH06 VISUAL 066 END roman-02-start
    narrator "로만이 종이 봉투를 내밀었다."
    # SOURCE CH06 L1103
    narrator "안에는 크림색 종이에 작은 파란 꽃이 그려진 책갈피가 들어 있었다."
    # SOURCE CH06 L1105
    narrator "뒷면에는 손글씨로 짧은 문장이 적혀 있었다."
    # SOURCE CH06 L1107
    narrator "「함께 읽고 싶은 이야기가 생겼어요.」"
    # SOURCE CH06 L1110 주인공
    mc "……이거 저 주시는 거예요?"
    # SOURCE CH06 L1113 로만
    # COMMON STANDING BEGIN CH06 L1113
    $ story_stage(faces={"roman": "embarrassed"})
    # COMMON STANDING END CH06 L1113
    roman "앗,,, 네……."
    # SOURCE CH06 L1115 로만
    roman "오늘 같이 와주셔서 고마워서요."
    # SOURCE CH06 L1118 주인공
    mc "정말 예뻐요. 감사해요."
    # SOURCE CH06 L1121 로만
    # COMMON STANDING BEGIN CH06 L1121
    $ story_stage(faces={"roman": "happy"})
    # COMMON STANDING END CH06 L1121
    roman "……후후."
    # SOURCE CH06 L1125
    narrator "로만은 안심한 듯 웃었다."
    # SOURCE CH06 L1127
    narrator "그러다 작은 목소리로 덧붙였다."
    # SOURCE CH06 L1130 로만
    roman "사실……."
    # SOURCE CH06 L1132 로만
    # COMMON STANDING BEGIN CH06 L1132
    $ story_stage(faces={"roman": "embarrassed"})
    # COMMON STANDING END CH06 L1132
    roman "다른 사람한테는 안 준 거예요."
    # SOURCE CH06 L1135 주인공
    mc "……저한테만요?"
    # SOURCE CH06 L1138 로만
    roman "……네."
    # CONTI SOURCE CH06 L1140 [ANIM] 로만이 눈을 깜빡인 뒤 시선을 아래로 내리는 표정 전환
    # SOURCE CH06 L1144
    narrator "로만은 책갈피 끝을 손가락으로 만지작거렸다."
    # SOURCE CH06 L1147 로만
    roman "그러니까……."
    # SOURCE CH06 L1149 로만
    roman "소중히 해주시면 좋겠어요."
    # SOURCE CH06 L1152 주인공
    mc "그럴게요."
    # SOURCE CH06 L1156
    narrator "나는 책갈피를 조심스럽게 봉투에 넣었다."
    # SOURCE CH06 L1158
    narrator "그냥 작은 종이 한 장이었다."
    # SOURCE CH06 L1160
    narrator "그런데 왠지 아무 데나 넣어두고 싶지는 않았다."
    # SOURCE CH06 L1162 [CONDITION] `ch04_partner == "roman"`
    if story_id(ch04_partner) == "roman":
        # SOURCE CH06 L1165 주인공
        mc "전에 보여주시기로 한 글도 아직 기다리고 있어요."
        # SOURCE CH06 L1168 로만
        roman "앗,,, 기억하고 계셨네요."
        # SOURCE CH06 L1171 주인공
        mc "네. 로만 씨가 직접 보여주고 싶으실 때까지요."
        # SOURCE CH06 L1174 로만
        roman "……."
        # SOURCE CH06 L1177 로만
        roman "그럼 오늘 책갈피는 먼저 드리는 선물이에요."
    # SOURCE CH06 L1182 로만
    roman "다음에는……."
    # SOURCE CH06 L1184 로만
    roman "축제처럼 특별한 날이 아니어도 같이 책 읽으러 가실래요?"
    # SOURCE CH06 L1187 주인공
    mc "좋아요. 저도 그러고 싶어요."
    # SOURCE CH06 L1190 로만
    # COMMON STANDING BEGIN CH06 L1190
    $ story_stage(faces={"roman": "happy"})
    # COMMON STANDING END CH06 L1190
    roman "……후후."
    # SOURCE CH06 L1192 로만
    roman "그럼 약속이에요."
    # CH06 VISUAL 066 BEGIN roman-02-end
    $ cg_end(transition=0.35)
    # CH06 VISUAL 066 END roman-02-end
    # SOURCE CH06 L1196
    narrator "로만과 함께 행사장을 나섰다."
    # SOURCE CH06 L1198
    narrator "돌아가는 길에도 로만은 평소보다 말을 많이 했다."
    # SOURCE CH06 L1200
    narrator "읽고 싶은 책 이야기."
    # SOURCE CH06 L1202
    narrator "최근에 쓴 문장 이야기."
    # SOURCE CH06 L1204
    narrator "그리고 다음에 함께 가고 싶은 도서관 이야기까지."
    # SOURCE CH06 L1206
    narrator "오늘은 로만을 조금 더 알게 된 것 같았다."
    # SOURCE CH06 L1208 [FLAG] `ch06_roman_festival_event = True`
    $ story_flag("ch06_roman_festival_event", True)
    # SOURCE CH06 L1210 [FLAG] `ch06_special_memory = roman_bookmark`
    $ story_flag("ch06_special_memory", 'roman_bookmark')
    # CONTI SOURCE CH06 L1212 [RETURN TO SC05]
    jump ch06_sc05

label ch06_sc04_sia:
    $ phone_timeline_enter("CH06", "ch06_sc04_sia")
    # SOURCE CH06 L1214 시아: 오늘만큼은 장난 금지
    # SOURCE CH06 L1216 [BG] 애니메이션학과 작품 전시관 · 오후
    $ story_draft_scene("애니메이션학과 작품 전시관 · 오후", cast=["sia"], standing=True)
    # COMMON STANDING BEGIN CH06 L1216
    $ story_stage_fade_in(["sia"])
    # COMMON STANDING END CH06 L1216
    # SOURCE CH06 L1218 [BGM] Playful Afternoon
    $ story_draft_bgm("Playful Afternoon")
    # CONTI SOURCE CH06 L1220 [ANIM] 시아 기본 LD · 가벼운 눈 깜빡임
    # SOURCE CH06 L1224
    narrator "전시관 입구부터 그림이 가득했다."
    # SOURCE CH06 L1226
    narrator "벽에는 학생들이 그린 일러스트와 짧은 만화가 걸려 있었고, 한쪽 화면에서는 애니메이션이 반복 재생되고 있었다."
    # SOURCE CH06 L1228
    narrator "시아는 입구에서 나를 발견하자 손을 번쩍 들었다."
    # SOURCE CH06 L1231 시아
    # COMMON STANDING BEGIN CH06 L1231
    $ story_stage(faces={"sia": "happy"})
    # COMMON STANDING END CH06 L1231
    # CH06 VISUAL 066 BEGIN sia-01-start
    $ cg_start("ch06_festival_sia_01", transition=0.35)
    # CH06 VISUAL 066 END sia-01-start
    sia "야! 여기!"
    # SOURCE CH06 L1234 주인공
    mc "오래 기다리셨어요?"
    # SOURCE CH06 L1237 시아
    sia "아니. 나도 방금 왔어."
    # SOURCE CH06 L1239 시아
    # COMMON STANDING BEGIN CH06 L1239
    $ story_stage(faces={"sia": "smug"})
    # COMMON STANDING END CH06 L1239
    sia "자, 오늘은 특별히 천재 작가님이 직접 안내해주지."
    # SOURCE CH06 L1242 주인공
    mc "입장료는 얼마인가요?"
    # SOURCE CH06 L1245 시아
    sia "너는 특별 할인."
    # SOURCE CH06 L1248 주인공
    mc "얼마나 할인해 주시는데요?"
    # SOURCE CH06 L1251 시아
    sia "0원."
    # SOURCE CH06 L1254 주인공
    mc "원래 무료 전시 아닌가요?"
    # SOURCE CH06 L1257 시아
    sia "……."
    # SOURCE CH06 L1259 시아
    # COMMON STANDING BEGIN CH06 L1259
    $ story_stage(faces={"sia": "confused"})
    # COMMON STANDING END CH06 L1259
    sia "그런 세세한 건 넘어가."
    # CH06 VISUAL 066 BEGIN sia-01-end
    $ cg_end(transition=0.35)
    # CH06 VISUAL 066 END sia-01-end
    # SOURCE CH06 L1263
    narrator "시아는 웃으면서 나를 전시관 안으로 데려갔다."
    # SOURCE CH06 L1265
    narrator "벽마다 서로 다른 그림체와 이야기가 걸려 있었다."
    # SOURCE CH06 L1268 주인공
    mc "와…… 생각보다 작품이 많네요."
    # SOURCE CH06 L1271 시아
    sia "그치? 다들 축제 때문에 고생 좀 했거든."
    # SOURCE CH06 L1274 주인공
    mc "시아 씨 작품은 어디 있어요?"
    # SOURCE CH06 L1277 시아
    # COMMON STANDING BEGIN CH06 L1277
    $ story_stage(faces={"sia": "smug"})
    # COMMON STANDING END CH06 L1277
    sia "어이구. 그렇게 보고 싶었냐?"
    # SOURCE CH06 L1280 주인공
    mc "네. 기대하고 왔으니까요."
    # SOURCE CH06 L1283 시아
    sia "……."
    # SOURCE CH06 L1285 시아
    # COMMON STANDING BEGIN CH06 L1285
    $ story_stage(faces={"sia": "embarrassed"})
    # COMMON STANDING END CH06 L1285
    sia "그렇게 바로 대답하지 마."
    # SOURCE CH06 L1288 주인공
    mc "왜요?"
    # SOURCE CH06 L1291 시아
    sia "……나 긴장되잖아."
    # SOURCE CH06 L1293 [BG] 시아 작품 전시 구역
    $ story_draft_scene("시아 작품 전시 구역", cast=["sia"], standing=True)
    # COMMON STANDING BEGIN CH06 L1293
    $ story_stage_fade_in(["sia"])
    # COMMON STANDING END CH06 L1293
    # SOURCE CH06 L1297
    narrator "시아는 자신의 작품 앞에서 걸음을 멈췄다."
    # SOURCE CH06 L1299
    narrator "제목은 「우당탕탕, 둘이서」."
    # SOURCE CH06 L1301
    narrator "성격이 전혀 다른 두 캐릭터가 함께 사건을 해결하는 짧은 만화였다."
    # SOURCE CH06 L1303
    narrator "한 명은 무조건 앞으로 달려가고, 다른 한 명은 뒤에서 계획을 세우는 타입이었다."
    # SOURCE CH06 L1306 주인공
    mc "……두 사람이 많이 다르네요."
    # SOURCE CH06 L1309 시아
    # COMMON STANDING BEGIN CH06 L1309
    $ story_stage(faces={"sia": "happy"})
    # COMMON STANDING END CH06 L1309
    sia "응. 그래서 재미있잖아."
    # SOURCE CH06 L1312 주인공
    mc "그런데 계속 싸우면서도 서로 도와주네요."
    # SOURCE CH06 L1315 시아
    sia "그치?"
    # SOURCE CH06 L1317 시아
    sia "맨날 똑같은 생각만 하는 사람끼리 있으면 재미없거든."
    # SOURCE CH06 L1320 주인공
    mc "마지막 장면이 좋네요."
    # SOURCE CH06 L1323 시아
    sia "어떤 거?"
    # SOURCE CH06 L1326 주인공
    mc "한 명이 넘어졌을 때 다른 한 명이 잡아주는 장면이요."
    # SOURCE CH06 L1329 시아
    sia "……."
    # SOURCE CH06 L1331 시아
    sia "그거 좋았어?"
    # SOURCE CH06 L1334 주인공
    mc "네. 앞에서는 서로 놀리기만 했는데, 진짜 필요할 때는 망설이지 않잖아요."
    # SOURCE CH06 L1338
    narrator "시아는 잠시 작품을 바라봤다."
    # SOURCE CH06 L1341 시아
    # COMMON STANDING BEGIN CH06 L1341
    $ story_stage(faces={"sia": "serious"})
    # COMMON STANDING END CH06 L1341
    sia "……맞아."
    # SOURCE CH06 L1343 시아
    sia "사실 그 장면 제일 오래 그렸어."
    # SOURCE CH06 L1346 주인공
    mc "정말요?"
    # SOURCE CH06 L1349 시아
    sia "응."
    # SOURCE CH06 L1351 시아
    sia "앞부분은 금방 나왔는데, 마지막에서 좀 막혔거든."
    # SOURCE CH06 L1354 시아
    sia "둘이 진짜 친하다는 걸 대사 없이 보여주고 싶어서."
    # SOURCE CH06 L1357 주인공
    mc "잘 표현된 것 같아요."
    # SOURCE CH06 L1360 시아
    sia "……."
    # CONTI SOURCE CH06 L1362 [ANIM] 시아의 미소가 작아지고, 한 차례 눈을 깜빡이는 표정 전환
    # SOURCE CH06 L1365 시아
    # COMMON STANDING BEGIN CH06 L1365
    $ story_stage(faces={"sia": "embarrassed"})
    # COMMON STANDING END CH06 L1365
    sia "……고맙다."
    # SOURCE CH06 L1369
    narrator "시아는 짧게 대답했다."
    # SOURCE CH06 L1371
    narrator "평소 같으면 '역시 내가 천재지' 같은 말을 덧붙였을 텐데."
    # SOURCE CH06 L1373
    narrator "이번에는 그러지 않았다."
    # CONTI SOURCE CH06 L1375 [시간 경과 · 오후 2:05]
    $ phone_timeline_cue("CH06", "CH06_L1375")
    # SOURCE CH06 L1377 [BG] 전시관 휴식 구역
    $ story_draft_scene("전시관 휴식 구역", cast=["sia"], standing=True)
    # COMMON STANDING BEGIN CH06 L1377
    $ story_stage_fade_in(["sia"])
    # COMMON STANDING END CH06 L1377
    # SOURCE CH06 L1381
    narrator "작품을 모두 둘러본 뒤 시아와 음료를 마시며 쉬었다."
    # SOURCE CH06 L1384 시아
    sia "야, 근데."
    # SOURCE CH06 L1387 주인공
    mc "네?"
    # SOURCE CH06 L1390 시아
    # COMMON STANDING BEGIN CH06 L1390
    $ story_stage(faces={"sia": "serious"})
    # COMMON STANDING END CH06 L1390
    sia "너 내 그림 진짜 좋아하냐?"
    # SOURCE CH06 L1393 주인공
    mc "네."
    # SOURCE CH06 L1396 시아
    # CH06 VISUAL 066 BEGIN sia-02-start
    $ cg_start("ch06_festival_sia_02", transition=0.35)
    # CH06 VISUAL 066 END sia-02-start
    sia "……그냥 나 기분 좋으라고 하는 말 아니고?"
    # SOURCE CH06 L1399 주인공
    mc "그랬으면 아까 그 장면이 왜 좋았는지도 말씀드리지 않았겠죠."
    # SOURCE CH06 L1402 시아
    sia "……."
    # SOURCE CH06 L1405 시아
    sia "와."
    # SOURCE CH06 L1407 시아
    sia "너 진짜 이상한 데서 논리적이다."
    # SOURCE CH06 L1410 주인공
    mc "감상 담당이니까요."
    # SOURCE CH06 L1413 시아
    # COMMON STANDING BEGIN CH06 L1413
    $ story_stage(faces={"sia": "happy"})
    # COMMON STANDING END CH06 L1413
    sia "아, 그거 아직도 기억하냐ㅋㅋ"
    # SOURCE CH06 L1416 주인공
    mc "시아 씨가 임명하셨잖아요."
    # SOURCE CH06 L1419 시아
    sia "그렇지."
    # SOURCE CH06 L1423
    narrator "시아는 음료 컵을 손가락으로 톡톡 두드렸다."
    # SOURCE CH06 L1426 시아
    # COMMON STANDING BEGIN CH06 L1426
    $ story_stage(faces={"sia": "serious"})
    # COMMON STANDING END CH06 L1426
    sia "사실 처음에는 좀 걱정했어."
    # SOURCE CH06 L1429 주인공
    mc "어떤 게요?"
    # SOURCE CH06 L1432 시아
    sia "네가 내 만화 보고 재미없다고 하면 어떡하지 싶어서."
    # SOURCE CH06 L1435 주인공
    mc "시아 씨도 그런 걱정을 하세요?"
    # SOURCE CH06 L1438 시아
    sia "야, 나도 사람이라니까."
    # SOURCE CH06 L1441 주인공
    mc "알아요."
    # SOURCE CH06 L1444 시아
    sia "……."
    # SOURCE CH06 L1447 시아
    sia "그런데 너는 신기해."
    # SOURCE CH06 L1450 주인공
    mc "뭐가요?"
    # SOURCE CH06 L1453 시아
    sia "내가 장난치면 받아주고."
    # SOURCE CH06 L1455 시아
    sia "진지하게 말하면 그것도 들어주잖아."
    # SOURCE CH06 L1459
    narrator "시아는 잠시 나를 바라봤다."
    # SOURCE CH06 L1462 시아
    sia "그래서 좀 편해."
    # SOURCE CH06 L1465 주인공
    mc "저도 시아 씨랑 있으면 재미있고 편해요."
    # SOURCE CH06 L1468 시아
    sia "……."
    # SOURCE CH06 L1470 시아
    # COMMON STANDING BEGIN CH06 L1470
    $ story_stage(faces={"sia": "embarrassed"})
    # COMMON STANDING END CH06 L1470
    sia "야, 그건 좀 반칙인데."
    # SOURCE CH06 L1473 주인공
    mc "뭐가요?"
    # SOURCE CH06 L1476 시아
    sia "그냥."
    # SOURCE CH06 L1478 시아
    sia "내가 먼저 멋있는 말 하려고 했거든."
    # SOURCE CH06 L1482
    narrator "시아는 결국 웃음을 터뜨렸다."
    # CH06 VISUAL 066 BEGIN sia-02-end
    $ cg_end(transition=0.35)
    # CH06 VISUAL 066 END sia-02-end
    # SOURCE CH06 L1484 [CONDITION] `ch04_partner == "sia"`
    if story_id(ch04_partner) == "sia":
        # SOURCE CH06 L1487 시아
        sia "아, 그리고 개인 웹툰은 약속대로 나중에 보여줄게."
        # SOURCE CH06 L1490 주인공
        mc "네. 그건 오늘 작품보다 더 기대되는데요?"
        # SOURCE CH06 L1493 시아
        sia "야, 부담 주지 마ㅋㅋ"
        # SOURCE CH06 L1496 시아
        sia "……근데 첫 번째로 보여주고 싶은 건 진짜야."
    # SOURCE CH06 L1501 시아
    sia "축제 끝나도 가끔 내 작품 보러 와라."
    # SOURCE CH06 L1504 주인공
    mc "작품 보러만 가도 되나요?"
    # SOURCE CH06 L1507 시아
    sia "어?"
    # SOURCE CH06 L1510 주인공
    mc "그냥 시아 씨랑 이야기하러 가도 되잖아요."
    # SOURCE CH06 L1513 시아
    sia "……."
    # SOURCE CH06 L1516 시아
    sia "야."
    # SOURCE CH06 L1518 시아
    sia "그건 당연하지."
    # SOURCE CH06 L1522
    narrator "시아는 이번에도 웃었다."
    # SOURCE CH06 L1524
    narrator "그런데 조금 전보다 더 기분 좋아 보였다."
    # SOURCE CH06 L1527 시아
    # COMMON STANDING BEGIN CH06 L1527
    $ story_stage(faces={"sia": "happy"})
    # COMMON STANDING END CH06 L1527
    sia "너 진짜 내 감상 담당 계속해라."
    # SOURCE CH06 L1530 주인공
    mc "그럼 다음 작품도 기대할게요."
    # SOURCE CH06 L1533 시아
    sia "당연하지."
    # SOURCE CH06 L1535 시아
    sia "이번보다 더 재미있을 거야."
    # SOURCE CH06 L1537 [FLAG] `ch06_sia_festival_event = True`
    $ story_flag("ch06_sia_festival_event", True)
    # SOURCE CH06 L1539 [FLAG] `ch06_special_memory = sia_exhibition`
    $ story_flag("ch06_special_memory", 'sia_exhibition')
    # CONTI SOURCE CH06 L1541 [RETURN TO SC05]
    jump ch06_sc05

label ch06_sc04_omu:
    $ phone_timeline_enter("CH06", "ch06_sc04_omu")
    # SOURCE CH06 L1872 오므: 이번엔 같이 찍자
    # SOURCE CH06 L1874 [BG] 축제 광장 · 오후
    $ story_draft_scene("축제 광장 · 오후", cast=["omu"], standing=True)
    # COMMON STANDING BEGIN CH06 L1874
    $ story_stage_fade_in(["omu"])
    # COMMON STANDING END CH06 L1874
    # SOURCE CH06 L1876 [BGM] Soft Photography
    $ story_draft_bgm("Soft Photography")
    # CONTI SOURCE CH06 L1878 [ANIM] 오므 기본 LD · 눈 깜빡임, 머리카락의 약한 움직임
    # SOURCE CH06 L1882
    narrator "오므와 약속한 장소에 도착했다."
    # SOURCE CH06 L1884
    narrator "광장 한쪽에서 오므가 카메라를 들고 있었다."
    # CH06 VISUAL 066 BEGIN omu-01-start
    $ cg_start("ch06_festival_omu_01", transition=0.35)
    # CH06 VISUAL 066 END omu-01-start
    # SOURCE CH06 L1887 주인공
    mc "오므 씨!"
    # SOURCE CH06 L1890 오므
    # COMMON STANDING BEGIN CH06 L1890
    $ story_stage(faces={"omu": "happy"})
    # COMMON STANDING END CH06 L1890
    omu "어. 왔나?"
    # SOURCE CH06 L1893 주인공
    mc "네. 사진 많이 찍으셨어요?"
    # SOURCE CH06 L1896 오므
    omu "아직. 니 기다리고 있었다."
    # SOURCE CH06 L1899 주인공
    mc "그럼 같이 돌아볼까요?"
    # SOURCE CH06 L1902 오므
    omu "좋지."
    # SOURCE CH06 L1906
    narrator "오므는 카메라 끈을 고쳐 멨다."
    # SOURCE CH06 L1908
    # CH06 VISUAL 066 BEGIN omu-01-end
    $ cg_end(transition=0.35)
    # CH06 VISUAL 066 END omu-01-end
    narrator "우리는 축제 광장을 천천히 걸었다."
    # SOURCE CH06 L1911 오므
    omu "야, 저기 봐라."
    # SOURCE CH06 L1914 주인공
    mc "어디요?"
    # SOURCE CH06 L1917 오므
    omu "저쪽 현수막이랑 그림자 겹치는 거."
    # SOURCE CH06 L1921
    narrator "오므가 가리킨 곳에는 나무 그림자가 길게 드리워져 있었다."
    # SOURCE CH06 L1923
    narrator "평소라면 아무 생각 없이 지나쳤을 풍경이었다."
    # SOURCE CH06 L1926 주인공
    mc "오…… 이렇게 보니까 예쁘네요."
    # SOURCE CH06 L1929 오므
    omu "그렇지?"
    # CONTI SOURCE CH06 L1931 [SFX] 카메라 셔터
    # SOURCE CH06 L1934 오므
    omu "이렇게 빛이 들어올 때가 좋다."
    # SOURCE CH06 L1937 주인공
    mc "오므 씨는 정말 이런 걸 잘 찾으시네요."
    # SOURCE CH06 L1940 오므
    omu "뭐, 계속 보다 보면 보인다."
    # SOURCE CH06 L1944
    narrator "오므는 별것 아니라는 듯 말했다."
    # SOURCE CH06 L1946
    narrator "하지만 나는 오므가 어떤 풍경을 좋아하는지 조금씩 알아가고 있었다."
    # CONTI SOURCE CH06 L1948 [시간 경과 · 오후 2:05]
    $ phone_timeline_cue("CH06", "CH06_L1948")
    # SOURCE CH06 L1950 [BG] 축제 장식 거리
    $ story_draft_scene("축제 장식 거리", cast=["omu"], standing=True)
    # COMMON STANDING BEGIN CH06 L1950
    $ story_stage_fade_in(["omu"])
    # COMMON STANDING END CH06 L1950
    # SOURCE CH06 L1954
    narrator "우리는 작은 소품 부스를 구경했다."
    # SOURCE CH06 L1956
    narrator "오므는 오래된 필름 카메라 모양 열쇠고리를 한참 바라봤다."
    # SOURCE CH06 L1959 주인공
    mc "마음에 드세요?"
    # SOURCE CH06 L1962 오므
    # COMMON STANDING BEGIN CH06 L1962
    $ story_stage(faces={"omu": "happy"})
    # COMMON STANDING END CH06 L1962
    omu "어. 좀 귀엽네."
    # SOURCE CH06 L1965 주인공
    mc "그럼 하나 사실래요?"
    # SOURCE CH06 L1968 오므
    omu "아니. 그냥 구경하는 거다."
    # SOURCE CH06 L1972
    narrator "잠시 뒤 오므가 웃었다."
    # SOURCE CH06 L1975 오므
    omu "야, 니는 사진 찍히는 거 별로 안 좋아하나?"
    # SOURCE CH06 L1978 주인공
    mc "왜요?"
    # SOURCE CH06 L1981 오므
    # COMMON STANDING BEGIN CH06 L1981
    $ story_stage(faces={"omu": "normal"})
    # COMMON STANDING END CH06 L1981
    omu "내는 니랑 같이 다니면서 사진은 많이 찍었는데."
    # SOURCE CH06 L1983 오므
    omu "정작 같이 찍은 사진은 별로 없잖아."
    # SOURCE CH06 L1986 주인공
    mc "그러네요."
    # SOURCE CH06 L1989 오므
    omu "그럼 오늘은 하나 남기자."
    # SOURCE CH06 L1992 주인공
    mc "좋아요. 어디서 찍을까요?"
    # SOURCE CH06 L1995 오므
    omu "그건 내가 찾아볼게."
    # SOURCE CH06 L1999
    narrator "오므는 카메라 화면을 살피다가 고개를 들었다."
    # SOURCE CH06 L2002 오므
    omu "근데 니도 찍어볼래?"
    # SOURCE CH06 L2005 주인공
    mc "제가요?"
    # SOURCE CH06 L2008 오므
    omu "어. 맨날 나만 찍으니까."
    # SOURCE CH06 L2011 주인공
    mc "그럼 알려주세요."
    # SOURCE CH06 L2014 오므
    omu "좋지. 자, 이쪽으로 봐라."
    # SOURCE CH06 L2018
    narrator "오므는 카메라를 내 손에 건넸다."
    # SOURCE CH06 L2020
    narrator "그리고 프레임을 보는 방법과 초점을 맞추는 방법을 간단하게 설명했다."
    # SOURCE CH06 L2023 주인공
    mc "이렇게 하면 되나요?"
    # SOURCE CH06 L2026 오므
    omu "어. 근데 니 지금 너무 아래 보고 있다."
    # SOURCE CH06 L2029 주인공
    mc "아, 그러네요."
    # SOURCE CH06 L2032 오므
    # COMMON STANDING BEGIN CH06 L2032
    $ story_stage(faces={"omu": "happy"})
    # COMMON STANDING END CH06 L2032
    omu "ㅋㅋㅋ 괜찮다. 다시 해봐."
    # CONTI SOURCE CH06 L2034 [SFX] 셔터
    # SOURCE CH06 L2038
    narrator "처음 찍은 사진은 조금 기울어져 있었다."
    # SOURCE CH06 L2041 오므
    omu "……."
    # SOURCE CH06 L2044 주인공
    mc "많이 이상한가요?"
    # SOURCE CH06 L2047 오므
    omu "아니."
    # SOURCE CH06 L2049 오므
    omu "좀 니답게 찍었네."
    # SOURCE CH06 L2052 주인공
    mc "그게 무슨 뜻이에요?"
    # SOURCE CH06 L2055 오므
    omu "그냥."
    # SOURCE CH06 L2057 오므
    omu "생각보다 재미있다는 뜻이다."
    # SOURCE CH06 L2061
    narrator "오므는 웃으며 카메라를 돌려받았다."
    # CONTI SOURCE CH06 L2063 [시간 경과 · 오후 2:40]
    $ phone_timeline_cue("CH06", "CH06_L2063")
    # SOURCE CH06 L2065 [BG] 축제 광장 가장자리 · 늦은 오후
    $ story_draft_scene("축제 광장 가장자리 · 늦은 오후", cast=["omu"], standing=True)
    # COMMON STANDING BEGIN CH06 L2065
    $ story_stage_fade_in(["omu"])
    # COMMON STANDING END CH06 L2065
    # SOURCE CH06 L2069
    narrator "해가 조금씩 기울고 있었다."
    # SOURCE CH06 L2071
    narrator "우리는 사람이 비교적 적은 광장 가장자리에 섰다."
    # SOURCE CH06 L2074 오므
    # COMMON STANDING BEGIN CH06 L2074
    $ story_stage(faces={"omu": "normal"})
    # COMMON STANDING END CH06 L2074
    omu "여기서 하나 찍자."
    # SOURCE CH06 L2077 주인공
    mc "좋아요."
    # SOURCE CH06 L2080 오므
    omu "잠깐."
    # SOURCE CH06 L2084
    narrator "오므는 카메라를 작은 삼각대에 올려놓고 타이머를 맞췄다."
    # SOURCE CH06 L2087 주인공
    mc "오므 씨도 같이 찍는 거죠?"
    # SOURCE CH06 L2090 오므
    omu "어. 당연하지."
    # SOURCE CH06 L2093 주인공
    mc "그럼 오므 씨도 사진 속에 남겠네요."
    # SOURCE CH06 L2096 오므
    omu "……."
    # SOURCE CH06 L2099 오므
    omu "그렇네."
    # SOURCE CH06 L2103
    narrator "오므는 잠시 화면을 바라보다가 나를 돌아봤다."
    # SOURCE CH06 L2106 오므
    omu "야."
    # SOURCE CH06 L2109 주인공
    mc "네?"
    # SOURCE CH06 L2112 오므
    omu "생각해보니까 나는 맨날 찍는 쪽이었거든."
    # SOURCE CH06 L2114 오므
    omu "사진 속에는 내가 없는 경우가 많았다."
    # SOURCE CH06 L2117 주인공
    mc "네."
    # SOURCE CH06 L2120 오므
    omu "근데 오늘은……."
    # SOURCE CH06 L2122 오므
    # COMMON STANDING BEGIN CH06 L2122
    $ story_stage(faces={"omu": "embarrassed"})
    # COMMON STANDING END CH06 L2122
    omu "나도 같이 남기고 싶네."
    # SOURCE CH06 L2125 주인공
    mc "저도 그래요."
    # CONTI SOURCE CH06 L2127 [ANIM] 오므의 시선이 잠시 아래로 내려갔다 돌아오는 표정 전환
    # SOURCE CH06 L2130 오므
    omu "……어."
    # SOURCE CH06 L2132 오므
    omu "그럼 웃어라."
    # CONTI SOURCE CH06 L2134 [SFX] 카메라 타이머 소리
    # SOURCE CH06 L2138
    narrator "나는 카메라를 바라봤다."
    # SOURCE CH06 L2140
    narrator "오므도 옆에서 카메라를 향해 웃었다."
    # CONTI SOURCE CH06 L2142 [SFX] 셔터
    # CONTI SOURCE CH06 L2144 [연출] CH05의 팀 단체 사진과 대비되는 둘만의 사진. 주인공의 외형을 특정하지 않는 구도 또는 사진 결과를 직접 보여주지 않고 오므의 반응으로 처리.
    # SOURCE CH06 L2147 오므
    omu "……오."
    # SOURCE CH06 L2150 주인공
    mc "잘 나왔어요?"
    # SOURCE CH06 L2153 오므
    omu "어."
    # SOURCE CH06 L2156 주인공
    mc "보여주세요."
    # SOURCE CH06 L2159 오므
    omu "잠깐만."
    # SOURCE CH06 L2163
    # CH06 VISUAL 066 BEGIN omu-02-start
    $ cg_start("ch06_festival_omu_02", transition=0.35)
    # CH06 VISUAL 066 END omu-02-start
    narrator "오므는 사진을 확인하더니 조금 웃었다."
    # SOURCE CH06 L2166 오므
    # COMMON STANDING BEGIN CH06 L2166
    $ story_stage(faces={"omu": "happy"})
    # COMMON STANDING END CH06 L2166
    omu "……좋네."
    # SOURCE CH06 L2169 주인공
    mc "많이 마음에 드세요?"
    # SOURCE CH06 L2172 오므
    omu "어."
    # SOURCE CH06 L2174 오므
    omu "오늘은 좀 오래 기억날 것 같다."
    # SOURCE CH06 L2177 주인공
    mc "사진이 남으니까요?"
    # SOURCE CH06 L2180 오므
    omu "그것도 있고."
    # SOURCE CH06 L2184
    narrator "오므는 잠시 말을 멈췄다."
    # SOURCE CH06 L2187 오므
    # COMMON STANDING BEGIN CH06 L2187
    $ story_stage(faces={"omu": "embarrassed"})
    # COMMON STANDING END CH06 L2187
    omu "……같이 있어서."
    # SOURCE CH06 L2190 주인공
    mc "저도 오늘 재미있었어요."
    # SOURCE CH06 L2193 오므
    omu "……."
    # SOURCE CH06 L2195 오므
    omu "그라면 됐다."
    # SOURCE CH06 L2197 [CONDITION] `ch04_partner == "omu"`
    if story_id(ch04_partner) == "omu":
        # SOURCE CH06 L2200 주인공
        mc "전에 학교 밖에도 같이 사진 찍으러 가자고 하셨잖아요."
        # SOURCE CH06 L2203 오므
        omu "어. 기억하지."
        # SOURCE CH06 L2206 주인공
        mc "그 약속도 꼭 지켜요."
        # SOURCE CH06 L2209 오므
        omu "당연하지."
        # SOURCE CH06 L2211 오므
        # COMMON STANDING BEGIN CH06 L2211
        $ story_stage(faces={"omu": "happy"})
        # COMMON STANDING END CH06 L2211
        omu "그때는 오늘보다 더 좋은 데 보여줄게."
    # SOURCE CH06 L2217
    # CH06 VISUAL 066 BEGIN omu-02-end
    $ cg_end(transition=0.35)
    # CH06 VISUAL 066 END omu-02-end
    narrator "우리는 부스로 돌아가기 시작했다."
    # SOURCE CH06 L2219
    narrator "오므는 중간중간 풍경을 한두 장 더 찍었다."
    # SOURCE CH06 L2221
    narrator "그런데 걸어가는 동안 카메라보다 나를 더 자주 바라보는 것 같은 기분이 들었다."
    # SOURCE CH06 L2223
    narrator "……착각일까?"
    # SOURCE CH06 L2225 [FLAG] `ch06_omu_festival_event = True`
    $ story_flag("ch06_omu_festival_event", True)
    # SOURCE CH06 L2227 [FLAG] `ch06_special_memory = omu_photo`
    $ story_flag("ch06_special_memory", 'omu_photo')
    # CONTI SOURCE CH06 L2229 [RETURN TO SC05]
    jump ch06_sc05

label ch06_sc04_lumi:
    $ phone_timeline_enter("CH06", "ch06_sc04_lumi")
    # SOURCE CH06 L2232 하린: 완성된 공간, 예상하지 못한 마음
    # SOURCE CH06 L2234 [BG] 축제 부스 · 오전 9:25
    $ phone_timeline_cue("CH06", "CH06_L2234")
    $ story_draft_scene("축제 부스 · 오전 9:25", cast=["lumi"], standing=True)
    # COMMON STANDING BEGIN CH06 L2234
    $ story_stage_fade_in(["lumi"])
    # COMMON STANDING END CH06 L2234
    # SOURCE CH06 L2236 [BGM] Calm Morning
    $ story_draft_bgm("Calm Morning")
    # CONTI SOURCE CH06 L2238 [ANIM] 하린 기본 LD · 자연스러운 눈 깜빡임
    # CONTI SOURCE CH06 L2240 [연출] SC04 시작 시 오전의 약속을 짧게 회상한 뒤 현재 시점으로 돌아온다.
    $ story_flashback_set(True)
    # SOURCE CH06 L2244
    narrator "하린 선배와의 약속은 축제 개장 전에 이미 시작됐다."
    # SOURCE CH06 L2246
    narrator "아직 손님이 들어오기 전, 선배는 나에게 부스 안을 함께 걸어보자고 했다."
    # SOURCE CH06 L2249 하린
    lumi "[player_name] 씨. 잠깐 시간 괜찮아요?"
    # SOURCE CH06 L2252 주인공
    mc "네. 무슨 일이세요?"
    # SOURCE CH06 L2255 하린
    lumi "전에 약속했잖아요."
    # SOURCE CH06 L2257 하린
    lumi "완성된 공간을 같이 둘러보기로."
    # SOURCE CH06 L2260 주인공
    mc "기억하고 있어요."
    # SOURCE CH06 L2263 하린
    # COMMON STANDING BEGIN CH06 L2263
    $ story_stage(faces={"lumi": "happy"})
    # COMMON STANDING END CH06 L2263
    lumi "후후. 그럼 가볼까요?"
    # SOURCE CH06 L2265 [BG] 완성된 체험 전시 부스 · 개장 전
    $ story_draft_scene("완성된 체험 전시 부스 · 개장 전", cast=["lumi"], standing=True)
    # COMMON STANDING BEGIN CH06 L2265
    $ story_stage_fade_in(["lumi"])
    # COMMON STANDING END CH06 L2265
    # SOURCE CH06 L2269
    narrator "아직 사람이 없는 부스는 어제와 다른 분위기였다."
    # SOURCE CH06 L2271
    narrator "전시물이 제자리에 걸려 있고, 햇빛이 테이블 위로 들어오고 있었다."
    # SOURCE CH06 L2273
    narrator "하린 선배는 천천히 걸으며 공간을 설명했다."
    # SOURCE CH06 L2276 하린
    # COMMON STANDING BEGIN CH06 L2276
    $ story_stage(faces={"lumi": "serious"})
    # COMMON STANDING END CH06 L2276
    lumi "처음에는 여기에 테이블을 하나 더 놓으려고 했어요."
    # SOURCE CH06 L2279 주인공
    mc "그런데 통로 때문에 바꾸셨죠?"
    # SOURCE CH06 L2282 하린
    lumi "네. 기억하시네요."
    # SOURCE CH06 L2285 주인공
    mc "선배가 여러 번 설명해 주셨잖아요."
    # SOURCE CH06 L2288 하린
    lumi "……그러게요."
    # SOURCE CH06 L2292
    narrator "하린 선배가 웃었다."
    # SOURCE CH06 L2295 하린
    lumi "사실 처음에는 이렇게 될 줄 몰랐어요."
    # SOURCE CH06 L2298 주인공
    mc "어떤 부분이요?"
    # SOURCE CH06 L2301 하린
    lumi "계획이 생각보다 많이 바뀌었잖아요."
    # SOURCE CH06 L2303 하린
    lumi "방문객 의견도 들어야 했고, 시범 운영에서 문제도 생겼고."
    # SOURCE CH06 L2306 주인공
    mc "네."
    # SOURCE CH06 L2309 하린
    lumi "그런데 막상 완성된 걸 보니까……."
    # SOURCE CH06 L2311 하린
    # COMMON STANDING BEGIN CH06 L2311
    $ story_stage(faces={"lumi": "happy"})
    # COMMON STANDING END CH06 L2311
    lumi "처음 생각한 것보다 더 마음에 들어요."
    # SOURCE CH06 L2315
    narrator "하린 선배는 전시 공간을 바라봤다."
    # SOURCE CH06 L2318 하린
    lumi "공간이라는 게 혼자서 설계한다고 끝나는 게 아니더라고요."
    # SOURCE CH06 L2320 하린
    lumi "누가 쓰느냐에 따라 달라지니까."
    # SOURCE CH06 L2323 주인공
    mc "저도 선배랑 같이 수정했던 부분이 기억에 남아요."
    # SOURCE CH06 L2326 하린
    lumi "……."
    # SOURCE CH06 L2329 하린
    # COMMON STANDING BEGIN CH06 L2329
    $ story_stage(faces={"lumi": "embarrassed"})
    # COMMON STANDING END CH06 L2329
    lumi "또 그런 말을 하시네."
    # SOURCE CH06 L2332 주인공
    mc "어떤 말이요?"
    # SOURCE CH06 L2335 하린
    lumi "사람 기분 좋게 만드는 말."
    # SOURCE CH06 L2338 주인공
    mc "그런 뜻으로 말씀드린 건 아닌데요."
    # SOURCE CH06 L2341 하린
    lumi "알아요."
    # SOURCE CH06 L2343 하린
    lumi "그래서 더 그런가 봐."
    # SOURCE CH06 L2347
    narrator "하린 선배는 잠시 시선을 피했다."
    # CONTI SOURCE CH06 L2349 [ANIM] 하린의 눈 깜빡임 후 작고 수줍은 미소
    # SOURCE CH06 L2352 하린
    lumi "……오늘 끝나고도 잠깐 같이 걸을래요?"
    # SOURCE CH06 L2355 주인공
    mc "좋아요."
    # SOURCE CH06 L2358 하린
    # COMMON STANDING BEGIN CH06 L2358
    $ story_stage(faces={"lumi": "happy"})
    # COMMON STANDING END CH06 L2358
    lumi "그럼 약속이에요."
    # CONTI SOURCE CH06 L2360 [TRANSITION] 현재 시점 · 오후 1:35
    $ phone_timeline_cue("CH06", "CH06_L2360")
    $ story_flashback_set(False)
    # SOURCE CH06 L2362 [BG] 축제 광장 · 오후
    $ story_draft_scene("축제 광장 · 오후", cast=["lumi"], standing=True)
    # COMMON STANDING BEGIN CH06 L2362
    $ story_stage_fade_in(["lumi"])
    # COMMON STANDING END CH06 L2362
    # SOURCE CH06 L2366
    narrator "그 약속을 떠올리며 하린 선배와 함께 부스 밖으로 나왔다."
    # SOURCE CH06 L2368
    narrator "교대 시간이라 조금 여유가 생겼다."
    # SOURCE CH06 L2371 하린
    lumi "어디 가보고 싶어요?"
    # SOURCE CH06 L2374 주인공
    mc "선배가 가보고 싶은 곳이요."
    # SOURCE CH06 L2377 하린
    # COMMON STANDING BEGIN CH06 L2377
    $ story_stage(faces={"lumi": "surprised"})
    # COMMON STANDING END CH06 L2377
    lumi "……저요?"
    # SOURCE CH06 L2380 주인공
    mc "네. 오늘은 선배가 정해주세요."
    # SOURCE CH06 L2383 하린
    lumi "후후. 그럼 너무 계획적으로 움직일 수도 있는데."
    # SOURCE CH06 L2386 주인공
    mc "괜찮아요."
    # SOURCE CH06 L2389 하린
    lumi "……."
    # SOURCE CH06 L2391 하린
    # COMMON STANDING BEGIN CH06 L2391
    $ story_stage(faces={"lumi": "happy"})
    # COMMON STANDING END CH06 L2391
    lumi "그럼 오히려 계획 없이 걸어볼까요?"
    # SOURCE CH06 L2394 주인공
    mc "선배가요?"
    # SOURCE CH06 L2397 하린
    lumi "왜요. 저도 가끔은 그래요."
    # SOURCE CH06 L2401
    narrator "조금 의외였다."
    # SOURCE CH06 L2403
    narrator "하린 선배는 먼저 축제 광장 쪽으로 걸어갔다."
    # SOURCE CH06 L2405
    narrator "우리는 길을 정하지 않고 부스를 둘러봤다."
    # SOURCE CH06 L2407 [BG] 축제 광장 · 작은 휴게 공간
    $ story_draft_scene("축제 광장 · 작은 휴게 공간", cast=["lumi"], standing=True)
    # COMMON STANDING BEGIN CH06 L2407
    $ story_stage_fade_in(["lumi"])
    # COMMON STANDING END CH06 L2407
    # SOURCE CH06 L2411
    narrator "잠시 후 우리는 나무 그늘 아래 벤치에 앉았다."
    # SOURCE CH06 L2413
    narrator "하린 선배는 멀리서 사람들이 지나가는 모습을 바라봤다."
    # SOURCE CH06 L2416 하린
    # COMMON STANDING BEGIN CH06 L2416
    $ story_stage(faces={"lumi": "happy"})
    # COMMON STANDING END CH06 L2416
    # CH06 VISUAL 0610 BEGIN lumi-01-start
    $ cg_start("ch06_festival_lumi_01", transition=0.35)
    # CH06 VISUAL 0610 END lumi-01-start
    lumi "……재미있네요."
    # SOURCE CH06 L2419 주인공
    mc "뭐가요?"
    # SOURCE CH06 L2422 하린
    lumi "사람들이 공간을 사용하는 모습이요."
    # SOURCE CH06 L2424 하린
    lumi "저쪽에는 그냥 벤치 하나만 있는데도 사람이 계속 앉았다 가잖아요."
    # SOURCE CH06 L2427 주인공
    mc "그러네요."
    # SOURCE CH06 L2430 하린
    lumi "누군가는 쉬고, 누군가는 사진 찍고."
    # SOURCE CH06 L2432 하린
    lumi "같은 장소인데 다르게 쓰이는 게 신기해요."
    # SOURCE CH06 L2435 주인공
    mc "선배는 정말 건축을 좋아하시는 것 같아요."
    # SOURCE CH06 L2438 하린
    lumi "……."
    # SOURCE CH06 L2440 하린
    lumi "네. 좋아해요."
    # SOURCE CH06 L2444
    narrator "하린 선배는 조금 생각하다 말을 이었다."
    # SOURCE CH06 L2447 하린
    # COMMON STANDING BEGIN CH06 L2447
    $ story_stage(faces={"lumi": "serious"})
    # COMMON STANDING END CH06 L2447
    lumi "그런데 요즘은 제가 왜 그걸 좋아하는지도 다시 생각하게 됐어요."
    # SOURCE CH06 L2450 주인공
    mc "왜요?"
    # SOURCE CH06 L2453 하린
    lumi "처음에는 반듯하고 예쁜 구조가 좋았거든요."
    # SOURCE CH06 L2455 하린
    lumi "그런데 실제로 사람들이 머무는 모습을 보니까……."
    # SOURCE CH06 L2457 하린
    lumi "꼭 그렇게만 생각할 필요는 없겠더라고요."
    # SOURCE CH06 L2460 주인공
    mc "그것도 좋은 변화 같아요."
    # SOURCE CH06 L2463 하린
    lumi "그렇죠?"
    # SOURCE CH06 L2467
    narrator "하린 선배는 웃었다."
    # SOURCE CH06 L2469
    narrator "잠시 바람이 불었다."
    # SOURCE CH06 L2472 하린
    lumi "오늘은 이상하게 시간이 빨리 가네요."
    # SOURCE CH06 L2475 주인공
    mc "재미있으니까 그런 거 아닐까요?"
    # SOURCE CH06 L2478 하린
    lumi "……그런가."
    # SOURCE CH06 L2481 주인공
    mc "저는 선배랑 이야기하는 게 재미있어요."
    # SOURCE CH06 L2484 하린
    # CH06 VISUAL 0610 BEGIN lumi-02-switch
    if cg_asset("ch06_festival_lumi_02"):
        $ cg_start("ch06_festival_lumi_02", transition=0.35)
    else:
        $ cg_end(transition=0.35)
        $ story_stage(faces={"lumi": "embarrassed"})
    # CH06 VISUAL 0610 END lumi-02-switch
    lumi "……."
    # SOURCE CH06 L2487 하린
    lumi "……진짜."
    # SOURCE CH06 L2491
    narrator "하린 선배가 작게 웃었다."
    # SOURCE CH06 L2493
    narrator "그러면서도 나를 바로 바라보지는 못했다."
    # SOURCE CH06 L2496 하린
    # COMMON STANDING BEGIN CH06 L2496
    $ story_stage(faces={"lumi": "embarrassed"})
    # COMMON STANDING END CH06 L2496
    lumi "이렇게 말하는 거, 일부러 연습하시는 거예요?"
    # SOURCE CH06 L2499 주인공
    mc "아니요. 그냥 생각나는 대로 말씀드리는 건데요."
    # SOURCE CH06 L2502 하린
    lumi "그럼 더 곤란한데."
    # SOURCE CH06 L2505 주인공
    mc "왜요?"
    # SOURCE CH06 L2508 하린
    lumi "……."
    # SOURCE CH06 L2510 하린
    lumi "자꾸 기대하게 되잖아."
    # SOURCE CH06 L2514
    narrator "목소리가 조금 작아졌다."
    # SOURCE CH06 L2516
    # CH06 VISUAL 0610 BEGIN lumi-02-end
    $ cg_end(transition=0.35)
    $ story_stage(faces={"lumi": "embarrassed"})
    # CH06 VISUAL 0610 END lumi-02-end
    narrator "나는 무슨 뜻인지 되묻고 싶었지만, 선배가 먼저 일어섰다."
    # SOURCE CH06 L2519 하린
    # COMMON STANDING BEGIN CH06 L2519
    $ story_stage(faces={"lumi": "happy"})
    # COMMON STANDING END CH06 L2519
    lumi "자, 이제 돌아가요."
    # SOURCE CH06 L2522 하린
    lumi "우리 팀 기다리겠네."
    # SOURCE CH06 L2525 주인공
    mc "네. 같이 가요."
    # SOURCE CH06 L2527 [CONDITION] `ch04_partner == "harin"`
    if story_id(ch04_partner) == "lumi":
        # SOURCE CH06 L2530 하린
        lumi "지난번에 모형 고칠 때도 그랬잖아요."
        # SOURCE CH06 L2533 주인공
        mc "어떤 거요?"
        # SOURCE CH06 L2536 하린
        lumi "그냥 옆에 있어주는 것도 도움이 될 때가 있다고."
        # SOURCE CH06 L2539 주인공
        mc "네. 기억해요."
        # SOURCE CH06 L2542 하린
        lumi "……오늘도 그런 것 같아요."
    # SOURCE CH06 L2548
    narrator "우리는 다시 부스로 돌아갔다."
    # SOURCE CH06 L2550
    narrator "하린 선배는 평소처럼 차분하게 걸었지만."
    # SOURCE CH06 L2552
    narrator "가끔 내 쪽을 바라볼 때마다, 조금씩 부끄러워하는 것 같았다."
    # SOURCE CH06 L2554
    narrator "오늘 나는 완성된 부스보다 더 기억에 남을 장면을 본 것 같았다."
    # SOURCE CH06 L2556 [FLAG] `ch06_harin_festival_event = True`
    $ story_flag("ch06_harin_festival_event", True)
    # SOURCE CH06 L2558 [FLAG] `ch06_special_memory = harin_space`
    $ story_flag("ch06_special_memory", 'harin_space')
    # CONTI SOURCE CH06 L2560 [RETURN TO SC05]
    jump ch06_sc05

label ch06_sc05:
    $ phone_timeline_enter("CH06", "ch06_sc05")
    # SOURCE CH06 L2563 마지막까지 사고라고?
    # SOURCE CH06 L2565 [BG] 공동 체험 전시 부스 · 오후
    $ story_draft_scene("공동 체험 전시 부스 · 오후", cast=["roman", "sia", "darim", "omu", "lumi"], standing=True)
    # COMMON STANDING BEGIN CH06 L2565
    $ story_stage_fade_in(["roman", "sia", "darim", "omu", "lumi"])
    # COMMON STANDING END CH06 L2565
    # SOURCE CH06 L2567 [BGM] Festival Afternoon
    $ story_draft_bgm("Festival Afternoon")
    # SOURCE CH06 L2571
    narrator "쉬는 시간이 끝나고 다시 부스로 돌아왔다."
    # SOURCE CH06 L2573
    narrator "오전보다 방문객이 더 많아져 있었다."
    # SOURCE CH06 L2575
    narrator "하지만 다림 선배가 운영표를 잘 조정한 덕분에 팀원들은 차례대로 쉴 수 있었다."
    # SOURCE CH06 L2578 다림
    darim "[player_name] 씨, 잘 쉬셨어요?"
    # SOURCE CH06 L2581 주인공
    mc "네. 덕분에 축제도 구경하고 왔어요."
    # SOURCE CH06 L2584 다림
    darim "다행이네요."
    # SOURCE CH06 L2587 시아
    # COMMON STANDING BEGIN CH06 L2587
    $ story_stage(faces={"sia": "happy", "darim": "happy", "roman": "happy"})
    # COMMON STANDING END CH06 L2587
    sia "야, 근데 우리 부스 오늘 진짜 인기 많지 않냐?"
    # SOURCE CH06 L2590 오므
    omu "생각보다 많이 오네."
    # SOURCE CH06 L2593 로만
    roman "앗,,, 질문 카드도 많이 사용했어요……!"
    # SOURCE CH06 L2596 하린
    lumi "통로도 지금까지는 괜찮았고요."
    # SOURCE CH06 L2600
    narrator "모두 기분이 좋아 보였다."
    # SOURCE CH06 L2602
    narrator "그런데 그때였다."
    # CONTI SOURCE CH06 L2604 [SFX] 바람이 세게 부는 소리
    # CONTI SOURCE CH06 L2606 [SFX] 덜컹, 금속 받침대가 움직이는 소리
    # SOURCE CH06 L2609 오므
    omu "……어?"
    # SOURCE CH06 L2612 하린
    lumi "잠깐만요."
    # SOURCE CH06 L2616
    narrator "공용 통로 쪽의 임시 안내판이 바람에 흔들리고 있었다."
    # SOURCE CH06 L2618
    narrator "축제 운영본부에서 설치한 방향 안내판이었다."
    # SOURCE CH06 L2620
    narrator "받침대가 한쪽으로 기울어지더니 바닥에 넘어졌다."
    # CONTI SOURCE CH06 L2622 [SFX] 안내판 넘어지는 소리
    # SOURCE CH06 L2625 방문객 A
    ch06_visitor_a "어? 저거 넘어졌어요!"
    # SOURCE CH06 L2628 방문객 B
    ch06_visitor_b "어디로 가야 하지?"
    # SOURCE CH06 L2632
    narrator "안내판이 통로 일부를 가로막았다."
    # SOURCE CH06 L2634
    narrator "방문객 몇 명이 멈춰 섰고, 뒤따라 오던 사람들이 다른 방향으로 움직이기 시작했다."
    # SOURCE CH06 L2637 다림
    darim "다들 잠깐만요."
    # SOURCE CH06 L2639 다림
    darim "방문객 안내부터 할게요."
    # SOURCE CH06 L2642 하린
    lumi "저쪽 통로는 잠시 비워야겠어요."
    # SOURCE CH06 L2645 주인공
    mc "제가 운영본부에 연락할게요."
    # SOURCE CH06 L2649
    narrator "나는 공용 안내판이 넘어졌다는 사실과 정확한 위치를 운영본부에 전달했다."
    # SOURCE CH06 L2652 운영본부 담당자 · 전화
    ch06_staff "확인했습니다. 안전 담당 인력을 보내겠습니다."
    # SOURCE CH06 L2654 운영본부 담당자 · 전화
    ch06_staff "그동안 통로를 비우고 방문객을 다른 길로 안내해주세요."
    # SOURCE CH06 L2657 주인공
    mc "네, 알겠습니다."
    # SOURCE CH06 L2660 주인공
    # COMMON STANDING BEGIN CH06 L2660
    $ story_stage(faces={"darim": "serious", "roman": "serious", "omu": "serious", "lumi": "serious", "sia": "serious"})
    # COMMON STANDING END CH06 L2660
    mc "다림 선배, 담당자가 오고 있대요. 우선 이쪽으로 안내해달라고 하셨어요."
    # SOURCE CH06 L2663 다림
    darim "좋아요. 제가 방문객들에게 설명할게요."
    # SOURCE CH06 L2666 다림
    darim "잠시만요. 이쪽 통로는 안전 점검 중이라 반대편으로 이동 부탁드릴게요."
    # SOURCE CH06 L2669 로만
    roman "앗,,, 저도 안내 카드 들고 있을게요……!"
    # SOURCE CH06 L2672 오므
    omu "내는 사람들이 안쪽으로 안 들어오게 봐줄게."
    # SOURCE CH06 L2675 하린
    lumi "좋아요. 이쪽부터 비워요."
    # SOURCE CH06 L2678 시아
    sia "야, 옆 부스에도 알려야겠다."
    # SOURCE CH06 L2680 [BG] 라이벌 팀 부스 앞
    $ story_draft_scene("라이벌 팀 부스 앞", cast=["sia", "ski", "hyeophap", "hess", "bambam"], standing=True)
    # COMMON STANDING BEGIN CH06 L2680
    $ story_stage_fade_in(["sia", "ski", "hyeophap", "hess", "bambam"])
    # COMMON STANDING END CH06 L2680
    # SOURCE CH06 L2684
    narrator "시아와 나는 옆 부스로 향했다."
    # SOURCE CH06 L2686
    narrator "스키가 쿠키를 포장하고 있었다."
    # SOURCE CH06 L2689 시아
    # COMMON STANDING BEGIN CH06 L2689
    $ story_stage(faces={"sia": "serious", "ski": "smug"})
    # COMMON STANDING END CH06 L2689
    sia "야, 스키!"
    # SOURCE CH06 L2692 스키
    ski "왜? 또 내 쿠키 먹고 싶냐?"
    # SOURCE CH06 L2695 시아
    # COMMON STANDING BEGIN CH06 L2695
    $ story_stage(faces={"sia": "serious", "ski": "serious", "hyeophap": "serious", "hess": "serious", "bambam": "serious"})
    # COMMON STANDING END CH06 L2695
    sia "아니, 지금 그럴 때 아니거든!"
    # SOURCE CH06 L2698 협합
    hyeophap "무슨 일이야?"
    # SOURCE CH06 L2701 주인공
    mc "공용 안내판이 넘어져서 통로가 막혔어요. 안전 담당자가 오고 있대요."
    # SOURCE CH06 L2704 협합
    hyeophap "알겠어. 그쪽은 잠깐 비워두자."
    # SOURCE CH06 L2707 스키
    ski "……뭐?"
    # SOURCE CH06 L2711
    narrator "스키는 통로를 한 번 보더니 곧바로 손님들에게 고개를 돌렸다."
    # SOURCE CH06 L2714 스키
    ski "잠깐만! 이쪽 통로는 지금 이용하면 안 돼."
    # SOURCE CH06 L2716 스키
    ski "다른 쪽으로 돌아가면 돼. 내가 안내할게."
    # SOURCE CH06 L2719 헤스
    hess "대기 중인 손님들부터 옮기겠습니다."
    # SOURCE CH06 L2722 밤밤
    bambam "제가 이쪽 줄 정리할게요."
    # SOURCE CH06 L2725 협합
    hyeophap "스키, 안내판 근처에는 가지 말고 사람들부터 이동시켜."
    # SOURCE CH06 L2728 스키
    ski "알았어."
    # SOURCE CH06 L2732
    narrator "이번에는 허세도 농담도 없었다."
    # SOURCE CH06 L2734
    narrator "스키는 바로 방문객 안내를 시작했다."
    # SOURCE CH06 L2736
    narrator "시아도 함께 움직였다."
    # SOURCE CH06 L2739 시아
    sia "여러분, 이쪽으로 돌아가시면 돼요!"
    # SOURCE CH06 L2742 스키
    ski "맞아. 천천히 이동해!"
    # SOURCE CH06 L2745 시아
    sia "야, 오늘은 좀 잘하는데?"
    # SOURCE CH06 L2748 스키
    # COMMON STANDING BEGIN CH06 L2748
    $ story_stage(faces={"ski": "happy"})
    # COMMON STANDING END CH06 L2748
    ski "너도 지금은 잘하고 있어."
    # SOURCE CH06 L2751 시아
    # COMMON STANDING BEGIN CH06 L2751
    $ story_stage(faces={"sia": "embarrassed"})
    # COMMON STANDING END CH06 L2751
    sia "……뭐야."
    # SOURCE CH06 L2754 스키
    ski "왜. 칭찬하면 안 되냐?"
    # SOURCE CH06 L2757 시아
    sia "……아니."
    # SOURCE CH06 L2759 시아
    sia "계속해."
    # SOURCE CH06 L2763
    narrator "짧은 대화가 오갔지만, 두 사람은 다시 각자 움직였다."
    # CONTI SOURCE CH06 L2765 [SD EVENT] `ch06_festival_joint_response`
    # CONTI SOURCE CH06 L2767 [연출] 단체 SD 한 장. 스키·시아는 방문객의 우회 방향을 안내하고, 협합·헤스·밤밤은 대기줄을 정리한다. 다림·로만·오므·하린은 각자의 위치에서 안전한 이동을 돕는다. 주인공의 모습은 표시하지 않는다.
    # CONTI SOURCE CH06 L2769 [전환] 일반 LD 및 배경
    # CONTI SOURCE CH06 L2771 [시간 경과 · 오후 4:25]
    $ phone_timeline_cue("CH06", "CH06_L2771")
    # CONTI SOURCE CH06 L2773 [SFX] 담당자 도착 안내
    # SOURCE CH06 L2776 운영본부 담당자
    # COMMON STANDING BEGIN CH06 L2776
    $ story_stage(cast=["roman", "sia", "darim", "omu", "lumi", "ski", "hyeophap", "hess", "bambam"])
    # COMMON STANDING END CH06 L2776
    ch06_staff "신고해 주셔서 감사합니다. 안내판은 저희가 안전하게 수거하겠습니다."
    # SOURCE CH06 L2778 운영본부 담당자
    ch06_staff "임시 안내표지는 다른 위치에 다시 설치하겠습니다."
    # SOURCE CH06 L2781 다림
    darim "네. 다친 분은 없는 것 같아요."
    # SOURCE CH06 L2784 운영본부 담당자
    ch06_staff "확인했습니다. 통로 안전 점검 후 다시 알려드릴게요."
    # SOURCE CH06 L2788
    narrator "담당자들이 안내판을 수거하고 주변을 점검했다."
    # SOURCE CH06 L2790
    narrator "우리는 허가가 나올 때까지 해당 구역을 비워뒀다."
    # SOURCE CH06 L2792
    narrator "다행히 다친 사람은 없었다."
    # SOURCE CH06 L2794
    narrator "잠시 뒤 통행이 재개됐다."
    # SOURCE CH06 L2796 [BG] 두 부스 사이 · 오후
    $ story_draft_scene("두 부스 사이 · 오후", cast=["roman", "sia", "darim", "omu", "lumi", "ski", "hyeophap", "hess", "bambam"], standing=True)
    # COMMON STANDING BEGIN CH06 L2796
    $ story_stage_fade_in(["roman", "sia", "darim", "omu", "lumi", "ski", "hyeophap", "hess", "bambam"])
    # COMMON STANDING END CH06 L2796
    # SOURCE CH06 L2799 시아
    sia "……하."
    # SOURCE CH06 L2801 시아
    sia "또 사고냐."
    # SOURCE CH06 L2804 오므
    omu "이번에는 우리 부스 문제도 아이었잖아."
    # SOURCE CH06 L2807 시아
    sia "그건 그렇지."
    # SOURCE CH06 L2810 하린
    lumi "그래도 모두 빨리 대응해서 다행이에요."
    # SOURCE CH06 L2813 다림
    darim "맞아요. 혼자 해결하려고 했으면 더 복잡해졌을 거예요."
    # SOURCE CH06 L2816 협합
    hyeophap "서로 연락한 게 도움이 됐어."
    # SOURCE CH06 L2819 헤스
    hess "대기줄도 금방 정리됐고요."
    # SOURCE CH06 L2822 밤밤
    bambam "손님들도 차분하게 이동해 주셨어요."
    # SOURCE CH06 L2825 스키
    ski "후우……."
    # SOURCE CH06 L2828 스키
    ski "이제 다시 쿠키 팔아도 되는 거지?"
    # SOURCE CH06 L2831 협합
    hyeophap "응. 운영본부 확인 끝났어."
    # SOURCE CH06 L2834 스키
    ski "좋아."
    # SOURCE CH06 L2837 스키
    # COMMON STANDING BEGIN CH06 L2837
    $ story_stage(faces={"ski": "smug"})
    # COMMON STANDING END CH06 L2837
    ski "그럼 다시 내 시간이군!"
    # SOURCE CH06 L2840 시아
    sia "……."
    # SOURCE CH06 L2843 시아
    sia "아까는 좀 멋있었는데."
    # SOURCE CH06 L2846 스키
    ski "지금도 멋있거든?"
    # SOURCE CH06 L2849 시아
    # COMMON STANDING BEGIN CH06 L2849
    $ story_stage(faces={"sia": "smug"})
    # COMMON STANDING END CH06 L2849
    sia "응 아니야~"
    # SOURCE CH06 L2852 스키
    ski "야!"
    # SOURCE CH06 L2856
    narrator "평소의 두 사람이 돌아왔다."
    # SOURCE CH06 L2858
    narrator "그런데 이상하게 조금 반가웠다."
    # SOURCE CH06 L2861 주인공
    mc "그래도 오늘은 정말 두 팀이 잘 맞았네요."
    # SOURCE CH06 L2864 협합
    hyeophap "그러게."
    # SOURCE CH06 L2867 다림
    darim "CH03 때도 서로 도와줬잖아요."
    # SOURCE CH06 L2870 하린
    lumi "그때 경험이 있어서 더 빠르게 움직일 수 있었던 것 같아요."
    # SOURCE CH06 L2873 로만
    roman "앗,,, 저도 이번에는 덜 당황했어요……."
    # SOURCE CH06 L2876 오므
    omu "내도."
    # SOURCE CH06 L2879 스키
    ski "……야, 근데."
    # SOURCE CH06 L2882 시아
    sia "왜."
    # SOURCE CH06 L2885 스키
    ski "우리 축제 끝나면 또 볼 일 있겠지?"
    # SOURCE CH06 L2888 시아
    sia "당연하지."
    # SOURCE CH06 L2890 시아
    sia "학교에서 계속 볼 거 아니야."
    # SOURCE CH06 L2893 스키
    ski "그건 그렇네."
    # SOURCE CH06 L2896 협합
    hyeophap "같은 학교니까."
    # SOURCE CH06 L2899 밤밤
    bambam "다음 행사 때 같이 할 수도 있고요."
    # SOURCE CH06 L2902 헤스
    hess "그때도 시끄럽겠네요."
    # SOURCE CH06 L2905 오므
    omu "그건 확실하지."
    # SOURCE CH06 L2909
    narrator "모두 웃었다."
    # SOURCE CH06 L2911
    # COMMON STANDING BEGIN CH06 L2911
    $ story_stage(faces={"roman": "happy", "sia": "happy", "darim": "happy", "omu": "happy", "lumi": "happy", "ski": "happy", "hyeophap": "happy", "hess": "happy", "bambam": "happy"})
    # COMMON STANDING END CH06 L2911
    narrator "처음 만났을 때는 서로 이기기 위해 경쟁하던 사람들이었다."
    # SOURCE CH06 L2913
    narrator "그런데 지금은 다음에 또 만나자는 이야기를 하고 있다."
    # SOURCE CH06 L2915
    narrator "축제가 끝나도 완전히 끝나는 건 아닐지도 모르겠다."
    # SOURCE CH06 L2917 [FLAG] `ch06_joint_response_complete = True`
    $ story_flag("ch06_joint_response_complete", True)
    # CONTI SOURCE CH06 L2919 [SCENE 05 END]
    jump ch06_sc06

label ch06_sc06:
    $ phone_timeline_enter("CH06", "ch06_sc06")
    # SOURCE CH06 L2921 우리가 만든 하루
    # SOURCE CH06 L2923 [BG] 공동 체험 전시 부스 · 저녁
    $ story_draft_scene("공동 체험 전시 부스 · 저녁", cast=["roman", "sia", "darim", "omu", "lumi"], standing=True)
    # COMMON STANDING BEGIN CH06 L2923
    $ story_stage_fade_in(["roman", "sia", "darim", "omu", "lumi"])
    # COMMON STANDING END CH06 L2923
    # SOURCE CH06 L2925 [BGM] Festival Sunset
    $ story_draft_bgm("Festival Sunset")
    # SOURCE CH06 L2929
    narrator "시간은 생각보다 빠르게 흘렀다."
    # SOURCE CH06 L2931
    narrator "오후에는 방문객이 계속 찾아왔고, 우리는 번갈아 가며 안내와 체험 운영을 맡았다."
    # SOURCE CH06 L2933
    narrator "마지막 방문객이 나간 뒤."
    # SOURCE CH06 L2935
    narrator "다림 선배가 운영표를 내려놓았다."
    # SOURCE CH06 L2938 다림
    darim "……오늘 운영은 여기까지예요."
    # SOURCE CH06 L2941 시아
    sia "……."
    # SOURCE CH06 L2944 시아
    sia "진짜?"
    # SOURCE CH06 L2947 다림
    darim "네. 이제 정리하면 돼요."
    # SOURCE CH06 L2950 시아
    sia "으아아아아!"
    # SOURCE CH06 L2953 오므
    omu "와, 니 오늘 몇 번째 소리 지르노."
    # SOURCE CH06 L2956 시아
    sia "아니, 오늘은 진짜 끝났잖아!"
    # SOURCE CH06 L2959 로만
    roman "앗,,, 정말 끝났네요……."
    # SOURCE CH06 L2962 하린
    lumi "후후. 다들 고생 많으셨어요."
    # SOURCE CH06 L2965 주인공
    mc "정말 수고 많으셨어요."
    # SOURCE CH06 L2969
    narrator "모두의 얼굴에 피곤한 기색이 있었다."
    # SOURCE CH06 L2971
    narrator "그런데도 아무도 바로 자리를 떠나지 않았다."
    # SOURCE CH06 L2973 [BG] 부스 내부 · 저녁 조명
    $ story_draft_scene("부스 내부 · 저녁 조명")
    # SOURCE CH06 L2977
    narrator "나는 전시 공간을 천천히 둘러봤다."
    # SOURCE CH06 L2979
    narrator "테이블 위에는 사용하고 남은 질문 카드가 정리되어 있었다."
    # SOURCE CH06 L2981
    narrator "벽에는 방문객이 공개에 동의한 기록들이 걸려 있었다."
    # SOURCE CH06 L2983
    narrator "오므가 찍은 사진 옆에는 로만이 고른 문장이 붙어 있었다."
    # SOURCE CH06 L2985
    narrator "시아의 만화는 입구에서 여전히 방문객에게 길을 알려주는 듯했다."
    # SOURCE CH06 L2987
    narrator "하린 선배의 설계대로 남겨둔 통로에는 마지막 손님들의 발자국만 남아 있었다."
    # SOURCE CH06 L2989
    narrator "다림 선배가 준비한 운영 자료는 오늘 하루 종일 사람들의 움직임을 도왔다."
    # SOURCE CH06 L2992 주인공 · 혼잣말
    mc "……정말 다 같이 만든 거네."
    # SOURCE CH06 L2996
    narrator "모두가 각자 다른 걸 잘하는 사람들이었다."
    # SOURCE CH06 L2998
    narrator "처음에는 그 차이 때문에 의견이 어긋나기도 했다."
    # SOURCE CH06 L3000
    narrator "그런데 지금은 그 차이가 부스를 완성한 이유가 된 것 같았다."
    # CONTI SOURCE CH06 L3002 [시간 경과 · 오후 7:00]
    $ phone_timeline_cue("CH06", "CH06_L3002")
    # SOURCE CH06 L3004 [BG] 부스 앞 · 노을
    $ story_draft_scene("부스 앞 · 노을", cast=["roman", "sia", "darim", "omu", "lumi"], standing=True)
    # COMMON STANDING BEGIN CH06 L3004
    $ story_stage_fade_in(["roman", "sia", "darim", "omu", "lumi"])
    # COMMON STANDING END CH06 L3004
    # SOURCE CH06 L3007 시아
    sia "야, 다들!"
    # SOURCE CH06 L3010 오므
    omu "또 왜."
    # SOURCE CH06 L3013 시아
    sia "오늘 소감 한마디씩 하자."
    # SOURCE CH06 L3016 다림
    darim "후후. 갑자기요?"
    # SOURCE CH06 L3019 시아
    sia "중요하잖아."
    # SOURCE CH06 L3022 하린
    lumi "그럼 시아 씨부터 하세요."
    # SOURCE CH06 L3025 시아
    sia "어?"
    # SOURCE CH06 L3028 하린
    lumi "제안하셨으니까요."
    # SOURCE CH06 L3031 시아
    sia "……."
    # SOURCE CH06 L3033 시아
    sia "좋아. 하지 뭐."
    # SOURCE CH06 L3037
    narrator "시아는 잠시 생각하더니 입을 열었다."
    # SOURCE CH06 L3040 시아
    sia "일단……."
    # SOURCE CH06 L3042 시아
    sia "재미있었어."
    # SOURCE CH06 L3044 시아
    sia "솔직히 중간에 진짜 귀찮기도 했거든."
    # SOURCE CH06 L3047 오므
    omu "그건 맨날 말했잖아."
    # SOURCE CH06 L3050 시아
    sia "야, 끝까지 들어!"
    # SOURCE CH06 L3053 시아
    sia "근데 너희랑 같이 하니까 결국 끝까지 했네."
    # SOURCE CH06 L3055 시아
    sia "그러니까……."
    # SOURCE CH06 L3057 시아
    sia "다음에도 이런 거 하면 불러."
    # SOURCE CH06 L3061
    narrator "시아는 웃었다."
    # SOURCE CH06 L3063
    narrator "이번에는 그 말이 장난처럼 들리지 않았다."
    # SOURCE CH06 L3066 로만
    roman "앗,,, 저도……."
    # SOURCE CH06 L3068 로만
    roman "처음에는 사람들 앞에서 이야기하는 게 많이 어려웠어요."
    # SOURCE CH06 L3070 로만
    roman "그런데 오늘은 방문객에게 직접 설명도 했고……."
    # SOURCE CH06 L3072 로만
    roman "제가 쓴 문장을 읽어주시는 분들도 계셔서……."
    # SOURCE CH06 L3075 로만
    roman "……정말 기뻤어요."
    # SOURCE CH06 L3078 다림
    darim "로만 씨, 오늘 정말 잘하셨어요."
    # SOURCE CH06 L3081 로만
    roman "앗,,, 고마워요……!"
    # SOURCE CH06 L3084 오므
    omu "나는 사진이 제일 기억에 남는다."
    # SOURCE CH06 L3087 시아
    sia "당연히 네가 찍었으니까?"
    # SOURCE CH06 L3090 오므
    omu "그것도 있고."
    # SOURCE CH06 L3092 오므
    omu "오늘 사진 찍을 때 다들 표정이 좋았거든."
    # SOURCE CH06 L3094 오므
    omu "우리 부스도, 축제도."
    # SOURCE CH06 L3097 오므
    omu "그냥 오래 기억날 것 같다."
    # SOURCE CH06 L3100 하린
    lumi "저는 실제로 사람들이 공간을 사용하는 모습을 본 게 좋았어요."
    # SOURCE CH06 L3102 하린
    lumi "처음에는 정말 계획대로 될까 걱정했는데."
    # SOURCE CH06 L3104 하린
    lumi "생각하지 못했던 방식으로 좋아해 주는 분들도 있더라고요."
    # SOURCE CH06 L3107 하린
    lumi "그래서……."
    # SOURCE CH06 L3109 하린
    lumi "설계하는 일이 조금 더 재미있어졌어요."
    # SOURCE CH06 L3112 다림
    darim "저는 모두가 맡은 일을 끝까지 해주신 게 가장 좋았어요."
    # SOURCE CH06 L3114 다림
    darim "중간에 의견도 달랐고, 예상하지 못한 문제도 있었지만."
    # SOURCE CH06 L3117 다림
    darim "결국 같이 해결했잖아요."
    # SOURCE CH06 L3121
    narrator "다림 선배는 미소 지었다."
    # SOURCE CH06 L3124 다림
    darim "혼자서는 절대 못 했을 거예요."
    # SOURCE CH06 L3127 시아
    sia "……와."
    # SOURCE CH06 L3129 시아
    sia "갑자기 진짜 감동적인데?"
    # SOURCE CH06 L3132 오므
    omu "니가 소감 말하자 했잖아."
    # SOURCE CH06 L3135 시아
    sia "그건 그렇지."
    # SOURCE CH06 L3138 하린
    lumi "그럼 마지막으로 [player_name] 씨 차례네요."
    # SOURCE CH06 L3141 주인공
    mc "저요?"
    # SOURCE CH06 L3144 로만
    roman "앗,,, 저도 듣고 싶어요……."
    # SOURCE CH06 L3147 다림
    darim "후후. 편하게 말씀해 주세요."
    # SOURCE CH06 L3151
    narrator "다섯 명이 나를 바라봤다."
    # SOURCE CH06 L3153
    narrator "처음 회의에서도 이런 적이 있었던 것 같다."
    # SOURCE CH06 L3155
    narrator "그때는 무슨 말을 해야 할지 몰라서 당황했는데."
    # SOURCE CH06 L3157
    narrator "지금은 조금 달랐다."
    # SOURCE CH06 L3159 ### [CHOICE] 오늘 가장 기억에 남는 것
    menu:
        # SOURCE CH06 L3161 선택지
        "다 같이 끝까지 해낸 게 가장 기억에 남아요.":
            # SOURCE CH06 L3164 주인공
            mc "저는 다 같이 끝까지 해낸 게 가장 기억에 남아요."
            # SOURCE CH06 L3166 주인공
            mc "처음에는 이렇게 잘 맞는 팀이 될 줄 몰랐거든요."
            # SOURCE CH06 L3169 다림
            darim "후후. 저도 그래요."
            # SOURCE CH06 L3172 시아
            sia "와, 처음에는 우리가 별로였냐?"
            # SOURCE CH06 L3175 주인공
            mc "그런 뜻은 아니었는데요!"
            # SOURCE CH06 L3178 오므
            omu "ㅋㅋㅋ 인정할 건 인정하자."
            # CONTI SOURCE CH06 L3180 [CHOICE EFFECT] [FLAG] `ch06_final_reflection = teamwork`
            $ story_apply("ch06_final_reflection_a", values={'ch06_final_reflection': 'teamwork'})
        # SOURCE CH06 L3182 선택지
        "처음 보는 사람들이 저희 전시를 즐겨준 게 좋았어요.":
            # SOURCE CH06 L3185 주인공
            mc "저는 방문객들이 전시를 즐겨준 게 가장 좋았어요."
            # SOURCE CH06 L3187 주인공
            mc "저희끼리만 준비하던 걸 다른 사람들도 좋아해 주니까 뿌듯하더라고요."
            # SOURCE CH06 L3190 로만
            roman "앗,,, 맞아요……!"
            # SOURCE CH06 L3193 하린
            lumi "그게 실제로 완성됐다는 느낌이죠."
            # SOURCE CH06 L3196 오므
            omu "사진 찍을 때도 그 생각했어."
            # CONTI SOURCE CH06 L3198 [CHOICE EFFECT] [FLAG] `ch06_final_reflection = visitors`
            $ story_apply("ch06_final_reflection_b", values={'ch06_final_reflection': 'visitors'})
        # SOURCE CH06 L3200 선택지
        "이 사람들을 알게 된 게 가장 좋았어요.":
            # SOURCE CH06 L3203 주인공
            mc "저는……."
            # SOURCE CH06 L3205 주인공
            mc "여러분을 알게 된 게 가장 좋았어요."
            # SOURCE CH06 L3208 시아
            sia "……."
            # SOURCE CH06 L3211 로만
            roman "앗……."
            # SOURCE CH06 L3214 주인공
            mc "축제 준비하면서 좋은 사람들을 많이 만났다고 생각하거든요."
            # SOURCE CH06 L3217 하린
            lumi "……후후."
            # SOURCE CH06 L3219 하린
            lumi "그런 말씀을 하시면 조금 부끄러운데."
            # SOURCE CH06 L3222 다림
            darim "저도 같은 마음이에요."
            # SOURCE CH06 L3225 오므
            omu "……어."
            # SOURCE CH06 L3227 오므
            omu "나도."
            # CONTI SOURCE CH06 L3229 [CHOICE EFFECT] [FLAG] `ch06_final_reflection = relationships`
            $ story_apply("ch06_final_reflection_c", values={'ch06_final_reflection': 'relationships'})
    # SOURCE CH06 L3235
    narrator "잠시 조용해졌다."
    # SOURCE CH06 L3237
    narrator "그런데 어색한 침묵은 아니었다."
    # SOURCE CH06 L3239
    narrator "서로 무슨 말을 하지 않아도 조금은 통하는 느낌이었다."
    # CONTI SOURCE CH06 L3241 [SFX] 카메라 셔터
    # SOURCE CH06 L3244 오므
    omu "자, 하나 찍었다."
    # SOURCE CH06 L3247 시아
    sia "야! 왜 몰래 찍는데!"
    # SOURCE CH06 L3250 오므
    omu "자연스러운 게 좋잖아."
    # SOURCE CH06 L3253 하린
    lumi "어제 단체 사진도 찍었잖아요."
    # SOURCE CH06 L3256 오므
    omu "어제랑 오늘은 다르지."
    # SOURCE CH06 L3259 로만
    roman "앗,,, 맞아요."
    # SOURCE CH06 L3262 다림
    darim "그럼 오늘 사진도 나중에 공유해 주세요."
    # SOURCE CH06 L3265 오므
    omu "알았다."
    # SOURCE CH06 L3269
    narrator "CH05에서 찍었던 단체 사진이 떠올랐다."
    # SOURCE CH06 L3271
    narrator "그때는 축제를 앞두고 웃고 있었다."
    # SOURCE CH06 L3273
    narrator "오늘은 축제를 마치고 웃고 있다."
    # SOURCE CH06 L3275
    narrator "같은 사람들이지만, 서로 다른 하루였다."
    # CONTI SOURCE CH06 L3277 [시간 경과 · 오후 7:45]
    $ phone_timeline_cue("CH06", "CH06_L3277")
    # SOURCE CH06 L3279 [BG] 부스 정리 후 · 야간 축제 광장
    $ story_draft_scene("부스 정리 후 · 야간 축제 광장", cast=["roman", "sia", "darim", "omu", "lumi"], standing=True)
    # COMMON STANDING BEGIN CH06 L3279
    $ story_stage_fade_in(["roman", "sia", "darim", "omu", "lumi"])
    # COMMON STANDING END CH06 L3279
    # SOURCE CH06 L3283
    narrator "개인 기록과 남은 물품을 분류하고, 운영본부에 반환해야 할 장비를 정리했다."
    # SOURCE CH06 L3285
    narrator "공개 동의가 없는 기록은 전시 자료에 섞이지 않도록 따로 처리했다."
    # SOURCE CH06 L3287
    narrator "남은 정산과 최종 반납은 내일 하기로 했다."
    # SOURCE CH06 L3289
    narrator "우리의 부스 운영은 여기서 마무리였다."
    # SOURCE CH06 L3292 시아
    sia "……야."
    # SOURCE CH06 L3295 주인공
    mc "네?"
    # SOURCE CH06 L3298 시아
    sia "진짜 끝났네."
    # SOURCE CH06 L3301 주인공
    mc "그러게요."
    # SOURCE CH06 L3304 시아
    sia "맨날 끝나면 좋겠다 했는데."
    # SOURCE CH06 L3306 시아
    sia "막상 끝나니까 좀 아쉽다."
    # SOURCE CH06 L3309 오므
    omu "내도."
    # SOURCE CH06 L3312 로만
    roman "앗,,, 저도 조금요……."
    # SOURCE CH06 L3315 다림
    darim "그래도 내일 마지막으로 한 번 더 모이잖아요."
    # SOURCE CH06 L3318 하린
    lumi "정산하고 정리해야 하니까요."
    # SOURCE CH06 L3321 시아
    sia "아, 맞다."
    # SOURCE CH06 L3323 시아
    sia "우리 아직 일 남았지."
    # SOURCE CH06 L3326 오므
    omu "그 말 듣고 표정 밝아지는 거 처음 본다."
    # SOURCE CH06 L3329 시아
    sia "야, 그런 뜻 아니거든!"
    # SOURCE CH06 L3333
    narrator "모두 웃었다."
    # SOURCE CH06 L3335
    narrator "축제의 불빛이 하나둘 켜지기 시작했다."
    # SOURCE CH06 L3337
    narrator "멀리서 공연 음악이 들려왔다."
    # SOURCE CH06 L3339
    narrator "우리 부스는 이제 운영을 끝냈지만, 캠퍼스 곳곳에서는 여전히 축제가 이어지고 있었다."
    # SOURCE CH06 L3342 주인공 · 혼잣말
    mc "……정말 끝나는구나."
    # SOURCE CH06 L3346
    narrator "조금 전까지는 이 시간이 끝나지 않았으면 좋겠다고 생각했다."
    # SOURCE CH06 L3348
    narrator "그런데 이제는 다른 생각이 들었다."
    # SOURCE CH06 L3350
    narrator "축제는 끝나도."
    # SOURCE CH06 L3352
    narrator "우리가 만나는 것까지 끝날 필요는 없지 않을까."
    # CONTI SOURCE CH06 L3354 [FADE OUT]
    # SOURCE CH06 L3356 [FLAG] `ch06_festival_operation_finished = True`
    $ story_flag("ch06_festival_operation_finished", True)
    # CONTI SOURCE CH06 L3358 [SCENE 06 END]
    jump ch06_sc07

label ch06_sc07:
    $ phone_timeline_enter("CH06", "ch06_sc07")
    # SOURCE CH06 L3360 끝이라는 말이 이상해서
    # SOURCE CH06 L3362 [BG] 주인공 방 · 다음 날 오전
    $ story_draft_scene("주인공 방 · 다음 날 오전")
    # SOURCE CH06 L3364 [BGM] Quiet Morning
    $ story_draft_bgm("Quiet Morning")
    # CONTI SOURCE CH06 L3366 [FADE IN]
    # SOURCE CH06 L3370
    narrator "축제가 끝났다."
    # SOURCE CH06 L3372
    narrator "어제 그렇게 시끄럽던 캠퍼스가 거짓말처럼 조용했다."
    # SOURCE CH06 L3374
    narrator "아침부터 울리던 단체 채팅방도 오늘은 별다른 메시지가 없었다."
    # SOURCE CH06 L3376
    narrator "……아니, 정확히는 있었다."
    # CONTI SOURCE CH06 L3378 [SFX] 휴대전화 알림
    # CONTI SOURCE CH06 L3380 [UI] 축제 준비팀 (6)
    $ story_chat(True, title="축제 준비팀")
    $ phone_threads["campus_group"]["title"] = "축제 준비팀"
    # SOURCE CH06 L3383 다림
    darim "다들 어제 정말 고생 많으셨어요."
    # SOURCE CH06 L3385 다림
    darim "오늘 한 시에 마지막 정리 모임 진행할게요."
    # SOURCE CH06 L3388 시아
    sia "마지막이라니"
    # SOURCE CH06 L3390 시아
    sia "뭔가 슬픈데"
    # SOURCE CH06 L3393 오므
    omu "니 어제는 끝났다고 좋아했잖아"
    # SOURCE CH06 L3396 시아
    sia "그건 어제고"
    # SOURCE CH06 L3399 하린
    lumi "참 일관성이 없으시네요."
    # SOURCE CH06 L3402 시아
    sia "사람 마음이 원래 그런 거야"
    # SOURCE CH06 L3405 로만
    roman "앗,,, 오늘도 다 같이 보는 거죠……?"
    # SOURCE CH06 L3408 다림
    darim "네. 오늘 정산하고 남은 자료 정리하면 끝이에요."
    # SOURCE CH06 L3412
    narrator "마지막 모임."
    # SOURCE CH06 L3414
    narrator "그 단어가 조금 낯설게 느껴졌다."
    # SOURCE CH06 L3417 주인공 · 혼잣말
    narrator "……이제 진짜 끝인가."
    # SOURCE CH06 L3421
    narrator "나는 가방을 챙겼다."
    # SOURCE CH06 L3423
    narrator "늘 가던 길인데 오늘은 조금 다른 기분이었다."
    # CONTI SOURCE CH06 L3425 [TRANSITION] 오후 1:00
    $ phone_timeline_cue("CH06", "CH06_L3425")
    $ story_chat(False)
    # SOURCE CH06 L3427 [BG] 공동 동아리실 · 낮
    $ story_draft_scene("공동 동아리실 · 낮", cast=["roman", "sia", "darim", "omu", "lumi"], standing=True)
    # COMMON STANDING BEGIN CH06 L3427
    $ story_stage_fade_in(["roman", "sia", "darim", "omu", "lumi"])
    # COMMON STANDING END CH06 L3427
    # SOURCE CH06 L3429 [BGM] Warm Memories
    $ story_draft_bgm("Warm Memories")
    # SOURCE CH06 L3433
    narrator "문을 열자 모두가 모여 있었다."
    # SOURCE CH06 L3435
    narrator "처음과 달리 누구도 어색하게 인사하지 않았다."
    # SOURCE CH06 L3438 시아
    # COMMON STANDING BEGIN CH06 L3438
    $ story_stage(faces={"sia": "happy"})
    # COMMON STANDING END CH06 L3438
    sia "오, 왔다!"
    # SOURCE CH06 L3441 오므
    omu "니 오늘은 일찍 왔네."
    # SOURCE CH06 L3444 시아
    sia "야, 나 원래 시간 잘 지키거든?"
    # SOURCE CH06 L3447 하린
    lumi "그럼 지난 몇 주간은 다른 분이셨나 봐요."
    # SOURCE CH06 L3450 시아
    sia "하린아!"
    # SOURCE CH06 L3453 주인공
    mc "안녕하세요. 오늘도 시끄럽네요."
    # SOURCE CH06 L3456 시아
    sia "야, 이제 이 정도는 익숙하잖아."
    # SOURCE CH06 L3459 주인공
    mc "네. 너무 익숙해졌어요."
    # SOURCE CH06 L3462 로만
    roman "후후……."
    # SOURCE CH06 L3465 다림
    # COMMON STANDING BEGIN CH06 L3465
    $ story_stage(faces={"darim": "serious"})
    # COMMON STANDING END CH06 L3465
    darim "자, 그럼 마지막으로 확인할게요."
    # SOURCE CH06 L3469
    narrator "다림 선배는 정산 자료를 펼쳤다."
    # SOURCE CH06 L3472 다림
    darim "운영본부에 반납할 물품은 모두 확인했고, 비용 정산도 끝났어요."
    # SOURCE CH06 L3474 다림
    darim "방문객 기록 중 공개에 동의한 자료는 정해진 보관 기준에 따라 정리하고, 나머지는 처리할 예정이에요."
    # SOURCE CH06 L3477 주인공
    mc "누락된 건 없나요?"
    # SOURCE CH06 L3480 다림
    darim "네. 저희가 확인할 수 있는 부분은 전부 점검했어요."
    # SOURCE CH06 L3483 하린
    lumi "부스 자재도 반납했고요."
    # SOURCE CH06 L3486 오므
    omu "사진은 공유 가능한 것만 따로 정리했다."
    # SOURCE CH06 L3489 시아
    sia "영상도 최종본 남겨뒀어."
    # SOURCE CH06 L3492 로만
    roman "앗,,, 질문 카드도 정리했어요……!"
    # SOURCE CH06 L3496
    narrator "이제 정말 남은 일이 없었다."
    # SOURCE CH06 L3498
    narrator "그런데 다림 선배는 자료를 덮고도 한동안 말을 하지 않았다."
    # SOURCE CH06 L3501 시아
    sia "……선배?"
    # SOURCE CH06 L3504 다림
    darim "……아."
    # SOURCE CH06 L3506 다림
    darim "이제 공식적으로 프로젝트가 끝났네요."
    # SOURCE CH06 L3510
    narrator "잠시 조용해졌다."
    # SOURCE CH06 L3513 로만
    # COMMON STANDING BEGIN CH06 L3513
    $ story_stage(faces={"roman": "sad", "sia": "sad", "darim": "sad", "omu": "serious", "lumi": "serious"})
    # COMMON STANDING END CH06 L3513
    roman "……끝났네요."
    # SOURCE CH06 L3516 오므
    omu "진짜 오래 준비했는데."
    # SOURCE CH06 L3519 하린
    lumi "그러게요."
    # SOURCE CH06 L3522 시아
    sia "야, 근데."
    # SOURCE CH06 L3525 시아
    sia "우리 이제 안 모이는 거냐?"
    # SOURCE CH06 L3528 다림
    darim "프로젝트 회의는 없겠죠."
    # SOURCE CH06 L3531 시아
    sia "……아."
    # SOURCE CH06 L3535
    narrator "시아가 조금 아쉬운 표정을 지었다."
    # SOURCE CH06 L3537
    narrator "그런데 그때 하린 선배가 웃으며 말했다."
    # SOURCE CH06 L3540 하린
    # COMMON STANDING BEGIN CH06 L3540
    $ story_stage(faces={"lumi": "happy"})
    # COMMON STANDING END CH06 L3540
    lumi "그렇다고 못 만나는 건 아니잖아요."
    # SOURCE CH06 L3543 오므
    omu "맞지."
    # SOURCE CH06 L3546 로만
    roman "앗,,, 저도 가끔 보고 싶어요."
    # SOURCE CH06 L3549 다림
    darim "후후. 다들 시간 맞으면 만나면 되죠."
    # SOURCE CH06 L3552 시아
    sia "……맞네."
    # SOURCE CH06 L3554 시아
    sia "야, 그럼 다음에는 진짜 일 말고 놀자."
    # SOURCE CH06 L3557 주인공
    mc "좋아요. 저도 그러고 싶어요."
    # SOURCE CH06 L3560 시아
    sia "오케이. 약속했다."
    # SOURCE CH06 L3564
    narrator "나는 웃었다."
    # SOURCE CH06 L3566
    narrator "왠지 조금 안심됐다."
    # SOURCE CH06 L3568
    narrator "프로젝트는 끝났지만, 우리 관계까지 끝나는 건 아니었다."
    # CONTI SOURCE CH06 L3570 [SFX] 문 두드리는 소리
    # SOURCE CH06 L3573 협합
    # COMMON STANDING BEGIN CH06 L3573
    $ story_offscreen_actor = "hyeophap"
    # COMMON STANDING END CH06 L3573
    hyeophap "잠깐 들어가도 돼?"
    # SOURCE CH06 L3576 다림
    # COMMON STANDING BEGIN CH06 L3576
    $ story_offscreen_actor = None
    # COMMON STANDING END CH06 L3576
    darim "네. 들어오세요."
    # SOURCE CH06 L3580
    narrator "협합이 문을 열었다."
    # SOURCE CH06 L3582
    # COMMON STANDING BEGIN CH06 L3582
    $ story_enter("ski", side="right", face="happy")
    $ story_enter("hyeophap", side="right", face="normal")
    $ story_enter("hess", side="right", face="normal")
    $ story_enter("bambam", side="right", face="happy")
    # COMMON STANDING END CH06 L3582
    narrator "뒤에는 스키, 헤스, 밤밤이 있었다."
    # SOURCE CH06 L3585 스키
    ski "야! 너희도 마지막 모임이냐?"
    # SOURCE CH06 L3588 시아
    sia "응. 너희도?"
    # SOURCE CH06 L3591 협합
    hyeophap "우리도 방금 정리 끝났어."
    # SOURCE CH06 L3594 밤밤
    bambam "다들 정말 고생 많으셨어요."
    # SOURCE CH06 L3597 헤스
    hess "축제 끝나니까 조용하네요."
    # SOURCE CH06 L3600 스키
    ski "뭐, 내 활약 덕분에 축제가 빛났지."
    # SOURCE CH06 L3603 협합
    hyeophap "방금까지는 멀쩡했는데."
    # SOURCE CH06 L3606 오므
    omu "끝나자마자 돌아왔네."
    # SOURCE CH06 L3609 시아
    # COMMON STANDING BEGIN CH06 L3609
    $ story_stage(faces={"sia": "smug"})
    # COMMON STANDING END CH06 L3609
    sia "야, 스키."
    # SOURCE CH06 L3612 스키
    ski "왜?"
    # SOURCE CH06 L3615 시아
    sia "다음에 또 경쟁하자."
    # SOURCE CH06 L3618 스키
    ski "……."
    # SOURCE CH06 L3620 스키
    # COMMON STANDING BEGIN CH06 L3620
    $ story_stage(faces={"ski": "happy"})
    # COMMON STANDING END CH06 L3620
    ski "좋지."
    # SOURCE CH06 L3623 스키
    ski "그때는 내가 완전히 이길 거야."
    # SOURCE CH06 L3626 시아
    sia "응 아니야~"
    # SOURCE CH06 L3629 헤스
    hess "아직 행사도 안 정해졌는데요."
    # SOURCE CH06 L3632 밤밤
    bambam "그래도 재미있겠네요."
    # SOURCE CH06 L3635 협합
    hyeophap "다음에는 좀 덜 시끄러우면 좋겠는데."
    # SOURCE CH06 L3639
    # COMMON STANDING BEGIN CH06 L3639
    $ story_stage(faces={"roman": "happy", "sia": "happy", "darim": "happy", "omu": "happy", "lumi": "happy", "ski": "happy", "hyeophap": "happy", "hess": "happy", "bambam": "happy"})
    # COMMON STANDING END CH06 L3639
    narrator "모두 웃었다."
    # SOURCE CH06 L3641
    narrator "스키와 시아는 마지막까지 티격태격했고, 협합은 그 둘을 말리려다 포기했다."
    # SOURCE CH06 L3643
    narrator "헤스와 밤밤은 익숙하다는 듯 그 모습을 바라봤다."
    # SOURCE CH06 L3645
    narrator "……이 사람들도 이제 꽤 익숙해졌다."
    # CONTI SOURCE CH06 L3647 [시간 경과 · 오후 2:10]
    $ phone_timeline_cue("CH06", "CH06_L3647")
    # SOURCE CH06 L3649 [BG] 공동 동아리실 · 빈 테이블
    $ story_draft_scene("공동 동아리실 · 빈 테이블", cast=["roman", "sia", "darim", "omu", "lumi"], standing=True)
    # COMMON STANDING BEGIN CH06 L3649
    $ story_stage_fade_in(["roman", "sia", "darim", "omu", "lumi"])
    # COMMON STANDING END CH06 L3649
    # SOURCE CH06 L3651 [BGM] Nostalgic Campus
    $ story_draft_bgm("Nostalgic Campus")
    # SOURCE CH06 L3655
    narrator "라이벌 팀이 먼저 떠나고, 우리도 짐을 정리했다."
    # SOURCE CH06 L3657
    narrator "테이블 위에는 더 이상 일정표가 펼쳐져 있지 않았다."
    # SOURCE CH06 L3659
    narrator "시아의 콘티도, 로만의 질문 카드도, 오므의 사진도 없었다."
    # SOURCE CH06 L3661
    narrator "하린 선배의 모형과 다림 선배의 운영 자료도 모두 정리되어 있었다."
    # SOURCE CH06 L3663
    narrator "처음 이곳에 왔던 날이 떠올랐다."
    # SOURCE CH06 L3665
    narrator "그때는 누가 누구인지도 몰랐고."
    # SOURCE CH06 L3667
    narrator "어떤 일을 하게 될지도 몰랐다."
    # SOURCE CH06 L3669
    narrator "그런데 지금은……"
    # SOURCE CH06 L3672 시아
    sia "야, [player_name]."
    # SOURCE CH06 L3675 주인공
    mc "네?"
    # SOURCE CH06 L3678 시아
    sia "다음에 뭐 할 거냐?"
    # SOURCE CH06 L3681 주인공
    mc "글쎄요. 밀린 과제부터 해야 하지 않을까요?"
    # SOURCE CH06 L3684 시아
    sia "와, 현실적인 대답."
    # SOURCE CH06 L3687 오므
    omu "그게 정상이지."
    # SOURCE CH06 L3690 다림
    darim "저도 과제가 좀 밀려 있어서요."
    # SOURCE CH06 L3693 로만
    roman "앗,,, 저도 책 읽어야 해요……."
    # SOURCE CH06 L3696 하린
    lumi "저는 작업실에 다시 가야겠네요."
    # SOURCE CH06 L3699 시아
    # COMMON STANDING BEGIN CH06 L3699
    $ story_stage(faces={"sia": "sad"})
    # COMMON STANDING END CH06 L3699
    sia "……."
    # SOURCE CH06 L3701 시아
    sia "다들 바쁘네."
    # SOURCE CH06 L3704 주인공
    mc "그래도 시간 맞추면 또 만날 수 있잖아요."
    # SOURCE CH06 L3707 시아
    sia "……그치?"
    # SOURCE CH06 L3710 주인공
    mc "네."
    # SOURCE CH06 L3714
    # COMMON STANDING BEGIN CH06 L3714
    $ story_stage(faces={"sia": "happy"})
    # COMMON STANDING END CH06 L3714
    narrator "시아가 웃었다."
    # SOURCE CH06 L3716
    narrator "그 모습을 보니 나도 조금 웃음이 났다."
    # SOURCE CH06 L3718 [BG] 캠퍼스 산책로 · 오후
    $ story_draft_scene("캠퍼스 산책로 · 오후")
    # SOURCE CH06 L3722
    narrator "마지막 인사를 나누고 동아리실을 나왔다."
    # SOURCE CH06 L3724
    narrator "다들 각자의 방향으로 걸어갔다."
    # SOURCE CH06 L3726
    narrator "로만은 도서관 쪽으로."
    # SOURCE CH06 L3728
    narrator "시아는 애니메이션학과 건물로."
    # SOURCE CH06 L3730
    narrator "다림 선배는 강의동으로."
    # SOURCE CH06 L3732
    narrator "오므는 카메라를 들고 광장으로."
    # SOURCE CH06 L3734
    narrator "하린 선배는 건축학과 작업실로."
    # SOURCE CH06 L3736
    narrator "나는 그 모습을 잠시 바라봤다."
    # SOURCE CH06 L3738
    narrator "……이제 다들 자기 일상으로 돌아가는구나."
    # SOURCE CH06 L3740
    narrator "그런데 조금 전의 약속이 떠올랐다."
    # SOURCE CH06 L3742
    narrator "다음에는 일 말고 만나자고 했던 말."
    # SOURCE CH06 L3744
    narrator "그 말이 생각보다 반가웠다."
    # CONTI SOURCE CH06 L3746 [SFX] 휴대전화 알림
    # CONTI SOURCE CH06 L3748 [UI] 축제 준비팀 (6)
    $ story_chat(True, title="축제 준비팀")
    $ phone_threads["campus_group"]["title"] = "축제 준비팀"
    # SOURCE CH06 L3751 시아
    sia "야 다들"
    # SOURCE CH06 L3753 시아
    sia "우리 단톡방은 안 없애는 거지?"
    # SOURCE CH06 L3756 오므
    omu "왜 없애는데"
    # SOURCE CH06 L3759 다림
    darim "그대로 두면 되죠. 후후."
    # SOURCE CH06 L3762 로만
    roman "앗,,, 저도 좋을 것 같아요……!"
    # SOURCE CH06 L3765 하린
    lumi "그럼 앞으로는 축제 준비팀이 아니라 그냥 친구들 단톡방이네요."
    # SOURCE CH06 L3768 시아
    sia "오"
    # SOURCE CH06 L3770 시아
    sia "그럼 이름 바꾸자"
    # CONTI SOURCE CH06 L3772 [UI] 단체 채팅방 이름 변경
    # CONTI SOURCE CH06 L3774 [CHAT TITLE] 「축제 준비팀」 → 「우리 사이」
    $ story_chat_title = "우리 사이"
    $ phone_threads["campus_group"]["title"] = "우리 사이"
    # SOURCE CH06 L3777 시아
    sia "어때"
    # SOURCE CH06 L3780 오므
    omu "갑자기 감성적이네"
    # SOURCE CH06 L3783 시아
    sia "나 원래 감성적이거든"
    # SOURCE CH06 L3786 하린
    lumi "이름은 괜찮네요."
    # SOURCE CH06 L3789 다림
    darim "후후. 저도 마음에 들어요."
    # SOURCE CH06 L3792 로만
    roman "앗,,, 예뻐요……!"
    # SOURCE CH06 L3796
    narrator "새로운 이름이 화면에 표시됐다."
    # SOURCE CH06 L3798
    narrator "「우리 사이」"
    # SOURCE CH06 L3800
    narrator "짧은 두 글자였다."
    # SOURCE CH06 L3802
    narrator "그런데 왠지 오래 바라보게 됐다."
    # SOURCE CH06 L3805 주인공 · 혼잣말
    narrator "……우리 사이."
    # SOURCE CH06 L3809
    narrator "처음에는 우연히 만난 사람들이었다."
    # SOURCE CH06 L3811
    narrator "축제 때문에 함께했고, 그 과정에서 조금씩 가까워졌다."
    # SOURCE CH06 L3813
    narrator "그리고 이제는."
    # SOURCE CH06 L3815
    narrator "함께할 이유를 스스로 만들 수 있는 사람들이 되었다."
    # SOURCE CH06 L3817
    narrator "나는 채팅창을 열었다."
    # SOURCE CH06 L3820 주인공 · 메시지
    mc "저도 마음에 들어요. 다음에 다 같이 또 만나요."
    # SOURCE CH06 L3823 시아
    sia "당연하지ㅋㅋ"
    # SOURCE CH06 L3826 오므
    omu "어. 다음에 보자"
    # SOURCE CH06 L3829 다림
    darim "후후. 시간 맞춰봐요."
    # SOURCE CH06 L3832 로만
    roman "앗,,, 좋아요!"
    # SOURCE CH06 L3835 하린
    lumi "그럼 다음 모임도 기대할게요."
    # CONTI SOURCE CH06 L3837 [UI] 스마트폰 화면 종료
    $ story_chat(False)
    # SOURCE CH06 L3841
    narrator "나는 휴대전화를 주머니에 넣었다."
    # SOURCE CH06 L3843
    narrator "축제는 끝났다."
    # SOURCE CH06 L3845
    narrator "그런데 이상하게도 무언가 시작되는 기분이었다."
    # SOURCE CH06 L3847
    narrator "누군가와 함께하는 시간이 기다려지고."
    # SOURCE CH06 L3849
    narrator "그 사람의 작은 메시지 하나에도 웃게 되고."
    # SOURCE CH06 L3851
    narrator "다음에 만날 이유를 찾게 되는 것."
    # SOURCE CH06 L3853
    narrator "아직은 그 마음을 정확히 설명할 수 없다."
    # SOURCE CH06 L3855
    narrator "하지만 이제는 알고 싶었다."
    # SOURCE CH06 L3857
    narrator "이 관계가 어디까지 이어질 수 있을지."
    # CONTI SOURCE CH06 L3859 [FADE TO BLACK]
    # SOURCE CH06 L3861 [BGM] CH06 Ending Theme
    $ story_draft_bgm("CH06 Ending Theme")
    # CONTI SOURCE CH06 L3863 [TEXT/PLAN] 「CHAPTER 06 COMPLETE」
    # CONTI SOURCE CH06 L3865 [TEXT/PLAN] 「다음 이야기」
    # CONTI SOURCE CH06 L3867 [TEXT/PLAN] 「우리 사이, 그 이상의 시작」
    # SOURCE CH06 L3869 [FLAG] `chapter06_complete = True`
    $ story_complete_chapter(6)
    # CONTI SOURCE CH06 L3871 [NEXT] CHAPTER 07 · 공통 루트 최종장
    # CONTI SOURCE CH06 L3873 [SCENE 07 END]
    jump chapter07
