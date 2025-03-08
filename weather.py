import json
import requests

city = 'Perm'
key = '1959ab8d4e86e0a1f706f7b74af6cdf4'
response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}')
result = json.loads(response.text)

temperature = int((int(result['main']['temp']) - 273.15))
humidity = result['main']['humidity']
pressure = int(int(result['main']['pressure']) * 0.75)

print(f'Температура: {temperature}°C')
print(f'Влажность: {humidity}%')
print(f'Давление: {pressure} мм.рт.ст.')
