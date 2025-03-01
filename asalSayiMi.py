def asalSayi_Mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, sayi):
         if sayi % i == 0:
            return False
    return True

sayi = int(input("Bir sayı girin: "))
if asalSayi_Mi(sayi):
    print(f"{sayi} bir asal sayıdır.")
else:
    print(f"{sayi} bir asal sayı değildir.")
