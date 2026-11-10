# Fix 289: security-checker: no test covers the entries that the osv parser skips

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(scanners): osv.py の parse_osv で未テストの分岐をテストする（5 行）
- Bug report: number 586 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/586))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/289-security-checker-586.patch](fixes/289-security-checker-586.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/289-security-checker-586.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-289-security-checker-586.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-289-security-checker-586.html

## The bug

parse_osv in src/security_checker/scanners/osv.py skips a result with no source path and a package with no name or ecosystem and a group with no usable ID. No test ran those lines.

## The fix

Tests only. A new file tests/unit/test_osv_parser_skipped_entries.py feeds made-up osv-scanner output for each case and expects the exact warning text for the first two cases and no candidate and no warning for a group with no ID.

## Files changed

- tests/unit/test_osv_parser_skipped_entries.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 289-security-checker-586.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 586.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The bug report lists the untested lines from a coverage run on an older commit. The chatbot did not run the tests or a coverage tool so nobody has confirmed that the new tests reach the named lines.

## Search words

security-checker osv parse_osv source path package name ecosystem groups ids warning skipped untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_osv_parser_skipped_entries.py b/tests/unit/test_osv_parser_skipped_entries.py
new file mode 100644
index 0000000..bb1984b
--- /dev/null
+++ b/tests/unit/test_osv_parser_skipped_entries.py
@@ -0,0 +1,52 @@
+"""parse_osv: source.path・パッケージ名・ID の無い項目を読み飛ばすこと."""
+
+from __future__ import annotations
+
+from pathlib import Path
+from typing import Any
+
+from security_checker.scanners.osv import parse_osv
+
+
+def _result(packages: list[dict[str, Any]], path: object = "requirements.txt") -> dict[str, Any]:
+    return {"source": {"path": path}, "packages": packages}
+
+
+def test_result_without_a_source_path_is_skipped_with_a_warning(tmp_path: Path) -> None:
+    payload = {"results": [{"source": {}, "packages": []}, _result([], path=None)]}
+
+    candidates, warnings = parse_osv(payload, tmp_path)
+
+    assert candidates == []
+    assert warnings == ["osv-scanner の結果に source.path がありません"] * 2
+
+
+def test_package_without_a_name_or_ecosystem_is_skipped_with_a_warning(tmp_path: Path) -> None:
+    payload = {
+        "results": [
+            _result(
+                [
+                    {"package": {"ecosystem": "PyPI"}, "vulnerabilities": [{"id": "GHSA-1"}]},
+                    {"package": {"name": "flask"}, "vulnerabilities": [{"id": "GHSA-2"}]},
+                ]
+            )
+        ]
+    }
+
+    candidates, warnings = parse_osv(payload, tmp_path)
+
+    assert candidates == []
+    assert warnings == ["requirements.txt: パッケージ名の無い結果を読み飛ばしました"] * 2
+
+
+def test_group_without_any_id_is_skipped_silently(tmp_path: Path) -> None:
+    package = {
+        "package": {"name": "flask", "ecosystem": "PyPI", "version": "1.0"},
+        "vulnerabilities": [{"id": "GHSA-1"}],
+        "groups": [{"ids": []}, {"ids": [None, 3]}, {}],
+    }
+
+    candidates, warnings = parse_osv({"results": [_result([package])]}, tmp_path)
+
+    assert candidates == []
+    assert warnings == []
`````

[Back to the shelf](README.md)
