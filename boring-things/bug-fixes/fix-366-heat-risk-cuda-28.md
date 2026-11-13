# Fix 366: heat-risk-cuda: a misspelled name in --impls crashes the benchmark after other timings are done

Status: UNSENT and UNTESTED. Free to take.

- Project: VolodymyrLinuxovich/heat-risk-cuda
- Bug report title: A typo in the benchmark implementation list crashes the run after other timings
- Bug report: number 28 ([open the bug report](https://github.com/VolodymyrLinuxovich/heat-risk-cuda/issues/28))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/366-heat-risk-cuda-28.patch](fixes/366-heat-risk-cuda-28.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/366-heat-risk-cuda-28.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-366-heat-risk-cuda-28.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-366-heat-risk-cuda-28.html

## The bug

bench.run accepts any name in --impls. An unknown name such as gpu-torch falls through to the CUDA path and fails there with a TypeError after the cpu timing has already run. The run ends with a traceback and keeps nothing.

## The fix

The five known names now sit in one list named IMPLS and argparse gets that list as choices so an unknown name is refused with exit code 2 before any data is generated. A new test file checks the refusal.

## Files changed

- bench/run.py
- tests/test_bench_impls.py

## How to use the fix

1. Get a copy of the project VolodymyrLinuxovich/heat-risk-cuda.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 366-heat-risk-cuda-28.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 28.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-12 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-12 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot checked the argparse behaviour with a small separate script and did not run the tests of the project.

## Search words

heat-risk-cuda bench run impls argparse choices unknown implementation name TypeError traceback

## The full patch

`````diff
diff --git a/bench/run.py b/bench/run.py
index 3d4503c..5380d13 100644
--- a/bench/run.py
+++ b/bench/run.py
@@ -48,6 +48,7 @@ SCHEMA_VERSION = 1
 RESULTS_DIR = Path(__file__).parent / "results"
 DEFAULT_SIZES = ["4x1000x365", "16x4000x365", "32x16000x365"]
 DRY_RUN_SIZES = ["2x50x30", "1x129x10"]
+IMPLS = ["cpu", "cpu_cpp", "gpu_torch", "gpu_cuda", "gpu_cuda_tiled"]
 
 
 class ResultsRefused(RuntimeError):
@@ -344,7 +345,8 @@ def main(argv: list[str] | None = None) -> int:
     p.add_argument(
         "--impls",
         nargs="+",
-        default=["cpu", "cpu_cpp", "gpu_torch", "gpu_cuda", "gpu_cuda_tiled"],
+        choices=IMPLS,
+        default=IMPLS,
     )
     p.add_argument("--device", default="cuda:0")
     p.add_argument("--reps", type=int, default=20)
diff --git a/tests/test_bench_impls.py b/tests/test_bench_impls.py
new file mode 100644
index 0000000..8903f4b
--- /dev/null
+++ b/tests/test_bench_impls.py
@@ -0,0 +1,16 @@
+import pytest
+
+from bench import run
+
+
+def test_an_unknown_implementation_name_is_refused_before_any_work(
+    capsys: pytest.CaptureFixture[str],
+) -> None:
+    with pytest.raises(SystemExit) as exc:
+        run.main(["--dry-run", "--impls", "cpu", "gpu-torch"])
+    assert exc.value.code == 2
+    assert "gpu-torch" in capsys.readouterr().err
+
+
+def test_every_known_implementation_name_is_offered() -> None:
+    assert run.IMPLS == ["cpu", "cpu_cpp", "gpu_torch", "gpu_cuda", "gpu_cuda_tiled"]
`````

[Back to the shelf](README.md)
