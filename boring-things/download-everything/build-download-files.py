# Rebuilds the download helper files in this folder.
# Run from the top folder of the repository:  python3 boring-things/download-everything/build-download-files.py
# The script reads the list of tracked files from git and writes four files next to this script:
#   file-list.json  file-list.txt  research-pages-all-in-one.txt  llms.txt
# and one more file named everything-in-one.md which joins nearly all the written text of the repository for upload to a chatbot.
import subprocess, json, os, datetime, urllib.parse

OWNER_REPO = "chmillera-hub/spare-token-bug-fixes"
RAW = "https://raw.githubusercontent.com/" + OWNER_REPO + "/main/"
BLOB = "https://github.com/" + OWNER_REPO + "/blob/main/"
SITE = "https://chmillera-hub.github.io/spare-token-bug-fixes/"
ZIP = "https://github.com/" + OWNER_REPO + "/archive/refs/heads/main.zip"
HERE = "boring-things/download-everything/"
RESEARCH = "1-research-click-here-first/"
GENERATED = {HERE + n for n in ("file-list.json", "file-list.txt", "research-pages-all-in-one.txt", "llms.txt", "everything-in-one.md")}
SMALL_TEXT_LIMIT = 100_000  # bytes; larger .txt files are data files and stay out of the all-in-one file

def q(p): return urllib.parse.quote(p)

def title_of(path):
    if path.endswith(".md"):
        with open(path, encoding="utf-8", errors="ignore") as f:
            for line in f:
                if line.startswith("# "): return line[2:].strip()
    return os.path.basename(path)

paths = sorted(p for p in subprocess.run(["git", "ls-files"], capture_output=True, text=True).stdout.split("\n") if p and p not in GENERATED)
today = datetime.date.today().isoformat()
files = []
for p in paths:
    ext = p.rsplit(".", 1)[-1].lower() if "." in os.path.basename(p) else ""
    files.append({"path": p, "title": title_of(p), "bytes": os.path.getsize(p), "type": ext,
                  "area": "research" if p.startswith(RESEARCH) else ("boring-things" if p.startswith("boring-things/") else "top"),
                  "raw_url": RAW + q(p), "page_url": BLOB + q(p)})

