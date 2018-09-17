#!/usr/local/bin/python2.7
"""Pydrill_Datetime_27_idle finds local time at branches WRT PDX."""
#
# Author: Laurette Roy
#
# Drill for python course, Tech Academy, Portland OR, Aug 2017
#
# Python v 2.7
#
# Purpose: Hypothetical company has branches in NYC, London. Need a simple program to find out if branches
# are open or closed based on the current time of HQ in PDX. Branch hours are each: 9am-9pm (ha, talk about banksers hours!!)
# in their own time zone. Create code that will use the current time of the Portland HQ to find out the time in the NYC &
# London branches, then compare that time with the branches hours to see if they are open or closed.
# Guildlines: -Use Python 2.7 IDLE -Use Datetime Module -Execute program on the Shell
# Assumption: User of this application is at HQ in Portland ((later can make input for other timezones))
# Note: London uses British Summer Time, which begins at 01:00 GMT on the last Sunday of March and ends at 01:00 GMT (02:00 BST)
# on the last Sunday of October.        ** use aware, be sure it accounts for it **
import datetime
import pytz

eastern = pytz.timezone('US/Eastern')
london = pytz.timezone('Europe/London')  # can erase utc when checked
pacific = pytz.timezone('US/Pacific')
utc_now2 = datetime.datetime.now(tz=pytz.utc)
utc = pytz.utc
utc_now=pytz.utc.localize(datetime.datetime.utcnow())
# isDST=none for times when might be ambiguity.
class Branches(): # this was setup original thinking like a list of structs, but not so
    #pass

    #def branch():
        
    def __init__(self, name):
            """Create an empty set of branches."""
            self.name = name
            self.location = []
            self.tz = []
            self.branch_time = []
            self.opening_time = datetime.time(9, 0, 0, 0)
            self.closing_time = datetime.time(21, 0, 0, 0)

    def add_location(self,e):
        """Assumes e is a text string and insert e into self."""
        if not e in self.location:
            self.location.append(e)
            
    def add_tz(self,e):
        """Assume e is a text string, and stores e into self."""
        self.tz = e 

    def local_time(self,tz):
        """Assume tz is text string as stored.
        try:
            self.branch_time = datetime.datetime.now(self.tz)
        except:
            raise ValueError(str(tz) + ' not found')""" # work on this later
        self.branch_time = datetime.datetime.now(self.tz)
        
    def member(self,e): # don't think this is needed
        """Assumes e is text string, check to see if branch name has been added
           Returns true if e is in self, False otherwise."""
        return e in self.name

    def remove(self,e):
        """Assumes e is a text string and removes e from self
           Raises ValueError if e is not in self."""
        try:
                self.name.remove(e)
        except:
                raise ValueError(str(e) + ' not found')

    def ___str___(self):
        """eh, prob not needed"""
        self.name.sort()
        result = ''
        for e in self.name:
                result = result + str(e)+','
        return '{' + result[:-1] + '}' #-1 omits trailing comma



# create branches

HQ = Branches('Portland')
HQ.add_location('Portland, OR')
HQ.add_tz('pacific')
# timePDX = HQ.local_time(pacific) # error catch not working yet

NYC = Branches('NYC')
NYC.add_location('New York City, NY')
NYC.add_tz('eastern')

London = Branches('London')
London.add_location('London, UK')
London.add_tz('london')

branches = ['HQ', 'NYC', 'London'] # work on this
time_msg = "The current time in {} is {:%a, %d, %b, %Y, %H, %M}."
i=0
for branches[i] in branches:
    # print (time_msg.format(branch), time_msg.time.branches[i])
    print (time_msg, branches[i])
branches = ['HQ', 'NYC', 'London']
#timePDX = pacific.localize(datetime.datetime.now())
timePDX = datetime.datetime.now(tz=pacific)
timeNYC = datetime.datetime.now(tz=eastern)
timeLondon = datetime.datetime.now(tz=london)
print "The current time in Portland, OR is {}", timePDX


# do a comparison maybe def isopen(branch, tz)
    
for branch in branches:
    if branches.opening_time < current_time < branches.closing_time:
        print('The {} branch is open.').format(('Portland, OR'), ('New York City, NY'), ('London, UK'))
    else:
        print('{} branch is closed.')
"""
branchOpen =
# def datetime.astimezone(self, tz):
#    if self.tzinfo is tz:
#        return self
#    utc =
OK, I think a good way to go about this would be to grab internet time, adjust to time zone in PDX. Can figure out NY time immediately
test if datatime adjust for BST.
if not, do a check on date, print to screen, times at HQ, London branch is open/closed, NYC branch is o/c

datetime.utcnow()
datetime.tzinfo
"""
