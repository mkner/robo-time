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

.. function:: imap(x, in_min, in_max, out_min, out_max)
  
   maps an integer value in the range **[in_min, in_max]** to interval **[out_min, out_max]**
   analogous to arduino map function that uses long int numeric types
   if the value x is a non-integer type it is converted to an int

  :param x: input numeric value to map
  :param in_min: lower bound of input range
  :param in_max: upper bound of input range
  :param out_min: lower bound of output range
  :param out_max: upper bound of output range

  :return: bounded value
  :rtype: int


.. function:: time()

   command line function
   prints the current time in HH:MM:SS format

   maps an integer value in the range **[in_min, in_max]** to interval **[out_min, out_max]**
   analogous to arduino map function that uses long int numeric types
   if the value x is a non-integer type it is converted to an int



#redid to here



.. function:: date()

   command line function 
   prints the current date in YYYY:MM:DD format 

  :param: None

  :return: printed string 


.. function:: now()

   command line function
   prints date/time/zone in the format YYYY-MM-DD HH:MM:SS <ZONE> 
   Whatever "now" is depends on the specific clock's worldview 

  :param: None

  :return: printed string 


  Example:

  now() for Clock, WorldClock, SystemClock 

  0000-00-00 01:37:13 
  2023-09-21 19:36:06 UTC
  2023-09-21 15:36:06 EDT


.. function:: today()

   command line version 
   prints the current date in YYYY:MM:DD format 

  :param: None
  :return: printed string 
  

.. code-block:: python

.. code-block:: python
