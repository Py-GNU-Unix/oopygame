import pygame

class movable:
    def __init__(self, window, obj):
        self.window = window
        self.obj = obj
        self.clicked = False
    
    def __call__(self):
        for event in self.window.get_events():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.obj.get_rect().collidepoint(event.pos):
                    self.clicked = True
            
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.clicked = False
            
            
        if self.clicked:
            mouse_pos = pygame.mouse.get_pos()
            obj_size = self.obj.get_size()
            pos_to_go = [mouse_pos[choor]-(obj_size[choor]/2) for choor in (0,1)]
            self.obj.set_pos(pos_to_go)
