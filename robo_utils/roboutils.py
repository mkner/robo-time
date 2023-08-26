#
#
# robo-utils - useful commonly used functions
# for mobile robotics and related applications
#
# (c) 2022 - 2023  Mike Knerr
#
# pypi releases start from dev v0.01.05b3
#
#

import numpy as np
from math import sin, cos

#pi = np.pi


def imap(x, in_min, in_max, out_min, out_max):
        # short hand ret int version of (float) fmap 
        # assumes bound checking already done
        # arduino map (that uses long numeric types) p
        y = fmap(int(x), int(in_min), int(in_max), \
                      int(out_min), int(out_max) ) 
        return int(y) #make sure
    
    
def fmap(x, in_min, in_max, out_min, out_max):
   #float map , really depends on python
  return (x - in_min) * (out_max - out_min) \
         / (in_max - in_min) + out_min


# imap(50, 0,100, 0,255)
# imap(0, 0,100, 0,255)
# imap(100, 0,100, 0,255)
# imap(49, 0,100, 0,255)


# important note  the difference
#fmap(1024/2,0,1024,0,255) # 127.5
#imap(1024/2,0,1024,0,255) # 127 GOOD! 

def constrain(x, xmin, xmax):
    return min(xmax, max(xmin, x))

def relerr(measured,expected):
    return (measured-expected)/expected

def rad2deg(radian):
    degree = radian/0.017453292519943295
    return degree

def deg2rad(deg):
    rad = deg*0.017453292519943295
    #rad = deg*((2*np.pi)/360)
    return rad

def radPerSecToRpm(rps):
    a = (rps*60)/(2*np.pi) # better fpoint
    return a
   
def rpmToRadPerSec(rpm):
    a = (rpm/60)*(2*np.pi)
    return a


def degPerSecToRadPerSec(deg):
    # better fpoint 
    a = fmap(deg,0,360,0,2*np.pi)
    return a
    #return deg*0.017453292519943

def radPerSecToDegPerSec(rad):
    a = fmap(rad,0,2*np.pi,0,360)
    return a
    #return rad*57.295779513082


def boundTo2pi(angle):
    # angle and bounded angle in radians
    # wind or unwind
    while (angle > 2.0 * np.pi):
        angle -= 2.0 * np.pi

    while (angle < -2.0*np.pi):
        angle += 2.0 * np.pi

    return angle;


#rad2deg(boundTo2pi(2*np.pi+(1/4)*np.pi))
#Out[11]: 45.0
#rad2deg(boundTo2pi(2*np.pi+(1/4)*2*np.pi))
#Out[9]: 90.0

def bound2pi(angle):
    # angle and bounded angle in radians
    return(np.arctan2(sin(angle),cos(angle)))


def getAngleFromTo(x0,y0,x1,y1,deg360=False):
    # 
    # return angle (in degrees) of line segment
    # from (x0,y0) to (x1,y1)  in WCF world coordinate frame
    # uses usual trig conventions for signed angles of rotation
    # positive angle are to left (counter-clockwise)
    # negative angles are to right (clockwise)
    # corresponds to normal rotation angle signs
    # handles no angle, vertical & horizontal lines ok
    # sees point directly behind on line as (+/-180) ok
    # keeps angles in [-180,180]  ([-pi,pi]) by default
    # set deg360 = True flag on to express angles in [0,360]
    # useful for turning to a point by spinning around in place

    dx = (x1-x0)
    dy = (y1-y0)

    if (dy != 0): #vertical line
      if (dx == 0 ):
          dx = dx+0.000000000000000001 #works

    angle=rad2deg(np.arctan2(dy,dx)) #atan2(dy/dx))

    if (deg360 == True):

      # keep no angle as 0 deg
      if (angle == 0):
          return 0
      else:
          return rad2deg(boundto2pi(deg2rad(360+angle)))
      
    else: # keep in [-180,180]
    
      return angle


def getDistanceFromTo(x0,y0,x1,y1):
    #usual 2-space euclidian
    d = np.sqrt(((x1-x0)**2 +(y1-y0)**2))
    return(d)


def getDistanceBetween(x0,y0,x1,y1):
    # aka
    d = getDistanceFromTo(x0,y0,x1,y1)
    return(d)


def getPointDistanceFrom(x0,y0,distance,angle):
    # angle is in degrees
    # distance can be signed?
    theta = deg2rad(angle)
    x1 = x0+distance*cos(theta)
    y1 = y0+distance*sin(theta)
    return(x1,y1)

def boundArctan(theta):
    # aka 
    return boundAtanDeg(theta)
    
def boundAtanDeg(theta):
#def boundArctan(theta):
    # degrees version
    # best way to keep rotations bounded
    # with +- angles & differential drive robots!
    # its not clever, just clearer?
    alpha = theta
    alpha = deg2rad(alpha)
    alpha= np.arctan2(np.sin(alpha),np.cos(alpha))
    alpha = rad2deg(alpha)
    return alpha

def boundAtanRad(theta):
    # radian version
    return np.arctan2(np.sin(theta),np.cos(theta))
    
# conversion constants
#        self._to_mph=2.237 # meters per second to mph
#        self._to_kmph=3.6 # meters per second to kmph


def mps2kmph( mps):
        # meters per second to kmph
        return mps * 3.6 # meters per second to kmph

def mps2mph(mps):
        # meters per second to mph
        return mps * 2.237 # meters per second to mph
        
# was put in wheel?
#def velocityToRate(v,wheel):
#    # wheel angular velocity omega is w hter
#    r = wheel.getRadius()
#    max_rpm = wheel.motor.getMaxRpm()
#    w = v/r
#    rpm  = abs(radPerSecToRpm( w))
#   rate = fmap(rpm,0,max_rpm,0,100)
#    
#    return(rate)


