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

from . import screen_backend
from . import colors
from . import exceptions
from . import image_tools

default_icon_fn=f"{'/'.join(__file__.split('/')[:-1])}/media/icon.svg"
default_icon = image_tools.load_image(default_icon_fn)

class Window:
    def __init__(self, size, flags=0, title=None, bg_color=colors.white, 
                icon=default_icon, screen=screen_backend.PygameScreenBackend):
        
        self.screen = screen(size, flags)

        if not title:
            self.title = self.generate_default_title()
        else:
            self.title = title
        self.set_title(self.title)

        self.bg_color = bg_color

        self.icon = icon
        self.set_icon(icon)

        self.objects = []
        self.screen.open_window()

    def update(self):
        self.screen.close_if_need()
        self.screen.fill(self.bg_color)
        self.screen.update()

#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+

    def add_object(self, *new_objects):
        self.objects = self.objects + list(new_objects)

    def remove_object(self, *objects_to_delete):
        try:
            [ self.objects.remove(object) for object in objects_to_delete ]

        except ValueError as previous_error:
            new_error = exceptions.MissingObjectException("Unable to remove object, not in list")
            raise new_error from previous_error

    def get_objects_layers(self):
        objects_layers = {}
        for current_object in self.objects:
            current_layer = objects_layers.get(current_object.depth, [])
            objects_layers[current_object.depth] = current_layer.append(current_object)
        object_layers = [objects_layers[key] for key in sorted(objects_layers.keys()) ]
        return object_layers

    def blit_objects(self):
        for layer in self.get_objects_layers():
            for object_to_blit in layer:
                if not object_to_blit.show:
                    continue

                object_position = object_to_blit.get_real_pos()
                object_image = object_to_blit.get_image()
                self.screen.blit(object_image, object_position)

#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+
    
    def set_title(self, new_title):
        self.screen.set_title(new_title)
    
    @staticmethod
    def generate_default_title():
        return __file__ + " - OOPygame"

    def set_icon(self, new_icon):
        self.screen.set_icon(new_icon)
