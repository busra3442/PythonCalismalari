def c_to_f(celcius):
    return (celcius * 9/5) + 32
def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9


print("**Sıcaklık Birim Dönüştürücü**\n")
print("1 - Celcius'tan Fahrenheit'e dönüştürür.")
print("2 - Fahrenheit'ten Celcius'a dönüştürür.")

secim = int(input("Lütfen yapmak istediğiniz işlemi seçiniz: "))

if secim == 1:
    celcius = float(input("Lütfen Celcius Cinsinden Sıcaklık Değerini Giriniz: "))
    fahrenheit = c_to_f(celcius)
    print(f"{celcius}°C = {fahrenheit}°F ")

elif secim == 2:
    fahrenheit = float(input("Lütfen Fahrenheit Cinsinden Sıcaklık Değerini Giriniz: "))
    celcius = f_to_c(fahrenheit)
    print(f"{fahrenheit}°F = {celcius}°C ")

else:
    print("Geçersiz seçim yaptınız lütfen tekrar deneyiniz!")