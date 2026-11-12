# Cloning with dulwich and then switching to one chosen older revision

## Link to the original question

https://discuss.python.org/t/94414

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 with the Python library dulwich version 1.2.21 on a small repository made on the spot and no other person has rerun the test yet which means the page is unconfirmed. The test used a local repository and not a GitHub address.

## The question

On 4 June 2025 somebody asked on the Python help forum how to fetch a repository with the pure-Python git library dulwich and then check out one specific revision.
The asker knew that porcelain.clone with refspecs=None brings the latest commit and could not work out the checkout step.
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

The test repository had three commits. Commit 2 holds "version 2" in one file and has an extra file that commit 3 removes again.

- After porcelain.clone the working files showed commit 3 (one file with "version 3").
- After porcelain.reset(target, "hard", sha_of_commit_2) the working files showed exactly commit 2 (two files with "version 2") and the branch pointed at commit 2.
- After porcelain.checkout(target, sha_of_commit_2) in a second clone the working files also showed exactly commit 2 while the branch name still pointed at commit 3 (the state that git calls a detached head).

## Best-guess answer

Two lines worked in the test:

porcelain.clone("https://github.com/mystuff/repo", target)
porcelain.reset(target, "hard", "full 40 character hash of the wanted revision")

The reset route moves the branch itself to the wanted revision. The checkout route (porcelain.checkout(target, hash)) leaves the branch alone and only switches the working files which fits a temporary look at an old state.
One practical note from the test machine: a commit signing setting in the global git configuration made dulwich commits fail until the test ran with an empty configuration and reading or switching revisions was not affected.

The test file named dulwich_checkout.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
