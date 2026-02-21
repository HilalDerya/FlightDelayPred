import pandas as pd 
import requests
from time import sleep

coords_df=pd.read_csv('')

coords_df = coords_df.dropna()

print(f"{len(coords_df)} havalimanı için hava durumu çekilecek")

weather_data_list = []

for index, row in coords_df.iterrows():
    airport = row['airport_code']
    lat = row['latitude']
    lon =row['longitude']

    url="https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": "2022-01-01",
        "end_date": "2022-12-31",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max,weathercode"
    }

    try:
        response = requests.get(url,params=params)
        weather = response.json()

        for i, date in enumerate(weather['daily']['time']):
            weather_data_list.append({
                'airport_code': airport,
                'date': date,
                'temp_max': weather['daily']['temperature_2m_max'][i],
                'temp_min': weather['daily']['temperature_2m_min'][i],
                'precipitation': weather['daily']['precipitation_sum'][i],
                'windspeed_max': weather['daily']['windspeed_10m_max'][i],
                'weather_code': weather['daily']['weathercode'][i]
            })
        print(f"{airport} ✓ ({index+1}/{len(coords_df)})")
        sleep(1) 
    except Exception as e:
        print(f"{airport} Hata: {e}")

weather_df = pd.DataFrame(weather_data_list)
weather_df.to_csv('weather_data_2022.csv', index=False)
print(f"\n✓ weather_data_2022.csv oluşturuldu! ({len(weather_df)} satır)")