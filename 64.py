import os.path, time
print(time.ctime(os.path.getctime('35.py')))
print(time.ctime(os.path.getmtime('35.py')))