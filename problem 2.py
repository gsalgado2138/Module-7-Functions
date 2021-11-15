#giovanni salgado
#11/13/2021
#problem 2
# Write a Python function to check whether a number is in a given range. Use range(1,10).
# Print whether the number is in or not in the range.
def inrange(g):
    if g in range(1,11):
        print(g, 'is in the range')
    else:
        print(g, "is not in the range")
inrange(4)