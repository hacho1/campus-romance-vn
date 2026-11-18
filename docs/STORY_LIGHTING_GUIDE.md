# 밤 배경과 저장 복원 가이드

기존 CH01~CH03의 방 / 밤 캠퍼스 두 배경 종류만 다룹니다. 대사·선택·캐릭터 그림·SD/LD 컷은 변경하지 않습니다.

## 파일

- 낮 원본: game/images/backgrounds/room.png, campus.png
- 별도 밤 그림: game/images/backgrounds/room_night.png, campus_night.png
- 등록·표시 함수: game/systems/story_lighting.rpy
- native QA: game/tests/story_lighting_followup.rpy

두 밤 그림은 built-in image_gen의 lighting-weather 편집으로 만들었습니다. 방 창밖은 남색 밤하늘·달·어두운 나무·학교 창빛, 실내는 기존 스탠드의 따뜻한 조명으로 바꿨습니다. 캠퍼스는 밤하늘·달·별·기존 가로등의 빛을 사용합니다. 구도와 기존 소품을 보존하도록 지시하고 출력물을 시각적으로 확인했습니다. 인물·문자·UI는 넣지 않았습니다.

낮 원본은 덮어쓰지 않았습니다. 기존 night 파일은 배우/UI가 포함된 QA 캡처이므로 클린 배경 자산으로 재사용하지 않았습니다.

**해상도 한계:** 방 원본은 1920×1080, 캠퍼스 원본은 1672×941입니다. 방 편집에 1920×1080을 두 차례 요청했으나 도구는 모두 1672×941로 저장했습니다. 선택한 두 밤 자산의 실제 크기는 1672×941입니다. 임의 코드 리사이즈나 다른 생성 API로 전환하지 않았습니다. 기존과 같은 1920×1080 Ren’Py Transform으로 표시하므로 화면 비율과 배치는 유지되지만, 방 밤 원화가 원본과 동일한 픽셀 해상도라는 주장은 하지 않습니다.

## 표시 계약

story_background_display(bg, light)는 하나의 Displayable을 반환합니다.

- day: 기존 낮 경로와 기존 흰색 Tint.
- evening: 기존 경로와 기존 따뜻한 Tint.
- night: 등록된 별도 밤 PNG/WebP가 있으면 사용하고 밤 Tint를 더하지 않음.
- 밤 파일 누락: 기존 배경과 이전 밤 Tint로 계속 플레이. 파일 누락 fallback이지 창밖까지 밤으로 다시 그린 결과는 아님.
- 알 수 없는 시간대: day. 없는 배경 ID: 기존 corridor SVG까지 순서대로 검색.

별도 밤 그림에는 IdentityMatrix()를 명시합니다. 색을 어둡게 덧칠하지 않으며, 불러오기에서 같은 태그를 교체할 때 구 파란 Tint 상태가 전이되는 것도 막습니다.

| 일반 ID | 호환 별칭 | 밤 이미지 |
| --- | --- | --- |
| room | 없음 | images/backgrounds/room_night.png |
| campus | night_campus | images/backgrounds/campus_night.png |

기존 prep_room → clubroom 별칭도 유지합니다. story_background_info(bg, light)는 선택 경로·전용 밤 이미지 여부·Tint를 돌려주는 진단 함수입니다. story_runtime.rpy의 story_scene()이 story_light 저장과 helper 호출을 담당합니다.

## 불러오기와 되돌리기

story_lighting_restore_after_load()는 config.after_load_callbacks에 등록됩니다. 실제 저장을 불러올 때는 before_load에서 엔진 세션에 일회성 복구 표시를 남기고, start_interact에서 다시 복구합니다. SDK가 불러온 say 상호작용을 재개하며 초기 after_load의 store/SceneList 변경을 되돌릴 수 있으므로, 실제 첫 표시 직전에 밤 메타데이터와 master 배경을 함께 재구성합니다. 표시 후 플래그는 제거하며 매 프레임·일반 되돌리기에 이 작업을 반복하지 않습니다. 실제 story_light는 계속 저장·되돌리기가 되는 store 변수입니다.

1. 새 story_light 필드가 day인 구 저장도 night_campus 또는 끝이 밤인 위치 이름이면 night로 복구합니다.
2. 공식 story 진행 중이고 master에 기존 story_background 태그가 있을 때만 그 태그를 갱신합니다.
3. scene()/story_scene()을 다시 호출하지 않습니다. 수치·선택·캐스트·현재 대사·음악을 바꾸지 않습니다.
4. ld_cg와 sd_events 레이어/현재 컷에는 손대지 않습니다. 배경은 그 아래 master에서 복구되어 컷이 끝난 뒤에도 밤으로 남습니다.
5. 공식 story/master 배경 태그가 없는 0.1 저장 화면에는 새 배경을 끼워 넣지 않습니다.

