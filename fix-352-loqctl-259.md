# Fix 352: loqctl: a power mode change during a fan curve write still reports success

Status: UNSENT and UNTESTED. Free to take.

- Project: liualt/loqctl
- Bug report title: Fn+Q during a fan curve write still reports success
- Bug report: number 259 ([open the bug report](https://github.com/liualt/loqctl/issues/259))
- Project license: GPL-3.0
- Language: Python
- Test included: yes
- Patch file: [fixes/352-loqctl-259.patch](fixes/352-loqctl-259.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/352-loqctl-259.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-352-loqctl-259.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-352-loqctl-259.html

## The bug

Hardware.write_fancurve in loqctl/hardware.py checks the mode once and then writes every point. The firmware can change the mode (Fn+Q) during the write. Points written after the change land in a mode that resets them and loqctl still reports success.

## The fix

write_fancurve now reads the mode again after the write and raises ControlError that names the new mode when the mode is no longer custom. A new block in the existing fan curve test makes read_mode answer custom and then balanced and expects the error.

## Files changed

- loqctl/hardware.py
- tests/test_fancurve.py

## How to use the fix

1. Get a copy of the project liualt/loqctl.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 352-loqctl-259.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 259.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's code or tests. The bug report also says active.json should not be updated in that case. The chatbot did not read the callers so nobody has confirmed that every caller skips the update when write_fancurve raises. The bug report says real hardware is needed to see what the firmware does with points written during a mode change.

## Search words

loqctl write_fancurve Fn+Q mode change during write custom mode fan curve success read_mode

## The full patch

`````diff
diff --git a/loqctl/hardware.py b/loqctl/hardware.py
index 63a3999..292c1d1 100644
--- a/loqctl/hardware.py
+++ b/loqctl/hardware.py
@@ -304,7 +304,12 @@ class Hardware:
             hwmon = find_legion_hwmon(self.root)
             if hwmon is None:
                 raise ControlError("legion_laptop hwmon not found.")
-            return write_curve(hwmon, points, curve_scale(hwmon))
+            result = write_curve(hwmon, points, curve_scale(hwmon))
+            after = self.read_mode()
+            if after != "custom":
+                raise ControlError(f"The power mode changed to {after} during the fan curve write, "
+                                   "so the curve may not be kept. Select custom and apply again.")
+            return result
 
 
 def check_changes(changes):
diff --git a/tests/test_fancurve.py b/tests/test_fancurve.py
index 94d862c..7b36d61 100644
--- a/tests/test_fancurve.py
+++ b/tests/test_fancurve.py
@@ -441,6 +441,9 @@ class FanCurveSurfaceTests(FanPanelFixture):
         with self.assertRaisesRegex(m_common.ControlError, "locked in balanced mode"):
             self.hw.write_fancurve(CURVE)
         self.set_mode("custom")
+        with patch.object(self.hw, "read_mode", side_effect=["custom", "balanced"]):
+            with self.assertRaisesRegex(m_common.ControlError, "changed to balanced during"):
+                self.hw.write_fancurve(CURVE)
         self.hw.write_fancurve(edit(CURVE, {(1, "fan1"): 90}))
         self.assertEqual(self.hw.fancurve()["points"][1]["fan1"], 90)
         self.assertFalse(m_hardware.Hardware(self.root / "nowhere").fancurve()["available"])
`````

[Back to the shelf](README.md)
