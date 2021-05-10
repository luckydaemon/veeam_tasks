from TestCase1 import *
from TestCase2 import *

if __name__ == "__main__":
    test1= TestCase1(1, "First test")
    test1.execute()

    test2 = TestCase2(2, "Second test")
    test2.execute()