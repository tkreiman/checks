from check50 import *

class Average(Checks):

    @check()
    def exists(self):
        """Average.c exists"""
        self.require("Average.c")

    @check("Compiles")
    def compiles(self):
        """Average.c compiles"""
        self.spawn("make Average").exit(0)

    @check("Averages 2 Numbers")
    def test_1_10_input(self):
        """Outputs 5.5"""
        self.spawn("./Average 1 10").stdout("5.5\n", "5.5\n").exit(0)
