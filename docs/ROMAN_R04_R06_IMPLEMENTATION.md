# 로만 R04–R06·시크릿 원고 구현

## 범위와 원본

`design_docs/story_sources`의 네 원고를 처음부터 끝까지 읽은 뒤 아래 네 신규 파일로 옮겼다. 공유 runtime/state, 기존 roman.rpy, CH 원고·코드, CG registry, 엔딩 JSON은 이 작업에서 수정하지 않았다.

| 원고 | 행 수 | SHA256 | 대상 |
| --- | ---: | --- | --- |
| roman_r04.txt | 1841 | `3b2e8156bff36198cf5f586128ef684fb9d78a123e050753fe7a23606cf455de` | game/routes/roman_r04.rpy |
| roman_r05.txt | 1981 | `cdd751ce57be398f45b37c461f3adda58e25ec4aef087bee797a8ed7896b3069` | game/routes/roman_r05.rpy |
| roman_r06.txt | 2175 | `f9fe5ae94b3463c8fbb6099369c3efeddb411ccb2d04b5a0071c2b0bd496b9cc` | game/routes/roman_r06.rpy |
| roman_secret.txt | 1100 | `a93930b3a39295ffa1c425f1e7cf3daefef25b2f4a92e320c37842a2a3710a65` | game/routes/roman_secret.rpy |

주요 label은 `roman_r04 → roman_r05 → roman_r06`이다. 시크릿은 별도 `roman_secret`이며 해피 뒤에 자동 진입하지 않는다. 각 씬은 `roman_r04_sc01` 같은 별도 label로 유지한다. R06의 해피·배드 전용 씬과 후일담은 각각 분리된 label로 연결한다.

모든 대사·선택지·조건·FLAG·연출 앞에 `SOURCE <원고> L<행>`을 붙였다. 원고의 맞춤법·말투와 챕터 번호를 언급하는 대사도 그대로 유지했다. Markdown 강조 표시만 표시용 문장 밖으로 제거했다. 창작 설명·콘티와 실제 서술은 구분했다. 예를 들어 R04 L820의 작가용 씬 설명과 R06 L1350–1356의 구현 메모는 플레이 대사로 표시하지 않는다.

## 선택지와 효과

| 원고 | 시작 행 | 선택 수 | 처리 |
| --- | ---: | ---: | --- |
| R04 | 473 | 3 | 결말 존중·자율성·승인 의존 |
| R04 | 1187 | 3 | 번호 없는 세 선택지를 원고 순서대로 menu 처리 |
| R05 | 1092 | 3 | direct / companionship / honest 고백 방식 |
| R05 | 1712 | 3 | 관계 균형·비현실적 약속·의존 위험 |
| R06 | 1198 | 3 | respect / negotiate / surrender 최종 선택 |

선택지 한 옵션의 FLAG는 `story_apply` 한 번으로 묶는다. `values`는 대입, `counters`는 원고의 raw 증감 값이다. 후반 네 원고에는 새로운 호감·신뢰 보상이 없으며, 별도 `roman_affection`/`roman_trust` scalar를 만들지 않았다. 앞 세 편의 호감·신뢰는 기존 전역 map과 ×5 정책을 그대로 사용한다.

R01–R03에서 도입한 변수는 중복 default를 선언하지 않는다. 후반에서 처음 도입하는 bool·문자열·카운터만 해당 소유 파일에 default를 둔다. 앞편 누적 카운터 조회는 `getattr(store, key, 0)`으로 안전하게 처리한다.

## R06의 미정 수치 해결

원고 R06 L1352–1356은 누적 관계 선택과 마지막 경계 선택의 원칙만 정하고 수치는 확정하지 않았다. 다음 수치는 원문에 있는 숫자가 아니라, 실제 변수에 맞춰 구현자가 정하고 parent가 승인한 결정적 판정 기준이다.

`roman_later_relationship_scores()`는 다음 두 정수를 반환한다.

```text
D = roman_unrealistic_promise
  + roman_reassurance_dependency
  + roman_approval_dependency
  + roman_dependency_risk

P = roman_mutual_respect
  + roman_mutual_understanding
  + roman_creative_autonomy
  + roman_relationship_balance
  + (전역 trust['roman']이 50 이상이면 1, 아니면 0)
```

