import sys

if sys.byteorder == 'little':
    print('Little Endian Program')
else:
    print('Big Endian Program')