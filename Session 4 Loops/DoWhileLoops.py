# Python version of do_while
# Python does not have a Do-While so we need to force it to go in at least once whithe a true and then  use an if to detect the change in the condition to break out of the loop.

print("count up")
i = 1
while True:
    print(i)
    i += 1
    if i > 5:
        break

i = 5
print("count down")
while True:
    print(i)
    i -= 1
    if i <= 0:
        break


i = 5
print("count down?")
while True:
    print(i)
    i += 1
    if not (i < 5):
        break

# Input validation example (do..while style)
choice = ""
while True:
    print("Enter data, 1 to 5 ")
    choice = input().strip()
    choice_char = choice[0] if choice else ""
    if '1' <= choice_char <= '5':
        break

print("Processing...")
