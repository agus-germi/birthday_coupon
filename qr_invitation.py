import qrcode

url = "https://agus-germi.github.io/birthday_coupon/#" 
qr = qrcode.make(url)
qr.save("invite_qr.png")
