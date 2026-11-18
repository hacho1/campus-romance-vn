# 우리 사이, 그 이상: PC 런처 설치와 갱신

## 현재 운영

기준 게임 원본은 `D:\CampusRomance_VN\renpy_project`다. 플레이어는 Windows 런처를 한 번 내려받아 PC에 게임을 설치하고, 같은 런처로 실행하거나 이후 변경 파일을 받는다.

- 제품 페이지: <https://campus-romance-playtest.naiski.chatgpt.site/>
- 런처 다운로드: <https://campus-romance-playtest.naiski.chatgpt.site/downloads/CampusRomanceLauncher.exe>
- 최신 배포 정보: <https://campus-romance-playtest.naiski.chatgpt.site/releases/latest.json>

사용자가 공개·온라인 연결을 승인했고 기존 Site는 **public, revision 2**다. 현재 Windows 런처는 **1.1**, 게임은 **0.6.11-test / build `2026111501`**이며 실제 R2에 활성화했다. Site version 3의 CH01–CH07 공통 루트·로만 R01–R06과 엔딩 안내를 유지한다. 수달 아이콘과 설치/공지 탭을 유지하며 현재 버전과 공지를 활성 manifest에서 읽는다. 사용자의 실제 전체 게임 설치는 수행하지 않았다.

0.6.11-test는 CH07 공통SD1장·인물별LD5장, 해피/배드 완료 대사창의 실제제목 표시10곳과 개별루트30챕터 스탠딩 계획을 반영했다. 새로만집착표정·시크릿특수의상은 대기로 두고 제작위치49곳을 기록했다. 네이티브71케이스(대본원문없는배포형2케이스포함)와 컴파일·Lint, 530소스/스냅샷 일치를 통과했다. 전체1,907파일·642,419,775바이트, 새96조각·24,564,802바이트 게시, 기존1,809조각 재사용. manifest SHA256은 `85aa039d147ea0f5e49c4cd039b7f93996277ba3e06081b93cc689cf47f85a20`다. 공개97RPYC를 보존했다. productionCLI·고정RSA/TLS·공개15파일21,057,624바이트와 사이트 공지도 실제 확인했다. [CH07·개별스탠딩 릴리스 보고서](CH07_PRIVATE_STANDING_RELEASE_0.6.11.md), [제작 대기 위치](PRIVATE_ROUTE_ART_SLOTS.md)에 범위를 기록했다.

0.6.10-test는 CH06 다림·하린 첨부 CG4컷과 인물별 두 컷 갤러리2항목, 로만·시아·오므·다림 NOTE03 시크릿 문구를 반영했다. 원본 PNG 바이트와 기존 대사·선택·해금 판정을 유지한다. 네이티브11케이스·36검증, 컴파일·Lint, 521소스/공개스냅샷 일치를 통과했다. 전체1,898파일·621,821,119바이트이며 새90조각·14,398,567바이트 게시, 기존1,806조각 재사용. manifest SHA256은 `c264afe611cbce472ae3e12bf238623bc1af3970dc1ef823a8e34b772b568e12`다. 공개95RPYC를 보존했다. productionCLI·고정RSA/TLS·공개9파일10,950,273바이트와 실제 사이트 공지도 확인했다. [CH06 다림·하린 릴리스 보고서](CH06_DARIM_HARIN_RELEASE_0.6.10.md)에 정확한 대사 구간과 메모 원문·검증 범위를 기록했다.

0.6.9-test는 하린 H01~H06 및 해피·배드·시크릿 대본, 오므 O04~O06 개정 분기와 새 배드엔딩 「흐려진 나의 시선」을 반영했다. 하린 테스트 이어읽기와 다섯 명의 시크릿 진입을 연결하고 5/10점 단위·기존 기록을 유지한다. 네이티브15케이스·74검증, 컴파일·Lint, 517소스/snapshot 일치와 기존39저장 기록 보존을 확인했다. 새90조각·3,889,301바이트, 기존1,802조각 재사용. 전체1,894파일·611,291,247바이트, manifest SHA256은 `94d571be40bc63f13edfdcb112579e494c86f5aeedf79f823a83583c2e00b6d8`다. 공개95RPYC를 보존했다. productionCLI·고정RSA/TLS·공개37파일5,589,582바이트 및 실제 사이트 공지를 확인했다. [하린·오므 릴리스 보고서](HARIN_OMU_RELEASE_0.6.9.md), [실행 검증](HARIN_OMU_QA_0.6.9.md)에 범위와 미제공 이미지를 기록했다.

