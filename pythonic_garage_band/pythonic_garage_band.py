from cgi import test
from typing_extensions import Self
from unicodedata import name

class Musician :
    """
    superClass which other classes will Inherets from 
    """
    def __init__(self, name):
        self.name = name




class Guitarist(Musician):
    """
    Class Guitarist which have two methods get in strument and play solo
    """

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    def get_instrument(self):
        return "guitar"
    
    
    def play_solo(self):
        return "face melting guitar solo"



class Bassist(Musician):
    """
    Class Bassist which have two methods get in strument and play solo
    """
    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

    def get_instrument(self):
        return "bass"
    
    
    def play_solo(self):
        return "bom bom buh bom"



class Drummer(Musician):
    """
    Class Drummer which have two methods get in strument and play solo
    """

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    def get_instrument(self):
        return "drums"
    
    
    def play_solo(self):
        return "rattle boom crash"

class Band:
    """
    Class Band which have two methods play_solos and to_list
    play solo ask each instance to play solo as per the order list 
    and to list will show the list of added instances 
    """
    instances = []
    def __init__(self, name , members):
        self.name = name
        self.members = members
        Band.instances.append(self)

   
    def play_solos(self):
        solos_list = []
        for i in  self.members:
            solos_list.append(i.play_solo())
        return solos_list
    
    @classmethod
    def to_list(cls):
        return cls.instances   #which returns a list of previously created Band instances


#if __name__== "__main__":
    
