#!/bin/bash

idx=0
NVALUES="4 5 6 7 8 9 10 15 20 50 100"
MAXWEIGHTS="10 100 1000"

white='\033[00m'
red='\033[01;31m'
green='\033[01;32m'

for NLEAVES in ${NVALUES}; do
	for MAXWEIGHT in ${MAXWEIGHTS}; do
		idx=`expr ${idx} + 1`
		echo -ne "[${idx}]\tgen "
		python3 ./test.py gen "tests/${idx}.txt" "${NLEAVES}" "${MAXWEIGHT}" >> log.txt
		echo -ne "${green}[OK]${white} check "
		python3 ./test.py check "tests/${idx}.txt" "${NLEAVES}" "${MAXWEIGHT}" >> log.txt
		ret="$?"
		[ "${ret}" == 0 ] && echo -ne "${green}[OK]${white}" || echo -ne "${red}[NO]${white}"
		echo ""
	done
done
