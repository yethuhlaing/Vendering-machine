from sensor import Sensor
from temp_sensor import TempSensor
from hum_sensor import HumSensor
from multi_sensor import MultiSensor
from segment_display import SegmentDisplay
class Main:
        def __init__(self) -> None:
                print("Vending machine booting...\n")
                # sensor2 = MultiSensor("ab-cd-ef-12-34-57", "Lappeenranta")
                # sensor2.printLocation()
                # sensor2.printReading()
                sensor = MultiSensor("ab-cd-ef-12-34-56", "internal")
                print("Component group: 1")
                sensor.printLocation()
                humidity = sensor.printReading()
                # Show the digit on 7 segment Display
                sensor_display = SegmentDisplay(1,1,1)
                sensor_display.showOnDisplay(int(humidity))
                print("Vending machine shutting down.")
if __name__ == "__main__":
        app = Main()