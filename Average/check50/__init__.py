from check50 import *

class Average(Checks):

    @check()
    def exists(self):
        """Average.c exists"""
        self.require("Average.c")

    @check("Compiles")
    def compiles(self):
        """Average.c compiles"""
        self.spawn("clang -o Average Average.c -lcs50 -lm").exit(0)

    @check("Averages 2 Numbers")
    def test_41_cents(self):
        """Outputs 5.5"""
        self.spawn("./Average").stdout("5.5\n").exit(0)
