#!/usr/bin/python

from relays import *

relays = SeqRelays("USB0", 4)
relays.walking(RIGHT, 0.05, 20)

relays.set(0, OFF)
exit(0)

