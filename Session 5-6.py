moves = 0
lives = 3

solution = "SSNWES"
move = ""



while True:

    value = input("You're in the maze, where do you want to go? (N,S,E,W): ")

    if value != "N" \
        and value != "S" \
        and value != "E" \
        and value != "W":

            print("Cannot make this move")

    moves += 1

    if lives == 0:
        print("You lost")
        break

    if moves == 10:
        lives -= 1
        print("You lost a life. " + lives, " lives left!")
        continue

    if direction.__contains__(solution):
        print("You got out in ", moves, " moves!")
        break
