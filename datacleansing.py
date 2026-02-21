import pandas as pd

data = pd.read_csv('')
flight_date = data['FlightDate'].unique()
arrtime = data['ArrTime']
month = data['Month']
year = data['Year']
origin_airports = data['Origin'].unique()
dest_airports = data['Dest'].unique()
all_airports = list(set(list(origin_airports) + list(dest_airports)))

print(f"Toplam {len(all_airports)} farklı havalimanı var")
print("İlk 10 havalimanı:", all_airports[:10])
print(f"Farklı tarih: {len(flight_date)}")
print(f"Farklı havalimanı: {len(all_airports)}")
print(f"Maksimum API: {len(flight_date)} x {len(all_airports)} = {len(flight_date) * len(all_airports)}")

pd.DataFrame({'airport_code': all_airports}).to_csv('airports_list.csv', index=False)

unique_combinations = data[['FlightDate', 'Origin']].drop_duplicates()
print(f"Toplam {len(unique_combinations)} API çağrısı gerekiyor")