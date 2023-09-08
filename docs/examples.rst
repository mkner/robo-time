

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

   robot.worldclock.today()
   Fri Sep 01 1970 00:02:01 UTC

   robot.worldclock.now()
   1970-01-01 00:02:04 UTC

   robot.worldclock.now()
   1970-01-01 00:02:09 UTC

   robot.worldclock.now();delay(1000);robot.worldclock.now()
   1970-01-01 00:06:59 UTC
   1970-01-01 00:07:00 UTC






