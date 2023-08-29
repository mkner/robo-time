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

  :param  rad:  input angle in radians

  :return: angle in degrees
  :rtype: float


.. function:: deg2rad(deg)

   converts angle in degrees to radians

  :param  deg:  input angle in degrees

  :return: angle in radians
  :rtype: float


.. function::  bound2pi(angle)

  bounds angle to (+/-) pi radians

  :param  angle: angle in radians

  :return: bounded angle in radians
  :rtype: float


.. function::  bound2piDeg(angle)

  bounds angle to (+/-) 180 degrees

  :param  angle: angle in degrees

  :return: bounded angle in degrees
  :rtype: float


.. function::  boundTo2pi(angle)

  bounds angle into one circular rotation of 2 pi radians (360 degrees)
  so even if input is spinning perpertually to an even greater (or lesser) 
  angle, the output is contained into only one equivalent full circular 
  rotation of 2 pi radians (360 degres)

  :param  angle: angle in radians

  :return: bounded angle in radians
  :rtype: float


.. function::  radPerSecToRpm(rps)

   converts angular velocity in radians per second
   to RPM (revolutions per minute)

  :param  rps:  angular velocity in radians per second

  :return: angular velocity in revolutions per second
  :rtype: float


.. function::  rpmToRadPerSec(rpm)

   converts angular velocity in RPM (revolutions per minute)
   to radians per second

  :param  rpm:  angular velocity in RPM

  :return: angular velocity radians per second
  :rtype: float


.. function::  degPerSecToRadPerSec(dps)

   converts angular rotational rate in degrees per second
   to radians per second

  :param  deg:  angular rotational rate in degrees per second 

  :return: angular rotational rate in radians per second
  :rtype: float


.. function::  radPerSecToDegPerSec(rps)

   converts angular rotational rate in radians per second
   to degrees per second

  :param  rad: angular rotational rate in radians per second 

  :return: angular rotational rate in degrees per second
  :rtype: float


.. function::  mps2kmph(mps)

   converts meters per second to kmph

  :param  mps: rate in meters per second

  :return: rate in kilometers per hour

  :rtype: float

.. function::  mps2mph(mps)

   converts meters per second to mph

  :param  mps: rate in meters per second

  :return: rate in miles per hour

  :rtype: float


.. function::  getDistance(x0,y0,x1,y1)

   usual 2-space euclidian distance

  :param  x0: start pos x
  :param  y0: start pos y
  :param  x1: end pos x
  :param  y1: end pos y

  :return: distance

  :rtype: float


.. function::  getDistanceFromTo(x0,y0,x1,y1)

  same as getDistance(x0,y0,x1,y1)


.. function::  getPositionAt(x0,y0, d, theta)

  returns point (x1,y1) of position d distance away
  from (x0,y0) at relative angle theta

  Useful for getting the point of a remote object when using ranging sensors
  For example, IR sensors, that return distance at a known sensor mounting angle
  theta relative to robots frame forward heading when robot is at current position (x0,y0)

  :param  x0: start pos x
  :param  y0: start pos y
  :param  d: distance from some current position (x0,y0) to remote point
  :param  theta: angle (deg) relative to current heading (x0,y0) to remote point
 
  :return: (x1,y1): tuple of remote coordinates 

  :rtype: float


.. function::  getAngleFromTo(x0,y0,x1,y1,<deg360>)

  
  :param  x0: start pos x
  :param  y0: start pos y
  :param  x1: end pos x
  :param  y1: end pos y
  :param  deg360:  = False (default) to bound angle to 180 degrees
                   = True to  bound in full rotation of 360 degrees
 
  :return: angle in degrees

  :rtype: float







