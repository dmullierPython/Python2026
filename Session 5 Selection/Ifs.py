#This program is demonstrating ifs, you'd never have a program with all 4 like this because the fourth one does it all and that's all you'd need.


#if it is raining outside, I will take my umbrella.
raining_outside = False
sunny = False

if raining_outside:
    print("I will take my umbrella.")
    print("as I don't want to get wet")
print("=========End of If 1===================")
#if it is raining outside, I will take my umbrella, if not I will take my baseball cap.
if raining_outside:
    print("I will take my umbrella.")
else:
    print("I will take my baseball cap.")
print("=========End of If 2===================")
#if it is raining outside, I will take my umbrella, or if it is sunny I will take my sun hat.
if raining_outside:
    print("I will not take my baseball cap.")
elif sunny:
    print("I will take my sun hat.")
print("=========End of If 3===================")
#if it is raining outside, I will take my umbrella, or if it is sunny I will take my sun hat, otherwise I will take my basball cap.
if raining_outside:
    print("I will not take my baseball cap.")
elif sunny:
    print("I will take my sun hat.")
else:
    print("I will take my baseball cap.")
print("=========End of If 4===================")