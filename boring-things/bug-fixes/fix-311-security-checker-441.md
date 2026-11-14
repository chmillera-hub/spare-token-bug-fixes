# Fix 311: security-checker: an ignore annotation with empty brackets suppresses every rule on the line

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(policy): ignore 注釈の角括弧が空 (ignore[]) だと、その行の全ルールを抑制する
- Bug report: number 441 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/441))
- Project license: MIT
- Language: Python
- Test included: yes
- Patch file: [fixes/311-security-checker-441.patch](fixes/311-security-checker-441.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/311-security-checker-441.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-311-security-checker-441.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-311-security-checker-441.html

## The bug

parse_annotation in src/security_checker/policy/ignore.py turns empty brackets into the wildcard. A half-written annotation such as ignore[] silently suppresses every detection on the line (secrets included).

## The fix

Empty brackets now suppress nothing. apply_suppressions adds a warning that tells the writer to use ignore[*] for every rule. ignore[*] works as before. The patch updates one line of the existing test for parse_annotation and adds two sentences to docs/configuration.md and adds a new file tests/unit/test_ignore_annotation_empty_brackets.py.

## Files changed

- docs/configuration.md
- src/security_checker/policy/ignore.py
- src/security_checker/policy/suppress.py
- tests/unit/test_ignore_annotation_empty_brackets.py
- tests/unit/test_suppression.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 311-security-checker-441.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 441.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The chatbot did not run the project's tests so nobody has confirmed that the new test passes or that every existing test still passes. The wording of the warning and of the two sentences in the docs is the chatbot's own.

## Search words

security-checker policy ignore annotation ignore[] empty brackets wildcard suppress all rules warning ignore[*]

## The full patch

`````diff
diff --git a/docs/configuration.md b/docs/configuration.md
index d39729b..233a6c2 100644
--- a/docs/configuration.md
+++ b/docs/configuration.md
@@ -172,5 +172,8 @@ subprocess.run(cmd, shell=True)  # security-checker: ignore[python.lang.security
 subprocess.run(cmd, shell=True)
 ```
 
+角括弧を空にした `ignore[]` は何も抑制せず、警告を出します。その行のすべてのルールを抑制するときは
+`ignore[*]` と書きます。
+
 信用できない検査対象 (`SECURITY_CHECKER_UNTRUSTED_TARGET=1`) では、検査対象の中の ignore ファイルと
 注釈を読みません。PR 側が自分の指摘を自分で消せてしまうためです。
diff --git a/src/security_checker/policy/ignore.py b/src/security_checker/policy/ignore.py
index 07632fb..b17bdfe 100644
--- a/src/security_checker/policy/ignore.py
+++ b/src/security_checker/policy/ignore.py
@@ -134,7 +134,8 @@ def parse_annotation(line: str) -> Annotation | None:
     reason = match.group("reason")
     if reason is not None:
         reason = _COMMENT_TAIL_RE.sub("", reason).strip() or None
-    return Annotation(rules=rules or ("*",), reason=reason)
+    # 空の角括弧は全ルールの抑制にしない (#441). 全ルールは ignore[*] と明示する
+    return Annotation(rules=rules, reason=reason)
 
 
 class AnnotationReader:
@@ -172,8 +173,9 @@ class AnnotationReader:
                 if number != location.start_line and not is_annotation_only(line):
                     continue
                 annotation = parse_annotation(line)
-                if annotation is not None and any(
-                    rule_matches(rule, candidate) for rule in annotation.rules
+                if annotation is not None and (
+                    not annotation.rules
+                    or any(rule_matches(rule, candidate) for rule in annotation.rules)
                 ):
                     return annotation
         return None
diff --git a/src/security_checker/policy/suppress.py b/src/security_checker/policy/suppress.py
index a4c7f6c..ce40f4d 100644
--- a/src/security_checker/policy/suppress.py
+++ b/src/security_checker/policy/suppress.py
@@ -67,6 +67,12 @@ def apply_suppressions(
     warnings: list[str] = []
     for candidate in candidates:
         annotation = rules.annotations.find(candidate) if rules.annotations else None
+        if annotation is not None and not annotation.rules:
+            warnings.append(
+                f"{candidate.where}: ignore[] にルール ID が無いため抑制していません。"
+                "全ルールを抑制するときは ignore[*] と書いてください"
+            )
+            annotation = None
         if annotation is not None:
             if annotation.reason is None:
                 warnings.append(
diff --git a/tests/unit/test_ignore_annotation_empty_brackets.py b/tests/unit/test_ignore_annotation_empty_brackets.py
new file mode 100644
index 0000000..9833348
--- /dev/null
+++ b/tests/unit/test_ignore_annotation_empty_brackets.py
@@ -0,0 +1,35 @@
+"""ignore[]: 空の角括弧は抑制せずに警告し、ignore[*] は従来どおり全ルールを抑制すること (#441)."""
+
+from __future__ import annotations
+
+from pathlib import Path
+
+from security_checker.config.schema import Config
+from security_checker.models.candidate import Location
+from security_checker.policy.suppress import apply_suppressions, load_rules
+from tests.factories import make_candidate
+
+
+def _run(tmp_path: Path, line: str) -> tuple[list[object], list[object], list[str]]:
+    (tmp_path / "a.py").write_text(line + "\n", encoding="utf-8")
+    rules = load_rules(Config(), tmp_path)
+    candidate = make_candidate("c1", location=Location(path="a.py", start_line=1, end_line=1))
+    kept, suppressed, warnings = apply_suppressions([candidate], rules)
+    return list(kept), list(suppressed), warnings
+
+
+def test_empty_brackets_do_not_suppress_and_give_a_warning(tmp_path: Path) -> None:
+    kept, suppressed, warnings = _run(tmp_path, "x  # security-checker: ignore[] reason=書きかけ")
+
+    assert len(kept) == 1
+    assert suppressed == []
+    assert len(warnings) == 1
+    assert "ignore[*]" in warnings[0]
+
+
+def test_star_still_suppresses_every_rule(tmp_path: Path) -> None:
+    kept, suppressed, warnings = _run(tmp_path, "x  # security-checker: ignore[*] reason=テスト用")
+
+    assert kept == []
+    assert len(suppressed) == 1
+    assert warnings == []
diff --git a/tests/unit/test_suppression.py b/tests/unit/test_suppression.py
index 7306f82..cd10045 100644
--- a/tests/unit/test_suppression.py
+++ b/tests/unit/test_suppression.py
@@ -115,7 +115,7 @@ def test_ignore_matches_paths_and_rules():
     [
         ("x()  # security-checker: ignore[rules.a] reason=固定値のみ", ("rules.a",), "固定値のみ"),
         ("/* security-checker: ignore[a, b] reason=テスト用 */", ("a", "b"), "テスト用"),
-        ("# Security-Checker: ignore[] ", ("*",), None),
+        ("# Security-Checker: ignore[] ", (), None),
         ("<!-- security-checker: ignore[x] reason=y -->", ("x",), "y"),
     ],
 )
`````

[Back to the shelf](README.md)
