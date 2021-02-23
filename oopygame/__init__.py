# ~ This file is part of oopygame.

# ~ oopygame is free software: you can redistribute it and/or modify
# ~ it under the terms of the GNU General Public License as published by
# ~ the Free Software Foundation, either version 3 of the License, or
# ~ (at your option) any later version.

# ~ oopygame is distributed in the hope that it will be useful,
# ~ but WITHOUT ANY WARRANTY; without even the implied warranty of
# ~ MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# ~ GNU General Public License for more details.

# ~ You should have received a copy of the GNU General Public License
# ~ along with oopygame.  If not, see <https://www.gnu.org/licenses/>.

"""
This is an object oriented API based on pygame
"""

__version__ = "0.1.1"
__author__ = 'Py-GNU-Unix'

class OOPyException(Exception):     pass

from .window import Window, BaseWindow
from .objects import Object, BaseObject, SvgObject, PercentedObject, ShadowObject
from . import time
from . import image_tools
from . import colors
from . import demons
