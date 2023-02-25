from lib_sensor import SensorLIB
from abc import abstractmethod, ABC
class Sensor(ABC):
        id: str
        location: str
        @abstractmethod
        def __init__(self,  id, location) -> None:
                self.id = id
                self.location = location
        def getId(self) -> str:
                return self.id
        def printLocation(self) -> None:
                print(f"Location: {self.location}")
                return None
        def printReading(self) -> None:
                raw = SensorLIB(3,2)
                value = raw.readAnalog()
                print(f"Raw sensor value: {value}")
                return None
        def readRaw(self, min, max)-> int:
                raw_value = SensorLIB(2, 1)
                value = raw_value.readAnalog()
                zero_to_one = float(value) / 65535
                wanted_range = float(abs(max - min))
                converted_value = zero_to_one * wanted_range + min
                return round(converted_value, 2)
