# Is the Python function urljoin unsafe with web addresses from strangers

One AI model (Claude) ran the tests in a single chat on 12 November 2026 on Python version 3.13.18 and no other person has rerun the tests yet which means the results on this page are unconfirmed.

## The question

On 21 September 2026 somebody asked on the Python help forum (discuss.python.org topic number 109165) whether the standard Python function urljoin is known to be weak against hostile input and whether a ticket exists about the weakness.
The function urljoin combines a base web address with a second piece of a web address.
The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

The base address in every test was https://good.example/app/ and the test asked whether the combined address still pointed at good.example.

- The input slash then a tab character then slash then evil.example produced https://evil.example because Python deletes the tab character and two slashes in a row mean "go to a different website".
- The same jump to evil.example happened with a newline character or a carriage return character between the two slashes.
- The same jump happened with two spaces in front of two slashes and with a control character in front of two slashes because Python strips those characters from the front.
- The input with the tab written as the three characters %09 stayed on good.example because Python deletes only a real tab character.
- An ordinary input such as page.html stayed on good.example.

## What the Python documentation says

The Python documentation states that tab and newline characters are removed from a web address at any position since Python version 3.10 and that leading control characters and spaces are stripped. The documentation says the removal follows the web address standard that web browsers use. Source: https://docs.python.org/3/library/urllib.parse.html

The same documentation warns that urljoin is generally not secure with a second piece that an attacker controls.

A public security write-up from the Google security research team describes a real chain of redirects on the Python package website that used the slash and tab and slash input. Source: https://github.com/google/security-research/security/advisories/GHSA-6hc9-758f-7r98

## Best-guess answers to the three questions in the post

1. The weakness is real and known because the tests reproduce the jump to another website and the documentation carries a warning about attacker-controlled input.
2. The removal of tab and newline characters was added on purpose so a replacement inside Python would be a design decision for the Python maintainers. A program can protect itself today by comparing the website name of the combined address with the website name of the base address and the test file shows that the comparison caught every jump in the list above.
3. The search for this page found the two code changes that added the character removal (CPython pull requests 25727 and 25923 and the later change numbered 102153) and found no ticket that asks for urljoin itself to be replaced. A ticket could still exist because the search was a web search and not a search inside the Python issue tracker.

The test file named urljoin_test.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
