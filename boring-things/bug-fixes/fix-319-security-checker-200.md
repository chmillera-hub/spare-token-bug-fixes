# Fix 319: security-checker: providers check starts a new event loop for every reviewer

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(cli): providers check が Reviewer ごとに asyncio.run を呼び、Provider を閉じる前にイベントループが変わる
- Bug report: number 200 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/200))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/319-security-checker-200.patch](fixes/319-security-checker-200.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/319-security-checker-200.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-319-security-checker-200.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-319-security-checker-200.html

## The bug

providers_check in src/security_checker/cli.py calls asyncio.run once per reviewer. Each call closes its event loop while a provider may still hold connections that belong to that loop.

## The fix

The loop over the reviewers now runs inside one coroutine and providers_check calls asyncio.run once. The output per reviewer and the exit code are unchanged. A new file tests/unit/test_providers_check_single_event_loop.py replaces check_reviewer and expects both reviewers to be checked inside the same event loop.

## Files changed

- src/security_checker/cli.py
- tests/unit/test_providers_check_single_event_loop.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 319-security-checker-200.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 200.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The reviewers are still checked one after another. The bug report mentions asyncio.gather as an option and this patch does not use gather. The bug report also says that a provider is not closed before the loop ends. This patch does not add a close call.

## Search words

security-checker cli providers check asyncio.run event loop per reviewer closed loop provider aclose single loop

## The full patch

`````diff
diff --git a/src/security_checker/cli.py b/src/security_checker/cli.py
index 6f0a497..dd227ab 100644
--- a/src/security_checker/cli.py
+++ b/src/security_checker/cli.py
@@ -855,17 +855,22 @@ def providers_check(
             ExitCode.CONFIG_ERROR,
         )
     console = Console()
-    failed = False
-    for reviewer in reviewers:
-        result = asyncio.run(check_reviewer(reviewer, probe=not no_probe))
-        mark = "[green]✓[/green]" if result.ok else "[red]✗[/red]"
-        console.print(f"{mark} [bold]{result.name}[/bold] ({result.transport})")
-        for step in result.steps:
-            step_mark = "[green]ok[/green]" if step.ok else "[red]NG[/red]"
-            console.print(f"    {step.label:<8} {step_mark}  {step.detail}", highlight=False)
-        for suggestion in result.suggestions:
-            console.print(f"    [yellow]→[/yellow] {suggestion}", highlight=False)
-        failed = failed or not result.ok
+    async def check_all() -> bool:
+        """全 Reviewer を 1 つのイベントループの中で順に確かめる (#200)."""
+        failed = False
+        for reviewer in reviewers:
+            result = await check_reviewer(reviewer, probe=not no_probe)
+            mark = "[green]✓[/green]" if result.ok else "[red]✗[/red]"
+            console.print(f"{mark} [bold]{result.name}[/bold] ({result.transport})")
+            for step in result.steps:
+                step_mark = "[green]ok[/green]" if step.ok else "[red]NG[/red]"
+                console.print(f"    {step.label:<8} {step_mark}  {step.detail}", highlight=False)
+            for suggestion in result.suggestions:
+                console.print(f"    [yellow]→[/yellow] {suggestion}", highlight=False)
+            failed = failed or not result.ok
+        return failed
+
+    failed = asyncio.run(check_all())
     raise typer.Exit(code=int(ExitCode.EXECUTION_ERROR if failed else ExitCode.OK))
 
 
diff --git a/tests/unit/test_providers_check_single_event_loop.py b/tests/unit/test_providers_check_single_event_loop.py
new file mode 100644
index 0000000..f051783
--- /dev/null
+++ b/tests/unit/test_providers_check_single_event_loop.py
@@ -0,0 +1,48 @@
+"""providers check: 全 Reviewer を 1 回の asyncio.run の中で確かめること (#200)."""
+
+from __future__ import annotations
+
+import asyncio
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
+    "  - name: r2\n    transport: http\n    dialect: openai_chat\n"
+    "    base_url: http://127.0.0.1:9/v1\n    model: m\n"
+)
+
+
+def test_two_reviewers_are_checked_inside_one_event_loop(
+    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
+) -> None:
+    (tmp_path / "security-checker.yml").write_text(CONFIG, encoding="utf-8")
+    loops: list[asyncio.AbstractEventLoop] = []
+
+    async def fake_check(reviewer: Any, *, probe: bool) -> Any:
+        loops.append(asyncio.get_running_loop())
+        return SimpleNamespace(
+            ok=True, name=reviewer.name, transport="http", steps=[], suggestions=[]
+        )
+
+    monkeypatch.setattr(cli, "check_reviewer", fake_check)
+
+    result = runner.invoke(cli.app, ["providers", "check", "--path", str(tmp_path)])
+
+    assert result.exit_code == 0
+    assert len(loops) == 2
+    assert loops[0] is loops[1]
+    assert "r1" in result.stdout
+    assert "r2" in result.stdout
`````

[Back to the shelf](README.md)
