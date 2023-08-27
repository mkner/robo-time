
Functions
---------

.. py:mod: 
.. py:mod:: py_mod

.. function:: imap(x, in_min, in_max, out_min, out_max)
  
   maps an integer value in the range **[in_min, in_max]** to interval **[out_min, out_max]**
   analogous to arduino map function that uses long int numeric types
   if the value x is a non-integer type it is converted to an int

  :param x: input numeric value to map
  :param in_min: lower bound of input range
  :param in_max: upper bound of input range
  :param out_min: lower bound of output range
  :param out_max: upper bound of output range

  :return: bounded value
  :rtype: int

  note: the input is *not* constrained
  use the **constrain(...)** function to bound it first if required
 
  a typical use of this function with robotic control would be to take a
  value in decimal range of **[0,100]** and map into **[0,255]** (**[0,FF]** hex) 
  before sending it to a motor controller

.. function:: fmap(x, in_min, in_max, out_min, out_max)
  
   maps an float value in the range **[in_min, in_max]** to interval **[out_min, out_max]**
  
  :param x: input numeric value to map
  :param in_min: lower bound of input range
  :param in_max: upper bound of input range
  :param out_min: lower bound of output range
  :param out_max: upper bound of output range

  :return: bounded value
  :rtype: float

.. function:: constrain(x, xmin, xmax)
  
   bounds a numeric value to range **[xmin, xmax]**

  :param  x: input numeric value 
  :param  xmin: lower bound
  :param  xmax: upper bound

  :return: bounded value


.. function:: rad2deg(rad)

   converts angle in radians to degrees

  :param  rad: input angle in radians

  :return: angle in degrees
  :rtype: float


.. function:: deg2rad(deg)

   converts angle in degrees to radians

  :param  deg: input angle in degrees

  :return: angle in radians
  :rtype: float


.. function::  radPerSecToRpm(rps)

   converts angular velocity in radians per second
   to RPM (revolutions per minute)

  :param  rps - angular velocity in radians per second

  :return: angular velocity in revolutions per second
  :rtype: float


.. function::  rpmToRadPerSec(rpm)

   converts angular velocity in RPM (revolutions per minute)
   to radians per second

  :param  rpm - angular velocity in RPM

  :return: angular velocity radians per second
  :rtype: float


.. function::  degPerSecToRadPerSec(deg)

   converts angular rotational rate in degrees per second
   to radians per second

  :param  rpm - angular rotational rate in degrees per second 

  :return: angular rotational rate in radians per second
  :rtype: float


.. function::  radPerSecToDegPerSec(rad)

   converts angular rotational rate in radians per second
   to degrees per second

  :param  rpm - angular rotational rate in radians per second 

  :return: angular rotational rate in degrees per second
  :rtype: float



