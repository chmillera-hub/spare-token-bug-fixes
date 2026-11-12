# Bible quote builder

This folder holds an experiment where short phrases from the World English Bible are shuffled by programs and an AI model (Claude) then connects the phrases into short replies under rules that the repository owner set one at a time.

Warning about a wording change: the repository owner replaces the name "yahweh" with the word "god" everywhere in the Bible programs and in the newer results as a personal reading choice that helps the repository owner follow the quotes which means the quotes differ from the World English Bible at every place where the World English Bible prints the name and a reader who wants the original wording can open the World English Bible itself.

Warning about changed wording in the joined Bible passages: the passages that the AI model joined by hand for the Claude Bible set and My Personal Bible set and the Jesus Bible set are not exact Bible quotes because the repository owner set rules that allow added words and changed pronouns and replaced names and added punctuation which means a reader who wants the exact wording needs to open the World English Bible itself.

## Start here

- [best-outputs.md](best-outputs.md) holds only the finished paragraphs with no commentary and the file named best-outputs-spaced.txt holds every one of the same paragraphs without italics for copying and puts an invisible blank character on its own line between paragraphs for apps that drop empty lines when text is pasted.
- [rules.md](rules.md) lists all fifty-four rules now in force with the reason for each rule.
- [prompt-for-new-chat.txt](prompt-for-new-chat.txt) is a ready-made prompt that a person can paste into a new chat with an AI model so that the AI model can make outputs from any input sentence.
- The public link to the chat on 11 November 2026 where a new chat used the ready-made prompt to make three outputs about Gen Z and work is https://claude.ai/share/e599b4d3-3058-46f9-b138-9f3dd71d925c and those three outputs are copied in full into the three best-outputs files.
- [corrections.md](corrections.md) lists lines that the AI model wrote and that the repository owner flagged as wrong and shows each line before the fix and after the fix with the reason for the fix which makes the page useful to anyone who wants to teach a chatbot to care for people without hurting people by accident.

## Bible source text

- The folder named [bible-source](bible-source) holds the full World English Bible so that every quote can be copied from the source text and never from the memory of an AI model.
- [bible-source/bible-verses.txt](bible-source/bible-verses.txt) holds 38028 verses with one verse on each line (the verse reference and then a tab and then the verse text) which is the format that a program can search and pick from at random. The file keeps the original wording which means the name "Yahweh" is still printed there.
- [bible-source/bible-verses-for-outputs.txt](bible-source/bible-verses-for-outputs.txt) is the modified copy that the random picker uses for outputs. The repository owner asked on 12 November 2026 for the genealogies and the long lists of names to be removed because a row of names gives almost nothing to build a reply from which means 1765 verses were left out (such as the family lines in Genesis 5 and the first nine chapters of 1 Chronicles and the family lines at the start of Matthew and in Luke 3) and 36263 verses remain. The modified copy is not the World English Bible any more because verses were removed and the complete text stays in bible-verses.txt.
- [bible-source/make-outputs-file.py](bible-source/make-outputs-file.py) is the small program that makes the modified copy and the program lists every section that was left out.
- [bible-source/world-english-bible.pdf](bible-source/world-english-bible.pdf) is the original file that the repository owner supplied on 12 November 2026 and the first page of that file states that the World English Bible is in the public domain.
- [bible-source/make-verses-file.py](bible-source/make-verses-file.py) is the small program that turned the PDF into the verses file.
- The verses file also holds the extra books that the PDF prints between Malachi and Matthew (such as Tobit and Sirach) and the random picker for the Claude Bible set skips those extra books unless the repository owner says otherwise.

## How the experiment developed

- [how-outputs-evolved.md](how-outputs-evolved.md) shows one sample output from each stage so that a visitor can watch the outputs change from noise into readable paragraphs as the repository owner added rules.
- [full-record.md](full-record.md) is the full record which holds every rule and every passage in the order the rules were added.
- [single-word-stage.md](single-word-stage.md) reports the earlier stage where copying agents built strings out of single words from three Bible selections.
- [john-10-remixes.md](john-10-remixes.md) holds three remixes of John chapter 10 where the chapter was dealt at random into four piles and each pile was turned into one readable paragraph.

## Live programs

- [program-3-key-phrases.html](program-3-key-phrases.html) is the program for the key phrase method which is the method behind the finished outputs and the file runs in a web browser after downloading.
- The folder named [old](old) holds the two earlier programs (copying letters and copying single words) which the repository owner does not expect to use again.
- Bible Key Phrases: Claude Selection (an older set of 41 passages): https://claude.ai/artifact/PK8tNEMDZM2eVaCfuNSxdR
- Bible Key Phrases: Personal Version (an older set of ten whole books): https://claude.ai/artifact/4pJdWtCH4ahdFjsb4GVb8Q
- Bible Key Phrases: Jesus Version (the words of Jesus in Matthew and Mark and Luke and John): https://claude.ai/artifact/Bzcg2eYnte9cTc7wtpBArz
- The live programs only shuffle phrases and do not carry out the joining rules which means the finished paragraphs are made by an AI model that follows the rules page.
