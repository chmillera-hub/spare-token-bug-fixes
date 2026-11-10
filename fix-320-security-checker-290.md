# Fix 320: security-checker: internal Japanese docstrings are sent to the model inside the answer schema

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(review): 応答スキーマの description に pydantic の docstring（日本語の内部メモ）が入り、そのまま LLM に送られる
- Bug report: number 290 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/290))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/320-security-checker-290.patch](fixes/320-security-checker-290.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/320-security-checker-290.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-320-security-checker-290.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-320-security-checker-290.html

## The bug

_harden in src/security_checker/review/structured.py removes title from the schema and keeps description. pydantic fills description from the docstrings of the classes so internal notes in Japanese go into the prompt and into the schema sent to the provider.

## The fix

_harden now also removes every description that is a text value. A field that is itself named description would stay because its value is a schema object. A new file tests/unit/test_verdict_schema_has_no_descriptions.py walks the schema and expects no description text.

## Files changed

- src/security_checker/review/structured.py
- tests/unit/test_verdict_schema_has_no_descriptions.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 320-security-checker-290.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 290.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The schema is pasted into the prompt so this patch changes the prompt text. The bug report offers an optional second step (English descriptions written with Field). This patch does not add that step. An existing test that compares the full schema may need an update.

## Search words

security-checker review structured verdict_schema _harden description docstring pydantic schema prompt json_schema

## The full patch

`````diff
diff --git a/src/security_checker/review/structured.py b/src/security_checker/review/structured.py
index eb316a0..1947bdd 100644
--- a/src/security_checker/review/structured.py
+++ b/src/security_checker/review/structured.py
@@ -54,6 +54,9 @@ def _harden(node: Any) -> Any:
             # 求める実装があるため、省略可能な項目も null 許容にしたうえで必須にする。
             hardened["required"] = sorted(hardened["properties"])
         hardened.pop("title", None)
+        # docstring 由来の description (内部メモ) をモデルに送らない (#290)
+        if isinstance(hardened.get("description"), str):
+            del hardened["description"]
         return hardened
     if isinstance(node, list):
         return [_harden(item) for item in node]
diff --git a/tests/unit/test_verdict_schema_has_no_descriptions.py b/tests/unit/test_verdict_schema_has_no_descriptions.py
new file mode 100644
index 0000000..b54a653
--- /dev/null
+++ b/tests/unit/test_verdict_schema_has_no_descriptions.py
@@ -0,0 +1,31 @@
+"""verdict_schema: docstring 由来の description をスキーマに残さないこと (#290)."""
+
+from __future__ import annotations
+
+from collections.abc import Iterator
+from typing import Any
+
+from security_checker.review.structured import verdict_schema
+
+
+def _descriptions(node: Any) -> Iterator[str]:
+    if isinstance(node, dict):
+        for key, value in node.items():
+            if key == "description" and isinstance(value, str):
+                yield value
+            else:
+                yield from _descriptions(value)
+    elif isinstance(node, list):
+        for item in node:
+            yield from _descriptions(item)
+
+
+def test_schema_sent_to_the_model_holds_no_description_text() -> None:
+    assert list(_descriptions(verdict_schema())) == []
+
+
+def test_schema_still_lists_the_judgement_fields() -> None:
+    """対になるケース. 項目そのものは消さない."""
+    properties = verdict_schema()["properties"]
+
+    assert {"vulnerable", "severity", "confidence", "reasoning"} <= set(properties)
`````

[Back to the shelf](README.md)
