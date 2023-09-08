

Example
-------

.. |robo-clocks
.. |***********

|

For example:

Clock
*****

| create a primary object clock
| 
|

.. code-block:: python

   import roboclocks
   from roboclocks import Clock

   c = Clock()


WorldClock
**********

 Before WorldClock is initialized and synced to the global servers
 its only sense of date & time is relative to the 
 only beginning of time it knows. The Unix epoch.
 And **now** is its uptime offset from  1970-01-01 00:00:00 UTC

.. code-block:: python
   
   robot.worldclock.uptime()
   00:01:11

   robot.worldclock.now()
   1970-01-01 00:01:19 UTC

   robot.worldclock.date()
   1970-01-01

   robot.worldclock.time()
   00:01:49

   robot.worldclock.now()
   1970-01-01 00:02:04 UTC

   robot.worldclock.now()
   1970-01-01 00:02:09 UTC

   robot.worldclock.now();delay(1000);robot.worldclock.now()
   1970-01-01 00:06:59 UTC
   1970-01-01 00:07:00 UTC

.. code-block:: python

   robot.worldclock.init()
   
   WorldClock version: v0.01.12c starting up...
   Begin initialization from global NTP system...
   Checking NTP connection...
   Connection established...
   Initializing UTC time from NTP reference signal...
   Synchronization phase # 1
   Synchronization phase # 2
   Current WorldClock NTP time (UTC): 2023-09-08 21:17:41.688104
   Synchronization phase # 3
   Resynchronizing world clock...
   checking delta threshold: ||0.0094454288|| < 0.05
   delta within range. Updating...
   Get time check...
   After adjustment... 
   delta: 0.009749889373779297 (fp)
   delta: 9 (ms)
   Initialization done!

   robot.worldclock.now()
   2023-09-08 21:18:18 UTC
   
   robot.worldclock.now();delay(1000);robot.worldclock.now()
   2023-09-08 21:18:21 UTC
   2023-09-08 21:18:22 UTC




