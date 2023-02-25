from sensor import Sensor
from lib_sensor import SensorLIB
from temp_sensor import TempSensor
from hum_sensor import HumSensor

class MultiSensor(Sensor):
        def __init__(self, id, location) -> None:
                super().__init__(id, location)
                self.t_sensor = TempSensor(id, location)
                self.h_sensor = HumSensor(id, location)
        def printReading(self) -> float:
                temp, unit_temp = self.t_sensor.displayTemp()
                hum, unit_hum = self.h_sensor.displayHum()
                print(f"Measurements - Temp: {temp} {unit_temp}, Hum: {hum} {unit_hum}\n")
                return hum
