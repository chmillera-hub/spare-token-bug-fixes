# Fix 299: security-checker: --preset with ../ reads a YAML file outside the presets folder

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(config): --preset に ../ を含む値を渡すと presets ディレクトリの外の YAML を読む
- Bug report: number 211 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/211))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/299-security-checker-211.patch](fixes/299-security-checker-211.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/299-security-checker-211.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-299-security-checker-211.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-299-security-checker-211.html

## The bug

load_config in src/security_checker/config/loader.py opens PRESET_DIR / preset.yml with no check of the name. A value such as ../../somewhere/x reads any .yml file as a preset.

## The fix

load_config now raises the existing preset does not exist ConfigError when the name is not one of available_presets(). A new file tests/unit/test_preset_name_outside_presets_dir.py points PRESET_DIR at a temporary folder and expects exit code 2 for ../outside and exit code 0 for a listed preset.

## Files changed

- src/security_checker/config/loader.py
- tests/unit/test_preset_name_outside_presets_dir.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 299-security-checker-211.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 211.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The test assumes that a preset file holding only version: 1 is a valid preset.

## Search words

security-checker config loader load_config preset PRESET_DIR path traversal ../ available_presets ConfigError

## The full patch

`````diff
diff --git a/src/security_checker/config/loader.py b/src/security_checker/config/loader.py
index d1fecb5..15de53a 100644
--- a/src/security_checker/config/loader.py
+++ b/src/security_checker/config/loader.py
@@ -219,7 +219,7 @@ def load_config(
 
     if preset is not None:
         preset_path = PRESET_DIR / f"{preset}.yml"
-        if not preset_path.is_file():
+        if preset not in available_presets() or not preset_path.is_file():
             raise ConfigError(
                 f"preset '{preset}' は存在しません。利用可能: {', '.join(available_presets())}"
             )
diff --git a/tests/unit/test_preset_name_outside_presets_dir.py b/tests/unit/test_preset_name_outside_presets_dir.py
new file mode 100644
index 0000000..e23bde5
--- /dev/null
+++ b/tests/unit/test_preset_name_outside_presets_dir.py
@@ -0,0 +1,43 @@
+"""--preset: presets ディレクトリの外の YAML を名前で指せないこと (#211)."""
+
+from __future__ import annotations
+
+from pathlib import Path
+
+import pytest
+from typer.testing import CliRunner
+
+from security_checker.cli import app
+from security_checker.config import loader
+
+runner = CliRunner()
+
+
+def _presets(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
+    presets = tmp_path / "presets"
+    presets.mkdir()
+    (presets / "only.yml").write_text("version: 1\n", encoding="utf-8")
+    (tmp_path / "outside.yml").write_text("version: 1\n", encoding="utf-8")
+    monkeypatch.setattr(loader, "PRESET_DIR", presets)
+    target = tmp_path / "target"
+    target.mkdir()
+    return target
+
+
+def test_preset_with_parent_directory_is_rejected(
+    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
+) -> None:
+    target = _presets(tmp_path, monkeypatch)
+
+    result = runner.invoke(app, ["config", "show", str(target), "--preset", "../outside"])
+
+    assert result.exit_code == 2
+
+
+def test_listed_preset_is_still_accepted(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
+    """対になるケース."""
+    target = _presets(tmp_path, monkeypatch)
+
+    result = runner.invoke(app, ["config", "show", str(target), "--preset", "only"])
+
+    assert result.exit_code == 0
`````

[Back to the shelf](README.md)
