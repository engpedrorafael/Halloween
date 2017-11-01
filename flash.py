#!/usr/bin/python

from relays import *

relays = SeqRelays("USB0", 4)
relays.flashing(0.0, 0.6, 1000)

relays.set(0, OFF)
exit(0)

