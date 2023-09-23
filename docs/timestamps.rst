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

   returns current timestamp for the particular clock type
   as floating point number
   this is necessarily epoch dependent since the current time
   is always an offset from the beginning of the particular epoch
   for a given timesystem
    
  :param: None
  :return: timestamp as floating point value
  :rtype: floag


.. function:: mkTimestamp(fptime)

   | makes a timestamp from a floating point time 
   | in the form of a tuple of integers 
   
  :param fptime: time as floating point value
  :return: timestamp components as integers in tuple form
  :rtype: tuple




