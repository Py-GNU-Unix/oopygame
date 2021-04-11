import pygame

class draggable:
    def __init__(self, window, obj):
        self.window = window
        self.obj = obj
        self.clicked = False

    def hear_mouse(self):
        for event in self.window.get_events():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.obj.get_rect().collidepoint(event.pos):
                    self.clicked = True

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.clicked = False

    def drag(self):
        if self.clicked:
            mouse_pos = pygame.mouse.get_pos()
            obj_size = self.obj.get_size()
            pos_to_go = [mouse_pos[choor]-(obj_size[choor]/2) for choor in (0,1)]
            self.obj.set_pos(pos_to_go)

    def __call__(self):
        self.hear_mouse()
        self.drag()

class gravity:
    def __init__(self, obj, gravital_acceleration=0.3, platforms=[]):
        self.obj = obj
        self.fall_speed = 0
        self.gravital_acceleration = gravital_acceleration
        self.platforms = platforms
        self.side_size = 0

    def add_platforms(self, new_platform):
        self.platforms.add(new_platform)

    def remove_platform(self, plt_remove):
        self.platforms.remove(plt_remove)

    def set_platforms(self, new_platforms):
        self.platforms = new_platforms

    def is_on_a_platform(self, side_size=10):
        obj_down_side = self.obj.get_side("down", side_size=side_size)

        for current_platform in self.platforms:
            current_platform_up_side = current_platform.get_side("up", side_size=side_size)

            if obj_down_side.colliderect(current_platform_up_side):
                return True

        return False

    def __call__(self):
        if not self.is_on_a_platform():
            self.fall_speed += self.gravital_acceleration
            if self.fall_speed > 15:
                self.fall_speed = 15

            self.obj.move_down(self.fall_speed)
        else:
            self.fall_speed = 0

class OnEvent:
    def __init__(self, event, action):
        self.event = event
        self.action = action

    def __call__(self):
        if self.event():
            self.action()

class OnObjectEvent(OnEvent):
    pass

class OnObjectClick(OnObjectEvent):
    def __init__(self, object, action):
        OnObjectEvent.__init__(self, object.is_clicked, action)

class OnObjectUnderCursor(OnObjectEvent):
    def __init__(self, object, action):
        OnObjectEvent.__init__(self, object.is_under_cursor, action)

class OnObjectNotUnderCursor(OnObjectEvent):
    def __init__(self, object, action):
        event = lambda: not object.is_under_cursor()
        OnObjectEvent.__init__(self, event, action)
