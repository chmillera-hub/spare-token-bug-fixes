# Fix 347: coding-agent-skills: a release entry that is not an object is skipped like a draft

Status: UNSENT and UNTESTED. Free to take.

- Project: EJRyan89/coding-agent-skills
- Bug report title: runtime_changelogs: a release item that is not an object is passed over
- Bug report: number 2530 ([open the bug report](https://github.com/EJRyan89/coding-agent-skills/issues/2530))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/347-coding-agent-skills-2530.patch](fixes/347-coding-agent-skills-2530.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/347-coding-agent-skills-2530.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-347-coding-agent-skills-2530.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-347-coding-agent-skills-2530.html

## The bug

github_releases in tools/runtime_changelogs.py skips a member of the releases list that is not an object in the same branch that skips drafts and prereleases. A changed answer shape from GitHub gives fewer releases and no failure.

## The fix

github_releases now raises WatchError that names the address and the position of the entry when a member is not an object. Drafts and prereleases are skipped as before. A new file tests/tools/test_runtime_changelogs_release_shape.py covers a text entry and a null entry and a list that holds only a draft.

## Files changed

- tests/tools/test_runtime_changelogs_release_shape.py
- tools/runtime_changelogs.py

## How to use the fix

1. Get a copy of the project EJRyan89/coding-agent-skills.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 347-coding-agent-skills-2530.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 2530.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's code or tests. The wording of the new error is the chatbot's own. The new test file imports the module the same way the existing test file does.

## Search words

coding-agent-skills runtime_changelogs github_releases release item not an object skipped draft WatchError

## The full patch

`````diff
diff --git a/tests/tools/test_runtime_changelogs_release_shape.py b/tests/tools/test_runtime_changelogs_release_shape.py
new file mode 100644
index 0000000..92d9c27
--- /dev/null
+++ b/tests/tools/test_runtime_changelogs_release_shape.py
@@ -0,0 +1,29 @@
+"""github_releases refuses a release entry that is not an object."""
+
+from __future__ import annotations
+
+import sys
+from pathlib import Path
+
+import pytest
+
+sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
+sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "skills" / "ejryan89-skill-core" / "scripts"))
+
+from tools import runtime_changelogs as watch
+
+URL = "https://example.com/releases"
+
+
+@pytest.mark.parametrize("entry", ["v1.2.3", None, 7, ["tag_name"]])
+def test_an_entry_that_is_not_an_object_is_refused_by_position(entry: object) -> None:
+    payload = [{"tag_name": "v1.2.4", "body": "notes"}, entry]
+
+    with pytest.raises(watch.WatchError, match="release 2 that is not an object") as raised:
+        watch.github_releases(payload, URL)
+
+    assert URL in str(raised.value)
+
+
+def test_a_draft_is_still_passed_over() -> None:
+    assert watch.github_releases([{"tag_name": "v1.2.3", "draft": True}], URL) == []
diff --git a/tools/runtime_changelogs.py b/tools/runtime_changelogs.py
index 6c7f998..572046b 100644
--- a/tools/runtime_changelogs.py
+++ b/tools/runtime_changelogs.py
@@ -453,8 +453,10 @@ def github_releases(payload: object, url: str) -> list[Release]:
     if not isinstance(payload, list):
         raise WatchError(f"{url} did not return a list of releases")
     releases: list[Release] = []
-    for item in payload:
-        if not isinstance(item, dict) or item.get("draft") or item.get("prerelease"):
+    for number, item in enumerate(payload, start=1):
+        if not isinstance(item, dict):
+            raise WatchError(f"{url} returned release {number} that is not an object")
+        if item.get("draft") or item.get("prerelease"):
             continue
         found = re.search(r"(?<![0-9.])([0-9]+(?:\.[0-9]+)+)(?![0-9.]|-)", str(item.get("tag_name", "")))
         if found:
`````

[Back to the shelf](README.md)
