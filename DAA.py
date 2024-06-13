from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives import serialization
import base64

# Generate a key pair (usually done once)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Serialize and save the private key (keep this secret)
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Load the private key from saved data (simulating loading from a file)
loaded_private_key = load_pem_private_key(private_pem, password=None)

# Serialize and share the public key
public_key = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Simulate a message to be authenticated
message = b"Hello, this is a secure message."

# Sign the message using the private key
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Verify the signature using the public key
try:
    loaded_public_key = load_pem_public_key(public_key)
    loaded_public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is valid. Message is authentic.")
except utils.InvalidSignature:
    print("Signature is invalid. Message may have been tampered with.")
