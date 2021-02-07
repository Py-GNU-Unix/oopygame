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

import pygame
import sys
import os

from . import image_tools
from . import colors

common_window_flags = pygame.RESIZABLE | pygame.SCALED | pygame.DOUBLEBUF

default_icon = f"{'/'.join(__file__.split('/')[:-1])}/icon.svg"

x = 0
y = 1


class NotInizializedScreen: pass


class BaseWindow:
    def __init__(self, size=(500, 500), pos=None, flags=0):
        self.open_size = size
        self.flags = flags
        self.screen = NotInizializedScreen()
        self.objects = {}

        self.init_pygame()
        self.set_window_open_point(pos)

    # <><><><><><><><>#

    @staticmethod
    def init_pygame():
        pygame.init()

    def open_window(self):
        self.screen = pygame.display.set_mode(self.open_size, self.flags)

    @staticmethod
    def detect_key(key):
        all_keys = pygame.key.get_pressed()
        return all_keys[key]

    def do_routine(self):
        self.have_to_close()
        self.update()

    def have_to_close(self):
        for event in pygame.event.get(eventtype=pygame.QUIT):
            pygame.quit()
            sys.exit(0)

    def update(self):
        self.clear_screen()
        self.blit_objects()
        pygame.display.update()

    def clear_screen(self, color=colors.black):
        self.screen.fill(color)

    # <><><><><><><><>#

    def add_object(self, new_obj):
        depth_level = new_obj.get_depth_level()
        created_depth_levels = self.objects.keys()

        if depth_level not in created_depth_levels:
            self.objects[depth_level] = [new_obj]
        else:
            self.objects[depth_level].append(new_obj)

    def remove_object(self, obj):
        obj_depth_level = obj.get_depth_level()

        try:
            self.objects[obj_depth_level].remove(obj)
        except ValueError:
            raise ValueError(f"Object {obj} isn't in {self}.objects.")

        obj.set_master_window(None)

    def get_objects_depth_levels(self):
        depth_levels_list = list(self.objects.keys())
        depth_levels_list.sort()

        return depth_levels_list

    def blit_objects(self):
        depth_levels_list = self.get_objects_depth_levels()

        for depth_level in depth_levels_list:
            objects_on_this_level = self.objects[depth_level]

            for object_to_blit in objects_on_this_level:
                object_position = object_to_blit.get_real_pos()
                object_image = object_to_blit.get_image()
                self.screen.blit(object_image, object_position)

    # <><><><><><><><>#

    @staticmethod
    def get_monitor_size():
        size = os.popen("xdpyinfo | awk '/dimensions:/ { print $2 }'").read()
        size = map(int, size.split("x"))
        return list(size)

    def get_window_size(self):
        return pygame.display.get_surface().get_size()

    # <><><><><><><><>#

    def set_cursor(self, cursor):
        pygame.mouse.set_cursor(cursor)

    def set_icon(self, new_icon):
        if type(new_icon) == str:
            new_icon = image_tools.load_image(new_icon)

        pygame.display.set_icon(new_icon)

    def set_title(self, new_title):
        pygame.display.set_caption(new_title)

    def set_window_open_size(self, new_size):
        self.open_size = new_size

    def set_window_open_point(self, pos):
        if pos is None:
            pass
        else:
            pos = f"{pos[x]},{pos[y]}"
            os.environ['SDL_VIDEO_WINDOW_POS'] = pos


# °*°*°*°*°*°*°*°*°*°*°*°*°*°*°*#


class Window(BaseWindow):
    def __init__(self, size=(500, 500), pos=None, icon=default_icon,
                 flags=common_window_flags, title=None, 
                 bg_color=colors.black):
                     
        BaseWindow.__init__(self, size=size, pos=pos, flags=flags)
        self.set_icon(icon)
        self.bg_color = bg_color

        if not title:
            title = Window.generate_default_title()

        self.set_title(title)
        self.open_window()

    def update(self, blit_objs=True):
        self.clear_screen(self.bg_color)
        self.blit_objects()
        pygame.display.update()
        
        
    @staticmethod
    def generate_default_title():
        import __main__
        base_file = __main__.__file__
        return base_file + " - OOPygame"

    def px_to_perc(self, n_pixels, mode, round_func=int):
        mode = 0 if mode == "x" else 1
        window_size = self.get_window_size()
        perc = round_func(100 / (window_size[mode] / n_pixels))
        return perc

    def perc_to_px(self, perc, mode, round_func=int):
        mode = 0 if mode == "x" else 1
        window_size = self.get_window_size()
        px = round_func(window_size[mode] / 100 * perc)
        return px
