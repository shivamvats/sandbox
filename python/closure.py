
def makeClosure(a, b):
    d = 1
    def closure(c):
        """The nested function must use the variables from the outer scope to \
        be turned into a closure."""
        print(a + b + c)
    return closure

if __name__ == "__main__":
    fn = makeClosure(1, 2)
    fn(3)