0.6.8-test는 테스트판의 비밀 메모15칸과 엔딩별내용15종, 준비된 갤러리50장면·58컷을 실제 기록 변경 없이 열람하도록 했다. 기존 획득·스토리 진입 판정13함수는 유지하고 실제 해금도 정상 기록한다. 네이티브4케이스·45검증과 Lint·506소스/snapshot, productionCLI·RSA·공개10파일 다운로드 검증을 통과했다. 새73조각·3,082,848바이트 게시, 기존1,808조각 재사용. 전체1,883파일·610,751,159바이트, manifest SHA256은 `4a225c029f37b89dc6a7c286d55946c55e6b4bc336db4b8182c720787cb82679`다. 공개85RPYC를 보존했다. 실제 실행 중인 게임을 종료한 뒤 기존 런처의 **업데이트 확인 → 설치·업데이트**로 받는다. [테스트판 전체 열람 보고서](TEST_COLLECTIONS_RELEASE_0.6.8.md)에 범위와 미완성 문구를 기록했다.

0.6.7-test는 챕터 테스트를 개별01→06·엔딩까지 이어 읽게 하고 선택·이름·5/10점·메시지와 현재 화수를 유지한다. 공통7개챕터에서 선택한 인물의 이야기로 연결하고 수동 종료로 호출 전 상태를 복원한다. 실제13케이스·67검증·Lint와 productionCLI·RSA·공개16파일 확인을 통과했다. manifest SHA256은 `4bdd7f9a73892d097823b55c4605ea7819b76744a8f13528b3a82ad0d8e33679`다. 원래 대본과 점수는 바꾸지 않았고 로만 래퍼만 Replay의 최종 복귀용2줄을 추가했다. [이어 읽기 보고서](TEST_CONTINUATION_RELEASE_0.6.7.md)에 검증 범위·실행 중인 실제게임의persistent파일 관찰 한계를 기록했다.

0.6.6-test는 CH06 개장 SD 1장과 로만·시아·오므 축제 CG 6컷을 지정 대사 구간에 연결했다. 기존 다림 대본을 유지하고 CH06/07 스탠딩을 점검했으며 갤러리는 인물별 두 컷을 한 항목으로 묶었다. 실제 Ren'Py 14케이스·38검증, 구065저장 기준1케이스·2검증·Lint·506소스/snapshot·사용자14기록 보존 및 productionCLI·고정RSA·공개20파일 다운로드를 통과했다. 첨부원본7장의 바이트를 그대로 유지했다. 새83조각·25,439,146바이트를 게시하고 기존1,798조각 재사용. 전체1,883파일·610,746,995바이트, manifest SHA256은 `edbcda4a52eebd4c06bfd7f4fe77f8207970322bb5784cffc837ad8220aad46c`다. 공개85RPYC를 보존했다. 기존 런처의 **업데이트 확인 → 설치·업데이트**로 받는다. [CH06 축제 보고서](CH06_FESTIVAL_RELEASE_0.6.6.md), `tests/ch06_visual_066`, `tests/ch06_visual_066_public`에 근거가 있다.

0.6.5-test는 다림 시크릿 **이번에는 제가 놀릴게요**의256대사·5씬과 원본2048×1152 CG를 추가했다. 해피 이후 진입·첫 표시/완료 수집·DARIM/ENDING 한 작품·4시크릿 버튼·7다림 테스트 항목을 연결했으며 점수·새스탠딩·SD는 추가하지 않았다. 네이티브 채택4케이스·15검증, 구064기준1케이스·2검증과 Lint·499소스/snapshot·사용자14기록 보존·productionCLI·고정RSA·공개13파일 다운로드를 통과했다. UI기하 하네스의 부모/자식 좌표 가정 오류1개는 통과 수에서 제외하고 배치는 실제 다림 버튼 클릭과 소스 검토로 확인했다. 업로드 연결 종료 후 조각 재사용 재시도로 최종23조각·4,866,839바이트를 추가하고1,851조각 재사용. 전체1,876파일·588,666,721바이트, manifest SHA256은 `8489d90114f23821acd88d135664ba2432ef81d0450261f0d666f1db9de60fb5`다. 공개85RPYC를 보존했고 같은 런처에서 **업데이트 확인 → 설치·업데이트**로 받는다. [다림 시크릿 보고서](DARIM_SECRET_RELEASE_0.6.5.md), `tests/darim_secret_065`, `tests/darim_secret_065_public`에 근거가 있다.

