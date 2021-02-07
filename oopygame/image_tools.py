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
import cairosvg
import io

def load_svg(filename, fit_to=False):
    if fit_to:
        new_bites = cairosvg.svg2png(url = filename, output_width=fit_to[0], output_height=fit_to[1])
    else:
        new_bites = cairosvg.svg2png(url = filename)
    byte_io = io.BytesIO(new_bites)
    return pygame.image.load(byte_io)

def load_normal_image(filename, fit_to=False):
    pygame.init()
    image = pygame.image.load(filename)
    if fit_to:
        image = pygame.transform.scale(image, fit_to)
        
    return image

def load_image(filename, fit_to=False):
    if filename.endswith(".svg"):
        return load_svg(filename, fit_to)
    else:
        image = load_normal_image(filename, fit_to)
        return image
    
def scale_image(image, fit_to):
    return pygame.transform.scale(image, fit_to)

def chop_image(image, part):
    return image.subsurface(part)

def rotate_image(image, angle):
    return pygame.transform.rotate(image, angle)

def roto_zoom_image(image, angle, scale):
    return pygame.transform.rotozoom(image, angle, scale)
