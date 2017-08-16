"""
**************************************************************************************
Python:     2.7.13
Author:     Laurette Roy
Purpose:    This program (my first python) tells what change to return for a $0.05 item, using
            small bills and change, I'm selling fireballs for a nickel.
            Programs calls the following functions: start, getName, getQuantity, fireballCost, xxx
            readVal checks to be sure entry is an int
            local variables: name, quantity, cost, paid, xxx
            Note: I still need to format the money. I don't want to change it all to a string right now tho
            This program is an exercise for the python module of the Tech Academy bootcamp, Aug 2017.
***************************************************************************************
"""
def start(quantity=0, paid=0, cost=0, name=""):     # We start with our variables initialized
    name = getName(name)                    #get user's name and display back to screen 
    getQuantity(quantity, cost, name)
        
def getName(name):  # function asks user for name  
    name = raw_input("\nWhat is your first name? ").capitalize()    #(36-2,4)
    return name         # returns name to calling function          #36-12

def readVal(valType, requestMsg, errorMsg):             # checks to be sure input is of correct type
    while True:
        val = raw_input(requestMsg + ' ')
        try:
            val = valType(val)
            return val
        except: 
            print val, errorMsg
            
def getQuantity(quantity, cost, name):
    print("Hello {}, How many fireballs would you like? They cost a nickel ($0.05) each.").format(name)
    quantity= readVal(int, '\nFor example: 5', 'is not an integer') #(36-1)
    fireballCost(quantity, cost, name)  # pass these variables to next function 

def fireballCost(quantity, cost, name):     #determine x#fireballs costs  y amount
    cost=(quantity*0.05)                    #(36-3) (36-5)
    print("quantity ", quantity, "fireballs costs", cost,)
   
    while quantity > 0:                     #36-8
        print("{}, {} fireballs costs {}. Would you still like this number of fireballs?").format(name,quantity,cost)
        answer= raw_input("\n y/n ")        #36-7
        if answer == 'y':       # if they agree input is what was meant, see what they will pay
            howPay(name, quantity, cost)
            break
        
        elif answer == 'n':     #if they choose no, get a new value 
            getQuantity(quantity, cost, name)
            #break #not sure if this is needed. see if broken
           
        else:
            print("\nYour choices are 'y' for 'YES', or 'n' for 'NO'. ")
        break
    if quantity == 0:
        print 'You chose 0 fireballs. This will end the dialogue. Choose a larger value to have returned change print to screen.'     

    # val check above takes care of invalid entry case
    
def howPay(name, quantity, cost):
    print("{}, {} fireballs costs: ${}. How much are you paying? (Use numbers please )\n").format(name,quantity, cost) #removed float
    paid=readVal(float, 'e.g., 0.50 ', 'is not the correct form. Try 1.00')

    changeOwed=float (paid - cost)      #36-5
    if changeOwed > 20.00:
        print 'Please use a smaller bill.'
        howPay(name, quantity, cost)
    else:
        if paid == cost:
            changeOwed=0
            print 'Exact change, great. Thanks for your business! Enjoy the candy.'
            return
        elif paid > cost: 
            print 'Great! Your change is: $', changeOwed
            determineChange(name, changeOwed, quantity, cost, paid)
        else:
            print "I'm sorry, that is not enough money. You need $", abs(paid-cost), 'more.'
            howPay(name, quantity, cost)
 
def determineChange(name, changeOwed, quantity, cost, paid):
    bills=(20, 10, 5, 1)                     # just using common low bills  
    coins=(25, 10, 5, 1)                     # just using common coins      #36-11
    billsReturned = []
    billsChange=[]
    while changeOwed > 1.00:        # If changed owed is greater than a dollar, enter the bills section                   
        dollars = int(changeOwed)
        for bill in bills:                  # 36-9
            billsChange, dollars =  divmod(dollars, bill)
            billsReturned.append(int(billsChange))
        break
    if billsChange != ' ':                  #36-6
        coinsReturned = []
        coinsChange=[]
        cents=changeOwed % 1
        
        remaining = int(cents*100)                          # I don't think I used a +=, but I can change a recursive to a loop and do it if required
        for coin in coins:
            coinsChange, remaining =  divmod(remaining, coin)  #36-5 (/ and %)
            coinsReturned.append(int(coinsChange))
          
        print'{}, you bought {} fireballs for ${}. You paid ${}. \n'.format(name, quantity, cost, paid) #36-13
        print'Your change is: '
        for amount, bill in zip(billsReturned, bills):      #36-11, 10
            print '   %d  $ %d bills ' % (amount, bill)
        for amount, coin in zip(coinsReturned, coins):  # can clean this up, put quarters dimes etc
            print '   %d  $0.%d '% (amount, coin)
     








if __name__ == "__main__":       # this code tells python that it's a script 
    start() 
