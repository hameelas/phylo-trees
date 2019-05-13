#!/bin/bash

idx=0
NVALUES="4 5 6 7 8 9 10 15 20 50 100 200 300"
MAXWEIGHTS="10 100 1000 10000 1000000"

for NLEAVES in ${NVALUES}; do
	for MAXWEIGHT in ${MAXWEIGHTS}; do
		idx=`expr ${idx} + 1`
		echo -ne "[${idx}]\tgen "
		python3 ./test.py gen "tests/${idx}.txt" "${NLEAVES}" "${MAXWEIGHT}" >> log.txt
		sleep 1
		echo -ne "[OK] check "
		python3 ./test.py check "tests/${idx}.txt" >> log.txt
		ret="$?"
		echo -ne "ret = ${ret} "
		[ "${ret}" == 0 ] && echo -ne "[OK]" || echo -ne "[NO]"
		echo ""
	done
done
