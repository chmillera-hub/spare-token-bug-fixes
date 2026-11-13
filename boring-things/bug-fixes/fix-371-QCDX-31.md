# Fix 371: QCDX: eight misspellings and one wrong path in the README and the docs and the changelog

Status: UNSENT and UNTESTED. Free to take.

- Project: cooldood155/QCDX
- Bug report title: [Bug]: Typos and wrong paths in the docs
- Bug report: number 31 ([open the bug report](https://github.com/cooldood155/QCDX/issues/31))
- Project license: MIT
- Language: Markdown
- Test included: yes
- Patch file: [fixes/371-QCDX-31.patch](fixes/371-QCDX-31.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/371-QCDX-31.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-371-QCDX-31.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-371-QCDX-31.html

## The bug

README.md says writting. docs/PLATFORMS.md says corrosponds and names the path scripts/helpers/releases/release/release.conf. docs/REQUIREMENTS.md says compiler.cpstd and ompmiler.cstd and conan profile detec and intalling and fom Xcode. CHANGELOG.md says wehn.

## The fix

Each of the nine spots now has the correct spelling and the path reads scripts/helpers/release/release.conf as the bug report asks. A new test file fails when one of the nine old spellings comes back.

## Files changed

- CHANGELOG.md
- README.md
- docs/PLATFORMS.md
- docs/REQUIREMENTS.md
- tests/test_docs_spelling.py

## How to use the fix

1. Get a copy of the project cooldood155/QCDX.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 371-QCDX-31.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 31.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-12 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-12 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The corrected path is the place of the file inside a generated project and the same file sits under template/ in this repository. The fix leaves four points of the bug report open because each needs wording from the maintainers: the sentence that starts Every single the compiled code in README.md and the heading Cross Targets above a table of sanitizers in docs/PLATFORMS.md and the sentence Setting CC to a Homebrew causes in docs/REQUIREMENTS.md and the words of of the table which the chatbot could not find in the newest files. The report asks for a spell check that catches the next misspellings and the new test only guards the nine fixed spots. The chatbot checked with a small separate script that the nine old spellings are gone after the patch and did not run the tests of the project.

## Search words

QCDX docs README PLATFORMS REQUIREMENTS CHANGELOG typos writting corrosponds cpstd ompmiler detec intalling release.conf path

## The full patch

`````diff
diff --git a/CHANGELOG.md b/CHANGELOG.md
index 19f2222..537a3b7 100644
--- a/CHANGELOG.md
+++ b/CHANGELOG.md
@@ -42,7 +42,7 @@ and/or fixes that directly impact users and is not logged in this document.
 - `pk dep rm` and `pk dep lock --clean`: pruning `conan.lock` only looked at
   one profile (`native` by default). This caused every package not for the
   platform running the command to be dropped (gtk, glib, wayland, etc. for
-  Linux, dropped wehn `pd dep rm` ran from a Windows machine). The lock then
+  Linux, dropped when `pd dep rm` ran from a Windows machine). The lock then
   failed on those platforms. Pruning now checks every profile in `profiles/`,
   keeps an entry if any of them uses it, and drops nothing if one of their
   graphs can't be read. With more than one `--profile`, `pk dep lock --clean`
diff --git a/README.md b/README.md
index 9f681a4..c2b7328 100644
--- a/README.md
+++ b/README.md
@@ -10,7 +10,7 @@
 A template for C and C++ projects built on **projectkit**, a set of CMake
 modules and scripts under `cmake/projectkit/`. A fresh copy already contains a
 working library, application, test and build-time tool, so it configures,
-builds, tests, installs and packages before you start writting code.
+builds, tests, installs and packages before you start writing code.
 
 - **CMake 3.30+, Ninja and Conan 2**, with presets for native builds, host
   tools and cross builds.
diff --git a/docs/PLATFORMS.md b/docs/PLATFORMS.md
index 7ee9e2d..b3b82ac 100644
--- a/docs/PLATFORMS.md
+++ b/docs/PLATFORMS.md
@@ -22,8 +22,8 @@ Tools needed on the **development machine** are listed within the
 | Windows       | `x86_64`  | `windows-ucrt64`, `windows-clang64`   | `cross-x86_64-mingw-w64`       | yes (`windows-ucrt64`)       |
 | Windows       | `arm64`   | `windows-clangarm64`                  | `cross-aarch64-mingw-llvm-w64` | yes (`windows-clangarm64`)   |
 
-"Released by default" corrosponds to the variable `PK_RELEASE_TARGETS` within
-`scripts/helpers/releases/release/release.conf`
+"Released by default" corresponds to the variable `PK_RELEASE_TARGETS` within
+`scripts/helpers/release/release.conf`
 
 ## Native Targets
 
diff --git a/docs/REQUIREMENTS.md b/docs/REQUIREMENTS.md
index 070d33f..56af20d 100644
--- a/docs/REQUIREMENTS.md
+++ b/docs/REQUIREMENTS.md
@@ -85,7 +85,7 @@ Compilers to oldest supported Conan version (the table above) were found by
 checking the last patch release of every Conan 2.x minor line (e.g., the 2.29
 lines 2.29.1 patch).
 
-`conan profile detec --force` ran after intalling Conan will generate a default
+`conan profile detect --force` ran after installing Conan will generate a default
 Conan profile on the system, representing the systems environment details. This
 profile serves as a fallback in-case the project's `profiles/native` profile
 cannot be found.
@@ -93,7 +93,7 @@ cannot be found.
 ## Compilers
 
 Projects build as C++23 by default (`pk_project_setup`). The native profile
-sets `compiler.cpstd=23` and `compiler.cstd=23`, and Conan's profile check
+sets `compiler.cppstd=23` and `compiler.cstd=23`, and Conan's profile check
 only accepts compilers that can provide both. That Conan profile check is what
 sets the floor for toolchains below:
 
@@ -104,7 +104,7 @@ sets the floor for toolchains below:
 | AppleClang | 15 | 21 | `cppstd=23` from AppleClang 13; 15 is the oldest any QCDX doc lists |
 | MSVC | not supported | - | Conan accepts `cstd` 11 and 17 only for MSVC; no verify target uses it |
 
-GCC 13 still works through the profiles that leave out `ompmiler.cstd`:
+GCC 13 still works through the profiles that leave out `compiler.cstd`:
 
 - Linux cross profiles
 - `x86_64-mingw-w64` (Ubuntu 24.04's cross GCC is 13)
@@ -184,7 +184,7 @@ brew install cmake ninja pipx
 pipx install "conan>=2.4,<3"
 ```
 
-AppleClang comes fom Xcode or the Command Line Tools. If `CC` is unset, the
+AppleClang comes from Xcode or the Command Line Tools. If `CC` is unset, the
 native profile detects AppleClang. Setting `CC` to a Homebrew causes `clang` to
 switch the profiles to `compiler=clang`, which `macos-*` targets don't expect
 to get.
diff --git a/tests/test_docs_spelling.py b/tests/test_docs_spelling.py
new file mode 100644
index 0000000..0d29f50
--- /dev/null
+++ b/tests/test_docs_spelling.py
@@ -0,0 +1,32 @@
+"""Misspellings that were once in the docs stay out."""
+
+import pytest
+
+from conftest import ROOT
+
+DOCS = sorted([
+    ROOT / "README.md",
+    ROOT / "CHANGELOG.md",
+    *(ROOT / "docs").glob("*.md"),
+])
+MISSPELLINGS = [
+    "writting",
+    "corrosponds",
+    "scripts/helpers/releases/",
+    "compiler.cpstd",
+    "ompmiler.cstd",
+    "profile detec ",
+    "intalling",
+    " fom ",
+    " wehn ",
+]
+
+
+def name(doc):
+    return doc.relative_to(ROOT).as_posix()
+
+
+@pytest.mark.parametrize("doc", DOCS, ids=name)
+def test_known_misspellings_stay_out(doc):
+    text = doc.read_text(encoding="utf-8")
+    assert not [word for word in MISSPELLINGS if word in text]
`````

[Back to the shelf](README.md)
