# Mini model files

This folder holds a tiny text model that an AI chatbot (Claude) trained only on the 6020 comments in the owner-comments-full folder of this repository. The page named mini-model-findings.md in that folder explains what the model learned and shows sample outputs.

- model.pt holds the 2.6 million trained numbers of the model.
- word-pieces.json holds the 4096 word pieces that the model reads and writes.
- train.py is the program that trained the model and the program needs the Python packages named torch and tokenizers. Run the program from inside this folder with a number of seconds to train for such as: python3 train.py 1320
- write.py is the program that makes the model write. Run python3 write.py gen to print sample outputs or run python3 write.py nb to print the closest words to a set of test words.

The model only imitates which words tend to follow which words in the comments which means the model does not understand the comments and the outputs are not statements to rely on.
- tests.py is the program that ran the tests reported on the page named mini-model-outputs.md. Run python3 tests.py from inside this folder.
