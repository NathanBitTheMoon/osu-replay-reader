import lib.fp.LEB128

class StringReader:
    def __init__(self, fp):
        self.fp = fp
    
    def _string_is_present(self):
        """ Check if a string is present """

        check_byte = self.fp.read(1)
        return check_byte == 0x0b
    
    def read_string(self):
        """ Read the next string from the file """

        leb128_reader = lib.fp.LEB128.LEB128(self.fp)

        if self._string_is_present():
            # Get the ULEB128 length value
            length = leb128_reader.read()

            string_value = self.fp.read(length)
            del leb128_reader

            return string_value.decode()
        else:
            return ""
    
    def write_string(self, value):
        """ Write a string to a file with a ULEB128 length value prefacing it """

        leb128_writer = lib.fp.LEB128.LEB128(self.fp)

        header_byte = chr(0x00 if len(value) == 0 else 0x0b).encode()
        self.fp.write(header_byte)

        if len(value) > 0:
            leb128_writer.write(len(value))
            self.fp.wirte(value.encode())