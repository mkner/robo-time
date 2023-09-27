Timestamps
----------

.. py:mod: 
.. py:mod:: py_mod

|
| Timestamp interface functions for all clocks:
|
- Clock (UptimeClock)
- WorldClock
- SystemClock
|

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


.. function:: getTimestampInt()

   | returns a tuple of integers containing the timestamp
   | components (year, month, day, hour, minute, second, remainder)
    
  :param: None
  :return: timestamp components as integers in tuple form
  :rtype: tuple


.. function:: getTimestamp()

   | same as getTimestampStr()
   | future version may let the type of format
   | that is a default for this call to be set
   
  :param: None
  :return: timestamp 
  :rtype: string


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
   month MM and day DD to **dsep** in the
   timestamp output sequence YYYY<**dsep**>MM<**dsep**>DD
  

   Builtin character used is a dash '-'
   for all 3 presets: 'basic', iso-utc' and 'iso-local'

  :param: dsep
  :return: None


.. function:: setTimestampSep(dtsep)

   Sets the character used between the year and 
   the time to dtsep in the timestamp output
   sequence YYYY<dsep>MM<dsep>DD<**dtsep**>HH<tsep>MM<tsep>SS

   Builtin characters used for presets are:

   - 'basic' or 'default'  - ' ' one blank space
   - 'iso-utc'  - ISO-8601 format - 'T'
   - 'iso-local' - ISO-8601 format - 'T'

  :param: dtsep
  :return: None


.. function:: setTimestampTimeSep(tsep)

   Sets the character used between the hour HH,
   minute MM and seconds SS to *tsep* in the
   timestamp output sequence HH<tsep>MM<**tsep**>SS 

   Builtin character used for presets is a colon ':'
   for all 3 presets: 'basic', iso-utc' and 'iso-local'

  :param: tsep
  :return: None


.. function:: setTimestampResSep(rsep)

   Sets the character used between the timedate section
   of the timestamp and the fractional remainder at the
   end of the timestamp (if used)

   Builtin character used for presets is a blank space ' ' 
   for the 'basic' preset and a period '.' for iso-utc'
   and 'iso-local'

  :param: rsep
  :return: None


.. function:: setZtailOn()

   Use the **Z** character at the end of UTC time for
   zone 0 instead of **+00:00** (ISO-8601 format)
   
  :param: None
  :return: None


.. function:: setZtailOff()

   Use **+00:00** at the end of UTC time for zone 0
   instead of the **Z** character (ISO-8601 format)
   
  :param: None
  :return: None


.. function:: setTimestampCompressOn()

   Removes all delimiters as separators between the
   sections of the timestamp format. The output is
   a "compressed" ASCII string of only numbers and letters.
   Settings are saved and can be restored with **setTimestampCompressOff()**
 

  :param: None
  :return: None


.. function:: setTimestampCompressOff()

   Restores all delimiters as separators between the
   sections of the timestamp format from previous settings
   if currently in compressed mode. 

  :param: None
  :return: None

