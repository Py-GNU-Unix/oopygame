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
import pygame
from . import image_tools

default_image_fn = f"{'/'.join(__file__.split('/')[:-1])}/icon.svg"
default_image = image_tools.load_image(default_image_fn)

platform_image_fn = f"{'/'.join(__file__.split('/')[:-1])}/platform.png"
platform_image = image_tools.load_image(platform_image_fn)

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

    def get_size(self):
        return self.size

#<><><><><><><><>#

    def set_image(self, new_image):
        self.image = new_image

    def set_depth_level(self, new_level):
        self.depth_level = new_level

    def set_pos(self, new_pos):
        self.pos = new_pos

    def set_size(self, new_size):
        print(f"set_size method is deprecated for {self.__class__}", file=sys.stderr)

        self.size = new_size
        new_image = image_tools.scale_image(self.image, new_size)
        self.set_image(new_image)

    set_real_pos = set_pos
    get_real_pos = get_pos

    set_real_size = set_size
    get_real_size = get_size

#°*°*°*°*°*°*°*°*°*°*°*°*°*°*°*#

class Object(BaseObject):
    def __init__(self, master_window, pos=(0,0), depth_level=0,
            image=default_image, size=None, show=True):

        self.show = show
        BaseObject.__init__(
            self, pos=pos, depth_level=depth_level, image=image)

        self.set_master_window(master_window)

        if size:
            self.size = size
            self.image = image_tools.scale_image(self.image, size)
        else:
            self.size = image.get_size()

#<><><><><><><><>#

    def move_right(self, px):
        current_pos = self.get_pos()
        self.set_pos((current_pos[x] + px, current_pos[y]))

    def move_left(self, px):
        current_pos = self.get_pos()
        self.set_pos((current_pos[x] - px, current_pos[y]))

    def move_up(self, px):
        current_pos = self.get_pos()

        self.set_pos((current_pos[x], current_pos[y] - px))

    def move_down(self, px):
        current_pos = self.get_pos()
        self.set_pos((current_pos[x], current_pos[y] + px))

#<><><><><><><><>#

    def set_master_window(self, new_master):
        self.master_window = new_master
        self.master_window.add_object(self)

#<><><><><><><><>#

    def is_out_of_window(self):
        pos = self.get_real_pos()
        obj_size = self.get_real_size()
        window_size = self.master_window.get_window_size()

        for choor in x,y:
            if pos[choor] < (0-obj_size[choor]):
                return choor, pos[choor]-(0-obj_size[choor])
            if pos[choor] > window_size[choor]:
                return choor, pos[choor] - window_size[choor]

        return False

    def is_touching_borders(self):
        pos = self.get_pos()
        obj_size = self.get_real_size()
        window_size = self.master_window.get_window_size()

        for choor in x,y:
            if pos[choor] < 0 and pos[choor] > -obj_size[choor]:
                return True

            border_distance = pos[choor] - window_size[choor]
            if border_distance < obj_size[choor] and border_distance > 0:
                return True

        return False

    def is_touching(self, other):
        rects = []

        for obj in self, other:
            obj_rect = obj.get_rect()
            rects.append(obj_rect)

        return rects[0].colliderect(rects[1])

    def is_clicked(self, btn_number=0):
        mouse_status = pygame.mouse.get_pressed()[btn_number]

        if mouse_status:
            return self.is_under_cursor()

    def is_under_cursor(self):
        choords_mouse = pygame.mouse.get_pos()
        my_rect = self.get_rect()
        return my_rect.collidepoint(choords_mouse)

    def get_rect(self):
        my_real_pos = self.get_real_pos()
        my_real_size = self.get_real_size()
        my_rect = pygame.Rect(my_real_pos, my_real_size)

        return my_rect

    def get_side(self, side, side_size=5):
        my_real_pos = self.get_real_pos()
        my_real_size = self.get_real_size()

        if side == "up":
            my_real_size = (my_real_size[0], side_size)

        elif side == "down":
            my_real_pos = (my_real_pos[0], my_real_pos[1]+my_real_size[1]-side_size)
            my_real_size = (my_real_size[0], side_size)

        elif side == "right":
            my_real_pos = (my_real_pos[0]+my_real_size[0], my_real_pos[1]-side_size)
            my_real_size = (side_size, my_real_size[1])

        elif side == "left":
            my_real_size = (side_size, my_real_size[0])

        else:
            raise TypeError(f"unknow side {side}")

        my_side = pygame.Rect(my_real_pos, my_real_size)

        return my_side


#°*°*°*°*°*°*°*°*°*°*°*°*°*°*°*#

class SvgObject(Object):
    def __init__(self, master_window, filename=default_image_fn,
            pos=(0,0), depth_level=0, size=None, *args, **kwargs):

        image = image_tools.load_svg(filename, size)
        self.filename = filename

        Object.__init__(self, master_window=master_window, pos=pos,
            image=image, depth_level=depth_level, size=size, *args, **kwargs)

    def set_size(self, new_size):
        self.size = new_size
        new_image = image_tools.load_svg(self.filename, new_size)
        self.set_image(new_image)

    def set_filename(self, new_fn):
        self.filename = new_fn

    def get_filename(self):
        return self.filename

#°*°*°*°*°*°*°*°*°*°*°*°*°*°*°*#

class PercentedObject(Object):
    def __init__(self, master_window, pos=(0,0), depth_level=0,
            image=default_image, size=None):

        BaseObject.__init__(
            self, pos=pos, depth_level=depth_level, image=image, *args, **kwargs)

        self.set_master_window(master_window)
        if not size:
            size = image.get_size()
            self.set_real_size(size)
        else:
            self.set_size(size)

#<><><><><><><><>#

    def get_real_pos(self):
        x_pos = self.master_window.perc_to_px(self.pos[x], "x")
        y_pos = self.master_window.perc_to_px(self.pos[y], "y")
        return x_pos, y_pos

    def get_real_size(self):
        real_size_x = self.master_window.perc_to_px(self.size[x], "x")
        real_size_y = self.master_window.perc_to_px(self.size[y], "y")

        return real_size_x, real_size_y

    def get_size(self):
        return self.size

    def get_image(self):
        real_size = self.get_real_size()
        return image_tools.scale_image(self.image, real_size)

#<><><><><><><><>#

    def set_real_pos(self, new_pos):
        x_pos = self.master_window.px_to_perc(new_pos[x], "x")
        y_pos = self.master_window.px_to_perc(new_pos[y], "y")
        self.set_pos((x_pos, y_pos))

    def set_real_size(self, new_size):
        size_x = self.master_window.px_to_perc(new_size[x], "x")
        size_y = self.master_window.px_to_perc(new_size[y], "y")

        self.set_size((size_x, size_y))

    def set_size(self, new_size):
        self.size = new_size

class ShadowObject(Object):
    """
    Only for debugging
    """
    def __init__(self, *args, **kwargs):
        Object.__init__(self, *args, **kwargs)
        rect = self.get_rect()
        self.image = pygame.Surface((rect.w,rect.h))
