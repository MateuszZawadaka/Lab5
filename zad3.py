import time

uzytkownik_czas = int(input("Podaj czas w sekundach: "))
while uzytkownik_czas > 0:
    print("Pozostało sekund:", uzytkownik_czas)
    time.sleep(1)
    uzytkownik_czas -= 1
print("Czas minął!")