

Examples
--------

.. |robo-time
.. |*********


Clock
*****

| basic time & date 

.. code-block:: python
   
   from robotime.clocks import Clock

   # alternate forms 
   # from robotime import UptimeClock
   # from robotime import Clock

   c = Clock() 
   
   c.uptime()
   00:00:08
   
   c.time()
   00:00:14
   
   c.date()
   0000-00-00
   
   c.now()
   0000-00-00 00:00:26
   
   c.today()
   0000-00-00 00:00:30


SystemClock
***********

| basic time & date 

.. code-block:: python

   from robtime.clocks import SystemClock

   sc = SystemClock()

   sc.uptime()
   00:00:10
   
   sc.time()
   18:04:19
   
   sc.date()
   2023-09-17
   
   sc.now()
   2023-09-17 18:04:30 EDT
   
   sc.today()
   Sun Sep 17 2023 18:04:34 EDT



WorldClock
**********

| Before WorldClock is initialized and synced to global servers
| its only sense of date & time is relative to the only beginning 
| of time it knows. The Unix epoch.
|
| And **now()** is its uptime offset from  1970-01-01 00:00:00 UTC
| and not from the current UTC time.
|

.. code-block:: python

   from robotime.clocks import WorldClock

   wc = WorldClock()
   
   wc.uptime()
   00:00:03
   
   wc.time()
   00:00:09
   
   wc.date()
   1970-01-01
   
   wc.now()
   1970-01-01 00:00:22 UTC
   
   wc.today()
   Thu Jan 01 1970 00:00:26 UTC
   
   wc.timestamp()
   1970-01-01 00:00:49 734483

| Running the initialization routine for WorldClock updates and
| synchronizes its time to the global NTP UTC servers.
|

.. code-block:: python

   wc.init()
   
   WorldClock version: v0.01.14b
   
   Starting up...
   Current WorldClock NTP (UTC) time: 1970-01-01 00:01:14.412665
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
   Current WorldClock NTP (UTC) time: 2023-09-17 20:49:51.506208
   Initialization done!
   
   
   wc.now()
   2023-09-17 20:49:57 UTC
   
   wc.today()
   Sun Sep 17 2023 20:50:02 UTC
   
   wc.timestamp()
   2023-09-17 20:50:10 174461

| WorldClock can also by resynced at any time. A resync is not as
| thorough as an full initialization, but can be useful to keep the
| WorldClock accurate within a certain delta threshold.
|
| A resync can be scheduled periodically at some interval
| as frequently as required. 
|

.. code-block:: python

   wc.resync()

   Resynchronizing world clock...
   Connection to NTP server OK!
   Checking delta threshold...
   Within range. Updating...
   Get time check...
   Current WorldClock NTP (UTC) time: 2023-09-17 20:50:32.701712
   
   wc.now()
   2023-09-17 20:50:50 UTC
   
   wc.today()
   Sun Sep 17 2023 20:50:53 UTC

   wc.timestamp()
   2023-09-17 20:50:55 953406


.. code-block:: python


Robot
*****

Example using python command line interface

Accsss some basic clock functions of an autonomous mobile robot 
that is running the primary clocks: Clock, WorldClock, and SystemClock

The robot has been logged into via a secure shell and
python (command mode) is launched from there


.. code-block:: python

   user@robot:~$ python
   Python 3.8.10 (default, Mar 13 2023, 10:26:41) 
   [GCC 9.4.0] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> from robot import Robot
   >>> robot = Robot()
   >>> robot.whoami()
   Robot v0.01.23x11c 
   >>> robot.uptime()
   00:00:38
   >>> robot.worldclock.now()
   1970-01-01 00:00:48 UTC
   >>> robot.worldclock.ts()
   1970-01-01 00:00:54 704200
   >>> robot.worldclock.init()

   WorldClock version: v0.01.14b
   
   Starting up...
   Current WorldClock NTP (UTC) time: 1970-01-01 00:01:06.353826
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
   Current WorldClock NTP (UTC) time: 2023-09-22 03:28:29.001089
   Initialization done!
   
   >>> robot.worldclock.now() 
   2023-09-22 03:28:37 UTC
   >>> robot.sysclock.now()
   2023-09-22 03:29:02 UTC
   >>> robot.sysclock.now();robot.worldclock.now()
   2023-09-22 03:29:20 UTC
   2023-09-22 03:29:20 UTC
   >>> robot.worldclock.resync()
   Resynchronizing world clock...
   Connection to NTP server OK!
   Checking delta threshold...
   Within range. Updating...
   Get time check...
   Current WorldClock NTP (UTC) time: 2023-09-22 03:29:52.343513
   >>> robot.worldclock.timestamp()
   2023-09-22 03:30:07 932513
   >>> robot.worldclock.setTimestampFormat('iso-utc')
   >>> robot.worldclock.timestamp()                  
   2023-09-22T03:30:53.398023Z
   >>> robot.uptime()
   00:04:35


Timestamps
**********

Formats

Getting familiar with  formats and time representations

These examples are generated by using the **robotime.test** module
to show a side-by-side comparison of the outputs for all three clocks:
Clock (UptimeClock), WorldClock, SystemClock (in that order)
Calling **roll()**  cycles through the functions

.. code-block:: python

   from robotime.test import *
   roll()

.. code-block:: python

   #format
   getTstype()
   default
   default
   default

   #uptime
   up()
   01:22:46
   01:22:46
   01:22:46

date
0000-00-00
1970-01-01
2023-10-02

time
01:22:50
01:22:50
17:57:03

now
0000-00-00 01:22:52
1970-01-01 01:22:52 UTC
2023-10-02 17:57:05 EDT

today
0000-00-00 01:22:54
Thu Jan 01 1970 01:22:54 UTC
Mon Oct 02 2023 17:57:07 EDT

timestamp()
0000-00-00 01:22:56 158234
1970-01-01 01:22:56 158220
2023-10-02 17:57:09 889590

getTimestamp()
0000-00-00 01:22:58 158454
1970-01-01 01:22:58 158433
2023-10-02 17:57:11 889797

getTimestampInt()
(0, 0, 0, 1, 23, 0, 158657)
(1970, 1, 1, 1, 23, 0, 158633)
(2023, 10, 2, 17, 57, 13, 889992)

getTimestampFp()
4982.158804454999
4982.158780668
1696283835.890115

getUptimeFp()
4984.158967056999
4984.158931133001
4984.1589574459995



Example - floating point timestamp

Comparision of floating point timetamp times for all 3 clock types.

The floating point timestamp time is always dependent on the epoch start 
date/time in floating point. This is the UNIX epoch.

Comparative output shows the timestamp values before WorldClock initialization and then after.
SystemClock get its system time from the underlying Linux system and its local timezone settings.

In this example, the floating point sync between the WorldClock and the SystemClock is 
to the 1/10 second or about 100 milliseconds but no further. This is a limitation of
the NTP/UTC global internet sync system and the current test environment. In general, the NTP/UTC 
system can be repeatedly accurate within millisecond ranges. For many purposes it is accurate
enough and is widely used as a standard globally.


.. code-block:: python

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


.. code-block:: python
   
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
   



