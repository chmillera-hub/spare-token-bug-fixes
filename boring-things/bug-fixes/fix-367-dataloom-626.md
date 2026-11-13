# Fix 367: DataLoom: the Contents list of CONTRIBUTING.md has a misspelled entry and wrong nesting

Status: UNSENT and UNTESTED. Free to take.

- Project: c2siorg/dataloom
- Bug report title: [Bug] CONTRIBUTING.md Contents has a typo and wrong nesting
- Bug report: number 626 ([open the bug report](https://github.com/c2siorg/dataloom/issues/626))
- Project license: Apache-2.0
- Language: Markdown
- Test included: no
- Patch file: [fixes/367-dataloom-626.patch](fixes/367-dataloom-626.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/367-dataloom-626.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-367-dataloom-626.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-367-dataloom-626.html

## The bug

The Contents list of CONTRIBUTING.md spells Playwright as Playright. The list shows Migrations beside Backend Setup although the Migrations heading sits one level under Backend Setup. The top entries are bold inside the link text and no blank line follows the Contents heading which differs from the rest of the file.

## The fix

The entry now reads E2E Tests (Playwright). Migrations is nested under Backend Setup. The bold marks are gone from the top entries and a blank line follows the Contents heading.

## Files changed

- CONTRIBUTING.md

## How to use the fix

1. Get a copy of the project c2siorg/dataloom.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 367-dataloom-626.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 626.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-12 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-12 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- No test was added because the change is in a documentation file. Every link target was left as it was.

## Search words

dataloom CONTRIBUTING.md Contents Playright Playwright Migrations nesting bold table of contents

## The full patch

`````diff
diff --git a/CONTRIBUTING.md b/CONTRIBUTING.md
index 15d218f..3afaafa 100644
--- a/CONTRIBUTING.md
+++ b/CONTRIBUTING.md
@@ -3,23 +3,24 @@
 Thank you for your interest in contributing to DataLoom! This document provides guidelines and instructions for contributing.
 
 ## Contents
-- [**Picking Up Work**](#picking-up-work)
-- [**Getting Started**](#getting-started)
-- [**Development Setup**](#development-setup)
+
+- [Picking Up Work](#picking-up-work)
+- [Getting Started](#getting-started)
+- [Development Setup](#development-setup)
   - [Prerequisites](#prerequisites)
   - [Database Setup](#database-setup)
   - [Backend Setup](#backend-setup)
-  - [Migrations](#migrations)
+    - [Migrations](#migrations)
   - [Frontend Setup](#frontend-setup)
-- [**Development Workflow**](#development-workflow)
+- [Development Workflow](#development-workflow)
   - [Benchmarks](#benchmarks)
-  - [E2E Tests (Playright)](#e2e-tests-playwright)
-- [**Code Style**](#code-style)
+  - [E2E Tests (Playwright)](#e2e-tests-playwright)
+- [Code Style](#code-style)
   - [Frontend](#frontend)
   - [Backend](#backend)
-- [**Reporting Bugs**](#reporting-bugs)
-- [**Requesting Features**](#requesting-features)
-- [**License**](#license)
+- [Reporting Bugs](#reporting-bugs)
+- [Requesting Features](#requesting-features)
+- [License](#license)
 
 ## Picking Up Work
`````

[Back to the shelf](README.md)