되돌리기는 Ren’Py가 저장한 story_light와 SceneList Displayable을 함께 복원합니다. 비가역적인 외부 화면 상태를 만들지 않습니다.

## 교체

같은 구도의 고해상도 그림을 준비하면 두 night PNG를 교체하세요. 같은 stem의 WebP도 검색합니다. 파일명이 달라지면 등록표의 night 경로를 수정합니다.

방은 침대·책상·의자·창틀·커튼·책장·식물의 위치를 유지하고 창밖에 낮 구름/밝은 하늘이 남지 않게 합니다. 캠퍼스는 벤치·계단·건물·가로등·벚나무의 위치를 유지합니다.

## 검증

준비한 11개 native 사례는 낮/저녁 유지, 실제 밤 자산 선택, 파일 누락 fallback, 구 시간대 기본값의 저장·불러오기 모사, 두 밤 장면의 저장 복원, 낮↔밤 되돌리기, SD/LD 유지와 master 배경 복구를 확인합니다.

이 문서 작성자가 엔진을 실행한 결과는 아닙니다. 루트 작업자가 D드라이브 QA 복사본에서 test story_lighting_followup --overwrite-screenshots를 실행하고 실제 로그·캡처를 완료 근거로 남깁니다. 구 시간대 테스트는 새 테스트 저장에서 예전 기본값을 모사한 것이며 모든 외부 구 저장을 검증했다는 뜻은 아닙니다.

## 최종 프롬프트

도구: built-in image_gen. CLI/API fallback 사용하지 않음.

### 방

> Use case: lighting-weather edit. Edit target: the supplied empty university student's room background. Create a NIGHT variant of this exact background for a Korean visual novel. Retain the same 1920x1080 16:9 canvas, camera perspective, bed at left, desk and chair at right, shelves, plants, curtains, window frames, wall and floor geometry, and all existing objects. Change only time of day and illumination. The window exterior MUST visibly be true late-night: deep navy sky with subtle stars and a small distant moon, dark tree and cherry blossom silhouettes, university building outside mostly dark with a few warm lit windows. Remove all blue daytime sky, bright white daytime clouds, direct sunlight and bright daytime greenery. Keep the interior comfortably readable with the EXISTING right desk lamp switched on, warm amber light falling across the desk and bed, soft cool night fill through the window. Preserve the original polished Japanese anime background painting style and gentle campus romance mood. Do not add, remove, or move furniture or props. No people, no character silhouettes, no text, no UI, no watermarks. This is one complete clean background image, not a collage or a before/after comparison. Match the supplied image composition exactly.

### 캠퍼스

> Use case: lighting-weather edit. Edit target: the supplied empty cherry-blossom university courtyard background. Create the true NIGHT version of this EXACT scene for a Korean visual novel. Preserve the original 1672x941 wide canvas and framing if possible, with the same camera angle, university building silhouette and windows, entrance stairs at right, central paved paths, left wooden bench, flower beds and cherry trees arching across the top corners. Change only time of day and illumination. The sky is unmistakably deep navy blue at late night with a small moon and restrained stars; daytime white clouds and bright blue sky are gone. Switch on the EXISTING path lamps to cast soft warm pools of light, with only a few university windows warmly lit. Make cherry blossoms and foliage softly moonlit, darker and cooler than daytime, while the path, bench and entrance remain readable for dialogue scenes. Preserve the polished anime background style and the calm romantic mood of this same campus. Do not add, remove or reposition objects, architecture, signs or props. No people or silhouettes, no character illustrations, no text, no UI, no watermarks, no montage or before/after comparison. One complete clean background, matching the original composition.



## 자산 지문

| 파일 | 실제 크기 | SHA-256 |
| --- | --- | --- |
| room.png | 1920x1080 | 6c579c676200cffca54892d3f2ac106e82b6d62663b95572babfc2f38d7afcdd |
| campus.png | 1672x941 | 846c39c27404d5cd3031cd5906730141606d05793d14ae95fea1e8c71a81b9ea |
| room_night.png | 1672x941 | 7e19c1c7b2e392cb9557f37b54386a776dcd92c56e71e8d4e4ecc5daba331666 |
| campus_night.png | 1672x941 | 6884d0d34e577e7343ba79f1cdb939734a00527f58ab5e3c1829cc8381c4c6bb |
