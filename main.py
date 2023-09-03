import sys
import time

import emoji


def todo():
    print("\n" + "#" * 25)
    print(emoji.emojize(" " * 6 + "Best of luck :ninja: "))
    print("#" * 25 + "\n")


def in_progress():
    print("#" * 20)
    for i in range(101):
        time.sleep(0.1)
        sys.stdout.write("\r%d%% completed work" % i)
        sys.stdout.flush()
    print("\n" + "#" * 20 + "\n")


def done():
    print("#" * 53)
    print(emoji.emojize(
        ":partying_face: :partying_face: :partying_face: Send it us @ email: hr@jeevee.com :saluting_face:  :saluting_face: :saluting_face:"))
    print("#" * 53 + "\n")


if __name__ == '__main__':
    todo()
    in_progress()
    done()
