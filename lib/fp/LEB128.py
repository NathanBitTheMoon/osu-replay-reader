class LEB128:
    def __init__(self, fp):
        """ An object used for encoding and decoding LEB128 values from a file object """

        self.fp = fp
    
    def _seek_end(self):
        """ Seek for the end of the end of the LEB128 value """

        seek = 0
        while True:
            value = self.fp.read(1)
            seek += 1
            # Check if the high order bit is set
            if value & 0x80 == 0:
                break
        # Return to where the reading started
        self.fp.seek(seek * -1, 1)
        return seek
    
    @staticmethod
    def decode(values):
        """ Convert a byte array to an integer """

        result = 0
        shift = 0

        for byte in values:
            result |= (byte & 0x7f) << shift
            shift += 7
        
        return result

    def read(self):
        """ Seek for the end of a LEB128 value and decode the number """

        leb_128_length = self._seek_end()
        values = [ord(i) for i in self.fp.read(leb_128_length)]

        return self.decode(values)
    
    @staticmethod
    def encode(value):
        """ Convert an integer to an unsigned LEB128 integer array """

        result = []

        while value != 0:
            byte = value & 0x7f
            value >>= 7

            if value != 0:
                # Set high order bit
                byte |= 0x80
            
            result.append(byte)
        
        # Convert the result array to a byte string
        return result
    
    def write(self, value):
        """ Encode the value as an unsigned LEB128 value and write it to the file """

        value = self.encode(value)
        self.fp.write(value)