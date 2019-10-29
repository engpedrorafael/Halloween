#!/usr/bin/python

from relays import *

relays = SeqRelays("USB0", 4)
relays.set(5, ON)
exit(0)

