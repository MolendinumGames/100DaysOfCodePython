
# Stage1: at crossroads : left or right?
# stage2: come to a lake: wait or swim?
# stage3: at island: 3doors, red yellow blue?

def main():
    treasure_ascii = r"""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
"""
    print("Welcome to your adventure!")
    stage1_answer = input("You are at a crossroads. Do you want to go left or right? (L/R) ").lower()
    if stage1_answer == "l":
        print("You come to a lake and see the island in the middle.")
        stage2_answer = input("Do you want to swim across or wait? (Swim/Wait) ").lower()
        if stage2_answer == "wait":
            print("You find a boat while looking around and get safely across.")
            print("At the island you find a house with 3 doors. The first one is red,"
                  + " the second one yellow and the third one is blue.")
            stage3_answer = input("What door do you go through? (Red/Yellow/Blue) ").lower()
            if stage3_answer == "red":
                print("A Dragon awaits you in the room and you die. Game Over!")
            elif stage3_answer == "blue":
                print("The floorboards give in and you fall into a trap! Game Over!")
            else:
                print(treasure_ascii)
                print("Congratulations, you found the treasure!")
        else:
            print("A giant sea creature emerges while you are halfway through the lake and eats you.")
            print("Game Over!")
    else:
        print("You come to a dead end. Game Over!")


main()
