# global in the function is variable that have the same value outside the local functions that you can use inside them without changing the global value
# globlal variables can be altered by any part of the code
x: int = 1


def foo():
    print(x)
    x = 4
    foo()
# we get error in this part of the code because the x is not assigned before being asked to be printed
