mahsulotlar = {
    "non": 4000,
    "sut": 12000,
    "olma": 8000
}
nom=input("Mahsulot nomini kiriting: ")
narx=int(input("Mahsulot narxini kiriting: "))
if nom in mahsulotlar:
    mahsulotlar[nom] = narx
    print("Narx yangilandi.")
    print(mahsulotlar)
else:
    print("Bunday mahsulot mavjud emas.")