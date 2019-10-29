#!/usr/bin/python

from relays import *

relays = SeqRelays("USB0", 2, [2,3])
relays.walking(RIGHT, 0.1, 20)

relays.set(1, OFF)
relays.set(2, OFF)
relays.set(3, OFF)
relays.set(4, OFF)
exit(0)

