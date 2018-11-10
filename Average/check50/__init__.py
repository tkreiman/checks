from check50 import *

class Average(Checks):

    @check()
    def exists(self):
        """Average.c exists"""
        self.require("Average.c")

    @check("Compiles")
    def compiles(self):
        """Average.c compiles"""
        self.spawn("clang -fsanitize=signed-integer-overflow -fsanitize=undefined -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wshadow    Average.c  -lcrypt -lcs50 -lm -o Average").exit(0)

    @check("Averages 2 Numbers")
    def test_1_10_input(self):
        """Outputs 5.5"""
        self.spawn("./Average 1 10").stdout("5.5\n", "5.5\n").exit(0)
