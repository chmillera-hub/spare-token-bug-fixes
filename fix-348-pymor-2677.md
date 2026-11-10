# Fix 348: pymor: DiscreteTimeStepper reports the time of the previous step

Status: UNSENT and UNTESTED. Free to take.

- Project: pymor/pymor
- Bug report title: `DiscreteTimeStepper` reports wrong timestamps
- Bug report: number 2677 ([open the bug report](https://github.com/pymor/pymor/issues/2677))
- Project license: BSD-2-Clause
- Language: Python
- Test included: yes
- Patch file: [fixes/348-pymor-2677.patch](fixes/348-pymor-2677.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/348-pymor-2677.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-348-pymor-2677.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-348-pymor-2677.html

## The bug

DiscreteTimeStepper.iterate in src/pymor/algorithms/timestepping.py computes the state after step k and then yields that state with the time k. The state belongs to time k + 1. A time-varying input is then read one step late (the example in the bug report gives 0 0 1 where 0 1 2 is expected).

## The fix

iterate now yields the new state together with k + sign (the time after the step for forward and backward stepping). A new test in src/pymortests/algorithms/timestepping.py collects the times of a forward run from 0 to 5 and of a backward run from 5 to 0 and expects 0 to 5 and 5 to 0.

## Files changed

- src/pymor/algorithms/timestepping.py
- src/pymortests/algorithms/timestepping.py

## How to use the fix

1. Get a copy of the project pymor/pymor.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 348-pymor-2677.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 2677.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's code or tests. The new test checks the reported times of the stepper. The chatbot did not run the LTIModel example from the bug report so nobody has confirmed that the output of that example is now 0 1 2. Code that relied on the old time values would see times shifted by one step.

## Search words

pymor DiscreteTimeStepper iterate timestamp k wrong time feedthrough LTIModel sampling_time output

## The full patch

`````diff
diff --git a/src/pymor/algorithms/timestepping.py b/src/pymor/algorithms/timestepping.py
index 29f3ed9..b320bdc 100644
--- a/src/pymor/algorithms/timestepping.py
+++ b/src/pymor/algorithms/timestepping.py
@@ -498,7 +498,7 @@ class DiscreteTimeStepper(TimeStepper):
             U = M.apply_inverse(rhs, mu=mu_t, initial_guess=U)
             while sign * (k - k0) + 1 + (min(sign*dt, sign*DT) * 0.5) >= sign * num_ret_values * DT:
                 num_ret_values += 1
-                yield U, k
+                yield U, k + sign
 
 
 def _depends_on_time(obj, mu):
diff --git a/src/pymortests/algorithms/timestepping.py b/src/pymortests/algorithms/timestepping.py
index eef8247..a17d90f 100644
--- a/src/pymortests/algorithms/timestepping.py
+++ b/src/pymortests/algorithms/timestepping.py
@@ -107,3 +107,14 @@ def test_backward_stepping_discrete():
     U_backwards = time_stepper.solve(end_time, initial_time, initial_data, dt * operator, rhs=dt * rhs, mass=-mass,
                                      num_values=num_values)
     assert np.all((U - U_backwards).norm() <= tol)
+
+
+def test_discrete_time_stepper_reports_the_time_after_each_step():
+    fom, initial_time, end_time, nt, num_values, initial_data, operator, rhs, mass = setup_non_parametric_example()
+    time_stepper = DiscreteTimeStepper()
+
+    forward = time_stepper.iterate(0, 5, initial_data, 0.1 * operator, rhs=0.1 * rhs, mass=mass)
+    assert [t for _, t in forward] == [0, 1, 2, 3, 4, 5]
+
+    backward = time_stepper.iterate(5, 0, initial_data, 0.1 * operator, rhs=0.1 * rhs, mass=-mass)
+    assert [t for _, t in backward] == [5, 4, 3, 2, 1, 0]
`````

[Back to the shelf](README.md)
