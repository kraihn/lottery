#! /usr/bin/env python
import sys

def main():		
	if len(sys.argv[1:]) == 4:
		probability(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))

	else:
		print 'Illegal number of arguments.'
		
def probability(m, n, t, p):
	if (1 <= m <= 1000) and (1 <= n <= m) and (1 <= t <= 100) and (1 <= p <= m):
		print 'valid'
		
	else:
		print 'Input requirements have not been met.'
	
	
	
if __name__ == '__main__':
	main()
