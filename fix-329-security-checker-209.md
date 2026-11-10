# Fix 329: security-checker: init --stdout mixes the detection list into the YAML on standard output

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(cli): `init --stdout` が検出結果の一覧も標準出力に書き、`> security-checker.yml` が YAML として読めない
- Bug report: number 209 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/209))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/329-security-checker-209.patch](fixes/329-security-checker-209.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/329-security-checker-209.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-329-security-checker-209.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-329-security-checker-209.html

## The bug

init in src/security_checker/cli.py prints the list of detected tools to standard output and then prints the generated YAML to the same stream when --stdout is set. Redirecting the output to a file gives a file that is not valid YAML.

## The fix

With --stdout the detection list and every other message of init now go to standard error and only the YAML goes to standard output. Without --stdout nothing changes. A new file tests/unit/test_init_stdout_only_yaml.py runs the command from the bug report and expects standard output to parse as YAML.

## Files changed

- src/security_checker/cli.py
- tests/unit/test_init_stdout_only_yaml.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 329-security-checker-209.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 209.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The test uses the command line from the bug report and assumes that the command needs no answer from a person.

## Search words

security-checker cli init --stdout YAML detections standard output stderr redirect invalid yaml

## The full patch

`````diff
diff --git a/src/security_checker/cli.py b/src/security_checker/cli.py
index 6f0a497..d7436c2 100644
--- a/src/security_checker/cli.py
+++ b/src/security_checker/cli.py
@@ -550,7 +550,8 @@ def init(
     root = path.expanduser().resolve()
     if not root.is_dir():
         _fail(f"ディレクトリが見つかりません: {path}", ExitCode.CONFIG_ERROR)
-    console = Console()
+    # --stdout では YAML だけを標準出力に出し、検出結果の一覧などは標準エラーに回す (#209)
+    console = Console(stderr=True) if stdout else Console()
 
     usable = _print_detections(console, detect_all())
     blocks: list[dict[str, Any]] = []
diff --git a/tests/unit/test_init_stdout_only_yaml.py b/tests/unit/test_init_stdout_only_yaml.py
new file mode 100644
index 0000000..9b7b547
--- /dev/null
+++ b/tests/unit/test_init_stdout_only_yaml.py
@@ -0,0 +1,21 @@
+"""init --stdout: 標準出力には YAML だけを出し、検出結果の一覧は標準エラーに回すこと (#209)."""
+
+from __future__ import annotations
+
+from pathlib import Path
+
+import yaml
+from typer.testing import CliRunner
+
+from security_checker.cli import app
+
+runner = CliRunner()
+
+
+def test_stdout_holds_only_the_generated_yaml(tmp_path: Path) -> None:
+    result = runner.invoke(app, ["init", str(tmp_path), "--command", "mycmd --x", "--stdout"])
+
+    assert result.exit_code == 0
+    assert "環境を検出しています" not in result.stdout
+    assert "環境を検出しています" in result.stderr
+    assert isinstance(yaml.safe_load(result.stdout), dict)
`````

[Back to the shelf](README.md)
