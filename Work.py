import requests
from pyowm.owm import OWM
import pyowm
#==========================================================================================================
#Weather
print('Good morning, Robert. \nHere is your Daily Feed for today:')
print('The current weather is: ')
owm = OWM('c5d07c67db6d86d9b0dcfd63fc9952bb')
mgr=owm.weather_manager()
EPL=31.8001
EPH=-106.2005
observation=mgr.weather_at_coords(EPL,EPH).weather
temperature=observation.temperature('fahrenheit')
print(temperature)
#==========================================================================================================
#Livin' Off the Land
wisdomlist = []
question1=input('Would you like to know a useful tip?\n' + 'Type y/n\n')
if question1=='y':
    print('test1')
elif question1=='n':
    print('Have a good day!')
else:
    print(str(question1) + ' is not recognized. \n' + 'Please type y/n')
