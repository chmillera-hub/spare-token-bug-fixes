# Download everything

An AI chatbot (Claude) wrote this page and built the files in this folder on 14 November 2026. Every file in this repository is public and any person or AI agent may download the files for research.

## The fastest ways to get the files

- **One zip of the whole repository.** This address downloads every file in one zip of about 75 megabytes and the zip always holds the newest version because the hosting service builds the zip at the moment of the download: https://github.com/chmillera-hub/spare-token-bug-fixes/archive/refs/heads/main.zip
- **Every reading page in one text file.** The file named [research-pages-all-in-one.txt](research-pages-all-in-one.txt) joins 156 reading pages from the research folder into one plain text file of about 1.4 megabytes so a person or an AI agent can read the research with a single download: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/boring-things/download-everything/research-pages-all-in-one.txt
- **Any single file.** Put the path of a file after this address to download the plain file with no web page around the file: https://raw.githubusercontent.com/chmillera-hub/spare-token-bug-fixes/main/
- **A copy with the full history.** A person with the program named git can run the command `git clone https://github.com/chmillera-hub/spare-token-bug-fixes.git` which needs no account and no password.

## Lists for programs and AI agents

- [file-list.json](file-list.json) lists every file with the path and the title and the size in bytes and a direct download address so a program can pick files without crawling the website.
- [file-list.txt](file-list.txt) holds one direct download address per line so a download program can fetch every file from the list.
- [llms.txt](llms.txt) is a short map written for AI agents that starts with the download addresses and then links every research page by title.

## What the one text file leaves out

The one text file holds the pages written for reading. The one text file leaves out large data files such as the full Bible text and the full set of owner comments and leaves out program files and pictures because those files would make the one text file too large to read in one pass. The end of the one text file lists every file that was left out with a direct download address for each.

## How fresh the lists are

The zip address and the git command always give the newest files. The four built files in this folder were made on 14 November 2026 and show the repository as of that day. A file added after that day is still public and still downloadable and is missing from the lists until the lists are rebuilt.

## How to rebuild the lists

Run this command from the top folder of the repository: `python3 boring-things/download-everything/build-download-files.py`
