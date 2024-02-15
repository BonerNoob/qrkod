import qrcode
#merhaba kodu kullanmak için data = "" yere linki at ve çıkan qr kodu dene

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

data = ""
qr.add_data(data)
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")


img.save("abc.png")
