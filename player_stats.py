player_name = str(input('Enter the name of the player: '))
player_team_name = str(input("Enter the name of the player's team name: "))
player_total_runs_in_ODI = int(input('Enter total runs in ODI: '))
player_total_runs_in_T20I = int(input('Enter total runs in T20I: '))
player_total_runs_in_Test = int(input('Enter total runs in Test: '))
player_total_runs_in_IPL = int(input('Enter total runs in IPL: '))
#average value comes with decimal so it should belong to float data-type
player_average_of_runs = (player_total_runs_in_ODI+player_total_runs_in_T20I+player_total_runs_in_Test+player_total_runs_in_IPL)/4 
print("				PLAYER STATS				")
print("	player_name: ", player_name)
print("	player_team_name: ", player_team_name)
print("	player_total_runs_in_ODI: ", player_total_runs_in_ODI)
print("	player_total_runs_in_T20I: ", player_total_runs_in_T20I)
print("	player_total_runs_in_Test: ", player_total_runs_in_Test)
print("	player_total_runs_in_IPL: ", player_total_runs_in_IPL)
print("	player_average_of_runs: ", player_average_of_runs)
print("-------------------------------------------------------------------------")
print("		Data Field Identifier & Data Type		")
print("	player_name: ", type(player_name))
print("	player_team_name: ", type(player_team_name))
print("	player_total_runs_in_ODI: ", type(player_total_runs_in_ODI))
print("	player_total_runs_in_T20I: ", type(player_total_runs_in_T20I))
print("	player_total_runs_in_Test: ", type(player_total_runs_in_Test))
print("	player_total_runs_in_IPL: ", type(player_total_runs_in_IPL))
print("	player_average_of_runs: ", type(player_average_of_runs))
print("-------------------------------------------------------------------------")
print("		Reasons for using this data-type		")
print("	player_name: Names may contain letters and any other characters")
print("	player_team_name: Names may contain letters and any other characters")
print("	player_total_runs_in_ODI: Runs are always numeric(int) literals")
print("	player_total_runs_in_T20I: Runs are always numeric(int) literals")
print("	player_total_runs_in_Test: Runs are always numeric(int) literals")
print("	player_total_runs_in_IPL: Runs are always numeric(int) literals")
print("	player_average_of_runs: Runs are always numeric(float) literals")
