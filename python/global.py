
x = 5

def fn():
    """fn can access the global variable without the need to declare it global
    as long as it is only reading it and not writing on it."""
    print(x)

if __name__ == "__main__":
    fn()