json.dump({"repository": "https://github.com/" + OWNER_REPO, "website": SITE, "zip_of_everything": ZIP,
           "raw_url_pattern": RAW + "<path>", "built_on": today, "file_count": len(files),
           "total_bytes": sum(f["bytes"] for f in files), "files": files},
          open(HERE + "file-list.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)

with open(HERE + "file-list.txt", "w", encoding="utf-8") as f:
    for x in files: f.write(x["raw_url"] + "\n")

# One text file that holds every reading page in the research folder
picked = [x for x in files if x["area"] == "research" and (x["type"] == "md" or (x["type"] == "txt" and x["bytes"] <= SMALL_TEXT_LIMIT))]
left_out = [x for x in files if x["area"] == "research" and x not in picked]
with open(HERE + "research-pages-all-in-one.txt", "w", encoding="utf-8") as f:
    f.write("EVERY READING PAGE IN THE RESEARCH FOLDER IN ONE FILE\n")
    f.write("Built on " + today + " by the script named build-download-files.py. An AI chatbot (Claude) wrote the pages and no other person has rechecked the pages.\n")
    f.write("This file holds " + str(len(picked)) + " pages. Each page starts with a line of equals signs and then the path of the page and the direct download address of the page.\n")
    f.write("Large data files and program files are left out of this file and are listed at the end with a direct download address for each.\n\n")
    for x in picked:
        f.write("=" * 80 + "\nFILE: " + x["path"] + "\nDOWNLOAD: " + x["raw_url"] + "\n" + "=" * 80 + "\n\n")
        f.write(open(x["path"], encoding="utf-8", errors="ignore").read().rstrip() + "\n\n")
    f.write("=" * 80 + "\nFILES LEFT OUT OF THIS FILE (data files and program files and pictures)\n" + "=" * 80 + "\n\n")
    for x in left_out: f.write(x["path"] + " (" + str(x["bytes"]) + " bytes)\n" + x["raw_url"] + "\n\n")

# llms.txt : a short map for AI agents
with open(HERE + "llms.txt", "w", encoding="utf-8") as f:
    f.write("# spare-token-bug-fixes\n\n")
    f.write("> Research pages and reflections and free bug fixes that an AI chatbot (Claude) wrote for the repository author. Every file is public and may be downloaded for research. The repository author says anyone may use and copy and share the writing without asking. No other person has rechecked the pages.\n\n")
    f.write("## Download everything\n\n")
    f.write("- [Zip of the whole repository](" + ZIP + "): one download that holds every file\n")
    f.write("- [Every reading page in one text file](" + RAW + q(HERE + "research-pages-all-in-one.txt") + "): " + str(len(picked)) + " pages joined into one plain text file\n")
    f.write("- [List of every file as JSON](" + RAW + q(HERE + "file-list.json") + "): path and title and size and direct download address for " + str(len(files)) + " files\n")
    f.write("- [List of direct download addresses](" + RAW + q(HERE + "file-list.txt") + "): one address per line\n")
    f.write("- Any single file: " + RAW + "<path of the file>\n\n")
    f.write("## Research pages\n\n")
    for x in files:
        if x["area"] == "research" and x["type"] == "md":
            f.write("- [" + x["title"] + "](" + x["raw_url"] + ")\n")
    f.write("\n## Other files\n\n- [Bug fix shelf map for AI agents](" + RAW + "boring-things/bug-fixes/llms.txt)\n- [Bug fix shelf list as JSON](" + RAW + "boring-things/bug-fixes/index.json)\n")

print("files listed", len(files), "| pages in all-in-one", len(picked), "| left out", len(left_out))

# everything-in-one.md : one large Markdown file with nearly all the written text of the repository
BIBLE = RESEARCH + "bible-quote-builder/bible-source/"
DUPLICATE = RESEARCH + "emotion-stories/all-stories-in-one.md"
def in_big(x):
    p, t = x["path"], x["type"]
    if p == DUPLICATE or p.startswith(BIBLE): return False
    if x["area"] == "top": return t == "md"
    if x["area"] == "research": return t in ("md", "txt", "lean", "py")
    return t == "md"
order = {"top": 0, "research": 1, "boring-things": 2}
big = sorted((x for x in files if in_big(x)), key=lambda x: (order[x["area"]], x["path"]))
skipped = [x for x in files if not in_big(x)]
with open(HERE + "everything-in-one.md", "w", encoding="utf-8") as f:
    f.write("# Everything in one file\n\n")
    f.write("This file joins " + str(len(big)) + " text files from the repository at https://github.com/" + OWNER_REPO + " into one Markdown file so that a person can upload a single file to a chatbot and ask questions about any topic in the repository. The script named build-download-files.py built this file on " + today + ". An AI chatbot (Claude) wrote most of the pages and no other person has rechecked the pages.\n\n")
    f.write("Each joined file starts with a heading line that begins with the words FILE and then gives the path of the file. A reader or a chatbot can search this file for the path of a file to jump to that file.\n\n")
    f.write("This file holds the reading pages and the plain text data files of the research folder and the Lean proof files and the notes about each bug fix. This file leaves out videos and pictures and programs and patch files and the full text of the Bible (a public text that is easy to find elsewhere) and one page that only repeats the emotion stories. The end of this file lists every file that was left out with a direct download address.\n\n")
    f.write("## List of the joined files\n\n")
    for x in big: f.write("- " + x["path"] + "\n")
    for x in big:
        body = open(x["path"], encoding="utf-8", errors="ignore").read().rstrip()
        f.write("\n\n---\n\n# FILE: " + x["path"] + "\n\nDownload address: " + x["raw_url"] + "\n\n")
        if x["type"] == "md": f.write(body + "\n")
        else: f.write("````" + ("text" if x["type"] == "txt" else x["type"]) + "\n" + body + "\n````\n")
    f.write("\n\n---\n\n# FILES LEFT OUT OF THIS FILE\n\n")
    for x in skipped: f.write("- " + x["path"] + " (" + str(x["bytes"]) + " bytes) " + x["raw_url"] + "\n")
print("everything-in-one.md holds", len(big), "files |", os.path.getsize(HERE + "everything-in-one.md"), "bytes")
for n in sorted(GENERATED): print(n, os.path.getsize(n))
