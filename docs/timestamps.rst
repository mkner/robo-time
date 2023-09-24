Timestamps
----------

.. py:mod: 
.. py:mod:: py_mod


.. function:: timestamp()

    prints timestamp string 
    
  :param: None
  :return: prints timestamp string
  :rtype: None


.. function:: ts()

    short call for timestamp()

  :param: None
  :return: prints timestamp string
  :rtype: None


.. function:: getTimestampStr()

    returns a string containing the formatted timestamp
    
  :param: None
  :return: timestamp string
  :rtype: string


.. function:: getTimestamp()

   | returns a tuple of integers containing the timestamp
   | components (year, month, day, hour, minute, second, remainder)
    
  :param: None
  :return: timestamp components as integers in tuple form
  :rtype: tuple


.. function:: getTimestampFp()

   Returns current timestamp for the particular clock type
   as floating point number. The actual date and time for the clock
   is necessarily epoch dependent since the returned value is an offset
   from the beginning of the particular epoch for a given timesystem.
    
  :param: None
  :return: timestamp as floating point value
  :rtype: float


.. function:: setTimestampFormat(tsformat)

   Sets the format for the timestamps.  

   Choices for tsformat are:

   - 'basic' - the default format - plain, ordinary, easy to read
   - 'iso-utc'  - ISO-8601 format using UTC time
   - 'iso-local' - ISO-8601 format using system local time

   **basic** is the same format for all 3 clocks: Uptime Clock, 
   System Clock and World Clock

   **iso-local** for WorldClock is UTC time once a WorldClock is
   initialized since its *"local"* time is *always* UTC

   **iso-utc** for SystemClock uses ISO-8601 format and local system
   time is expressed in UTC with an offset to its zone

   **iso-local** for SystemClock uses ISO-8601 for its format
   but local system time is expressed in local time with no zone
   offset and not in UTC time


  :param: tsformat
  :return: None



