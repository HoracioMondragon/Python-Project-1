import requests

url = 'https://api.darksky.net/forecast/bdd13177f9f4a33b5211a473d9338e55/34.0575651,-117.820741'

jsonData = requests.get(url).json()

# pull current and get current temp
text = "Current Weather at Cal Poly: "
getAll = jsonData['currently']
temp = getAll.get('temperature')

# pull daily to obtain min and max
getDailyData = jsonData['daily']['data']
tempHigh = getDailyData[0]['temperatureHigh']
tempLow = getDailyData[0]['temperatureLow']

print(text)
print("Temp: ", int(temp), '˚F')
print("")
print("High: ", int(tempHigh), '˚F')
print("Low: ", int(tempLow), '˚F')

