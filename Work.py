import requests
from pyowm.owm import OWM
import pyowm
print('Good morning, Robert. \nHere is your Daily Feed for today:')
print('The current weather is: ')
owm = OWM('c5d07c67db6d86d9b0dcfd63fc9952bb')
mgr=owm.weather_manager()
EPL=31.8001
EPH=-106.2005
observation=mgr.weather_at_coords(EPL,EPH).weather
temperature=observation.temperature('fahrenheit')
print(temperature)
question1=input('Would you like to know a useful tip?\n' + 'Type y/n\n')
if question1=='y':
    print('test1')
elif question1=='n':
    print('test2')
else:
    print('test 3')
