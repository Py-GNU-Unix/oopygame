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

white = (255, 255, 255)
black = (000, 000, 000)
red   = (255, 000, 000)
green = (000, 255, 000)
blue  = (000, 000, 255)

aqua =          (25, 255, 255)
dark_green =    (000, 112, 000)
orange =        (255, 128, 000)
magenta =       (255, 000, 255)
yellow =        (255, 255, 0)

def make_lighter(color, how_much):
    color = list(color)

    def add_how_much(number):
        return number + how_much

    def validate(number):
        if number > 255:
            return 255
        else:
            return number

    color = map(add_how_much, color)
    color = map(validate, color)

    return list(color)

def make_darker(color, how_much):
    color = list(color)

    def sottract_how_much(number):
        return number - how_much

    def validate(number):
        if number < 0:
            return 0
        else:
            return number

    color = map(sottract_how_much, color)
    color = map(validate, color)

    return list(color)
