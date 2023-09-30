import sys, getopt
from input_controller import *

def usage():
    print('python3 main.py -s <size> -c <num colors> -t <turns>')

def main(argv):
    size = 1
    colors = 1
    turns = 1

    try:
        opts, args = getopt.getopt(
            argv,
            "hs:c:t:",
            ["help", "size=", "colors=", "turns="]
        )
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-s", "--size"):
            size = arg
        elif opt in ("-c", "--colors"):
            colors = arg
        elif opt in ("-t", "--turns"):
            turns = arg

    print("size: ", size)
    print("colors: ", colors)
    print("turns: ", turns)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        usage()