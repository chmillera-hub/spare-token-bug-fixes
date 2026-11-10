# Fix 284: bitwarden-to-apple-keychain converter: no way to choose where the Chrome CSV is written

Status: UNSENT and UNTESTED. Free to take.

- Project: MehdiMamas/bitwarden-to-apple-keychain-converter-script
- Bug report title: Add an --output option for the Chrome CSV path
- Bug report: number 5 ([open the bug report](https://github.com/MehdiMamas/bitwarden-to-apple-keychain-converter-script/issues/5))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/284-bitwarden-to-apple-keychain-5.patch](fixes/284-bitwarden-to-apple-keychain-5.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/284-bitwarden-to-apple-keychain-5.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-284-bitwarden-to-apple-keychain-5.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-284-bitwarden-to-apple-keychain-5.html

## The bug

convert.py always writes chrome_import.csv next to the input file.

## The fix

convert.py now reads its arguments with argparse (standard library) and accepts an optional --output PATH for the Chrome CSV. Without the option the file is written next to the input as before. The README usage section shows the option. A new file tests/test_output_option.py covers the option and the default.

## Files changed

- README.md
- convert.py
- tests/test_output_option.py

## How to use the fix

1. Get a copy of the project MehdiMamas/bitwarden-to-apple-keychain-converter-script.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 284-bitwarden-to-apple-keychain-5.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 5.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- Two behaviour changes come with argparse: a wrong number of arguments now ends with exit code 2 and the argparse usage text and the script now answers --help. multi_site_entries.txt is still written next to the input file because the bug report asks only about the Chrome CSV. The folder of the --output path must already exist. The chatbot did not run the script or the tests.

## Search words

bitwarden apple keychain convert.py --output argparse chrome_import.csv path option

## The full patch

`````diff
diff --git a/README.md b/README.md
index a68a705..69213f3 100644
--- a/README.md
+++ b/README.md
@@ -36,6 +36,12 @@ Then follow the [import steps](#import-steps).
 python3 convert.py <your_bitwarden_export.csv>
 ```
 
+To write the Chrome CSV somewhere else, add `--output`:
+
+```
+python3 convert.py <your_bitwarden_export.csv> --output <path/to/passwords.csv>
+```
+
 This produces two files:
 
 - **`chrome_import.csv`** -- all your website logins in Chrome's import format (`username, password, url`). Non-login entries (notes, wifi passwords, cards, identities) are filtered out.
diff --git a/convert.py b/convert.py
index d735464..a2c4a69 100644
--- a/convert.py
+++ b/convert.py
@@ -6,10 +6,10 @@ Converts a Bitwarden CSV export into a CSV that Chrome can import,
 which you can then import from Chrome into Safari → Keychain.
 
 Usage:
-    python3 convert.py <bitwarden_export.csv>
+    python3 convert.py <bitwarden_export.csv> [--output PATH]
 
 Output:
-    chrome_import.csv (in the same directory as the input file)
+    chrome_import.csv (in the same directory as the input file, or at PATH)
 
 Steps after running this script:
     1. Open Google Chrome
@@ -21,6 +21,7 @@ Steps after running this script:
     7. Passwords will sync to iCloud Keychain
 """
 
+import argparse
 import csv
 import sys
 from pathlib import Path
@@ -28,12 +29,12 @@ from pathlib import Path
 PLACEHOLDER = "aaa"
 
 
-def convert(input_path: str) -> None:
+def convert(input_path: str, output_path: str | None = None) -> None:
     input_file = Path(input_path)
     if not input_file.exists():
         sys.exit(f"File not found: {input_file}")
 
-    output_file = input_file.parent / "chrome_import.csv"
+    output_file = Path(output_path) if output_path else input_file.parent / "chrome_import.csv"
     multi_site_file = input_file.parent / "multi_site_entries.txt"
     kept = 0
     skipped = 0
@@ -96,6 +97,13 @@ def convert(input_path: str) -> None:
 
 
 if __name__ == "__main__":
-    if len(sys.argv) != 2:
-        sys.exit(f"Usage: python3 {sys.argv[0]} <bitwarden_export.csv>")
-    convert(sys.argv[1])
+    parser = argparse.ArgumentParser(
+        description="Convert a Bitwarden CSV export into a CSV that Chrome can import."
+    )
+    parser.add_argument("export", metavar="bitwarden_export.csv",
+                        help="path of the Bitwarden CSV export")
+    parser.add_argument("--output", metavar="PATH",
+                        help="where to write the Chrome CSV "
+                             "(default: chrome_import.csv next to the export)")
+    args = parser.parse_args()
+    convert(args.export, args.output)
diff --git a/tests/test_output_option.py b/tests/test_output_option.py
new file mode 100644
index 0000000..d8b3a3e
--- /dev/null
+++ b/tests/test_output_option.py
@@ -0,0 +1,49 @@
+import csv
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
+class OutputOptionTest(unittest.TestCase):
+    def setUp(self):
+        self.tmp = Path(tempfile.mkdtemp())
+        self.export = self.tmp / "export.csv"
+        shutil.copy(FIXTURE, self.export)
+
+    def tearDown(self):
+        shutil.rmtree(self.tmp)
+
+    def test_output_option_chooses_the_chrome_csv_path(self):
+        target = self.tmp / "elsewhere.csv"
+        result = run(self.export, "--output", target)
+        self.assertEqual(result.returncode, 0)
+        with open(target, newline="", encoding="utf-8") as f:
+            rows = list(csv.reader(f))
+        self.assertEqual(rows[0], ["username", "password", "url"])
+        self.assertEqual(len(rows), 4)
+        self.assertFalse((self.tmp / "chrome_import.csv").exists())
+        self.assertIn(str(target), result.stdout)
+
+    def test_default_path_is_unchanged(self):
+        result = run(self.export)
+        self.assertEqual(result.returncode, 0)
+        self.assertTrue((self.tmp / "chrome_import.csv").exists())
+
+    def test_missing_export_argument_fails(self):
+        self.assertNotEqual(run().returncode, 0)
+
+
+if __name__ == "__main__":
+    unittest.main()
`````

[Back to the shelf](README.md)
