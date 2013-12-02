'''
@author: Kevin Cooper
@version: 0.0.0
@date: 01 Dec 13
@class: CS 359
'''

import pygame
from CustomExceptionList import *

if __name__ == '__main__':
    try:
        pygame.init()
        raise DetailedException("Test")
    except DetailedException as EO:
        EO.handleItself()
        