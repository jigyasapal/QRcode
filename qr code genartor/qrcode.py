import qrcode as qr
img = qr.make("https://youtu.be/c2f03oSSDAM?si=u98ISRqTtFV6T4ws")
img.save("qrcode.png")