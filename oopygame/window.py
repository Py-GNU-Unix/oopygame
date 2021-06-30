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

import operator

from . import screen_backend
from . import colors
from . import exceptions
from . import image_tools

default_icon_fn=f"{'/'.join(__file__.split('/')[:-1])}/media/icon.svg"
default_icon = image_tools.load_image(default_icon_fn)

class Window:
    def __init__(self, size, flags=0, title=None, bg_color=colors.white, 
                icon=default_icon, screen=screen_backend.PygameScreenBackend,
                open_point=None):
        
        self.screen = screen(size, flags)
        self.set_icon(icon)
        self.bg_color = bg_color
        self.objects = []
        self.screen.set_window_open_point(open_point)
        self.screen.open_window()

        if not title:
            self.title = self.generate_default_title()
        else:
            self.title = title
        self.set_title(self.title)

    def update(self):
        self.screen.close_if_need()
        self.screen.fill(self.bg_color)
        self.blit_objects()
        self.screen.update()

    def close_if_need(self):
        self.screen.close_if_need()

#<><><><><><><>#

    def add_object(self, *new_objects):
        self.objects = self.objects + list(new_objects)
        self.objects.sort(key=operator.attrgetter('depth_level'))

    def remove_object(self, *objects_to_delete):
        try:
            [ self.objects.remove(object) for object in objects_to_delete ]

        except ValueError as previous_error:
            new_error = exceptions.MissingObjectException("Unable to remove object, not in list")
            raise new_error from previous_error

    def blit_objects(self):
        for object_to_blit in self.objects:
            if object_to_blit.show:
                object_position = object_to_blit.get_real_pos()
                object_image = object_to_blit.get_image()
                self.screen.blit(object_image, object_position)

#<><><><><><><>#

    def get_screen_size(self):
        return self.screen.get_screen_size()

    def detect_key(self, key):
        return self.screen.detect_key(key)

    def get_monitor_size(self):
        return self.screen.get_monitor_size()

    def is_focused(self):
        return self.screen.is_focused()

    def get_events(self, eventtype=None):
        return self.screen.get_events(eventtype)

    def get_cursor_pos(self):
        return self.screen.get_cursor_pos()

#<><><><><><><>#

    def set_title(self, new_title):
        self.screen.set_title(new_title)

    @staticmethod
    def generate_default_title():
        import __main__
        return __main__.__file__ + " - OOPygame"

    def set_icon(self, new_icon):
        self.icon = new_icon
        self.screen.set_icon(new_icon)

    def set_bg_color(self, new_bg_color):
        self.bg_color = new_bg_color

    def set_cursor_visibility(self, state):
        self.screen.set_cursor_visibility(state)

#<><><><><><><>#

    def run(self):
        raise NotImplementedError
