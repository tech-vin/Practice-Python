import subprocess

txt = subprocess.check_output('dir', shell=True, universal_newlines=True)
print(txt)