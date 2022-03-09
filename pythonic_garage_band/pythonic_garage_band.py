from cgi import test
from typing_extensions import Self
from unicodedata import name


    



class Musician :

    def __init__(self, name):
        self.name = name




class Guitarist(Musician):

    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    def get_instrument(self):
        return "guitar"
    
    
    def play_solo(self):
        return "face melting guitar solo"



class Bassist(Musician):
    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

    def get_instrument(self):
        return "bass"
    
    
    def play_solo(self):
        return "bom bom buh bom"



class Drummer(Musician):
    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    def get_instrument(self):
        return "drums"
    
    
    def play_solo(self):
        return "rattle boom crash"

class Band:
    Band_list = []
    def __init__(self, name , members):
        self.name = name
        self.members = members
        Band.Band_list.append(self.name)

   
    def play_solos(self):
        solos_list = []
        for i in  range(0,len(self.members)):
            oneSole = globals()[self.members[i]].play_solo(globals()[self.members[i]])
            solos_list.append(oneSole)
        return solos_list
    
    @classmethod
    def to_list(cls):
        return cls.Band_list    #which returns a list of previously created Band instances


#if __name__== "__main__":
    
