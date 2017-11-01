import serial, time 
from threading import Thread, Lock

#STATES
OFF    = 0
ON     = 1
STROBE = 2

LEFT = True
RIGHT = False

DEBUG  = False
RUN    = True

#serialMutex = Lock()
#queueMutex = Lock()

class RelayBoard(object):
    def __init__(self, usb):
        self.port = "/dev/tty" + usb
        self.ser = serial.Serial(self.port, 9600, timeout=0.5)
        print(self.ser.name + ' is open.')


    def set(self, num, state):
        """num=0:  All relays"""
        #serialMutex.acquire(1)
        cmd = "FF" + ("%02x" % (num )) + (state and "01" or "00")
        if DEBUG:  print("Set: state="+ cmd)
        self.ser.write(cmd.decode('hex'))
        #serialMutex.release()
 

    def __del__(self):
        self.ser.close()
        print(self.ser.name + ' is closed.')


class SeqRelays(RelayBoard):
    def __init__(self, usb, nRelays = 8):
        self.nRelays = nRelays
        super(SeqRelays,self).__init__(usb)
        self.set(0, OFF)

    def walking(self, direction = LEFT, duration = 1, repeat = 1):
        for rep in range(repeat):
            sequence = direction == LEFT and range(1,self.nRelays+1) \
                                          or list(reversed(range(1,self.nRelays+1)))
            for n in sequence:
                self.set(n, ON)
                time.sleep(0.01)
                self.set(n, OFF)
                time.sleep(duration)

    def filling(self, direction = LEFT, duration = 1, repeat = 1):
        state = OFF
        for rep in range(repeat):
            state = not state
            sequence = direction == LEFT and range(1,self.nRelays+1) \
                                          or list(reversed(range(1,self.nRelays+1)))
            for n in sequence:
                self.set(n, state)
                time.sleep(duration)

    def flashing(self, durationOn = 1, durationOff = 1, repeat = 1):
        for rep in range(repeat):
            for n in range(1,self.nRelays+1):
                self.set(n, ON)
            time.sleep(durationOn)
            for n in range(1,self.nRelays+1):
                self.set(n, OFF)
            time.sleep(durationOff)

 


class StrobeRelays:
    def __init__(self, usb, nThreads = 8):
        self.nThreads = nThreads
        self.relays = RelayBoard(usb)
        self.rThreads = []
        self.rStates = [OFF] * nThreads

        for n in range(nThreads):
            self.rThreads.append(Thread(target=self.Rthread, args=(n,)))
            self.rThreads[n].start()

    def Rthread(self, num):
        if DEBUG: print("Thread for R%d started" % num)
        queueMutex.acquire(1)
        lastState = (self.rStates)[num]
        (self.rStates)[num] = lastState
        queueMutex.release()
        strobeState = OFF

        while (RUN):
            queueMutex.acquire(1)
            if lastState != self.rStates[num]:
                if DEBUG: print("Changed R%d state from %d to %d" % (num, lastState, self.rStates[num]))
                lastState = self.rStates[num]
                if lastState == STROBE:
                    self.relays.set(num+1, strobeState)
                else:
                    self.relays.set(num+1, lastState)

            if self.rStates[num] == STROBE:
                strobeState = not strobeState
                self.relays.set(num+1, strobeState)

            queueMutex.release()
            time.sleep(0.050)
        if DEBUG: print("Thread for R%d stopped" % num) 

    def set(self, num, state):
        #TODO: Implement strobe rate
        queueMutex.acquire(1)
        if num == 0:
            for x in range(self.nThreads):
                self.rStates[x] = state
        else:
            self.rStates[num-1] = state
        queueMutex.release()
        



if __name__ == "__main__":
    DEBUG = False

    relays = SeqRelays("USB1", 4)

    relays.walking(RIGHT, 0.1, 3)
    relays.filling(RIGHT, 0.1, 3)
    relays.flashing(0.05, 0.3, 5)

    relays.set(0, OFF)
    exit(0)


    #relays = StrobeRelays("USB1",4)
    #for x in range (1,9):
    #    relays.set(x, ON)
    #    time.sleep(0.3)

    relays.set(1, STROBE)
    relays.set(3, STROBE)
    relays.set(4, STROBE)



    print "Waiting..."
    time.sleep(3)



    #EXIT
    relays.set(0, OFF)
    time.sleep(1)
    RUN = False


