import math

dlugosc_krotki = 10

przedzial_uzytkownika = int(input("Podaj zakres losowania liczb: "))

losowa_krotka = tuple(random.randint(1, przedzial_uzytkownika) for _ in range(dlugosc_krotki))

srednia_geometryczna = math.exp(sum(math.log(num) for num in losowa_krotka) / len(losowa_krotka))

print("Losowa krotka:", losowa_krotka)
print("Średnia geometryczna krotki:", srednia_geometryczna)