import numpy as np
import string, subprocess


def length(a, b,c):

    if a in range(1, 100):
        gen_string = string.ascii_uppercase
    if b is True:
        gen_string += '!"№;%:?*()_+'
    if c is True:
        gen_string += '0123456789'

    random_symbols = np.random.randint(1, len(gen_string), a)
    return ''.join([gen_string[i] for i in random_symbols])



#print(length(50, True, True))


#subprocess.run(['touch', 'code.txt'])

file = open('1.py')
print(file.read())

data = file.readlines()
for line in data:
    word = line.split()
print(word)
