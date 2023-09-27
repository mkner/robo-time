
Test
----

.. py:mod: 
.. py:mod:: py_mod


| Short command line functions to quickly 
| check on and compare formatting of all clocks
|

- Clock (UptimeClock)
- WorldClock
- SystemClock

Access the functions by importing them as

from robotime.test import *

Three clocks are already instantiated in the module:

c = robotime.test.c
wc = robotime.test.wc
sc = robotime.sc


.. function:: ts()

    prints timestamp strings for all clocks
    
  :param: None
  :return: prints timestamp string
  :rtype: None


.. function:: ts()

    short call for timestamp()

  :param: None
  :return: prints timestamp string
  :rtype: None
