import json
with open("products.json","r")as file:
    mahsulotlar=json.load(file)
    nom=input("Mahsulot nomi: ")
    narx=int(input("Yangi narx: "))
    topildi=False
    for mahsulot in mahsulotlar:
        if mahsulot["nom"]==nom:
            mahsulot["narx"]=narx
            topildi=True
            break
    if topildi:
        with open("products.json","w")as file:
            json.dump(mahsulotlar,file)
            print("Mahsulot yangilandi.")
    else:
            print("Bunday mahsulot mavjud emas.")