from sensor import Sensor
class HumSensor(Sensor):
        __unit: str = "%"
        R_MIN: int = 0
        R_MAX: int = 99
        def __init__(self, id, location) -> None:
                super().__init__(id, location)
        def displayHum(self) -> float:
                humidity = super().readRaw(self.R_MIN, self.R_MAX)
                # print(f"Humidity: {humidity} {self.__unit}")
                return humidity, self.__unit
