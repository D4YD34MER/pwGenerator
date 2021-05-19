import random
from string import ascii_lowercase, ascii_uppercase

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
lowerCase = []
for i in range(len(ascii_lowercase)):
	lowerCase.append(ascii_lowercase[i])
upperCase = []
for i in range(len(ascii_uppercase)):
	lowerCase.append(ascii_uppercase[i])
all = symbols + lowerCase + upperCase

print('Length: ', end='')
length = int(input())

pw = ''.join(random.choices(all, k=length))
print(pw)