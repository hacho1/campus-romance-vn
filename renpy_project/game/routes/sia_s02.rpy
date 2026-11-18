# Sia S02 · confirmed manuscript, text-first storyboard
# SOURCE: design_docs/story_sources/sia_s02.txt
# SHA256: 3a539c6a47f644bb49d1090a21874c8ca9cbca9f8c26b7f985c90d304770a17c
# Rebuild only these two route files: tools/import_sia_first.py --write
# LD/SD/CG directions remain comments until the artwork pass.

default sia_s02_rhythm_game_win = False
default sia_s02_cat_name = None
default sia_s02_cat_prize_obtained = False
default sia_s02_photo_taken = False
default sia_serious_side_seen = False
default sia_s02_jealousy_seen = False
default sia_s02_complete = False
default sia_s02_date_complete = False

label sia_s02:
    $ phone_timeline_enter("S02", "sia_s02")
    $ sia_begin_episode("S02", "너랑 있으면 이상하게 재밌어")
    jump sia_s02_sc01

label sia_s02_sc01:
    $ phone_timeline_enter("S02", "sia_s02_sc01")
    # SOURCE S02 L29 SCENE 01. 오늘은 내가 이긴다
    # SOURCE S02 L31 [BG] 주인공 방 · 토요일 오전
    $ sia_draft_scene("주인공 방 · 토요일 오전")
    # SOURCE S02 L33 [BGM] Playful Morning
    $ story_draft_bgm("Playful Morning")
    # SOURCE S02 L35 # CONTI [FADE IN]
    # SOURCE S02 L39
    narrator "토요일."
    # SOURCE S02 L41
    narrator "오늘은 오랜만에 과제도, 축제 준비도 없는 날이다."
    # SOURCE S02 L43
    narrator "그런데 해야 할 일이 하나 있다."
    # SOURCE S02 L45
    narrator "……아니, 해야 할 일이라기보다는."
    # SOURCE S02 L47
    narrator "누군가와의 약속이다."
    # SOURCE S02 L49 # CONTI [SFX] 휴대전화 진동
    # SOURCE S02 L51 # CONTI [UI] 시아 개인 메시지
    $ story_chat(True, title="시아")
    # SOURCE S02 L54 (시아)
    sia "야"
    # SOURCE S02 L56 (시아)
    sia "일어났냐"
    # SOURCE S02 L59 (주인공 · 메시지)
    mc "네. 일어났어요."
    # SOURCE S02 L62 (시아)
    sia "좋아"
    # SOURCE S02 L64 (시아)
    sia "오늘 무슨 날인지 알지?"
    # SOURCE S02 L67 (주인공 · 메시지)
    mc "토요일이요."
    # SOURCE S02 L70 (시아)
    sia "……."
    # SOURCE S02 L72 (시아)
    sia "야"
    # SOURCE S02 L74 (시아)
    sia "그걸 물어본 게 아니잖아ㅋㅋㅋ"
    # SOURCE S02 L77 (주인공 · 메시지)
    mc "게임센터 가는 날이요."
    # SOURCE S02 L80 (시아)
    sia "정답"
    # SOURCE S02 L82 (시아)
    sia "오늘은 내가 너를 완전히 박살 내주겠어"
    # SOURCE S02 L85 (주인공 · 메시지)
    mc "아직 무슨 게임을 할지도 안 정했는데요."
    # SOURCE S02 L88 (시아)
    sia "그건 중요하지 않아"
    # SOURCE S02 L90 (시아)
    sia "천재는 장르를 가리지 않거든"
    # SOURCE S02 L93 (주인공 · 메시지)
    mc "그럼 지셔도 변명은 없으시겠네요."
    # SOURCE S02 L96 (시아)
    sia "……."
    # SOURCE S02 L98 (시아)
    sia "야 너 요즘 말빨 많이 늘었다?"
    # SOURCE S02 L102
    narrator "메시지를 읽으면서 웃음이 났다."
    # SOURCE S02 L104
    narrator "시아 씨와 이야기하면 항상 이런 식이다."
    # SOURCE S02 L106
    narrator "뭔가 대단한 승부를 벌이는 것처럼 말하지만, 사실 그냥 같이 놀러 가는 거다."
    # SOURCE S02 L108
    narrator "그런데."
    # SOURCE S02 L110
    narrator "요즘은 그런 약속이 조금 더 기다려진다."
    # SOURCE S02 L112 # CONTI [UI] 추가 메시지
    # SOURCE S02 L115 (시아)
    sia "아무튼 두 시에 역 앞 게임센터"
    # SOURCE S02 L117 (시아)
    sia "늦으면 패배 처리임"
    # SOURCE S02 L120 (주인공 · 메시지)
    mc "알겠어요. 시아 씨도 늦지 마세요."
    # SOURCE S02 L123 (시아)
    sia "야 나 오늘 절대 안 늦거든?"
    # SOURCE S02 L126 (주인공 · 메시지)
    mc "그럼 먼저 도착하시는 쪽이 1점 받는 걸로 할까요?"
    # SOURCE S02 L129 (시아)
    sia "……."
    # SOURCE S02 L132 (시아)
    sia "그런 규칙은 없었잖아!"
    # SOURCE S02 L136
    narrator "……이미 패배를 예상한 건가."
    # SOURCE S02 L138
    narrator "나는 웃으며 휴대전화를 내려놓았다."
    # SOURCE S02 L140 # CONTI [TRANSITION] 오후 1:50
    $ phone_timeline_cue("S02", "S02_L140")
    $ story_chat(False)
    # SOURCE S02 L142 [BG] 역 앞 번화가 · 오후
    $ sia_draft_scene("역 앞 번화가 · 오후")
    # SOURCE S02 L144 [BGM] City Afternoon
    $ story_draft_bgm("City Afternoon")
    # SOURCE S02 L148
    narrator "약속 장소에 도착했다."
    # SOURCE S02 L150
    narrator "주말이라 거리는 평소보다 북적였다."
    # SOURCE S02 L152
    narrator "게임센터 앞에는 친구끼리 놀러 온 사람들과 연인들이 보였다."
    # SOURCE S02 L154
    narrator "……연인들."
    # SOURCE S02 L156
    narrator "괜히 그쪽에 시선이 갔다."
    # SOURCE S02 L159 (주인공 · 혼잣말)
    mc "……뭔 생각을 하는 거야."
    # SOURCE S02 L161 # CONTI [SFX] 발소리
    # SOURCE S02 L164 (시아)
    sia "야아아!"
    # SOURCE S02 L168
    narrator "익숙한 목소리가 들렸다."
    # SOURCE S02 L170
    narrator "고개를 돌리자 시아 씨가 손을 흔들며 다가오고 있었다."
    # SOURCE S02 L172 # CONTI [LD] 시아 · 자신만만한 표정
    # SOURCE S02 L175 (시아)
    sia "봐라!"
    # SOURCE S02 L177 (시아)
    sia "나 안 늦었지?"
    # SOURCE S02 L180 (주인공)
    mc "네. 약속 시간보다 일찍 오셨네요."
    # SOURCE S02 L183 (시아)
    sia "당연하지."
    # SOURCE S02 L185 (시아)
    sia "오늘은 승부의 날이니까."
    # SOURCE S02 L188 (주인공)
    mc "저도 일찍 왔는데요?"
    # SOURCE S02 L191 (시아)
    sia "……."
    # SOURCE S02 L193 (시아)
    sia "몇 분?"
    # SOURCE S02 L196 (주인공)
    mc "한 5분쯤요."
    # SOURCE S02 L199 (시아)
    sia "……아."
    # SOURCE S02 L203
    narrator "시아 씨가 잠시 굳었다."
    # SOURCE S02 L206 (시아)
    sia "야, 그럼 너한테 1점 주는 거 취소."
    # SOURCE S02 L209 (주인공)
    mc "왜요?"
    # SOURCE S02 L212 (시아)
    sia "내가 만든 규칙 아니거든."
    # SOURCE S02 L215 (주인공)
    mc "시아 씨가 만드신 규칙도 아니잖아요."
    # SOURCE S02 L218 (시아)
    sia "그러니까 취소라고ㅋㅋㅋ"
    # SOURCE S02 L222
    narrator "시아 씨는 웃으며 게임센터 쪽을 가리켰다."
    # SOURCE S02 L225 (시아)
    sia "자, 들어가자."
    # SOURCE S02 L228 (시아)
    sia "오늘은 봐주는 거 없다?"
    # SOURCE S02 L231 (주인공)
    mc "저도 최선을 다할게요."
    # SOURCE S02 L234 (시아)
    sia "오호."
    # SOURCE S02 L236 (시아)
    sia "그 자신감 언제까지 가나 보자."
    # SOURCE S02 L240
    narrator "그렇게 우리의 첫 번째 게임센터 승부가 시작됐다."
    # SOURCE S02 L242 # CONTI [SCENE 01 END]
    jump sia_s02_sc02

