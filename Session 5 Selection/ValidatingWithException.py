# this example uses EAFP "easier to ask for forgiveness than permission"
print("Enter a number 1 to 10")
number = input()
try:
    number = int(number)
except ValueError:
    print("That is not a number!")
    exit(1)

if number > 10:
    print("I said 1 to 10, not more than 10!")
elif number < 1:
    print("I said 1 to 10, not less than 1!")
else:
    print(f"Thank you for entering {number} you win.")
print("======End of If 1======")

# we can do this on one by using an OR.
if number > 10 or number < 1:
    print("I said 1 to 10, not more than 10 or less than 1!")
else:
    print(f"Thank you for entering {number} you win.")
print("======End of If 1======")
