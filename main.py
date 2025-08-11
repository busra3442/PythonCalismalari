import qrcode

'''
img = qrcode.make("Hello World! My name is Büşra! I love python:)")
img.save("mycode.png")
# bu qr ile (mycode.png) yukarıda yazdığım metin telefon ekranına bastırılıyor.
'''

qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L,
                   box_size = 20,
                   border = 2)
qr.add_data("https://www.neuralnine.com/books")
qr.make(fit = True)

img = qr.make_image(fill_color = "black", back_color = "white")
img.save("advanced.png")
# bu qr ile (advanced.png) yukarıda belirttiğim web siteye ulaşabiliyorum

