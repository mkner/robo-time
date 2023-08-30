

Example
-------

.. |robo-utils
.. |**********

|

For example:


| Use rad/deg conversion functions and the classic 
| arctan2 method to bound angles to +/- 180 degrees
|

.. code-block:: python

   import numpy as np
   from math import sin, cos
   from robo_utils import rad2deg, deg2rad

.. code-block:: python

   def bound2PiDeg(angle): 
    
     # input: angle in degrees
     # output: bounded angle in (+/-) 180 degrees (pi radians)

     return(rad2deg(np.arctan2( sin(deg2rad(angle)) ,cos(deg2rad(angle)))))








