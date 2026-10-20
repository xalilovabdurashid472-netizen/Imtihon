from matplotlib import pyplot
kunlar = ["Du", "Se", "Cho", "Pay", "Ju", "Sha", "Yak"]
daromad = [120, 150, 100, 180, 200, 240, 210]
pyplot.plot(kunlar,daromad,marker="o")
pyplot.grid(True)
pyplot.legend()
pyplot.title("Bir haftalik daromad")
pyplot.xlabel("Kunlar")
pyplot.ylabel("Daromad")
pyplot.savefig("daromad.png")