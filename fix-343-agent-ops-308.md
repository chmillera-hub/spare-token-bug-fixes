# Fix 343: agent-ops: an inspection test fails under make gate because the nested make prints directory lines

Status: UNSENT and UNTESTED. Free to take.

- Project: jesdi/agent-ops
- Bug report title: Inspection test fails under make gate because nested Make prints directory lines
- Bug report: number 308 ([open the bug report](https://github.com/jesdi/agent-ops/issues/308))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/343-agent-ops-308.patch](fixes/343-agent-ops-308.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/343-agent-ops-308.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-343-agent-ops-308.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-343-agent-ops-308.html

## The bug

test_explicit_makefile_draft_bypasses_default_precedence in tests/test_inspection_commands.py starts make and compares the full output with verified. When pytest itself runs under make (make gate) the nested make inherits MAKELEVEL and MAKEFLAGS and prints Entering directory and Leaving directory lines so the comparison fails.

## The fix

The test now starts the nested make with an environment that leaves out MAKEFLAGS and MAKELEVEL and MFLAGS. The nested make then behaves like a top-level make and prints only verified. The strict comparison stays so the test still proves that the explicit Makefile target ran.

## Files changed

- tests/test_inspection_commands.py

## How to use the fix

1. Get a copy of the project jesdi/agent-ops.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 343-agent-ops-308.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 308.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- Only a test changed. The chatbot did not run the project's tests or make. The chatbot did not check whether other tests in the project start a nested make and compare the full output.

## Search words

agent-ops make gate nested make Entering directory MAKELEVEL MAKEFLAGS test_inspection_commands verified

## The full patch

`````diff
diff --git a/tests/test_inspection_commands.py b/tests/test_inspection_commands.py
index 17fdb82..fe95c47 100644
--- a/tests/test_inspection_commands.py
+++ b/tests/test_inspection_commands.py
@@ -155,14 +155,19 @@ def test_implicit_make_draft_cannot_use_a_shadowed_makefile(tmp_path, box, monke
 
 
 def test_explicit_makefile_draft_bypasses_default_precedence(tmp_path, box, monkeypatch):
+    import os
     import subprocess
     command = 'make -f Makefile gate'
     rec = draft_for_repository(tmp_path, box, monkeypatch,
         {'Makefile': 'gate:\n\t@printf "verified\\n"\n', 'GNUmakefile': 'other:\n\t@true\n'},
         {'gate_cmd': {'value': command, 'reason': 'explicit Makefile target', 'evidence': 'Makefile'}})
     repository = rec.proposal['repositories'][0]
+    # Under `make gate` this test runs inside make: drop the variables that make a nested
+    # make print "Entering directory" / "Leaving directory" lines.
+    env = {key: value for key, value in os.environ.items()
+           if key not in ('MAKEFLAGS', 'MAKELEVEL', 'MFLAGS')}
     actual = subprocess.run(['make', '-f', 'Makefile', 'gate'], cwd=repository['clone_path'],
-                            capture_output=True, text=True, timeout=10)
+                            capture_output=True, text=True, timeout=10, env=env)
     assert actual.returncode == 0
     assert actual.stdout == 'verified\n'
     assert repository['gate_cmd'] == command
`````

[Back to the shelf](README.md)
