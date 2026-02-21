import pandas as pd

flights = pd.read_csv('')
weather = pd.read_csv('weather_data_2022.csv')

print(f"Uçuş verisi: {len(flights)} satır")
print(f"Hava durumu: {len(weather)} satır")

final_data = flights.merge(
    weather,
    left_on=['FlightDate', 'Origin'],
    right_on=['date', 'airport_code'],
    how='left'
)

print(f"Birleştirilmiş veri: {len(final_data)} satır")
print(f"Hava durumu bulunan: {final_data['temp_max'].notna().sum()} satır")

final_data = final_data.drop(['date', 'airport_code'], axis=1)

final_data.to_csv('flights_with_weather_2022.csv', index=False)
print("\n✓ flights_with_weather_2022.csv oluşturuldu!")