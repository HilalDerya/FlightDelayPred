import pandas as pd
import requests
from time import sleep

airports=pd.read_csv('')

coord_list = []

for airport_code in airports['airport_code']:
    url =f"https://nominatim.openstreetmap.org/search"
    params={
        'q': f"{airport_code} airport",
        'format': 'json',
        'limit': 1
    }
    headers = {'User-Agent': 'FlightDelayPrediction/1.0'}

    try:
        response = requests.get(url, params=params, headers=headers)
        data =response.json()

        if data:
            coord_list.append({
                'airport_code':airport_code,
                'latitude':float(data[0]['lat']),
                'longitude':float(data[0]['lon'])
            })
            print(f"{airport_code}: {data[0]['lat']}, {data[0]['lon']}")
        else:
            print(f"{airport_code}: Bulunamadı!")
            coord_list.append({
                'airport_code': airport_code,
                'latitude': None,
                'longitude': None
            })
    except:
        print(f"{airport_code}:Hata!")
        coord_list.append({
            'airport_code':airport_code,
            'lantitude':None,
            'longitude':None
        })
    sleep(1)
coords_df = pd.DataFrame(coord_list)
coords_df.to_csv('airport_coordinates.csv', index=False)
print("\nairport_coordinates.csv oluşturuldu!")