label sia_s02_sc02:
    $ phone_timeline_enter("S02", "sia_s02_sc02")
    # SOURCE S02 L246 SCENE 02. 천재의 첫 번째 패배
    # SOURCE S02 L248 [BG] 게임센터 내부 · 오후
    $ sia_draft_scene("게임센터 내부 · 오후")
    # SOURCE S02 L250 [BGM] Arcade Fun
    $ story_draft_bgm("Arcade Fun")
    # SOURCE S02 L252 # CONTI [SFX] 오락실 기계음, 사람들의 웃음소리
    # SOURCE S02 L256
    narrator "게임센터 안은 여러 게임의 소리로 가득했다."
    # SOURCE S02 L258
    narrator "리듬 게임 기계 앞에는 사람들이 줄을 서 있었고, 안쪽에는 레이싱 게임과 인형 뽑기 기계가 놓여 있었다."
    # SOURCE S02 L260
    narrator "시아 씨는 주변을 둘러보더니 한 기계 앞에서 걸음을 멈췄다."
    # SOURCE S02 L263 (시아)
    sia "좋아."
    # SOURCE S02 L265 (시아)
    sia "첫 번째 종목은 이거다."
    # SOURCE S02 L268 (주인공)
    mc "리듬 게임이요?"
    # SOURCE S02 L271 (시아)
    sia "응."
    # SOURCE S02 L274 (시아)
    sia "나 이거 좀 하거든."
    # SOURCE S02 L277 (주인공)
    mc "어느 정도로 잘하세요?"
    # SOURCE S02 L280 (시아)
    sia "……."
    # SOURCE S02 L283 (시아)
    sia "설명하면 길어."
    # SOURCE S02 L286 (주인공)
    mc "그렇게 잘하시는군요."
    # SOURCE S02 L289 (시아)
    sia "후후."
    # SOURCE S02 L291 (시아)
    sia "드디어 내 실력을 알아보는군."
    # SOURCE S02 L295
    narrator "……아직 실력을 본 적도 없는데."
    # SOURCE S02 L297 [BG] 리듬 게임 기계 앞
    $ sia_draft_scene("리듬 게임 기계 앞")
    # SOURCE S02 L300 (시아)
    sia "자, 규칙은 간단해."
    # SOURCE S02 L302 (시아)
    sia "점수 높은 사람이 승리."
    # SOURCE S02 L305 (주인공)
    mc "좋아요."
    # SOURCE S02 L308 (시아)
    sia "진 사람은 이긴 사람 소원 하나 들어주기."
    # SOURCE S02 L311 (주인공)
    mc "소원이요?"
    # SOURCE S02 L314 (시아)
    sia "응."
    # SOURCE S02 L316 (시아)
    sia "너무 어려운 건 말고."
    # SOURCE S02 L319 (주인공)
    mc "그럼 음료수 사주기 정도로 할까요?"
    # SOURCE S02 L322 (시아)
    sia "뭐야, 너무 평범한데?"
    # SOURCE S02 L325 (주인공)
    mc "그럼 시아 씨는 뭘 생각하셨어요?"
    # SOURCE S02 L328 (시아)
    sia "음……."
    # SOURCE S02 L330 (시아)
    sia "천재 작가님이라고 세 번 부르기?"
    # SOURCE S02 L333 (주인공)
    mc "……그걸로 만족하세요?"
    # SOURCE S02 L336 (시아)
    sia "당연하지."
    # SOURCE S02 L340
    narrator "정말 돈이 안 드는 사람이다."
    # SOURCE S02 L342
    narrator "……아니, 그건 아닌가."
    # SOURCE S02 L344 # CONTI [SFX] 게임 시작
    $ refresh_sfx("game_start")
    # SOURCE S02 L348
    narrator "음악이 시작됐다."
    # SOURCE S02 L350
    narrator "처음에는 시아 씨가 여유롭게 버튼을 눌렀다."
    # SOURCE S02 L352
    narrator "그런데 곡이 빨라지자 표정이 조금씩 바뀌었다."
    # SOURCE S02 L355 (시아)
    sia "……어?"
    # SOURCE S02 L358 (주인공)
    mc "왜 그러세요?"
    # SOURCE S02 L361 (시아)
    sia "아니, 잠깐."
    # SOURCE S02 L363 (시아)
    sia "이 부분 원래 이렇게 빨랐나?"
    # SOURCE S02 L367
    narrator "시아 씨의 손이 바빠졌다."
    # SOURCE S02 L369
    narrator "나는 화면에 집중했다."
    # SOURCE S02 L371 # CONTI [SFX] 게임 종료
    # SOURCE S02 L373 # CONTI [UI] GAME RESULT
    # SOURCE S02 L377
    narrator "결과가 화면에 나타났다."
    # SOURCE S02 L379
    narrator "내 점수가 시아 씨보다 조금 높았다."
    # SOURCE S02 L381
    narrator "……이겼네?"
    # SOURCE S02 L384 (시아)
    sia "……."
    # SOURCE S02 L387 (주인공)
    mc "제가 이겼네요."
    # SOURCE S02 L390 (시아)
    sia "……."
    # SOURCE S02 L393 (주인공)
    mc "시아 씨?"
    # SOURCE S02 L396 (시아)
    sia "……기계가 이상한데?"
    # SOURCE S02 L400
    narrator "나왔다."
    # SOURCE S02 L403 (주인공)
    mc "아까는 장르를 가리지 않는다고 하셨잖아요."
    # SOURCE S02 L406 (시아)
    sia "그건 맞는데."
    # SOURCE S02 L409 (시아)
    sia "오늘 내 손이 좀 덜 풀렸어."
    # SOURCE S02 L412 (주인공)
    mc "그럼 다시 하실래요?"
    # SOURCE S02 L415 (시아)
    sia "당연하지!"
    # SOURCE S02 L417 # CONTI [시간 경과 · 오후 2:25]
    $ phone_timeline_cue("S02", "S02_L417")
    # SOURCE S02 L419 # CONTI [SFX] 게임 종료
    # SOURCE S02 L423
    narrator "두 번째 판도 내가 이겼다."
    # SOURCE S02 L426 (시아)
    sia "……."
    # SOURCE S02 L429 (주인공)
    mc "이번에는 손 풀리셨나요?"
    # SOURCE S02 L432 (시아)
    sia "야."
    # SOURCE S02 L434 (시아)
    sia "그 말투 좀 킹받는데?"
    # SOURCE S02 L437 (주인공)
    mc "제가 뭐라고 했는데요?"
    # SOURCE S02 L440 (시아)
    sia "ㅋㅋㅋㅋ 진짜."
    # SOURCE S02 L442 # CONTI [SD EVENT] `sia_s02_arcade_defeat`
    # SOURCE S02 L444 # CONTI [연출] 패배한 점수판 앞에서 억울하게 항의하는 시아를 그린 완성형 SD 1장. 주인공은 화면 밖. 게임 기계나 점수판에 특정 게임 브랜드는 사용하지 않는다.
    # SOURCE S02 L447 (시아)
    sia "좋아."
    # SOURCE S02 L449 (시아)
    sia "이번에는 종목 변경이다."
    # SOURCE S02 L452 (주인공)
    mc "도망가시는 건가요?"
    # SOURCE S02 L455 (시아)
    sia "전략적 후퇴거든!"
    # SOURCE S02 L459
    narrator "나는 결국 웃음을 터뜨렸다."
    # SOURCE S02 L461
    narrator "시아 씨도 조금 웃더니 나를 노려보는 척했다."
    # SOURCE S02 L464 (시아)
    sia "야, 근데."
    # SOURCE S02 L467 (주인공)
    mc "네?"
    # SOURCE S02 L470 (시아)
    sia "너 생각보다 잘하네."
    # SOURCE S02 L473 (주인공)
    mc "감사해요."
    # SOURCE S02 L476 (시아)
    sia "아, 칭찬하는 게 아닌데."
    # SOURCE S02 L479 (주인공)
    mc "그럼 취소하실 건가요?"
    # SOURCE S02 L482 (시아)
    sia "……."
    # SOURCE S02 L484 (시아)
    sia "아냐."
    # SOURCE S02 L486 (시아)
    sia "이번에는 인정해주지."
    # SOURCE S02 L490
    narrator "시아 씨는 손을 내밀었다."
    # SOURCE S02 L493 (시아)
    sia "다음에는 안 진다."
    # SOURCE S02 L496 (주인공)
    mc "저도 다음 승부 기대할게요."
    # SOURCE S02 L500
    narrator "가볍게 손을 마주쳤다."
    # SOURCE S02 L502
    narrator "시아 씨는 곧바로 다른 기계 쪽으로 걸어갔다."
    # SOURCE S02 L505 (시아)
    sia "자, 다음은 인형 뽑기다!"
    # SOURCE S02 L508 (주인공)
    mc "이번에도 점수 대결인가요?"
    # SOURCE S02 L511 (시아)
    sia "아니."
    # SOURCE S02 L513 (시아)
    sia "이번에는 협동이다."
    # SOURCE S02 L517
    narrator "……벌써 방식을 바꾸네."
    # SOURCE S02 L520 (시아)
    sia "왜."
    # SOURCE S02 L522 (시아)
    sia "같이 하는 것도 재밌잖아."
    # SOURCE S02 L526
    narrator "그 말에 나는 잠깐 웃었다."
    # SOURCE S02 L528
    narrator "……맞는 말이긴 하다."
    # SOURCE S02 L530 [FLAG] `sia_s02_rhythm_game_win = True`
    $ story_flag("sia_s02_rhythm_game_win", True)
    # SOURCE S02 L532 # CONTI [SCENE 02 END]
    jump sia_s02_sc03

