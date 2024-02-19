from datetime import datetime, timedelta

def obliczenia_daty():
    # a.
    rok = int(input("Podaj rok: "))
    miesiac = int(input("Podaj miesiąc: "))
    dzien = int(input("Podaj dzień: "))

    data = datetime(rok, miesiac, dzien)
    dzien_roku = data.timetuple().tm_yday
    print(f"a. Dzień roku: {dzien_roku}")

    # b.
    numer_tygodnia = data.strftime("%U")
    print(f"b. Numer tygodnia: {numer_tygodnia}")

    # c.
    dwa_tygodnie_przed = data - timedelta(days=14)
    dwa_tygodnie_po = data + timedelta(days=14)
    print(f"c. Data dwa tygodnie przed: {dwa_tygodnie_przed.strftime('%Y-%m-%d')}")
    print(f"   Data dwa tygodnie po: {dwa_tygodnie_po.strftime('%Y-%m-%d')}")

    # d.
    dni_do_niedzieli = (6 - data.weekday() + 7) % 7
    najblizsza_niedziela = data + timedelta(days=dni_do_niedzieli)
    print(f"d. Najbliższa niedziela: {najblizsza_niedziela.strftime('%Y-%m-%d')}")

    # e.
    czas_unixowy = int((data - datetime(1970, 1, 1)).total_seconds())
    print(f"e. Czas unixowy bieżącej godziny w podanym dniu: {czas_unixowy}")

# Wywołanie funkcji
obliczenia_daty()