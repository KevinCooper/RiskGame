'''
@author: Kevin Cooper
@version: 0.0.0
@date: 01 Dec 13
@class: CS 359
'''

class AbstractBaseException(Exception):
    def handleItself(self):
        print("An unknown exception occurred")

class DetailedException(AbstractBaseException):
    
    def __init__(self, msg):
        self.msg = msg
        
    def handleItself(self):
       if type(self.msg) is string:
            print("The error that occurred is described by: %s" %(self.msg))
       elif type(self.msg) is int:
            print("The error that occurred is described by: %d" %(self.msg))
       else:
            print("The error that occurred is described by: %r" %(self.msg))