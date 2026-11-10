# Fix 326: DL_bathy: set_reproducible switches cudnn.benchmark on which undoes deterministic training

Status: UNSENT and UNTESTED. Free to take.

- Project: buckai-observatory/DL_bathy
- Bug report title: set_reproducible enables cudnn.benchmark, which undoes deterministic training
- Bug report: number 37 ([open the bug report](https://github.com/buckai-observatory/DL_bathy/issues/37))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/326-DL_bathy-37.patch](fixes/326-DL_bathy-37.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/326-DL_bathy-37.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-326-DL_bathy-37.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-326-DL_bathy-37.html

## The bug

set_reproducible in dl_bathy/train.py sets torch.backends.cudnn.deterministic to True and on the next line sets cudnn.benchmark to True. With benchmark on cuDNN may pick a different algorithm from run to run.

## The fix

set_reproducible now sets cudnn.benchmark to False. A new file tests/test_set_reproducible.py calls the function and expects deterministic to be True and benchmark to be False.

## Files changed

- dl_bathy/train.py
- tests/test_set_reproducible.py

## How to use the fix

1. Get a copy of the project buckai-observatory/DL_bathy.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 326-DL_bathy-37.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 37.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The bug report also offers an optional call to torch.use_deterministic_algorithms. This patch does not add that call. Training on a GPU may run slower with benchmark off. The chatbot did not run the project's code or tests.

## Search words

DL_bathy set_reproducible cudnn.benchmark deterministic torch reproducible training seed

## The full patch

`````diff
diff --git a/dl_bathy/train.py b/dl_bathy/train.py
index 61c494f..6eef9df 100644
--- a/dl_bathy/train.py
+++ b/dl_bathy/train.py
@@ -57,7 +57,7 @@ def set_reproducible(seed=42):
     torch.cuda.manual_seed(seed)
     torch.cuda.manual_seed_all(seed)
     torch.backends.cudnn.deterministic = True
-    torch.backends.cudnn.benchmark     = True
+    torch.backends.cudnn.benchmark     = False
 
 
 # =============================================================================
diff --git a/tests/test_set_reproducible.py b/tests/test_set_reproducible.py
new file mode 100644
index 0000000..69188a5
--- /dev/null
+++ b/tests/test_set_reproducible.py
@@ -0,0 +1,13 @@
+import pytest
+
+torch = pytest.importorskip("torch")
+pytest.importorskip("segmentation_models_pytorch")
+
+from dl_bathy.train import set_reproducible
+
+
+def test_set_reproducible_keeps_cudnn_deterministic():
+    set_reproducible(7)
+
+    assert torch.backends.cudnn.deterministic is True
+    assert torch.backends.cudnn.benchmark is False
`````

[Back to the shelf](README.md)
