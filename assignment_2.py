from score_stats import calculate_avg_score

"""
Input Example:

Enter player name


"""
# stpre players as a list of tupils
players = ["Sally", 95, ("Toby", 88), ("Sandeep", 10), ("Zainab", 5)]

# setup variables to store uuh summary values?
highest_score_player = (None, 0)
lowest_score_player = (None, 0)
average_score = 0

## pull the scores into a separate list
# declare a new variable  to hold a list of scores
# iterate over the player list
# add each score to the new list
player_scores = []
score_total = 0

for player in players:
    player_scores.append(player[1])
    score_total += player[1]

average_score = score_total / len(player_scores)
print(score_total)
print(player_scores)
"""
output examples:

=== summary ===
Players: 2
Highest Alice - 95
Lowest: cara - 88
Average 91.5
"""

# output player
#print("=== Summary ===")
print(f"Players: {len(players)}")
print(f"Highest  {None}") # Sally - 95
print(f"Lowest: {None}") # Zainab - 5
print(f"Average: {average_score}")