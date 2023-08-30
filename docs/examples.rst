

Example
-------

robo-utils
**********

For example:

>>> import robo_utils

>>> from robo_utils import rad2deg, deg2rad

# use arctan2 function to bound angles to +/- 180 degrees

def bound2piDeg(angle):
    # angle and bounded angle in degrees
    # bounds angle to (+/-) 180 degrees
    return(rad2deg(np.arctan2( sin(deg2rad(angle)) ,cos(deg2rad(angle)))))



>>> from robo_utils import imap