label sia_s02_sc03:
    $ phone_timeline_enter("S02", "sia_s02_sc03")
    # SOURCE S02 L536 SCENE 03. 이건 반칙 아니냐?
    # SOURCE S02 L538 # CONTI [TIME] 오후 2:45 · 인형 뽑기 코너 · 둘 사이의 거리
    $ phone_timeline_cue("S02", "S02_L538")
    # SOURCE S02 L540 # CONTI [HEADING] S02 SC03 · 이건 반칙 아니냐?
    # SOURCE S02 L542 [BG] 게임센터 인형 뽑기 코너 · 오후
    $ sia_draft_scene("게임센터 인형 뽑기 코너 · 오후")
    # SOURCE S02 L544 [BGM] Playful Arcade
    $ story_draft_bgm("Playful Arcade")
    # SOURCE S02 L548
    narrator "시아 씨가 향한 곳에는 작은 인형 뽑기 기계들이 줄지어 있었다."
    # SOURCE S02 L550
    narrator "그중 하나에 유독 시선이 갔다."
    # SOURCE S02 L552
    narrator "작은 고양이 인형이 들어 있는 기계였다."
    # SOURCE S02 L555 (시아)
    sia "오."
    # SOURCE S02 L557 (시아)
    sia "이거 귀여운데?"
    # SOURCE S02 L560 (주인공)
    mc "고양이 인형이네요."
    # SOURCE S02 L563 (시아)
    sia "응."
    # SOURCE S02 L565 (시아)
    sia "저 표정 봐."
    # SOURCE S02 L569
    narrator "인형은 눈을 반쯤 감고 있었다."
    # SOURCE S02 L571
    narrator "어딘가 세상을 귀찮아하는 듯한 표정이었다."
    # SOURCE S02 L574 (주인공)
    mc "시아 씨랑 조금 닮았는데요?"
    # SOURCE S02 L577 (시아)
    sia "……뭐?"
    # SOURCE S02 L580 (주인공)
    mc "눈매가요."
    # SOURCE S02 L583 (시아)
    sia "야!"
    # SOURCE S02 L585 (시아)
    sia "나 저렇게 생겼냐?"
    # SOURCE S02 L588 (주인공)
    mc "아니요. 느낌이 조금 비슷해서요."
    # SOURCE S02 L591 (시아)
    sia "……."
    # SOURCE S02 L594 (시아)
    sia "그럼 내가 뽑아주지."
    # SOURCE S02 L598
    narrator "……왜 그렇게 되는 거지?"
    # SOURCE S02 L601 (시아)
    sia "자, 잘 봐라."
    # SOURCE S02 L603 (시아)
    sia "천재의 인형 뽑기 실력."
    # SOURCE S02 L605 # CONTI [SFX] 동전 투입
    # SOURCE S02 L609
    narrator "시아 씨는 조이스틱을 움직였다."
    # SOURCE S02 L611
    narrator "집게가 내려갔다."
    # SOURCE S02 L613
    narrator "고양이 인형의 머리를 살짝 건드렸다."
    # SOURCE S02 L615
    narrator "그리고 그대로 올라왔다."
    # SOURCE S02 L617 # CONTI [SFX] 실패 효과음
    $ refresh_sfx("game_fail")
    # SOURCE S02 L620 (시아)
    sia "……."
    # SOURCE S02 L623 (주인공)
    mc "조금 아쉽네요."
    # SOURCE S02 L626 (시아)
    sia "아직 첫판이잖아."
    # SOURCE S02 L628 # CONTI [시간 경과 · 세 번째 시도]
    # SOURCE S02 L630 # CONTI [SFX] 실패 효과음
    $ refresh_sfx("game_fail")
    # SOURCE S02 L633 (시아)
    sia "……야."
    # SOURCE S02 L636 (주인공)
    mc "네?"
    # SOURCE S02 L639 (시아)
    sia "이거 집게가 너무 약한데?"
    # SOURCE S02 L642 (주인공)
    mc "그러게요."
    # SOURCE S02 L645 (시아)
    sia "이건 기계 문제야."
    # SOURCE S02 L648 (주인공)
    mc "혹시 이번에도요?"
    # SOURCE S02 L651 (시아)
    sia "……."
    # SOURCE S02 L654 (시아)
    sia "너 오늘 진짜 나 놀리려고 작정했냐?"
    # SOURCE S02 L658
    narrator "나는 웃었다."
    # SOURCE S02 L661 (주인공)
    mc "그럼 이번에는 제가 해볼게요."
    # SOURCE S02 L664 (시아)
    sia "오?"
    # SOURCE S02 L666 (시아)
    sia "좋아. 해봐."
    # SOURCE S02 L669 (시아)
    sia "근데 너도 실패하면 같이 놀릴 거야."
    # SOURCE S02 L672 (주인공)
    mc "그건 조금 불공평한데요?"
    # SOURCE S02 L675 (시아)
    sia "세상은 원래 불공평해."
    # SOURCE S02 L679
    narrator "……정말 당당하다."
    # SOURCE S02 L681 # CONTI [SFX] 동전 투입
    # SOURCE S02 L685
    narrator "나는 조이스틱을 움직였다."
    # SOURCE S02 L687
    narrator "집게를 고양이 인형 바로 위에 맞췄다."
    # SOURCE S02 L689 # CONTI [SFX] 집게 작동
    # SOURCE S02 L691
    narrator "인형이 살짝 들렸다."
    # SOURCE S02 L694 (시아)
    sia "오오오!"
    # SOURCE S02 L698
    narrator "그런데 출구에 도착하기 전에 인형이 떨어졌다."
    # SOURCE S02 L700 # CONTI [SFX] 실패 효과음
    $ refresh_sfx("game_fail")
    # SOURCE S02 L703 (시아)
    sia "ㅋㅋㅋㅋㅋ"
    # SOURCE S02 L705 (시아)
    sia "야! 너도 못하네!"
    # SOURCE S02 L708 (주인공)
    mc "아깝네요."
    # SOURCE S02 L711 (시아)
    sia "아, 이거 진짜 아깝다."
    # SOURCE S02 L715
    narrator "시아 씨는 화면을 들여다봤다."
    # SOURCE S02 L717
    narrator "그러더니 갑자기 나를 불렀다."
    # SOURCE S02 L720 (시아)
    sia "야, 잠깐."
    # SOURCE S02 L723 (주인공)
    mc "네?"
    # SOURCE S02 L726 (시아)
    sia "이번에는 내가 방향 봐줄게."
    # SOURCE S02 L729 (주인공)
    mc "좋아요."
    # SOURCE S02 L732 (시아)
    sia "조금 왼쪽."
    # SOURCE S02 L735 (주인공)
    mc "이 정도요?"
    # SOURCE S02 L738 (시아)
    sia "아니, 조금만 더."
    # SOURCE S02 L742
    narrator "시아 씨는 기계 화면을 가까이 들여다봤다."
    # SOURCE S02 L744
    narrator "나도 조이스틱을 움직이려고 화면에 집중했다."
    # SOURCE S02 L746
    narrator "그런데 순간 시아 씨의 얼굴이 생각보다 가까이 있었다."
    # SOURCE S02 L748
    narrator "……어?"
    # SOURCE S02 L751 (시아)
    sia "아니, 거기 말고……."
    # SOURCE S02 L755
    narrator "시아 씨가 고개를 돌렸다."
    # SOURCE S02 L757
    narrator "그리고 우리 눈이 마주쳤다."
    # SOURCE S02 L760 (시아)
    sia "……."
    # SOURCE S02 L763 (주인공)
    mc "……."
    # SOURCE S02 L767
    narrator "정말 잠깐이었다."
    # SOURCE S02 L769
    narrator "그런데 시아 씨가 먼저 고개를 돌렸다."
    # SOURCE S02 L771 # CONTI [표정] 시아 · 옅은 홍조
    # SOURCE S02 L774 (시아)
    sia "……야!"
    # SOURCE S02 L777 (주인공)
    mc "네?"
    # SOURCE S02 L780 (시아)
    sia "너무 가까워!"
    # SOURCE S02 L783 (주인공)
    mc "시아 씨가 먼저 가까이 오셨잖아요."
    # SOURCE S02 L786 (시아)
    sia "……."
    # SOURCE S02 L788 (시아)
    sia "그건……."
    # SOURCE S02 L792
    narrator "시아 씨의 말이 끊겼다."
    # SOURCE S02 L794
    narrator "평소라면 바로 반박했을 텐데."
    # SOURCE S02 L796
    narrator "이번에는 조금 달랐다."
    # SOURCE S02 L799 (시아)
    sia "아, 됐어."
    # SOURCE S02 L801 (시아)
    sia "일단 뽑기나 해!"
    # SOURCE S02 L805
    narrator "나는 다시 화면을 바라봤다."
    # SOURCE S02 L807
    narrator "……이상하다."
    # SOURCE S02 L809
    narrator "방금 시아 씨도 조금 당황한 것 같았는데."
    # SOURCE S02 L811 # CONTI [SFX] 집게 작동
    # SOURCE S02 L815
    narrator "시아 씨의 안내대로 움직인 집게가 인형을 들어 올렸다."
    # SOURCE S02 L817
    narrator "이번에는 출구까지 거의 다 왔다."
    # SOURCE S02 L820 (시아)
    sia "오오! 제발!"
    # SOURCE S02 L822 # CONTI [SFX] 인형 획득 효과음
    $ refresh_sfx("game_clear")
    # SOURCE S02 L826
    narrator "고양이 인형이 출구 안으로 떨어졌다."
    # SOURCE S02 L829 (시아)
    sia "됐다아아!"
    # SOURCE S02 L832 (주인공)
    mc "성공했네요!"
    # SOURCE S02 L835 (시아)
    sia "봤지?!"
    # SOURCE S02 L837 (시아)
    sia "이게 바로 팀워크라는 거다!"
    # SOURCE S02 L841
    narrator "시아 씨는 신나게 웃었다."
    # SOURCE S02 L843
    narrator "나는 인형을 꺼냈다."
    # SOURCE S02 L845
    narrator "작고 말랑한 회색 고양이 인형이었다."
    # SOURCE S02 L848 (주인공)
    mc "자, 시아 씨."
    # SOURCE S02 L851 (시아)
    sia "어?"
    # SOURCE S02 L854 (주인공)
    mc "시아 씨가 갖고 싶어 하셨잖아요."
    # SOURCE S02 L857 (시아)
    sia "……."
    # SOURCE S02 L861
    narrator "시아 씨는 인형을 바라봤다."
    # SOURCE S02 L864 (시아)
    sia "아니, 같이 뽑았는데."
    # SOURCE S02 L867 (주인공)
    mc "그래도 처음부터 시아 씨가 마음에 들어 하셨으니까요."
    # SOURCE S02 L870 (시아)
    sia "……."
    # SOURCE S02 L873 (시아)
    sia "야, 너."
    # SOURCE S02 L876 (주인공)
    mc "네?"
    # SOURCE S02 L879 (시아)
    sia "이런 건 좀……."
    # SOURCE S02 L883
    narrator "시아 씨는 잠시 말을 고르더니 웃었다."
    # SOURCE S02 L886 (시아)
    sia "……고맙다."
    # SOURCE S02 L890
    narrator "평소와 달리 짧고 조용한 대답이었다."
    # SOURCE S02 L893 (주인공)
    mc "별말씀을요."
    # SOURCE S02 L896 (시아)
    sia "……."
    # SOURCE S02 L899 (시아)
    sia "근데 이거 나 닮았다고 했지?"
    # SOURCE S02 L902 (주인공)
    mc "네. 조금요."
    # SOURCE S02 L905 (시아)
    sia "그럼 이름은 네가 지어."
    # SOURCE S02 L908 (주인공)
    mc "제가요?"
    # SOURCE S02 L911 (시아)
    sia "응. 같이 뽑았잖아."
    # SOURCE S02 L915
    narrator "나는 인형을 다시 바라봤다."
    # SOURCE S02 L917 [CHOICE 01 · 고양이 인형 이름]
    menu:
        # SOURCE S02 L919 선택지
        "천재냥은 어떠세요?":
            # SOURCE S02 L922 (주인공)
            mc "천재냥은 어떠세요?"
            # SOURCE S02 L925 (시아)
            sia "……."
            # SOURCE S02 L927 (시아)
            sia "야."
            # SOURCE S02 L929 (시아)
            sia "너 진짜 천재냐?"
            # SOURCE S02 L932 (주인공)
            mc "시아 씨가 천재라고 하시니까요."
            # SOURCE S02 L935 (시아)
            sia "ㅋㅋㅋㅋ"
            # SOURCE S02 L937 (시아)
            sia "좋아. 채택!"
            # SOURCE S02 L939 [FLAG] `sia_s02_cat_name = "천재냥"`
            $ story_apply("sia_s02_choice01_a", values={'sia_s02_cat_name': '천재냥'})
        # SOURCE S02 L943 선택지
        "졸냥이는 어떠세요?":
            # SOURCE S02 L946 (주인공)
            mc "졸냥이는 어떠세요?"
            # SOURCE S02 L949 (시아)
            sia "왜?"
            # SOURCE S02 L952 (주인공)
            mc "항상 졸린 표정이라서요."
            # SOURCE S02 L955 (시아)
            sia "……."
            # SOURCE S02 L957 (시아)
            sia "야, 귀엽네."
            # SOURCE S02 L959 (시아)
            sia "채택!"
            # SOURCE S02 L961 [FLAG] `sia_s02_cat_name = "졸냥이"`
            $ story_apply("sia_s02_choice01_b", values={'sia_s02_cat_name': '졸냥이'})
        # SOURCE S02 L965 선택지
        "시아냥은 어떠세요?":
            # SOURCE S02 L968 (주인공)
            mc "시아냥은 어떠세요?"
            # SOURCE S02 L971 (시아)
            sia "……."
            # SOURCE S02 L973 (시아)
            sia "야!!"
            # SOURCE S02 L976 (주인공)
            mc "왜요?"
            # SOURCE S02 L979 (시아)
            sia "너 나 놀리는 거지?"
            # SOURCE S02 L982 (주인공)
            mc "귀여워서요."
            # SOURCE S02 L985 (시아)
            sia "……."
            # SOURCE S02 L987 (시아)
            sia "……아."
            # SOURCE S02 L991
            narrator "시아 씨가 잠깐 말을 잃었다."
            # SOURCE S02 L994 (시아)
            sia "……아, 진짜."
            # SOURCE S02 L996 (시아)
            sia "그럼 그렇게 해."
            # SOURCE S02 L998 [FLAG] `sia_s02_cat_name = "시아냥"`
            $ story_apply("sia_s02_choice01_c", values={'sia_s02_cat_name': '시아냥'})
    # SOURCE S02 L1003 (시아)
    sia "좋아."
    # SOURCE S02 L1005 (시아)
    sia "그럼 오늘의 전리품은 이 녀석이다."
    # SOURCE S02 L1009
    narrator "시아 씨는 인형을 품에 안았다."
    # SOURCE S02 L1011
    narrator "그런데 조금 전 가까이 마주 봤던 순간이 자꾸 생각났다."
    # SOURCE S02 L1013
    narrator "……왜 하필 그 장면이 기억에 남는 거지?"
    # SOURCE S02 L1015 [FLAG] `sia_s02_cat_prize_obtained = True`
    $ story_flag("sia_s02_cat_prize_obtained", True)
    # SOURCE S02 L1017 # CONTI [SCENE 03 END]
    jump sia_s02_sc04

