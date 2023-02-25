from lib_sensor import SensorLIB
class SegmentDisplay(SensorLIB):
        def __init__(self, pin_out: int = -1, pin_in: int = -1, freq: int = -1) -> None:
                super().__init__(pin_out, pin_in, freq)
        def  showOnDisplay(self, symbol: int) -> None:
                self.first_binary: str
                self.second_binary: str
                if len(str(symbol)) == 2:
                        self.first_digit = int(str(symbol)[0])
                        self.second_digit = int(str(symbol)[1:])
                        for key ,value in self._SEG_CHAR.items():
                                if str(self.first_digit) == key:
                                        self.first_binary = value
                                        parity_bit = str(value.count("1") % 2)
                                        self.first_binary += parity_bit
                                if str(self.second_digit) == key:
                                        self.second_binary = value
                                        parity_bit = str(value.count("1") % 2)
                                        self.second_binary += parity_bit
                        super()._writeSerial(self.first_binary, debug=True)
                        super()._writeSerial(self.second_binary, debug=True)
                else:
                        self.first_digit = str(symbol)
                        for key, value in self._SEG_CHAR.items():
                            if str(self.first_digit) == key:
                                self.first_binary = value
                                parity_bit = str(value.count("1") % 2)
                                self.first_binary += parity_bit
                        super()._writeSerial(self.first_binary, debug=True)

                
