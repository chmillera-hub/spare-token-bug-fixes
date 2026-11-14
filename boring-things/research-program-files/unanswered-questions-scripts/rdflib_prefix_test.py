# Shows that rdflib keeps one prefix per namespace (run: python3 rdflib_prefix_test.py)
import rdflib
NS = "http://purl.org/dc/terms/"
def ttl(first, second):
    return f'''@prefix {first}: <{NS}> .
@prefix {second}: <{NS}> .
@prefix ex: <http://example.org/> .
ex:a {first}:title "A" ; {second}:creator "B" .
'''
def kept(g):
    return [p for p, n in g.namespaces() if str(n) == NS]
print("rdflib", rdflib.__version__)
for first, second in (("dct", "dcterms"), ("dcterms", "dct")):
    for mode in ("rdflib", "none"):
        g = rdflib.Graph(bind_namespaces=mode)
        g.parse(data=ttl(first, second), format="turtle")
        print(f"declared {first} then {second} | built-in prefixes {mode} | kept {kept(g)}")
g = rdflib.Graph()
g.parse(data=ttl("dct", "dcterms"), format="turtle")
g.bind("dct", NS, override=True, replace=True)
print("after bind(dct, override=True, replace=True) | kept", kept(g))
print(g.serialize(format="turtle"))