label sia_s02_sc04:
    $ phone_timeline_enter("S02", "sia_s02_sc04")
    # SOURCE S02 L1021 SCENE 04. 오늘은 좀 다르게 보이네
    # SOURCE S02 L1023 # CONTI [TIME] 오후 3:35 · 셀프 포토부스 · 예상하지 못한 설렘
    $ phone_timeline_cue("S02", "S02_L1023")
    # SOURCE S02 L1025 # CONTI [HEADING] S02 SC04 · 오늘은 좀 다르게 보이네
    # SOURCE S02 L1027 [BG] 게임센터 인근 포토부스 거리 · 오후
    $ sia_draft_scene("게임센터 인근 포토부스 거리 · 오후")
    # SOURCE S02 L1029 [BGM] Light City Pop
    $ story_draft_bgm("Light City Pop")
    # SOURCE S02 L1033
    narrator "게임센터를 나왔을 때 시아 씨는 인형을 계속 품에 안고 있었다."
    # SOURCE S02 L1036 (주인공)
    mc "많이 마음에 드시나 봐요."
    # SOURCE S02 L1039 (시아)
    sia "당연하지."
    # SOURCE S02 L1041 (시아)
    sia "우리의 위대한 승리의 상징이잖아."
    # SOURCE S02 L1044 (주인공)
    mc "인형 하나인데요?"
    # SOURCE S02 L1047 (시아)
    sia "그 하나에 의미가 있는 거야."
    # SOURCE S02 L1051
    narrator "시아 씨는 고양이 인형의 머리를 톡톡 두드렸다."
    # SOURCE S02 L1053
    narrator "그러다가 무언가를 발견하고 걸음을 멈췄다."
    # SOURCE S02 L1056 (시아)
    sia "야, 저기!"
    # SOURCE S02 L1059 (주인공)
    mc "네?"
    # SOURCE S02 L1062 (시아)
    sia "사진 찍자."
    # SOURCE S02 L1066
    narrator "시아 씨가 가리킨 곳에는 셀프 포토부스가 있었다."
    # SOURCE S02 L1069 (주인공)
    mc "사진이요?"
    # SOURCE S02 L1072 (시아)
    sia "응."
    # SOURCE S02 L1074 (시아)
    sia "오늘 승리 기념."
    # SOURCE S02 L1077 (주인공)
    mc "리듬 게임은 제가 이겼는데요?"
    # SOURCE S02 L1080 (시아)
    sia "인형은 같이 뽑았잖아."
    # SOURCE S02 L1082 (시아)
    sia "그러니까 공동 승리."
    # SOURCE S02 L1086
    narrator "틀린 말은 아니었다."
    # SOURCE S02 L1088
    narrator "……그런데 왠지 다 시아 씨가 정한 기준 같다."
    # SOURCE S02 L1090 [BG] 셀프 포토부스 내부
    $ sia_draft_scene("셀프 포토부스 내부")
    # SOURCE S02 L1092 [BGM] Photo Booth Pop
    $ story_draft_bgm("Photo Booth Pop")
    # SOURCE S02 L1096
    narrator "부스 안은 생각보다 좁았다."
    # SOURCE S02 L1098
    narrator "화면에는 여러 프레임과 꾸미기 옵션이 표시되어 있었다."
    # SOURCE S02 L1100
    narrator "시아 씨는 익숙한 듯 메뉴를 넘겼다."
    # SOURCE S02 L1103 (시아)
    sia "오, 이거 봐."
    # SOURCE S02 L1105 (시아)
    sia "고양이 프레임 있다."
    # SOURCE S02 L1108 (주인공)
    mc "인형이랑 맞추기 좋겠네요."
    # SOURCE S02 L1111 (시아)
    sia "그치?"
    # SOURCE S02 L1115
    narrator "시아 씨는 고양이 인형을 가운데에 놓았다."
    # SOURCE S02 L1117
    narrator "그리고 내 옆에 섰다."
    # SOURCE S02 L1120 (시아)
    sia "자, 첫 번째는 정상적으로 찍자."
    # SOURCE S02 L1123 (주인공)
    mc "네."
    # SOURCE S02 L1125 # CONTI [SFX] 촬영 카운트다운
    # SOURCE S02 L1128 (시아)
    sia "하나, 둘……."
    # SOURCE S02 L1130 # CONTI [SFX] 카메라 셔터
    $ story_sfx("shutter")
    # SOURCE S02 L1134
    narrator "첫 번째 사진이 찍혔다."
    # SOURCE S02 L1136
    narrator "시아 씨는 화면을 확인했다."
    # SOURCE S02 L1139 (시아)
    sia "오."
    # SOURCE S02 L1141 (시아)
    sia "괜찮네."
    # SOURCE S02 L1144 (주인공)
    mc "그러네요."
    # SOURCE S02 L1147 (시아)
    sia "두 번째는 웃긴 표정."
    # SOURCE S02 L1150 (주인공)
    mc "갑자기요?"
    # SOURCE S02 L1153 (시아)
    sia "당연하지."
    # SOURCE S02 L1155 (시아)
    sia "추억은 다양해야 하거든."
    # SOURCE S02 L1159
    narrator "시아 씨는 얼굴을 잔뜩 찌푸리며 이상한 표정을 지었다."
    # SOURCE S02 L1161
    narrator "나도 비슷하게 따라 해봤다."
    # SOURCE S02 L1163 # CONTI [SFX] 카메라 셔터
    $ story_sfx("shutter")
    # SOURCE S02 L1166 (시아)
    sia "ㅋㅋㅋㅋㅋ"
    # SOURCE S02 L1168 (시아)
    sia "야, 이거 진짜 웃기다."
    # SOURCE S02 L1171 (주인공)
    mc "시아 씨 표정이 더 재미있는데요?"
    # SOURCE S02 L1174 (시아)
    sia "아니거든?"
    # SOURCE S02 L1178
    narrator "세 번째 사진을 준비할 때였다."
    # SOURCE S02 L1180
    narrator "시아 씨가 고양이 인형을 들어 올렸다."
    # SOURCE S02 L1183 (시아)
    sia "이번에는 얘랑 같이 찍자."
    # SOURCE S02 L1186 (주인공)
    mc "좋아요."
    # SOURCE S02 L1190
    narrator "인형이 화면을 가리지 않도록 서로 위치를 조정했다."
    # SOURCE S02 L1192
    narrator "그러다가 시아 씨가 내 옆으로 조금 더 가까이 왔다."
    # SOURCE S02 L1194
    narrator "어깨가 가볍게 닿았다."
    # SOURCE S02 L1197 (시아)
    sia "……."
    # SOURCE S02 L1200 (주인공)
    mc "괜찮으세요?"
    # SOURCE S02 L1203 (시아)
    sia "어?"
    # SOURCE S02 L1205 (시아)
    sia "아, 응."
    # SOURCE S02 L1209
    narrator "시아 씨는 화면을 바라봤다."
    # SOURCE S02 L1211
    narrator "그런데 이상하게 평소보다 조용했다."
    # SOURCE S02 L1213 # CONTI [SFX] 카메라 카운트다운
    # SOURCE S02 L1216 (안내 음성)
    sia_announcer "3, 2, 1."
    # SOURCE S02 L1219 (시아)
    sia "……야."
    # SOURCE S02 L1222 (주인공)
    mc "네?"
    # SOURCE S02 L1225 (시아)
    sia "웃어."
    # SOURCE S02 L1228 (주인공)
    mc "웃고 있는데요?"
    # SOURCE S02 L1231 (시아)
    sia "……."
    # SOURCE S02 L1233 (시아)
    sia "그러네."
    # SOURCE S02 L1235 # CONTI [SFX] 카메라 셔터
    $ story_sfx("shutter")
    # SOURCE S02 L1239
    narrator "사진이 찍혔다."
    # SOURCE S02 L1241
    narrator "시아 씨는 화면을 잠시 바라봤다."
    # SOURCE S02 L1244 (시아)
    sia "……."
    # SOURCE S02 L1247 (주인공)
    mc "잘 나왔어요?"
    # SOURCE S02 L1250 (시아)
    sia "……응."
    # SOURCE S02 L1254
    narrator "시아 씨는 고개를 끄덕였다."
    # SOURCE S02 L1256
    narrator "그리고 곧바로 장난스러운 표정으로 돌아왔다."
    # SOURCE S02 L1259 (시아)
    sia "자, 마지막은 내가 정한다!"
    # SOURCE S02 L1262 (주인공)
    mc "어떤 포즈인데요?"
    # SOURCE S02 L1265 (시아)
    sia "비밀."
    # SOURCE S02 L1269
    narrator "시아 씨는 고양이 인형을 내 쪽으로 내밀었다."
    # SOURCE S02 L1272 (시아)
    sia "자, 이거 들어."
    # SOURCE S02 L1275 (주인공)
    mc "네."
    # SOURCE S02 L1278 (시아)
    sia "그리고 나 따라 해."
    # SOURCE S02 L1282
    narrator "시아 씨가 손으로 고양이 귀 모양을 만들었다."
    # SOURCE S02 L1285 (주인공)
    mc "……고양이 포즈요?"
    # SOURCE S02 L1288 (시아)
    sia "응."
    # SOURCE S02 L1290 (시아)
    sia "오늘은 고양이의 날이거든."
    # SOURCE S02 L1293 (주인공)
    mc "처음 듣는 이야기인데요."
    # SOURCE S02 L1296 (시아)
    sia "방금 정했으니까."
    # SOURCE S02 L1300
    narrator "나는 결국 웃었다."
    # SOURCE S02 L1302 # CONTI [SFX] 카메라 셔터
    $ story_sfx("shutter")
    # SOURCE S02 L1304 # CONTI [UI] 촬영 완료
    # SOURCE S02 L1306 # CONTI [시간 경과 · 오후 3:55]
    $ phone_timeline_cue("S02", "S02_L1306")
    # SOURCE S02 L1308 [BG] 포토부스 밖 · 오후
    $ sia_draft_scene("포토부스 밖 · 오후")
    # SOURCE S02 L1312
    narrator "사진이 출력됐다."
    # SOURCE S02 L1314
    narrator "시아 씨는 두 장 중 한 장을 내게 건넸다."
    # SOURCE S02 L1317 (시아)
    sia "자, 네 거."
    # SOURCE S02 L1320 (주인공)
    mc "감사해요."
    # SOURCE S02 L1323 (시아)
    sia "잘 보관해라."
    # SOURCE S02 L1326 (주인공)
    mc "네. 소중히 보관할게요."
    # SOURCE S02 L1329 (시아)
    sia "……."
    # SOURCE S02 L1333
    narrator "시아 씨가 잠시 나를 바라봤다."
    # SOURCE S02 L1336 (시아)
    sia "그렇게까지?"
    # SOURCE S02 L1339 (주인공)
    mc "네. 같이 찍은 사진이잖아요."
    # SOURCE S02 L1342 (시아)
    sia "……."
    # SOURCE S02 L1344 # CONTI [표정] 시아 · 순간적인 당황
    # SOURCE S02 L1347 (시아)
    sia "……아."
    # SOURCE S02 L1349 (시아)
    sia "그렇지."
    # SOURCE S02 L1353
    narrator "시아 씨는 사진을 내려다봤다."
    # SOURCE S02 L1355
    narrator "그리고 작은 목소리로 말했다."
    # SOURCE S02 L1358 (시아)
    sia "……나도."
    # SOURCE S02 L1361 (주인공)
    mc "네?"
    # SOURCE S02 L1364 (시아)
    sia "나도 잘 보관할 거라고."
    # SOURCE S02 L1368
    narrator "시아 씨는 사진을 가방에 넣었다."
    # SOURCE S02 L1370
    narrator "그러고는 다시 내 쪽을 바라봤다."
    # SOURCE S02 L1373 (시아)
    sia "야, 근데 다음에는 더 웃긴 거 찍자."
    # SOURCE S02 L1376 (주인공)
    mc "좋아요."
    # SOURCE S02 L1379 (시아)
    sia "이번엔 너도 먼저 포즈 생각해와."
    # SOURCE S02 L1382 (주인공)
    mc "숙제인가요?"
    # SOURCE S02 L1385 (시아)
    sia "응."
    # SOURCE S02 L1387 (시아)
    sia "다음 데이트 숙제."
    # SOURCE S02 L1391
    narrator "……데이트?"
    # SOURCE S02 L1393
    narrator "그 단어가 잠시 마음에 남았다."
    # SOURCE S02 L1395
    narrator "하지만 시아 씨는 아무렇지도 않게 앞서 걸었다."
    # SOURCE S02 L1397
    narrator "아마 그냥 평소처럼 말한 거겠지."
    # SOURCE S02 L1399
    narrator "그런데."
    # SOURCE S02 L1401
    narrator "나는 왜 그 말이 조금 반가웠을까."
    # SOURCE S02 L1403 # CONTI [CG 후보] 포토부스 내부에서 시아가 고양이 인형을 들고 웃는 장면. 주인공의 얼굴이나 체형은 표시하지 않고 시아를 중심으로 구성한다.
    # SOURCE S02 L1405 [FLAG] `sia_s02_photo_taken = True`
    $ story_flag("sia_s02_photo_taken", True)
    # SOURCE S02 L1407 # CONTI [SCENE 04 END]
    jump sia_s02_sc05

