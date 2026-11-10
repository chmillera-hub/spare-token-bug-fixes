# Fix 361: neuralforecast: Tweedie.variance raises AttributeError because of the misspelled torch.ones_line

Status: UNSENT and UNTESTED. Free to take.

- Project: Nixtla/neuralforecast
- Bug report title: Tweedie.variance raises AttributeError (torch.ones_line typo)
- Bug report: number 1693 ([open the bug report](https://github.com/Nixtla/neuralforecast/issues/1693))
- Project license: Apache-2.0
- Language: Python
- Test included: yes
- Patch file: [fixes/361-neuralforecast-1693.patch](fixes/361-neuralforecast-1693.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/361-neuralforecast-1693.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-361-neuralforecast-1693.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-361-neuralforecast-1693.html

## The bug

Tweedie.variance in neuralforecast/losses/pytorch.py calls torch.ones_line which does not exist. variance and stddev raise AttributeError every time.

## The fix

variance now returns mean to the power rho which is the formula the bug report gives (sigma2 times mean to the power rho with sigma2 fixed at 1 as the class docstring says). A new file tests/test_losses/test_tweedie_variance.py expects variance 1 and 8 and the matching stddev for means 1 and 4 with rho 1.5.

## Files changed

- neuralforecast/losses/pytorch.py
- tests/test_losses/test_tweedie_variance.py

## How to use the fix

1. Get a copy of the project Nixtla/neuralforecast.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 361-neuralforecast-1693.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 1693.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's code or tests. The old line carried a TODO comment that said the value still had to be assigned. The new line follows the formula from the bug report and the chatbot did not check the formula against a statistics reference.

## Search words

neuralforecast Tweedie variance stddev AttributeError torch.ones_line ones_like losses pytorch rho

## The full patch

`````diff
diff --git a/neuralforecast/losses/pytorch.py b/neuralforecast/losses/pytorch.py
index f6be248..8247165 100644
--- a/neuralforecast/losses/pytorch.py
+++ b/neuralforecast/losses/pytorch.py
@@ -1097,7 +1097,8 @@ class Tweedie(Distribution):
 
     @property
     def variance(self):
-        return torch.ones_line(self.log_mu)  # TODO need to be assigned
+        # sigma2 * mean ** rho, with the dispersion sigma2 fixed in 1 (see the class docstring)
+        return self.mean**self.rho
 
     def sample(self, sample_shape=torch.Size()):
         shape = self._extended_shape(sample_shape)
diff --git a/tests/test_losses/test_tweedie_variance.py b/tests/test_losses/test_tweedie_variance.py
new file mode 100644
index 0000000..e954820
--- /dev/null
+++ b/tests/test_losses/test_tweedie_variance.py
@@ -0,0 +1,10 @@
+import torch
+
+from neuralforecast.losses.pytorch import Tweedie
+
+
+def test_variance_is_the_mean_to_the_power_rho():
+    distribution = Tweedie(log_mu=torch.log(torch.tensor([1.0, 4.0])), rho=1.5)
+
+    torch.testing.assert_close(distribution.variance, torch.tensor([1.0, 8.0]))
+    torch.testing.assert_close(distribution.stddev, torch.tensor([1.0, 8.0]).sqrt())
`````

[Back to the shelf](README.md)
