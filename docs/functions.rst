
Functions
---------

.. py:mod: 
.. py:mod:: py_mod

.. function:: imap(x, in_min, in_max, out_min, out_max)
  
   maps an integer value in the range **[in_min, in_max]** to interval **[out_min, out_max]**
   analogous to arduino map function that uses long int numeric types\
   if the vaule x non-integer type it is converted to an int

    x: input numeric value to map
    in_min: lower bound of input range
    in_max: upper bound of input range
    out_min: lower bound of output range
    out_max: upper bound of output range

   :return: bounded value
   :rtype: int

  note: the input is not constrained
  use the **constrain(...)** function to bound it first
 
  a typical use of this function with robotic control would be to take a
  value in decimal range of [0,100] and map into [0,255] (or [0,FF] hex) 
  before sending it to a motor controller

.. function:: fmap(x, in_min, in_max, out_min, out_max)
  
   maps an float value in the range [in_min, in_max] to interval [out_min, out_max]
  :return: bounded value

.. function:: constrain(x, xmin, xmax)
  
  bounds a numeric value to range [xmin, xmax]

  :param  x: input numeric value to map
  :param  x: input numeric value 
  :param  xmin: lower bound
  :param  xmax: upper bound

  :return: the bounded value



   