label sia_s02_sc05:
    $ phone_timeline_enter("S02", "sia_s02_sc05")
    # SOURCE S02 L1411 SCENE 05. 장난 아닌 질문 하나
    # SOURCE S02 L1413 # CONTI [TIME] 오후 5:20 · 학교 근처 식당 · 좋아한다는 감정에 관한 대화
    $ phone_timeline_cue("S02", "S02_L1413")
    # SOURCE S02 L1415 # CONTI [HEADING] S02 SC05 · 장난 아닌 질문 하나
    # SOURCE S02 L1417 [BG] 학교 근처 작은 식당 · 저녁
    $ sia_draft_scene("학교 근처 작은 식당 · 저녁")
    # SOURCE S02 L1419 [BGM] Cozy Evening
    $ story_draft_bgm("Cozy Evening")
    # SOURCE S02 L1423
    narrator "게임센터와 포토부스를 둘러본 뒤 우리는 저녁을 먹으러 갔다."
    # SOURCE S02 L1425
    narrator "시아 씨는 메뉴판을 보다가 한참 고민했다."
    # SOURCE S02 L1428 (시아)
    sia "야."
    # SOURCE S02 L1431 (주인공)
    mc "네?"
    # SOURCE S02 L1434 (시아)
    sia "오늘은 뭘 먹을까."
    # SOURCE S02 L1437 (주인공)
    mc "점심은 드셨어요?"
    # SOURCE S02 L1440 (시아)
    sia "응."
    # SOURCE S02 L1443 (시아)
    sia "근데 놀다 보니까 다시 배고파."
    # SOURCE S02 L1446 (주인공)
    mc "지난번에도 그러셨잖아요."
    # SOURCE S02 L1449 (시아)
    sia "그건 작업하느라 배고픈 거였고."
    # SOURCE S02 L1451 (시아)
    sia "오늘은 놀아서 배고픈 거야."
    # SOURCE S02 L1455
    narrator "결국 이유만 다르지 똑같이 배고픈 거잖아."
    # SOURCE S02 L1458 (주인공)
    mc "그럼 시아 씨가 드시고 싶은 걸로 정하세요."
    # SOURCE S02 L1461 (시아)
    sia "……."
    # SOURCE S02 L1464 (시아)
    sia "너는?"
    # SOURCE S02 L1467 (주인공)
    mc "저도 대부분 괜찮아요."
    # SOURCE S02 L1470 (시아)
    sia "야, 그런 게 제일 어려운 대답이거든."
    # SOURCE S02 L1474
    narrator "시아 씨는 결국 메뉴 두 개를 골랐다."
    # SOURCE S02 L1476
    narrator "우리는 음식을 주문하고 앉았다."
    # SOURCE S02 L1478 # CONTI [시간 경과 · 오후 5:40]
    $ phone_timeline_cue("S02", "S02_L1478")
    # SOURCE S02 L1481 (시아)
    sia "근데 오늘 진짜 재밌었다."
    # SOURCE S02 L1484 (주인공)
    mc "저도요."
    # SOURCE S02 L1487 (시아)
    sia "특히 네가 리듬 게임 잘하는 건 좀 의외였어."
    # SOURCE S02 L1490 (주인공)
    mc "그렇게 못할 것 같았나요?"
    # SOURCE S02 L1493 (시아)
    sia "아니, 그건 아닌데."
    # SOURCE S02 L1495 (시아)
    sia "좀 얌전하게 할 줄 알았거든."
    # SOURCE S02 L1498 (주인공)
    mc "게임할 때도 존댓말을 써야 하나요?"
    # SOURCE S02 L1501 (시아)
    sia "ㅋㅋㅋㅋ"
    # SOURCE S02 L1503 (시아)
    sia "야, 그건 너무 웃긴데?"
    # SOURCE S02 L1507
    narrator "시아 씨는 웃음을 터뜨렸다."
    # SOURCE S02 L1509
    narrator "그러다가 조금 조용해졌다."
    # SOURCE S02 L1512 (시아)
    sia "……야."
    # SOURCE S02 L1515 (주인공)
    mc "네?"
    # SOURCE S02 L1518 (시아)
    sia "너는 누군가랑 같이 있으면 뭐가 제일 좋아?"
    # SOURCE S02 L1522
    narrator "갑작스러운 질문이었다."
    # SOURCE S02 L1525 (주인공)
    mc "어떤 의미예요?"
    # SOURCE S02 L1528 (시아)
    sia "그냥."
    # SOURCE S02 L1530 (시아)
    sia "친구든 누구든."
    # SOURCE S02 L1532 (시아)
    sia "같이 놀 때 말이야."
    # SOURCE S02 L1535 (주인공)
    mc "음……."
    # SOURCE S02 L1539
    narrator "나는 잠시 생각했다."
    # SOURCE S02 L1542 (주인공)
    mc "편하게 이야기할 수 있는 게 좋은 것 같아요."
    # SOURCE S02 L1545 (시아)
    sia "편하게?"
    # SOURCE S02 L1548 (주인공)
    mc "네. 별것 아닌 말도 할 수 있고, 진지한 이야기도 할 수 있는 사이요."
    # SOURCE S02 L1551 (시아)
    sia "……."
    # SOURCE S02 L1555
    narrator "시아 씨는 컵을 천천히 내려놓았다."
    # SOURCE S02 L1558 (시아)
    sia "진지한 이야기도?"
    # SOURCE S02 L1561 (주인공)
    mc "네."
    # SOURCE S02 L1564 (시아)
    sia "……흠."
    # SOURCE S02 L1568
    narrator "시아 씨는 잠시 생각하다 웃었다."
    # SOURCE S02 L1571 (시아)
    sia "그럼 나랑은?"
    # SOURCE S02 L1574 (주인공)
    mc "시아 씨랑요?"
    # SOURCE S02 L1577 (시아)
    sia "응."
    # SOURCE S02 L1579 (시아)
    sia "나랑 있으면 어떠냐고."
    # SOURCE S02 L1583
    narrator "그 질문을 듣고 잠시 말을 골랐다."
    # SOURCE S02 L1585
    narrator "시아 씨는 장난스럽게 웃고 있었다."
    # SOURCE S02 L1587
    narrator "하지만 이번에는 내 대답을 기다리는 것 같았다."
    # SOURCE S02 L1589 [CHOICE 02 · 시아와 함께 있을 때]
    menu:
        # SOURCE S02 L1591 선택지
        "시아 씨랑 있으면 정말 재미있어요.":
            # SOURCE S02 L1594 (주인공)
            mc "시아 씨랑 있으면 정말 재미있어요."
            # SOURCE S02 L1596 (주인공)
            mc "별것 아닌 일도 특별해지는 느낌이에요."
            # SOURCE S02 L1599 (시아)
            sia "……."
            # SOURCE S02 L1601 (시아)
            sia "오."
            # SOURCE S02 L1603 (시아)
            sia "그거 꽤 높은 평가인데?"
            # SOURCE S02 L1606 (주인공)
            mc "네. 진심이에요."
            # SOURCE S02 L1609 (시아)
            sia "……."
            # SOURCE S02 L1611 (시아)
            sia "아, 진짜."
            # SOURCE S02 L1613 (시아)
            sia "너는 꼭 그렇게 덧붙이더라."
            # SOURCE S02 L1615 [FLAG] `sia_affection += 1`
            $ story_apply("sia_s02_choice02_a")
        # SOURCE S02 L1619 선택지
        "장난칠 때도 좋지만, 진지한 모습도 좋아요.":
            # SOURCE S02 L1622 (주인공)
            mc "시아 씨가 장난치실 때도 재미있지만, 진지하게 작품 이야기하실 때도 좋아요."
            # SOURCE S02 L1625 (시아)
            sia "……어?"
            # SOURCE S02 L1628 (주인공)
            mc "그때는 정말 멋있거든요."
            # SOURCE S02 L1631 (시아)
            sia "……."
            # SOURCE S02 L1633 # CONTI [표정] 시아 · 홍조
            # SOURCE S02 L1636 (시아)
            sia "야, 잠깐만."
            # SOURCE S02 L1638 (시아)
            sia "그건 좀……."
            # SOURCE S02 L1641 (주인공)
            mc "왜요?"
            # SOURCE S02 L1644 (시아)
            sia "……아니다."
            # SOURCE S02 L1646 (시아)
            sia "그냥 고맙다고."
            # SOURCE S02 L1648 [FLAG] `sia_affection += 2`
            # SOURCE S02 L1650 [FLAG] `sia_serious_side_seen = True`
            $ story_apply("sia_s02_choice02_b", values={'sia_serious_side_seen': True})
        # SOURCE S02 L1654 선택지
        "시아 씨라서 편한 것 같아요.":
            # SOURCE S02 L1657 (주인공)
            mc "저는 시아 씨라서 편한 것 같아요."
            # SOURCE S02 L1660 (시아)
            sia "……."
            # SOURCE S02 L1662 (시아)
            sia "뭐야, 그거."
            # SOURCE S02 L1665 (주인공)
            mc "시아 씨 앞에서는 별것 아닌 이야기도 편하게 할 수 있으니까요."
            # SOURCE S02 L1668 (시아)
            sia "……."
            # SOURCE S02 L1671 (시아)
            sia "……아."
            # SOURCE S02 L1673 (시아)
            sia "그건 좀 기분 좋네."
            # SOURCE S02 L1675 [FLAG] `sia_mutual_trust += 2`
            $ story_apply("sia_s02_choice02_c")
    # SOURCE S02 L1683
    narrator "시아 씨는 잠시 음료를 마셨다."
    # SOURCE S02 L1685
    narrator "평소 같으면 바로 장난을 쳤을 텐데."
    # SOURCE S02 L1687
    narrator "이번에는 조금 조용했다."
    # SOURCE S02 L1690 (주인공)
    mc "시아 씨는요?"
    # SOURCE S02 L1693 (시아)
    sia "어?"
    # SOURCE S02 L1696 (주인공)
    mc "저랑 있으면 어떠세요?"
    # SOURCE S02 L1699 (시아)
    sia "……."
    # SOURCE S02 L1703
    narrator "시아 씨가 잠시 멈췄다."
    # SOURCE S02 L1706 (시아)
    sia "야, 그걸 나한테 다시 물어보냐?"
    # SOURCE S02 L1709 (주인공)
    mc "시아 씨가 먼저 물어보셨잖아요."
    # SOURCE S02 L1712 (시아)
    sia "……."
    # SOURCE S02 L1714 (시아)
    sia "맞네."
    # SOURCE S02 L1718
    narrator "시아 씨는 잠깐 웃었다."
    # SOURCE S02 L1721 (시아)
    sia "나는……."
    # SOURCE S02 L1725
    narrator "말이 이어지지 않았다."
    # SOURCE S02 L1728 (시아)
    sia "……음."
    # SOURCE S02 L1730 (시아)
    sia "재밌지."
    # SOURCE S02 L1733 (주인공)
    mc "네."
    # SOURCE S02 L1736 (시아)
    sia "너랑 있으면 평소보다 좀 더 재밌어."
    # SOURCE S02 L1739 (주인공)
    mc "그럼 다행이네요."
    # SOURCE S02 L1742 (시아)
    sia "……근데."
    # SOURCE S02 L1745 (주인공)
    mc "네?"
    # SOURCE S02 L1748 (시아)
    sia "그게 좀 이상해."
    # SOURCE S02 L1752
    narrator "나는 시아 씨를 바라봤다."
    # SOURCE S02 L1755 (주인공)
    mc "왜 이상하세요?"
    # SOURCE S02 L1758 (시아)
    sia "……몰라."
    # SOURCE S02 L1761 (시아)
    sia "그냥."
    # SOURCE S02 L1763 (시아)
    sia "평소에도 다른 애들이랑 놀면 재미있거든."
    # SOURCE S02 L1766 (시아)
    sia "근데 너랑 놀 때는……."
    # SOURCE S02 L1770
    narrator "시아 씨가 잠시 말을 멈췄다."
    # SOURCE S02 L1773 (시아)
    sia "……아, 됐다."
    # SOURCE S02 L1776 (주인공)
    mc "네?"
    # SOURCE S02 L1779 (시아)
    sia "그냥 오늘 재미있었다고ㅋㅋ"
    # SOURCE S02 L1783
    narrator "시아 씨는 웃으며 말을 돌렸다."
    # SOURCE S02 L1785
    narrator "하지만 방금 하려던 말이 무엇인지 조금 궁금했다."
    # SOURCE S02 L1788 (주인공)
    mc "혹시 더 하실 말씀 있으세요?"
    # SOURCE S02 L1791 (시아)
    sia "……."
    # SOURCE S02 L1794 (시아)
    sia "나중에."
    # SOURCE S02 L1797 (주인공)
    mc "네?"
    # SOURCE S02 L1800 (시아)
    sia "나중에 말해줄게."
    # SOURCE S02 L1804
    narrator "시아 씨는 다시 웃었다."
    # SOURCE S02 L1806
    narrator "그런데 이번에는 조금 어색해 보였다."
    # SOURCE S02 L1808 # CONTI [SCENE 05 END]
    jump sia_s02_sc06

