"""
LRsort(x)
This function takes in a list of integers, sorts it ascending, and returns it.
Not checking to be sure user follows directions.
This is the second function for the python module, Tech Academy.
Python: 3.6.2
Author: Laurette Roy
Date:   Aug 2017


********************************************************************************
"""


def LRsort(x):
 
    workingList=x[:] # create a copy of original list
    i,j,temp=0,0,0
   
    for j in range(len(workingList)): 

        for i in range(len(workingList)-1): 

            if workingList[i] > workingList[i+1]: #swaps positions if larger value on right
                temp = workingList[i]
                workingList[i]=workingList[i+1]
                workingList[i+1]=temp
    
    print (workingList)
    return workingList
#x=[89, 23, 33, 45, 10, 12, 45, 45, 45]
x=[67, 45, 2, 13, 1, 998]
print('x=',x)
print("x'=",end='')
xsorted=LRsort(x)


