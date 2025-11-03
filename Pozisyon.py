import time

name = ("Kimyasal Mekanik Pipet Pozisyonu Hesaplayıcı")

print(name)
time.sleep(2)

print("formül")
time.sleep(1)
print("Kramayerin alacağı yol = çarkın tur sayısı * [çarkın diş sayısı * (kramayer adımı + kramayer diş kalınlığı)]")
time.sleep(1)
print("h=N*[D*(a+K)]")
time.sleep(2)

print("sözlük")
time.sleep(1)
print("h = Kramayerin alacağı yol")
time.sleep(0.30)
print("N = Çarkın tur sayısı")
time.sleep(0.30)
print("D = Çarkın diş sayısı")
time.sleep(0.30)
print("a = Kramayer adımı")
time.sleep(0.30)
print("K = Kramayer diş kalınlığı")
time.sleep(2)

print("HESAPLAMA")
time.sleep(1)

h = ("Hesaplanıyor...")

# Fonksiyon: geçerli sayı girene kadar sor
def get_input(prompt):
    while True:
        value = input(prompt)
        if value.strip() == "":
            print("Giriş boş olamaz! Lütfen bir sayı girin.")
            continue
        try:
            return int(value)
        except ValueError:
            print("Geçersiz giriş! Lütfen geçerli bir sayı girin.")

N = get_input("N değerini giriniz: ")
D = get_input("D değerini giriniz: ")
a = get_input("a değerini giriniz: ")
K = get_input("K değerini giriniz: ")

time.sleep(0.30)
print("Değerleriniz kaydediliyor...")
time.sleep(3)

info = [h, N, D, a, K]
print("Değerleriniz: h:{} N:{} D:{} a:{} K:{}".format(info[0], info[1], info[2], info[3], info[4]))
time.sleep(2)
print("Formülünüz: h={}*[{}*({}+{})]".format(info[1], info[2], info[3], info[4]))
time.sleep(2)

result = N * (D * (a + K))
result_data = [result]

print("Sonucunuz hesaplanıyor...")
time.sleep(2)
print("h değeriniz = {}".format(result_data[0]))
time.sleep(1)
son = input("Kapatmak için Enter'a basın!")