label sia_s02_sc06:
    $ phone_timeline_enter("S02", "sia_s02_sc06")
    # SOURCE S02 L1812 SCENE 06. 이상하게 신경 쓰이네
    # SOURCE S02 L1814 # CONTI [TIME] 오후 6:10 · 식당 밖 · 오므 등장과 감정 자각
    $ phone_timeline_cue("S02", "S02_L1814")
    # SOURCE S02 L1816 # CONTI [HEADING] S02 SC06 · 이상하게 신경 쓰이네
    # SOURCE S02 L1818 [BG] 학교 앞 거리 · 저녁
    $ sia_draft_scene("학교 앞 거리 · 저녁")
    # SOURCE S02 L1820 [BGM] Evening Walk
    $ story_draft_bgm("Evening Walk")
    # SOURCE S02 L1824
    narrator "저녁을 먹고 밖으로 나왔다."
    # SOURCE S02 L1826
    narrator "해가 조금씩 지고 있었다."
    # SOURCE S02 L1828
    narrator "시아 씨는 고양이 인형이 들어 있는 가방을 가볍게 흔들었다."
    # SOURCE S02 L1831 (시아)
    sia "오늘 진짜 알차게 놀았다."
    # SOURCE S02 L1834 (주인공)
    mc "그러게요."
    # SOURCE S02 L1837 (시아)
    sia "리듬 게임도 하고."
    # SOURCE S02 L1839 (시아)
    sia "인형도 뽑고."
    # SOURCE S02 L1841 (시아)
    sia "사진도 찍고."
    # SOURCE S02 L1844 (주인공)
    mc "시아 씨가 원하시던 건 거의 다 했네요."
    # SOURCE S02 L1847 (시아)
    sia "……그치."
    # SOURCE S02 L1851
    narrator "그때 익숙한 목소리가 들렸다."
    # SOURCE S02 L1854 (오므)
    omu "어?"
    # SOURCE S02 L1856 (오므)
    omu "시아 아이가?"
    # SOURCE S02 L1859 (시아)
    sia "오?"
    # SOURCE S02 L1861 (시아)
    sia "오므!"
    # SOURCE S02 L1865
    narrator "오므 씨가 카메라 가방을 메고 걸어오고 있었다."
    # SOURCE S02 L1868 (오므)
    omu "니 여기서 뭐 하노?"
    # SOURCE S02 L1871 (시아)
    sia "놀았지."
    # SOURCE S02 L1874 (오므)
    omu "누구랑?"
    # SOURCE S02 L1878
    narrator "시아 씨는 자연스럽게 나를 가리켰다."
    # SOURCE S02 L1881 (시아)
    sia "얘랑."
    # SOURCE S02 L1884 (주인공)
    mc "오므 씨, 안녕하세요."
    # SOURCE S02 L1887 (오므)
    omu "어. 안녕."
    # SOURCE S02 L1890 (오므)
    omu "둘이 같이 놀았나?"
    # SOURCE S02 L1893 (시아)
    sia "응."
    # SOURCE S02 L1895 (시아)
    sia "게임센터 갔다 왔어."
    # SOURCE S02 L1898 (오므)
    omu "오."
    # SOURCE S02 L1900 (오므)
    omu "재밌었겠다."
    # SOURCE S02 L1903 (시아)
    sia "당연하지."
    # SOURCE S02 L1906 (오므)
    omu "누가 이겼는데?"
    # SOURCE S02 L1909 (시아)
    sia "……."
    # SOURCE S02 L1913
    narrator "시아 씨가 잠깐 굳었다."
    # SOURCE S02 L1916 (주인공)
    mc "리듬 게임은 제가 이겼어요."
    # SOURCE S02 L1919 (시아)
    sia "야!"
    # SOURCE S02 L1922 (오므)
    omu "ㅋㅋㅋㅋ"
    # SOURCE S02 L1924 (오므)
    omu "시아 니 또 졌나?"
    # SOURCE S02 L1927 (시아)
    sia "아니, 오늘 컨디션이 좀……."
    # SOURCE S02 L1930 (오므)
    omu "그 말 고등학교 때도 했잖아."
    # SOURCE S02 L1933 (시아)
    sia "아 진짜ㅋㅋㅋ"
    # SOURCE S02 L1937
    narrator "오므 씨는 웃으며 시아 씨의 가방을 바라봤다."
    # SOURCE S02 L1940 (오므)
    omu "그거 뭐고?"
    # SOURCE S02 L1943 (시아)
    sia "아, 이거?"
    # SOURCE S02 L1946 (시아)
    sia "오늘 같이 뽑은 거."
    # SOURCE S02 L1950
    narrator "시아 씨는 고양이 인형을 꺼냈다."
    # SOURCE S02 L1953 (오므)
    omu "귀엽네."
    # SOURCE S02 L1956 (오므)
    omu "근데 니가 뽑았나?"
    # SOURCE S02 L1959 (시아)
    sia "둘이 같이."
    # SOURCE S02 L1962 (오므)
    omu "……오."
    # SOURCE S02 L1966
    narrator "오므 씨가 시아 씨를 잠시 바라봤다."
    # SOURCE S02 L1968
    narrator "그러더니 아주 작게 웃었다."
    # SOURCE S02 L1971 (오므)
    omu "그렇구나."
    # SOURCE S02 L1974 (시아)
    sia "……왜."
    # SOURCE S02 L1977 (오므)
    omu "아무것도 아니다."
    # SOURCE S02 L1981
    narrator "오므 씨는 카메라를 고쳐 멨다."
    # SOURCE S02 L1984 (오므)
    omu "아, [player_name] 씨."
    # SOURCE S02 L1987 (주인공)
    mc "네?"
    # SOURCE S02 L1990 (오므)
    omu "다음에 시간 되면 축제 때 찍은 사진도 같이 정리해볼래요?"
    # SOURCE S02 L1993 (주인공)
    mc "좋아요. 아직 정리할 게 많이 남았나요?"
    # SOURCE S02 L1996 (오므)
    omu "몇 장은 다시 골라보려고."
    # SOURCE S02 L1999 (주인공)
    mc "네. 시간 맞춰봐요."
    # SOURCE S02 L2002 (오므)
    omu "어. 좋다."
    # SOURCE S02 L2006
    narrator "별다른 의미 없는 약속이었다."
    # SOURCE S02 L2008
    narrator "축제 때 찍은 사진을 정리하는 일."
    # SOURCE S02 L2010
    narrator "그런데 옆에서 시아 씨가 갑자기 말을 꺼냈다."
    # SOURCE S02 L2013 (시아)
    sia "야, 오므."
    # SOURCE S02 L2016 (오므)
    omu "왜."
    # SOURCE S02 L2019 (시아)
    sia "너 사진 정리 아직 안 끝났냐?"
    # SOURCE S02 L2022 (오므)
    omu "어. 왜?"
    # SOURCE S02 L2025 (시아)
    sia "아니, 그냥."
    # SOURCE S02 L2028 (시아)
    sia "그럼 나도 나중에 볼래."
    # SOURCE S02 L2031 (오므)
    omu "니는 전에 다 봤잖아."
    # SOURCE S02 L2034 (시아)
    sia "……."
    # SOURCE S02 L2037 (시아)
    sia "다시 보면 되지!"
    # SOURCE S02 L2041
    narrator "오므 씨가 시아 씨를 바라봤다."
    # SOURCE S02 L2043
    narrator "그러더니 피식 웃었다."
    # SOURCE S02 L2046 (오므)
    omu "그래. 니도 와라."
    # SOURCE S02 L2049 (시아)
    sia "……응."
    # SOURCE S02 L2053
    narrator "그렇게 오므 씨와 헤어졌다."
    # SOURCE S02 L2055 # CONTI [시간 경과 · 오후 6:25]
    $ phone_timeline_cue("S02", "S02_L2055")
    # SOURCE S02 L2057 [BG] 캠퍼스 진입로 · 저녁
    $ sia_draft_scene("캠퍼스 진입로 · 저녁")
    # SOURCE S02 L2061
    narrator "우리는 다시 학교 쪽으로 걸었다."
    # SOURCE S02 L2063
    narrator "그런데 시아 씨가 조금 조용해졌다."
    # SOURCE S02 L2066 (주인공)
    mc "시아 씨?"
    # SOURCE S02 L2069 (시아)
    sia "응?"
    # SOURCE S02 L2072 (주인공)
    mc "무슨 생각하세요?"
    # SOURCE S02 L2075 (시아)
    sia "아니."
    # SOURCE S02 L2077 (시아)
    sia "그냥."
    # SOURCE S02 L2081
    narrator "시아 씨는 잠시 나를 바라봤다."
    # SOURCE S02 L2084 (시아)
    sia "너 오므랑도 친하지?"
    # SOURCE S02 L2087 (주인공)
    mc "네. 축제 준비하면서 친해졌잖아요."
    # SOURCE S02 L2090 (시아)
    sia "……그치."
    # SOURCE S02 L2094
    narrator "시아 씨는 고개를 끄덕였다."
    # SOURCE S02 L2097 (시아)
    sia "다림 선배랑도 친하고."
    # SOURCE S02 L2099 (시아)
    sia "하린이랑도 잘 지내잖아."
    # SOURCE S02 L2102 (주인공)
    mc "네. 다 좋은 분들이죠."
    # SOURCE S02 L2105 (시아)
    sia "……."
    # SOURCE S02 L2108 (시아)
    sia "그렇지."
    # SOURCE S02 L2112
    narrator "시아 씨는 잠시 말을 멈췄다."
    # SOURCE S02 L2114
    narrator "그러다가 갑자기 웃었다."
    # SOURCE S02 L2117 (시아)
    sia "야, 근데."
    # SOURCE S02 L2120 (주인공)
    mc "네?"
    # SOURCE S02 L2123 (시아)
    sia "오늘은 나랑 제일 오래 놀았지?"
    # SOURCE S02 L2126 (주인공)
    mc "그렇죠."
    # SOURCE S02 L2129 (시아)
    sia "그럼 됐어."
    # SOURCE S02 L2133
    narrator "……응?"
    # SOURCE S02 L2136 (주인공)
    mc "그게 중요한가요?"
    # SOURCE S02 L2139 (시아)
    sia "……."
    # SOURCE S02 L2142 (시아)
    sia "아니?"
    # SOURCE S02 L2144 (시아)
    sia "그냥 물어본 건데?"
    # SOURCE S02 L2148
    narrator "시아 씨는 고개를 돌렸다."
    # SOURCE S02 L2150
    narrator "그런데 귀 끝이 조금 붉어진 것 같았다."
    # SOURCE S02 L2153 (시아)
    sia "아, 진짜."
    # SOURCE S02 L2156 (주인공)
    mc "왜요?"
    # SOURCE S02 L2159 (시아)
    sia "그냥!"
    # SOURCE S02 L2163
    narrator "시아 씨는 조금 빠르게 걸었다."
    # SOURCE S02 L2165
    narrator "나는 그 옆으로 따라갔다."
    # SOURCE S02 L2167
    narrator "……이상하네."
    # SOURCE S02 L2169
    narrator "평소 같으면 오므 씨와도 같이 놀자고 먼저 말했을 텐데."
    # SOURCE S02 L2171
    narrator "오늘은 조금 다른 모습이었다."
    # SOURCE S02 L2173 [FLAG] `sia_s02_jealousy_seen = True`
    $ story_flag("sia_s02_jealousy_seen", True)
    # SOURCE S02 L2175 # CONTI [SCENE 06 END]
    jump sia_s02_sc07

