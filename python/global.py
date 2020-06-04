
x = 5

def fn():
    """fn can access the global variable without the need to declare it global
    as long as it is only reading it and not writing on it."""
    print(x)

def bar():
    global y
    y = 10

def printZ():
    print(z)

if __name__ == "__main__":
    fn()
    bar()
    print(y)

    # Not need to use the global keyboard
    # Variables defined in an `if` block leak to the enclosing namespace
    z = 'shivam'
    printZ()
