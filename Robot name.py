Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
import string


class Robot(object):
    """docstring for Robot"""
    
    def __init__(self):
        super(Robot, self).__init__()
        random.seed()
        self.reset()
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name):
        self._name = name
        
    def reset(self):
        name = random.sample(
            string.ascii_uppercase, 2) + random.sample(string.digits, 3)
        self._name = ''.join(name)
