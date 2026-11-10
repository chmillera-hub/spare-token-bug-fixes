# Fix 291: security-checker: no test covers a rate limiter slot that frees up after one minute

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: test(review): scheduler.py の acquire で未テストの分岐をテストする（1 行）
- Bug report: number 563 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/563))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/291-security-checker-563.patch](fixes/291-security-checker-563.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/291-security-checker-563.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-291-security-checker-563.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-291-security-checker-563.html

## The bug

RateLimiter.acquire in src/security_checker/review/scheduler.py drops send records older than 60 seconds before counting. No test ran the line that drops them.

## The fix

Tests only. A new file tests/unit/test_rate_limiter_expired_events.py puts one record from 61 seconds ago into a limiter with 1 request per minute and expects acquire to return with no wait and expects only the new record to remain.

## Files changed

- tests/unit/test_rate_limiter_expired_events.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 291-security-checker-563.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 563.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The bug report lists the untested lines from a coverage run on an older commit. The chatbot did not run the tests or a coverage tool so nobody has confirmed that the new tests reach the named lines.

## Search words

security-checker scheduler RateLimiter acquire rpm events popleft expired 60 seconds untested branch

## The full patch

`````diff
diff --git a/tests/unit/test_rate_limiter_expired_events.py b/tests/unit/test_rate_limiter_expired_events.py
new file mode 100644
index 0000000..009b4b8
--- /dev/null
+++ b/tests/unit/test_rate_limiter_expired_events.py
@@ -0,0 +1,21 @@
+"""RateLimiter.acquire: 60 秒より古い送信記録は捨て、待たずに枠を渡すこと."""
+
+from __future__ import annotations
+
+import time
+
+from security_checker.review.scheduler import RateLimiter
+
+
+async def _no_sleep(seconds: float) -> None:
+    raise AssertionError(f"acquire は待たないはずなのに {seconds} 秒待とうとした")
+
+
+async def test_event_older_than_a_minute_is_dropped_and_the_slot_is_free() -> None:
+    limiter = RateLimiter(rpm=1)
+    limiter._events.append(time.monotonic() - 61.0)
+
+    await limiter.acquire(sleep=_no_sleep)
+
+    assert len(limiter._events) == 1
+    assert time.monotonic() - limiter._events[0] < 5.0
`````

[Back to the shelf](README.md)
