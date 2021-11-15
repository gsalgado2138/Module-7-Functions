#giovanni salgado
#11/13/2021
#problem 4
#Write a Python function that takes a list of numbers and returns a new list with unique elements of the first list.
# Use list [1, 3, 3, 3, 6, 2, 3, 5]. Use the append function.
def list(l):
    g = []
    for i in l:
        if i not in g:
            g.append(i)
            return g
x = [1, 3, 3, 3, 6, 2, 3, 5]
print(list(x))