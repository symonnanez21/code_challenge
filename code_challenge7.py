name = input("Enter your name:") 
purchase = input("Did you purchase a grocery today(yes/no):") 
item = input("What did you purchase:") 
price =eval(input("Item price:")) 
age = eval(input("Your age:")) 
bill = eval(input("Your payment:")) 

#if the total price is less than 4000 
result = (price * 0.123) 
taxp = (result + price) 
change = (bill - taxp ) 

if price >=1 and price <= 4000: 	
    print(f"Your change is:",change)

#if the total price is more than 4000, you have a discount of 3.8% 
result2 = (price * 0.038) 
discount = (price - result2) 
change2 = (bill - discount)

if price >=4001: 	
    print(f"Your change is:",change2) 

#if age is more than 60 and not higher than 150. 
result3 = (price * 0.123) 
discount2 = (price - result3) 
change3 = (bill - discount2 )

if age >=60 and age<= 150: 	
    print(f"Your change is:",change3)