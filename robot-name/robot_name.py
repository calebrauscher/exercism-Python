from random import choice
from string import ascii_uppercase, digits

class Robot(object):
    ''' Robot class initializes with a unique name with the ability to reset
        the name.
    '''
    robot_names = []

    def __init__(self):
        ''' Initializes by starting with a unique name. '''
        self.reset()

    def __set_name(self):
        ''' Checks that generated name has not been used. '''
        while True:
            new_name = self.__random_name()
            if new_name not in type(self).robot_names:
                type(self).robot_names.append(new_name)
                return new_name

    def __random_name(self):
        ''' Generates a random name with 2 letters and 3 numbers. '''
        return (choice(ascii_uppercase) + choice(ascii_uppercase)
                + choice(digits) + choice(digits) + choice(digits))

    def reset(self):
        ''' Sets a new name. '''
        self.name = self.__set_name()
        type(self).robot_names.append(self.name)
