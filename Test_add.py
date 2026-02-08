from Addition import add
import os
import sys

a = int(os.getenv("NUM1", 0))
b = int(os.getenv("NUM2", 0))

if add(a, b) == a + b:
    print(f"TEST PASSED for {a} + {b}")
else:
    print(f"TEST FAILED for {a} + {b}")
    sys.exit(1)
