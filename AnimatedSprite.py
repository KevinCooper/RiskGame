#Documentation for this class http://shinylittlething.com/2009/07/21/pygame-and-animated-sprites/

import pygame
class AnimatedSprite(pygame.sprite.Sprite):
        def __init__(self, images, location, fps = 1):
            pygame.sprite.Sprite.__init__(self)
            
            # Animation 
            self._delay             = 1000 / fps
            self._last_update       = 0
            self._frame             = 0
            self._images            = images
            self.image              = self._images[self._frame]
            self.location           = location
            self.update(pygame.time.get_ticks())
                                
        def update(self, t):
            if t - self._last_update > self._delay:
                self._frame += 1
                if self._frame >= len(self._images):
                    self._frame = 0       
                self.image = self._images[self._frame]
                self._last_update = t
        def render(self, screen):
            screen.blit(self.image, self.location)