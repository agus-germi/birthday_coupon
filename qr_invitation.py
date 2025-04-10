import qrcode

url = "https://yourdomain.com" 
qr = qrcode.make(url)
qr.save("invite_qr.png")
