import random
import time


def howToWinACofee():
    print("Simple rules, heads I win, tail you lose.")
    print("The loser pays a coffee to the winner !")
    print("Are you ready ? (press any key to continue...)")
    input()
    rand = random.randrange(20, 40, 1)
    timing = 0.05
    coin = {
        0: "Tail",
        1: "Heads",
    }
    for i in range(rand):
        print(f"\r{coin[i % 2]} ", end="", flush=True)
        time.sleep(timing)
        timing += 0.01
    print("")
    if i % 2 == 0:
        print("You lose...")
    else:
        print("I win !")
