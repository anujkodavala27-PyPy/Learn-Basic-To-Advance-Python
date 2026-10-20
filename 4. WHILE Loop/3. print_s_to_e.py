# start and end by user
# start to end print using while loop

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

i = start
while i <= end:
    print(i, end=" ")
    i += 1
print("\n")
print(f"After while loop, start value is {start}")
