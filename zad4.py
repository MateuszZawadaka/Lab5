from datetime import datetime

data_ostatnich_laboratoriow = datetime(2024, 2,26)
data_kolokwium = datetime(2024, 2, 12)

aktualna_data = datetime.now()
dni_od_laboratoriow = (aktualna_data - data_ostatnich_laboratoriow).days
dni_do_kolokwium = (data_kolokwium - aktualna_data).days

print(f"Dni od ostatnich laboratoriów: {dni_od_laboratoriow} dni")
print(f"Dni do kolokwium: {dni_do_kolokwium} dni")