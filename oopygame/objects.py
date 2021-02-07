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

import sys
from . import image_tools

default_image_fn = f"{'/'.join(__file__.split('/')[:-1])}/icon.svg"
default_image = image_tools.load_image(default_image_fn)

x = 0
y = 1


class BaseObject:
    def __init__(self, pos=(0,0), depth_level=0, image=default_image):
        self.pos = pos
        self.image = image
        self.depth_level = depth_level

#<><><><><><><><>#

    def get_image(self):
        return self.image 
    
    def get_depth_level(self):
        return self.depth_level

    def get_pos(self):
        return self.pos

#<><><><><><><><>#

    def set_image(self, new_image):
        self.image = new_image

    def set_depth_level(self, new_level):
        self.depth_level = new_level

    def set_pos(self, new_pos):
        self.pos = new_pos
    
    set_real_pos = set_pos
    get_real_pos = get_pos

#°*°*°*°*°*°*°*°*°*°*°*°*°*°*°*#
        
class Object(BaseObject):
    def __init__(self, master_window, pos=(0,0), depth_level=0,
            image=default_image, size=None):
                
        BaseObject.__init__(
            self, pos=pos, depth_level=depth_level, image=image)
            
        self.master_window = master_window
        self.size = size if size else image.get_size()
        
        self.master_window.add_object(self)

#<><><><><><><><>#
    
    def move_right(self, px):
        current_pos = self.get_pos()
        self.set_pos((current_pos[x] + px, current_pos[y]))
        
    def move_left(self, px):
        current_pos = self.get_pos()[x]
        self.set_pos((current_pos[x] - px, current_pos[y]))
        
    def move_up(self, px):
        current_pos = self.get_pos()[y]
        self.set_pos((current_pos[x] + px, current_pos[y]))
        
    def move_down(self, px):
        current_pos = self.get_pos()[y]
        self.set_pos((current_pos[x] - px, current_pos[y]))
        
#<><><><><><><><>#

    def set_master_window(self, new_master):
        self.master_window = new_master
        
    def set_size(self, new_size):
        print(f"set_size method is deprecated for {self.__class__}", file=sys.stderr)
        
        self.size = new_size
        new_image = image_tools.scale_image(self.image, new_size)
        self.set_image(new_image)

#<><><><><><><><>#
        
    def get_size(self):
        return self.size
        
#<><><><><><><><>#
    
    def is_out_of_window(self):
        pos = self.get_real_pos()
        obj_size = self.get_size()
        window_size = self.master_window.get_window_size()
        
        for choor in x,y:
            if pos[choor] < (0-obj_size[choor]):
                return True
            if pos[choor] > window_size[choor]:
                return True
        
        return False
        
    def is_touching_borders(self):
        pos = self.get_pos()
        obj_size = self.get_size()
        window_size = self.master_window.get_window_size()
        
        for choor in x,y:
            if pos[choor] < 0:
                return True
            if pos[choor] + obj_size[choor] > window_size[choor]:
                return True
        
        return False

class SvgObject(Object):
    def __init__(self, master_window, filename=default_image_fn, 
            pos=(0,0), depth_level=0, size=None):
        
        image = image_tools.load_svg(filename, size)
        self.filename = filename
        
        Object.__init__(self, master_window=master_window, pos=pos, 
            image=image, depth_level=depth_level, size=size)

    def set_size(self, new_size):
        self.size = new_size
        new_image = image_tools.load_svg(self.filename, new_size)
        self.set_image(new_image)
    
    def set_filename(self, new_fn):
        self.filename = new_fn
    
    def get_filename(self):
        return self.filename

class PercentedObject(Object):
    def get_real_pos(self):
        x_pos = self.master_window.perc_to_px(self.pos[x], "x")
        y_pos = self.master_window.perc_to_px(self.pos[y], "y")
        return x_pos, y_pos
    
    def set_real_pos(self, new_pos):
        x_pos = self.master_window.px_to_perc(new_pos[x], "x")
        y_pos = self.master_window.px_to_perc(new_pos[y], "y")
        self.set_pos(x_pos, y_pos)        
        
