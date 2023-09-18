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
    The underlying timing mechanism uses the most accurate, 
    valid monotonic time available. This delay function can be
    used safely inside a process thread. It is an equivalent to
    the **arduino** delay function.

  :param delay_time: amount of time to delay (milliseconds)

  :return: None

  Example

  | Variations on 1 second delays with
  | 2 forms of printing out uptime 

.. code-block:: python
    
    from roboclocks.time import delay
    from roboclocks import Clock
    c = Clock()

for i in range(5): 
    print(c.getUptimeStr())
    delay(1000)

print()
delay(1000) # wait 3 sec

for i in range(5):
    print(c.getUptimeStr())
    delay(1000)
    
print()
c.delay(1000) # use delay on Clock() interface

c.uptime()

for i in range(2):
 for j in range(10): # same as delay(1000)
      delay(100)
      
 c.uptime()
 delay(1000) # same delay as j loop
 c.uptime()
 

.. code-block:: python

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
    
    00:00:14
    00:00:15
    00:00:16
    00:00:17
    00:00:18


