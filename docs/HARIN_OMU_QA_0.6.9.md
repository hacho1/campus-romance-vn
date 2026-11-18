# Harin / Omu native QA — 0.6.9-test

**PASS — 15 accepted native cases, 74 explicit SDK assertions.** Ren'Py 8.5.3 Windows / Python 3.12.7 ran with SDL dummy and the existing software-renderer compatibility fixture. All native saves and persistent writes were isolated under `D:/CampusRomance_VN/tests/harin_omu_069`. No foreground activation, desktop input, cursor movement, generated art, or real-save write/restore was used.

## Accepted evidence

| Native group | Cases | SDK assertions | Log |
| --- | ---: | ---: | --- |
| Harin test menu, H01→H06 Replay continuity, common dispatch, manual secret | 4 | 16 | `replay-first.log` |
| Ordinary scores/save/load/rollback/gates, Harin BAD, Omu revised BAD and positive paths | 6 | 36 | Six passing cases in `ordinary-third.log` |
| Harin ordinary happy + actual secret, mixed recovery | 2 | 15 | `completion-final.log` |
| Actual ordinary 0.6.3 Omu save upgrade and native roundtrip | 1 | 3 | `upgrade-second.log` |
| All five secret buttons and final visible geometry | 1 | 2 | `buttons-refined-final.log` |
| Independent native save and persistent sentinel | 1 | 2 | `isolation-final.log` |

Logs, fixtures, the candidate, exact source hashes, and the machine-readable `RESULT.json` are in `tests/harin_omu_069`.

Compile and lint passed. Lint counted 31,440 dialogue blocks, 119 menus, and 65 screens. The candidate was seeded from the 85 compiled scripts in the official `2026111203` release before compilation, preserving the supported Ren'Py name history.

## Behavior checked

- The actual test selector exposes Harin H01–H06 and SECRET. Its selection text uses “하린 시크릿”. The existing five secret entries are retained.
- H01→H06 stays in one official Replay. Player name, choices, award IDs, red and black hearts, phone history, and the isolated persistent object survive every boundary. Exiting restores the caller and its collections. Common CH07 with `selected_route == "lumi"` dispatches H01 in the same Replay.
- Native catalog awards use literal +5/+10 values; duplicate calls do not award twice. Ordinary native Harin save/load retains scores, choices, phone, name, and chapter context. Native rollback removes the choice and award, then reapplies it exactly once.
- Actual H04/H05/H06 core menu selections reach ordinary happy, mixed recovery, and repeated-core-choice BAD. The mixed path cannot record happy before the authored H06 SC05-H recovery hook; repair changes neither scores nor history. The new BAD scenes and epilogue finish before `lumi_bad` is recorded.
- Harin secret is gated by a real happy clear. An actual happy endpoint enables its secret replay, which completes. Manual test-menu secret prerequisites stay inside the Replay's persistent copy.
- Revised Omu choice bodies set the new authored flags. O04/O06 conditional memories require the corresponding actual new scalar values. The new BAD epilogue runs before `omu_bad` unlocks. Positive Omu choices still reach happy, and secret access still requires happy.
- A real ordinary 0.6.3 Omu O04 save loaded and roundtripped without changing its original +45 hearts, choices, award IDs, phone history, or chapter context. New distortion flags default false; old history does not fabricate the new events. Resuming at an earlier Say is the engine's normal saved checkpoint behavior.
- Secret buttons appear only for their actual happy clears. A separate, explicitly synthetic QA-only all-happy fixture verifies all five together; it does not stand in for earned story clears.

## UI correction verified

Screenshot review caught lower-half clipping in the secret controls. Root changed only `screens_ending_diary.rpy` after the initial freeze: footer y850→800, secret slots y920→870, and the paw's position/size. The affected native UI case alone was rerun, and its screenshot was viewed again.

All five actual focus rectangles are 252×52 at y870, with x positions 305, 572, 839, 1106, and 1373. Their bottom edge is y922, inside the visible diary sheet. Final evidence: `tests/harin_omu_069/screenshots/current/ending_five_secret_buttons.png`. The before-fix screenshot is retained separately. Earlier happy/BAD endpoint screenshots document functional states before this layout-only correction.

## Integrity and limits

Final candidate/live parity passed for 517 source/assets files. The post-freeze audit records exactly the authorized ending-screen file change. All 39 inventoried real save/persistent records retained their original bytes and modification times. QA never restored or modified those records.

This was bounded native sampling, not a full text readthrough: QA-only AST jumps reach authored menus, their selected effects, episode completion boundaries, and final-scene tails. Production route text, flags, scores, thresholds, and rendering screens were not replaced by the harness. Exact manuscript coverage belongs to the import/source audits.

The first harness run placed a phone marker outside a script save checkpoint; moving it before Say made the strict native state comparison valid. Two initial happy/recovery cases reached their real endpoints but failed an incorrect assertion expecting secret buttons for heroines without happy clears. Those two cases alone were rerun after separating earned gates from the five-button UI fixture. Their earlier partial assertions are excluded from the accepted total.
