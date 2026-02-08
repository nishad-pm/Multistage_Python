import os

def add(a, b):
    return a + b

if __name__ == "__main__":
    try:
        print(add(int(os.getenv("NUM1", 10)), int(os.getenv("NUM2", 20))))
    except ValueError:
        print("Invalid input")
