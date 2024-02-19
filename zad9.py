import random

def gra_w_zgadywanie():
    dolny_zakres = int(input("Podaj dolny zakres losowania: "))
    gorny_zakres = int(input("Podaj górny zakres losowania: "))
    
    tajna_liczba = random.randint(dolny_zakres, gorny_zakres)
    proby = 3
    
    while proby > 0:
        zgadnij = int(input(f"Zgadnij liczbę ({proby} próby): "))
        
        if zgadnij == tajna_liczba:
            print("Gratulacje! Zgadłeś liczbę.")
            break
        elif zgadnij < tajna_liczba:
            print("Za mało! Spróbuj ponownie.")
        else:
            print("Za dużo! Spróbuj ponownie.")
        
        proby -= 1
    
    if proby == 0:
        print(f"Przykro mi, skończyły Ci się próby. Prawidłowa liczba to {tajna_liczba}.")

gra_w_zgadywanie()