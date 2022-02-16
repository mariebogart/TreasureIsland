print("Welcome to Treasure Island. Your mission is to find the treasure!")
left_right = input("Would you like to go left or right?\n")
if left_right == "Left" or left_right == "left":
    swim_wait = input("Swim across, or wait for a boat?\n")
    if swim_wait == "Wait" or swim_wait == "wait":
        door = input("There is a red door, a yellow door, and a blue door in front of you. Which do you choose?\n")
        if door == "Yellow" or door == "yellow":
            print("You've reached the treasure! You Win!")
        elif door == "Red" or door == "red":
            print("You've been burned by fire! Game Over.")
        elif door == "Blue" or door == "blue":
            print("You've been eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("You were attacked by trout! Game Over!")
else:
    print("You fell into a hole! Game Over.")