일반적인 의존 **누적** 묘사는 D > 0, 원고에서 **높은 의존**이라고만 한 분기는 D ≥ 4로 처리한다. R06 L497의 조건은 원고가 직접 지정한 `roman_unrealistic_promise > 0 or roman_dependency_risk > 0`을 그대로 쓴다. R05 L719의 `roman_creative_autonomy >= 3`도 원문 수치를 그대로 쓴다.

순수 함수 `roman_r06_select_ending(dependency, support, boundary)`의 판정:

| 마지막 선택 | 배드 조건 | 그 외 |
| --- | --- | --- |
| respect | 없음: 마지막 경계 존중에 의한 회복 허용 | happy |
| negotiate | D ≥ 4 이면서 D > P + 2 | happy |
| surrender | D ≥ 4 이면서 D ≥ P | happy |

따라서 낮은 의존 상태에서 마지막 C 하나만 골라도 배드로 강제하지 않는다. 중간 B는 이전의 건강한 관계 선택으로 회복할 수 있다. 반복된 의존이 누적됐고 마지막에도 문제를 외면한 경우에만 배드가 가능하다. QA는 store 없이 이 순수 함수를 직접 검사할 수 있다.

해피 후일담의 마지막은 `roman_record_ending("happy")`, 배드는 `roman_record_ending("bad")`를 호출하고 return한다. 원고의 happy/bad 완료·시크릿 해금 가능·루트 완료 FLAG도 각 분기에서 적용한다.

## 시크릿과 연출 보류

`roman_secret` 진입 시 `persistent.endings`에 `roman_happy`가 없으면 안내 후 return한다. 원고의 해피 완료 조건과 별개로 실행 입구에서도 막는다. 마지막에는 `roman_record_ending("secret")` 후 return한다.

이번 사용자 지시에 따라 모든 LD/SD/SPRITE와 새 CG 후보는 `# CONTI` 주석과 `ROMAN_R04_R06_CONTI_GUIDE.md`에 보존한다. 실제 스탠딩·신규 일러스트를 만들거나 표시하지 않았다. 배경은 parent의 `story_draft_scene`, 음악은 `story_draft_bgm`으로 전달하며 draft scene helper가 standing=False를 보장한다. SFX·fade·표정·카메라 지시는 콘티로 남겼다.

유일한 실제 일러스트 예외는 사용자가 첨부한 시크릿 그림이다. 원고 Secret L273의 메인 CG 표시와 L473의 유지 지점에서 parent의 `roman_secret_illustration()`을 호출한다. SC03 배경 재설정 후 같은 그림을 다시 표시하고, SC04의 새 배경에서 해제된다. 이미지 파일·registry·갤러리 해금은 parent 소유다.

휴대전화는 기존 `story_chat`을 사용한다. 로만 개인방, R04 로만 시점의 다림 개인방, R06의 「우리 사이」 단체방을 원고대로 구분한다. 별도 UI 표시는 없지만 메시지가 재개되는 R06 L397/L2076과 Secret L153에서 열고, Secret L181의 문 너머 음성으로 넘어갈 때 닫는다. scene/transition/episode 끝에서도 닫는다.

R05의 안내 방송·진행자·참가자는 원고의 화자명을 보존하는 private Character 정의를 그 파일에만 두고 기존 `story_speaking` callback을 재사용한다. 기존 인물은 roman/mc/darim/sia/omu/lumi identifier를 사용한다.

## 재현과 검증

```powershell
& 'D:\CampusRomance_VN\tools\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe' -B -X utf8 'D:\CampusRomance_VN\tools\import_roman_later.py'
```

이 명령은 네 소유 RPY와 이 범위의 import audit/콘티 가이드만 생성한다. 게임 실행이나 저장 조작을 하지 않는다. 재생성할 때는 importer와 원고 행 경계 설정을 함께 유지한다.

생성 audit: `docs/ROMAN_R04_R06_IMPORT_AUDIT.json`.

- R04: 대사·서술 655개, 8씬, 선택 옵션 6개
- R05: 641개, 8씬, 선택 옵션 6개
- R06: 659개, 10씬, 선택 옵션 3개
- Secret: 338개, 5씬, 선택 옵션 0개

별도 정적 대조에서 원고의 인용 대사 누락 0개, 구현 메모·FLAG·CG 지시의 본문 유출 0개를 확인했다. 실제 Ren'Py 통합 Lint·분기·저장/로드·갤러리 검사는 parent와 QA가 수행한다. 이 구현 작업에서는 실제 원본 게임을 실행하거나 저장을 조작하지 않았다.
