Clocks
------

.. py:mod: 
.. py:mod:: py_mod

| The three most important primary clocks are:
| Uptime Clock, World Clock, System Clock
|
| The projects object oriented design makes it easier
| to use the clocks in logical and consistent way. 
|
| There is a common interface for all 3 clocks for many features.
| Additional functionality is provided for specific time variations.
| The primordal clock is the Uptime Clock.  Both World Clock
| and System Clock are directly derived from Clock and its interface.
| Each has additional capabilities for the type of time awareness and 
| time representation they implement.
|

  Clock()

  SystemClock()

  WorldClock()

  Command Line 
.. function:: time()
   Command line mode

     :return:  prints the current time in YYYY:MM:DD format


  :param delay_time: amount of time to delay (milliseconds)

  :return: None

  Example

  | Variations on 1 second delays with 2 forms of output for uptime

.. code-block:: python

.. code-block:: python
