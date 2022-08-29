#A Different Calculator

num1=input("insert a number:")
variable=input("insert a variable(+,-,*,/):")
num2=input("insert a number:")

add=float(num1) + float(num2)
subtract=float(num1) - float(num2)
multiply=float(num1) * float(num2)
divide=float(num1) / float(num2)

if variable == "+":
    print(add)
elif variable == "-":
    print(subtract)
elif variable == "*":
    print(multiply)
elif variable == "/":
    print(divide) 

else:
    print("Error")