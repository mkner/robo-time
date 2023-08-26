
"""
robo-utils  - useful functions for mobile robotics
"""

# flit uses this as one source version #
# note: pep whatever doesnt like > 'x.y.<number>c'
# for example: 0.01.08d doesnt fly building from pyproject.toml

__version__ = '0.01.03b2'

# import acts to export 

import robo_utils as roboutils # make it avail like this also

from .roboutils import imap
from .roboutils import fmap
from .roboutils import rad2deg
from .roboutils import deg2rad

from .roboutils import boundTo2pi
from .roboutils import bound2pi
    
from .roboutils import boundArctan
from .roboutils import boundAtanDeg
from .roboutils import boundAtanRad

from .roboutils import getAngleFromTo

from .roboutils import getDistanceFromTo
from .roboutils import getDistanceBetween
from .roboutils import getPointDistanceFrom

from .roboutils import mps2kmph
from .roboutils import mps2mph








