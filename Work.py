import requests
import pyowm
print('Good morning, Robert. \nHere is your Daily Feed for today:')
print('The current weather is: ')
APIKEY= 'c5d07c67db6d86d9b0dcfd63fc9952bb'
OpenWMap=pyowm.OWM(APIKEY)
Weather=OpenWMap.weather_at_place('London')
Data=Weather.get_weather()
temp = Data.get_temperature(unit='celsius')      # get current temparature in celsius
print ("Average Temp. Currently ", temp['temp']) # get avg. tmp
print ("Max Temp. Currently ", temp['temp_max']) # get max tmp
print ("Min Temp. Currently ", temp['temp_min']) # get min tmp>>