num = eval(input("Enter a number:"))
sum = 0
IsRepeat = True

while IsRepeat == True:
    sum += num
    num = eval(input("Enter a number:"))
    if num == 0:
        print(f"the sum of all the given numbers is:{sum}")