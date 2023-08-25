
Functions
---------

.. py:mod: 
.. py:mod:: py_mod

.. function:: imap(x, in_min, in_max, out_min, out_max)
  
   maps an integer value in the range [in_min, in_max] to interval [out_min, out_max]
   analogous to arduino map function that uses long int numeric types\
   if the vaule x non-integer type it is converted to an int
   :param parameters

   :param  x: input numeric value to map
    in_min: lower bound of input range
   :param  in_max: upper bound of input range
   :param  out_min: lower bound of output range
   :param  out_max: upper bound of output range

   :return: bounded value
   :rtype: int

  note: the input is not constrained
  use the **constrain(...)** function to bound it first
 
  a typical use of this function with robotic control would be to take a
  value in decimal range of [0,100] and map into [0,255] (or [0,FF] hex) 
  before sending it to a motor controller

.. py:function:: function(sender, recipient, message_body, [priority=1])

   Send a message to a recipient

   :param str sender: The person sending the message
   :param str recipient: The recipient of the message
   :param str message_body: The body of the message
   :param priority: The priority of the message, can be a number 1-5
   :type priority: integer or None
   :return: the message id
   :rtype: int
   :raises ValueError: if the message_body exceeds 160 characters
   :raises TypeError: if the message_body is not a basestring



 .. py:function::  indent 1 imap(x, in_min, in_max, out_min, out_max)

  .. py:function:: indent 2 imap(x, in_min, in_max, out_min, out_max)

  .. function:: imap(x, in_min, in_max, out_min, out_max)
