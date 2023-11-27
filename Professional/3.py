import sys

def determine_winner(socks_moves):
    last_player = 0
    last_socks = None
    for socks in socks_moves:
        print(socks)
        last_player = 1 - last_player
        last_socks = socks
    if last_socks % 2 == 0:
        return "Анри" if last_player == 1 else "Дима"
    else:
        return "Анри" if last_player == 0 else "Дима"
    

socks_moves = [int(line) for line in sys.stdin]
# socks_moves = [1, 3, 5, 10, 3, 2, 12]
winner = determine_winner(socks_moves)
print(winner)
