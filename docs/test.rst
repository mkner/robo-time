
Test
----

.. py:mod: 
.. py:mod:: py_mod


| The test module contains short command line functions to 
| quickly check on and compare formatting of all clocks
| 

- Clock (UptimeClock)
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
