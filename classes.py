# Task 1.2
class ContactList:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size
    
    @staticmethod
    def hash(inputstr):
        total = 0
        for pnum in range(len(inputstr)):
            char = inputstr[pnum]
            cnum = ord(char)
            total += (pnum * cnum)
        return total
    
    def add(self, key, value):
        index = self.hash(key) % self.size
        if self.data[index] is None:
            self.data[index] = {key: value}
        else:
            self.data[index][key] = value

    def get(self, key):
        index = self.hash(key) % self.size
        return self.data[index][key]