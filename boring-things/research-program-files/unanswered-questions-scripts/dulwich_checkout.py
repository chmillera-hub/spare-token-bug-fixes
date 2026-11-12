# Clones a repository with dulwich and then switches the working files to one chosen older revision (Python forum topic 94414)
# Uses a small repository made on the spot, so no network is needed.
import os, shutil, tempfile, dulwich
from dulwich import porcelain
from dulwich.repo import Repo
print("dulwich", dulwich.__version__)
base = tempfile.mkdtemp(); src = os.path.join(base, "source"); os.mkdir(src)
repo = porcelain.init(src); shas = []
for n in (1, 2, 3):
    with open(os.path.join(src, "file.txt"), "w") as f: f.write(f"version {n}\n")
    if n == 2:
        with open(os.path.join(src, "extra.txt"), "w") as f: f.write("added in commit 2\n")
    if n == 3: os.remove(os.path.join(src, "extra.txt")); porcelain.remove(src, [os.path.join(src, "extra.txt")])
    porcelain.add(src, [os.path.join(src, p) for p in os.listdir(src) if not p.startswith(".")])
    shas.append(porcelain.commit(src, message=f"commit {n}".encode(), author=b"A <a@example.com>", committer=b"A <a@example.com>"))
print("three commits made:", [s.decode()[:8] for s in shas])

def state(path):
    files = sorted(p for p in os.listdir(path) if not p.startswith("."))
    return files, open(os.path.join(path, "file.txt")).read().strip(), Repo(path).head().decode()[:8]

target = os.path.join(base, "clone1")
porcelain.clone(src, target)                                   # an ordinary clone: latest commit
print("after clone:", state(target))
wanted = shas[1]                                               # the middle commit
porcelain.reset(target, "hard", wanted)                        # move the working files and the branch to that commit
print("after porcelain.reset(target, 'hard', sha):", state(target), "| matches commit 2:", state(target)[1] == "version 2" and "extra.txt" in state(target)[0])

target2 = os.path.join(base, "clone2")
porcelain.clone(src, target2)
if hasattr(porcelain, "checkout"):
    try:
        porcelain.checkout(target2, wanted.decode())
        r = Repo(target2)
        print("after porcelain.checkout(target, sha):", state(target2), "| branch file still points at commit 3:", r.refs[b"refs/heads/master"].decode()[:8] == shas[2].decode()[:8])
    except Exception as e: print("porcelain.checkout failed:", type(e).__name__, e)
else:
    print("this dulwich version has no porcelain.checkout")
shutil.rmtree(base)
