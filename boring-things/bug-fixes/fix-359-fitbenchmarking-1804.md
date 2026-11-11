# Fix 359: fitbenchmarking: typos in three error messages

Status: UNSENT and UNTESTED. Free to take.

- Project: fitbenchmarking/fitbenchmarking
- Bug report title: Typos in error messages
- Bug report: number 1804 ([open the bug report](https://github.com/fitbenchmarking/fitbenchmarking/issues/1804))
- Project license: BSD-3-Clause
- Language: Python
- Test included: no
- Patch file: [fixes/359-fitbenchmarking-1804.patch](fixes/359-fitbenchmarking-1804.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/359-fitbenchmarking-1804.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-359-fitbenchmarking-1804.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-359-fitbenchmarking-1804.html

## The bug

fitbenchmarking/utils/exceptions.py spells occurred as occured in two error messages and says raised and exception where raised an exception is meant.

## The fix

The three messages now read An error occurred while verifying controller and Fitting Problem raised an exception and An error occurred during handling the checkpoint file.

## Files changed

- fitbenchmarking/utils/exceptions.py

## How to use the fix

1. Get a copy of the project fitbenchmarking/fitbenchmarking.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 359-fitbenchmarking-1804.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 1804.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- No test was added because only message texts changed. A text search found neither misspelling in any other Python file under the fitbenchmarking folder. The chatbot did not run the project's tests so nobody has confirmed that no test compares the old texts. The license name on the shelf is the chatbot's reading of LICENSE.txt (redistribution allowed with conditions).

## Search words

fitbenchmarking exceptions typo occured occurred raised and exception error message

## The full patch

`````diff
diff --git a/fitbenchmarking/utils/exceptions.py b/fitbenchmarking/utils/exceptions.py
index 9379cb7..95fe1d4 100644
--- a/fitbenchmarking/utils/exceptions.py
+++ b/fitbenchmarking/utils/exceptions.py
@@ -36,7 +36,7 @@ class ValidationException(FitBenchmarkException):
     a combination from running.
     """
 
-    class_message = "An error occured while verifying controller."
+    class_message = "An error occurred while verifying controller."
 
 
 class OptionsError(FitBenchmarkException):
@@ -120,7 +120,7 @@ class FittingProblemError(FitBenchmarkException):
     Indicates a problem with the fitting problem.
     """
 
-    class_message = "Fitting Problem raised and exception."
+    class_message = "Fitting Problem raised an exception."
     error_code = 10
 
 
@@ -306,7 +306,7 @@ class CheckpointError(FitBenchmarkException):
     Indicates an error occured during checkpointing.
     """
 
-    class_message = "An error occured during handling the checkpoint file."
+    class_message = "An error occurred during handling the checkpoint file."
     error_code = 28
`````

[Back to the shelf](README.md)
