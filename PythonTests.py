from sympy import false


def is_leap_year(year):
    #Write your code here. 
    #Don't change the function name.
    print (year % 4)
    print(year/100)
    print (year%100)
    print ((year/100)%2)
    print (year%400)
    
    if year % 4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else: return false
            
        else: return True
    else:
        return False
            
if is_leap_year(2020):
    print ("Leap year.")
else:
    print ("Not leap year.")