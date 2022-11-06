# Модуль 3: UI

import data_provider as prov
import logger as log

def temperature_view(sensor):
    data = prov.get_temperature(sensor)
    log.temperature_logger(data)
    return data
    
def pressure_view(sensor):
    data = prov.get_preassure(sensor)
    log.pressure_logger(data)
    return data

def wind_speed_view(sensor):
    data = prov.get_wind_speed(sensor)
    log.wind_speed_logger(data)
    return data