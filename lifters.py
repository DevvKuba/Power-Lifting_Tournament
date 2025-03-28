import random

class PowerLifter:

    def __init__(self, school_name, weight, squat, bench, deadlift, first_name):
        self.school_name = school_name
        self.weight = int(weight)
        self.squat = squat
        self.bench = bench
        self.deadlift = deadlift
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
            "Total": self.calc_total(),
        }

        return self.info


class School:
    def __init__(self, school_name, region):
        self.school_name = school_name
        self.region = region
        self.ranking = None # can only be calculated after one tournament, changes with concurring tournaments
        self.lifters_list = []

    def assign_to_correct_school(self, lifter_info):
        if lifter_info["School"] == self.school_name:
            self.lifters_list.append(lifter_info)

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



class Team:
    pass


