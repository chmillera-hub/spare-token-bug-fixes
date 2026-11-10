# Fix 336: security-checker: the pre-commit hook reports a gitleaks crash as a leaked secret

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(contrib): pre-commit フックが gitleaks の実行エラーを「シークレットを検出」と表示する
- Bug report: number 671 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/671))
- Project license: MIT
- Language: Python
- Test included: no
- Patch file: [fixes/336-security-checker-671.patch](fixes/336-security-checker-671.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/336-security-checker-671.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-336-security-checker-671.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-336-security-checker-671.html

## The bug

contrib/host-audit/hooks/pre-commit runs gitleaks with --exit-code 1 and hides all output. Any failure of gitleaks itself (a bad option or a broken install) also ends with a non-zero code so the hook says the commit may hold a secret and hides the real error.

## The fix

The hook now passes --exit-code 99 and keeps the error output. Exit code 99 gives the existing secret message. Any other non-zero code gives a new message that says gitleaks could not run and shows what gitleaks wrote to standard error. Both cases still stop the commit.

## Files changed

- contrib/host-audit/hooks/pre-commit

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 336-security-checker-671.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 671.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- No test was added because the project has no tests for the hook scripts as far as the chatbot saw. The chatbot checked the script with bash -n and did not run the hook. The bug report does not say whether a gitleaks failure should stop the commit. The chatbot kept the stop because a check that did not run is not a pass.

## Search words

security-checker contrib host-audit pre-commit hook gitleaks --exit-code 99 execution error stderr secret false alarm

## The full patch

`````diff
diff --git a/contrib/host-audit/hooks/pre-commit b/contrib/host-audit/hooks/pre-commit
index 6234647..f6e238f 100755
--- a/contrib/host-audit/hooks/pre-commit
+++ b/contrib/host-audit/hooks/pre-commit
@@ -11,11 +11,19 @@ if command -v gitleaks >/dev/null 2>&1; then
   else
     sub=(protect --staged)
   fi
-  if ! gitleaks "${sub[@]}" --exit-code 1 >/dev/null 2>&1; then
+  # 検出 (99) と gitleaks 自体の実行エラー (それ以外の非 0) を区別する (#671)
+  leak_err=$(gitleaks "${sub[@]}" --exit-code 99 2>&1 >/dev/null)
+  leak_status=$?
+  if [[ "$leak_status" -eq 99 ]]; then
     echo "❌ コミットにシークレットが含まれている可能性があります (gitleaks)"
     echo "   詳細: gitleaks ${sub[*]} --verbose"
     echo "   誤検知なら: git commit --no-verify"
     exit 1
+  elif [[ "$leak_status" -ne 0 ]]; then
+    echo "❌ gitleaks を実行できませんでした (終了コード $leak_status)。シークレット検査は行われていません"
+    [[ -n "$leak_err" ]] && echo "$leak_err"
+    echo "   一時的に外すなら: git commit --no-verify"
+    exit 1
   fi
 else
   # gitleaks が無い場合の簡易パターン検査
`````

[Back to the shelf](README.md)
