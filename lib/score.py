import lib.fp.values

class ScoreReader:
    def __init__(self, fp):
        self.fp = fp

        self._300s = 0
        self._100s = 0
        self._50s = 0
        self.gekis = 0
        self.katsu = 0
        self.misses = 0
        self.score = 0
        self.combo = 0
        self.full_combo = False
    
    def _update(self):
        """ Read the data from the file and update the data in the class"""

        value_reader = lib.fp.values.ValueReader(self.fp)

        self._300s = value_reader.read_short()
        self._100s = value_reader.read_short()
        self._50s = value_reader.read_short()
        self.gekis = value_reader.read_short()
        self.katsu = value_reader.read_short()
        self.misses = value_reader.read_short()
        self.score = value_reader.read_integer()
        self.combo = value_reader.read_short()
        self.full_combo = value_reader.read_byte() == 1
    
    def export(self):
        """ Create a byte string for the data in the class """

        value_writer = lib.fp.values.ValueReader(self.fp)

        result = b''

        result += value_writer._pad(self._300s, 2)
        result += value_writer._pad(self._100s, 2)
        result += value_writer._pad(self._50s, 2)
        result += value_writer._pad(self.gekis, 2)
        result += value_writer._pad(self.katsu, 2)
        result += value_writer._pad(self.misses, 2)
        result += value_writer._pad(self.score, 4)
        result += value_writer._pad(self.combo, 2)
        result += value_writer._pad(int(self.full_combo), 1)

        return result