label sia_s02_sc07:
    $ phone_timeline_enter("S02", "sia_s02_sc07")
    # SOURCE S02 L2179 SCENE 07. 조금만 더 놀다 가자
    # SOURCE S02 L2181 # CONTI [TIME] 오후 6:45 · 캠퍼스 산책로 · 둘만의 특별한 저녁
    $ phone_timeline_cue("S02", "S02_L2181")
    # SOURCE S02 L2183 # CONTI [HEADING] S02 SC07 · 조금만 더 놀다 가자
    # SOURCE S02 L2185 [BG] 캠퍼스 산책로 · 저녁
    $ sia_draft_scene("캠퍼스 산책로 · 저녁")
    # SOURCE S02 L2187 [BGM] Soft Evening
    $ story_draft_bgm("Soft Evening")
    # SOURCE S02 L2191
    narrator "학교에 도착할 무렵 하늘은 어두워져 있었다."
    # SOURCE S02 L2193
    narrator "가로등이 하나둘 켜지고 있었다."
    # SOURCE S02 L2195
    narrator "이제는 헤어질 시간이었다."
    # SOURCE S02 L2198 (주인공)
    mc "그럼 저는 이쪽으로 가볼게요."
    # SOURCE S02 L2201 (시아)
    sia "……어?"
    # SOURCE S02 L2204 (주인공)
    mc "시아 씨도 조심히 들어가세요."
    # SOURCE S02 L2207 (시아)
    sia "……."
    # SOURCE S02 L2211
    narrator "시아 씨는 잠시 나를 바라봤다."
    # SOURCE S02 L2213
    narrator "그러더니 갑자기 물었다."
    # SOURCE S02 L2216 (시아)
    sia "야."
    # SOURCE S02 L2219 (주인공)
    mc "네?"
    # SOURCE S02 L2222 (시아)
    sia "지금 바로 들어가야 하냐?"
    # SOURCE S02 L2225 (주인공)
    mc "아니요. 특별히 급한 일은 없는데요."
    # SOURCE S02 L2228 (시아)
    sia "……그럼."
    # SOURCE S02 L2232
    narrator "시아 씨는 잠시 주위를 둘러봤다."
    # SOURCE S02 L2235 (시아)
    sia "조금만 더 놀다 가자."
    # SOURCE S02 L2238 (주인공)
    mc "어디 가고 싶으세요?"
    # SOURCE S02 L2241 (시아)
    sia "음……."
    # SOURCE S02 L2244 (시아)
    sia "그냥 걸을까?"
    # SOURCE S02 L2248
    narrator "……시아 씨가 그냥 산책을 하자고?"
    # SOURCE S02 L2250
    narrator "조금 의외였다."
    # SOURCE S02 L2253 (주인공)
    mc "좋아요."
    # SOURCE S02 L2256 (시아)
    sia "오케이."
    # SOURCE S02 L2260
    narrator "우리는 산책로를 따라 걸었다."
    # SOURCE S02 L2262
    narrator "주변에는 학생들이 몇 명 지나가고 있었다."
    # SOURCE S02 L2264
    narrator "시아 씨는 처음에는 평소처럼 오늘 있었던 일을 이야기했다."
    # SOURCE S02 L2266
    narrator "리듬 게임에서 졌던 일."
    # SOURCE S02 L2268
    narrator "인형 뽑기에 성공했던 일."
    # SOURCE S02 L2270
    narrator "포토부스에서 찍었던 이상한 표정 이야기까지."
    # SOURCE S02 L2273 (시아)
    sia "야, 근데 그 사진은 절대 남한테 보여주지 마라."
    # SOURCE S02 L2276 (주인공)
    mc "왜요?"
    # SOURCE S02 L2279 (시아)
    sia "내 이미지 관리해야 하거든."
    # SOURCE S02 L2282 (주인공)
    mc "시아 씨가 직접 그렇게 찍으셨잖아요."
    # SOURCE S02 L2285 (시아)
    sia "그건 그렇지만!"
    # SOURCE S02 L2289
    narrator "시아 씨는 웃었다."
    # SOURCE S02 L2291
    narrator "그런데 조금 뒤에는 조용해졌다."
    # SOURCE S02 L2293 [BG] 캠퍼스 작은 공원 · 밤
    $ sia_draft_scene("캠퍼스 작은 공원 · 밤")
    # SOURCE S02 L2297
    narrator "우리는 작은 공원에 도착했다."
    # SOURCE S02 L2299
    narrator "벤치에 앉자 시아 씨는 고양이 인형을 꺼내 옆자리에 놓았다."
    # SOURCE S02 L2302 (시아)
    sia "……야."
    # SOURCE S02 L2305 (주인공)
    mc "네?"
    # SOURCE S02 L2308 (시아)
    sia "오늘 진짜 재미있었다."
    # SOURCE S02 L2311 (주인공)
    mc "저도요."
    # SOURCE S02 L2314 (시아)
    sia "근데 좀 이상해."
    # SOURCE S02 L2317 (주인공)
    mc "뭐가요?"
    # SOURCE S02 L2320 (시아)
    sia "그냥……."
    # SOURCE S02 L2323 (시아)
    sia "오늘 하루 종일 놀았잖아."
    # SOURCE S02 L2326 (주인공)
    mc "네."
    # SOURCE S02 L2329 (시아)
    sia "그러니까 이제 집에 가면 되거든?"
    # SOURCE S02 L2332 (주인공)
    mc "그렇죠."
    # SOURCE S02 L2335 (시아)
    sia "……근데."
    # SOURCE S02 L2339
    narrator "시아 씨는 손에 든 인형을 바라봤다."
    # SOURCE S02 L2342 (시아)
    sia "아직 좀 아쉬워."
    # SOURCE S02 L2346
    narrator "나는 잠시 시아 씨를 바라봤다."
    # SOURCE S02 L2349 (주인공)
    mc "그럼 다음에 또 놀면 되잖아요."
    # SOURCE S02 L2352 (시아)
    sia "……그렇긴 하지."
    # SOURCE S02 L2355 (주인공)
    mc "게임센터도 다시 갈 수 있고요."
    # SOURCE S02 L2358 (시아)
    sia "응."
    # SOURCE S02 L2361 (주인공)
    mc "포토부스도요."
    # SOURCE S02 L2364 (시아)
    sia "……응."
    # SOURCE S02 L2368
    narrator "시아 씨는 고개를 끄덕였다."
    # SOURCE S02 L2370
    narrator "그런데 표정은 아직 조금 복잡해 보였다."
    # SOURCE S02 L2373 (주인공)
    mc "시아 씨."
    # SOURCE S02 L2376 (시아)
    sia "왜."
    # SOURCE S02 L2379 (주인공)
    mc "오늘은 저도 헤어지기 조금 아쉬워요."
    # SOURCE S02 L2382 (시아)
    sia "……."
    # SOURCE S02 L2386
    narrator "시아 씨의 눈이 조금 커졌다."
    # SOURCE S02 L2389 (시아)
    sia "……뭐?"
    # SOURCE S02 L2392 (주인공)
    mc "시아 씨랑 있으면 정말 재미있거든요."
    # SOURCE S02 L2394 (주인공)
    mc "그래서 시간이 빨리 가는 것 같아요."
    # SOURCE S02 L2397 (시아)
    sia "……."
    # SOURCE S02 L2401
    narrator "시아 씨는 잠시 아무 말도 하지 않았다."
    # SOURCE S02 L2403
    narrator "평소라면 장난스럽게 받아쳤을 텐데."
    # SOURCE S02 L2405
    narrator "이번에는 고양이 인형만 바라봤다."
    # SOURCE S02 L2408 (시아)
    sia "야, 너……."
    # SOURCE S02 L2411 (주인공)
    mc "네?"
    # SOURCE S02 L2414 (시아)
    sia "그런 말 아무한테나 하고 다니지 마."
    # SOURCE S02 L2417 (주인공)
    mc "왜요?"
    # SOURCE S02 L2420 (시아)
    sia "……."
    # SOURCE S02 L2423 (시아)
    sia "아, 몰라!"
    # SOURCE S02 L2427
    narrator "시아 씨가 갑자기 고개를 돌렸다."
    # SOURCE S02 L2429
    narrator "그러다가 다시 나를 바라봤다."
    # SOURCE S02 L2432 (시아)
    sia "……아니다."
    # SOURCE S02 L2435 (시아)
    sia "그냥 해."
    # SOURCE S02 L2438 (주인공)
    mc "네?"
    # SOURCE S02 L2441 (시아)
    sia "아, 진짜."
    # SOURCE S02 L2444 (시아)
    sia "나도 내가 무슨 말 하는지 모르겠네."
    # SOURCE S02 L2448
    narrator "시아 씨는 어이없다는 듯 웃었다."
    # SOURCE S02 L2450
    narrator "나도 조금 웃었다."
    # SOURCE S02 L2452
    narrator "하지만 이제는 알 것 같았다."
    # SOURCE S02 L2454
    narrator "시아 씨도 오늘이 끝나는 게 아쉬운 모양이다."
    # SOURCE S02 L2457 (주인공)
    mc "그럼 다음에는 조금 더 오래 놀아요."
    # SOURCE S02 L2460 (시아)
    sia "……."
    # SOURCE S02 L2463 (시아)
    sia "……응."
    # SOURCE S02 L2467
    narrator "시아 씨는 작게 고개를 끄덕였다."
    # SOURCE S02 L2469
    narrator "그러더니 나를 바라봤다."
    # SOURCE S02 L2472 (시아)
    sia "근데 다음에는 네가 장소 정해."
    # SOURCE S02 L2475 (주인공)
    mc "제가요?"
    # SOURCE S02 L2478 (시아)
    sia "응."
    # SOURCE S02 L2480 (시아)
    sia "오늘은 내가 정했잖아."
    # SOURCE S02 L2483 (주인공)
    mc "좋아요."
    # SOURCE S02 L2486 (시아)
    sia "……그리고."
    # SOURCE S02 L2489 (주인공)
    mc "네?"
    # SOURCE S02 L2492 (시아)
    sia "다음에도……."
    # SOURCE S02 L2496
    narrator "시아 씨는 잠시 말을 멈췄다."
    # SOURCE S02 L2499 (시아)
    sia "……둘이서 놀자."
    # SOURCE S02 L2503
    narrator "그 말에 잠깐 심장이 빨리 뛰었다."
    # SOURCE S02 L2505
    narrator "……둘이서."
    # SOURCE S02 L2508 (주인공)
    mc "네. 저도 그러고 싶어요."
    # SOURCE S02 L2511 (시아)
    sia "……."
    # SOURCE S02 L2514 (시아)
    sia "……오케이."
    # SOURCE S02 L2518
    narrator "시아 씨는 고양이 인형을 가방에 넣었다."
    # SOURCE S02 L2520
    narrator "그리고 평소처럼 웃었다."
    # SOURCE S02 L2523 (시아)
    sia "좋아!"
    # SOURCE S02 L2525 (시아)
    sia "그럼 다음에는 내가 안 진다!"
    # SOURCE S02 L2528 (주인공)
    mc "아직 게임을 한다고 말씀드리지 않았는데요."
    # SOURCE S02 L2531 (시아)
    sia "그런 건 상관없어."
    # SOURCE S02 L2534 (시아)
    sia "인생은 승부거든!"
    # SOURCE S02 L2538
    narrator "……정말 한결같은 사람이다."
    # SOURCE S02 L2540
    narrator "그런데 이제는 그 모습이 더 좋아 보였다."
    # SOURCE S02 L2542 # CONTI [SCENE 07 END]
    jump sia_s02_sc08

