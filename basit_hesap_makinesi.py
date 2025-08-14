"""
kullanıcıdan alınan iki sayının toplama çıkarma çarpma ve bölme işlemlerini yapabilen
basit bir hesap makinesi
"""
sayi1 = int(input("sayı 1 = "))
sayi2 = int(input("sayı 2 = "))

print("Lütfen hesap makinesine yaptırmak isteğiniz işlemi seçin!")
print("Toplama","Cikarma","Carpma","Bolme")

secilen = input("Seçtiğiniz İşlem = ")

if secilen == "Toplama":
    print("Sonuç: ",sayi1+sayi2 )

elif secilen == "Cikarma":
    print("Sonuç: ", sayi1-sayi2)

elif secilen == "Carpma":
    print("Sonuç: ", sayi1*sayi2)

elif secilen == "Bolme":
    print("Sonuç: ", sayi1/sayi2)

else:
    print("Lütfen işleminizi yazıldığı gibi seçin!")



