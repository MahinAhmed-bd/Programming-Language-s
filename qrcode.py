import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

def take_student_info():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    return student_id, name


def generate_qr_code(student_id, name):
    data = f"Student ID: {student_id}\nName: {name}"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("QR_Code_1.png")
    print("QR code generated successfully!")


def decode_images():
    try:
        qr_img_paths = ["QR_Code_1.png"]  # You can add more images
        
        for qr_img_path in qr_img_paths:
            img = Image.open(qr_img_path)
            decoded_qr = decode(img)

            for obj in decoded_qr:
                print("Decoded Data:")
                print(obj.data.decode("utf-8"))

            print("Decoded QR code from", qr_img_path)

    except Exception as e:
        print("Error decoding QR code:", e)