from typing import List

def greet(name: str) -> str:
    return "Hello " + name

def getList(n: int) -> List[str]:
    return ['Shivam']*n

if __name__ == "__main__":
    print(greet("Shivam"))
    l = getList(2)
    print(l)
