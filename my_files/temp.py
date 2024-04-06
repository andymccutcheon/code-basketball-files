team_1 = 120
team_2 = 110
team_1_won = team_1 > team_2 
team_2_won = team_1 < team_2 
teams_tied = team_1 == team_2 
teams_did_not_tie = team_1 != team_2

if team_1_won: 
    message = "nice job team 1!" 
elif team_2_won: 
    message = "nice job team 2!" 
else: message = "must have tied!?"

#print(message)

intro = "Let's see our superteam lineup: "
roster_dict = {
        'PG': 'caitlin clark', 
        'SG': 'paige beuckers',
        'SF': 'hailey van_lith', 
        'C': 'angel reese'
    }
"""
print(intro)
print(roster_dict['PG'])
print(roster_dict['SG'])
print(roster_dict['SF'])

roster_dict['C'] = 'angel_reese'
print(roster_dict)
"""
roster_list = ['caitlin clark', 'paige beuckers', 'hailey van_lith', 'angel reese', "flau'jae johnson"]
roster_list_upper = ['', '', '', '', '']
i=0
for player in roster_list: 
    roster_list_upper[i] = player.title()
    i = i+1
#print(roster_list_upper)

"""
for x in roster_dict: 
    print(f"position: {x}")
    print(f"player: {roster_dict[x]}")
 """
"""   
for x, y in roster_dict.items(): 
    print(f"position: {x}")
    print(f"player: {y}")
"""
"""
roster_list_proper = [x.title() for x in roster_list]
print(roster_list_proper)
"""
"""
roster_last_names = [full_name.split(' ')[1]
                     for full_name in roster_list]
print(roster_last_names)
"""

"""full_name = 'caitlin clark'
print(full_name.split(' ')[1])
"""

roster_k_only = [ 
    x for x in roster_list if x.startswith('f')]
print(roster_k_only)
















































