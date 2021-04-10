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

from . import objects
from . import OOPyException
import pygame
import math

class Text(objects.Object):
    def __init__(self, master_window, text, size=(900, 300), color=(0, 0, 0), pos=(0, 0), font=pygame.font.SysFont(None, 24), padding=(20, 20), truncate_words=False):
        self.text = text
        self.color = color
        self.size = size
        self.font = font
        self.padding = padding
        self.truncate_words = truncate_words

        objects.Object.__init__(self, master_window, pos, image=self.generate_text_surface())

    def generate_text_surface(self):
        max_chars_for_line = self.calc_max_chars_for_line()
        arranged_text = self.get_arranged_text(max_chars_for_line)
        ## TODO: if can't arrange the text, change font size and retry
        surface = self.generate_trasparent_surface(self.size)
        self.blit_text_on_surface(surface, arranged_text)
        return surface


    def calc_max_chars_for_line(self):
        maximum_width = self.size[0] - self.padding[0]
        font_size = self.font.size("X")
        return math.ceil(maximum_width / font_size[0])

    def generate_trasparent_surface(self, size):
        surface = pygame.Surface(size, pygame.SRCALPHA)
        return surface.convert_alpha()

    def blit_text_on_surface(self, surface, text):
        y = 0
        for line in text.splitlines():
            line_text_surface = self.font.render(line, True, self.color)
            surface.blit(line_text_surface, (0, y))
            y += line_text_surface.get_height()

    def get_arranged_text(self, max_chars_for_line):
        if not self.truncate_words:
            arranged_text = TextArranger.arrange_words(self.text, max_chars_for_line)
        else:
            arranged_text = TextArranger.arrange_chars(self.text, max_chars_for_line)

        return arranged_text

class TextArranger:
    @staticmethod
    def arrange_chars(text, max_line_len):
        lines = [text[i:i+max_line_len]
            for i in range(0, len(text), max_line_len)]

        return "\n".join(lines)

    @staticmethod
    def arrange_words(text, max_line_len):
        new_text = [""]
        for current_word in text.split():
            TextArranger.arrange_single_word(current_word, new_text, max_line_len)

        return "\n".join(new_text)

    @staticmethod
    def arrange_single_word(word, text, max_line_len):
        if TextArranger.is_there_space_for_word(word, text[-1], max_line_len):
            text[-1] += word + " "
        else:
            TextArranger.format_line_in_iterable(text, -1)
            TextArranger.is_too_long(word, max_line_len)
            text.append(word + " ")

    @staticmethod
    def is_there_space_for_word(word, line, max_line_len):
        line_len = len(line)
        word_len = len(word)

        return line_len + word_len <= max_line_len


    @staticmethod
    def format_line_in_iterable(iterable, index):
        iterable[index] = iterable[index].strip(" ")

    @staticmethod
    def is_too_long(word, max_len):
        if len(word) > max_len:
            assert f"Word {word} is more long than the maximum_line_len({max_len}). Cannot fit properly."

if __name__ == "__main__":
    print(Text.arrange_words("some text", 5))
