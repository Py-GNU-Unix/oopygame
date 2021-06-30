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
        snake = oopygame.Object(self, pos=(0,150))
        snake.set_size((100,100))
        clock = oopygame.time.Clock(60)
        movement = 2

        while True:
            if snake.is_out_of_window():
                movement *= -1

            snake.move_right(movement)

            clock.tick()
            self.update()

if __name__ == "__main__":
    A = App((500, 400))
    A.run()
