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

   Sets the format for the timestamps 

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


.. function:: getTimestampFormat()

   Returns the format for the timestamps 

   Return values for are:

   - 'basic' - or 'default' the default format - plain, ordinary, easy to read
   - 'iso-utc'  - ISO-8601 format using UTC time
   - 'iso-local' - ISO-8601 format using system local time

  :param: None
  :return: timestamp format type
  :rtype: literal


.. function:: setTimestampRes(res)

   Sets the resolution for the fractional part of
   the timestamp

   Choices for res are:

   - 'milli' - milliseconds (3 digits)
   - 'micro' - microseconds (6 digits)
   - 'none'  - no fractional remainder is used

  :param: res
  :return: None


.. function:: setTimestampDateSep(dsep)

   Sets the character used between the year YYYY, 
   month MM and day DD in the sequence YYYY<dsep>MM<dsep>DD
   in the timestamp output to dsep

   Builtin character used for presets is a dash '-'
   for all 3 presets: 'basic', iso-utc' and 'iso-local'

  :param: dsep
  :return: None


.. function:: setTimestampSep(dtsep)

   Sets the character used between the year YYYY-MM-DD 
   and the time HH:MM:SS in the timestamp output
   YYYY-MM-DD<dtsep>HH:MM:SS to dtsep

   Builtin characters used for presets are:

   - 'basic' or 'default'  - ' ' one blank space
   - 'iso-utc'  - ISO-8601 format - 'T'
   - 'iso-local' - ISO-8601 format - 'T'

  :param: dtsep
  :return: None








