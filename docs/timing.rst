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

  Example

.. code block:: python

    from roboclocks.time import Clock
    from roboclocks import Clock
    
    c = Clock()
    
    for i in range(5): 
        print(c.getUptimeStr())
        delay(1000)
    
    print()
    delay(3000) # wait 3 sec
    
    for i in range(5):
        print(c.getUptimeStr())
        delay(1000)
    
.. code block:: python

    00:00:00
    00:00:01
    00:00:02
    00:00:03
    00:00:04
    
    00:00:08
    00:00:09
    00:00:10
    00:00:11
    00:00:12


