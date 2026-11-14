# Fix 340: security-checker: dependency findings from osv carry no CWE although the advisory names one

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: feat(scanners): osv の advisory にある CWE (database_specific.cwe_ids) を候補の cwe に入れる
- Bug report: number 276 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/276))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/340-security-checker-276.patch](fixes/340-security-checker-276.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/340-security-checker-276.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-340-security-checker-276.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-340-security-checker-276.html

## The bug

parse_osv in src/security_checker/scanners/osv.py does not pass cwe to the candidate. Advisories that come from GitHub hold the CWE in database_specific.cwe_ids so dependency findings reach the reviewer and the PR comment with no CWE while the same finding from trivy has one.

## The fix

parse_osv now collects database_specific.cwe_ids from every advisory of a group and keeps values of the form CWE-number once each in the order found. An advisory with no value still gives an empty list. A new file tests/unit/test_osv_parser_cwe_ids.py covers both cases with made-up osv-scanner output.

## Files changed

- src/security_checker/scanners/osv.py
- tests/unit/test_osv_parser_cwe_ids.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 340-security-checker-276.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 276.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The bug report asks for a test built from real osv-scanner output as a fixture. The chatbot has no such output and used a small made-up payload with the advisory ID from the report.

## Search words

security-checker osv parse_osv cwe database_specific cwe_ids CWE dependency candidate GHSA reviewer hint

## The full patch

`````diff
diff --git a/src/security_checker/scanners/osv.py b/src/security_checker/scanners/osv.py
index e1f2901..f904f6b 100644
--- a/src/security_checker/scanners/osv.py
+++ b/src/security_checker/scanners/osv.py
@@ -74,6 +74,19 @@ def _group_severity(group: dict[str, Any], vulns: list[dict[str, Any]]) -> Sever
     return max(known, key=lambda s: s.order) if known else None
 
 
+_CWE_RE = re.compile(r"^CWE-\d+$")
+
+
+def _cwe_ids(vulns: list[dict[str, Any]]) -> list[str]:
+    """advisory の `database_specific.cwe_ids` から CWE を重複なく集める (#276)."""
+    found: list[str] = []
+    for vuln in vulns:
+        for item in as_dict(vuln.get("database_specific")).get("cwe_ids") or []:
+            if isinstance(item, str) and _CWE_RE.match(item) and item not in found:
+                found.append(item)
+    return found
+
+
 def _fixed_version(vulns: list[dict[str, Any]], name: str) -> str | None:
     fixed: list[str] = []
     for vuln in vulns:
@@ -160,6 +173,7 @@ def parse_osv(
                         package=ref,
                         # 不明を info にするとゲートから消える。依存の脆弱性は控えめに中とする
                         severity_reported=severity or Severity.MEDIUM,
+                        cwe=_cwe_ids(vulns),
                         cve=sorted({a for a in [*aliases, *group_ids] if _CVE_RE.match(a)}),
                         references=list(dict.fromkeys(references))[:MAX_REFERENCES],
                         fix_available=_fixed_version(vulns, name),
diff --git a/tests/unit/test_osv_parser_cwe_ids.py b/tests/unit/test_osv_parser_cwe_ids.py
new file mode 100644
index 0000000..1ae400c
--- /dev/null
+++ b/tests/unit/test_osv_parser_cwe_ids.py
@@ -0,0 +1,49 @@
+"""parse_osv: advisory の database_specific.cwe_ids を候補の cwe に入れること (#276)."""
+
+from __future__ import annotations
+
+from pathlib import Path
+from typing import Any
+
+from security_checker.scanners.osv import parse_osv
+
+
+def _payload(vulnerabilities: list[dict[str, Any]]) -> dict[str, Any]:
+    return {
+        "results": [
+            {
+                "source": {"path": "requirements.txt"},
+                "packages": [
+                    {
+                        "package": {"name": "django", "version": "3.2.0", "ecosystem": "PyPI"},
+                        "vulnerabilities": vulnerabilities,
+                        "groups": [{"ids": [item["id"] for item in vulnerabilities]}],
+                    }
+                ],
+            }
+        ]
+    }
+
+
+def test_cwe_ids_of_every_advisory_in_the_group_are_collected_once(tmp_path: Path) -> None:
+    payload = _payload(
+        [
+            {
+                "id": "GHSA-2gwj-7jmv-h26r",
+                "summary": "SQL injection",
+                "database_specific": {"cwe_ids": ["CWE-89", "CWE-89", "not-a-cwe", 5]},
+            },
+            {"id": "PYSEC-2022-1", "database_specific": {"cwe_ids": ["CWE-20"]}},
+        ]
+    )
+
+    candidates, _ = parse_osv(payload, tmp_path)
+
+    assert [candidate.cwe for candidate in candidates] == [["CWE-89", "CWE-20"]]
+
+
+def test_advisory_without_cwe_ids_keeps_an_empty_list(tmp_path: Path) -> None:
+    """対になるケース."""
+    candidates, _ = parse_osv(_payload([{"id": "GHSA-aaaa-bbbb-cccc"}]), tmp_path)
+
+    assert [candidate.cwe for candidate in candidates] == [[]]
`````

[Back to the shelf](README.md)
