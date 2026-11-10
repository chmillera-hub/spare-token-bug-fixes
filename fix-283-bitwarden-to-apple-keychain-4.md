# Fix 283: bitwarden-to-apple-keychain converter: empty logins are counted as non-login entries in the skip message

Status: UNSENT and UNTESTED. Free to take.

- Project: MehdiMamas/bitwarden-to-apple-keychain-converter-script
- Bug report title: Skip message counts empty logins as "non-login entries"
- Bug report: number 4 ([open the bug report](https://github.com/MehdiMamas/bitwarden-to-apple-keychain-converter-script/issues/4))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/283-bitwarden-to-apple-keychain-4.patch](fixes/283-bitwarden-to-apple-keychain-4.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/283-bitwarden-to-apple-keychain-4.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-283-bitwarden-to-apple-keychain-4.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-283-bitwarden-to-apple-keychain-4.html

## The bug

convert.py adds one to the same counter for a row that is not a login and for a login row with no URL and no username and no password. The message then calls all of them non-login entries.

## The fix

convert.py now counts empty logins in a counter of their own and prints a second line such as Skipped 1 empty login. The line for non-login entries keeps its wording. A new file tests/test_skip_counts.py covers a made-up export with two notes and one empty login and checks that the sample export prints no empty login line.

## Files changed

- convert.py
- tests/test_skip_counts.py

## How to use the fix

1. Get a copy of the project MehdiMamas/bitwarden-to-apple-keychain-converter-script.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 283-bitwarden-to-apple-keychain-4.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 4.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The bug report gives the wording of both lines as an example. The chatbot kept the existing ending (notes and cards etc.) on the non-login line and chose logins for a count above one. The chatbot did not run the script or the tests. This patch and the patch of fix 282 on this shelf change neighbouring lines of convert.py and do not apply together.

## Search words

bitwarden apple keychain convert.py skipped non-login entries empty login count message

## The full patch

`````diff
diff --git a/convert.py b/convert.py
index d735464..d1ddd6c 100644
--- a/convert.py
+++ b/convert.py
@@ -38,6 +38,7 @@ def convert(input_path: str) -> None:
     kept = 0
     skipped = 0
     multi_site_entries = []
+    empty_logins = 0
 
     with open(input_file, newline="", encoding="utf-8-sig") as fin, \
          open(output_file, "w", newline="", encoding="utf-8") as fout:
@@ -57,7 +58,7 @@ def convert(input_path: str) -> None:
             name = (row.get("name") or "").strip()
 
             if not raw_uri and not username and not password:
-                skipped += 1
+                empty_logins += 1
                 continue
 
             uris = [u.strip() for u in raw_uri.split(",") if u.strip()] if raw_uri else [""]
@@ -93,6 +94,9 @@ def convert(input_path: str) -> None:
         print(f"Found {len(multi_site_entries)} multi-site entries — see {multi_site_file}")
     if skipped:
         print(f"Skipped {skipped} non-login entries (notes, cards, etc.)")
+    if empty_logins:
+        noun = "login" if empty_logins == 1 else "logins"
+        print(f"Skipped {empty_logins} empty {noun}")
 
 
 if __name__ == "__main__":
diff --git a/tests/test_skip_counts.py b/tests/test_skip_counts.py
new file mode 100644
index 0000000..2190f51
--- /dev/null
+++ b/tests/test_skip_counts.py
@@ -0,0 +1,51 @@
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
+class SkipCountsTest(unittest.TestCase):
+    def setUp(self):
+        self.tmp = Path(tempfile.mkdtemp())
+
+    def tearDown(self):
+        shutil.rmtree(self.tmp)
+
+    def test_non_logins_and_empty_logins_are_counted_separately(self):
+        export = self.tmp / "export.csv"
+        export.write_text(
+            HEADER
+            + ",,note,Wifi,network: example,,0,,,,\n"
+            + ",,card,Test card,,,0,,,,\n"
+            + ",,login,Empty,,,0,,,,\n"
+            + ",,login,Kept,,,0,https://a.example.com,alice,pw-1,\n",
+            encoding="utf-8",
+        )
+        result = run(export)
+        self.assertEqual(result.returncode, 0)
+        self.assertIn("1 passwords written", result.stdout)
+        self.assertIn("Skipped 2 non-login entries", result.stdout)
+        self.assertIn("Skipped 1 empty login", result.stdout)
+        self.assertNotIn("empty logins", result.stdout)
+
+    def test_sample_export_has_no_empty_login_line(self):
+        export = self.tmp / "export.csv"
+        shutil.copy(FIXTURE, export)
+        result = run(export)
+        self.assertIn("Skipped 2 non-login entries", result.stdout)
+        self.assertNotIn("empty login", result.stdout)
+
+
+if __name__ == "__main__":
+    unittest.main()
`````

[Back to the shelf](README.md)
