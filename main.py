import qrcode
import os  # work with file paths and directories.
from datetime import datetime  # generate a timestamp gor the file name


def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=3
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    if not os.path.exists("generatedQRs"):
        os.makedirs("generatedQRs")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    img_filename = f"qrimg_{timestamp}.png"

    img_path = os.path.join("generatedQRs", img_filename)
    img.save(img_path)


input = input("Entre text: ")
generate_qrcode(input)
