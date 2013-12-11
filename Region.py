'''
@author: Kevin Cooper
@version: 0.0.3
@date: 01 Dec 13
@class: CS 359
@purpose:
'''
import CustomExceptionList as CEL
import pygame
import math
import os
import AnimatedSprite


class Region(object):

    def __init__(self, image,  name, position):
        self.image = pygame.image.load(os.path.join('resources', image))\
                                                                .convert()
        self._name = name
        self._player = None
        self._units = 0
        self._position = position
        self.animated = AnimatedSprite.AnimatedSprite(self.load_sliced_sprites\
                            (16, 16, 'explosions-sprite.png'), self._position)
        self._animated_pos = 0
        self._animated_len = len(self.load_sliced_sprites(16, 16,\
                                                       'explosions-sprite.png'))
        self.animate = False

    def __eq__(self, otherRegion):
        if(otherRegion == None):
            return None
        return otherRegion.getName() == self._name

    def __str__(self):
        return self._name

    def setPlayer(self, player):
        self._player = player

    def getPlayer(self):
        return self._player

    def addUnits(self, number):
        self._units += number

    def subUnits(self, number):
        self._units -= number

    def validMove(self, player):
        return self._player == player

    def validAttack(self, player):
        return self._player != player

    def getUnits(self):
        return self._units

    def getName(self):
        return self._name

    def setAnimate(self):
        self.animate = True

    def update(self, time, screen):
        if(self.animate == True):
            self.animated.update(time)
            self.animated.render(screen)
            if(self._animated_pos >= self._animated_len):
                _animated_pos = -1
                self.animate = False
            self._animated_pos += 1

    def draw(self, screen):
        pygame.draw.circle(screen, self._player.getColor(), self.getCenterPosition(), 10, 0)
        # screen.blit(self.image, self._position)

    def getCenterPosition(self):
        # ADD 10,10 because circle of radius 10!!
        return (self._position[0] + 10, self._position[1] + 10)

    def wasClicked(self, mouseX, mouseY):
        if(mouseX < 0 or mouseY < 0):
            CEL.DetailedException("A mouse event was called on a region with a mouse value that was less than zero.")
        try:
            if (math.fabs(mouseX - self._position[0]) < 20 and math.fabs(mouseY - self._position[1]) < 20):
                return True
            else:
                return False
        except Exception as e:
            print("Error in the wasClicked method:\n %s" % (e.message))

    def canMove(self):
        return self._units > 1

    def canAttack(self):
        return self._units > 1

    def removeUnits(self, numberToRemove):
        try:
            if(self._units - numberToRemove < 0):
                raise CEL.TooFewPiecesException
            self._units -= numberToRemove
        except CEL.TooFewPiecesException as error:
            error.handleItself()

    def load_sliced_sprites(self, w, h, filename):
        # http://shinylittlething.com/2009/07/21/pygame-and-animated-sprites/
        '''
        Specs :
            Master can be any height.
            Sprites frames width must be the same width
            Master width must be len(frames)*frame.width
        Assuming you resources directory is named "resources"
        '''
        images = []
        master_image = pygame.image.load(os.path.join('resources', filename)).convert_alpha()
        master_width, master_height = master_image.get_size()
        for i in xrange(int(master_width / w)):
            images.append(master_image.subsurface((i * w, 0, w, h)))
        return images
