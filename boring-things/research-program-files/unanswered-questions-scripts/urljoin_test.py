# Shows which inputs make urllib.parse.urljoin leave the base host (run: python3 urljoin_test.py)
import sys
from urllib.parse import urljoin, urlsplit
base = "https://good.example/app/"
tests = ["/\t/evil.example/x", "/\n/evil.example/x", "/\r/evil.example", "  //evil.example/x",
         "\x01//evil.example/x", "/%09/evil.example", "\\\\evil.example", "page.html"]
print("Python", sys.version.split()[0])
for t in tests:
    joined = urljoin(base, t)
    same_host = urlsplit(joined).netloc == urlsplit(base).netloc and urlsplit(joined).scheme == urlsplit(base).scheme
    print(repr(t), "->", repr(joined), "| stays on base host:", same_host)
