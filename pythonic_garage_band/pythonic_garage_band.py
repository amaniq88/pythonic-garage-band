from unicodedata import name


class Musician :
    def __init__(self, name, members):
        self.name = name
        self.members = members 

    def __str__(self):
        return f'Name is {self.name}'

    def __repr__(self):
        return f'this is represntaion for  {self.name}'

    def play_solos():
        pass # method that asks each member musician to play a solo, in the order they were added to band.

    def to_list():
        pass    #which returns a list of previously created Band instances



class Guitarist(Musician):
    def __str__(self):
        return f'Name is {self.name}'

    def __repr__(self):
        return f'this is represntaion for  {self.name}'

    def get_instrument() # method that returns string.
        pass
    
    
    def play_solo():
        pass # method that returns string.



class Bassist(Musician):
    def __str__(self):
        return f'Name is {self.name}'

    def __repr__(self):
        return f'this is represntaion for  {self.name}'

    def get_instrument() # method that returns string.
        pass
    
    
    def play_solo():
        pass # method that returns string.



class Drummer(Musician):
    def __str__(self):
        return f'Name is {self.name}'

    def __repr__(self):
        return f'this is represntaion for  {self.name}'

    def get_instrument() # method that returns string.
        pass
    
    
    def play_solo():
        pass # method that returns string.


if __name__== "__main__":
    band = Musician()


