# Putting an LDAP address with host and attribute description into a certificate with the cryptography library

## Link to the original question

https://discuss.python.org/t/87403

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 with the Python library cryptography version 50.0.1 and no other person has rerun the test yet which means the page is unconfirmed.

## The question

On 7 April 2025 somebody asked on the Python help forum whether the cryptography library can add the host part and the attribute description part of an LDAP address to the relative_name of a certificate revocation list location.
The asker quoted the certificate standard which wants an LDAP address such as ldap://ldap.example.com/cn=example%20CA,dc=example,dc=com?certificateRevocationList;binary.
The asker already knew how to put name parts such as CN and DC into relative_name.
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

- A distribution point built with full_name holding one UniformResourceIdentifier accepted the complete LDAP address including the host and the attribute description.
- A certificate signed with that extension returned exactly the same address when read back.
- Putting a host into relative_name was refused with a TypeError because relative_name accepts only name attributes such as CN and DC.
- Giving both full_name and relative_name was refused with the message that one of the two must be None.

## Best-guess answer

The host and the attribute description do not belong in relative_name because relative_name holds only a fragment of a directory name. The complete LDAP address goes into full_name as one address:

dp = x509.DistributionPoint(
    full_name=[x509.UniformResourceIdentifier("ldap://ldap.example.com/cn=example%20CA,dc=example,dc=com?certificateRevocationList;binary")],
    relative_name=None, reasons=None, crl_issuer=None)
builder = builder.add_extension(x509.CRLDistributionPoints([dp]), critical=False)

The test file named ldap_crl.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
