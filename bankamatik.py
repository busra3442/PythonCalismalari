a = int(input("Paranız: "))
while True:
 b = int(input(("Lütfen bir işlem seçiniz\n\n1-Bakiye Sorgulama\n2-Para Yatırma\n3-Para Çekme\n4-Çıkış\n")))

 if b == 1:
     print("Anlık bakiyeniz: ",a)
 elif b == 2:
     c = int(input("Ne kadar para yatırmak istersiniz? "))
     a = a + c
     print("Anlık bakiyeniz: ",a)

 elif b == 3:
     d = int(input("Ne kadar para çekmek istersiniz? "))
     if d<a:
      a = a - d
     print("Anlık bakiyeniz: ",a)
     if d==a:
         a = a-d
         print("Anlık bakiyeniz: ",a)
     else:
      print("Hesabınızda o kadar para yok!")

 elif b == 4:
     print("Hoşçakalın!")
     break


