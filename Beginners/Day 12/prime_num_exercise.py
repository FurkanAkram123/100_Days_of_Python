import math

def is_prime(num):

    #square root the number
    sqrt_num = int(math.sqrt(num))

    #if 1 or negative, return False
    if num <= 1:
        return False

    # If 2 return True
    elif num ==2:
        return True

    #if number divisible by 2 (all even numbers), return True
    elif num %2 == 0:
        return False

    #For all odd numbers, check if the number is divisible by any odd numbers starting from 3
    else:
        for i in range (3, sqrt_num+1, 2):
            if num % i == 0:
                return False
                
    return True

#Test the new function        
print (is_prime(75))
print (is_prime(73))               
                
    