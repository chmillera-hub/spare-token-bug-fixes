# Fix 330: security-checker: providers check and baseline update hide the warnings about settings that have no effect

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(cli): `providers check` と `baseline update` が設定の警告（受け付けたが効かない項目）を表示しない
- Bug report: number 214 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/214))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/330-security-checker-214.patch](fixes/330-security-checker-214.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/330-security-checker-214.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-330-security-checker-214.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-330-security-checker-214.html

## The bug

load_config collects warnings about settings that are accepted and have no effect. scan and review and config show and eval show them. providers_check and baseline_update in src/security_checker/cli.py show them nowhere so a mistyped reviewer setting gets a green check mark.

## The fix

A new helper _print_config_warnings prints the warnings to standard error and both commands call the helper right after loading the settings. A new file tests/unit/test_cli_config_warnings_providers_check_baseline_update.py uses the reviewer from the bug report (an http reviewer with a command) and expects the warning from both commands.

## Files changed

- src/security_checker/cli.py
- tests/unit/test_cli_config_warnings_providers_check_baseline_update.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 330-security-checker-214.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 214.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The bug report also asks to use one shared function in every command that loads the settings. This patch adds the function and uses the function in the two commands that showed no warnings. The other commands keep their own code. This patch and the patch of fix 307 on this shelf change neighbouring lines of providers_check and do not apply together.

## Search words

security-checker cli providers check baseline update loaded.warnings config warnings stderr unimplemented settings

## The full patch

`````diff
diff --git a/src/security_checker/cli.py b/src/security_checker/cli.py
index 6f0a497..bb41fcf 100644
--- a/src/security_checker/cli.py
+++ b/src/security_checker/cli.py
@@ -497,6 +497,12 @@ def _reviewer_block(name: str, command: list[str]) -> dict[str, Any]:
     }
 
 
+def _print_config_warnings(loaded: LoadedConfig) -> None:
+    """受け付けたが効かない設定の警告を標準エラーに出す (P9, #214)."""
+    for message in loaded.warnings:
+        err_console.print(f"[yellow]警告[/yellow]: {message}", highlight=False)
+
+
 def _print_detections(console: Console, detections: list[Detection]) -> list[Detection]:
     """検出結果を表示する. 推奨マークは付けず、検出順のまま並べる (§9.8)."""
     console.print("環境を検出しています…\n")
@@ -697,6 +703,7 @@ def baseline_update(
     if not root.is_dir():
         _fail(f"検査対象が見つかりません: {path}", ExitCode.CONFIG_ERROR)
     loaded = _load(root, config_path, None, {})
+    _print_config_warnings(loaded)
     config_dir = loaded.config_path.parent if loaded.config_path is not None else root
     configured = loaded.config.policy.baseline
     destination = output or (config_dir / (configured or DEFAULT_BASELINE))
@@ -848,6 +855,7 @@ def providers_check(
     """
     root = path.expanduser().resolve()
     loaded = _load(root, config_path, None, {})
+    _print_config_warnings(loaded)
     reviewers = [r for r in loaded.config.reviewers if name is None or r.name == name]
     if not reviewers:
         _fail(
diff --git a/tests/unit/test_cli_config_warnings_providers_check_baseline_update.py b/tests/unit/test_cli_config_warnings_providers_check_baseline_update.py
new file mode 100644
index 0000000..c697064
--- /dev/null
+++ b/tests/unit/test_cli_config_warnings_providers_check_baseline_update.py
@@ -0,0 +1,52 @@
+"""providers check / baseline update: 受け付けたが効かない設定の警告を出すこと (#214)."""
+
+from __future__ import annotations
+
+from pathlib import Path
+from types import SimpleNamespace
+from typing import Any
+
+import pytest
+from typer.testing import CliRunner
+
+from security_checker import cli
+
+runner = CliRunner()
+
+CONFIG = (
+    "version: 1\n"
+    "scanners:\n  semgrep: { enabled: false }\n  gitleaks: { enabled: false }\n"
+    "reviewers:\n"
+    "  - name: r1\n    transport: http\n    dialect: openai_chat\n"
+    "    base_url: http://127.0.0.1:9/v1\n    model: m\n"
+    "    command: [\"x\"]\n"
+)
+
+
+def test_providers_check_prints_the_config_warnings(
+    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
+) -> None:
+    (tmp_path / "security-checker.yml").write_text(CONFIG, encoding="utf-8")
+
+    async def fake_check(reviewer: Any, *, probe: bool) -> Any:
+        return SimpleNamespace(
+            ok=True, name=reviewer.name, transport="http", steps=[], suggestions=[]
+        )
+
+    monkeypatch.setattr(cli, "check_reviewer", fake_check)
+
+    result = runner.invoke(
+        cli.app, ["providers", "check", "--path", str(tmp_path), "--no-probe"]
+    )
+
+    assert "警告" in result.stderr
+    assert "command" in result.stderr
+
+
+def test_baseline_update_prints_the_config_warnings(tmp_path: Path) -> None:
+    (tmp_path / "security-checker.yml").write_text(CONFIG, encoding="utf-8")
+
+    result = runner.invoke(cli.app, ["baseline", "update", str(tmp_path)])
+
+    assert "警告" in result.stderr
+    assert "command" in result.stderr
`````

[Back to the shelf](README.md)
