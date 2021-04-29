### English ###

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
başlık = "Hesap Makinesi / Calculator"
print(başlık.center(23))
print("")

print("Dil Seçin / Select Language")

print("")

print("1.Türkçe")

print("")

print("2.English")

print("")

dil = int(input(""))

if dil == 1:
    print("")

    sayi1 = int(input("Birinci Sayıyı Giriniz: "))

    print("")

    sayi2 = int(input("İkinci Sayıyı Giriniz: "))

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
        sys.exit(1)     

    print("")

    kapat = input("Kapatmak için herhangi bir tuşa basın")

elif dil == 2:
    print("")

    number1 = int(input("Enter The First Number: "))

    print("")

    number2 = int(input("Enter The Second Number: "))

    print("")

    print("What do you want to do?")
    print("===========================")
    print("1.addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")

    print("")

    Selection = int(input("Select: "))

    print("")

    if Selection == 1:
        print(number1,"+",number2,"=", topla(number1,number2))
    elif Selection == 2:
        print(number1,"-",number2,"=", çıkarma(number1,number2))
    elif Selection == 3:
        print(number1,"*",number2,"=", çarpma(number1,number2))    
    elif Selection == 4:
        print(number1,"/",number2,"=", bölme(number1,number2))
    else:
        print("Invalid Value")   
        sys.exit(1)     

    print("")

    kapat = input("For exit press any button")