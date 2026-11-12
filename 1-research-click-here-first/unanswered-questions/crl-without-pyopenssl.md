# Parsing certificate revocation lists after pyOpenSSL dropped its CRL functions

## Link to the original question

https://discuss.python.org/t/77561

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 with pyOpenSSL 26.4.0 and cryptography 50.0.1 and no other person has rerun the test yet which means the page is unconfirmed.

## The question

On 18 January 2025 somebody asked on the Python help forum whether pyOpenSSL has removed its functions for certificate revocation lists (lists of certificates that were cancelled before their end date) and whether another pyOpenSSL function can still parse such a list.
The asker could no longer find OpenSSL.crypto.CRL and Revoked and dump_crl and load_crl.
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

- In pyOpenSSL 26.4.0 the names OpenSSL.crypto.CRL and Revoked and dump_crl and load_crl do not exist.
- The cryptography library (the library that pyOpenSSL itself is built on and installs alongside) built a revocation list with two cancelled serial numbers and read the list back from both common file encodings (PEM and DER).
- The read-back list gave the issuer name and both serial numbers (1001 and 1002) with their reasons (key compromise and superseded) and the signature check against the issuer key passed.
- A lookup of serial 1002 found the entry and a lookup of serial 9999 found nothing.

## Best-guess answer

The four functions are gone from current pyOpenSSL and the test found no replacement inside pyOpenSSL.
The replacement that worked in the test is the cryptography library:

from cryptography import x509
crl = x509.load_pem_x509_crl(pem_bytes)        # or x509.load_der_x509_crl(der_bytes)
for revoked in crl:
    print(revoked.serial_number, revoked.revocation_date_utc)
entry = crl.get_revoked_certificate_by_serial_number(serial)

The asker listed cryptography.x509 among the missing things and one possibility is a very old or broken installation of the cryptography library because the module is present in the tested version.

The test file named crl_parse.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
