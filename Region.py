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
    '''
    The region object contains all the information about the cells that are\
    displayed on the board.  They keep track things such as the current owning\
    player to whether the coordinates given clicked on it.
    '''

    def __init__(self, name, position):
        '''
        name - String
        position - 2 item integer tuple
        '''
        self._name = name
        self._player = None
        self._units = 0
        self._position = position
        try:
            self.animated = AnimatedSprite.AnimatedSprite(self.load_sliced_sprites\
                            (16, 16, 'explosions-sprite.png'), self._position)
            self._animated_pos = 0
            self._animated_len = len(self.load_sliced_sprites(16, 16, \
                                                       'explosions-sprite.png'))
            self.animate = False
        except:
            pass

    def __eq__(self, otherRegion):
        '''
        otherRegion - Region object

        return - boolean

        Returns whether the two Regions have the same name
        '''
        if(otherRegion == None):
            return None
        return otherRegion.getName() == self._name

    def __str__(self):
        '''
        return - String

        Returns the name of the Region
        '''
        return self._name

    def setPlayer(self, player):
        '''
        player - Player object
        '''
        self._player = player

    def getPlayer(self):
        '''
        return - Player object

        Returns the player trhat currently owns the region.
        '''
        return self._player

    def addUnits(self, number):
        '''
        number - integer

        Adds number to the amount of units that the Region has.
        '''
        self._units += number

    def validMove(self, player):
        '''
        player - Player object

        return - boolean

        Determines whether the Region is able to be moved into by the given\
        player
        '''
        return self._player == player

    def validAttack(self, player):
        '''
        player - Player object

        return - boolean

        Determines whether the Region is able to be attacked by the given player
        '''
        return self._player != player

    def getUnits(self):
        '''
        return - integer

        Returns the number of units in the Region
        '''
        return self._units

    def getName(self):
        '''
        return - string

        Returns the string representation of the Region
        '''
        return self._name

    def setAnimate(self):
        '''
        Sets the Region to start animating the explosion sequence
        '''
        self.animate = True

    def update(self, time, screen):
        '''
        time - integer
        screen - Pygame display object

        Increments the image used in displaying the explosion animation if \
        enough time has passed.  Stops the animation if the last image of \
        the sequence has been reached.
        '''
        if(self.animate == True):
            self.animated.update(time)
            self.animated.render(screen)
            if(self._animated_pos >= self._animated_len):
                _animated_pos = -1
                self.animate = False
            self._animated_pos += 1

    def draw(self, screen):
        '''
        screen - Pygame display object

        Draws a circle of radius 10 of the players color to the given display \
        object.
        '''
        pygame.draw.circle(screen, self._player.getColor(), \
                            self.getCenterPosition(), 10, 0)
        # screen.blit(self.image, self._position)

    def getCenterPosition(self):
        ''' No longer implemented due to design change'''
        return (self._position[0] + 10, self._position[1] + 10)

    def wasClicked(self, mouseX, mouseY):
        '''
        mouseX - integer
        mouseY - integer

        return - boolean

        Returns whether the mouse coordinates are within the Region.
        '''
        if(mouseX < 0 or mouseY < 0):
            CEL.DetailedException("A mouse event was called on a region with a \
            mouse value that was less than zero.")
        try:
            if (math.fabs(mouseX - self._position[0]) < 20 and \
                math.fabs(mouseY - self._position[1]) < 20):
                return True
            else:
                return False
        except Exception as e:
            print("Error in the wasClicked method:\n %s" % (e.message))

    def canMove(self):
        '''
        return - boolean

        Returns true if the number of units is greater than 1
        '''
        return self._units > 1

    def canAttack(self):
        '''
        return - boolean

        Returns true if the number of units is greater than 1
        '''
        return self._units > 1

    def removeUnits(self, numberToRemove):
        '''
        numberToRemove - integer

        Removes number from the amount of units that the Region has.  Raises a \
        TooFewPiecesException if the number goes below 0.
        '''
        try:
            if(self._units - numberToRemove < 0):
                self._units = 0
            else:
                self._units -= numberToRemove
        except:
            pass

    def load_sliced_sprites(self, w, h, filename):
        # http://shinylittlething.com/2009/07/21/pygame-and-animated-sprites/
        '''
        Specs :
            Master can be any height.
            Sprites frames width must be the same width
            Master width must be len(frames)*frame.width
        Assuming you resources directory is named "resources"
        '''
        try:
            images = []
            master_image = pygame.image.load(os.path.join('resources', \
                                            filename)).convert_alpha()
            master_width, master_height = master_image.get_size()
            for i in xrange(int(master_width / w)):
                images.append(master_image.subsurface((i * w, 0, w, h)))
            return images
        except:
            pass
