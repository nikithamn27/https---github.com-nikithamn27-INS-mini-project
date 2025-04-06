import os
from PyPDF2 import PdfReader
from cryptography.hazmat.primitives import hashes, serialization
from datetime import datetime
from cryptography.exceptions import InvalidSignature

def read_pdf_content(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def sign_pdf(pdf_path, signature_path="files/pdf_signature.sig"):
    # Load your private key
    with open("private_key.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    # Extract text from the PDF
    content = read_pdf_content(pdf_path)

    # Prepend a timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_text = f"[Timestamp: {timestamp}]\n{content}"

    # --- DEBUG: print what we're signing ---
    print("=== DEBUG: Signing these bytes ===")
    print(full_text[:200], "…")  # first 200 chars
    print("=================================")

    # Ensure the output folder exists
    os.makedirs("files", exist_ok=True)

    # Save the exact text you will sign
    with open("files/signed_pdf.txt", "w", encoding="utf-8") as f:
        f.write(full_text)

    # Sign the bytes of that text
    data = full_text.encode("utf-8")
    signature = private_key.sign(data, hashes.SHA256())

    # Save the signature
    with open(signature_path, "wb") as f:
        f.write(signature)

    return timestamp, signature_path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization

def verify_pdf(pdf_path, signature_path="files/pdf_signature.sig"):
    # Load your public key
    with open("public_key.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    # Read back exactly what was signed
    with open("files/signed_pdf.txt", "r", encoding="utf-8") as f:
        signed_text = f.read()

    # --- DEBUG: print what we're verifying ---
    print("=== DEBUG: Verifying against these bytes ===")
    print(signed_text[:200], "…")
    print("===========================================")

    signed_data = signed_text.encode("utf-8")

    # Load the signature
    with open(signature_path, "rb") as f:
        signature = f.read()

    # Perform verification
    try:
        public_key.verify(signature, signed_data, hashes.SHA256())
        return True
    except InvalidSignature:
        return False
