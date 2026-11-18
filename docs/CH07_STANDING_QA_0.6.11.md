# CH07 / private standing native QA — 0.6.11-test

Result: **PASS**

Runs use the Ren’Py 8.5.3 native test runner, SDL dummy video/audio, software drawing, and the production screens. The test-only software scaling shim avoids the SDK Windows software blitter fault; it does not replace the game renderer or screen logic. No foreground window, physical mouse, or keyboard input is used.

Only the frozen product copy under `tests/ch07_standing_0611/candidate` is compiled. It starts with all 95 published compiled statement seeds from build 2026111401. Product source and artwork hashes are recorded in `source_hashes.json` and checked against both the authoritative source and candidate.

## Coverage

- All six CH07 illustration intervals: exact source filename/line at preceding Say, first Say, last Say, and following Say. The five private paths use the actual final choice and confirmation menu; each collects only its own CH07 LD CG. The reunion uses the SPECIAL SD card; private cards use ROMAN, SIA, DARIM, OMU and HARIN.
- Native mid-CG save/load, SD and LD end-boundary rollback, standing restoration, all six gallery cards and thumbnails, read-only test preview, missing-art start and active-load fallback.
- Ten happy/bad endpoint titles in normal play and the official isolated Replay. The actual final authored Say reaches original flags/recording, then the shared narrator Say displays the canonical ENDINGS title. The ending Say remains until the test issues a user advance, then the existing gallery or Replay return occurs.
- Endpoint tests are bounded completion tests, not full route playthroughs. Harin fixtures seed the pre-existing relationship evidence inside isolated QA saves; the authored final completion flags and original recording guard still run. The title helper is verified read-only for endings, CGs, notes, counters, choices and flags, and rejects unearned/unknown/secret titles.
- Bounded previous CH06 Darim/Harin CG regression reuses the prior native scenarios in a QA-only namespace.
- A separate distribution-style copy contains 97 compiled product scripts and zero product `.rpy` files. Two additional native cases verify a private standing Say and the new ending Say without any authored product source; only QA fixtures retain `.rpy` sources.
- Private standing coverage is source-driven: actual early and late Say statements for each heroine, authored expressions and multi-cast speaker focus, and source exclusions for phone, MC-alone, pending Roman expressions and secret costumes. Detailed case rows are in the native result JSON.

## Native runs

| Run | Result |
| --- | --- |
| `compile-final` | PASS |
| `lint-final` | PASS |
| `isolation-final` | PASS |
| `cg-final` | PASS |
| `gallery-final` | PASS |
| `endings-normal-final` | PASS |
| `endings-replay-final` | PASS |
| `standing-final` | PASS |
| `oldch06-final` | PASS |
| `sourceless-final` | PASS |

Native cases passed: **71**. Native result records: **124**. Captured frames: **56**.

## Save isolation and artifacts

`CAMPUS_SAVE_DIR`, `--savedir`, TEMP and TMP all point to QA directories on D:. The isolation fixture filters both Ren’Py save-location initialization passes before persistent merging. It checks every active save location and writes a QA-only sentinel save/persistent record.

`real_saves_before.json` and `real_saves_after.json` inventory save/persistent SHA-256 and mtime under the real D: save roots. `real_save_audit.json` records exact equality. No real player files are restored or modified.

- Machine result: `tests/ch07_standing_0611/RESULT.json`
- Native assertions: `tests/ch07_standing_0611/native_results.json`
- Source parity: `tests/ch07_standing_0611/source_parity.json`
- Native frames: `tests/ch07_standing_0611/screenshots/current/`
- Frozen source hashes: `tests/ch07_standing_0611/source_hashes.json`
