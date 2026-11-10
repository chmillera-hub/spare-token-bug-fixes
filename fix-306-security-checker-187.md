# Fix 306: security-checker: review --dry-run and --estimate show a traceback when the scan raises a configuration error

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(cli): review --estimate / --dry-run がスキャン中の SecurityCheckerError を捕まえず、トレースバックで終わる
- Bug report: number 187 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/187))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/306-security-checker-187.patch](fixes/306-security-checker-187.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/306-security-checker-187.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-306-security-checker-187.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-306-security-checker-187.html

## The bug

_estimate and _dry_run in src/security_checker/cli.py call run_scan with no try block. A ConfigError during the scan ends with a Python traceback and exit code 1 while the promise for configuration errors is exit code 2.

## The fix

Both run_scan calls now sit inside try and except SecurityCheckerError and go through _fail like scan and review do. A new file tests/unit/test_review_dry_run_scan_error.py makes run_scan raise ConfigError and expects exit code 2 and the formatted message for --dry-run.

## Files changed

- src/security_checker/cli.py
- tests/unit/test_review_dry_run_scan_error.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 306-security-checker-187.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 187.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The new test covers --dry-run only. The --estimate path got the same change and has no test because the chatbot did not read what --estimate needs before the scan.

## Search words

security-checker cli review --dry-run --estimate run_scan SecurityCheckerError ConfigError traceback exit code 2

## The full patch

`````diff
diff --git a/src/security_checker/cli.py b/src/security_checker/cli.py
index 6f0a497..c44ca30 100644
--- a/src/security_checker/cli.py
+++ b/src/security_checker/cli.py
@@ -380,15 +380,18 @@ def _estimate(
 ) -> None:
     """何件・いくらかかるかを、送信前に見せる (設計書 §24.3)."""
     console = Console()
-    outcome = asyncio.run(
-        run_scan(
-            loaded.config,
-            root,
-            extra_warnings=loaded.warnings,
-            diff=diff,
-            suppression=_suppression(loaded, root),
+    try:
+        outcome = asyncio.run(
+            run_scan(
+                loaded.config,
+                root,
+                extra_warnings=loaded.warnings,
+                diff=diff,
+                suppression=_suppression(loaded, root),
+            )
         )
-    )
+    except SecurityCheckerError as exc:
+        _fail(str(exc), exc.exit_code)
     tasks, overflow = build_tasks(outcome.report.candidates, root, loaded.config)
     result = estimate_run(tasks, loaded.config, price_table)
     console.print(
@@ -426,15 +429,18 @@ def _dry_run(
 ) -> None:
     """何が送信されるかを、送信前に全部見せる (設計書 §19.3)."""
     console = Console()
-    outcome = asyncio.run(
-        run_scan(
-            loaded.config,
-            root,
-            extra_warnings=[*loaded.warnings, *diff_warnings],
-            diff=diff,
-            suppression=_suppression(loaded, root),
+    try:
+        outcome = asyncio.run(
+            run_scan(
+                loaded.config,
+                root,
+                extra_warnings=[*loaded.warnings, *diff_warnings],
+                diff=diff,
+                suppression=_suppression(loaded, root),
+            )
         )
-    )
+    except SecurityCheckerError as exc:
+        _fail(str(exc), exc.exit_code)
     for message in diff_warnings:
         console.print(f"[yellow]警告[/yellow]: {message}", highlight=False)
     if diff is not None:
diff --git a/tests/unit/test_review_dry_run_scan_error.py b/tests/unit/test_review_dry_run_scan_error.py
new file mode 100644
index 0000000..335b130
--- /dev/null
+++ b/tests/unit/test_review_dry_run_scan_error.py
@@ -0,0 +1,39 @@
+"""review --dry-run: スキャン中の SecurityCheckerError を整形して終了すること (#187)."""
+
+from __future__ import annotations
+
+from pathlib import Path
+from typing import Any
+
+import pytest
+from typer.testing import CliRunner
+
+from security_checker import cli
+from security_checker.errors import ConfigError, ExitCode
+
+runner = CliRunner()
+
+
+def test_config_error_during_the_scan_is_a_formatted_exit_2(
+    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
+) -> None:
+    (tmp_path / "security-checker.yml").write_text(
+        "version: 1\n"
+        "scanners:\n  semgrep: { enabled: false }\n  gitleaks: { enabled: false }\n"
+        "reviewers:\n"
+        "  - name: r1\n    transport: http\n    dialect: openai_chat\n"
+        "    base_url: http://127.0.0.1:9/v1\n    model: m\n",
+        encoding="utf-8",
+    )
+
+    async def broken(*args: Any, **kwargs: Any) -> Any:
+        raise ConfigError("同梱ルールを解決できません")
+
+    monkeypatch.setattr(cli, "run_scan", broken)
+    monkeypatch.chdir(tmp_path)
+
+    result = runner.invoke(cli.app, ["review", str(tmp_path), "--dry-run"])
+
+    assert result.exit_code == ExitCode.CONFIG_ERROR
+    assert isinstance(result.exception, SystemExit)
+    assert "同梱ルールを解決できません" in result.stderr
`````

[Back to the shelf](README.md)
