import random

# a.
szczesliwy_numer = random.randint(1, 100)
print("Szczęśliwy numer:", szczesliwy_numer)

# b.
lata_urodzenia = [random.randint(1980, 2000) for _ in range(10)]
szczesliwy_rocznik = random.choice(lata_urodzenia)
print("Szczęśliwy rocznik:", szczesliwy_rocznik)

# c.
lotto_liczby = random.sample(range(1, 50), 6)
print("Liczby lotto:", lotto_liczby)