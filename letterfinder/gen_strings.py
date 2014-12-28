import sys
import random
import string

VALID_CHARS = string.digits + string.letters + string.punctuation

def gen_string(n, valid=VALID_CHARS):
    return ''.join(random.sample(valid, 1)[0] for i in range(n))

def main(args):
    num_lines, max_chars = [int(e) for e in args]
    random.seed("shar pug!")

    for n in range(num_lines):
        str_length = random.randint(1, max_chars)
        print gen_string(str_length)


if __name__ == "__main__":
    main(sys.argv[1:])
