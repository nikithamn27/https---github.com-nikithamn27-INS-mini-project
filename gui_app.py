import tkinter as tk
from qr_utils import generate_qr
from tkinter import messagebox, scrolledtext, filedialog
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import dsa
from datetime import datetime
from pdf_utils import sign_pdf, verify_pdf  # make sure pdf_utils.py is in the same folder

# --- Core Functions ---

def generate_keys():
    private_key = dsa.generate_private_key(key_size=2048)
    public_key = private_key.public_key()

    with open("private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    with open("public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    messagebox.showinfo("Success", "Keys generated successfully.")

def sign_message():
    message = message_input.get("1.0", tk.END).strip()
    if not message:
        messagebox.showwarning("Empty", "Enter a message to sign.")
        return

    try:
        with open("private_key.pem", "rb") as f:
            private_key = serialization.load_pem_private_key(f.read(), password=None)
    except FileNotFoundError:
        messagebox.showerror("Error", "Private key not found. Generate keys first.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[Timestamp: {timestamp}]\n{message}"
    data = full_message.encode("utf-8")

    signature = private_key.sign(data, hashes.SHA256())

    with open("files/signed_message.txt", "w", encoding="utf-8") as f:
        f.write(full_message)

    with open("files/signature.sig", "wb") as f:
        f.write(signature)

    messagebox.showinfo("Success", "Message signed and saved.")

def verify_signature():
    try:
        with open("public_key.pem", "rb") as f:
            public_key = serialization.load_pem_public_key(f.read())
        with open("files/signed_message.txt", "r", encoding="utf-8") as f:
            message = f.read()
        with open("files/signature.sig", "rb") as f:
            signature = f.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "Missing signed message or key file.")
        return

    try:
        public_key.verify(signature, message.encode("utf-8"), hashes.SHA256())
        messagebox.showinfo("Verification", "Message signature is VALID.")
    except Exception:
        messagebox.showerror("Verification", "Message signature is INVALID or tampered.")

        
# — PDF Functions —

pdf_path = None

def select_pdf():
    global pdf_path
    path = filedialog.askopenfilename(
        title="Select PDF",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if path:
        pdf_path = path
        lbl_pdf.config(text=f"Selected: {path.split('/')[-1]}")

def sign_pdf_gui():
    if not pdf_path:
        messagebox.showwarning("No PDF", "Please select a PDF first.")
        return
    try:
        timestamp, sig_file = sign_pdf(pdf_path)
        messagebox.showinfo("PDF Signed", f"Signed at {timestamp}\nSaved:\n • files/signed_pdf.txt\n • {sig_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to sign PDF:\n{e}")

def verify_pdf_gui():
    if not pdf_path:
        messagebox.showwarning("No PDF", "Please select a PDF first.")
        return
    try:
        valid = verify_pdf(pdf_path)
        if valid:
            messagebox.showinfo("PDF Verification", "PDF signature is VALID.")
        else:
            messagebox.showerror("PDF Verification", "PDF signature is INVALID or tampered.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to verify PDF:\n{e}")

# --- GUI Setup ---

root = tk.Tk()
root.title("DSS Digital Signature GUI")
root.geometry("700x500")

tk.Label(root, text="DSS Digital Signature Standard", font=("Helvetica", 16, "bold")).pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Generate Keys", width=18, command=generate_keys).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Verify Message", width=18, command=verify_signature).grid(row=0, column=1, padx=10)

tk.Label(root, text="Enter message to sign:").pack(pady=5)
message_input = scrolledtext.ScrolledText(root, height=6, width=70)
message_input.pack()
tk.Button(root, text="Sign Message", width=18, command=sign_message).pack(pady=10)

# PDF section
tk.Label(root, text="— PDF Signing / Verification —", font=("Helvetica", 14)).pack(pady=15)
pdf_frame = tk.Frame(root)
pdf_frame.pack(pady=5)
tk.Button(pdf_frame, text="Select PDF", width=15, command=select_pdf).grid(row=0, column=0, padx=5)
lbl_pdf = tk.Label(pdf_frame, text="No PDF selected", wraplength=400)
lbl_pdf.grid(row=0, column=1, padx=5)
tk.Button(pdf_frame, text="Sign PDF", width=15, command=sign_pdf_gui).grid(row=1, column=0, pady=5)
tk.Button(pdf_frame, text="Verify PDF", width=15, command=verify_pdf_gui).grid(row=1, column=1, pady=5)

# QR Code section
tk.Label(root, text="— QR Code Export —", font=("Helvetica", 14)).pack(pady=15)
qr_frame = tk.Frame(root)
qr_frame.pack(pady=5)

tk.Button(qr_frame, text="Export Msg Sig QR", width=15, command=lambda: export_qr('message')).grid(row=0, column=0, padx=5)
tk.Button(qr_frame, text="Export PDF Sig QR", width=15, command=lambda: export_qr('pdf')).grid(row=0, column=1, padx=5)

def export_qr(kind: str):
    """
    kind: 'message' or 'pdf'
    """
    if kind == 'message':
        sig_path = "files/signature.sig"
        out_png = "files/signature_qr.png"
    else:
        sig_path = "files/pdf_signature.sig"
        out_png = "files/pdf_signature_qr.png"

    try:
        with open(sig_path, "rb") as f:
            sig_bytes = f.read()
    except FileNotFoundError:
        messagebox.showerror("Error", f"{sig_path} not found. Generate and sign first.")
        return

    qr_file = generate_qr(sig_bytes, out_png)
    messagebox.showinfo("QR Generated", f"QR code saved to:\n{qr_file}")

root.mainloop()
