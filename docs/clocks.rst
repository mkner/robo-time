Clocks
------

.. py:mod: 
.. py:mod:: py_mod

| The three most important primary clocks are Uptime Clock, World Clock,
| and System Clock. The primordal clock is the Uptime Clock. Both World Clock
| and System Clock are directly derived from Clock. The projects object oriented
| design makes it easier to use the various clocks in logical and consistent way.
| There is a common interface for many features. Additional functionality is provided
| for the type of time awareness, time variations and time representation.
|


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
   | Whatever "now" is depends on the specific clock's worldview 
   
  :param: None
  :return: printed string 

 | Example:

 |  now() for Clock(), WorldClock(), SystemClock()

 |  0000-00-00 01:37:13 
 |  2023-09-21 19:36:06 UTC
 |  2023-09-21 15:36:06 EDT


.. function:: today()

   | prints the current date in YYYY:MM:DD format 

  :param: None
  :return: printed string 
  

.. code-block:: python

.. code-block:: python
