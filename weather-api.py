import requests

url = 'https://api.darksky.net/forecast/<api>/34.0575651,-117.820741'

json_data = requests.get(url).json()
json_data = requests.get(url).json()

# pull current and get current temp
text = "Current Weather at Cal Poly: "
get_all = json_data['currently']
temp = get_all.get('temperature')

# pull daily to obtain min and max
get_daily_data = json_data['daily']['data']

print(text)
print("Temp: ", temp, '˚F')
print("High: ", '˚F')
print(get_daily_data)
