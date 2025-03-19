import holidayapi

KEY = '08b6d1d3-a60d-4b56-a898-e24e2e705471'
hapi = holidayapi.v1(KEY)
holidays = hapi.holidays({
    'country': 'RU',
    'year': '2024',
    'month': '8'
})

ans = holidays['holidays']
#print(ans)

for i in range(6):
    print(f'Праздник: {ans[i]["name"]} '
          f'| Дата: {ans[i]["date"]} '
          f'| День недели: {ans[i]["weekday"]["date"]["name"]}')