0.6.4-test는 다림 D01~D06 확정 대본과 해피·배드 엔딩을 추가했다. 대사우선·스탠딩/새그림콘티 방식이며 시크릿 본문은 준비 중이다. 실제5·10점, CH06 실제 게임 기억, 삭제/회상/초안/전화, 담당자 말풍선과 다림–시아 소유자별 대화방·빈 보관함, 기존 다림 대기 저장 이어가기를 연결했다. 새77조각·3,306,773바이트 업로드, 기존1,795조각 재사용. 전체1,874파일·586,093,204바이트, manifest SHA256은 `bab2df7a5ee637a381662a66f23ce41243148a2d92b990aba67f131de76a7952`다. 네이티브18케이스·48검증, 구063기준3케이스·6검증, Lint·497소스/snapshot 일치·사용자14기록 보존과 productionCLI·고정RSA·공개20파일 실제 다운로드를 통과했다. 마지막 같은 날 날짜 설정은 코드/그림 변경 없이 JSON1개만 재포장하고 최종해시를 다시 대조했다. 공개84RPYC는 다음 업데이트용으로 보존했다. 같은 런처에서 **업데이트 확인 → 설치·업데이트**로 받는다. [다림 전체 반영 보고서](DARIM_ROUTE_RELEASE_0.6.4.md), `tests/darim_route_064`, `tests/darim_route_064_public`에 근거가 있다.

0.6.3-test는 오므 O01~O06 확정 원고·해피/배드 및 해피 이후 시크릿과 제공된 원본CG를 추가했다. 요청대로 개인 루트에 스탠딩을 넣지 않고 그림 지시는 콘티로 보관했다. 독립5·10점 정책, 미전송 초안과 실제 발송, 사진 동아리 전용 단체방, 기존 오므 선택 대기 저장의 이어가기 버튼을 연결했다. 새71조각·5,305,677바이트 업로드, 기존1,792조각 재사용. 전체1,865파일·585,647,171바이트, manifest SHA256은 `43e4f7457c68c293326cf52f3e6abee59aa11bc78432ed24e314fe8e2870705c`다. 네이티브13케이스·40검증, 구062 기준저장3케이스·6검증, Lint·488소스/snapshot 일치와 사용자14기록 불변, productionCLI·고정RSA·공개16파일 실제 다운로드가 통과했다. 공개76RPYC 이름 정보는 다음 업데이트용으로 보존했다. Site/런처 EXE는 유지하며 기존 런처에서 **업데이트 확인 → 설치·업데이트**로 받는다. [오므 전체 반영 보고서](OMU_ROUTE_RELEASE_0.6.3.md), `tests/omu_route_063`, `tests/omu_route_063_public`에 근거가 있다.

