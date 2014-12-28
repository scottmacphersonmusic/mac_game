import sys
from collections import OrderedDict

def find_first_nrc_naive(st):
    for ch in st:
        if st.count(ch) == 1:
            return ch
    return None

def find_first_nrc_onepass(st):
    order_seen, seen, nr_counter = [], {}, 0
    for ch in st:
        if ch not in seen:
            order_seen.append({'char': ch, 'times_seen': 1})
            seen[ch] = (len(order_seen) - 1)
        else:
            order_seen[seen[ch]]['times_seen'] += 1
            while nr_counter < len(order_seen) and \
                  order_seen[nr_counter]['times_seen'] > 1:
                nr_counter += 1

    if nr_counter < len(order_seen):
        return order_seen[nr_counter]['char']
    return None

def find_first_nrc_onepass_od(st):
    seen, nr_counter = OrderedDict(), 0
    for ch in st:
        if ch not in seen:
            seen[ch] = 1
        else:
            seen[ch] += 1
            while nr_counter < len(seen) and \
                  seen.values()[nr_counter] > 1:
                nr_counter += 1

    if nr_counter < len(seen):
        return seen.keys()[nr_counter]
    return None

def main(args):
    testfile, version = args
    find_first_nrc = eval("find_first_nrc_" + version)

    with open(testfile) as fp:
        for line in fp:
            print find_first_nrc(line.strip())


if __name__ == '__main__':
    main(sys.argv[1:])
