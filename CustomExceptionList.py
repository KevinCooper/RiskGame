'''
@author: Kevin Cooper
@version: 0.0.1
@date: 01 Dec 13
@class: CS 359
@purpose: This file contains classes for multiple different custom exceptions\
 that can be implemented throughout the project.
'''


class AbstractBaseException(Exception):

    def __init__(self, msg):
        '''
        _msg - string
        '''
        self._msg = msg

    def handleItself(self):
        print("An unknown exception occurred: %r" % (self._msg))


class DetailedException(AbstractBaseException):

    def handleItself(self):
        print("The error that occurred is described by:\n %r" % (self._msg))


class TooFewPiecesException(AbstractBaseException):
    def handleItself(self):
        print("Too few pieces exception hit:\n %s", (self.message))


class TooFewCardsException(AbstractBaseException):
    ''' Not implemented'''
    def handleItself(self):
        print("Too few cards exception hit\n %s", (self.message))
