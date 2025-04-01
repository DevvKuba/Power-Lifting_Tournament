from lifters import *
import random

class Tournament:
    pass

class SchoolMatch:
    def __init__(self, school_1, school_2):
        pass

class Match:
    def __init__(self, team_1, team_2):
        self.contender_1 = random.choice(team_1)
        match_weight_class = self.contender_1["Weight Class"]
        self.contender_2 = [lifter for lifter in team_2 if lifter["Weight Class"] == match_weight_class]

    def display_match_contenders(self):
        return self.contender_1, self.contender_2

    def begin_match(self):
        pass

        # at random choose a lifter from each team,
        # the weight class is random out of the three, but needs to be the same for both lifters
        # same when it comes to the lift, random out of three but, the same one needs to be compared between the lifters
        # do this three times, once