from S1E9 import Character

class Baratheon(Character):
    """
    Representing the Baratheon family.
    """
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive=True)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'
    def die(self):
        self.is_alive = False
    def __str__(self):
        return '(\'' + self.family_name + ', ' +  self.eyes + ' ,' + self.hairs + '\')'
    def __repr__(self):
        return '(\'' + self.family_name + ', ' +  self.eyes + ' ,' + self.hairs + '\')'
        
class Lannister(Character):
    """
    And who are you that I must bow so deep?
    """
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive=True)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'
    def die(self):
        self.is_alive = False
    @classmethod
    def create_lannister(c, first_name, is_alive):
        instance = c(first_name)
        instance.is_alive = is_alive
        return instance
