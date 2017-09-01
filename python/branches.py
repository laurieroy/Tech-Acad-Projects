import datetime
# get help with this at class
class branches(object):
    """Branches of bank, stores location and timezone."""
    def __init__(self, location, tz):
        """ Create an empty set of branches"""
        self.locations = []
        self.tz = []

    def insertLocation(self,e):
        """Assumes e is a text string and insert e into self."""
        if not e in self.locations:
            self.locations.append(e)

    def insertTZ(self,e,tz):
        """Assumes e is a text string and insert e into self."""
        for self.locations[e]
            if not e in self.tz:
                self.locations.append(tz)

    def member(self,e):
        """Assumes e is text string
           Returns true if e is in self, False otherwise"""
        return e in self.locations

    def remove(self,e):
        """Assumes e is a text string and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.locations.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def getMembers(self):
        """Returns an unordered list containing the elements of self."""
        return self.locations[:]

    def ___str___(self):
        """eh, prob not needed"""
        self.locations.sort()
        result = ''
        for e in self.locations:
            result = result + str(e)+','
        return '{' + result[:-1] + '}' #-1 omits trailing comma

    def timezone(self,e):
        """Assume e is a text string, and stores e into self."""
        self.tz(e) # maybe a yes/no check
"""    
