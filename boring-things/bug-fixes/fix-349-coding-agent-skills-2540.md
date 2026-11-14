# Fix 349: coding-agent-skills: a local reviewer manifest that cannot be examined is printed as missing

Status: UNSENT and UNTESTED. Free to take.

- Project: EJRyan89/coding-agent-skills
- Bug report title: review_reviewer_setup: a local reviewer manifest it cannot stat is printed as missing
- Bug report: number 2540 ([open the bug report](https://github.com/EJRyan89/coding-agent-skills/issues/2540))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/349-coding-agent-skills-2540.patch](fixes/349-coding-agent-skills-2540.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/349-coding-agent-skills-2540.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-349-coding-agent-skills-2540.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-349-coding-agent-skills-2540.html

## The bug

review_reviewer_setup.py prints MANIFEST local with present or missing from Path.is_file(). is_file answers False for an error such as a permission problem so the line says missing and the next step is to create a file that already exists.

## The fix

A new helper manifest_state reads the path with stat and answers present or missing or unreadable with the reason in brackets. Only a path that is not there (or whose parent is not a folder) counts as missing. A new file test_review_reviewer_setup_manifest_state.py next to the script covers a present file and a missing file and a path whose stat raises PermissionError.

## Files changed

- skills/ejryan89-code-review-core/scripts/review_reviewer_setup.py
- skills/ejryan89-code-review-core/scripts/test_review_reviewer_setup_manifest_state.py

## How to use the fix

1. Get a copy of the project EJRyan89/coding-agent-skills.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 349-coding-agent-skills-2540.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 2540.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's code or tests. The new test file finds the folder of the shared scripts by walking up from its own folder because the chatbot did not work out how the existing tests locate that folder. The wording unreadable (reason) is the chatbot's own.

## Search words

coding-agent-skills review_reviewer_setup MANIFEST local missing is_file cannot stat unreadable permission

## The full patch

`````diff
diff --git a/skills/ejryan89-code-review-core/scripts/review_reviewer_setup.py b/skills/ejryan89-code-review-core/scripts/review_reviewer_setup.py
index 6370c5e..7d77263 100644
--- a/skills/ejryan89-code-review-core/scripts/review_reviewer_setup.py
+++ b/skills/ejryan89-code-review-core/scripts/review_reviewer_setup.py
@@ -4,6 +4,7 @@ from __future__ import annotations
 
 import functools
 import re
+import stat
 import sys
 import tempfile
 from collections.abc import Mapping, Sequence
@@ -293,6 +294,16 @@ def _reviewer_commit(checkout: Path, reviewer: dict[str, Any], ref: str | None,
         raise PipelineError(f"Cannot resolve {candidate} in {checkout}; pass --ref: {exc}") from exc
 
 
+def manifest_state(local: Path) -> str:
+    """present, missing, or unreadable with the reason: a path that cannot be examined is never read as absent."""
+    try:
+        return "present" if stat.S_ISREG(local.stat().st_mode) else "missing"
+    except (FileNotFoundError, NotADirectoryError):
+        return "missing"
+    except OSError as exc:
+        return f"unreadable ({exc.strerror or exc})"
+
+
 def inspect_reviewer(
     repository: str, *, ref: str | None = None, config_path: Path | None = None, services: Services | None = None
 ) -> list[str]:
@@ -312,7 +323,7 @@ def inspect_reviewer(
     lines.extend(f"REFERENCES {path}" for path in inspection.references)
     local = manifest_location(reviewer, config_path, repository)
     if local is not None:
-        lines.append(f"MANIFEST local {local} {'present' if local.is_file() else 'missing'}")
+        lines.append(f"MANIFEST local {local} {manifest_state(local)}")
         verdict = "manifest-configured"
     else:
         verdict = {"yes": "manifest-required", "no": "entrypoint-ok", "unknown": "undetermined"}[inspection.delegates]
diff --git a/skills/ejryan89-code-review-core/scripts/test_review_reviewer_setup_manifest_state.py b/skills/ejryan89-code-review-core/scripts/test_review_reviewer_setup_manifest_state.py
new file mode 100644
index 0000000..314121e
--- /dev/null
+++ b/skills/ejryan89-code-review-core/scripts/test_review_reviewer_setup_manifest_state.py
@@ -0,0 +1,37 @@
+"""manifest_state: a manifest that cannot be examined is unreadable, never missing."""
+
+from __future__ import annotations
+
+import sys
+from pathlib import Path
+from unittest import mock
+
+HERE = Path(__file__).resolve().parent
+sys.path.insert(0, str(HERE))
+for base in HERE.parents:
+    core = base / "ejryan89-skill-core" / "scripts"
+    if core.is_dir():
+        sys.path.insert(0, str(core))
+        break
+
+import review_reviewer_setup as setup
+
+
+def test_a_file_is_present(tmp_path: Path) -> None:
+    manifest = tmp_path / "manifest.json"
+    manifest.write_text("{}", encoding="utf-8")
+
+    assert setup.manifest_state(manifest) == "present"
+
+
+def test_a_path_that_is_not_there_is_missing(tmp_path: Path) -> None:
+    assert setup.manifest_state(tmp_path / "manifest.json") == "missing"
+
+
+def test_a_path_that_cannot_be_examined_is_unreadable_with_the_reason(tmp_path: Path) -> None:
+    refused = PermissionError(13, "Permission denied")
+
+    with mock.patch.object(Path, "stat", side_effect=refused):
+        state = setup.manifest_state(tmp_path / "manifest.json")
+
+    assert state == "unreadable (Permission denied)"
`````

[Back to the shelf](README.md)
