from sensor import Sensor
class TempSensor(Sensor):
        __unit: str ="C"
        R_MIN: int = -50
        R_MAX: int = 50
        def __init__(self, id, location) -> None:
                super().__init__(id, location)
        def displayTemp(self) -> float:
                temperature = super().readRaw(self.R_MIN, self.R_MAX)
                # print(f"Temperature: {temperature} {self.__unit}")
                return temperature, self.__unit
