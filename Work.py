from pyowm.owm import OWM
import pyowm

owm=pyowm.OWM('c5d07c67db6d86d9b0dcfd63fc9952bb')
obs=owm.weather_manager().weather_at_place('London, GB')

print(w)

