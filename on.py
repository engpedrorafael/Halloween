#!/usr/bin/python

from relays import *

relays = SeqRelays("USB0", 4)
relays.set(1,ON)
relays.set(2,ON)
relays.set(3,ON)
relays.set(4,ON)
exit(0)

