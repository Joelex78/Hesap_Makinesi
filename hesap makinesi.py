import sys

# Toplama İşlemi
def topla(x,y):
    return x + y

# Çıkarma İşlemi
def çıkarma(x,y):
    return x - y

# Çarpma İşlemi
def çarpma(x,y):
    return x * y

# Bölme İşlemi
def bölme(x,y):
    return x / y
#############################################################################################
başlık = "Hesap Makinesi"
print(başlık.center(23))
print("")
print("Ne yapmak istiyorsunuz?")
print("===========================")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")

print("")

Seçim = int(input("Seçiniz: "))

print("")

if Seçim > 4:
    print("Geçersiz İşlem")
    sys.exit(1)

print("")

sayi1 = int(input("Birinci Sayıyı Giriniz: "))

print("")

sayi2 = int(input("İkinci Sayıyı Giriniz: "))

print("")

if Seçim == 1:
    print(sayi1,"+",sayi2,"=", topla(sayi1,sayi2))
elif Seçim == 2:
    print(sayi1,"-",sayi2,"=", çıkarma(sayi1,sayi2))
elif Seçim == 3:
    print(sayi1,"*",sayi2,"=", çarpma(sayi1,sayi2))    
elif Seçim == 4:
    print(sayi1,"/",sayi2,"=", bölme(sayi1,sayi2))
else:
    print("Geçersiz Sayı")        

print("")

kapat = input("Kapatmak için herhangi bir tuşa basın")