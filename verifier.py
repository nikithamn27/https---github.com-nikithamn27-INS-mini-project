from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

def verify_signature(file_path="files/signed_message.txt", signature_path="files/signature.sig"):
    # Load public key
    with open("public_key.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    # Read full message (with timestamp)
    with open(file_path, "r",encoding="utf-8") as f:
        full_message = f.read()
        data = full_message.encode("utf-8")
        text = full_message

    # Read signature
    with open(signature_path, "rb") as f:
        signature = f.read()

    try:
        public_key.verify(signature, data, hashes.SHA256())
        print("Signature is VALID.")
        print("Message and timestamp:")
        print("----------------------")
        print(text)
    except InvalidSignature:
        print("Signature is INVALID. The message may have been tampered with.")
