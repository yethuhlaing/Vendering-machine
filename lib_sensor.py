from random import random

class SensorLIB:
    pin_signal_in: int
    pin_signal_out: int
    __freq: int
    __min: int = 0
    __max: int = 65535
    __analogOut: int
    __digitalOut: int
    __data_packet: str
    _SEG_CHAR = {
        "1": "0b0110000",
        "2": "0b1101101",
        "3": "0b1111001",
        "4": "0b0110011",
        "5": "0b1011011",
        "6": "0b1011111",
        "7": "0b1110000",
        "8": "0b1111111",
        "9": "0b1110011",
        "0": "0b1111110",
        "empty": "0b0000000"
    }
    """
    This dictionary consists of key values for displaying values on the screen. Last "parity bit" is missing.
    https://docs.python.org/3/reference/lexical_analysis.html#integer-literals
    key => bininteger
    """
    def __init__(self, pin_out: int = -1, pin_in: int = -1, freq: int = -1) -> None:
        """
        To use this sensor library, you may create object from it. Assigning pins is required for every communication.
        Assigning frequency is required only for the serial bus communication.

        Params
        ----------
            pin_out: can be any positive integer. Represents one communication pin
            pin_in: can be any positive integer. Represents one communication pin
            freq: can be any positive integer. Represents frequency in serial bus
                commonly known baud rates: 110, 150, 300, 600, 900, 1200, 2400, 4800, 9600, 14400, 19200, 38400, 57800...

        Returns
        ----------
            None
        """
        self.pin_signal_out = pin_out
        self.pin_signal_in = pin_in
        self.__analogBuffer = 0
        self.__freq = freq
        return None
    def readAnalog(self) -> int:
        """
        This method replicates reading analog signal to digital (ADC).
        Computers usually represent these signals in bits, in
        this case a 16-bit value (0-65535) will be returned.

        Returns
        ----------
            16-bit value as an integer.

        Exceptions
        ----------
            If the signal pins aren't assigned, this method will throw an exception.
        """
        value = -1
        if (self.pin_signal_in >= 0) and (self.pin_signal_out >= 0):
            range = abs(self.__max - self.__min)
            value = int((random() * range) + self.__min)
        else:
            raise Exception("Assign the pins first.")
        return value
    def readDigital(self) -> int:
        """
        This method replicates reading digital signals.
        Digital IO is representable in HIGH (1) state or LOW (0) state.

        Returns
        ----------
            HIGH (1) or LOW (1) as an integer.
            
        Exceptions
        ----------
            If the signal pins aren't assigned, this method will throw an exception.
        """
        value = -1
        if (self.pin_signal_in >= 0) and (self.pin_signal_out >= 0):
            if random() >= 0.5:
                value = 1
            else:
                value = 0
        else:
            raise Exception("Assign the pins first.")
        return value
    def writeAnalog(self, value: int) -> None:
        """
        This method is similar to "readAnalog", but instead it will take the 
        16-bit value in and pushes it out as analog signal (DAC).
        
        Returns
        ----------
            None
        
        Exceptions
        ----------
            If the signal pins aren't assigned, this method will throw an exception.
        """
        if (self.pin_signal_in >= 0) and (self.pin_signal_out >= 0):
            self.__analogOut = 0
        else:
            raise Exception("Assign the pins first.")
        return None
    def writeDigital(self, high: bool) -> None:
        """
        This method is similar to "readDigital", but instead it will take the 
        param "high" and pushes it out as digital signal (HIGH or LOW).

        Returns
        ---------
            None
        
        Exceptions
        ---------
            If the signal pins aren't assigned, this method will throw an exception.
        """
        if (self.pin_signal_in >= 0) and (self.pin_signal_out >= 0):
            if high == True:
                self.__digitalOut = 1
            else:
                self.__digitalOut = 0
        else:
            raise Exception("Assign the pins first.")
        return None
    def _writeSerial(self, packet: str, debug = False) -> None:
        """
        This method writes packets to the serial bus.

        (Use this method to send a message for the "7-segment" display in the W4_T5)

        Parameters
        ---------
            packet: str
                Or "frame" is considered as one "message" in serial bus. One packet in this case is  8-bits long, where
                1st to 7th bits are data bits
                8th bit is parity bit of the datas

                Construct the following "frame" using string representation e.g. "0b10101010"
                            |---------|---------|---------|---------|---------|---------|---------|------------|
                bit         |    1    |    2    |    3    |    4    |    5    |    6    |    7    |     8      |
                            |---------|---------|---------|---------|---------|---------|---------|------------|
                description:| data[0] | data[1] | data[2] | data[3] | data[4] | data[5] | data[6] |   parity   |
                            |---------|---------|---------|---------|---------|---------|---------|------------|
                example:    |   0|1   |   0|1   |   0|1   |   0|1   |   0|1   |   0|1   |   0|1   |odd=1,even=0|
                            |---------|---------|---------|---------|---------|---------|---------|------------|
            debug: bool
                Set debug parameter to `True` for a debug message. It will show the 7-segments, which would light up.
            

        Returns
        ---------
            None , but there will be printed rows as result
        """
        if (self.pin_signal_in >= 0) and (self.pin_signal_out >= 0) and (self.__freq >= -1):
            try:
                # print(packet)
                if isinstance(packet, int):
                    print("Warning! change the datatype from integer to string (use Python binary literal).")
                    binary_str = bin(packet)
                    if len(binary_str) < 8:
                        missing_bits = 8 - len(binary_str)
                        binary_str += missing_bits * "0"
                        # print("bin_str: " + binary_str + " len: " + str(len(binary_str)))
                    self.__data_packet = binary_str
                elif isinstance(packet, str):
                    if len(packet) != 10:
                        raise Exception("Packet needs to be 8-bit long and has to contain binary literal '0b'")
                    elif (packet[0] != '0') and (packet[1] != 'b' or packet[1] != 'B'):
                        raise Exception("Unable to parse binary literal")
                    self.__data_packet = packet
                else:
                    raise Exception("Couldn't convert the packet '{}' into suitable 8-bit format for the serial bus".format(packet))
                if debug == True:
                    # print("packet: " + self.__data_packet)
                    vision: str = "  " # "  __\n /_/\n/_/ "
                    bits = self.__data_packet.replace("0b","").replace("0B","")
                    vision += "__\n" if bits[0] == "1" else "  \n"
                    vision += " /" if bits[5] == "1" else "  "
                    vision += "_" if bits[6] == "1" else " "
                    vision += "/\n" if bits[1] == "1" else " \n"
                    vision += "/" if bits[4] == "1" else " "
                    vision += "_" if bits[3] == "1" else " "
                    vision += "/\n" if bits[2] == "1" else " \n"
                    print(vision)
                    datas = bits[:-1]
                    # print("datas: " + datas)
                    parity_bit = str(datas.count("1") % 2)
                    parityOK = "OK" if parity_bit == bits[7] else "not OK"
                    # print("Parity: " + parityOK)
            except Exception as err:
                raise Exception(err)
        else:
            raise Exception("Assign the pins or set the frequency")
        return None

