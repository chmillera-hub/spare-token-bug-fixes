# Fix 339: security-checker: the SARIF upload category of the action is fixed so a monorepo cannot upload more than one result

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: feat(action): upload-sarif の category を入力で変えられるようにし、モノレポで複数の target を検査できるようにする
- Bug report: number 330 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/330))
- Project license: MIT
- Language: Python
- Test included: no
- Patch file: [fixes/339-security-checker-330.patch](fixes/339-security-checker-330.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/339-security-checker-330.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-339-security-checker-330.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-339-security-checker-330.html

## The bug

action.yml uploads report.sarif with the fixed category security-checker. A workflow that uses the action more than once in one repository (a monorepo) overwrites the earlier result because the category is the same.

## The fix

A new input sarif-category (default security-checker as before) sets the category of the upload. The input table and the SARIF section of docs/github-actions.md describe the input.

## Files changed

- action.yml
- docs/github-actions.md

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 339-security-checker-330.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 330.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- No test was added because the change is in the action file and the docs. Nobody has run the action with the change. This patch and the patch for bug report 249 of the same project change neighbouring lines and do not apply together.

## Search words

security-checker action.yml upload-sarif category sarif-category input monorepo code scanning overwrite

## The full patch

`````diff
diff --git a/action.yml b/action.yml
index a2e1123..e0ded59 100644
--- a/action.yml
+++ b/action.yml
@@ -49,6 +49,9 @@ inputs:
   min-score:
     description: このスコア未満なら失敗させる (0 で判定しない。v1 と同じ入力名)
     default: "0"
+  sarif-category:
+    description: Code Scanning に上げる SARIF の category (モノレポで複数回使うときは呼び出しごとに変える)
+    default: security-checker
   comment:
     description: PR に sticky サマリと inline コメントを投稿するか
     default: "true"
@@ -297,13 +300,13 @@ runs:
         fi
         echo "upload=true" >> "$GITHUB_OUTPUT"
 
-    # tool 名と category は security-checker に固定する。Ruleset はこの名前をキーにする (§18.4.4)
+    # tool 名は security-checker に固定する。category の既定も同じで、Ruleset はこの名前をキーにする (§18.4.4)
     - name: SARIF をアップロード
       if: always() && steps.sarif.outputs.upload == 'true'
       uses: github/codeql-action/upload-sarif@9b3254085494b55a0f7c4c2b3d2d52cc712ce370 # v4.39.1
       with:
         sarif_file: ${{ steps.run.outputs.dir }}/report.sarif
-        category: security-checker
+        category: ${{ inputs.sarif-category }}
         # workflow_run から呼ぶときは PR に紐づける。指定しないと既定ブランチの結果になる (§18.4.3)
         ref: ${{ inputs.pr-number != '' && format('refs/pull/{0}/head', inputs.pr-number) || '' }}
         sha: ${{ inputs.pr-number != '' && inputs.head-sha || '' }}
diff --git a/docs/github-actions.md b/docs/github-actions.md
index 7250be2..285169e 100644
--- a/docs/github-actions.md
+++ b/docs/github-actions.md
@@ -54,6 +54,7 @@ jobs:
 | `review` | `auto` | `auto` / `true` / `false`。fork PR では常にスキャンのみ |
 | `fail-on` | `high` | この重大度以上の `confirmed` / `likely` で失敗 (`none` で判定しない) |
 | `min-score` | `0` | このスコア未満で失敗 (0 で判定しない。スコアは補助指標) |
+| `sarif-category` | `security-checker` | Code Scanning に上げる SARIF の category。モノレポで 1 つの workflow から複数回使うときは、呼び出しごとに別の値にする |
 | `comment` | `true` | PR に sticky サマリと inline コメントを投稿する |
 | `upload-sarif` | `true` | SARIF を Code Scanning に登録する |
 | `gitleaks-version` / `trivy-version` / `osv-scanner-version` / `semgrep-version` | 空 (固定版) | スキャナの版。空なら [`scripts/scanner-versions.sh`](../scripts/scanner-versions.sh) の版を固定した sha256 で検証して入れる。別の版や `latest` はリリース側のチェックサムで検証し、警告を出す |
@@ -178,7 +179,7 @@ fork PR はこれで検出を減らせます。コードが実行されるわけ
 
 SARIF は次の規約で作られます (§18.3〜18.4)。
 
-- `tool.driver.name` と category は常に `security-checker`。Ruleset はこの名前で指定します。
+- `tool.driver.name` は常に `security-checker`。category の既定も `security-checker` で、入力 `sarif-category` で変えられます。Ruleset はこの名前で指定します。
 - `level` は**スキャナの severity** で決めます。LLM の判定で決めると、非決定性で alert が
   開いたり閉じたりするためです。LLM の判定は `message` と `properties` に載ります。
`````

[Back to the shelf](README.md)
