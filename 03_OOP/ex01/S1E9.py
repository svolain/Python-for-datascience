from abc import ABC

class Character(ABC):
    """
    abstract class
    """
    def __init__(self, first_name, is_alive=True):
        """
        takes a first_name as first parameter,
        is_alive as second non mandatory parameter 
        set to True by default and can change the
        health state of the character with a method
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        method that passes is_alive from True to False.
        """
        pass

class Stark(Character):
    """
    a "stark" class which inherits from Character
    """
    def __init__(self, first_name, is_alive=True):
        """
        takes a first_name as first parameter,
        is_alive as second non mandatory parameter 
        set to True by default and can change the
        health state of the character with a method
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        method that passes is_alive from True to False.
        """
        self.is_alive = False

    