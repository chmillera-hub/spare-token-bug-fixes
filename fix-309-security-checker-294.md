# Fix 309: security-checker: the fix example in report.md is a code block with no language

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: feat(report): report.md の修正例のコードブロックに言語を付ける
- Bug report: number 294 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/294))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/309-security-checker-294.patch](fixes/309-security-checker-294.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/309-security-checker-294.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-309-security-checker-294.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-309-security-checker-294.html

## The bug

_finding_block in src/security_checker/report/markdown.py calls md.code_block for the fix example with no language. GitHub shows the example with no syntax colours.

## The fix

markdown.py now holds a small table from file extension to language name (letters and digits only) and passes the language of the candidate path to md.code_block. A new file tests/unit/test_markdown_remediation_code_block_language.py expects a python fence for a .py candidate and a plain fence for an unknown extension.

## Files changed

- src/security_checker/report/markdown.py
- tests/unit/test_markdown_remediation_code_block_language.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 309-security-checker-294.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 294.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The bug report asks for a small table and names no list of extensions. The chatbot chose 21 common extensions.

## Search words

security-checker report markdown code_block language fence python remediation example syntax highlight extension

## The full patch

`````diff
diff --git a/src/security_checker/report/markdown.py b/src/security_checker/report/markdown.py
index d78c871..e000d9f 100644
--- a/src/security_checker/report/markdown.py
+++ b/src/security_checker/report/markdown.py
@@ -195,6 +195,38 @@ def _findings(report: Report) -> list[str]:
     return lines
 
 
+#: 修正例のコードブロックに付ける言語名. 拡張子 (小文字・ドット無し) から決める (#294)
+_FENCE_LANGUAGES = {
+    "py": "python",
+    "js": "javascript",
+    "mjs": "javascript",
+    "cjs": "javascript",
+    "jsx": "jsx",
+    "ts": "typescript",
+    "tsx": "tsx",
+    "go": "go",
+    "rb": "ruby",
+    "java": "java",
+    "kt": "kotlin",
+    "php": "php",
+    "rs": "rust",
+    "c": "c",
+    "cs": "csharp",
+    "sh": "bash",
+    "yml": "yaml",
+    "yaml": "yaml",
+    "json": "json",
+    "tf": "hcl",
+    "sql": "sql",
+}
+
+
+def _fence_language(path: str) -> str:
+    """パスの拡張子に対応する言語名. 分からなければ空文字 (言語無しのフェンス)."""
+    _, dot, suffix = path.rsplit("/", 1)[-1].rpartition(".")
+    return _FENCE_LANGUAGES.get(suffix.lower(), "") if dot else ""
+
+
 def _finding_block(finding: Finding) -> list[str]:
     candidate = finding.candidate
     mark = SEVERITY_MARK[finding.severity]
@@ -231,7 +263,8 @@ def _finding_block(finding: Finding) -> list[str]:
         if verdict.remediation is not None and verdict.remediation.approach:
             lines += ["**対応方針**", "", md.text(verdict.remediation.approach.strip()), ""]
             if verdict.remediation.example:
-                lines += [*md.code_block(verdict.remediation.example.strip()), ""]
+                language = _fence_language(candidate.location.path if candidate.location else "")
+                lines += [*md.code_block(verdict.remediation.example.strip(), language), ""]
             break
 
     details = [v for v in ok_verdicts if v.reasoning]
diff --git a/tests/unit/test_markdown_remediation_code_block_language.py b/tests/unit/test_markdown_remediation_code_block_language.py
new file mode 100644
index 0000000..5d60526
--- /dev/null
+++ b/tests/unit/test_markdown_remediation_code_block_language.py
@@ -0,0 +1,39 @@
+"""report.md: 修正例のコードブロックに、候補のパスの拡張子から決めた言語を付けること (#294)."""
+
+from __future__ import annotations
+
+import pytest
+
+from security_checker.models.enums import FindingStatus
+from security_checker.models.verdict import Remediation
+from security_checker.report.markdown import _finding_block
+from tests.factories import make_candidate, make_finding, make_verdict
+
+
+def _block(path: str) -> list[str]:
+    remediation = Remediation(approach="引数を配列で渡す", example="subprocess.run(argv)")
+    finding = make_finding(
+        make_candidate(path=path),
+        FindingStatus.CONFIRMED,
+        verdicts=[make_verdict("r1", remediation=remediation)],
+    )
+    return _finding_block(finding)
+
+
+@pytest.mark.parametrize(
+    ("path", "fence"),
+    [("src/app.py", "```python"), ("web/App.TSX", "```tsx"), ("deploy/main.tf", "```hcl")],
+)
+def test_known_extension_sets_the_fence_language(path: str, fence: str) -> None:
+    lines = _block(path)
+
+    assert fence in lines
+    assert lines[lines.index(fence) + 1] == "subprocess.run(argv)"
+
+
+@pytest.mark.parametrize("path", ["Dockerfile", "data/notes.unknownext"])
+def test_unknown_extension_keeps_a_plain_fence(path: str) -> None:
+    """対になるケース."""
+    lines = _block(path)
+
+    assert lines[lines.index("subprocess.run(argv)") - 1] == "```"
`````

[Back to the shelf](README.md)
