#!/usr/bin/env python
#
#
# robotime - clocks - timestamps
# for mobile robotics and related applications
#
# (c) 2023  Mike Knerr
#
#
# floating point timestamp 
# comparative tests
#
# v0.01.01
#
# 


from robotime.clocks import Clock

#from robotime.clocks import UptimeClock # robotime version >= 0.01.08
from robotime.clocks import WorldClock
from robotime.clocks import SystemClock

from robotime.time import delay

c = Clock()
#c = UptimeClock() # aka Clock
wc = WorldClock()
sc = SystemClock()


def  tsfp():
    print(c.getTimestampFp())
    print(wc.getTimestampFp())
    print(sc.getTimestampFp())
    

def tsfploop(count):
    count = abs(count)
    print()
    for i in range(count):
        tsfp()
        c.delay(1000)
        print()


delay(1500)
print()

tsfp()

delay(1000)

tsfploop(3)

delay(1000)

wc.init()
delay(1000)

tsfploop(3)
delay(1000)

# after a resync
wc.resync()

tsfploop(3)

# compare to
# timestamp output in ISO-8601 format for 
# each clock type

c.setTimestampFormat('iso-utc')
wc.setTimestampFormat('iso-utc')
sc.setTimestampFormat('iso-utc')

c.timestamp()
wc.timestamp()
sc.timestamp()


"""
Python 3.6.7 | packaged by conda-forge | (default, Mar  4 2020, 16:55:12) 
Type "copyright", "credits" or "license" for more information.

IPython 7.16.1 -- An enhanced Interactive Python.


1.5001420569988113
1.5001360289988952
1695500245.02725

2.500298708999253
2.5002869050003937
1695500246.027396

3.5004274419989088
3.500416478000261
1695500247.027525

4.50056647800011
4.500554522999664
1695500248.027663



WorldClock version: v0.01.14b

Starting up...
Current WorldClock NTP (UTC) time: 1970-01-01 00:00:06.500824
Begin initialization from global NTP system...
Checking NTP connection...
Connection established...
Initializing UTC time from NTP reference signal...
Synchronization phase # 1  OK
Synchronization phase # 2  OK
Synchronization phase # 3
Resynchronizing world clock...
Connection to NTP server OK!
Checking delta threshold...
Within range. Updating...
Get time check...
Current WorldClock NTP (UTC) time: 2023-09-23 20:17:34.557621
Initialization done!


12.034300036999412
1695500255.5578709
1695500255.561397

13.034432016998835
1695500256.5580013
1695500256.561528

14.034629161998964
1695500257.5582378
1695500257.56177

Resynchronizing world clock...
Connection to NTP server OK!
Checking delta threshold...
Within range. Updating...
Get time check...
Current WorldClock NTP (UTC) time: 2023-09-23 20:17:41.848998

18.323208375999457
1695500261.849695
1695500261.850624

19.323674803999893
1695500262.8501484
1695500262.850771

20.324074559999644
1695500263.8505542
1695500263.851183

0000-00-00T00:00:21.324426
2023-09-23T20:17:44.850927Z
2023-09-23T16:17:44.851667-0400

10/60
Out[2]: 0.16666666666666666
"""
