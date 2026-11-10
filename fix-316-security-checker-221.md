# Fix 316: security-checker: LC_ALL=C is ignored and the report language comes from LANG

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(language): `LC_ALL=C` を明示しても `LANG` の言語でレポートを書かせる
- Bug report: number 221 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/221))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/316-security-checker-221.patch](fixes/316-security-checker-221.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/316-security-checker-221.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-316-security-checker-221.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-316-security-checker-221.html

## The bug

resolve_language in src/security_checker/language.py skips a locale variable whose value is C or POSIX and reads the next variable. A user who sets LC_ALL=C on purpose still gets the report in the language of LANG.

## The fix

resolve_language now stops at the first locale variable that is not empty. A value of C or POSIX gives the default (English). Only an empty or unset variable moves on to the next one. The docstring states the rule. A new file tests/unit/test_language_explicit_c_locale.py covers both cases.

## Files changed

- src/security_checker/language.py
- tests/unit/test_language_explicit_c_locale.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 316-security-checker-221.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 221.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. This patch applies together with the patch of fix 314 on this shelf (the same file).

## Search words

security-checker language resolve_language LC_ALL=C LANG locale POSIX default English auto first non-empty variable

## The full patch

`````diff
diff --git a/src/security_checker/language.py b/src/security_checker/language.py
index 2473d2e..c34bddd 100644
--- a/src/security_checker/language.py
+++ b/src/security_checker/language.py
@@ -42,14 +42,18 @@ LANGUAGE_NAMES = {
 
 
 def resolve_language(configured: str, environ: Mapping[str, str] | None = None) -> str:
-    """設定値を実際の言語タグに解決する. `auto` のときだけ環境を見る."""
+    """設定値を実際の言語タグに解決する. `auto` のときだけ環境を見る.
+
+    空でない最初のロケール変数で判定を打ち切る (#221)。その値が C / POSIX なら既定 (英語)。
+    変数が空・未設定のときだけ次の変数を見る。
+    """
     if configured != AUTO:
         return configured
     source = environ if environ is not None else os.environ
     for variable in LOCALE_VARS:
-        tag = _tag_from_locale(source.get(variable))
-        if tag is not None:
-            return tag
+        value = source.get(variable)
+        if value:
+            return _tag_from_locale(value) or DEFAULT_LANGUAGE
     return DEFAULT_LANGUAGE
 
 
diff --git a/tests/unit/test_language_explicit_c_locale.py b/tests/unit/test_language_explicit_c_locale.py
new file mode 100644
index 0000000..a4e2a77
--- /dev/null
+++ b/tests/unit/test_language_explicit_c_locale.py
@@ -0,0 +1,21 @@
+"""auto の言語推定: 空でない最初のロケール変数で打ち切ること (#221)."""
+
+from __future__ import annotations
+
+import pytest
+
+from security_checker.language import resolve_language
+
+
+@pytest.mark.parametrize("neutral", ["C", "POSIX", "C.UTF-8"])
+def test_explicit_c_locale_wins_over_a_later_variable(neutral: str) -> None:
+    environ = {"LC_ALL": neutral, "LANG": "ja_JP.UTF-8"}
+
+    assert resolve_language("auto", environ) == "en"
+
+
+def test_empty_variable_falls_through_to_the_next_one() -> None:
+    """対になるケース. 空・未設定のときだけ次の変数を見る."""
+    environ = {"LC_ALL": "", "LANG": "ja_JP.UTF-8"}
+
+    assert resolve_language("auto", environ) == "ja"
`````

[Back to the shelf](README.md)
