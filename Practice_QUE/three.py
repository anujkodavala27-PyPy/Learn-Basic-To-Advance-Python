age = int(input("Enter your age :- "))

if age >= 18 and age <= 60:
    print("You can vote")
elif age >= 60:
    print("Your are senior")
else:
    print("Enter a valid age")
