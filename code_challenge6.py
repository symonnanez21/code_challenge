name = input("Enter your name:") 
age =eval(input("Enter your age:")) 
if age >= 1 and age <= 8: 	
    print("Your age is considered as Toddler") 
if age >= 9 and age <= 14: 	
    print("Your age is considered as Preteen") 
if age >= 15 and age <= 18: 	
    print("Your age is considered as Teenage") 
if age >= 19 and age <= 27: 	
    print("Your age is considered as Early Adulthood") 
if age >= 28 and age <= 44: 	
    print("Your age is considered as Middle Age") 
if age >= 45 and age <= 59: 	
    print("Your age is considered as Post Adulthood") 
if age >= 60 and age <= 100: 	
    print("Your age is considered as Post Senior") 
    
else: 	
    print(f"Invalid Age")