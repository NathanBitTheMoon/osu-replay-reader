# osu-replay-reader
A python library for reading osu! replay files (.osr)

## Module info:
* lib
    * fp
        * **bytearray** Used for converting integer arrays to byte strings and visa versa
        * **LEB128** Used for reading, decoding, encoding and writing unsigned ULEB128 values
        * **values** Used for reading and writing bytes as numbers
        * **string** Used for reading and writing strings
    * **gamemode** Contains Enum values for gamemodes
    * **score** Used to load the score from the file
    * **mods** Used to load and save mods from the file
