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

# Copyright 2020-present Py-GNU-Unix <py.gnu.unix.moderator@gmail.com>

import pygame
from . import image_tools

default_image_fn = f"{'/'.join(__file__.split('/')[:-1])}/media/icon.svg"
default_image = image_tools.load_image(default_image_fn)

X = 0
Y = 1

class BaseObject:
    def __init__(self, pos=(0,0), image=default_image, show=True, depth_level=0):
        self.show = show
        self.pos = pos
        self.size = None # The size will be setted from the image in the next line
        self.set_image(image)
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
        self.size = self.image.get_size()

    def set_depth_level(self, new_level):
        self.depth_level = new_level

    def set_pos(self, new_pos):
        self.pos = new_pos

    def set_size(self, new_size):
        self.size = new_size
        new_image = image_tools.scale_image(self.image, new_size)
        self.set_image(new_image)

    set_real_pos = set_pos
    get_real_pos = get_pos

    set_real_size = set_size
    get_real_size = get_size

#%#%#%#%#%#%#%#%#%#%#%#%#%#

class Object(BaseObject):
    def __init__(self, master_window, pos=(0,0), image=default_image, show=True, depth_level=0):
        BaseObject.__init__(self, pos, image, show, depth_level)
        self.master_window = None
        self.set_master_window(master_window)

#<><><><><><><><>#

    def move_right(self, px):
        current_pos = self.get_pos()
        self.set_pos((current_pos[X] + px, current_pos[Y]))

    def move_left(self, px):
        current_pos = self.get_pos()
        self.set_pos((current_pos[X] - px, current_pos[Y]))

    def move_up(self, px):
        current_pos = self.get_pos()
        self.set_pos((current_pos[X], current_pos[Y] - px))

    def move_down(self, px):
        current_pos = self.get_pos()
        self.set_pos((current_pos[X], current_pos[Y] + px))

#<><><><><><><><>#

    def set_master_window(self, new_master):
        if self.master_window:
            self.disconnect_from_master_window()

        new_master.add_object(self)
        self.master_window = new_master

    def disconnect_from_master_window(self):
        self.master_window.remove_object(self)
        self.master_window = None

#<><><><><><><><>#

    def is_out_of_window(self):
        pos = self.get_real_pos()
        obj_size = self.get_real_size()
        window_size = self.master_window.get_screen_size()

        for choor in X,Y:
            if pos[choor] < (0-obj_size[choor]):
                return choor, pos[choor]-(0-obj_size[choor])
            if pos[choor] > window_size[choor]:
                return choor, pos[choor] - window_size[choor]

        return False

    def is_touching_borders(self):
        pos = self.get_pos()
        obj_size = self.get_real_size()
        window_size = self.master_window.get_screen_size()

        for choor in X,Y:
            if pos[choor] < 0 and pos[choor] > -obj_size[choor]:
                return True

            border_distance = pos[choor] - window_size[choor]

            if 0 < border_distance < obj_size[choor]:
                return True

        return False

    def is_touching(self, other):
        rects = []

        for obj in self, other:
            obj_rect = obj.get_rect()
            rects.append(obj_rect)

        return rects[0].colliderect(rects[1])

    def is_clicked(self, btn_number=0):
        mouse_click = pygame.mouse.get_pressed()[btn_number]

        return bool(mouse_click and self.is_under_cursor())

    def is_under_cursor(self):
        choords_mouse = pygame.mouse.get_pos()

        if not self.master_window.is_the_cursor_in_this_window():
            return False

        my_rect = self.get_rect()
        return my_rect.collidepoint(choords_mouse)

    def get_rect(self):
        my_real_pos = self.get_real_pos()
        my_real_size = self.get_real_size()
        my_rect = pygame.Rect(my_real_pos, my_real_size)

        return my_rect
