import random

class PowerLifter:

    def __init__(self, school_name, weight, squat, bench, deadlift, first_name):
        self.school_name = school_name
        self.weight = int(weight)
        self.squat = int(squat)
        self.bench = int(bench)
        self.deadlift = int(deadlift)
        self.first_name = first_name
        self.weight_class = self.calc_weight_class()
        self.total = self.calc_total()
        self.info = self.lifter_info_dict()

    def calc_weight_class(self):
        if 50 < self.weight <= 70:
            self.weight_class = "Light Weight"
        elif 70 < self.weight <= 90:
            self.weight_class = "Medium Weight"
        elif 90 < self.weight <= 110:
            self.weight_class = "Heavy Weight"

        return self.weight_class

    def calc_total(self):
        bench_est = random.randint(self.bench-5, self.bench+5)
        squat_est = random.randint(self.squat-10, self.squat+10)
        deadlift_est = random.randint(self.deadlift-15, self.deadlift+15)
        total = (bench_est + squat_est + deadlift_est)
        return total

    def lifter_info_dict(self):
        self.info = {
            "Name": self.first_name,
            "School": self.school_name,
            "Weight": self.weight,
            "Weight Class": self.calc_weight_class(),
            "Bench": self.bench,
            "Squat": self.squat,
            "Deadlift": self.deadlift,
            "Total": self.calc_total(),
        }
        return self.info


class School:
    def __init__(self, school_name, region):
        self.school_name = school_name
        self.region = region
        self.ranking = None # can only be calculated after one tournament, changes with concurring tournaments
        self.school_team = None
        self.team_obj = None
        self.lifters_list = []


    def assign_to_lifting_team(self, lifter):
        if lifter.school_name == self.school_name:
            self.lifters_list.append(lifter.info)


    # need () to invoke as we passed in objects creating self.lifters_list
    def display_lifters(self):
        return self.lifters_list


    def display_top_lifter(self):
        pos = 0
        strength_dict = {}
        for lifter in self.lifters_list:
            strength_rating = lifter["Total"] / lifter["Weight"]
            strength_dict[pos] = f"{strength_rating:.2f}"
            pos += 1
        return self.lifters_list[max(strength_dict)]

    def create_comp_team(self):
        self.team_obj = Team(self.lifters_list)
        self.school_team = self.team_obj.assemble_team()
        return self.school_team

    def team_total(self):
        return f"{self.team_obj.combined_total()}kg"



class Team:

     def __init__(self, lifters_dicts):
         self.team = []
         self.team_total = 0
         self.lifters_dict = lifters_dicts

     def assemble_team(self):
         light_slot = 0
         medium_slot = 0
         heavy_slot = 0
         for lifter in self.lifters_dict:
            if lifter["Weight Class"] == "Medium Weight" and medium_slot == 0:
                self.team.append(lifter)
                medium_slot += 1
            elif lifter["Weight Class"] == "Heavy Weight" and heavy_slot == 0:
                self.team.append(lifter)
                heavy_slot += 1
            elif lifter["Weight Class"] == "Light Weight" and light_slot == 0:
                self.team.append(lifter)
                light_slot += 1
         return self.team


     def combined_total(self):
         for lifter in self.team:
             self.team_total += lifter["Total"]
         return self.team_total




