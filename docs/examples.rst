

Example
-------

robo-utils
**********

For example:

>>> import robo_utils

>>> from robo_utils import rad2deg, deg2rad

.. code-block:: python

 # use classic arctan2 method to bound angles to +/- 180 degrees

   def bound2piDeg(angle):
     # input: angle in degrees
     # output: bounded angle in (+/-) 180 degrees
     return(rad2deg(np.arctan2( sin(deg2rad(angle)) ,cos(deg2rad(angle)))))





>>> from robo_utils import imap






