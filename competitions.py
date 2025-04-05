from lifters import *
import random

class Tournament:
    def __init__(self, school_team_1,school_team_2, school_team_3, school_team_4):
        self.schools_list = [school_team_1,school_team_2, school_team_3, school_team_4]
        self.schools_dict = {}
        team_number = 1
        while len(self.schools_list) != 0:
            school_choice = random.choice(self.schools_list)
            self.schools_dict["school_team_" + str(team_number)] = school_choice
            team_number += 1
            self.schools_list.remove(school_choice)


    # self.school_team_1 = self.schools_list.remove(random.choice(self.schools_list))
    # self.school_team_2 = self.schools_list.remove(random.choice(self.schools_list))
    # self.school_team_3 = self.schools_list.remove(random.choice(self.schools_list))
    # self.school_team_4 = self.schools_list.remove(random.choice(self.schools_list))

    def begin_tournament_matches(self):

        match_1 = Match(self.schools_dict["school_team_1"], self.schools_dict["school_team_2"])
        match_1_winner = match_1.begin_match()
        match_2 = Match(self.schools_dict["school_team_3"], self.schools_dict["school_team_4"])
        match_2_winner = match_2.begin_match()

        final_round = Match(match_1_winner, match_2_winner)
        winner = final_round.begin_match()
        return f"{winner["Name"]} has won the final round! {winner["School"]} wins"


    def return_participating_school_teams(self):
        return self.schools_dict




class Match:
    def __init__(self, team_1, team_2):
        if not isinstance(team_1, list) and not isinstance(team_2, list):
            self.contender_1 = team_1
            self.contender_2 = team_2
        else:
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

        while contender_1_score < 3 and contender_2_score < 3:
            if contender_1_score == 2:
                return self.contender_1
                # return f"contender 1, {self.contender_1["Name"]} wins! , from: {self.contender_1["School"]}"
            elif contender_2_score == 2:
                return self.contender_2
                # return f"contender 2, {self.contender_2["Name"]} wins!, from: {self.contender_1["School"]}"

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