0.6.2-test는 공통CH01~CH07 스탠딩을 점검하고 CH06/CH07의 대면46곳과 CH03의 돌아온 방문객을 보완했다. 기존 시아 전체 루트와5·10점 정책/수집은 유지한다. 새58조각·2,512,507바이트 업로드, 기존1,794조각 재사용. 전체1,854파일·582,725,740바이트, manifest SHA256은 `17112d1d71ff85c4f122554aa7f37f6b2d946f6bf00912a05269f17cc5241129`다. 네이티브19케이스·52검증·Lint와 공개7파일·RSA·productionCLI를 통과했다. 구CH06저장의 현재배치는 그대로 복원되며 새스탠딩은 다음배경부터 적용되는 한계가 있다. [공통 스탠딩 보고서](COMMON_STANDING_RELEASE_0.6.2.md), `tests/common_standings_062`, `tests/common_standings_062_public`에 기록했다.
0.6.1-test는 시아 S03~S06·해피/배드 엔딩·해피 이후 시크릿 애프터를 확정 원고로 추가했다. S02 기존 저장 이어가기와 제공된 시크릿 그림의 최초 표시/완료 후 수집을 연결했다. 새61조각·2,368,964바이트를 게시하고 기존1,791조각 재사용. 전체1,854파일·582,693,162바이트, manifest SHA256은 `5deae162171e6cecc5529e61a5b26f6a213ea8282a2d0896029d56fc859caa18`이다. 네이티브9케이스·21검증·Lint, 기존0.6 두 저장 연결, 공개11파일·RSA·productionCLI·공지 확인을 통과했다. Site/런처 EXE는 그대로다. [시아 전체 반영 보고서](SIA_FULL_RELEASE_0.6.1.md)와 `tests/sia_full_061`, `tests/sia_full_061_public`에 근거가 있다.
0.6.0-test는 해피·배드 독립 게이지의 실제 5·10점 정책, 기존 선택 의미별 재분류와 원본 점수 보관, 로만 누적 엔딩 판정, 시아 S01·S02 확정 대본을 추가했다. 시아 시크릿 그림은 원본으로 등록하되 대본 미구현으로 잠금을 유지한다. 공개 0.5.2의 저장 위치 이름 정보를 보존해 대표 실제 저장의 정확한 대사 위치 복원도 검증했다. 새 59조각/4,915,513바이트 게시, 기존 1,787조각 재사용. 1,848파일·582,317,032바이트 manifest SHA256은 `26bde57a576160535ba64390a13ef92e5d071fca78c3bd5c4a85edf510c2bddf`다. 실제 Ren'Py 22케이스·66검증·Lint와 production CLI·공개 RSA·8파일 다운로드 대조를 통과했다. Site와 런처 EXE는 그대로이며 설치된 런처에서 **업데이트 확인 → 설치·업데이트**로 받는다. 새 버전의 RPYC61개도 다음 업데이트를 위해 별도로 보존했다. 범위·저장 이전의 한계는 [0.6.0 변경·검증 보고서](RELATIONSHIP_SYSTEM_0.6.md), `tests/relationship_overhaul_060`에 기록했다.
0.5.2-test는 CH05 준비·설치의 첨부5장을 연결했다. 첫 네 독백은 배경만 표시하고 준비 단체 컷이 등장하며, 설치 컷2→3→4는 각 지점에서 이어지고 노을의 배경/5명 스탠딩으로 복귀한다. 마지막 단체 사진은 COMMON, SD4장은 SPECIAL에 등록했다. 기존 조각1,773개 재사용·새67조각/17,833,337바이트를 게시했다. 1,842파일·579,248,002바이트의 manifest SHA256은 `251579548fd70c47d99609cf85b16866df8061f1c89f8309bb50ba1ff9f334e1`이다. 실행3케이스·46검증·대사 흐름별 관측·저장/불러오기·Lint에 더해 production CLI·공개 RSA 서명·첨부5장/컴파일 대본의 실제 다운로드 대조도 통과했다. 배포 상세는 [0.5.2-test 릴리스 가이드](RELEASE_0.5.2-test.md), `tests/ch05_art_052`에 기록했다.

0.5.1-test는 CH04 SC08 시아·다림·오므·하린의 첨부 CG 4장과 첫 호명 대사 이후 등장·각 갤러리 등록을 추가했다. 기존 조각 1,770개 재사용·새 65조각/14,709,427바이트를 게시했다. 1,837파일·563,774,891바이트의 manifest SHA256은 `56869ac0db4e8f715cd550fcc244d101219128ee8a9a2e2719d5028d4a459459`다. 실제 분기·갤러리·저장/불러오기 6케이스·110검증과 Lint, production CLI·공개 RSA 서명·첨부4장/컴파일 대본의 실제 다운로드 검증까지 통과했다. 배포 상세는 [0.5.1-test 릴리스 가이드](RELEASE_0.5.1-test.md), `tests/sc08_cgs_051`에 기록했다.

