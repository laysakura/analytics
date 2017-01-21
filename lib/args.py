import sys


def get_arguments():
    if len(sys.argv) != 4:
        print("number of arugments must be 3.  code, from_date, to_date")
        sys.exit(1)

    return (sys.argv[1], sys.argv[2], sys.argv[3])
