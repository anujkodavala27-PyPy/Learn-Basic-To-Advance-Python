a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

result = 0

for i in range(abs(b)):
    result += a

if b < 0:
    result = -result

print(f"Product: {result}")