0.5.0-test는 테스트 전용 챕터 선택, 폰 시간·날짜·시점·확대, 빨간/검은 하트, 회상 구분·헤더 정렬, 시크릿 CG 보정, 배경4장·BGM2곡·SFX4개를 포함한다. 실제 진행과 수집에 반영되지 않는 테스트 Replay의 진입 버튼은 `CAMPUS_TEST_BUILD=True`일 때만 표시한다. 기존 1,756조각 재사용·새75조각/25,749,961바이트를 게시했고 Site/런처 EXE는 유지했다. manifest SHA256은 `82280a90ef263d90769a569cb37a4853b0857a97f63c39498bfbb71a6a31e647`이다. production CLI의 QA override 없는 버전·1,833파일 확인, 고정 RSA 서명, 대표4파일의 공개 다운로드와 공지5개를 검증했다. 범위·저장 호환·검사 한계는 [0.5.0-test 릴리스 가이드](RELEASE_0.5.0-test.md), `tests\ui_refresh_050`에 기록했다.

0.4.1은 CH07 SC01→SC02 시아 인사 메시지의 중복 발송과 기존 저장의 해당 중복 이력을 수정했다. 기존 1,759조각 재사용·새 53조각/2,129,408바이트를 게시했으며 Site 재배포와 런처 EXE 변경은 없다. manifest SHA256은 `a1af095b25a6d4c689bbc4250bf24d3c6281a3e1dea5994f27bb5383578d1c8a`다. 새 진행과 이전 공개판 중복/부분 중복 저장 복구 등 네이티브 4사례 및 Lint가 통과했다. 실제 production CLI의 0.4.1/0804·1,814파일 확인, 고정 서명과 CH07/phone RPYC의 공개 청크 SHA, 공지 두 개도 검증했다. [0.4.1 릴리스 가이드](RELEASE_0.4.1.md), `tests\phone_scene_echo_20261108`에 근거를 기록했다.

0.4.0은 기존 조각 1,754개를 재사용하고 새 58조각/3,883,690바이트를 게시했다. 1,814파일·527,823,418바이트의 전체 payload에서 개인 저장과 개인키는 제외했다. manifest SHA256은 `1d08f93a38acbf74e0b06412980c26648ba223e9060269ad6c77d091fc2f165f`다. production CLI의 QA override 없는 확인, RSA 서명과 CH06/R06/첨부 CG의 실제 HTTPS 다운로드, 공개 페이지 24검사와 네이티브 분기·구버전 저장 호환 검사가 통과했다. 세부 범위와 한계는 [0.4.0 릴리스 가이드](RELEASE_0.4.0.md), `tests\story_release_20261108`에 기록했다.

## 첫 설치와 이후 사용

1. 제품 페이지에서 `CampusRomanceLauncher.exe`를 내려받아 실행한다.
2. 설치 폴더를 고른다. 기본 제안은 `D:\CampusRomance_VN\Installed`다. D 드라이브가 없으면 사용자 LocalAppData 아래 CampusRomance 폴더를 제안하며, 다른 폴더도 선택할 수 있다.
3. **업데이트 확인 → 설치·업데이트 → 게임 시작**을 사용한다. 게임은 `<설치 위치>\Game`에서 실행된다.
4. 새 배포가 나오면 설치한 런처를 다시 열어 같은 순서로 갱신한다.

GUI 첫 설치가 성공하면 런처를 `<설치 위치>\CampusRomanceLauncher.exe`에 복사하고 바탕화면에 **우리 사이, 그 이상 런처** 바로가기를 만든다. 같은 이름의 다른 파일이나 바로가기는 덮어쓰지 않는다. Launcher1.1 UI 개선 때 이 개발 PC에는 해당 위치에 새 런처 EXE만 준비하고 같은 이름의 바로가기를 생성했다. 실제 전체 게임 설치·실행·기록 가져오기는 수행하지 않았다.

런처는 달라진 파일과 필요한 조각만 받는다. 이미 검증된 조각은 로컬 캐시에서 재사용하며 변경이 없으면 게임 payload 전송은 0바이트다. 설치된 게임은 채널에 접속하지 않고 실행할 수 있다. 런처 자체의 자동 업데이트는 이번 범위에 포함하지 않는다. 브라우저 게임 실행이나 클라우드 저장 동기화도 제공하지 않는다.

