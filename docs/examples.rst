

Examples
--------

.. |robo-clocks
.. |***********


Clock
*****

| create a primary clock

.. code-block:: python

   from roboclocks import Clock

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

| Create a system clock

.. code-block:: python

   from roboclocks import SystemClock

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

   from roboclocks import WorldClock

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


   

