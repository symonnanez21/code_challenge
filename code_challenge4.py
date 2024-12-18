name = input("What is your name:") 
dep = eval(input("Enter amount to deposit:")) 
thousand = dep // 1000 
bal = dep % 1000 
fiveh = bal // 500 
bal= bal % 500 
twoh = bal // 200 
bal = bal % 200 
oneh = bal // 100 
bal = bal % 100 
fifty = bal // 50 
bal = bal % 50 
twenty = bal // 20 
bal = bal % 20 
ten = bal // 10 
bal = bal % 10 
five = bal // 5 
bal = bal % 5 
one = bal // 1 
bal= bal % 1 


print(thousand,"-  1000") 
print(fiveh,"-  500") 
print(twoh,"-  200") 
print(oneh,"-  100") 
print(fifty,"-  50") 
print(twenty,"-  20") 
print(ten,"-  10") 
print(five,"-  5") 
print(one,"-  1")