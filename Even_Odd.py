# Write a program to check if the no is odd or even


x = int(input("Enter a no: "))
print(x)
even = x % 2
odd = x % 5
if x % 2 == 0:
    print("even")
else:
    print("odd")


given_digit = int(input("Enter a number: "))
if given_digit % 2 == 1:
    print("odd")
else:
    print("even")