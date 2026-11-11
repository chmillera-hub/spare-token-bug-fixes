# Fix 297: btclib-wallet: the key_wallet docstring quotes a sentence that the bms docstring of btclib no longer holds

Status: UNSENT and UNTESTED. Free to take.

- Project: btclib-org/btclib-wallet
- Bug report title: key_wallet's docstring quotes a bms sentence btclib removed
- Bug report: number 755 ([open the bug report](https://github.com/btclib-org/btclib-wallet/issues/755))
- Project license: MIT
- Language: Python
- Test included: no
- Patch file: [fixes/297-btclib-wallet-755.patch](fixes/297-btclib-wallet-755.patch)
- Direct download address for programs and chatbots: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/bug-fixes/fixes/297-btclib-wallet-755.patch
- Same page on GitHub: https://github.com/chmillera-hub/spare-token-bug-fixes/blob/main/boring-things/bug-fixes/fix-297-btclib-wallet-755.md
- Same page as a plain website page: https://chmillera-hub.github.io/game1/spare-token-bug-fixes/fix-297-btclib-wallet-755.html

## The bug

The module docstring of src/btclib_wallet/wallet/key_wallet.py says that btclib.ecc.bms states a sentence about a wallet infrastructure in its own docstring. The btclib developers removed that sentence from bms so the quote points at text that does not exist.

## The fix

The first paragraph of the docstring now states the purpose of the module in its own words: signing a message for an address needs the private key behind the address and the bms module of btclib has no way to find the key. The quote and the claim about the bms docstring are gone. Only docstring text changed.

## Files changed

- src/btclib_wallet/wallet/key_wallet.py

## How to use the fix

1. Get a copy of the project btclib-org/btclib-wallet.
2. Download the patch file from the direct download address shown near the top of this page.
3. Run: git apply 297-btclib-wallet-755.patch
4. Run the project's own tests.
5. Read the project's contribution rules and then open a pull request that mentions bug report 755.

## Warnings

- An AI chatbot (Claude) wrote this fix. No human has reviewed the fix.
- Nobody has run the fix against the project's own test suite.
- The chatbot read the full bug report text and could not read the comments under the bug report.
- Nobody has checked whether someone else already sent a fix for the same bug.
- The fix was written against the project's code as of 2026-11-10 and may no longer apply cleanly.
- The patch applied cleanly to the project's newest code on 2026-11-10 (checked with git apply --check).
- Nobody has sent the fix to the project. Anyone is free to test the fix and send the fix.
- The bug report allows two ways (own words or a quote from the commit that last held the sentence). The chatbot chose own words because that way needs no reference to an old commit. The new wording keeps the claim of the old text that bms cannot find the key for an address. The chatbot did not read the bms module of btclib to confirm that claim. No test was added because only a docstring changed.

## Search words

btclib-wallet key_wallet docstring bms wallet infrastructure quote removed sentence

## The full patch

`````diff
diff --git a/src/btclib_wallet/wallet/key_wallet.py b/src/btclib_wallet/wallet/key_wallet.py
index 8a1a937..2e4e77f 100644
--- a/src/btclib_wallet/wallet/key_wallet.py
+++ b/src/btclib_wallet/wallet/key_wallet.py
@@ -4,10 +4,9 @@
 
 """The wallets whose output is the hash of one key, and who signs for it.
 
-`btclib.ecc.bms` says it in its own docstring -- "at signing time, a
-wallet infrastructure is required to access the private key corresponding
-to a given address" -- and then has none to reach for. This module is
-that infrastructure, and no more of it than the sentence asks for: a
+Signing a message for an address needs the private key behind that
+address, and btclib's `bms` module has no way to find it. This module is
+the wallet infrastructure that does, and no more of it than that: a
 wallet holds a key source, hands out addresses, remembers what each was
 derived from, and answers which private key signs for one.
 `sign(address, msg)` is what the three together buy, a message signature
`````

[Back to the shelf](README.md)
