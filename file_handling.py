# -*- coding: utf-8 -*-
"""
Code to work on accessing, manipulating, handling and saving files on python.

Created on Sun Oct  9 19:15:48 2022.

@author: RUBIN
"""

# %% Write mode - create new file

file = open('test.txt', 'w')
file.write('New file created with "w" option in open command')
file.write('Lines created with file.write')
file.close()

# %% Append mode - append

file = open('test.txt', 'a')
file.write('New line appended with "a" option in open command')
file.write('This line and previous are appended with file.write')
file.close()

# %% Temporary Aliasing using with-as (avoids using .close function) 

with open('test.txt', 'r') as fr:
    for line in fr:
        print(line)

with open('test.txt', 'a+') as fa:
    #fa.next()
    fa.write("\n Line appended using aliasing")
    for line in fa:
        print(line)

# %% Rewrite file contents 
# Note:use r+ intead of w+

with open('test.txt', 'r+') as fw:
    fw.write('New rewritten file contents \n')
    for lines in fw:
        print(line)
    fw.close()
