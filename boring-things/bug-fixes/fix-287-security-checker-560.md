# Fix 287: security-checker: no test covers a report section with more findings than the section limit

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(report): markdown.py の _findings で未テストの分岐をテストする（1 行）
- Bug report: number 560 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/560))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/287-security-checker-560.patch](fixes/287-security-checker-560.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/287-security-checker-560.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-287-security-checker-560.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-287-security-checker-560.html

## The bug

_findings in src/security_checker/report/markdown.py shows at most 20 findings per section and then adds a line that points to report.json for the rest. No test ran that line.

## The fix

Tests only. A new file tests/unit/test_markdown_findings_section_overflow.py builds 21 confirmed findings and expects the line for 1 more finding and builds exactly 20 and expects no such line.

## Files changed

- tests/unit/test_markdown_findings_section_overflow.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 287-security-checker-560.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 560.

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

security-checker markdown _findings MAX_FINDINGS_PER_SECTION overflow report.json section limit untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_markdown_findings_section_overflow.py b/tests/unit/test_markdown_findings_section_overflow.py
new file mode 100644
index 0000000..0957b0d
--- /dev/null
+++ b/tests/unit/test_markdown_findings_section_overflow.py
@@ -0,0 +1,27 @@
+"""report.md: 1 つのセクションの Finding が上限を超えたら、残りの件数を案内すること."""
+
+from __future__ import annotations
+
+from security_checker.models.enums import FindingStatus
+from security_checker.models.report import Report
+from security_checker.report.markdown import MAX_FINDINGS_PER_SECTION, _findings
+from tests.factories import make_candidate, make_finding, make_report
+
+
+def _report(count: int) -> Report:
+    candidates = [make_candidate(f"c{index}", line=index + 1) for index in range(count)]
+    findings = [make_finding(candidate, FindingStatus.CONFIRMED) for candidate in candidates]
+    return make_report(candidates, findings)
+
+
+def test_one_finding_over_the_limit_points_to_report_json() -> None:
+    lines = _findings(_report(MAX_FINDINGS_PER_SECTION + 1))
+
+    assert "_ほか 1 件は `report.json` を参照_" in lines
+
+
+def test_exactly_the_limit_shows_no_overflow_line() -> None:
+    """対になるケース."""
+    lines = _findings(_report(MAX_FINDINGS_PER_SECTION))
+
+    assert not any("report.json` を参照" in line for line in lines)
`````

[Back to the shelf](README.md)
