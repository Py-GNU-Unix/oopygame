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

import oopygame as oop
import pygame

if __name__ == "__main__":
    W = oop.Window(flags=pygame.DOUBLEBUF, bg_color=oop.colors.white)
    clock = oop.time.Clock(FPS=120, window=W)
    obj = oop.Object(W, pos=(0, 250))

    restart_pos = (0-obj.get_image().get_width(), 250)

    while True:
        obj.move_right(4)
        if obj.is_out_of_window() and not obj.is_touching_borders():
            obj.set_pos(restart_pos)

        clock.tick()
        W.do_routine()
