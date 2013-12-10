'''
@author: Kevin Cooper
@version: 0.0.1
@date: 01 Dec 13
@class: CS 359
'''
import types

class AbstractBaseException(Exception):
    
    def __init__(self, msg):
        self.msg = msg
        
    def handleItself(self):
        print("An unknown exception occurred: %r" % (self.msg))

class DetailedException(AbstractBaseException):
        
    def handleItself(self):
        if type(self.msg) is types.StringType:
            print("The error that occurred is described by:\n %s" % (self.msg))
        elif type(self.msg) is types.IntType:
            print("The error that occurred is described by:\n %d" % (self.msg))
        else:
            print("The error that occurred is described by:\n %r" % (self.msg))

class TooFewPiecesException(AbstractBaseException):
    def handleItself(self):
        print("Too few pieces exception hit:\n %s", (self.message))
    
class TooFewCardsException(AbstractBaseException):
    def handleItself(self):
        print("Too few cards exception hit\n %s", (self.message))
