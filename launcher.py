import easykvchat.main
import sys
import os

args = []

if len(sys.argv) > 1:
    args = sys.argv[1:]

    if hasattr(sys, "_MEIPASS"):
        args = [os.path.join(sys._MEIPASS)] + args

sys.exit(easykvchat.main.run(args))
