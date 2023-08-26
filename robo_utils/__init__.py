
"""
robo-utils  - useful functions for mobile robotics
"""

# flit uses this as one source version #
# note: pep whatever doesnt like > 'x.y.<number>c'
# for example: 0.01.08d doesnt fly building from pyproject.toml

__version__ = '0.01.03b1'

# import acts to export 

import .roboutils as roboutils # make it avail like this also

from .roboutils import imap
from .roboutils import fmap
from .roboutils import rad2deg
from .roboutils import deg2rad

from .roboutils import boundTo2pi







