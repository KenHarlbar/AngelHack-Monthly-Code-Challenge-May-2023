from itertools import permutations


def get_avg(string):
	perms = list(permutations(string))
	num_list = []
	for p in perms:
		num = int(''.join(c for c in p))
		if num % 7 == 0:
			num_list.append(num)
	avg = (max(num_list) + min(num_list)) / 2
	print(num_list)
	print(avg)
	
	
if __name__ == '__main__':
	while True:
		string = str(input('string: '))
		get_avg(string)