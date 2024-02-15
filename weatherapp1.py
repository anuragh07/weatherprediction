OIKO_KEY = '05453b5e7ad448ada150f4ce35c9057b'
URL = 'https://api.oikolab.com/weather'

import json
import requests
import pandas as pd

def get_temperature(start_date, end_date, city):

    resp = requests.get(URL,
        params = {
            'param': ['temperature'],
            'start': start_date,
            'location': city,
            'end': end_date,
            'api-key': OIKO_KEY,
            'freq': 'D'
            }
    )
    weather_data = json.loads(resp.json()['data'])
    df = pd.DataFrame(index=pd.to_datetime(weather_data['index'],unit='s'),
                    data=weather_data['data'],
                    columns=weather_data['columns'])

    temperature = df.iloc[0,4]        

    return int(temperature)


city = input()
date = input()
temperature = get_temperature(date, date, city)


print(f'Temperature for {city} on {date} = {temperature}C')