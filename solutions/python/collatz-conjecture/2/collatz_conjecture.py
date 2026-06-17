"""bilangan collatz conjecture"""
def steps(number):
    """mencari bilangan collatz conjecture"""
    if not isinstance(number, int) or number < 1:
        
        raise ValueError("Only positive integers are allowed")
        
    count = 0
        
    while number != 1:
           if number % 2 == 0:
              number //= 2 # number = number // 2 (//=2), (// =2, wrong)
           else: # else (wrong) 
               number = 3 * number + 1
           count +=1
           
    return count
        
        