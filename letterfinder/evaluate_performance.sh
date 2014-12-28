#!/bin/bash

# -- first run naive and onepass on the smaller test set
echo "small dataset, naive algorithm"
time python jmm_find_first_nonrepeated_char.py testset.lines1000.maxchars500 naive > results.l1000.c500.naive
echo "small dataset, one-pass algorithm"
time python jmm_find_first_nonrepeated_char.py testset.lines1000.maxchars500 onepass > results.l1000.c500.onepass
echo "md5 sums"
md5sum results.l1000.c500.onepass results.l1000.c500.naive

# -- now run on the larger test set
echo "large dataset, naive algorithm"
time python jmm_find_first_nonrepeated_char.py testset.lines1000.maxchars5000 naive > results.l1000.c5000.naive
echo "large dataset, one-pass algorithm"
time python jmm_find_first_nonrepeated_char.py testset.lines1000.maxchars5000 onepass > results.l1000.c5000.onepass
echo "md5 sums"
md5sum results.l1000.c5000.onepass results.l1000.c5000.naive
