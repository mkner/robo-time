Timing Functions
----------------

.. py:mod: 
.. py:mod:: py_mod

| The most frequently used timing delay functions. Some are also available on the
| various clock interfaces, but these standalone versions are decoupled here
| for more lightweight, streamlined inline requirements. For accurate and precise
| timing only **delay(...)** and **delayMicros(...)** are recommended. The other
| versions are for testing and comparative purposes only.

.. function:: delay(delay_time)

    Initiates a delay for the specified amount of time in milliseconds
    The underlying timing mechanism uses the most accurate, valid monotonic
    time available. Monotonic time moves unidirectionally forward and runs
    independently of the variations that occur with a system clock. This delay
    function can be  used safely inside a process thread. It is named after
    the **arduino** delay function.

  :param delay_time: amount of time to delay (milliseconds)

  :return: None

  Example

  | Variations on 1 second delays with 2 forms of output for uptime

.. code-block:: python
    
    from robotime.time import delay
    from robotime.clocks import Clock

    c = Clock()
    
    for i in range(5): 
        print(c.getUptimeStr())
        delay(1000)
    
    print()
    delay(1000) # wait 1 sec
    
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

|

.. function:: delayMicros(delay_time)

    Initiates a delay for the specified amount of time in microseconds
    The underlying timing mechanism uses the most accurate, 
    valid monotonic time available. This delay function can be
    used safely inside a process thread. 

  :param delay_time: amount of time to delay (microseconds)

  :return: None


  Example

.. code-block:: python
    
    from robotime.time import delayMicros
    from robotime.clocks import Clock

    c = Clock()

    for i in range(5): 
        print(c.getUptimeStr())
        delayMicros(1000000) # 1 second

.. code-block:: python

   00:00:00
   00:00:01
   00:00:02
   00:00:03
   00:00:04 


Uptime Functions
----------------

.. function:: getMonotime()

     Returns monotonic time in floating point seconds 
     since system startup or when the system board started 
     running This depends on the underlying OS/HW configuration
        
  :param: None

  :return: current monotonic time 
  :rtype: float


Alternate Delay Test Functions
------------------------------

.. function:: delaySp(delay_time)

    Initiates a delay for the specified amount of time in microseconds
    This is a time.sleep() based version of delay. Included here for comparison
    testing or other applications. Never as accurate as monotime based delay.

  :param delay_time: amount of time to delay (microseconds)

  :return: None


.. function:: delayTc(delay_time)

    Initiates a delay for the specified amount of time in microseconds
    This is a time.clock() based version of delay. Included here for 
    comparison testing or other applications. Never as accurate as 
    monotime based delay.

  :param delay_time: amount of time to delay (microseconds)

  :return: None


.. function:: delayTm(delay_time):
 
    Initiates a delay for the specified amount of time in microseconds.
    This is a time.time() based version of delay. Included here only for
    comparison testing. The timing delay mechanism can skew forward or 
    backward in time depending on the underlying OS (HW/SW) system clock and
    its adjustments for regions, time zones and other geographic related 
    parameters. Or abruptly jump or change time if the system clock is set
    or reset. Never as accurate as monotime based delay.


  :param delay_time: amount of time to delay (microseconds)

  :return: None

