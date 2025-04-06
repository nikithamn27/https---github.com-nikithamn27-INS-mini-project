# 🛡️ DSS Digital Signature Project with GUI

This project is a mini demonstration of the **Digital Signature Standard (DSS)** using DSA keys for signing and verifying both messages and PDF documents. It also includes a simple **Tkinter-based GUI** for ease of use, QR code generation for digital signatures, and a terminal CLI interface.

## 📁 Features

- 🔐 Key generation (DSA 2048-bit)
- ✍️ Message signing with timestamp
- ✅ Signature verification (message + PDF)
- 📄 PDF signing and validation
- 📷 QR code export of signatures
- 🖥️ User-friendly GUI (Tkinter) + CLI support

---

## 🛠️ Installation

### 🔧 Requirements
---

```markdown
# 🚀 How to Run the Project

This guide explains how to run both the **CLI** and **GUI** versions of the Digital Signature DSS project.

---

## 🔧 Prerequisites

Make sure you have the following installed:

- Python 3.8 or higher
- Pip (Python package installer)

---

## 📦 Install Dependencies

Navigate to your project folder and install the required packages:

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` file yet, create one with:

```
cryptography
PyPDF2
qrcode
pillow
```

Save it as `requirements.txt` and run the install command again.

---

## 🖥️ Run the CLI Version

```bash
python main.py
```

You will see a text-based menu with options to:

- Generate Keys
- Sign a Message
- Verify a Signature

---

## 🧩 Run the GUI Version

```bash
python gui_app.py
```

The graphical interface allows you to:

- Generate DSA key pairs
- Sign and verify text messages
- Sign and verify PDF documents
- Export signatures as QR codes

---

## 📂 Output Files

Signed data, keys, and QR codes are saved in the `files/` directory:

- `signature.sig` – Signature file
- `signed_message.txt` – Signed text message
- `pdf_signature.sig` – PDF signature
- `signature_qr.png` – QR code for text signature
- `pdf_signature_qr.png` – QR code for PDF signature
- `private_key.pem`, `public_key.pem` – Key files

---

## 🛑 Stop Execution

Use `CTRL+C` in the terminal to stop the CLI version. For the GUI, simply close the window.

---

## 📬 Need Help?

If you run into any issues, make sure:
- You're using the correct Python version
- All dependencies are installed
- Key files are generated before verifying signatures

---
## 🗂 Folder Structure

```
project/
├── gui_app.py             # GUI implementation using Tkinter
├── main.py                # Terminal CLI mode
├── key_utils.py           # DSA key generation logic
├── signer.py              # Text message signing logic
├── verifier.py            # Text message signature verification
├── pdf_utils.py           # PDF signing and verification
├── qr_utils.py            # QR code generation for signatures
├── private_key.pem        # Private key (generated)
├── public_key.pem         # Public key (generated)
├── /files                 # All generated files go here
│   ├── signed_message.txt
│   ├── signature.sig
│   ├── signed_pdf.txt
│   ├── pdf_signature.sig
│   ├── signature_qr.png
│   └── pdf_signature_qr.png
```

---
## 🔒 Security Notes

- Private keys should **never be shared**. For demo purposes, keys are generated and stored locally.
- Messages include a **timestamp** to ensure freshness and protect against replay attacks.
- **Any change** to the message or file after signing will cause the signature verification to **fail**.

---

## 📸 Screenshots

![Screenshot (37)](https://github.com/user-attachments/assets/6e9e66a6-982a-4e33-a89d-d83b6f935158)


---

## 📃 License

This project is for educational use only. You are free to modify, improve, and redistribute with proper attribution.

---







