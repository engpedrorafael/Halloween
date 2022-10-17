#!/usr/bin/python

from relays import *

relays = SeqRelays("USB0", 2, [1,4])
relays.flashing(0.050, 0.150,20)

relays.set(1, OFF)
relays.set(2, OFF)
relays.set(3, OFF)
relays.set(3, OFF)
exit(0)

