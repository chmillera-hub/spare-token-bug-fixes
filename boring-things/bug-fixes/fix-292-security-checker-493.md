# Fix 292: security-checker: no test covers the file limit or the skipped folders or the auth marker of the repository facts

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(context): facts.py の collect_repo_facts で未テストの分岐をテストする（5 行）
- Bug report: number 493 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/493))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/292-security-checker-493.patch](fixes/292-security-checker-493.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/292-security-checker-493.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-292-security-checker-493.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-292-security-checker-493.html

## The bug

collect_repo_facts in src/security_checker/context/facts.py stops after MAX_FILES files and skips folders such as node_modules and sets has_auth_layer when a path contains a marker such as login. No test ran those lines.

## The fix

Tests only. A new file tests/unit/test_repo_facts_limits_and_skips.py sets MAX_FILES to 0 and expects no language and puts a JavaScript file under node_modules and expects only Python and expects has_auth_layer to be true for login_view.py and None with no marker.

## Files changed

- tests/unit/test_repo_facts_limits_and_skips.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 292-security-checker-493.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 493.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The bug report also names two lines that handle a manifest file that cannot be read. The new tests do not cover those two lines. The tests assume that the temporary folder path made by pytest holds no folder named build or dist or vendor and no auth marker word. The chatbot did not run the tests or a coverage tool.

## Search words

security-checker context facts collect_repo_facts MAX_FILES SKIP_DIRS node_modules AUTH_MARKERS has_auth_layer untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_repo_facts_limits_and_skips.py b/tests/unit/test_repo_facts_limits_and_skips.py
new file mode 100644
index 0000000..21f72f6
--- /dev/null
+++ b/tests/unit/test_repo_facts_limits_and_skips.py
@@ -0,0 +1,38 @@
+"""collect_repo_facts: 走査の上限・読み飛ばすディレクトリ・認証らしいパスの検出."""
+
+from __future__ import annotations
+
+from pathlib import Path
+
+import pytest
+
+from security_checker.context import facts
+
+
+def test_scan_stops_at_the_file_limit(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
+    (tmp_path / "app.py").write_text("print(1)\n", encoding="utf-8")
+    monkeypatch.setattr(facts, "MAX_FILES", 0)
+
+    assert facts.collect_repo_facts(tmp_path).languages == []
+
+
+def test_files_under_a_skipped_directory_are_not_counted(tmp_path: Path) -> None:
+    hidden = tmp_path / "node_modules" / "pkg"
+    hidden.mkdir(parents=True)
+    (hidden / "index.js").write_text("module.exports = 1\n", encoding="utf-8")
+    (tmp_path / "app.py").write_text("print(1)\n", encoding="utf-8")
+
+    assert facts.collect_repo_facts(tmp_path).languages == ["Python"]
+
+
+def test_a_path_with_an_auth_marker_sets_has_auth_layer(tmp_path: Path) -> None:
+    (tmp_path / "login_view.py").write_text("print(1)\n", encoding="utf-8")
+
+    assert facts.collect_repo_facts(tmp_path).has_auth_layer is True
+
+
+def test_no_auth_marker_leaves_has_auth_layer_unknown(tmp_path: Path) -> None:
+    """対になるケース. 見つからないときは False ではなく None (不明)."""
+    (tmp_path / "app.py").write_text("print(1)\n", encoding="utf-8")
+
+    assert facts.collect_repo_facts(tmp_path).has_auth_layer is None
`````

[Back to the shelf](README.md)
