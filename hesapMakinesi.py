
    
sayi1 = int(input("Lütfen bir sayı giriniz: "))
islem = input("Lütfen (+, -, /, *) işlemlerinden birini seçin: ") 
if islem not in ["+", "-", "/", "*"]:
    print("Geçersiz işlem!")
else:
  sayi2 = int(input("Lütfen bir sayı giriniz: "))



def topla(sayi1,sayi2):
        return sayi1+sayi2
     
def cikart(sayi1,sayi2):
        return sayi1-sayi2
     
def carp(sayi1,sayi2):
        return sayi1*sayi2

def bol(sayi1,sayi2):
        return sayi1/sayi2 if sayi2 != 0 else " Hata: Bölme işlemi için ikinci sayı 0 olamaz! "

if islem == "+":
       print(f"Sonuç: {topla(sayi1,sayi2)}")
elif islem == "-":
       print(f"Sonuç: {cikart(sayi1,sayi2)}")
elif islem == "*":
       print(f"Sonuç: {carp(sayi1,sayi2)}")
elif islem == "/":
       print(f"Sonuç: {bol(sayi1,sayi2)}")








             
      
     
          




  