import random

# sayi = 25
hak = 10

# Burada dilersek sayıyı bilgisayardan random olarak da oluşturabiliriz.
pc_secimi = random.randint(0,100) # 0 ve 100 dahil olmak üzere bilgisayar bu aralıktan bir sayı seçer

print("Sayı Tahmini Oyununa Hoşgeldiniz!\nToplam 10 hakkınız var!\n"
      "Haklarınız biterse oyun biter:(")

while hak > 0:
    tahmin = int(input("Lütfen 0 ile 100 arasında pozitif bir sayı giriniz: "))
    if tahmin < 0:
        print("Girdiğiniz sayı negatif:(")
        continue
    hak -= 1

    if pc_secimi == tahmin:
        print("Doğru tahmin ettiniz Tebrikler :))))")
        break
    elif pc_secimi > tahmin:
        print("Yukarı, Kalan Hakkınız {}".format(hak))
    else:
        print("Aşağı, Kalan Hakkınız {}".format(hak))

    if hak == 0:
        print("Hakkınız Kalmadı :( Doğru Sayı {} olacaktı.".format(pc_secimi))