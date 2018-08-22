import requests
url='https://api.darksky.net/forecast/<api>/34.0575651,-117.820741'
json_data = requests.get(url).json()
# pull current and get current temp
get_all = json_data['currently']
temp = get_all.get('temperature')
icon = get_all.get('icon')
# pull daily to obtain min and max
get_daily_data = json_data['daily']['data']
tempHigh = get_daily_data[0]['temperatureHigh']
tempLow = get_daily_data[0]['temperatureLow']
summary = get_daily_data[0]['summary']
precip = get_daily_data[0]['precipProbability']
precip = get_daily_data[0]['precipProbability']
print("Current Weather at Cal Poly: ")
print("Temp:", int(temp), "˚F")
print("High:", int(tempHigh), "˚F")
print("Low: ", int(tempLow), "˚F")
print("Chance of Rain: ", int(precip), "%")
print(summary)
#print(get_daily_data)
