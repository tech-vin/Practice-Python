import os

path = os.path.expanduser('~')

print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
