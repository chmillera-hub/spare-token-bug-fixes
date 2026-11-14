# Fix 318: security-checker: semgrep severities CRITICAL and HIGH and MEDIUM are all treated as low

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(scanners): semgrep の重大度 CRITICAL / HIGH / MEDIUM を知らず、すべて low として扱う
- Bug report: number 271 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/271))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/318-security-checker-271.patch](fixes/318-security-checker-271.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/318-security-checker-271.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-318-security-checker-271.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-318-security-checker-271.html

## The bug

SEVERITY_MAP in src/security_checker/scanners/semgrep.py knows only ERROR and WARNING and INFO. Newer semgrep rules report CRITICAL or HIGH or MEDIUM or LOW and every one of those falls back to low. A critical finding can pass a gate set to high.

## The fix

The table now maps CRITICAL and HIGH and MEDIUM and LOW to the same levels and keeps ERROR and WARNING and INFO. A value outside the table (a missing value included) now adds a parse warning and counts as medium like the osv and trivy parsers do. The line about semgrep in docs/DESIGN.md names the new values. A new file tests/unit/test_semgrep_severity_levels.py covers all seven values and three unknown ones.

## Files changed

- docs/DESIGN.md
- src/security_checker/scanners/semgrep.py
- tests/unit/test_semgrep_severity_levels.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 318-security-checker-271.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 271.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The bug report asks for the new cases inside tests/unit/test_semgrep_parser.py. The chatbot put them in a new file to keep the patch free of collisions. A result with no severity at all now gives a warning and medium where the old code gave low with no warning.

## Search words

security-checker semgrep SEVERITY_MAP CRITICAL HIGH MEDIUM LOW severity low parse_semgrep unknown severity medium warning

## The full patch

`````diff
diff --git a/docs/DESIGN.md b/docs/DESIGN.md
index 869c899..841445d 100644
--- a/docs/DESIGN.md
+++ b/docs/DESIGN.md
@@ -551,7 +551,7 @@ v1 の最大のバグは **「ツールが失敗しても findings 0 件とし
 
 | Scanner | 対象 | 主な正規化 |
 |---|---|---|
-| `semgrep` | SAST | `results[].extra.severity` (ERROR/WARNING/INFO) → Severity、`check_id` → rule_id、`extra.metadata.cwe` を Candidate.cwe に |
+| `semgrep` | SAST | `results[].extra.severity` (CRITICAL/HIGH/MEDIUM/LOW、旧形式の ERROR/WARNING/INFO) → Severity、`check_id` → rule_id、`extra.metadata.cwe` を Candidate.cwe に |
 | `gitleaks` | Secret | `--report-format json`。**検出値(`Secret`/`Match`)は Candidate に載せない**(§19) |
 | `osv-scanner` | 依存 CVE | `results[].packages[].vulnerabilities[]` を CVE 単位に展開。`database_specific.severity` と CVSS から Severity 決定 |
 | `trivy` | IaC / 設定 | `config` スキャンモード。`Misconfigurations[]` を正規化 |
diff --git a/src/security_checker/scanners/semgrep.py b/src/security_checker/scanners/semgrep.py
index ac8f80c..d08cdc6 100644
--- a/src/security_checker/scanners/semgrep.py
+++ b/src/security_checker/scanners/semgrep.py
@@ -29,6 +29,10 @@ from security_checker.scanners.filters import is_excluded
 CWE_RE = re.compile(r"CWE-\d+")
 
 SEVERITY_MAP = {
+    "CRITICAL": Severity.CRITICAL,
+    "HIGH": Severity.HIGH,
+    "MEDIUM": Severity.MEDIUM,
+    "LOW": Severity.LOW,
     "ERROR": Severity.HIGH,
     "WARNING": Severity.MEDIUM,
     "INFO": Severity.LOW,
@@ -108,10 +112,14 @@ def parse_semgrep(
         message = extra.get("message")
         message_text = message.strip() if isinstance(message, str) else check_id
         severity_raw = extra.get("severity")
-        severity = SEVERITY_MAP.get(
-            severity_raw.upper() if isinstance(severity_raw, str) else "",
-            Severity.LOW,
-        )
+        severity = SEVERITY_MAP.get(severity_raw.upper() if isinstance(severity_raw, str) else "")
+        if severity is None:
+            # 表に無い重大度を黙って low にしない (#271). osv・trivy と同じく不明は medium
+            warnings.append(
+                f"semgrep: {check_id} ({path}) の重大度 {severity_raw!r} は未知のため、"
+                "medium として扱います"
+            )
+            severity = Severity.MEDIUM
         confidence_raw = metadata.get("confidence")
         confidence = (
             CONFIDENCE_MAP.get(confidence_raw.upper()) if isinstance(confidence_raw, str) else None
diff --git a/tests/unit/test_semgrep_severity_levels.py b/tests/unit/test_semgrep_severity_levels.py
new file mode 100644
index 0000000..9d6cf81
--- /dev/null
+++ b/tests/unit/test_semgrep_severity_levels.py
@@ -0,0 +1,56 @@
+"""parse_semgrep: semgrep の重大度 7 種類の対応と、表に無い値の扱い (#271)."""
+
+from __future__ import annotations
+
+from pathlib import Path
+from typing import Any
+
+import pytest
+
+from security_checker.models.enums import Severity
+from security_checker.scanners.semgrep import parse_semgrep
+
+ROOT = Path("/repo")
+
+
+def _payload(severity: object) -> dict[str, Any]:
+    return {
+        "results": [
+            {
+                "check_id": "rules.example",
+                "path": "app.py",
+                "start": {"line": 3},
+                "end": {"line": 3},
+                "extra": {"severity": severity, "message": "m", "lines": "x = 1"},
+            }
+        ]
+    }
+
+
+@pytest.mark.parametrize(
+    ("raw", "expected"),
+    [
+        ("CRITICAL", Severity.CRITICAL),
+        ("HIGH", Severity.HIGH),
+        ("MEDIUM", Severity.MEDIUM),
+        ("LOW", Severity.LOW),
+        ("ERROR", Severity.HIGH),
+        ("WARNING", Severity.MEDIUM),
+        ("INFO", Severity.LOW),
+        ("critical", Severity.CRITICAL),
+    ],
+)
+def test_known_severity_is_mapped_without_a_warning(raw: str, expected: Severity) -> None:
+    candidates, warnings = parse_semgrep(_payload(raw), ROOT)
+
+    assert [candidate.severity_reported for candidate in candidates] == [expected]
+    assert warnings == []
+
+
+@pytest.mark.parametrize("raw", ["EXPERIMENT", "INVENTORY", None])
+def test_unknown_severity_becomes_medium_with_a_warning(raw: object) -> None:
+    candidates, warnings = parse_semgrep(_payload(raw), ROOT)
+
+    assert [candidate.severity_reported for candidate in candidates] == [Severity.MEDIUM]
+    assert len(warnings) == 1
+    assert "rules.example" in warnings[0]
`````

[Back to the shelf](README.md)
