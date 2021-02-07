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

import time
import pygame

class Clock:
    def __init__(self, FPS, window):
        self.FPS = FPS
        self.window = window
        self.delay = 1 / FPS
        self.wait = 0.02
        self.last = time.time()
        
    def is_ready(self):
        now = time.time()
        passed = now - self.last 
        
        if passed > self.delay:
            self.last = now
            return True
        
        return False
        
    def tick(self):
        while not self.is_ready():
            self.window.have_to_close()
            pygame.display.flip()
            time.sleep(self.wait)
