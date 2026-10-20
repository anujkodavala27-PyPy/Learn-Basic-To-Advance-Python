num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(f"Num1 is {num1} greater")
elif num2 > num1:
    print(f"Num2 is {num2} greater")
else:
    print("Both are equal")