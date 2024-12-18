sum = 0 
odd = 0 
even = 0 

for x in range(1, 11):   
    num =eval(input("Enter a number:"))   
    sum += num     
    
    if num % 2 == 0:     
        even += num   
    
    else:     
        odd += num     
    
print(f"The total value of all the given number is {sum}:") 
print(f"The total value of all the EVEN number is {even}:") 
print(f"The total value of all the ODD number is {odd}:")