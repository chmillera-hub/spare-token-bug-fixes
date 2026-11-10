# Fix 345: loqctl: a busy firmware during a mode switch reports an error about limits

Status: UNSENT and UNTESTED. Free to take.

- Project: liualt/loqctl
- Bug report title: Mode switch EBUSY reports a limits error
- Bug report: number 258 ([open the bug report](https://github.com/liualt/loqctl/issues/258))
- Project license: GPL-3.0
- Language: Python
- Test included: yes
- Patch file: [fixes/345-loqctl-258.patch](fixes/345-loqctl-258.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/345-loqctl-258.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-345-loqctl-258.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-345-loqctl-258.html

## The bug

Hardware._write in loqctl/hardware.py turns EBUSY into the message Limits are only editable in custom mode for every caller. When the platform profile write returns EBUSY loqctl mode shows that message although the user changed no limit.

## The fix

_write now takes the EBUSY message as a parameter with the limits message as the default. set_mode passes a message about the mode switch (the example wording from the bug report). A new test in tests/test_hardware.py makes the profile write raise EBUSY and expects the mode message and no word about limits.

## Files changed

- loqctl/hardware.py
- tests/test_hardware.py

## How to use the fix

1. Get a copy of the project liualt/loqctl.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 345-loqctl-258.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 258.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The bug report allows two ways (a message per caller or a mapping inside set_mode). Both give the same behaviour and the chatbot chose the parameter. The chatbot did not run the project's code or tests.

## Search words

loqctl mode EBUSY platform_profile Limits are only editable in custom mode set_mode firmware busy

## The full patch

`````diff
diff --git a/loqctl/hardware.py b/loqctl/hardware.py
index 63a3999..87716f0 100644
--- a/loqctl/hardware.py
+++ b/loqctl/hardware.py
@@ -207,14 +207,14 @@ class Hardware:
                     "mode": mode, "modes": (read(choices, "") or "").split(),
                     "mode_driver": mode_driver, "gamezone_holder": self.gamezone_holder(), "attributes": attrs, "extra_limits": self.extra_limits(), "mode_limits": table, "mode_limits_error": reason}
 
-    def _write(self, path, value):
+    def _write(self, path, value, busy="Limits are only editable in custom mode. Select custom first."):
         try:
             path.write_text(str(value) + "\n")
         except PermissionError as exc:
             raise ControlError("Permission denied. Use sudo or start the privileged loqctl server.") from exc
         except OSError as exc:
             if exc.errno == errno.EBUSY:
-                raise ControlError("Limits are only editable in custom mode. Select custom first.") from exc
+                raise ControlError(busy) from exc
             raise ControlError(f"Firmware rejected the write: {exc.strerror}") from exc
         actual = read(path)
         if actual != str(value):
@@ -235,7 +235,8 @@ class Hardware:
                 raise ControlError("Custom cannot be selected through the legacy platform_profile file, "
                                    f"and no {GAMEZONE} platform profile was found.")
             self._static = {}
-            actual = self._write(profile, mode)
+            actual = self._write(profile, mode, busy="The firmware is busy and refused the mode change. "
+                                                     "Try again in a few seconds.")
             return {"mode": mode, "previous": previous, "current": actual, "verified": True}
 
     def set_value(self, key, value):
diff --git a/tests/test_hardware.py b/tests/test_hardware.py
index 598e834..6752137 100644
--- a/tests/test_hardware.py
+++ b/tests/test_hardware.py
@@ -330,6 +330,12 @@ class HardwareTests(helpers.SysfsCase):
             with self.assertRaisesRegex(m_common.ControlError, "custom mode"):
                 self.hw.set_value("ppt_pl1_spl", 60)
 
+    def test_ebusy_on_mode_switch_talks_about_the_mode(self):
+        with patch.object(Path, "write_text", side_effect=OSError(errno.EBUSY, "busy")):
+            with self.assertRaisesRegex(m_common.ControlError, "refused the mode change") as caught:
+                self.hw.set_mode("balanced")
+        self.assertNotIn("Limits", str(caught.exception))
+
     def add_profile(self, slot, name, mode="balanced"):
         profile = self.root / f"class/platform-profile/platform-profile-{slot}"
         profile.mkdir(parents=True)
`````

[Back to the shelf](README.md)
