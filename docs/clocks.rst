Clocks
------

.. py:mod: 
.. py:mod:: py_mod

| The three most important primary clocks are Uptime Clock, World Clock,
| and System Clock. The primordal clock is the Clock . Both World Clock
| and System Clock are directly derived from Clock. The projects object oriented
| design makes it easier to use the various clocks in logical and consistent way.
|
| There is a common interface for many features. Additional functionality is provided
| for the type of time awareness, time variations and time representation.
|


.. function:: uptime()
   
   | Prints the uptime for the clock as HH:MM:SS at a minimal
   | If the clock is running longer than 24 hours then days are added in the 
   | format as DDD:MM:SS where the number of days is the number of days in the year.
   | After one year the format is extended to the full format YYYY:DDD:HH:MM:SS
   | This function is available on all 3 clocks

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


.. function:: getUptime()  
   
   | returns the current uptime in a tuple of integers 
   | in the format (days, hours, minutes, seconds) 

  :param: None
  :return: tuple 


.. function:: getUptime()  
   
   | returns the current uptime in a tuple of integers 
   | in the format (days, hours, minutes, seconds) 

  :param: None
  :return: tuple
  

.. function:: getUptimeStr()

   | string version of command line uptime()
   | returns the same format as uptime() but in a string
   | useful for parsing and reformatting

  :param: None
  :return: string


.. code-block:: python

.. code-block:: python
