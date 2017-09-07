#!/usr/local/bin/python2.7
def branchOpen():
    """Find local time at branches(NYC, London) WRT PDX"""
#Name: branchOpen --- Pydrill_Datetime_27_idle
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
# Guidelines: Use Python 2.7 IDLE -Use Datetime Module -Execute program on the Shell
# Assumption: User of this application is at HQ in Portland 
# Note: London uses British Summer Time, which begins at 01:00 GMT on the last Sunday of March and ends at 01:00 GMT (02:00 BST)
# on the last Sunday of October.      
# #################################################################################################
    import datetime
    import pytz
    # create aware time zones for cities in question
    eastern = pytz.timezone('US/Eastern')
    london = pytz.timezone('Europe/London')
    pacific = pytz.timezone('US/Pacific')
    # get time now, and format
    timePDX = datetime.datetime.now(tz=pacific)
    timeNYC = datetime.datetime.now(tz=eastern)
    timeLondon = datetime.datetime.now(tz=london)
    hrNYC=timeNYC.strftime("%H")
    hrLondon = timeLondon.strftime("%H")

    opening_time = (datetime.time(9, 0, 0, 0)).strftime("%H")
    closing_time = (datetime.time(21, 0, 0, 0)).strftime("%H")

    def isOpen(tz):
        """Compare time passed to HQ to see whether branch is open."""
        if int(tz) > int(opening_time) and int(tz) < int(closing_time):
            return 'Open'
        else:
            return 'Closed'
        
    isNYCopen = isOpen(hrNYC)
    isLondonOpen = isOpen(hrLondon)

    print('The time now in Portland, OR is {:%a, %d %b %Y, %H:%M, %Z}.').format(timePDX)
    print('The time now in London, England is {:%a, %d %b %Y, %H:%M, %Z}. \n The branch is {}.\n').format(timeLondon,isLondonOpen ) 
    print('The time now in NYC, NY is {:%a, %d %b %Y, %H:%M, %Z}. \n The branch is {}. \n' ).format(timeNYC, isNYCopen) 

if __name__=='__main__':
    branchOpen()
