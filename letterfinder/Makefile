# all: testset.lines1000.maxchars500 testset.lines1000.maxchars500
all: testset.lines1000.maxchars500 testset.lines1000.maxchars5000

testset.lines1000.maxchars500:
	python gen_strings.py 1000 500 > testset.lines1000.maxchars500

testset.lines1000.maxchars5000:
	python gen_strings.py 1000 5000 > testset.lines1000.maxchars5000

clean:
	rm -f testset.lines*.maxchars*
