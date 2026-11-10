# Fix 334: security-checker: the action downloads Linux scanner binaries on macOS and Windows runners and fails later

Status: UNSENT and UNTESTED. Free to take.

- Project: Sh1n1230/security-checker
- Bug report title: fix(action): Linux 以外のランナーで action を使うと、スキャナのインストールが分かりにくい形で失敗する
- Bug report: number 648 ([open the bug report](https://github.com/Sh1n1230/security-checker/issues/648))
- Project license: MIT
- Language: Python
- Test included: no
- Patch file: [fixes/334-security-checker-648.patch](fixes/334-security-checker-648.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/fixes/334-security-checker-648.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/fix-334-security-checker-648.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-334-security-checker-648.html

## The bug

scripts/install-scanners.sh handles only Linux binaries and checks only the CPU type. On a macos-latest runner the script downloads the Linux arm64 binaries and the checksums match and the scanners then fail with exec format error. Neither action.yml nor the docs say that the action needs a Linux runner.

## The fix

install-scanners.sh now stops near the top with an ::error:: line when uname -s is not Linux. The description in action.yml and a new sentence at the top of docs/github-actions.md say that the action needs a Linux runner.

## Files changed

- action.yml
- docs/github-actions.md
- scripts/install-scanners.sh

## How to use the fix

1. Get a copy of the project Sh1n1230/security-checker.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 334-security-checker-648.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 648.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- No test was added because the change is a guard in a shell script plus two lines of text. The chatbot checked the script with bash -n and did not run the script. Nobody has run the action with the change.

## Search words

security-checker action install-scanners.sh uname -s Linux only macos windows runner exec format error action.yml

## The full patch

`````diff
diff --git a/action.yml b/action.yml
index a2e1123..b7462d4 100644
--- a/action.yml
+++ b/action.yml
@@ -19,7 +19,7 @@
 # 設計書 §21.1 は Docker コンテナアクションを最終形としているが、GHCR へのイメージ公開 (P6) までは
 # composite で配る。composite なら Code Scanning へのアップロードに公式の upload-sarif を使える。
 name: security-checker
-description: スキャナの検出を LLM でレビューし、PR コメントと SARIF (Code Scanning) で報告する
+description: スキャナの検出を LLM でレビューし、PR コメントと SARIF (Code Scanning) で報告する (Linux ランナー専用)
 author: Sh1n1230
 branding:
   icon: shield
diff --git a/docs/github-actions.md b/docs/github-actions.md
index 7250be2..4151e5e 100644
--- a/docs/github-actions.md
+++ b/docs/github-actions.md
@@ -2,6 +2,9 @@
 
 security-checker を PR ごとに動かし、結果を 3 か所に出す方法です。
 
+この action は Linux のランナー (`ubuntu-latest` など) 専用です。スキャナのバイナリが Linux 用しか無いため、
+macOS・Windows のランナーではスキャナのインストールの段階でエラーにして止めます。
+
 | 出し先 | 中身 | 役割 |
 |---|---|---|
 | **status check** (ジョブの成否) | exit code | 「ツールが壊れたか」「ポリシー違反があるか」 |
diff --git a/scripts/install-scanners.sh b/scripts/install-scanners.sh
index db636d0..21cf239 100755
--- a/scripts/install-scanners.sh
+++ b/scripts/install-scanners.sh
@@ -19,6 +19,12 @@ script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
 # shellcheck source=scripts/scanner-versions.sh
 source "$script_dir/scanner-versions.sh"
 
+# Linux 用のバイナリしか扱わない。ほかの OS では、取得した後に exec format error で失敗する前に止める (#648)
+if [[ "$(uname -s)" != "Linux" ]]; then
+  echo "::error::install-scanners.sh は Linux のランナー専用です (この環境: $(uname -s))" >&2
+  exit 1
+fi
+
 if [[ $# -ne 1 ]]; then
   echo "使い方: $0 <インストール先ディレクトリ>" >&2
   exit 2
`````

[Back to the shelf](README.md)
