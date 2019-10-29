#!/usr/bin/python

from relays import *

relays = SeqRelays("USB0", 4)
relays.filling(RIGHT, 0.060, 10)

relays.set(1, OFF)
relays.set(2, OFF)
relays.set(3, OFF)
relays.set(4, OFF)
exit(0)

