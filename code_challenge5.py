#Create a program that will accept Prelim, Midterm, Semi-Final, Final, Quiz, Project Grade.
#Compute the final Grade: FG(prelim x 15%) + (midterm x 15%) + (semi-final x 15%) + (final x 15%) + (quiz x 25%) + (project x 15%)
#Display a remark Congratulations! You passed the course if final grade is 75 above; otherwise display Sorry, you failed

num1 = eval(input("Enter your grade in prelim here: "))
num2 = eval(input("Enter your grade in midterm here: "))
num3 = eval(input("Enter your semi-final grade here: "))
num4 = eval(input("Enter your grade in final here: "))
num5 = eval(input("Enter your grade in Quiz here: "))
num6 = eval(input("Enter your grade in project here: "))

fg = (num1 * .15) + (num2 * .15) + (num3 * .15) + (num4 * .15) + (num5 * .25) + (num6 * .15)

if fg >= 75 :
	print(f"Congratulations! You passed the course and your final grade is {fg}")
else :
	print(f"Sorry, you failed and your final grade is {fg}")