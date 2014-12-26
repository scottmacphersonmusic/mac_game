import sys
import random
import string

NSTRINGS = 1000
MAX_LENGTH = 500
VALID_CHARS = string.digits + string.letters + string.punctuation

def gen_string(n, valid=VALID_CHARS):
    return ''.join(random.sample(valid, 1)[0] for i in range(n))

def main(args):
    random.seed("shar pug!")

    for n in range(NSTRINGS):
        str_length = random.randint(1, MAX_LENGTH)
        print gen_string(str_length)


if __name__ == "__main__":
    main(sys.argv[1:])
