Clocks
------

.. py:mod: 
.. py:mod:: py_mod

| The three most important primary clocks are: Uptime Clock, World Clock,
| and. System Clock, The primordal clock is the Uptime Clock. Both World Clock
| and System Clock are directly derived from Clock. The projects object oriented
| design makes it easier to use the various clocks in logical and consistent way.
| There is a common interface for many features. Additional functionality is provided
| for the type of time awareness, time variations and time representation.
|


  Clock()

  SystemClock()

  WorldClock()

  Command Line 
.. function:: time()
  
Command line mode

  :param delay_time: amount of time to delay (milliseconds)

  :return: prints the current time in YYYY:MM:DD format

  Example

  | Variations on 1 second delays with 2 forms of output for uptime

.. code-block:: python

.. code-block:: python
