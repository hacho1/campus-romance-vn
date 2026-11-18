# 오므 O01–O06·시크릿 원고 적용

사용자가 제공한 확정7원고의 대사·선택·조건·기억을 변환했다. 신규 스탠딩·SD/LD는 만들지 않는다.
제공된 시크릿 CG만 OSECRET L302에서 보이고 SC03의 새 배경 L565에서 종료한다. 나머지 그림·표정 지시는 CONTI로 보존한다.
실제 점수는 omu_relationship_choices.json의 검토된 5/10 정책만 적용한다. 원고의 권장 점수 변수를 직접 계산하지 않는다.
O01의 연속 CONDITION 3개는 같은 공통 복귀를 갖는 배타 분기다. O02의 ELSE IF와 O04/O05 조건도 원문 그대로 보존한다.
작성하다 지운 주인공 초안은 발송하지 않는다. 사진 동아리 담당 메시지는 별도 방을, 사고 연락의 전화 속 목소리는 일반 대사창을 사용한다.
O06 BAD의 사고는 점수 선택의 인과 결과라고 새로 설명하지 않는다. 사고·애도 서사는 확정 원문만 출력한다.
O06의 중간/엔딩 서사10문장과 시크릿 마무리2문장은 실제 대사창에 출력한다. 완료/다음 장 제목은 제작 메타다.
재생성 후 tools/import_roman_first.py --phone-cues로 최종 전화 시간·시점 조회를 갱신한다.

## O01

- 원본 SHA256: `3ad23a26238f58c2385ab08b1de0f05cec972bc05e0457cd656eae49e7bcbfc9`
- 실제 대사/서술: 708, 씬: 8, 메뉴: 2, 조건: 1
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\omu_o01.rpy`

### 미제작 그림·표정·연출 콘티

- L311: [LD] 오므 · 기본 미소
- L1334: [CG 후보] `omu_o01_natural_smile`
- L1336: [연출] 따뜻한 오후 햇빛이 드는 오래된 골목에서 고개를 살짝 돌려 웃는 오므의 자연스러운 모습. 카메라를 의식하지 않은 표정. 주인공은 촬영자 시점이므로 화면에 등장하지 않는다.

## O02

- 원본 SHA256: `7fcf6195ddb226afc07a29123f394437fba51917251a400d92c7996fac27767a`
- 실제 대사/서술: 667, 씬: 8, 메뉴: 2, 조건: 1
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\omu_o02.rpy`

### 미제작 그림·표정·연출 콘티

- L439: [SD EVENT] `omu_o02_popcorn_comedy`
- L441: [연출] 어두운 영화관에서 큰 팝콘 통을 품에 안고 태연하게 먹는 오므의 SD 이벤트 1장. 주인공은 화면에 표시하지 않는다.
- L1499: [CG 후보] `omu_o02_after_rain_smile`
- L1501: [연출] 비가 막 그친 저녁 산책로에서 오므가 카메라 없이 주인공 쪽을 바라보며 조용히 웃는 근접 구도. 물웅덩이에 노을빛이 비치고, 오므의 얼굴에는 약한 홍조가 있다. 주인공 외형은 표시하지 않는다.

## O03

- 원본 SHA256: `4dc3616365e20bcc7d03ea3433cc87c770cdaf335d8e66404b0997e22c2842bc`
- 실제 대사/서술: 804, 씬: 8, 메뉴: 3, 조건: 0
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\omu_o03.rpy`

### 미제작 그림·표정·연출 콘티

- L1561: [CG 후보] `omu_o03_confession`
- L1563: [연출] 노을빛이 내려앉은 공원 전망 공간에서 오므가 카메라 없이 주인공을 바라본다. 평소의 담담한 표정에 옅은 홍조가 나타나며, 한 손은 가방끈을 가볍게 잡고 있다. 주인공은 화면에 표시하지 않는 1인칭 구도.
- L2024: [연출] 별도 CG 없이 LD와 짧은 화면 페이드. 1인칭 손잡기 연출은 선택 사항.

## O04

- 원본 SHA256: `2e42d96055533e21e3e994173fdcc54348a290b2efad1bc46c56a4ce52acc779`
- 실제 대사/서술: 668, 씬: 8, 메뉴: 3, 조건: 5
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\omu_o04.rpy`

### 미제작 그림·표정·연출 콘티

- L138: [LD] 오므 · 기본 미소

## O05

- 원본 SHA256: `f140113cc5c500e5b845a0a9b2e524c59ccc94a4c878d28c88c3658d63384a92`
- 실제 대사/서술: 864, 씬: 8, 메뉴: 4, 조건: 3
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\omu_o05.rpy`

### 미제작 그림·표정·연출 콘티

- L216: [LD] 오므 · 미소
- L1470: [LD] 시아 · 장난스러운 미소

## O06

- 원본 SHA256: `71a74cb5087ce8be1ce447709d7f8c40df77152c8168e53cf04bacaa354ce82a`
- 실제 대사/서술: 1024, 씬: 12, 메뉴: 1, 조건: 0
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\omu_o06.rpy`

### 미제작 그림·표정·연출 콘티

- L208: [LD] 오므 · 기본 미소
- L1592: [CG 후보] `omu_o06_happy_seaside`
- L1594: [연출]
- L2909: [CG 후보] `omu_o06_bad_last_photo`
- L2911: [연출]

## OSECRET

- 원본 SHA256: `d2407b12c7373fd268041fbeb0daffccbfcd618324d06a0139a0acc46c9a4422`
- 실제 대사/서술: 623, 씬: 5, 메뉴: 1, 조건: 0
- 파일: `D:\CampusRomance_VN\renpy_project\game\routes\omu_secret.rpy`

### 미제작 그림·표정·연출 콘티

- L302: [CG MAIN] `omu_secret_maid_welcome`
- L304: [연출]

