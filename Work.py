from pyowm.owm import OWM
import pyowm

owm = OWM('c5d07c67db6d86d9b0dcfd63fc9952bb')
mgr=owm.weather_manager()
observation=mgr.weather_at_place('London,GB').weather
temp_dict_kelvin=observation.temperature('fahrenheit')
print(temp_dict_kelvin)


