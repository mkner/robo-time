#
#
# robotime - test
#
# for mobile robotics and related applications
#
# some useful functions for testing
# and sanity checks using robo-time
#
# (c) 2022 - 2024  Mike Knerr
#
#
#
#
# robotime - clocks - timestamps
# for mobile robotics and related applications
#
# quickcheck
#
# short form calls to check
# basic integrity of functionality
#
# (c) 2023  Mike Knerr
#
#

# for vers
import robobase
import robotime
import roboutils

### working or installed HERE

#from clocks import Clock
from robotime.clocks import Clock

#from clocks import SystemClock
from robotime.clocks import SystemClock

#from clocks import WorldClock
from robotime.clocks import WorldClock

### MAKE CLOCKS ###

c = Clock()
sc = SystemClock()
wc = WorldClock()

# CK THAT WORKS
from robotime import UptimeClock
uc = UptimeClock()

from robotime.time import delay

#from robot import Robot


def up():
    c.uptime()
    wc.uptime()
    sc.uptime()

def now():
    c.now()
    wc.now()
    sc.now()

def date():
    c.date()
    wc.date()
    sc.date()
    
def time():
    c.time()
    wc.time()
    sc.time()
    

def today():
    c.today()
    wc.today()
    sc.today()
    
def ts():
    ## timestamps
    c.timestamp()
    wc.timestamp()
    sc.timestamp()


def gts():
    print(c.getTimestamp())
    print(wc.getTimestamp())
    print(sc.getTimestamp())


def tsr():
    print(c.getTimestampStr())
    print(wc.getTimestampStr())
    print(sc.getTimestampStr())

def tsi():
    print(c.getTimestampInt())
    print(wc.getTimestampInt())
    print(sc.getTimestampInt())

def tsf():
    print(c.getTimestampFp())
    print(wc.getTimestampFp())
    print(sc.getTimestampFp())

def tsfp():
    print(c.getTimestampFp())
    print(wc.getTimestampFp())
    print(sc.getTimestampFp())

def upfp():
    print(c.getUptimeFp())
    print(wc.getUptimeFp())
    print(sc.getUptimeFp())
 
    
def upfploop(count):
    count = abs(count)
    print()
    for i in range(count):
        upfp()
        c.delay(1000)
        print()

def tsfploop(count):
    count = abs(count)
    print()
    for i in range(count):
        tsfp()
        c.delay(1000)
        print()

def epoch():
    c.epoch()
    wc.epoch()
    sc.epoch()


def ep():
    return(epoch())
 
def setTstype(ts):
    c.setTimestampFormat(ts)
    wc.setTimestampFormat(ts)
    sc.setTimestampFormat(ts)

def getTstype():
    print(c.getTimestampFormat())
    print(wc.getTimestampFormat())
    print(sc.getTimestampFormat())
    
    
def setbasic():
    setTstype('basic')
    
    
def setlocal():
    setTstype('iso-local')

    
def setutc():
    setTstype('iso-utc')
    
    
def setcompon():
    c.setTimestampCompressedOn()
    sc.setTimestampCompressedOn()
    wc.setTimestampCompressedOn()

def setcompoff():
    c.setTimestampCompressedOff()
    sc.setTimestampCompressedOff()
    wc.setTimestampCompressedOff()

def ztailon():
    c.setZtailOn()
    wc.setZtailOn()
    sc.setZtailOn()
    
def ztailoff():
    c.setZtailOff()
    wc.setZtailOff()
    sc.setZtailOff()


def setresMicros():
    c.setTimestampRes('micro')
    wc.setTimestampRes('micro')
    sc.setTimestampRes('micro')
    
def setresMillis():
    c.setTimestampRes('milli')
    wc.setTimestampRes('milli')
    sc.setTimestampRes('milli')    

def setresOff():
    c.setTimestampRes('none')
    wc.setTimestampRes('none')
    sc.setTimestampRes('none')    


def vers():
    print()
    print("robo-base - "+str(robobase.__version__))
    print("robo-time - "+str(robotime.__version__))
    print("robo-utils - "+str(roboutils.__version__))
    print()


def roll():
    print()
    delay(1000)
    

    print("getTimestampFormat()")
    getTstype()
    print()
    delay(1000)
    
    print("up()")
    up()
    print()
    delay(2000)
    
    print("date()")
    date()
    print()
    delay(2000)
    
    print("time()")
    time()
    print()
    delay(2000)
    
    print("now()")
    now()
    print()
    delay(2000)
    
    print("today()")
    today()
    print()
    delay(2000)
    
    print("timestamp()")
    ts()
    print()
    delay(2000)
    
    print("getTimestamp()")
    tsr()
    print()
    delay(2000)
    
    print("getTimestampInt()")
    tsi()
    print()
    delay(2000)

    print("getTimestampFp()")
    tsf()
    print()
    delay(2000)
    
    print("getUptimeFp()")
    upfp()
    print()
    delay(2000)
    
