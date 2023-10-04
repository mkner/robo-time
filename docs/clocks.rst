Clocks
------

.. py:mod: 
.. py:mod:: py_mod

| The three primary clocks are Uptime Clock, World Clock,
| and System Clock. The primordal clock is the Clock. Both World Clock
| and System Clock are directly derived from Clock. The projects object oriented
| design makes it easier to use the various clocks in logical and consistent way.
|
| There is a common interface for many features. Additional functionality is provided
| for the type of time awareness, time variations and time representation.
|


.. function:: uptime()
   
    Prints the uptime for the clock as HH:MM:SS at a minimal
    If the clock is running longer than 24 hours then days are added in the 
    format as DDD:MM:SS where the number of days is the number of days in the year.
    After one year the format is extended to the full format YYYY:DDD:HH:MM:SS
    This function is available on all 3 clocks

  :param: None
  :return: printed string 


.. function:: up()
   
    Short name for uptime(). Works the same.

  :param: None
  :return: printed string 


.. function:: time()

   | prints the current time in HH:MM:SS format 

  :param: None
  :return: printed string


.. function:: date()

   | prints the current date in YYYY:MM:DD format 

  :param: None
  :return: printed string 


.. function:: now()

   | prints date/time/zone in the format YYYY-MM-DD HH:MM:SS <ZONE> 
   | Whatever "now" is depends on the particular clock's worldview 
   
  :param: None
  :return: printed string 


 | Example:

 |  now() format for Clock, WorldClock, SystemClock

 |  0000-00-00 01:37:13 
 |  2023-09-21 19:36:06 UTC
 |  2023-09-21 15:36:06 EDT


.. function:: today()

   | prints the current date in YYYY:MM:DD format 

  :param: None
  :return: printed string 

.. function:: epoch()

   | prints a timestamp of the beginning of the epoch of the clock

  :param: None
  :return: printed string 


.. function:: getUptime()  
   
   | returns the current uptime in a tuple of integers 
   | in the format (days, hours, minutes, seconds) 

  :param: None
  :return: clocks uptime as a tuple of integers
  :rtype: tuple
  

.. function:: getUptimeStr()

    string version of command line uptime()
    returns the same format as uptime() but in a string
    useful for printing, parsing or reformatting

  :param: None
  :return: clocks formatted uptime 
  :rtype: string


.. function:: getUptimeFp()

   returns clocks uptime as a floating point value

  :param: None
  :return: clocks uptime 
  :rtype: float


.. function:: millis()
     
     Returns uptime of the clock in floating 
     point milliseconds since this clock was instantiated
     and initialized. Similar to the ubiquitous
     Arduino millis() function but not necessarily aligned
     with or offset from the actual underlying hardware startup.
   
  :param: None
  :return: clocks uptime in milliseconds
  :rtype: float


.. function:: micros()

     Returns uptime of the clock in floating 
     point microseconds since this clock was instantiated
     and initialized. 
        
  :param: None
  :return: clocks uptime in microseconds
  :rtype: float


.. function:: nanos()

     Returns uptime of this clock in floating 
     point nanoseconds since this clock was instantiated
     and initialized. Whether there is any accurate nanosecond
     resolution offset time available depends on the underlying
     operating system, hardware subsystems and the python implementation.

  :param: None
  :return: clocks uptime in nanoseconds
  :rtype: float


.. function:: getMonotime()

     Returns a monotonic floating point time in seconds.
     Monotonic time moves unidirectionally forward and runs
     independently of the variations that occur with a system clock.
     Its starting value depends on the underlying OS/HW configuration.
     Can be used for the most accurate relative time offset 
     references but not as an absolute hardware uptime.
        
  :param: None
  :return: current monotonic time 
  :rtype: float


WorldClock
----------

Additional interface functions for **WorldClock**


.. function:: getDeltaThreshold()

     Returns the current Delta threshold setting in milliseconds
        
  :param: None
  :return: delta threshold
  :rtype: int


.. function:: setDeltaThreshold(delta)

     Sets the current Delta threshold setting in milliseconds
        
  :param: delta
  :return: None
  :rtype: None


.. function:: setDelta(delta)

     same as **setDeltaThreshold(delta)**


.. function:: getDelta()

     same as **getDeltaThreshold(delta)**


.. code-block:: python

.. code-block:: python
