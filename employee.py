class Employee():
    favs = []

    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def __repr__(self) :
        return self.__str__()