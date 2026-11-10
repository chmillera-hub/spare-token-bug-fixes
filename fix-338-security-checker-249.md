# Fix 338: security-checker: the action always passes --fail-on so policy.fail_on in the settings file never applies

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(action): fail-on を常に `--fail-on` で渡しており、設定ファイルやプリセットの policy.fail_on が action では効かない
- Bug report: number 249 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/249))
- Project license: MIT
- Language: Python
- Test included: no
- Patch file: [fixes/338-security-checker-249.patch](fixes/338-security-checker-249.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/338-security-checker-249.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-338-security-checker-249.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-338-security-checker-249.html

## The bug

action.yml gives the input fail-on the default high and always passes --fail-on to the command. A repository that sets policy.fail_on in its settings file gets the value overridden by the action default.

## The fix

The default of the input is now empty and the action passes --fail-on only when the input holds a value (the same treatment as min-score). The settings default is still high so behaviour is unchanged when neither place sets a value. The input table in docs/github-actions.md shows the new default.

## Files changed

- action.yml
- docs/github-actions.md

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 338-security-checker-249.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 249.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- No test was added because the change is in the action file and the docs. Nobody has run the action with the change. This patch and the patch for bug report 330 of the same project change neighbouring lines and do not apply together.

## Search words

security-checker action.yml fail-on default --fail-on policy.fail_on overridden settings file github action input

## The full patch

`````diff
diff --git a/action.yml b/action.yml
index a2e1123..9387e64 100644
--- a/action.yml
+++ b/action.yml
@@ -44,8 +44,8 @@ inputs:
       fork からの PR ではシークレットが渡らないため、常にスキャンのみになる
     default: auto
   fail-on:
-    description: 'この重大度以上で失敗させる: critical | high | medium | low | none'
-    default: high
+    description: 'この重大度以上で失敗させる: critical | high | medium | low | none (空なら設定の policy.fail_on)'
+    default: ""
   min-score:
     description: このスコア未満なら失敗させる (0 で判定しない。v1 と同じ入力名)
     default: "0"
@@ -217,7 +217,8 @@ runs:
         set -uo pipefail
         dir="$RUNNER_TEMP/security-checker"
         echo "dir=$dir" >> "$GITHUB_OUTPUT"
-        args=("$COMMAND" "$TARGET" -o "$dir" -f terminal -f json -f markdown -f sarif --fail-on "$FAIL_ON")
+        args=("$COMMAND" "$TARGET" -o "$dir" -f terminal -f json -f markdown -f sarif)
+        [[ -n "$FAIL_ON" ]] && args+=(--fail-on "$FAIL_ON")
         [[ -n "$CONFIG" ]] && args+=(--config "$CONFIG")
         [[ -n "$PRESET" ]] && args+=(--preset "$PRESET")
         [[ "$MIN_SCORE" != "0" ]] && args+=(--min-score "$MIN_SCORE")
diff --git a/docs/github-actions.md b/docs/github-actions.md
index 7250be2..9f68f6d 100644
--- a/docs/github-actions.md
+++ b/docs/github-actions.md
@@ -52,7 +52,7 @@ jobs:
 | `target` | `.` | 検査対象ディレクトリ。inline コメントを使うならリポジトリ直下のままにする |
 | `mode` | `auto` | `auto` (PR は差分のみ・push は全件) / `full` / `diff` |
 | `review` | `auto` | `auto` / `true` / `false`。fork PR では常にスキャンのみ |
-| `fail-on` | `high` | この重大度以上の `confirmed` / `likely` で失敗 (`none` で判定しない) |
+| `fail-on` | (設定の値) | この重大度以上の `confirmed` / `likely` で失敗 (`none` で判定しない)。空なら設定の `policy.fail_on` (既定 `high`) |
 | `min-score` | `0` | このスコア未満で失敗 (0 で判定しない。スコアは補助指標) |
 | `comment` | `true` | PR に sticky サマリと inline コメントを投稿する |
 | `upload-sarif` | `true` | SARIF を Code Scanning に登録する |
`````

[Back to the shelf](README.md)
