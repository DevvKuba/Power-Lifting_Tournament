from lifters import *
import random

class Tournament:
    pass

class SchoolMatch:
    def __init__(self, school_1, school_2):
        self.school_1 = school_1
        self.school_2 = school_2
        pass

class Match:
    def __init__(self, team_1, team_2):
        self.contender_1 = random.choice(team_1)
        match_weight_class = self.contender_1["Weight Class"]
        contender_2 = [lifter for lifter in team_2 if lifter["Weight Class"] == match_weight_class]
        self.contender_2 = contender_2[0]

    def display_match_contenders(self):
        return self.contender_1, self.contender_2

    def begin_match(self):
        # now that lifters are passed in as objects, invoke a random lift within the match
        # loop 3 times who ever wins 2/3 wins
        contender_1_score = 0
        contender_2_score = 0
        lift_list = ["bench", "squat", "deadlift"]
        print(self.contender_1)
        print(self.contender_2)

        while contender_1_score < 3 and contender_2_score < 3:
            if contender_1_score == 2:
                return f"contender 1, {self.contender_1["Name"]} wins!"
            elif contender_2_score == 2:
                return f"contender 2, {self.contender_2["Name"]} wins!"

            current_lift = random.choice(lift_list)
            lift_list.remove(current_lift)
            if len(lift_list) == 0:
                lift_list = ["bench", "squat", "deadlift"]

            if current_lift == "bench":
                c1_bench = random.randint(self.contender_1["Bench"]-5, self.contender_1["Bench"]+5)
                c2_bench = random.randint(self.contender_2["Bench"] - 5, self.contender_2["Bench"] + 5)
                if c1_bench > c2_bench:
                    contender_1_score += 1
                elif c2_bench > c1_bench:
                    contender_2_score += 1
                else:
                    pass

            if current_lift == "squat":
                c1_squat = random.randint(self.contender_1["Squat"] - 5, self.contender_1["Squat"] + 5)
                c2_squat = random.randint(self.contender_2["Squat"] - 5, self.contender_2["Squat"] + 5)
                if c1_squat > c2_squat:
                    contender_1_score += 1
                elif c2_squat > c1_squat:
                    contender_2_score += 1
                else:
                    pass

            if current_lift == "deadlift":
                c1_deadlift = random.randint(self.contender_1["Deadlift"] - 5, self.contender_1["Deadlift"] + 5)
                c2_deadlift = random.randint(self.contender_2["Deadlift"] - 5, self.contender_2["Deadlift"] + 5)
                if c1_deadlift > c2_deadlift:
                    contender_1_score += 1
                elif c2_deadlift > c1_deadlift:
                    contender_2_score += 1
                else:
                    pass

            # maybe add some trackable rating system, for the school of the lifter,
            # either in match or in tournament/school match


