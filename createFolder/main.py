import os
from os.path import expanduser

hDirectory = home = expanduser("~")

os.chdir(hDirectory)
for f in os.listdir('.'):
    if not f.startswith('.'):
        print(f)
dirLoc = input('choose a directory: ')
os.chdir(dirLoc)

while True:
    mainName = input('Please Enter the folder name(enter \'n\' to exit): ')
    if mainName == 'n':
        break
    os.mkdir(mainName)
    os.chdir(mainName)
    while True:
        subName = input('Please enter the name for subdirectory(enter \'n\' to exit): ')
        if subName == 'n':
            os.chdir('..')
            break
        os.mkdir(subName)

