class ValueReader:
    def __init__(self, fp):
        self.fp = fp
    
    @staticmethod
    def _convert_to_byte_array(value):
        """ Convert an integer to a list of bytes """

        result = []
        while value != 0:
            byte = value & 0xff
            value >>= 8
            result.append(byte)
        
        return result[::-1]


    @staticmethod
    def _pad(value, width):
        """ Pad out a value to a width and convert it to a byte string """

        value = ValueReader._convert_to_byte_array(value)
        while len(value) != width:
            value.insert(0, 0)
        
        # Convert the integers to chars
        result = [chr(i) for i in value]
        result = ''.join(result)
        
        return result.encode()
    
    def _read(self, width):
        """ Read bytes and convert it to a number """

        result = 0

        for shift in range(width):
            byte = self.fp.read(1)
            byte <<= shift * 8
            result |= byte
    
    def read_byte(self):
        """ Read next byte as a number """

        return self._read(1)
    
    def read_short(self):
        """ Read next short as a number """

        return self._read(2)
    
    def read_integer(self):
        """ Read next integer as a number """

        return self._read(4)
    
    def read_long(self):
        """ Read next long as a number """

        return self._read(8)
    

    def write_byte(self, value):
        """ Convert a value to a byte and write it to the file """

        value = self._pad(value, 1)
        self.fp.write(value)
    
    def write_short(self, value):
        """ Convert a value to a short and write it to the file """

        value = self._pad(value, 2)
        self.fp.write(value)
    
    def write_integer(self, value):
        """ Convert a value to an integer and write it to the file """

        value = self._pad(value, 4)
        self.fp.write(value)
    
    def write_long(self, value):
        """ Convert a value to a long and write it to the file """

        value = self._pad(value, 8)
        self.fp.write(value)