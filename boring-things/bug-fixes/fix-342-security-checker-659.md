# Fix 342: security-checker: the security model page does not say that the trace keeps the full answer of the model

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: docs(security-model): トレースに LLM の応答全文が残ることを書いていない
- Bug report: number 659 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/659))
- Project license: MIT
- Language: Python
- Test included: no
- Patch file: [fixes/342-security-checker-659.patch](fixes/342-security-checker-659.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/342-security-checker-659.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-342-security-checker-659.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-342-security-checker-659.html

## The bug

Section 4 of docs/security-model.md says that by default the trace keeps only a SHA-256 hash of the prompt so that code does not stay on disk in clear text. The trace also stores the full answer of the model (the field raw of each call) with the default settings and the answer quotes code. A reader concludes that no code stays on disk.

## The fix

Section 4 now has one more list item that says the full answer of the model is saved in each call file even with the default settings and that the answer can quote the reviewed code and that the trace folder needs the same care as the code when the folder is uploaded as a CI artifact.

## Files changed

- docs/security-model.md

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 342-security-checker-659.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 659.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- Only documentation changed so no test was added. The chatbot read the code that builds the trace record (the field raw in src/security_checker/review/reviewer.py) and saw no condition on save_prompts around that field. The wording is the chatbot's own.

## Search words

security-checker docs security-model trace raw response full answer saved save_prompts artifact code on disk

## The full patch

`````diff
diff --git a/docs/security-model.md b/docs/security-model.md
index eab3123..948458a 100644
--- a/docs/security-model.md
+++ b/docs/security-model.md
@@ -50,6 +50,9 @@ gitleaks が検出した秘密の値をそのまま外部 LLM に送るのは、
 - 既定では**プロンプト全文を保存せず、SHA-256 ハッシュのみ**を残す。コードが平文でディスクに残るのを避けるため。
 - `output.save_prompts: true` にすると全文を保存する。この場合は起動時に警告を出す。
   出力ディレクトリを `.gitignore` に入れること。
+- **LLM の応答は、既定でも全文 (`calls/*.json` の `response.raw`) を保存する**。応答は検査対象のコードを
+  引用することがあるため、既定の設定でもコードの一部が平文でディスクに残りうる。trace を CI の artifact
+  として上げるときは、検査対象のコードと同じ扱い (公開範囲・保存期間) にすること。
 
 ## 5. プロンプトインジェクション
`````

[Back to the shelf](README.md)
