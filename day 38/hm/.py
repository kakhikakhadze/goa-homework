first = int(input("enter your first num:"))
second = int(input("enter your first second num:"))
operation = (input("enter your operation:"))

if operation == "+":
    total = first + second
elif operation == "-":
    total = first - second
elif operation == "*":
    total = first * second
elif operation == "/":
    total = first / second
else:
    total = str("operation do not work")




print(total)