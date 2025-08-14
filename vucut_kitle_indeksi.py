def bmi_hesaplama(kilo,boy):
    bmi = kilo/(boy**2)
    return bmi

kilo = float(input("Lütfen kilonuzu kg cinsinden giriniz : "))
boy = float(input("Lütfen boyunuzu metre cinsinden giriniz(örn 1.76 : "))

bmi = bmi_hesaplama(kilo,boy)

print(f"Vücut Kitle İndeksiniz (BMI) : {bmi:.2f}")

if bmi < 18.5:
    print("Durum : Zayıf")
elif 18.5 < bmi < 24.9:
    print("Durum : Normal Kilolu")
elif 24.9 < bmi < 29.9:
    print("Durum : Fazla Kilolu")
else:
    print("Durum : Obez")