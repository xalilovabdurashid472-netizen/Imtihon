talabalar = [("Ali", 85), ("Malika", 95), ("Vali", 78)]
alohida = sorted(
talabalar,
 key=lambda talaba: talaba[1],
 reverse=True)

print(alohida)