'''
@author: Kevin Cooper
@version: 0.0.3
@date: 01 Dec 13
@class: CS 359
'''
import pygame


class RiskGUI(object):
    '''
    This class contains the code to work with the GUI for the game.  In\
    addition, it also handles all events that come from the user.
    '''
    def __init__(self):
        '''
        Initializes the screen that will be used.  Starts the game in \
        fullscreen after determining the size of the screen from the computer.
        '''
        ##The 2 item integer tuple that represents the screen size
        self.size = (pygame.display.Info().current_w, \
                     pygame.display.Info().current_h)
        ##Pygame display set to the size with fullscreen flags
        self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
        pygame.display.set_caption("Kevin Cooper CS359 Project")
        self._white = 255, 255, 255
        self._black = 0, 0, 0
        self._red = 255, 0, 0
        self._blue = 0, 0, 255
        self._green = 0, 255, 0
        ##Pyagme sysfront, monospace, size 15
        self.font = pygame.font.SysFont("monospace", 15)
        self.screen.fill(self._white)

    def clearScreen(self):
        '''
        Fills the screen with _white.
        '''
        self.screen.fill(self._white)

    def drawBoard(self, board):
        '''
        board - RiskBoard object

        Draws each of the Regions in the board onto the screen.  Also draws the\
        edges for each of the nodes as _black lines between the regions.
        '''
        for region in board.getRegions():
            for neighbor in board.getNeighbors(region[0]):
                pygame.draw.line(self.screen, self._black, \
                                 neighbor.getCenterPosition(), \
                                 region[1].getCenterPosition(), 1)
        for region in board.getRegions():
            region[1].draw(self.screen)
            self.screen.blit(self.font.render(str(region[1].getUnits()),\
                                        1,\
                                        self._black), \
                                        (region[1].getCenterPosition()[0] + 10,\
                                        region[1].getCenterPosition()[1] - 25))

    def drawTurn(self, board, player, pieces):
        '''
        board - RiskBoard object
        player - Player object
        pieces - integer

        Draws the information text onto the top left of the screen.\
        Information includes current player, and how many pieces left.
        '''
        self.screen.blit(self.font.render(str(player), 1, self._black), (10, 10))
        self.screen.blit(self.font.render("You can place this many pieces: " +\
                                          str(pieces), 1, self._black), (10, 25))

    def battleSequence(self, AgressorRegion, DefenderRegion, Dice):
        '''
        AggressorRegion - Region object
        Defender Region - Region object
        Dice - Dice object

        Determines the winner of the attack starts the animation.  \
        Automatically updates the amount of pieces for both regions.
        '''
        if(AgressorRegion.canAttack()):
            if(Dice.rollDice() > Dice.rollDice()):
                DefenderRegion.setAnimate()
                DefenderRegion.removeUnits(1)
                if(DefenderRegion.getUnits() == 0):
                    DefenderRegion.setPlayer(AgressorRegion.getPlayer())
                    DefenderRegion.addUnits(1)
                    AgressorRegion.removeUnits(1)
            else:
                AgressorRegion.setAnimate()
                AgressorRegion.removeUnits(1)

    def moveSequence(self, sourceRegion, destRegion):
        '''
        sourceRegion - Region object
        destRegion - Region object

        Moves a piece from source to dest.  Automatically updates the piece \
        values for both of the Region objects
        '''
        if(sourceRegion.canMove()):
            sourceRegion.removeUnits(1)
            destRegion.addUnits(1)
            # Fancy animation here

    def resolveEvent(self, board, event):
        '''
        board - RiskBoard object
        event - PyGame event object

        return - tuple

        Returns a tuple with the information about what event occurred. For key\
        information, returns a 2 item string tuple, where the first element is \
        the Key/Action that occurred.  For mouse clicks, returns Region, Which \
        mouse button, and the associated region object.
        '''
        # Handle key events
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                return ("Exit", "Junk")
            if  event.key == pygame.K_SPACE:
                return ("SpaceBar", "Junk")
            if  event.key == pygame.K_h:
                return ("Help", "Junk")
        # Handle mouse events
        if event.type == pygame.MOUSEBUTTONUP:
            mousex, mousey = event.pos
            # print event.button
            if event.button == 1:
                for region in board.getRegions():
                    if(region[1].wasClicked(mousex, mousey)):
                        return ("Region", "Left", region)
                return ("Left", mousex, mousey)
            if event.button == 3:
                for region in board.getRegions():
                    if(region[1].wasClicked(mousex, mousey)):
                        return ("Region", "Right", region)
                return ("Right", mousex, mousey)
