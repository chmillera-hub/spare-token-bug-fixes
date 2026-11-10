# Fix 341: security-checker: implicit string concatenation inside list elements looks like a missing comma

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: refactor: 暗黙の文字列連結をリストの要素の中で使っている箇所に括弧を付ける (ISC004)
- Bug report: number 682 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/682))
- Project license: MIT
- Language: Python
- Test included: no
- Patch file: [fixes/341-security-checker-682.patch](fixes/341-security-checker-682.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/341-security-checker-682.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-341-security-checker-682.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-341-security-checker-682.html

## The bug

The ruff rule ISC004 reports list and tuple elements that join two string literals with no parentheses. A reader cannot tell such an element from two elements with a forgotten comma. The bug report counted 9 places and the newest code holds 15 in 6 files under src.

## The fix

Every reported element is now wrapped in parentheses. The chatbot let ruff 0.16.9 apply its own fix for ISC004 and then ran ruff format with the settings of the project. Behaviour is unchanged because the joined strings are the same.

## Files changed

- src/security_checker/eval/runner.py
- src/security_checker/github/comment.py
- src/security_checker/observability/explain.py
- src/security_checker/policy/baseline.py
- src/security_checker/providers/process/runner.py
- src/security_checker/report/markdown.py

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 341-security-checker-682.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 682.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- After the change the chatbot ran ruff with the rule ISC004 and saw no report left under src and ran ruff check and ruff format --check with the settings of the project on the six files and both passed. The chatbot did not run the project's tests. The bug report also suggests adding ISC004 to the ruff settings when possible. This patch does not change the settings. No test was added because behaviour is unchanged.

## Search words

security-checker ruff ISC004 implicit string concatenation collection literal parentheses missing comma refactor

## The full patch

`````diff
diff --git a/src/security_checker/eval/runner.py b/src/security_checker/eval/runner.py
index bd36a9c..8bddd68 100644
--- a/src/security_checker/eval/runner.py
+++ b/src/security_checker/eval/runner.py
@@ -164,24 +164,34 @@ def to_markdown(result: EvalResult) -> str:
         "",
         f"- Reviewer: {', '.join(result.reviewers) or '(なし)'}",
         f"- 集約戦略: {result.aggregation}",
-        f"- ケース数: {metrics.cases} "
-        f"(採点外: エラー {metrics.errors} / 未レビュー {metrics.not_reviewed})",
+        (
+            f"- ケース数: {metrics.cases} "
+            f"(採点外: エラー {metrics.errors} / 未レビュー {metrics.not_reviewed})"
+        ),
         "",
         "## 指標",
         "",
         "| 指標 | 値 | 位置づけ |",
         "|---|---|---|",
-        f"| **Recall (検出率)** | {_pct(metrics.recall)} | "
-        "**主指標**。陽性全体のうち自動で検出した割合。保留は検出に数えない |",
-        f"| 判定した中での Recall | {_pct(metrics.answered_recall)} | "
-        "参考値。保留が増えると上がるので比較に使わない |",
+        (
+            f"| **Recall (検出率)** | {_pct(metrics.recall)} | "
+            "**主指標**。陽性全体のうち自動で検出した割合。保留は検出に数えない |"
+        ),
+        (
+            f"| 判定した中での Recall | {_pct(metrics.answered_recall)} | "
+            "参考値。保留が増えると上がるので比較に使わない |"
+        ),
         f"| Precision | {_pct(metrics.precision)} | 副指標。ノイズの少なさ |",
         f"| F1 | {_pct(metrics.f1)} | 総合 |",
-        f"| **FP 削減率** | {_pct(metrics.fp_reduction)} | "
-        "このツールの価値そのもの。保留した陰性は削減に数えない |",
+        (
+            f"| **FP 削減率** | {_pct(metrics.fp_reduction)} | "
+            "このツールの価値そのもの。保留した陰性は削減に数えない |"
+        ),
         f"| **見逃した真陽性** | {metrics.missed_true_positives} 件 | **0 に近いことが必須条件** |",
-        f"| review_required 率 | {_pct(metrics.review_required_rate)} | "
-        f"高すぎると実用性が下がる (人間に渡した FP {metrics.deferred_negatives} 件) |",
+        (
+            f"| review_required 率 | {_pct(metrics.review_required_rate)} | "
+            f"高すぎると実用性が下がる (人間に渡した FP {metrics.deferred_negatives} 件) |"
+        ),
         f"| Severity MAE | {_num(metrics.severity_mae)} | 重大度判定の質 |",
         f"| CWE 一致率 | {_pct(metrics.cwe_match_rate)} | 分類の質 |",
         f"| コスト | {_usd(metrics)} | 実運用可能性 |",
@@ -191,10 +201,14 @@ def to_markdown(result: EvalResult) -> str:
         "",
         "| | 脆弱と報告 | 誤検知と判断 | 人間に委ねた |",
         "|---|---|---|---|",
-        f"| 正解: 脆弱 | {metrics.true_positives} | **{metrics.false_negatives}** "
-        f"| {metrics.deferred_positives} |",
-        f"| 正解: 問題なし | {metrics.false_positives} | {metrics.true_negatives} "
-        f"| {metrics.deferred_negatives} |",
+        (
+            f"| 正解: 脆弱 | {metrics.true_positives} | **{metrics.false_negatives}** "
+            f"| {metrics.deferred_positives} |"
+        ),
+        (
+            f"| 正解: 問題なし | {metrics.false_positives} | {metrics.true_negatives} "
+            f"| {metrics.deferred_negatives} |"
+        ),
         "",
     ]
 
diff --git a/src/security_checker/github/comment.py b/src/security_checker/github/comment.py
index 274992a..e69954b 100644
--- a/src/security_checker/github/comment.py
+++ b/src/security_checker/github/comment.py
@@ -204,8 +204,10 @@ def _summary_block(finding: Finding) -> list[str]:
         label += " (likely)"
     lines = [
         f"### {mark} {label}{cwe} · {title}",
-        f"{md.code_span(candidate.where)} · confidence **{finding.confidence:.0%}** · "
-        f"agreement **{finding.agreement.value}**",
+        (
+            f"{md.code_span(candidate.where)} · confidence **{finding.confidence:.0%}** · "
+            f"agreement **{finding.agreement.value}**"
+        ),
         "",
     ]
     ok = [v for v in finding.verdicts if v.status.value == "ok" and v.vulnerable]
@@ -264,8 +266,10 @@ def _candidate_table(report: Report) -> list[str]:
 def _footer(report: Report, report_url: str | None) -> str:
     parts = [
         f"security-checker v{report.tool_version}",
-        f"{report.coverage.candidates_total} candidates → "
-        f"{report.coverage.candidates_reviewed} reviewed",
+        (
+            f"{report.coverage.candidates_total} candidates → "
+            f"{report.coverage.candidates_reviewed} reviewed"
+        ),
     ]
     usage = report.usage
     if usage.cost_known and usage.estimated_usd is not None:
diff --git a/src/security_checker/observability/explain.py b/src/security_checker/observability/explain.py
index 939c35d..b5bc667 100644
--- a/src/security_checker/observability/explain.py
+++ b/src/security_checker/observability/explain.py
@@ -100,8 +100,10 @@ def render(result: Explanation) -> str:
     finding = result.finding
     if finding is not None:
         lines += [
-            f"判定: {finding.status.value}  severity {finding.severity.value}  "
-            f"confidence {finding.confidence:.2f}  agreement {finding.agreement.value}",
+            (
+                f"判定: {finding.status.value}  severity {finding.severity.value}  "
+                f"confidence {finding.confidence:.2f}  agreement {finding.agreement.value}"
+            ),
             f"  {finding.summary}",
         ]
         if finding.aggregation is not None:
diff --git a/src/security_checker/policy/baseline.py b/src/security_checker/policy/baseline.py
index 4680006..9141cbf 100644
--- a/src/security_checker/policy/baseline.py
+++ b/src/security_checker/policy/baseline.py
@@ -80,9 +80,11 @@ def load_baseline(path: Path) -> Baseline:
     warnings: tuple[str, ...] = ()
     if version in LEGACY_VERSIONS:
         warnings = (
-            f"{path} は古い形式 (version {version}) です。"
-            "同じ場所で値を差し替えた秘密も抑制されます。"
-            "`security-checker baseline update` で更新してください",
+            (
+                f"{path} は古い形式 (version {version}) です。"
+                "同じ場所で値を差し替えた秘密も抑制されます。"
+                "`security-checker baseline update` で更新してください"
+            ),
         )
     return Baseline(
         ids=frozenset(ids),
diff --git a/src/security_checker/providers/process/runner.py b/src/security_checker/providers/process/runner.py
index 49e2670..0074053 100644
--- a/src/security_checker/providers/process/runner.py
+++ b/src/security_checker/providers/process/runner.py
@@ -199,10 +199,12 @@ class ProcessProvider:
         if not result.created_paths:
             return []
         return [
-            f"{self.name}: Reviewer が隔離ディレクトリに書き込みを行いました "
-            f"({', '.join(result.created_paths)})。"
-            "隔離ディレクトリの外への書き込みは検知できません。"
-            "書き込み能力を無効化するフラグを command に加えてください"
+            (
+                f"{self.name}: Reviewer が隔離ディレクトリに書き込みを行いました "
+                f"({', '.join(result.created_paths)})。"
+                "隔離ディレクトリの外への書き込みは検知できません。"
+                "書き込み能力を無効化するフラグを command に加えてください"
+            )
         ]
 
     def _trace_params(self, result: SandboxResult) -> dict[str, Any]:
diff --git a/src/security_checker/report/markdown.py b/src/security_checker/report/markdown.py
index d78c871..56d5765 100644
--- a/src/security_checker/report/markdown.py
+++ b/src/security_checker/report/markdown.py
@@ -102,8 +102,10 @@ def _summary(report: Report) -> list[str]:
         "| 項目 | 値 |",
         "|---|---|",
         f"| スコア | **{score.value}/100** (rank {score.rank}){partial} |",
-        f"| 候補 | {report.coverage.candidates_total} 件 "
-        f"(レビュー済み {report.coverage.candidates_reviewed} 件) |",
+        (
+            f"| 候補 | {report.coverage.candidates_total} 件 "
+            f"(レビュー済み {report.coverage.candidates_reviewed} 件) |"
+        ),
     ]
     if report.suppression_label:
         lines.append(f"| 抑制 | {report.suppression_label} (レビュー・判定の対象外) |")
@@ -168,8 +170,10 @@ def _findings(report: Report) -> list[str]:
         lines += [f"## {title} ({len(group)} 件)", ""]
         if status is FindingStatus.NOT_REVIEWED:
             lines += [
-                "予算・上限・中断のためレビューされていません。"
-                "「問題なし」ではないことに注意してください。",
+                (
+                    "予算・上限・中断のためレビューされていません。"
+                    "「問題なし」ではないことに注意してください。"
+                ),
                 "",
             ]
             lines += [
@@ -274,8 +278,10 @@ def _footer(report: Report) -> list[str]:
     lines = [
         "---",
         "",
-        f"security-checker v{report.tool_version} / run `{report.run_id}` / "
-        f"target `{report.target.root}` ({report.target.label})",
+        (
+            f"security-checker v{report.tool_version} / run `{report.run_id}` / "
+            f"target `{report.target.root}` ({report.target.label})"
+        ),
     ]
     if report.stopped_reason:
         lines += ["", f"⚠️ 途中で停止しました: {report.stopped_reason}"]
`````

[Back to the shelf](README.md)
