def calculate_avg_score(players):
    player_scores = []
score_total = 0

for player in players:
    player_scores.append(player[1])
    score_total += player[1]

average_score = score_total / len(player_scores)