## 파일과 배포 구조

| 항목 | 경로·역할 |
| --- | --- |
| 기준 게임 원본 | `D:\CampusRomance_VN\renpy_project` |
| 런처 소스·사용자 EXE | `launcher_app`, `launcher_app\build\CampusRomanceLauncher.exe` |
| 제품 페이지 소스 | `launcher_storefront_source` |
| 격리 네이티브 빌드 | `launcher_publish\native_snapshot` |
| 로컬 배포 feed | `launcher_publish\feed` |
| manifest·서명 | `feed\releases\latest.json`, `latest.sig` |
| 로컬 조각 | `feed\payload\chunks\<sha256>.bin` |
| Worker 모듈 | `launcher_publish\worker_source\worker.mjs` |
| 기존 Site 체크아웃 | `web_preview\site` |
| 고정 Site ID | `appgprj_6aef4bed943081918cd1e61b5d2b7185` |
| 연결 메타데이터 | `web_preview\site\.openai\hosting.json` |

상대 경로는 `D:\CampusRomance_VN` 기준이다. 같은 Site와 URL을 재사용하며 새 사이트를 만들지 않는다. Site Worker에는 제품 페이지·그림·런처만 내장하고, 큰 게임 데이터는 논리 바인딩 `BUCKET`의 R2에 둔다. R2 구조는 `chunks/<sha256>`, `releases/<manifest-sha>.json`, 현재 배포를 가리키는 `active.json`이다.

제품 페이지는 버전·build·변경 사항만 표시하고, PC 런처가 게임 조각을 받는다. **게임 파일만 바뀌면 Site를 재배포하지 않는다.** 새 조각과 서명된 배포 정보를 R2에 올려 활성 포인터를 바꾸면 된다. 제품 페이지·런처 EXE·Worker가 바뀔 때만 같은 Site를 다시 빌드·게시한다.

## 게임 내용 갱신 명령

### 원본과 새 build 준비

원본에서 변경을 확정하고 필요한 Ren'Py 검증을 수행한다. 게임 버전은 `game\options.rpy`의 `config.version`에서 자동으로 읽는다. `build`는 매 배포마다 유일하게 증가해야 한다. 같은 build의 다른 manifest와 이전 build는 서버·런처가 거부한다.

최초 연결을 마친 뒤 후속 배포에서 사용할 명령:

```powershell
$currentRelease = Invoke-RestMethod -Uri 'https://campus-romance-playtest.naiski.chatgpt.site/releases/latest.json'
$releaseBuild = [long]$currentRelease.build + 1

& 'D:\CampusRomance_VN\tools\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe' -B -X utf8 'D:\CampusRomance_VN\launcher_publish\prepare_payload.py' --build $releaseBuild --note '이번 배포의 실제 변경 내용을 적습니다.'
```

변경 설명은 `--note`를 반복해 넣는다. 버전을 의도적으로 덮어써야 할 때만 같은 명령에 `--version '0.3.1'`처럼 추가한다. feed가 아직 503인 최초 seed는 이미 준비한 초기 build를 사용한다. 다른 게시자가 먼저 활성화해 409가 나면 최신 build를 다시 읽고 새 build로 준비·서명한다.

이 명령은 원본을 읽어 격리 snapshot을 만들고 컴파일한다. 개인 저장·테스트·캐시·개인키를 제외하며 원본과 실제 저장은 수정하지 않는다. 별도 Windows ZIP도 만들지 않는다.

### 서명

```powershell
& 'D:\CampusRomance_VN\launcher_publish\sign_manifest.ps1'
```

`latest.json`의 정확한 UTF-8 바이트에 RSA2048 PKCS#1 SHA256 서명을 만들고 `latest.sig`에 Base64 텍스트로 기록한다. 서명 후 JSON의 공백·줄바꿈도 바꾸지 않는다. 서명 개인키는 현재 Windows 사용자에게 묶인 DPAPI 파일로 보관하며 런처·사이트·R2에 포함하지 않는다.

