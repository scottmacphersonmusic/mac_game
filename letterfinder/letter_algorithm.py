# return first letter that does not repeat or None
import sys

def find_first_nrc_imp1(st):
	nrc = {}
	for index, char in enumerate(st):
		if char not in nrc:
			nrc[char] = index
		else:
			nrc[char] = (len(st) - 1)
	reducer = lambda accum, next: accum if accum < next else next
	return st[reduce(reducer, nrc.values())]

def find_first_nrc_imp2(st):
	nrc = []
	rc  = []
	for char in st:
		if char in nrc:
			nrc.remove(char)
			rc.append(char)
		else:
			if char not in rc:
				nrc.append(char)
	if nrc:
		return nrc[0] 
	else:
		return None

find_first_nrc = find_first_nrc_imp2
 
for line in open(sys.argv[1]):
	print find_first_nrc(line.strip()),
