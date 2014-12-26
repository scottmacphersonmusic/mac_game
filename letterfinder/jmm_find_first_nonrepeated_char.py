import sys

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

find_first_nrc = find_first_nrc_onepass

def main(args):
    assert find_first_nrc('') is None
    assert find_first_nrc('poo') == 'p'
    assert find_first_nrc('oop') == 'p'
    assert find_first_nrc('poop') is None

    with open(args[0]) as fp:
        for line in fp:
            onepass = find_first_nrc_onepass(line.strip())
            naive = find_first_nrc_naive(line.strip())
            assert onepass == naive


if __name__ == '__main__':
    main(sys.argv[1:])
