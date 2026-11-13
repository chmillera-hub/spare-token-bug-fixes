# Fix 368: Arcane: README.md closes a code block one line early and lists JavaScript assets under styles

Status: UNSENT and UNTESTED. Free to take.

- Project: capachow/arcane
- Bug report title: README.md code fence and asset path typos
- Bug report: number 51 ([open the bug report](https://github.com/capachow/arcane/issues/51))
- Project license: MIT
- Language: Markdown
- Test included: no
- Patch file: [fixes/368-arcane-51.patch](fixes/368-arcane-51.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/368-arcane-51.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-368-arcane-51.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-368-arcane-51.html

## The bug

An extra closing code fence in section 2.2 of README.md leaves the last path() example outside the PHP code block. Section 7 lists the three JavaScript assets under styles/ although the same section says scripts are read from /scripts.

## The fix

The extra closing fence is gone so both path() examples sit inside one PHP code block. The three JavaScript assets are now listed under scripts/.

## Files changed

- README.md

## How to use the fix

1. Get a copy of the project capachow/arcane.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 368-arcane-51.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 51.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-12 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-12 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The fix covers the first two of the three points in the bug report. The third point (whether the locale en+us gives the address /us/about or /en/about) is left open because the report does not say which of the two is right. No test was added because the change is in a documentation file.

## Search words

arcane README.md code fence path example styles scripts default.js pages blog assets

## The full patch

`````diff
diff --git a/README.md b/README.md
index 00099ef..83a59d1 100644
--- a/README.md
+++ b/README.md
@@ -106,7 +106,6 @@ Arcane keeps things minimal. You can build simple to complex applications using
 ``` php
 <?= path('/about/'); # normalized to /about ?>
 <?= path('/shop/cart'); # /us/shop/cart (if active locale) ?>
-```
 <?= path(['IMAGES', 'logo.svg']); # /images/logo.svg (no matter the URL) ?>
 ```
 
@@ -340,9 +339,9 @@ When a layout is active, Arcane scans your `/styles` and `/scripts` directories.
 
 For a user visiting `/blog/post` using the `default` layout, Arcane looks for and auto-injects:
 
-  1. **Layout Assets**: `styles/default.css` & `styles/default.js`
-  2. **Section Assets**: `styles/pages/blog.css` & `styles/pages/blog.js`
-  3. **Page Assets**: `styles/pages/blog/post.css` & `styles/pages/blog/post.js`
+  1. **Layout Assets**: `styles/default.css` & `scripts/default.js`
+  2. **Section Assets**: `styles/pages/blog.css` & `scripts/pages/blog.js`
+  3. **Page Assets**: `styles/pages/blog/post.css` & `scripts/pages/blog/post.js`
 
 *The Benefit*: You can create `styles/pages/blog.css` and it will automatically apply to every blog post, but nowhere else on the site. No manual `<link />` or `<script>` tags required. All assets are cache-busted automatically via `?m=` timestamp.
`````

[Back to the shelf](README.md)
