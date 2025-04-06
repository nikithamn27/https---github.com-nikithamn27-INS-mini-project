import qrcode
import os

def generate_qr(data: bytes, output_path: str):
    """
    Generate a QR code from raw bytes (e.g., a signature) and save as PNG.
    """
    # Convert bytes to hex string for embedding in QR
    hex_data = data.hex()
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4,
    )
    qr.add_data(hex_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    return output_path
