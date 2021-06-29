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

import os
import pygame

from . import colors, image_tools
from .exceptions import NotInizializedScreenError

X = 0
Y = 1


class NotInizializedScreen:
    def __getattribute__(self, _):
        raise NotInizializedScreenError("The screen hasn't been inizialized yet!")

class PygameScreenBackend:
    def __init__(self, screen_size, screen_flags=0):
        self.screen = NotInizializedScreen()
        self.screen_size = screen_size
        self.screen_flags = screen_flags
        self.events = tuple()
        self.init_pygame()
    
    def open_window(self):
        self.screen = pygame.display.set_mode(self.screen_size, self.screen_flags)
    
    def fill(self, color):
        self.screen.fill(color)
    
    @staticmethod
    def get_screen_size():
        return pygame.display.get_surface().get_size()
    
    @staticmethod
    def detect_key(key):
        all_keys = pygame.key.get_pressed()
        return all_keys[key]

    @staticmethod
    def get_monitor_size():
        info = pygame.display.Info()
        return info.current_w, info.current_h

    @staticmethod
    def have_to_close():
        for event in pygame.event.get(eventtype=pygame.QUIT):
            return True
        return False

    @staticmethod
    def close_if_need():
        if PygameScreenBackend.have_to_close():
            pygame.quit()

            import sys
            sys.exit(0)

    def clear_screen(self, bg_color=colors.black):
        self.fill(bg_color)

    @staticmethod
    def is_focused():
        return pygame.mouse.get_focused()
    
    @staticmethod
    def get_window_size():
        return pygame.display.get_surface().get_size()
    
    @staticmethod
    def set_icon(new_icon):
        if isinstance(new_icon, str):
            new_icon = image_tools.load_image(new_icon)

        pygame.display.set_icon(new_icon)
    
    @staticmethod
    def set_window_open_point(pos):
        if pos is None:
            pass
        else:
            pos = f"{pos[X]},{pos[Y]}"
            os.environ['SDL_VIDEO_WINDOW_POS'] = pos

    def update_events(self):
        new_events = pygame.event.get()
        self.events = new_events

    def get_events(self, eventtype=None):
        for event in self.events:
            if not eventtype or event.type==eventtype:
                yield event

    def blit(self, image, pos):
        self.screen.blit(image, pos)

    init_pygame = pygame.init

    update = pygame.display.update

    is_focused = pygame.mouse.get_focused

    set_cursor_visibility = pygame.mouse.set_visible

    get_cursor_pos = pygame.mouse.get_pos

    set_title = pygame.display.set_caption
    
