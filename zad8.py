import math

def pole_trojkata(a, b, kat):
    if a <= 0 or b <= 0 or kat <= 0 or kat >= 180:
        return "Błędne dane. Podaj poprawne długości boków i kąt."
    
    kat_radiany = math.radians(kat)
    pole = 0.5 * a * b * math.sin(kat_radiany)
    return pole

# Przykładowe użycie:
bok1 = float(input("Podaj długość pierwszego boku: "))
bok2 = float(input("Podaj długość drugiego boku: "))
kat_miedzy_bokami = float(input("Podaj szerokość kąta ostrym pomiędzy bokami (w stopniach): "))

wynik = pole_trojkata(bok1, bok2, kat_miedzy_bokami)
print("Pole trójkąta:", wynik)