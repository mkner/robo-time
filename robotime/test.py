#
#
# robo-time - test
# for mobile robotics and related applications
#
# some useful functions for testing
# and sanity checks
#
# (c) 2022 - 2023  Mike Knerr
#
# 

from datetime import datetime
from datetime import timezone

import calendar
import time

import robotime


#robot = False

from robot import Robot

#robot = robot

#not work import roboclocks as clocks

from robotime.clocks import Clock
#from clocks import Clock
c=Clock()
#or


from robotime.clocks import SystemClock
#from clocks import SystemClock
sc = SystemClock()
#or


from robotime.clocks import WorldClock
#from clocks import WorldClock# from local dir working version
wc = WorldClock()
#or

from robotime.time import delay

#datetime.now()


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
    

def roll():
    print()
    delay(1000)
    
    print("format")
    getTstype()
    print()
    delay(2000)
    
    print("up")
    up()
    print()
    delay(2000)
    
    print("date")
    date()
    print()
    delay(2000)
    
    print("time")
    time()
    print()
    delay(2000)
    
    print("now")
    now()
    print()
    delay(2000)
    
    print("today")
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
