import requests
url='https://api.darksky.net/forecast/<api>/34.0575651,-117.820741'
json_data = requests.get(url).json()
json_data = requests.get(url).json()
text = "Current Weather at Cal Poly: "
# pull current and get current temp
get_all = json_data['currently']
temp = get_all.get('temperature')
# pull daily to obtain min and max
get_daily_data = json_data['daily']['data']
print(text)
print ("Temp: ", temp)
print("High: ", )
print(get_daily_data)
