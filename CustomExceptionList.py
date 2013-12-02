'''
@author: Kevin Cooper
@version: 0.0.0
@date: 01 Dec 13
@class: CS 359
'''

class AbstractBaseException(Exception):
    def handleItself(self):
        pass

class DetailedException(AbstractBaseException):
    
    def __init__(self, msg):
        self.msg = msg
        
    def handleItself(self):
        print("The error that occurred is described by: %r" %(self.msg))
        