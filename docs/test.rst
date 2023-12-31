
Test
----

.. py:mod: 
.. py:mod:: py_mod


| The test module contains short command line functions to 
| quickly check on and compare formatting of all clocks
| 

- Clock
- WorldClock
- SystemClock

Access the functions by importing them as

.. code-block:: python

 from robotime.test import *

Three clocks are already instantiated in the module:

| c  - Clock
| wc - WorldClock
| sc - SystemClock
|

Functions
*********

For the current configuration use this function:

.. function:: vers()

   prints out current versions for robotime modules
    
  :param: None
  :return: prints module version ids

Every function below calls all 3 clocks in the order:

- Clock
- WorldClock
- SystemClock

This allows a side-by-side comparison to check on the the output type
settings and format


.. function:: up()

    calls uptime() 

  :param: None
  :return: None

.. function:: now()

    calls now() 

  :param: None
  :return: None

.. function:: date()

    calls date() 

  :param: None
  :return: None

.. function:: time()

    calls time() 

  :param: None
  :return: None

.. function:: today()

    calls today() 

  :param: None
  :return: None


.. function:: ts()

    calls timestamp() 
    
  :param: None
  :return: none


.. function:: tsr()

    calls getTimestampStr() 
    
  :param: None
  :return: timestamp strings


.. function:: tsi()

    calls getTimestampInt() 
    
  :param: None
  :return: timestamp tuples


.. function:: tsf()

    calls getTimestampFp()
    
  :param: None
  :return: timestamps in floating point form


.. function:: tsf()

    calls getTimestampFp()
    
  :param: None
  :return: timestamps in floating point form


.. function:: upfp()

    calls getUptimeFp()
    
  :param: None
  :return: clocks uptimes in floating point form


.. function:: ep()

    calls epoch()
    
  :param: None
  :return: clocks epoch start date/time 


The **roll()** function cycles through most of the test functions
to get a quick overview of the timestamp outputs and current formating

.. function:: roll()

    The most useful for quick comparisions
    calls most of the above functions in sequence
    
  :param: None
  :return: None


.. function:: setTstype(ts)

   sets the timestamp type 
   calls setTimestampFormat(ts)

  :param: ts
  :return: None


.. function:: getTstype()

   gets the timestamp type for all 3 clocks
   calls getTimestampFormat()

  :param: None
  :return: format types


.. function:: setbasic()

   calls setTstype('basic') 

  :param: None
  :return: None


.. function:: setlocal()

   calls setTstype('iso-local') 

  :param: None
  :return: None


.. function:: setutc()

   calls setTstype('iso-utc')

  :param: None
  :return: None


.. function:: setcompon()

   calls setTimestampCompressedOn()

  :param: None
  :return: None


.. function:: setcompoff()

   calls setTimestampCompressedOff()

  :param: None
  :return: None


.. function:: ztailon()

   calls setZtailOn()

  :param: None
  :return: None


.. function:: ztailoff()

   calls setZtailOff()

  :param: None
  :return: None


.. function:: setresMicros()

   calls setTimestampRes('micro')

  :param: None
  :return: None


.. function:: setresMillis()

   calls setTimestampRes('milli')

  :param: None
  :return: None


.. function:: setresOff()

   calls setTimestampRes('none')

  :param: None
  :return: None




