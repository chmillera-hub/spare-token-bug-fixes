# Builds a certificate whose CRL distribution point is an LDAP address with host and attribute description (Python forum topic 87403)
import datetime, cryptography
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
print("cryptography", cryptography.__version__)
key = ec.generate_private_key(ec.SECP256R1())
name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "example CA"), x509.NameAttribute(NameOID.DOMAIN_COMPONENT, "example"), x509.NameAttribute(NameOID.DOMAIN_COMPONENT, "com")])
uri = "ldap://ldap.example.com/cn=example%20CA,dc=example,dc=com?certificateRevocationList;binary"
dp = x509.DistributionPoint(full_name=[x509.UniformResourceIdentifier(uri)], relative_name=None, reasons=None, crl_issuer=None)
now = datetime.datetime.now(datetime.timezone.utc)
cert = (x509.CertificateBuilder().subject_name(name).issuer_name(name).public_key(key.public_key()).serial_number(x509.random_serial_number())
        .not_valid_before(now).not_valid_after(now + datetime.timedelta(days=30))
        .add_extension(x509.CRLDistributionPoints([dp]), critical=False).sign(key, hashes.SHA256()))
back = x509.load_der_x509_certificate(cert.public_bytes(encoding=serialization.Encoding.DER))
ext = back.extensions.get_extension_for_class(x509.CRLDistributionPoints).value
print("address read back from the finished certificate:", ext[0].full_name[0].value)
print("identical to the address that went in:", ext[0].full_name[0].value == uri, "| relative_name is empty:", ext[0].relative_name is None)
try:
    x509.DistributionPoint(full_name=[x509.UniformResourceIdentifier(uri)], relative_name=x509.RelativeDistinguishedName([x509.NameAttribute(NameOID.COMMON_NAME, "x")]), reasons=None, crl_issuer=None)
except ValueError as e: print("full_name and relative_name together are refused:", e)
try:
    x509.RelativeDistinguishedName([x509.NameAttribute(NameOID.COMMON_NAME, "CA"), "ldap.example.com"])
except Exception as e: print("a host put into relative_name is refused:", type(e).__name__)
