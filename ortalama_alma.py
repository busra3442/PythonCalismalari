a = []
b = int(input("Kaç tane sayının ortalamasını almak istersiniz? "))

for i in range(b):
    c = int(input("sayı giriniz: "))
    a.append(c)

d = sum(a)
ortalama = d/len(a)
print("Ortalama: ", ortalama)