label sia_s02_sc08:
    $ phone_timeline_enter("S02", "sia_s02_sc08")
    # SOURCE S02 L2546 SCENE 08. 이게 무슨 기분인데
    # SOURCE S02 L2548 # CONTI [TIME] 같은 날 밤 · 주인공 방 → 시아의 방 · S03 복선
    # SOURCE S02 L2550 # CONTI [HEADING] S02 SC08 · 이게 무슨 기분인데
    # SOURCE S02 L2552 [BG] 주인공 방 · 밤
    $ sia_draft_scene("주인공 방 · 밤")
    # SOURCE S02 L2554 [BGM] Quiet Night
    $ story_draft_bgm("Quiet Night")
    # SOURCE S02 L2556 # CONTI [FADE IN]
    # SOURCE S02 L2560
    narrator "방으로 돌아와 가방을 내려놓았다."
    # SOURCE S02 L2562
    narrator "오늘은 꽤 많이 걸었다."
    # SOURCE S02 L2564
    narrator "게임센터에서 놀고."
    # SOURCE S02 L2566
    narrator "사진을 찍고."
    # SOURCE S02 L2568
    narrator "같이 저녁을 먹었다."
    # SOURCE S02 L2570
    narrator "그런데 가장 기억에 남는 건 마지막 산책이었다."
    # SOURCE S02 L2572
    narrator "다음에도 둘이서 놀자."
    # SOURCE S02 L2574
    narrator "시아 씨가 했던 말이 자꾸 떠올랐다."
    # SOURCE S02 L2576
    narrator "……그냥 둘이 노는 게 재미있어서 그런 거겠지."
    # SOURCE S02 L2578
    narrator "그런데 나는 왜 그 말이 그렇게 좋았을까."
    # SOURCE S02 L2580 # CONTI [SFX] 휴대전화 진동
    # SOURCE S02 L2582 # CONTI [UI] 시아 개인 메시지
    $ story_chat(True, title="시아")
    # SOURCE S02 L2585 (시아)
    sia "야"
    # SOURCE S02 L2588 (주인공 · 메시지)
    mc "네, 시아 씨."
    # SOURCE S02 L2591 (시아)
    sia "오늘 사진 다시 봤는데"
    # SOURCE S02 L2593 (시아)
    sia "진짜 웃기다ㅋㅋㅋ"
    # SOURCE S02 L2596 (주인공 · 메시지)
    mc "저도 방금 봤어요."
    # SOURCE S02 L2599 (시아)
    sia "근데"
    # SOURCE S02 L2601 (시아)
    sia "세 번째는 좀 잘 나왔더라"
    # SOURCE S02 L2605
    narrator "세 번째."
    # SOURCE S02 L2607
    narrator "고양이 인형을 가운데에 두고 나란히 찍었던 사진이다."
    # SOURCE S02 L2610 (주인공 · 메시지)
    mc "네. 저도 그 사진이 제일 마음에 들어요."
    # SOURCE S02 L2613 (시아)
    sia "……."
    # SOURCE S02 L2615 (시아)
    sia "오"
    # SOURCE S02 L2617 (시아)
    sia "취향 일치네"
    # SOURCE S02 L2620 (주인공 · 메시지)
    mc "그러게요."
    # SOURCE S02 L2623 (시아)
    sia "아 그리고"
    # SOURCE S02 L2626 (주인공 · 메시지)
    mc "네?"
    # SOURCE S02 L2629 (시아)
    sia "다음 약속 잊지 마"
    # SOURCE S02 L2632 (주인공 · 메시지)
    mc "네. 장소 찾아볼게요."
    # SOURCE S02 L2635 (시아)
    sia "좋아"
    # SOURCE S02 L2637 (시아)
    sia "기대한다"
    # SOURCE S02 L2641
    narrator "잠시 뒤 마지막 메시지가 도착했다."
    # SOURCE S02 L2644 (시아)
    sia "오늘 진짜 재밌었어"
    # SOURCE S02 L2647 (주인공 · 메시지)
    mc "저도요. 좋은 밤 보내세요."
    # SOURCE S02 L2650 (시아)
    sia "응 잘자"
    # SOURCE S02 L2652 # CONTI [UI] 스마트폰 화면 종료
    $ story_chat(False)
    # SOURCE S02 L2656
    narrator "휴대전화를 내려놓았다."
    # SOURCE S02 L2658
    narrator "이상하다."
    # SOURCE S02 L2660
    narrator "단순히 친구와 놀았던 하루라고 생각하려고 했는데."
    # SOURCE S02 L2662
    narrator "오늘의 시아 씨는 조금 다르게 기억에 남는다."
    # SOURCE S02 L2664
    narrator "장난을 치던 표정."
    # SOURCE S02 L2666
    narrator "게임에서 졌을 때 억울해하던 모습."
    # SOURCE S02 L2668
    narrator "인형을 받고 조용히 고맙다고 말하던 순간."
    # SOURCE S02 L2670
    narrator "그리고 헤어지기 싫다고 했던 말까지."
    # SOURCE S02 L2672
    narrator "……혹시."
    # SOURCE S02 L2674
    narrator "나는 시아 씨를 조금 특별하게 생각하고 있는 걸까."
    # SOURCE S02 L2677 (주인공 · 혼잣말)
    mc "……아직은 모르겠네."
    # SOURCE S02 L2681
    narrator "하지만 다음에 만날 날이 기다려지는 건 확실했다."
    # SOURCE S02 L2683 # CONTI [TRANSITION] 같은 밤 · 시아의 방
    # SOURCE S02 L2685 # CONTI [POV] 시아
    $ phone_perspective_set("sia")
    # SOURCE S02 L2687 [BG] 시아의 방 · 밤
    $ sia_draft_scene("시아의 방 · 밤")
    # SOURCE S02 L2689 [BGM] Soft Romantic Comedy
    $ story_draft_bgm("Soft Romantic Comedy")
    # SOURCE S02 L2693
    narrator "시아는 침대 위에 누워 있었다."
    # SOURCE S02 L2695
    narrator "한쪽에는 오늘 뽑은 고양이 인형이 놓여 있었다."
    # SOURCE S02 L2697
    narrator "휴대전화 화면에는 포토부스에서 찍은 사진이 떠 있었다."
    # SOURCE S02 L2700 (시아 · 혼잣말)
    sia "……."
    # SOURCE S02 L2704
    narrator "시아는 사진을 확대했다."
    # SOURCE S02 L2706
    narrator "첫 번째 사진은 평범했다."
    # SOURCE S02 L2708
    narrator "두 번째는 둘 다 이상한 표정을 짓고 있었다."
    # SOURCE S02 L2710
    narrator "세 번째는 고양이 인형을 사이에 두고 나란히 웃는 사진이었다."
    # SOURCE S02 L2712
    narrator "시아는 그 사진을 한동안 바라봤다."
    # SOURCE S02 L2715 (시아 · 혼잣말)
    sia "……뭐야."
    # SOURCE S02 L2719
    narrator "그러다가 휴대전화를 내려놓았다."
    # SOURCE S02 L2722 (시아 · 혼잣말)
    sia "그냥 사진이잖아."
    # SOURCE S02 L2726
    narrator "잠시 뒤 다시 집어 들었다."
    # SOURCE S02 L2729 (시아 · 혼잣말)
    sia "……근데 좀 잘 나왔네."
    # SOURCE S02 L2733
    narrator "시아는 고양이 인형을 들어 올렸다."
    # SOURCE S02 L2736 (시아 · 혼잣말)
    sia "야, 너는 어떻게 생각하냐?"
    # SOURCE S02 L2740
    narrator "인형은 아무 대답도 하지 않았다."
    # SOURCE S02 L2743 (시아 · 혼잣말)
    sia "……."
    # SOURCE S02 L2745 (시아 · 혼잣말)
    sia "아, 내가 지금 인형한테 뭘 물어보냐."
    # SOURCE S02 L2749
    narrator "시아는 웃음을 터뜨렸다."
    # SOURCE S02 L2751
    narrator "그러다 문득 오늘 저녁의 일이 떠올랐다."
    # SOURCE S02 L2753
    narrator "오늘은 저도 헤어지기 조금 아쉬워요."
    # SOURCE S02 L2757
    narrator "그 말을 들었을 때."
    # SOURCE S02 L2759
    narrator "이상하게도 바로 장난이 나오지 않았다."
    # SOURCE S02 L2761
    narrator "평소 같으면 얼마든지 놀릴 수 있었을 텐데."
    # SOURCE S02 L2763
    narrator "그 순간에는 그냥 기분이 좋았다."
    # SOURCE S02 L2765
    narrator "너무 좋아서 오히려 뭐라고 대답해야 할지 몰랐다."
    # SOURCE S02 L2768 (시아 · 혼잣말)
    sia "……야."
    # SOURCE S02 L2772
    narrator "시아는 휴대전화를 다시 켰다."
    # SOURCE S02 L2774
    narrator "주인공과의 채팅창을 열었다."
    # SOURCE S02 L2776
    narrator "마지막 메시지는 짧았다."
    # SOURCE S02 L2778
    narrator "좋은 밤 보내세요."
    # SOURCE S02 L2781 (시아 · 혼잣말)
    sia "……."
    # SOURCE S02 L2783 (시아 · 혼잣말)
    sia "왜 이렇게 신경 쓰이지."
    # SOURCE S02 L2787
    narrator "시아는 침대에 벌렁 누웠다."
    # SOURCE S02 L2789
    narrator "천장을 바라봤다."
    # SOURCE S02 L2792 (시아 · 혼잣말)
    sia "그냥 같이 놀아서 재밌었던 거잖아."
    # SOURCE S02 L2794 (시아 · 혼잣말)
    sia "그치?"
    # SOURCE S02 L2798
    narrator "아무도 대답하지 않았다."
    # SOURCE S02 L2800
    narrator "시아는 잠시 눈을 감았다."
    # SOURCE S02 L2802
    narrator "그리고 아주 작은 목소리로 말했다."
    # SOURCE S02 L2805 (시아 · 혼잣말)
    sia "……근데."
    # SOURCE S02 L2807 (시아 · 혼잣말)
    sia "다른 사람이랑 놀러 간다고 하면……."
    # SOURCE S02 L2809 (시아 · 혼잣말)
    sia "좀 싫을 것 같은데."
    # SOURCE S02 L2813
    narrator "시아는 눈을 떴다."
    # SOURCE S02 L2816 (시아 · 혼잣말)
    sia "……."
    # SOURCE S02 L2818 (시아 · 혼잣말)
    sia "아."
    # SOURCE S02 L2822
    narrator "잠시 정적."
    # SOURCE S02 L2825 (시아 · 혼잣말)
    sia "……아니겠지?"
    # SOURCE S02 L2829
    narrator "시아는 베개로 얼굴을 가렸다."
    # SOURCE S02 L2832 (시아 · 혼잣말)
    sia "아아아아!"
    # SOURCE S02 L2834 (시아 · 혼잣말)
    sia "이게 무슨 기분인데!"
    # SOURCE S02 L2838
    narrator "한참 뒤 베개를 내려놓았다."
    # SOURCE S02 L2840
    narrator "그런데 얼굴에는 웃음이 남아 있었다."
    # SOURCE S02 L2843 (시아 · 혼잣말)
    sia "……일단."
    # SOURCE S02 L2845 (시아 · 혼잣말)
    sia "다음에 또 만나면 알겠지."
    # SOURCE S02 L2849
    narrator "시아는 고양이 인형을 옆에 놓았다."
    # SOURCE S02 L2851
    narrator "그리고 휴대전화에 다음 약속 날짜를 적었다."
    # SOURCE S02 L2853
    narrator "……평소 같았으면 그냥 기억하고 말았을 약속이었다."
    # SOURCE S02 L2855 # CONTI [FADE TO BLACK]
    # SOURCE S02 L2857 # CONTI [TEXT]
    # SOURCE S02 L2859 # CONTI [TEXT] SIA ROUTE
    # SOURCE S02 L2861 # CONTI [TEXT] S02 COMPLETE
    # SOURCE S02 L2863 # CONTI [TEXT] 「너랑 있으면 이상하게 재밌어」
    # SOURCE S02 L2865 # CONTI [TEXT] NEXT CHAPTER
    # SOURCE S02 L2867 # CONTI [TEXT] S03 「이건 장난이 아니야」
    # SOURCE S02 L2869 [FLAG] `sia_s02_complete = True`
    $ story_flag("sia_s02_complete", True)
    # SOURCE S02 L2871 [FLAG] `sia_s02_date_complete = True`
    $ story_flag("sia_s02_date_complete", True)
    # SOURCE S02 L2873 [FLAG] `sia_s02_photo_taken = True`
    $ story_flag("sia_s02_photo_taken", True)
    # SOURCE S02 L2875 # CONTI [NEXT] SIA ROUTE S03
    # SOURCE S02 L2877 # CONTI [CHAPTER S02 END]
    $ sia_complete_episode("S02")
    jump sia_s03
