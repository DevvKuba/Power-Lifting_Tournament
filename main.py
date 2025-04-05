from lifters import *
from competitions import *

#Creating all our possible universities
university_1 = School("Loughborough", "East Midlands")
university_2 = School("UCL", "Greater London")
university_3 = School("UOW", "Greater London")
university_4 = School("NYU", "New York")

# First University
lifter_1 = PowerLifter( "Loughborough",85, 140, 110, 200, "Jerry")
lifter_2 = PowerLifter( "Loughborough",107, 210, 160, 270, "Mike")
lifter_3 = PowerLifter( "Loughborough",65, 125, 100, 190, "Joseph")
lifter_4 = PowerLifter( "Loughborough", 73, 130, 80, 160, "Chris")
lifter_5 = PowerLifter( "Loughborough", 84, 150, 105, 210, "Josh")

# Second University
lifter_6 = PowerLifter( "UCL",109, 230, 170, 260, "Bogdan")
lifter_7 = PowerLifter( "UCL",76, 105, 130, 200, "Ross")
lifter_8 = PowerLifter( "UCL",60, 110, 90, 150, "Philip")
lifter_9 = PowerLifter( "UCL", 105, 200, 180, 230, "Peter")
lifter_10 = PowerLifter( "UCL", 81, 140, 115, 195, "Daniel")

# Third University
lifter_11 = PowerLifter( "UOW",89, 150, 120, 180, "Kuba")
lifter_12 = PowerLifter( "UOW",108, 210, 140, 240, "Mathew")
lifter_13 = PowerLifter( "UOW",62, 130, 80, 190, "Nathan")
lifter_14 = PowerLifter( "UOW", 103, 190, 150, 260, "Crollos")
lifter_15 = PowerLifter( "UOW", 82, 160, 130, 215, "Sebastian")

# Fourth University
lifter_16 = PowerLifter( "NYU",78, 140, 115, 170, "Rick")
lifter_17 = PowerLifter( "NYU",110, 210, 165, 250, "Soloman")
lifter_18 = PowerLifter( "NYU",59, 110, 100, 160, "Fareh")
lifter_19 = PowerLifter( "NYU", 90, 180, 130, 215, "Simon")
lifter_20 = PowerLifter( "NYU", 86, 150, 105, 220, "Tony")


# assigning athletes to School's lifting team
university_1.assign_to_lifting_team(lifter_1)
university_1.assign_to_lifting_team(lifter_2)
university_1.assign_to_lifting_team(lifter_3)
university_1.assign_to_lifting_team(lifter_4)
university_1.assign_to_lifting_team(lifter_5)

university_2.assign_to_lifting_team(lifter_6)
university_2.assign_to_lifting_team(lifter_7)
university_2.assign_to_lifting_team(lifter_8)
university_2.assign_to_lifting_team(lifter_9)
university_2.assign_to_lifting_team(lifter_10)

university_3.assign_to_lifting_team(lifter_11)
university_3.assign_to_lifting_team(lifter_12)
university_3.assign_to_lifting_team(lifter_13)
university_3.assign_to_lifting_team(lifter_14)
university_3.assign_to_lifting_team(lifter_15)

university_4.assign_to_lifting_team(lifter_16)
university_4.assign_to_lifting_team(lifter_17)
university_4.assign_to_lifting_team(lifter_18)
university_4.assign_to_lifting_team(lifter_19)
university_4.assign_to_lifting_team(lifter_20)


# need to use parenthesis to call bound method object

university_1_team = university_1.create_comp_team()
university_2_team = university_2.create_comp_team()
practice_match_1 = Match(university_1_team, university_2_team)
# print(practice_match_1.begin_match())

university_3_team = university_3.create_comp_team()
university_4_team = university_4.create_comp_team()

international_tournament = Tournament(university_1_team, university_2_team, university_3_team, university_4_team)
print(international_tournament.begin_tournament_matches())









