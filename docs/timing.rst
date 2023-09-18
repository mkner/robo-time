Timing Functions
----------------

.. py:mod: 
.. py:mod:: py_mod

| Some of the most frequently used timing functions.
| These functions are standalone. Some are also available on the
| various clock interfaces but are decoupled here for more 
| lightweight, streamlined inline requirements. 


.. function:: delay(delay_time)

    Initiates a delay for the specified amount of time in milliseconds
    It is an equivalent to the **arduino** delay function.
    The underlying timing mechanism uses the most accurate, 
    valid monotonic time available. This delay function can be
    used safely inside a process thread.

  :param delay_time: amount of time to delay (milliseconds)

  :return: None

  


