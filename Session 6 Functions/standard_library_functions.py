# Python has a huge library, it would be impossible to have them all available, so instead we import those that we need.


# library functions can be imported in several ways
# 1. Import the entire module
import math
help(math)
print("--------------------------")

print(math.floor(3.14))
print(math.ceil(3.14))

# yak! Much as I hate the American spelling, it is confusing to call it something different.
import math as maths
print(maths.floor(3.14))
print(maths.ceil(3.14))

# urg! Other languages don't allow this sort of nonsense.
from math import  *
print(floor(3.14))
print(ceil(3.14))
