sayfa = 5
toplam = 0
gun,ay,yil = 1,1,2025

def bir_sonraki_gunu_hesapla(gun,ay,yil):
    gun += 1
    if ay in [1,3,5,7,8,10,12] and gun > 31:
        gun = 1
        ay += 1

    elif ay in [4,6,9,11] and gun > 30:
        gun = 1
        ay += 1

    elif ay == 2 :
        if yil % 4 == 0 and gun > 29:
            gun = 1
            ay += 1
        elif yil % 4 != 0 and gun > 28:
            gun = 1
            ay += 1
    return gun,ay,yil

f = open("sayfa_sayisi.txt","w")
for i in range(365):
    f.write(str(gun) + "-" + str(ay) + "-" +
            str(yil) + ":" + str(sayfa) + "\n")
    gun, ay , yil = bir_sonraki_gunu_hesapla(gun,ay,yil)
    toplam += sayfa

    print("Toplam sayfa sayisi: ", toplam)
    print("Toplam kitap sayisi: ", toplam / 150)  # sayfa sayısını ort olarak 150 diyelim