### Windows TLS wrapper로 업로드

```powershell
& 'D:\CampusRomance_VN\launcher_publish\upload_feed.ps1' -BaseUrl 'https://campus-romance-playtest.naiski.chatgpt.site/'
```

SDK Python은 Windows 인증서 저장소를 자동 사용하지 않으므로 이 wrapper를 사용한다. Windows 신뢰 루트·중간 인증서를 `launcher_publish\windows_trusted_ca.pem`에 모으고 현재 프로세스의 `SSL_CERT_FILE`에 적용한다. TLS 인증서 검증은 켜 둔다. `upload_feed.py`를 직접 호출해 이 설정을 건너뛰지 않는다.

게시 토큰은 `launcher_private\publish_token.dpapi`에서 현재 Windows 사용자의 메모리로만 복호화한다. 인자·로그·문서에 토큰 값을 넣지 않는다. 업로더는 인증된 inventory를 페이지별로 읽고 원격에 없는 조각만 보낸다. 중단 후 같은 feed를 재업로드하면 이미 올린 조각은 재사용한다.

서버는 크기·SHA256·RSA 서명·참조 조각을 확인한 뒤 불변 release bundle을 먼저 저장하고, 마지막에 `active.json`을 ETag 조건부 쓰기로 바꾼다. 업로드 중에는 이전의 완전한 배포가 유지되며 동시 게시로 낮은 build가 재활성화되지 않는다. 런처는 받은 raw JSON의 SHA256을 `latest.sig?manifest=<sha256>`에 넣어 동일 manifest의 서명을 받는다.

### 결과 확인

준비 결과는 `launcher_publish\payload_audit.json`, 실제 업로드·활성화 결과는 `launcher_publish\r2_upload_result.json`에 기록된다. 실제 HTTPS의 manifest·서명·청크·사용자용 EXE와 설치 클라이언트의 연결을 확인한 뒤 상태를 갱신한다. 로컬 mock 성공을 온라인 설치 성공으로 기록하지 않는다.

## 런처와 게임 아이콘

사용자 제공 수달 원본은 `launcher_app\assets\launcher-source.png`에 보관한다. `build_icon.ps1`는 그림을 바꾸지 않고16/24/32/48/64/128/256 ICO로 변환하며 GUI EXE와 창 아이콘에 내장한다.

