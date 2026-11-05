print("count up")
i = 1
while i <= 5:
    print(i)
    i += 1

i = 5
print("count down")
while i > 0:
    print(i)
    i -= 1

print("loop does nothing")
i = 5
print("count down?")
while i < 5:
    print(i)
    i += 1

# Input validation using while
print("Enter data, 1 to 5 ")
choice = input().strip()
choice_char = choice[0] if choice else ""

while choice_char < '1' or choice_char > '5':
    print("\nIncorrect!")
    print("Enter data, 1 to 5 ")
    choice = input().strip()
    choice_char = choice[0] if choice else ""

print("Processing...")
