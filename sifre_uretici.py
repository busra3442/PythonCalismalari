import random
import string # bu modül sayesinde aşağıda belirttiğim tüm string ifadelere ulaşabilirim

# Soru
# eğer her karakterden en az iki tane kullanmamı isterse
# ve 10 haneli şifre (kalan 2 karakter opsiyonel) isterse nası yaparım?

'''
rakamlar = "0123456789"
semboller = ")(><+%=?-"
kucuk_harfler = "abcd"
'''

rakamlar = string.digits
semboller = string.punctuation
kucuk_harfler = string.ascii_lowercase
buyuk_harfler = string.ascii_uppercase
tum_karakterler = [rakamlar,semboller,kucuk_harfler,buyuk_harfler]

print(rakamlar)
print(semboller)
print(kucuk_harfler)
print(buyuk_harfler)

sifre =""

'''
for i in range(2):
    sifre += tum_karakterler[0][random.randint(0,9)]

for i in range(2):
    sifre += tum_karakterler[1][random.randint(0, 9)]

for i in range(2):
    sifre += tum_karakterler[2][random.randint(0, 9)]

for i in range(2):
    sifre += tum_karakterler[3][random.randint(0, 9)]
'''
# bunu yapmak yerine tek bir dögü açıp yapabilirim
for j in range(4):
    for i in range(2):
        sifre += tum_karakterler[j][random.randint(0, 9)]

print(sifre)
sifre = list(sifre) # sifre stringini listeye dönüştürdüm
random.shuffle(sifre) # shuffle metodu içine liste alır ve liste içindeki elemanları karıştırır
print(sifre)

yeni_sifre = ""

'''
for i in sifre:
    yeni_sifre += i
    bu şekilde de listeyi stringe dönüştürürüm
'''
yeni_sifre = yeni_sifre.join(sifre) # listenin tüm elemanlarını alıp stringe ekleme yaparak ilerler
print(yeni_sifre) # listeden string yaptım ve ekrana basıyorum