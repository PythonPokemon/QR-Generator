import qrcode
import tkinter as tk
from PIL import Image, ImageTk

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def show_qr_code_image(filename):
    root = tk.Tk()
    root.title("QR Code Viewer")

    image = Image.open(filename)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=photo)
    label.image = photo  # To keep a reference, otherwise the image won't show up.
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    data_to_store = "https://discord.gg/zcHmdXcE"
    file_name = "qr_code.png"
    generate_qr_code(data_to_store, file_name)
    show_qr_code_image(file_name)
