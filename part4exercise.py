#(What’s Wrong with This Code?)
#def cube(x):
  #  """Calculate the cube of x."""
   # return x ** 3
#print('The cube of 2 is', cube(2))
#Ansver: return

#(What’s Does This Code Do?) What does the following mystery function do?
# Assume you pass the list [1, 2, 3, 4, 5] as an argument.
def mystery(x):
    y = 0
    value = int(1, 2, 3, 4, 5)

    for value in x:
        y += value ** 2
    return y
