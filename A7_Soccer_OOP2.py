# Dakota Dowd, IS303
# This game accepts the name of teams in a soccer tournament, as well as how many games, 
# then outputs randomly assigned scores. At the end, final results are displayed.
"""
The goal of this assignment is to combine what you did in the original 
A4 Women's Soccer assignment (the one asking for inputs and looping 
through games) with the A5 Women’s Soccer OOP1 assignment, 
and now use the SoccerTeam class to store the variables for the home team 
as you’re looping through the games.
"""


import random


# Create a class called soccerTeam
class soccerTeam():

    def __init__(self, Team_Name, Wins, Losses, Goals_Scored, Goals_Allowed):
        self.Team_Name = Team_Name
        self.Wins = Wins
        self.Losses = Losses
        self.Goals_Scored = Goals_Scored
        self.Goals_Allowed = Goals_Allowed

# Method called seasonStatus
    def seasonStatus(self):
    # If they win at least 75%, then print out "Qualified for the NCAA Tournament"
        if (self.Wins/(self.Wins + self.Losses)) >= .75:
            sMessage = "Qualified for the NCAA Tournament!"
    # IF they win at least 50%, then print out "You had a good season"
        elif (self.Wins/(self.Wins + self.Losses)) >= .5:
            sMessage = "You had a good season."
    # Otherwise print "Your team needs to practice"
        else:
            sMessage = "Your team needs to practice."
    # return message
        return(sMessage)


# Ask the user for your soccer team name
sHomeTeam = input("Enter the name of the home team: ")

# Ask for how many games they should play/Initialize
iGamesNum = int(input(f"Enter the number of teams that {sHomeTeam} will play (1-10): "))

# Initialize variables
iWins = 0
iLosses = 0
iGoalsScored = 0
iGoalsAllowed = 0

# Loop through those games, calculating the scores of each team (make sure there are no ties)

for iCount in range(0, iGamesNum):
    sAwayTeam = input(f"\nEnter the name of the away team for game {iCount + 1}: " )
    iHomeScore = random.randint(1, 10)
    iAwayScore = random.randint(1, 10)
    # This prevents ties
    while iHomeScore == iAwayScore:
        iHomeScore = random.randint(1, 10)
        iAwayScore = random.randint(1, 10)
    # This prints out the Home and Away score
    print(f"{sHomeTeam}'s score: {iHomeScore} {sAwayTeam}'s score: {iAwayScore}")
    # Adjust the win/loss ratio
    if iHomeScore > iAwayScore:
        iWins += 1
    else:
        iLosses += 1
    iGoalsScored = iGoalsScored + iHomeScore
    iGoalsAllowed = iGoalsAllowed + iAwayScore


oTeam = soccerTeam(sHomeTeam, iWins, iLosses, iGoalsScored, iGoalsAllowed)

# Print final results

print(f"\nTeam Name: {oTeam.Team_Name}")
print(f"Final season record: {oTeam.Wins} - {oTeam.Losses}")
print(f"Total goals scored: {oTeam.Goals_Scored} - Total goals allowed: {oTeam.Goals_Allowed}")
print(oTeam.seasonStatus())