게임은 `renpy_project\icon.ico`를 EXE 빌드 아이콘으로 쓰고, `game\options.rpy`의 `config.window_icon = "images/ui/app_icon.png"`가 실행 중 창·작업표시줄 아이콘을 지정한다. PNG는 같은 ICO의256px 프레임이다. 이 구분은 [Ren'Py Windows 아이콘 설정](https://www.renpy.org/doc/html/build.html#special-files)과 [창 아이콘 안내](https://www.renpy.org/doc/html/gui.html#window-icon)에 따른다.

증분 게시 도구는 SDK의 공식 `change_icon.change_icons`로 **격리 snapshot의** `CampusRomance.exe`를 처리한다. 원본 SDK와 이전 배포 EXE는 보존하고, PE 코드 섹션·진입점 불변과7개 아이콘 프레임 일치를 확인한다. 따라서 게임 아이콘 변경도 이후 일반 게임 업데이트에 포함된다.

## 저장 보존과 복구

저장은 PC에 남고 feed에는 포함하지 않는다. 런처는 `saves`, `game/saves`, `persistent`, 사용자 로그·스크린샷 등을 관리 대상으로 받지 않는다. Game 폴더 전체를 삭제하지 않으며 이전의 서명된 관리 파일만 갱신한다.

변경 파일을 staging하고 조각·완성 파일의 크기와 SHA256을 확인한 뒤 적용한다. journal과 backup을 먼저 만들고 적용 오류를 복구한다. 중단된 트랜잭션은 다음 **설치·업데이트**에서 복구하며 게임 실행 중이거나 같은 위치를 갱신 중이면 충돌을 안내한다.

이 개발 PC의 기존 기록은 `D:\CampusRomance_VN\renpy_project\saves`에 있다. GUI 첫 설치에서 **이 PC의 기존 플레이 기록 가져오기**를 선택했고 대상에 기존 기록이 없을 때만 `.save`와 `persistent`를 복사한다. 원본은 이동·삭제·덮어쓰지 않으며 일반 업데이트에는 이 가져오기가 실행되지 않는다. 실제 사용자 기록 가져오기는 아직 실행하지 않았다.

## 초기 배포·아이콘 업데이트 검증 기록 (0.3.0)

| 단계 | 현재 상태 |
| --- | --- |
| 제품 페이지 | 로컬 브라우저 24검사 및 실제 공개 페이지 15검사 PASS, 1280/768/390 표시 확인 |
| 런처·증분 갱신 | 격리 CLI 21케이스, metadata race, GUI 기록 가져오기 fixture 4케이스 PASS |
| 오프라인 실행 | 네트워크0 확인, 실제 Play 경로를 창 없는 stub으로 검증 |
| R2 Worker | Mock R2 16케이스 PASS, CAS race·불변 서명·pointer 실패 보존 포함 |
| 현재 네이티브 payload 준비 | PASS, 1803파일·525,545,021바이트, 개인 저장 제외, ZIP 생성 없음 |
| Site 접근 범위 | 사용자 승인 후 public, revision 2 |
| 첫 실제 R2 업로드·활성화 | PASS, build2026110801, 1799개 조각, 서명된 manifest 활성화 |
| 게임 아이콘 증분 게시 | PASS, build2026110802, 1755개 조각 재사용·새46개/2,001,262바이트 업로드 |
| 같은 feed 재게시 | PASS, 원격1799개 재사용·전송0바이트·동일 manifest 유지 |
| 현재 실제 HTTPS 런처 연결 | PASS, QA override 없는 production CLI에서 build2026110802·1803파일·서명 확인 |
| 현재 게임 EXE 공개 다운로드 | PASS, manifest808078B/SHA 일치, EXE청크173056B GET·조립 후 검사한 게임 EXE와 SHA 일치 |
| 초기 실제 HTTPS 파일 다운로드 | PASS, manifest807147B·고정서명344B 일치, 대표청크65210B 및8MiB GET/SHA256 일치 |
| 초기 공개 페이지 버전 표시 | PASS, metadata200/ready, 버전0.3.0·build2026110801. 현재 피드는802를 반환 |
| 전체 네이티브 게임의 공개 HTTPS 첫 설치 | 수행하지 않음; 격리 updater fixture 설치·갱신과 실제 manifest/다운로드를 구분 |
| 사용자 실제 전체 게임 설치·기록 가져오기 | 실행하지 않음 |
| 개발 PC Launcher1.1 바로가기 | D:\CampusRomance_VN\Installed의 런처 EXE만 준비, 바탕화면 바로가기 생성·대상/아이콘 확인 |
| 개발 PC 기존 게임 바로가기 | 실행 대상 START_GAME.cmd를 유지하고 수달 icon.ico만 지정 |

Launcher1.1과 게임 아이콘 후속 검증은 `tests\launcher_ui_20261108\README.md`에 별도로 기록한다. 57개 UI assertion, Win32/Shell의7개 크기 아이콘 검사, 실제 patched 게임 엔진의 private-copy Lint가 통과했다. `.rsrc` 아이콘 처리 시 공식 SDK가 DIB의 biSizeImage를0으로 정규화하지만 그림의 픽셀과 실행 코드·진입점은 유지된다. 현재 게시 후 검증 근거는 `game-live-1794075454256\RESULT.json`이다. 기존 게임 원본56파일 중 의도한 options.rpy 아이콘 설정만 변경됐고 기존 저장9파일은 SHA256이 동일하다.

검증 근거는 `tests\launcher_update_20261108`의 `public-live-1794071845422\RESULT.json`, `public-feed-1794072116360\RESULT.json`, `public_first_upload.json`, `public_repeat_upload.json`에 있다. 런처 계약은 `launcher_app\README.md`, 페이지 계약은 `launcher_storefront_source\DESIGN.md`와 `README.md`를 따른다. 이전 브라우저 실험과 원본 SHA256 보존 검증은 `WEB_TEST_WORKFLOW.md`에 보존했다.
