from pyowm.owm import OWM
import pyowm

owm = OWM('c5d07c67db6d86d9b0dcfd63fc9952bb')
mgr=owm.weather_manager()
EPL=31.8001
EPH=-106.2005
observation=mgr.weather_at_coords(EPL,EPH).weather
temperature=observation.temperature('fahrenheit')
print(temperature)


