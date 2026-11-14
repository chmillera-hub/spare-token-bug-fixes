# Checks which CRL functions pyOpenSSL still has and parses a certificate revocation list with the cryptography library (Python forum topic 77561)
import datetime, OpenSSL, cryptography
from OpenSSL import crypto
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
print("pyOpenSSL", OpenSSL.__version__, "| cryptography", cryptography.__version__)
for name in ("CRL", "Revoked", "dump_crl", "load_crl"):
    print(f"OpenSSL.crypto.{name} exists:", hasattr(crypto, name))
key = ec.generate_private_key(ec.SECP256R1())
issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "Test CA")])
now = datetime.datetime.now(datetime.timezone.utc)
builder = x509.CertificateRevocationListBuilder().issuer_name(issuer).last_update(now).next_update(now + datetime.timedelta(days=7))
for serial, reason in ((1001, x509.ReasonFlags.key_compromise), (1002, x509.ReasonFlags.superseded)):
    builder = builder.add_revoked_certificate(x509.RevokedCertificateBuilder().serial_number(serial).revocation_date(now)
                                              .add_extension(x509.CRLReason(reason), critical=False).build())
crl = builder.sign(key, hashes.SHA256())
pem = crl.public_bytes(serialization.Encoding.PEM); der = crl.public_bytes(serialization.Encoding.DER)
for label, loaded in (("PEM", x509.load_pem_x509_crl(pem)), ("DER", x509.load_der_x509_crl(der))):
    entries = [(r.serial_number, r.extensions.get_extension_for_class(x509.CRLReason).value.reason.name) for r in loaded]
    print(f"{label}: issuer {loaded.issuer.rfc4514_string()} | revoked entries {entries} | signature valid: {loaded.is_signature_valid(key.public_key())}")
found = x509.load_pem_x509_crl(pem).get_revoked_certificate_by_serial_number(1002)
print("lookup of serial 1002:", found is not None, "| lookup of serial 9999:", x509.load_pem_x509_crl(pem).get_revoked_certificate_by_serial_number(9999) is not None)
