# Fix 282: bitwarden-to-apple-keychain converter: one multi-site entry is reported as 1 multi-site entries

Status: UNSENT and UNTESTED. Free to take.

- Project: MehdiMamas/bitwarden-to-apple-keychain-converter-script
- Bug report title: Fix plural in "Found 1 multi-site entries"
- Bug report: number 7 ([open the bug report](https://github.com/MehdiMamas/bitwarden-to-apple-keychain-converter-script/issues/7))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/282-bitwarden-to-apple-keychain-7.patch](fixes/282-bitwarden-to-apple-keychain-7.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/282-bitwarden-to-apple-keychain-7.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-282-bitwarden-to-apple-keychain-7.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-282-bitwarden-to-apple-keychain-7.html

## The bug

With exactly one multi-site entry convert.py prints Found 1 multi-site entries.

## The fix

convert.py now picks the word entry for a count of 1 and entries for every other count. A new file tests/test_multi_site_plural.py runs the script on the sample export (one multi-site entry) and on a made-up export with two.

## Files changed

- convert.py
- tests/test_multi_site_plural.py

## How to use the fix

1. Get a copy of the project MehdiMamas/bitwarden-to-apple-keychain-converter-script.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 282-bitwarden-to-apple-keychain-7.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 7.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the script or the tests. This patch and the patch of fix 283 on this shelf change neighbouring lines of convert.py and do not apply together.

## Search words

bitwarden apple keychain convert.py multi-site entries entry plural Found 1

## The full patch

`````diff
diff --git a/convert.py b/convert.py
index d735464..bc9a2cb 100644
--- a/convert.py
+++ b/convert.py
@@ -90,7 +90,9 @@ def convert(input_path: str) -> None:
 
     print(f"Done — {kept} passwords written to {output_file}")
     if multi_site_entries:
-        print(f"Found {len(multi_site_entries)} multi-site entries — see {multi_site_file}")
+        count = len(multi_site_entries)
+        noun = "entry" if count == 1 else "entries"
+        print(f"Found {count} multi-site {noun} — see {multi_site_file}")
     if skipped:
         print(f"Skipped {skipped} non-login entries (notes, cards, etc.)")
 
diff --git a/tests/test_multi_site_plural.py b/tests/test_multi_site_plural.py
new file mode 100644
index 0000000..314b43b
--- /dev/null
+++ b/tests/test_multi_site_plural.py
@@ -0,0 +1,47 @@
+import shutil
+import subprocess
+import sys
+import tempfile
+import unittest
+from pathlib import Path
+
+ROOT = Path(__file__).resolve().parent.parent
+FIXTURE = ROOT / "tests" / "fixtures" / "sample_export.csv"
+HEADER = "folder,favorite,type,name,notes,fields,reprompt,login_uri,login_username,login_password,login_totp\n"
+
+
+def run(*args):
+    return subprocess.run([sys.executable, str(ROOT / "convert.py"), *map(str, args)],
+                          capture_output=True, text=True)
+
+
+class MultiSitePluralTest(unittest.TestCase):
+    def setUp(self):
+        self.tmp = Path(tempfile.mkdtemp())
+
+    def tearDown(self):
+        shutil.rmtree(self.tmp)
+
+    def test_one_multi_site_entry_uses_the_singular(self):
+        export = self.tmp / "export.csv"
+        shutil.copy(FIXTURE, export)
+        result = run(export)
+        self.assertEqual(result.returncode, 0)
+        self.assertIn("Found 1 multi-site entry ", result.stdout)
+        self.assertNotIn("multi-site entries", result.stdout)
+
+    def test_two_multi_site_entries_use_the_plural(self):
+        export = self.tmp / "export.csv"
+        export.write_text(
+            HEADER
+            + ',,login,A,,,0,"https://a.example.com,https://b.example.com",alice,pw-1,\n'
+            + ',,login,B,,,0,"https://c.example.com,https://d.example.com",bob,pw-2,\n',
+            encoding="utf-8",
+        )
+        result = run(export)
+        self.assertEqual(result.returncode, 0)
+        self.assertIn("Found 2 multi-site entries ", result.stdout)
+
+
+if __name__ == "__main__":
+    unittest.main()
`````

[Back to the shelf](README.md)
