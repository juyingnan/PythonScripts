#!/usr/bin/python

# Yue Chen

class BugPopulation:
    def __init__(self, initial_size):
        self.bug_number = initial_size
        print "Initialized. There are ", self.bug_number, " bugs in Lindley Hall now."

    def wait(self, time=1):
        self.bug_number = self.bug_number * (2 ** time)
        print time, " period(s) passed. There are ", self.bug_number, " bugs in Lindley Hall now."

    def clean(self):
        self.bug_number -= int(self.bug_number * 0.25)
        # self.bug_number = int(self.bug_number * 0.75)
        # This is another way. 1 bug more than the result of first way.
        print "Cleaned. There are ", self.bug_number, " bugs in Lindley Hall now."

    def check(self):
        print "Checked. There are ", self.bug_number, " bugs in Lindley Hall now."


# Test
initial_population = 11
cycle = 3
myLindlyHall = BugPopulation(initial_population)
for i in range(0, cycle):
    myLindlyHall.wait()
    myLindlyHall.clean()
    myLindlyHall.check()
