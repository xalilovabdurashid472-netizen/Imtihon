mahsulotlar = [
    ["Olma", 8000, 12],
    ["Non", 4000, 20],
    ["Sut", 14000, 5]
]
with open("products.csv","w")as file:
    file.write("nom,narxi,soni\n")
    for mahsulot in mahsulotlar:
        file.write(f"{mahsulot[0]},{mahsulot[1]},{mahsulot[2]}\n")