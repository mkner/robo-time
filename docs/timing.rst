Functions
---------

.. py:mod: 
.. py:mod:: py_mod

.. function:: delay(delay_time)

    Initiates a delay for the specified amount of time in milliseconds
    It is an equivilent to the arduino delay function.
    The underlying timing mechanism uses the most accurate, 
    valid monotonic time available. This delay function can be
    used safely inside a process thread

  :param delay_time: amount of time to delay (milliseconds)

  :return: None

  


