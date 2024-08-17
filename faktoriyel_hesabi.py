a = int(input("Faktoriyeli hesaplanacak olan sayıyı giriniz: "))
b = 1

if a<0:
    print("Negatif sayıların faktoriyeli hesaplanamaz!")

elif a==0:
    print("Sonuç = 1")

else:
    for i in range(1,a+1):
        b = b*i
        print("Sonuç = ",b)