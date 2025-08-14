adres_defteri = []

def secenekler():
    print("\nAdres Defteri(Rehber) Uygulaması")
    print("1- Kişi Ekle")
    print("2- Kişi Sil")
    print("3- Kişileri Göster")
    print("4- Çıkış")

def kisi_ekle():
    isim = input("İsim: ")
    telefon = input("Telefon: ")
    email = input("Email: ")
    adres_defteri.append({"İsim":isim, "Telefon": telefon,"Email": email})
    print(f"{isim} kişisi Adres Defterine kaydedildi.")

def kisi_sil():
    silinen_isim = input("Lütfen silmek istediğiniz kişinin ismini giriniz: ")
    for i, kisi in enumerate(adres_defteri):
        if kisi["İsim"] == silinen_isim:
            silinen_kisi = adres_defteri.pop(i)
            print(f"{silinen_kisi['İsim']} Adres Defterinden silindi.")
            break
    else:
        print(f"{silinen_isim} bulunamadı.")


def kisileri_goster():
    if not adres_defteri:
        print("Adres Defteri boş.")
    else:
        print("\nAdres Defteri")
        for i, kisi in enumerate(adres_defteri,1):
            print(f"{i}. İsim: {kisi['İsim']},Telefon: {kisi['Telefon']},Email: {kisi['Email']}")

while True:
    secenekler()
    secim = int(input("Lütfen yapmak istediğiniz işlemi seçiniz: "))

    if secim == 1:
        kisi_ekle()
    elif secim == 2:
        kisi_sil()
    elif secim == 3:
        kisileri_goster()
    elif secim == 4:
        print("Programdan Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyiniz!")