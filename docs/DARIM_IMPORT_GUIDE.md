# 다림 D01–D06 원고 적용

확정6원고의 대사·선택·조건·기억을 변환했다. 신규 스탠딩·SD/LD를 만들거나 표시하지 않는다.
실제 점수는 darim_relationship_choices.json의 검토된 5/10 정책만 적용한다.
D01의 CH06 회상은 실제 ch06_darim_festival_event 플래그일 때만 회수한다. 파트너 선택만으로 추측하지 않는다.
D01/D06의 지난 메시지는 새 메시지로 보내지 않는다. D03 삭제된 초대 메시지는 원래 항목의 텍스트만 바꾼다.
D04 모임 담당자는 별도 서비스 방이다. D05 일반 문의는 실제 발화가 없으므로 메시지를 발명하지 않는다.
D06의 전화 대화는 대사창으로 표시하며 메시지 이력에 넣지 않는다. 혼잣말·초안·개인 메모도 전송하지 않는다.
시크릿은 이름만 예고돼 있으므로 새 대본·엔딩을 발명하지 않았다.
재생성 후 tools/import_roman_first.py --phone-cues로 시간·시점 큐를 갱신한다.

## D01

- 원본 SHA256: `b6b7ee8f399ec2e880fa6e68b08549a83e810d32692dbcba76fcbb71e644551d`
- 실제 대사/서술: 306, 씬: 8, 메뉴: 2, 조건: 2
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\darim_d01.rpy`

### 미제작 그림·표정·연출 콘티

- L317: [SD 선택 후보] `darim_d01_game_defeat`

## D02

- 원본 SHA256: `904fa50fdf52a973b8d6aaea5ed02ef73e1ba1b9eab3e612a142da58641b67a9`
- 실제 대사/서술: 593, 씬: 8, 메뉴: 2, 조건: 0
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\darim_d02.rpy`

### 미제작 그림·표정·연출 콘티

- L171: [LD] 다림 · 기본
- L1519: [CG 후보] `darim_d02_evening_request`
- L1521: [연출]

## D03

- 원본 SHA256: `96b7c430dd667b387e2f18e41683c94fee624d194b26742aa91c76c86e2e59d1`
- 실제 대사/서술: 829, 씬: 8, 메뉴: 3, 조건: 0
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\darim_d03.rpy`

### 미제작 그림·표정·연출 콘티

- L343: [LD] 다림 · 미소
- L1592: [CG 후보] `darim_d03_confession_sunset`
- L1594: [연출]
- L2060: [연출] 다림 LD를 화면 중앙에 두고 짧은 페이드. 손잡는 장면은 별도 CG 없이 대사로 처리 가능.

## D04

- 원본 SHA256: `79a0183793d56d7c32354e0613e10c33c1aa31d327bbb97b47c52ac34910477c`
- 실제 대사/서술: 602, 씬: 8, 메뉴: 3, 조건: 5
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\darim_d04.rpy`

### 미제작 그림·표정·연출 콘티

- L148: [LD] 다림 · 미소
- L1075: [LD] 다림 · 밝은 미소

## D05

- 원본 SHA256: `99d25ac175e7cb74f298f35f63c87ac9935a7790ec0ec44d4dca6ec6219c9d41`
- 실제 대사/서술: 796, 씬: 8, 메뉴: 4, 조건: 6
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\darim_d05.rpy`

### 미제작 그림·표정·연출 콘티

- L159: [LD] 다림 · 기본 미소
- L2346: [LD] 다림 · 진지한 표정

## D06

- 원본 SHA256: `18a656e67f33e9a483d87f05a823495ede21700cee11c72286d943d16acd15cc`
- 실제 대사/서술: 882, 씬: 12, 메뉴: 2, 조건: 1
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\darim_d06.rpy`

### 미제작 그림·표정·연출 콘티

- L1696: [CG 후보] `darim_d06_happy_holding_hands`
- L1698: [연출]
- L2895: [CG 후보] `darim_d06_bad_empty_schedule`
- L2897: [연출]

