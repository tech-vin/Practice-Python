# check whether a file path is a file or a directory.

import os

path = input('Enter Path: ')

file = '.'
if file in path:
    print('It is a file')
else:
    print('It is a directory')

# The correct way!
if os.path.isdir(path):
    print('It is a Directory')
elif os.path.isfile(path):
    print('It is a file')
else:
    print('Its iS a special file')
