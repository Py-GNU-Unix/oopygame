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
from oopygame.objects import  platform_image as image


if __name__ == "__main__":
    W = oop.Window(flags=pygame.DOUBLEBUF|pygame.RESIZABLE, bg_color=oop.colors.white)
    # obj = oop.Object(W, pos=(0,0))
    #
    # image = oop.image_tools.scale_image(image, (500,128))
    # platform = oop.Object(W, pos=(-80,372), image=image)
    # clock = oop.time.Clock(60, W)
    #
    # dem = oop.demons.gravity(obj, platforms=[platform])
    # W.add_demon(dem)
    #
    # dem2 = oop.demons.OnObjectClick(obj, action=lambda:print("hi"))
    # W.add_demon(dem2)
    #
    # while True:
    #     if W.detect_key(pygame.K_RIGHT):
    #         obj.move_right(2)
    #
    #     if W.detect_key(pygame.K_LEFT):
    #         obj.move_left(2)
    #
    #     if W.detect_key(pygame.K_UP):
    #         obj.move_up(8)
    #
    #
    #     W.do_routine()
    #     clock.tick()
    Text = oop.Text(W, "try fsdf fsd ds fds f ds fds f ds fds f ds f dsf  fsd  fdsfdsfds  sfd f sd f  fsdfsdfsdfsd  dsf ds f ds     fsdfsdfsd fds f dsf ds fffffsd f ds fds f ds fs f ds fs f ds fds f sf dsf ds f dsf s f sd fs df sd   fds fds f ds fs")

    while True:
        W.do_routine()
