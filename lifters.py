import random

class PowerLifter:
    def __init__(self, school_name, weight, squat, bench, deadlift, first_name):
        self.school_name = school_name
        self.weight = int(weight)
        self.squat = squat
        self.bench = bench
        self.deadlift = deadlift
        self.first_name = first_name
        self.weight_class = None
        self.total = None
        self.info = None

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
        total = (bench_est + squat_est + deadlift_est)//3
        return f"{total}kg"

    def lifter_info_dict(self):
        self.info = {
            "Name": self.first_name,
            "School": self.school_name,
            "Weight Class": self.calc_weight_class(),
            "Total": self.calc_total(),
        }
        return self.info


class Team:
    pass

class School:
    pass
