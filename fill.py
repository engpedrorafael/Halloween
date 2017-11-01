#!/usr/bin/python

from relays import *

relays = SeqRelays("USB0", 4)
relays.filling(RIGHT, 0.1, 10)

relays.set(0, OFF)
exit(0)

