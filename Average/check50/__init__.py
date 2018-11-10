from check50 import *

class Average(Checks):

    @check()
    def exists(self):
        """Average.c exists"""
        self.require("Average.c")

    @check("exists")
    def compiles(self):
        """Average.c compiles"""
        self.spawn("clang -o Average Average.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_1_10_input(self):
        """Outputs 5.5"""
        self.spawn("./Average 1 10").stdout("5.5\n", "5.5\n").exit(0)
