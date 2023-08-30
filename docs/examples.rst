

Example
-------

robo-utils
**********

For example:


| Use rad/deg conversion functions and the classic 
| arctan2 method to bound angles to +/- 180 degrees
|


>>> from robo_utils import rad2deg, deg2rad

.. code-block:: python

   def bound2piDeg(angle): 
    
     # input: angle in degrees
     # output: bounded angle in (+/-) 180 degrees
     return(rad2deg(np.arctan2( sin(deg2rad(angle)) ,cos(deg2rad(angle)))))





>>> from robo_utils import imap






