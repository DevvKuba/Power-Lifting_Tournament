from lifters import *

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
university_1.assign_to_lifting_team(lifter_1.lifter_info_dict())
university_1.assign_to_lifting_team(lifter_2.lifter_info_dict())
university_1.assign_to_lifting_team(lifter_3.lifter_info_dict())
university_1.assign_to_lifting_team(lifter_4.lifter_info_dict())
university_1.assign_to_lifting_team(lifter_5.lifter_info_dict())

university_2.assign_to_lifting_team(lifter_6.lifter_info_dict())
university_2.assign_to_lifting_team(lifter_7.lifter_info_dict())
university_2.assign_to_lifting_team(lifter_8.lifter_info_dict())
university_2.assign_to_lifting_team(lifter_9.lifter_info_dict())
university_2.assign_to_lifting_team(lifter_10.lifter_info_dict())

university_3.assign_to_lifting_team(lifter_11.lifter_info_dict())
university_3.assign_to_lifting_team(lifter_12.lifter_info_dict())
university_3.assign_to_lifting_team(lifter_13.lifter_info_dict())
university_3.assign_to_lifting_team(lifter_14.lifter_info_dict())
university_3.assign_to_lifting_team(lifter_15.lifter_info_dict())

university_4.assign_to_lifting_team(lifter_16.lifter_info_dict())
university_4.assign_to_lifting_team(lifter_17.lifter_info_dict())
university_4.assign_to_lifting_team(lifter_18.lifter_info_dict())
university_4.assign_to_lifting_team(lifter_19.lifter_info_dict())
university_4.assign_to_lifting_team(lifter_20.lifter_info_dict())


print(university_1.display_lifters())
university_1.create_comp_team()
print(university_1.team_total())




