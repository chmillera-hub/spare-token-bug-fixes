# Fix 317: security-checker: the --exclude help does not say that the option replaces the default excludes

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: docs(cli): `--exclude` の help が、既定の除外（vendor・node_modules など）を置き換えることを書いていない
- Bug report: number 228 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/228))
- Project license: MIT
- Language: Python
- Test included: no
- Patch file: [fixes/317-security-checker-228.patch](fixes/317-security-checker-228.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/317-security-checker-228.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-317-security-checker-228.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-317-security-checker-228.html

## The bug

The help of --exclude for scan and review in src/security_checker/cli.py says only exclude pattern (may be given more than once). The option replaces the excludes from the settings and the defaults (vendor and node_modules and others) and the help does not say so.

## The fix

Both help texts now say that the option replaces the settings and the default target.exclude and does not add to them (the wording the bug report gives).

## Files changed

- src/security_checker/cli.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 317-security-checker-228.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 228.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- No test was added because only two help texts changed. The bug report also raises a possible new option --exclude-add as something to consider. This patch does not add an option.

## Search words

security-checker cli --exclude help replaces default excludes target.exclude vendor node_modules scan review

## The full patch

`````diff
diff --git a/src/security_checker/cli.py b/src/security_checker/cli.py
index 6f0a497..abc0d87 100644
--- a/src/security_checker/cli.py
+++ b/src/security_checker/cli.py
@@ -232,7 +232,11 @@ def scan(
         typer.Option("--strict/--no-strict", help="スキャナの失敗を exit 3 にする (既定: 有効)"),
     ] = None,
     exclude: Annotated[
-        list[str] | None, typer.Option("--exclude", help="除外パターン (複数指定可)")
+        list[str] | None,
+        typer.Option(
+            "--exclude",
+            help="除外パターン (複数指定可)。設定と既定の target.exclude を置き換える (追加ではない)",
+        ),
     ] = None,
     output_dir: Annotated[
         Path | None,
@@ -302,7 +306,11 @@ def review(
         int | None, typer.Option("--max-candidates", min=1, help="レビューする候補の上限")
     ] = None,
     exclude: Annotated[
-        list[str] | None, typer.Option("--exclude", help="除外パターン (複数指定可)")
+        list[str] | None,
+        typer.Option(
+            "--exclude",
+            help="除外パターン (複数指定可)。設定と既定の target.exclude を置き換える (追加ではない)",
+        ),
     ] = None,
     output_dir: Annotated[
         Path | None,
`````

[Back to the shelf](README.md)
