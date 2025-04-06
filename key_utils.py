from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

def generate_keys():
    private_key = dsa.generate_private_key(key_size=2048)
    public_key = private_key.public_key()

    # Save private key
    with open("private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Save public key
    with open("public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    print("Keys generated and saved as 'private_key.pem' and 'public_key.pem'.")
