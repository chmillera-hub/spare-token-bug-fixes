# Fix 314: security-checker: auto language detection gives zh_TW and zh_CN the same language and drops @latin

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(language): auto でロケールから言語を推定するとき、地域と文字体系を捨てる（zh_TW も zh_CN も「Chinese」になる）
- Bug report: number 305 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/305))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/314-security-checker-305.patch](fixes/314-security-checker-305.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/314-security-checker-305.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-314-security-checker-305.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-314-security-checker-305.html

## The bug

_tag_from_locale in src/security_checker/language.py keeps only the language part of the locale. zh_TW and zh_CN both become zh (Chinese) and sr_RS@latin becomes sr. A reader of traditional Chinese can get a report in simplified Chinese.

## The fix

_tag_from_locale now returns zh-Hant for the regions TW and HK and MO and zh-Hans for every other zh locale and maps @latin and @cyrillic to -Latn and -Cyrl. LANGUAGE_NAMES gains zh-hant and zh-hans. The patch updates one line of tests/unit/test_language.py (zh_CN now gives zh-Hans) and adds tests/unit/test_language_auto_keeps_script.py.

## Files changed

- src/security_checker/language.py
- tests/unit/test_language.py
- tests/unit/test_language_auto_keeps_script.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 314-security-checker-305.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 305.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot ran a separate scratch copy of the new function against the eleven locales of the new test and all eleven gave the expected tag. The chatbot did not run the project's tests. The names Traditional Chinese and Simplified Chinese in LANGUAGE_NAMES are the chatbot's wording. A tag such as sr-Latn has no entry in LANGUAGE_NAMES so the prompt names the tag.

## Search words

security-checker language auto locale zh_TW zh_CN zh-Hant zh-Hans @latin @cyrillic _tag_from_locale LANGUAGE_NAMES

## The full patch

`````diff
diff --git a/src/security_checker/language.py b/src/security_checker/language.py
index 2473d2e..6c10302 100644
--- a/src/security_checker/language.py
+++ b/src/security_checker/language.py
@@ -38,6 +38,8 @@ LANGUAGE_NAMES = {
     "tr": "Turkish",
     "vi": "Vietnamese",
     "zh": "Chinese (中文)",
+    "zh-hans": "Simplified Chinese (简体中文)",
+    "zh-hant": "Traditional Chinese (繁體中文)",
 }
 
 
@@ -53,14 +55,33 @@ def resolve_language(configured: str, environ: Mapping[str, str] | None = None)
     return DEFAULT_LANGUAGE
 
 
+#: 繁体字を使う地域. それ以外の zh は簡体字として扱う (#305)
+_TRADITIONAL_CHINESE_REGIONS = frozenset({"tw", "hk", "mo"})
+#: ロケールの修飾子 (@latin など) から決める文字体系
+_SCRIPT_BY_MODIFIER = {"latin": "Latn", "cyrillic": "Cyrl"}
+
+
 def _tag_from_locale(value: str | None) -> str | None:
-    """`ja_JP.UTF-8` → `ja`. ロケール未設定 (C / POSIX) は不明として扱う."""
+    """`ja_JP.UTF-8` → `ja`. ロケール未設定 (C / POSIX) は不明として扱う.
+
+    中国語は地域から文字体系を決め (`zh_TW` → `zh-Hant`)、`@latin` / `@cyrillic` は
+    `-Latn` / `-Cyrl` として残す (#305)。
+    """
     if not value:
         return None
-    head = value.split(".")[0].split("@")[0].strip()
+    body, _, modifier = value.partition("@")
+    head = body.split(".")[0].strip()
     if head.lower() in NEUTRAL_LOCALES:
         return None
-    return head.replace("_", "-").split("-")[0].lower() or None
+    parts = head.replace("_", "-").split("-")
+    language = parts[0].lower()
+    if not language:
+        return None
+    if language == "zh":
+        region = parts[1].lower() if len(parts) > 1 else ""
+        return "zh-Hant" if region in _TRADITIONAL_CHINESE_REGIONS else "zh-Hans"
+    script = _SCRIPT_BY_MODIFIER.get(modifier.strip().lower())
+    return f"{language}-{script}" if script else language
 
 
 def language_name(tag: str) -> str:
diff --git a/tests/unit/test_language.py b/tests/unit/test_language.py
index 0ea204a..b283c1a 100644
--- a/tests/unit/test_language.py
+++ b/tests/unit/test_language.py
@@ -21,7 +21,7 @@ def test_explicit_setting_ignores_the_environment():
         ("ja_JP.UTF-8", "ja"),
         ("ja", "ja"),
         ("ko_KR.UTF-8", "ko"),
-        ("zh_CN.UTF-8", "zh"),
+        ("zh_CN.UTF-8", "zh-Hans"),
         ("en_US.UTF-8", "en"),
         ("pt_BR@euro", "pt"),
     ],
diff --git a/tests/unit/test_language_auto_keeps_script.py b/tests/unit/test_language_auto_keeps_script.py
new file mode 100644
index 0000000..39e650d
--- /dev/null
+++ b/tests/unit/test_language_auto_keeps_script.py
@@ -0,0 +1,33 @@
+"""auto の言語推定: 中国語の文字体系と @latin / @cyrillic を落とさないこと (#305)."""
+
+from __future__ import annotations
+
+import pytest
+
+from security_checker.language import language_name, resolve_language
+
+
+@pytest.mark.parametrize(
+    ("locale", "tag"),
+    [
+        ("zh_TW.UTF-8", "zh-Hant"),
+        ("zh_HK", "zh-Hant"),
+        ("zh_MO.UTF-8", "zh-Hant"),
+        ("zh_CN.UTF-8", "zh-Hans"),
+        ("zh_SG", "zh-Hans"),
+        ("zh", "zh-Hans"),
+        ("sr_RS@latin", "sr-Latn"),
+        ("sr_RS.UTF-8@latin", "sr-Latn"),
+        ("uz_UZ@cyrillic", "uz-Cyrl"),
+        ("ja_JP.UTF-8", "ja"),
+        ("de_DE@euro", "de"),
+    ],
+)
+def test_auto_resolves_the_locale_to_a_tag_with_its_script(locale: str, tag: str) -> None:
+    assert resolve_language("auto", {"LANG": locale}) == tag
+
+
+def test_the_two_chinese_scripts_have_different_names() -> None:
+    assert language_name("zh-Hant") != language_name("zh-Hans")
+    assert language_name("zh-Hant") != "zh-Hant"
+    assert language_name("zh-Hans") != "zh-Hans"
`````

[Back to the shelf](README.md)
