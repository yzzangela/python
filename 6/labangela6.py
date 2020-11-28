# START LAB EXERCISE 06
print('Lab Exercise 06 \n')

#SETUP
mario_kart_game = [
('Peach', 49), ('Mario', 35), ('Yoshi', 23),
('Wario', 20), ('Daisy', 18), ('Luigi', 10)
]
# END SETUP
# PROBLEM 1 (5 points)
def scores(game):
    team_1_sum = 0
    for i in game[:3]:
        team_1_sum += i[1]
    team_2_sum = 0
    for i in game[3:]:
        team_2_sum += i[1]
    final = (team_1_sum, team_2_sum)
    return final


# PROBLEM 2 (5 points)
def blue_shell(game):
    # [second player, third player] + [first player] + [fourth player, ...]
    return game[1:3] + [game[0]] + game[3:]

# PROBLEM 3 (5 points)
# SETUP
new_mario_kart_game =  [
('Donkey Kong', 45), ('Mario', 30), ('Yoshi', 22),
('Wario', 20), ('Toad', 18), ('Peach', 15)
]

# END SETUP

# PROBLEM 4 (5 points)
def top_three(game):
    players = []
    for player_score in game[:3]:
        players.append(player_score[0])
    return players

# main()
def main():
    team_scores = scores(mario_kart_game)
    # Call < scores() > and assign to < team_scores >
    print(f'First game team scores: {team_scores}') ## Uncomment when ready!

    # Call < blue_shell() > and assign to < blue_shell_players >
    blue_shell_players = blue_shell(mario_kart_game)
    print(f'Player positions after blue shell: {blue_shell_players}') ## Uncomment when ready!

    # Add new character tuple to < new_mario_kart_game >
    new_mario_kart_game.insert(0, ('Bowser', 60))
    print(f'Updated new game: {new_mario_kart_game}') ## Uncomment when ready!

    # Call < top_three() > and assign to top_three_players
    top_three_players = top_three(new_mario_kart_game)
    print(f'Top three players: {top_three_players}') ## Uncomment when ready!

    # END LAB EXERCISE
