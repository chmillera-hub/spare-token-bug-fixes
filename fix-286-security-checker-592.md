# Fix 286: security-checker: no test covers the entries that the trivy parser skips

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(scanners): trivy.py の parse_trivy で未テストの分岐をテストする（9 行）
- Bug report: number 592 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/592))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/286-security-checker-592.patch](fixes/286-security-checker-592.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/286-security-checker-592.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-286-security-checker-592.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-286-security-checker-592.html

## The bug

parse_trivy in src/security_checker/scanners/trivy.py skips a Results value that is not a list and a result with no Target and an excluded path and a check that did not fail and an entry with no ID. No test ran those lines.

## The fix

Tests only. A new file tests/unit/test_trivy_parser_skipped_entries.py feeds made-up trivy output for each case and expects the exact warning text or no warning and expects only the valid misconfiguration to become a candidate.

## Files changed

- tests/unit/test_trivy_parser_skipped_entries.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 286-security-checker-592.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 592.

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

security-checker trivy parse_trivy Results Target Misconfigurations Vulnerabilities exclude Status FAIL ID warning untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_trivy_parser_skipped_entries.py b/tests/unit/test_trivy_parser_skipped_entries.py
new file mode 100644
index 0000000..a43e6c1
--- /dev/null
+++ b/tests/unit/test_trivy_parser_skipped_entries.py
@@ -0,0 +1,77 @@
+"""parse_trivy: 形の崩れた結果・除外パス・FAIL 以外・ID の無い項目の扱い."""
+
+from __future__ import annotations
+
+from pathlib import Path
+from typing import Any
+
+from security_checker.scanners.trivy import parse_trivy
+
+
+def _misconfig(**overrides: Any) -> dict[str, Any]:
+    item: dict[str, Any] = {"Status": "FAIL", "ID": "DS002", "Title": "root user"}
+    item.update(overrides)
+    return item
+
+
+def test_results_that_are_not_a_list_give_one_warning(tmp_path: Path) -> None:
+    candidates, warnings = parse_trivy({"Results": {"Target": "Dockerfile"}}, tmp_path)
+
+    assert candidates == []
+    assert warnings == ["trivy の出力の Results が配列ではありません"]
+
+
+def test_result_without_a_target_is_skipped_with_a_warning(tmp_path: Path) -> None:
+    payload = {"Results": [{"Misconfigurations": [_misconfig()]}]}
+
+    candidates, warnings = parse_trivy(payload, tmp_path)
+
+    assert candidates == []
+    assert warnings == ["trivy の結果に Target がありません"]
+
+
+def test_excluded_target_is_skipped_without_a_warning(tmp_path: Path) -> None:
+    payload = {"Results": [{"Target": "vendor/Dockerfile", "Misconfigurations": [_misconfig()]}]}
+
+    candidates, warnings = parse_trivy(payload, tmp_path, exclude=["vendor"])
+
+    assert candidates == []
+    assert warnings == []
+
+
+def test_passed_checks_and_checks_without_an_id_are_skipped(tmp_path: Path) -> None:
+    payload = {
+        "Results": [
+            {
+                "Target": "Dockerfile",
+                "Misconfigurations": [
+                    _misconfig(Status="PASS"),
+                    {"Status": "FAIL", "Title": "no id"},
+                    _misconfig(),
+                ],
+            }
+        ]
+    }
+
+    candidates, warnings = parse_trivy(payload, tmp_path)
+
+    assert [candidate.rule_id for candidate in candidates] == ["DS002"]
+    assert warnings == ["Dockerfile: ID の無い誤設定を読み飛ばしました"]
+
+
+def test_vulnerability_without_id_or_package_name_is_skipped(tmp_path: Path) -> None:
+    payload = {
+        "Results": [
+            {
+                "Target": "requirements.txt",
+                "Type": "pip",
+                "Vulnerabilities": [{"PkgName": "flask"}, {"VulnerabilityID": "CVE-2024-0001"}],
+            }
+        ]
+    }
+
+    candidates, warnings = parse_trivy(payload, tmp_path)
+
+    assert candidates == []
+    assert len(warnings) == 2
+    assert all(warning.startswith("requirements.txt: ") for warning in warnings)
`````

[Back to the shelf](README.md)
