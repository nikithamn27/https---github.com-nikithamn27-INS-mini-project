from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import dsa
from datetime import datetime

def sign_message_terminal():
    # Load private key
    with open("private_key.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    # Get message from user input
    message = input("Enter the message to sign: ")

    # Add timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[Timestamp: {timestamp}]\n{message}"
    data = full_message.encode("utf-8")

    # Sign message
    signature = private_key.sign(data, hashes.SHA256())

    # Save signed message and signature
    with open("files/signed_message.txt", "w", encoding="utf-8") as f:
        f.write(full_message)

    with open("files/signature.sig", "wb") as f:
        f.write(signature)

    print("Message signed with timestamp. Saved as 'signed_message.txt' and 'signature.sig'.")
