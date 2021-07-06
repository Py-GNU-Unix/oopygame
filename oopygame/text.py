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
from . import objects, colors


pygame.font.init()
Font = pygame.font.SysFont

X = 0
Y = 1


class TextFitter:
    @staticmethod
    def fit_chars(text, max_line_len):
        lines = [text[i:i+max_line_len]
            for i in range(0, len(text), max_line_len)]

        return "\n".join(lines)

    @staticmethod
    def fit_words(text, max_line_len):
        new_text = [""]
        for current_word in text.split():
            TextFitter.fit_single_word(current_word, new_text, max_line_len)

        return "\n".join(new_text)

    @staticmethod
    def fit_single_word(word, text, max_line_len):
        if TextFitter.is_there_space_for_word(word, text[-1], max_line_len):
            text[-1] += word + " "
        else:
            TextFitter.fit_line_in_iterable(text, -1)
            TextFitter.is_too_long(word, max_line_len)
            text.append(word + " ")

    @staticmethod
    def is_there_space_for_word(word, line, max_line_len):
        line_len = len(line)
        word_len = len(word)

        return line_len + word_len <= max_line_len


    @staticmethod
    def fit_line_in_iterable(iterable, index):
        iterable[index] = iterable[index].strip(" ")

    @staticmethod
    def is_too_long(word, max_len):
        if len(word) > max_len:
            assert f"Word {word} is more long than the maximum_line_len({max_len}). Cannot fit properly."


class TextObject(objects.Object):
    def __init__(self, master_window, text="Text", font=Font(None, 24), size=(100,100), 
            color=colors.black, fitter_func=TextFitter.fit_words, **kwargs):

        self.text = text
        self.color = color
        self.size = size
        self.font = font
        self.fitter_func = fitter_func

        objects.Object.__init__(self, master_window, image=self.generate_text_surface(), **kwargs)

    def generate_text_surface(self):
        max_line_len = self.calc_max_chars_for_line()
        fitted_text = self.fit_text(self.text, max_line_len)
        surface = self.generate_trasparent_surface(self.size)
        self.blit_text_on_surface(surface, fitted_text)
        return surface
        
    def calc_max_chars_for_line(self):
        font_size = self.font.size("X")

        max_chars = int(self.size[X] / font_size[X])
        max_chars = max_chars if max_chars != 0 else 1

        return max_chars

    def fit_text(self, text, max_line_len):
        fitted_text = self.fitter_func(text, max_line_len)
        return fitted_text
    
    @staticmethod
    def generate_trasparent_surface(size):
        surface = pygame.Surface(size, pygame.SRCALPHA)
        return surface.convert_alpha()

    def blit_text_on_surface(self, surface, text):
        cursor_x, cursor_y = (0,0)
        for line in text.splitlines():
            line_text_surface = self.font.render(line, True, self.color)
            surface.blit(line_text_surface, (cursor_x, cursor_y))
            cursor_y += line_text_surface.get_height()
