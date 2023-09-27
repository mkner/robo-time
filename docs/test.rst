
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

Functions
*********

Every function below calls all 3 clocks:

.. function:: up()

    calls uptime() 

  :param: None
  :return: None

.. function:: now()

    calls now() 

  :param: None
  :return: None


.. function:: ts()

    calls timestamp() 
    
  :param: None
  :return: none




