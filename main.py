import random

def simulate_point(player_a_prob, player_b_prob):
    # 根据概率决定谁赢得这一回合
    return 'A' if random.random() < player_a_prob / (player_a_prob + player_b_prob) else 'B'

def simulate_game(player_a_prob, player_b_prob):
    score_a = 0
    score_b = 0
    while True:
        winner = simulate_point(player_a_prob, player_b_prob)
        if winner == 'A':
            score_a += 1
        else:
            score_b += 1
        if (score_a >= 11 or score_b >= 11) and abs(score_a - score_b) >= 2:
            break
    return 'A' if score_a > score_b else 'B'

def simulate_match(player_a_prob, player_b_prob, best_of=3):
    wins_a = 0
    wins_b = 0
    while wins_a < best_of // 2 + 1 and wins_b < best_of // 2 + 1:
        winner = simulate_game(player_a_prob, player_b_prob)
        if winner == 'A':
            wins_a += 1
        else:
            wins_b += 1
    return 'A' if wins_a > wins_b else 'B'

# 示例：模拟10000场比赛，球员A的能力值为0.6，球员B的能力值为0.4，采用三局两胜制
player_a_prob = 0.6
player_b_prob = 0.4
best_of = 3
num_matches = 10000

wins_a = 0
wins_b = 0
for _ in range(num_matches):
    winner = simulate_match(player_a_prob, player_b_prob, best_of)
    if winner == 'A':
        wins_a += 1
    else:
        wins_b += 1

print(f"球员A获胜场次: {wins_a} ({wins_a / num_matches * 100:.1f}%)")
print(f"球员B获胜场次: {wins_b} ({wins_b / num_matches * 100:.1f}%)")
