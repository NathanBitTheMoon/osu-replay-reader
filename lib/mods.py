# Byte offset values for mods
NONE = 0
NOFAIL = 1
EASY = 2
TOUCHDEVICE = 4
HIDDEN = 8
HARDROCK = 16
SUDDENDEATH = 32
DOUBLETIME = 64
RELAX = 128
HALFTIME = 256
NIGHTCORE = 512
FLASHLIGHT = 1024
AUTOPLAY = 2048
SPUNOUT = 4096
RELAX2 = 8192
PERFECT = 16384
KEY4 = 32768
KEY5 = 65536
KEY6 = 131072
KEY7 = 262144
KEY8 = 524288
KEYMOD = 1015808
FADEIN = 1048576
RANDOM = 2097152
LASTMOD = 4194304
TARGETPRACTICE = 8388608
KEY9 = 16777216
COOP = 33554432
KEY1 = 67108864
KEY3 = 134217728
KEY2 = 268435456

class ModReader:
    def __init__(self, value):
        """ Load the mods from the integer value read from the file """

        # osu!standard mods
        self.none = value & NONE == NONE
        self.no_fail = value & NOFAIL == NOFAIL
        self.easy = value & EASY == EASY
        self.touch_device = value & TOUCHDEVICE == TOUCHDEVICE
        self.hidden = value & HIDDEN == HIDDEN
        self.hard_rock = value & HARDROCK == HARDROCK
        self.sudden_death = value & SUDDENDEATH == SUDDENDEATH
        self.double_time = value & DOUBLETIME == DOUBLETIME
        self.relax = value & RELAX == RELAX
        self.half_time = value & HALFTIME == HALFTIME
        self.nightcore = value & NIGHTCORE == NIGHTCORE
        self.flashlight = value & FLASHLIGHT == FLASHLIGHT
        self.autoplay = value & AUTOPLAY == AUTOPLAY
        self.spun_out = value & SPUNOUT == SPUNOUT
        self.relax_2 = value & RELAX2 == RELAX2
        self.perfect = value & PERFECT == PERFECT

        # osu!mania mods
        self.key1 = value & KEY1 == KEY1
        self.key2 = value & KEY2 == KEY2
        self.key3 = value & KEY3 == KEY3
        self.key4 = value & KEY4 == KEY4
        self.key5 = value & KEY5 == KEY5
        self.key6 = value & KEY6 == KEY6
        self.key7 = value & KEY7 == KEY7
        self.key8 = value & KEY8 == KEY8
        self.key9 = value & KEY9 == KEY9
        self.key_mod = value & KEYMOD == KEYMOD

        # osu!lazer mods
        self.fade_in = value & FADEIN == FADEIN
        self.random = value & RANDOM == RANDOM
        self.last_mod = value & LASTMOD == LASTMOD
        self.target_practice = value & TARGETPRACTICE == TARGETPRACTICE
    
    def export(self):
        """ Export the current mod selections as an integer readable by osu! """

        result = 0

        # osu!standard mods
        result |= NONE if self.none else 0
        result |= NOFAIL if self.no_fail else 0
        result |= EASY if self.easy else 0
        result |= TOUCHDEVICE if self.touch_device else 0
        result |= HIDDEN if self.hidden else 0
        result |= HARDROCK if self.hard_rock else 0
        result |= SUDDENDEATH if self.sudden_death else 0
        result |= DOUBLETIME if self.double_time else 0
        result |= RELAX if self.relax else 0
        result |= HALFTIME if self.half_time else 0
        result |= NIGHTCORE if self.nightcore else 0
        result |= FLASHLIGHT if self.flashlight else 0
        result |= AUTOPLAY if self.autoplay else 0
        result |= SPUNOUT if self.spun_out else 0
        result |= RELAX2 if self.relax_2 else 0
        result |= PERFECT if self.perfect else 0

        # osu!mania mods
        result |= KEY1 if self.key1 else 0
        result |= KEY2 if self.key2 else 0
        result |= KEY3 if self.key3 else 0
        result |= KEY4 if self.key4 else 0
        result |= KEY5 if self.key5 else 0
        result |= KEY6 if self.key6 else 0
        result |= KEY7 if self.key7 else 0
        result |= KEY8 if self.key8 else 0
        result |= KEY9 if self.key9 else 0
        result |= KEYMOD if self.key_mod else 0

        # osu!lazer mods 
        result |= FADEIN if self.fade_in else 0
        result |= RANDOM if self.random else 0
        result |= LASTMOD if self.last_mod else 0
        result |= TARGETPRACTICE if self.target_practice else 0

        return result