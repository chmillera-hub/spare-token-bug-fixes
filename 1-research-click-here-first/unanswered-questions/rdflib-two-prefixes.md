# Why rdflib turns the prefix dct into dcterms

## Link to the original question

https://github.com/aigora-de/rdf-construct/issues/457

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the tests in a single chat on 12 November 2026 on rdflib version 7.6.0 and no other person has rerun the tests yet which means the results on this page are unconfirmed.

## The question

An open GitHub issue with zero comments (aigora-de/rdf-construct issue number 457) has the title "Two prefixes for one namespace: rdflib keeps one, so a source's dct: comes back as dcterms".
Only the title was readable because the request to open the issue page was not approved in time so the answer on this page responds to the title and not to the full text of the issue.
The library rdflib is a Python library for linked data files and a prefix is a short nickname for a long web address inside such a file.

## What the tests show

- A Turtle file that declares the nicknames dct and dcterms for the same web address (http://purl.org/dc/terms/) comes back from rdflib with only one nickname because rdflib stores one nickname per web address.
- The nickname declared last in the file is the nickname that rdflib keeps. Declaring dct then dcterms kept dcterms and declaring dcterms then dct kept dct.
- Turning off the built-in nicknames of rdflib (the setting bind_namespaces="none") did not change which nickname was kept.
- Calling g.bind("dct", "http://purl.org/dc/terms/", override=True, replace=True) after reading the file made rdflib write dct in the output.

## Best-guess answer

A program that wants the nickname from the source file to survive can remember the wanted nickname and call bind with override=True and replace=True after reading the file.
Keeping both nicknames at once was not possible in any test because rdflib 7.6.0 stores one nickname per web address.

The test file named rdflib_prefix_test.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
