'''

Given a string e.g. ABCDAABCD. Shuffle he string so that no two smilar letters together.


@author ben
'''


def swap(input, src, dest):
	tmp = input[src]
	input[src] = input[dest]
	input[dest] = tmp

def shuffle_letters(input):
	if (len(input) == 0 or len(input) == 1):
		return input
	for i in range(len(input)-1):
		curchar = input[i]
		for j in range(i, len(input)):
			if input[j] != curchar:
				swap(input, i+1, j)
				break
	return input


if __name__ == '__main__':
	testIn = list("greeeeek")
	print(shuffle_letters(testIn))
