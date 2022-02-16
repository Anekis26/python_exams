# Έστω μία σκακίερα 8*8 στην οποία τοποθετούμε πάνω της, σε τυχαίες θέσεις, έναν λευκό πύργο και ένα μαύρο αξιωματικό.
# Σε κάθε γύρο, ο κάθε παίκτης παίρνει ένα βαθμό αν το κομμάτι του τρώει κομμάτι του αντιπάλου.
# Μετά από 100 παιχνίδια, εμφανίστε τους βαθμούς των δύο παικτών.
# Επαναλλάβετε το πείραμα 100 φορές για σκακιέρες 7*7 και 7*8 και εμφανίστε τους αντίστοιχους βαθμούς των παικτών.
import random

# initializing the 8*8 chessboard and scores
score_w = 0
score_b = 0
chessboard = [[0] * 8 for i in range(8)]
counter8_8 = 0
while counter8_8 < 100:
    # placing the pieces on the board
    x1 = random.randint(0, 7)
    y1 = random.randint(0, 7)
    chessboard[x1][y1] = "W_tower"
    x2 = random.randint(0, 7)
    y2 = random.randint(0, 7)
    while x2 == x1 and y2 == y1:
        x2 = random.randint(0, 7)
        y2 = random.randint(0, 7)
    chessboard[x2][y2] = "B_bishop"

    if (x2 == x1) or (y2 == y1):
        score_w = score_w + 1
    if abs(x2 - x1) == abs(y2 - y1):
        score_b = score_b + 1
    counter8_8 = counter8_8 + 1
print("Game with 8*8 chessboard: ")
print("White =", score_w)
print("Black =", score_b)

# initializing the 7*7 chessboard and scores
score_w = 0
score_b = 0
chessboard = [[0] * 7 for i in range(7)]
counter7_7 = 0
while counter7_7 < 100:
    # placing the pieces on the board
    x1 = random.randint(0, 6)
    y1 = random.randint(0, 6)
    chessboard[x1][y1] = "W_tower"
    x2 = random.randint(0, 6)
    y2 = random.randint(0, 6)
    while x2 == x1 and y2 == y1:
        x2 = random.randint(0, 6)
        y2 = random.randint(0, 6)
    chessboard[x2][y2] = "B_bishop"

    if (x2 == x1) or (y2 == y1):
        score_w = score_w + 1
    if abs(x2 - x1) == abs(y2 - y1):
        score_b = score_b + 1
    counter7_7 = counter7_7 + 1
print("Game with 7*7 chessboard: ")
print("White =", score_w)
print("Black =", score_b)

# initializing the 7*8 chessboard and scores
score_w = 0
score_b = 0
chessboard = [[0] * 8 for i in range(7)]
counter7_8 = 0
while counter7_8 < 100:
    # placing the pieces on the board
    x1 = random.randint(0, 6)
    y1 = random.randint(0, 7)
    chessboard[x1][y1] = "W_tower"
    x2 = random.randint(0, 6)
    y2 = random.randint(0, 7)
    while x2 == x1 and y2 == y1:
        x2 = random.randint(0, 6)
        y2 = random.randint(0, 7)
    chessboard[x2][y2] = "B_bishop"

    if (x2 == x1) or (y2 == y1):
        score_w = score_w + 1
    if abs(x2 - x1) == abs(y2 - y1):
        score_b = score_b + 1
    counter7_8 = counter7_8 + 1
print("Game with 7*8 chessboard: ")
print("White =", score_w)
print("Black =", score_b)

