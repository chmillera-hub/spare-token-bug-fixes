# Fix 346: coding-agent-skills: the audit rotation record accepts dates in non-ASCII digits and dates that do not exist

Status: UNSENT and UNTESTED. Free to take.

- Project: EJRyan89/coding-agent-skills
- Bug report title: audit_repository DATE_FORMAT accepts non-ASCII digits and impossible dates
- Bug report: number 2544 ([open the bug report](https://github.com/EJRyan89/coding-agent-skills/issues/2544))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/346-coding-agent-skills-2544.patch](fixes/346-coding-agent-skills-2544.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/346-coding-agent-skills-2544.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-346-coding-agent-skills-2544.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-346-coding-agent-skills-2544.html

## The bug

record_entry in .claude/skills/audit-repository/scripts/audit_repository.py checks the date only with the pattern of four digits and two digits and two digits. The pattern also matches Arabic-Indic digits and an impossible date such as 2026-13-45 so both pass.

## The fix

A new helper is_calendar_date requires ASCII text that matches the pattern and that date.fromisoformat accepts. record_entry uses the helper and keeps its error message. Two new cases in the existing parametrized test of test_audit_repository.py cover an impossible date and a date written in Arabic-Indic digits.

## Files changed

- .claude/skills/audit-repository/scripts/audit_repository.py
- .claude/skills/audit-repository/scripts/test_audit_repository.py

## How to use the fix

1. Get a copy of the project EJRyan89/coding-agent-skills.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 346-coding-agent-skills-2544.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 2544.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot ran a separate scratch copy of the helper against six made-up values and all six gave the expected answer. The chatbot did not run the project's code or tests. The second new test case writes the digits as JSON escapes so the test file stays ASCII.

## Search words

coding-agent-skills audit_repository DATE_FORMAT rotation record date non-ASCII digits impossible date fromisoformat

## The full patch

`````diff
diff --git a/.claude/skills/audit-repository/scripts/audit_repository.py b/.claude/skills/audit-repository/scripts/audit_repository.py
index bd40a88..51ba86b 100644
--- a/.claude/skills/audit-repository/scripts/audit_repository.py
+++ b/.claude/skills/audit-repository/scripts/audit_repository.py
@@ -627,11 +627,22 @@ def read_record(path: Path) -> list[Entry]:
     return entries
 
 
+def is_calendar_date(text: str) -> bool:
+    """Whether text is YYYY-MM-DD in ASCII digits and names a date that exists."""
+    if not text.isascii() or not DATE_FORMAT.fullmatch(text):
+        return False
+    try:
+        date.fromisoformat(text)
+    except ValueError:
+        return False
+    return True
+
+
 def record_entry(name: str, number: int, item: object) -> Entry:
     if not isinstance(item, dict) or set(item) != {"date", "tag", "area"}:
         raise AuditError(f"{name} audit {number} must have exactly a date, a tag, and an area")
     when, tag, area = item["date"], item["tag"], item["area"]
-    if not isinstance(when, str) or not DATE_FORMAT.fullmatch(when):
+    if not isinstance(when, str) or not is_calendar_date(when):
         raise AuditError(f"{name} audit {number} has a date that is not YYYY-MM-DD")
     if not isinstance(tag, str) or not is_release_tag(tag):
         raise AuditError(f"{name} audit {number} has a tag that is not a release tag vX.Y.Z")
diff --git a/.claude/skills/audit-repository/scripts/test_audit_repository.py b/.claude/skills/audit-repository/scripts/test_audit_repository.py
index d421099..094dd7c 100644
--- a/.claude/skills/audit-repository/scripts/test_audit_repository.py
+++ b/.claude/skills/audit-repository/scripts/test_audit_repository.py
@@ -1320,6 +1320,17 @@ def test_a_code_literal_of_a_printable_path_is_its_json_string_in_backticks() ->
         pytest.param(
             '{"audits": [{"date": "1 Jan", "tag": "v1", "area": "deployer"}]}', "not YYYY-MM-DD", id="date-not-iso"
         ),
+        pytest.param(
+            '{"audits": [{"date": "2026-13-45", "tag": "v1.0.0", "area": "deployer"}]}',
+            "not YYYY-MM-DD",
+            id="date-that-does-not-exist",
+        ),
+        pytest.param(
+            '{"audits": [{"date": "\\u0662\\u0660\\u0662\\u0666-\\u0661\\u0661-\\u0660\\u0669", '
+            '"tag": "v1.0.0", "area": "deployer"}]}',
+            "not YYYY-MM-DD",
+            id="date-in-non-ascii-digits",
+        ),
         pytest.param(
             '{"audits": [{"date": "2026-01-01", "tag": " ", "area": "deployer"}]}',
             "has a tag that is not a release tag vX.Y.Z",
`````

[Back to the shelf](README.md)
