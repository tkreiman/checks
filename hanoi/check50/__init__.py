from check50 import *

class hanoi(Checks):

    @check()
    def exists(self):
        """hanoi.c exists"""
        self.require("hanoi.c")

    @check("exists")
    def compiles(self):
        """hanoi.c compiles"""
        self.spawn("clang -o hanoi hanoi.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_3_input(self):
        """Outputs Correct sequence for tower of 3"""
        self.spawn("./hanoi 3").stdout("A to C. A to B. C to B. A to C. B to A. B to C. A to C. ", "A to C. A to B. C to B. A to C. B to A. B to C. A to C. ").exit(0)
    
    @check("compiles")
    def test_4_input(self):
        """Outputs Correct sequence for tower of 4"""
        self.spawn("./hanoi 4").stdout("A to B. A to C. B to C. A to B. C to A. C to B. A to B. A to C. B to C. B to A. C to A. B to C. A to B. A to C. B to C. ", "A to B. A to C. B to C. A to B. C to A. C to B. A to B. A to C. B to C. B to A. C to A. B to C. A to B. A to C. B to C. ").exit(0)
