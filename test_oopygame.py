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

import oopygame

class App(oopygame.Window):
    def run(self):
        snake = oopygame.Object(self)
        snake.set_size((100,100))

        while True:
            self.screen.set_cursor_visibility(False)
            snake.set_pos([ e - 50 for e in self.get_cursor_pos() ])
            self.update()

if __name__ == "__main__":
    App((500, 400)).run()
