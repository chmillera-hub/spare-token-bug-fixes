# Fix 303: security-checker: report.md puts reviewer names and rule IDs between backticks without code_span

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(report): report.md のバッククォート囲みで code_span を通していない箇所がある（Reviewer 名・scanner・rule_id）
- Bug report: number 266 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/266))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/303-security-checker-266.patch](fixes/303-security-checker-266.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/303-security-checker-266.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-303-security-checker-266.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-303-security-checker-266.html

## The bug

_finding_block in src/security_checker/report/markdown.py wraps the reviewer name and the scanner and the rule ID in backticks directly. A backtick or a line break inside one of those values breaks the table and the layout of report.md.

## The fix

The four places now call md.code_span which replaces backticks and joins lines. A new file tests/unit/test_markdown_finding_block_backticks.py builds a rule ID and two reviewer names with a backtick and expects no raw backtick from those values in the block.

## Files changed

- src/security_checker/report/markdown.py
- tests/unit/test_markdown_finding_block_backticks.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 303-security-checker-266.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 266.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. This patch applies together with the patch of fix 309 on this shelf (the same function).

## Search words

security-checker report markdown _finding_block code_span backtick reviewer rule_id scanner table broken

## The full patch

`````diff
diff --git a/src/security_checker/report/markdown.py b/src/security_checker/report/markdown.py
index d78c871..8c293ce 100644
--- a/src/security_checker/report/markdown.py
+++ b/src/security_checker/report/markdown.py
@@ -205,7 +205,8 @@ def _finding_block(finding: Finding) -> list[str]:
     if finding.cwe:
         meta.insert(0, "**CWE** " + ", ".join(finding.cwe[:3]))
     lines += [" ・ ".join(meta), ""]
-    lines += [f"検出元: `{candidate.scanner}` / `{candidate.rule_id}`", ""]
+    source = f"{md.code_span(candidate.scanner)} / {md.code_span(candidate.rule_id)}"
+    lines += [f"検出元: {source}", ""]
 
     summary = finding.summary or candidate.message
     if summary:
@@ -216,7 +217,8 @@ def _finding_block(finding: Finding) -> list[str]:
         lines += ["| Reviewer | 判定 | 確信度 |", "|---|---|---|"]
         for verdict in ok_verdicts:
             judgement = f"{verdict.severity.value}" if verdict.vulnerable else "脆弱ではない"
-            lines.append(f"| `{verdict.reviewer}` | {judgement} | {verdict.confidence:.0%} |")
+            reviewer = md.code_span(verdict.reviewer)
+            lines.append(f"| {reviewer} | {judgement} | {verdict.confidence:.0%} |")
         lines.append("")
 
     for verdict in ok_verdicts:
@@ -238,12 +240,14 @@ def _finding_block(finding: Finding) -> list[str]:
     if details:
         lines += ["<details><summary>各 Reviewer の判断理由</summary>", ""]
         for verdict in details:
-            lines += [f"**`{verdict.reviewer}`** — {md.text(verdict.reasoning.strip())}", ""]
+            reviewer = md.code_span(verdict.reviewer)
+            lines += [f"**{reviewer}** — {md.text(verdict.reasoning.strip())}", ""]
         lines += ["</details>", ""]
 
     failed = [v for v in finding.verdicts if v.status.value != "ok"]
     for verdict in failed:
-        lines += [f"> ⚠️ `{verdict.reviewer}` は判定できませんでした: {verdict.status.value}", ""]
+        reviewer = md.code_span(verdict.reviewer)
+        lines += [f"> ⚠️ {reviewer} は判定できませんでした: {verdict.status.value}", ""]
     return lines
 
 
diff --git a/tests/unit/test_markdown_finding_block_backticks.py b/tests/unit/test_markdown_finding_block_backticks.py
new file mode 100644
index 0000000..8b38769
--- /dev/null
+++ b/tests/unit/test_markdown_finding_block_backticks.py
@@ -0,0 +1,29 @@
+"""report.md の Finding ブロック: バッククォートを含む名前で崩れないこと (#266)."""
+
+from __future__ import annotations
+
+from security_checker.models.enums import FindingStatus
+from security_checker.models.verdict import VerdictStatus
+from security_checker.report.markdown import _finding_block
+from tests.factories import make_candidate, make_finding, make_verdict
+
+
+def test_backticks_in_rule_id_and_reviewer_name_cannot_leave_the_code_span() -> None:
+    candidate = make_candidate(rule_id="rules.x`y")
+    finding = make_finding(
+        candidate,
+        FindingStatus.CONFIRMED,
+        verdicts=[
+            make_verdict("re`viewer"),
+            make_verdict("bro`ken", status=VerdictStatus.PROVIDER_ERROR, vulnerable=False),
+        ],
+    )
+
+    text = "\n".join(_finding_block(finding))
+
+    assert "`rules.x'y`" in text
+    assert "rules.x`y" not in text
+    assert "`re'viewer`" in text
+    assert "re`viewer" not in text
+    assert "`bro'ken`" in text
+    assert "bro`ken" not in text
`````

[Back to the shelf](README.md)
