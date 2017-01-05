import os, sys

path = sys.argv[1]
pref = sys.argv[2]
count = int(sys.argv[3])
mode = int(sys.argv[4], 8)

fullpath = os.path.join(path, pref) 

for i in range(1, count+1):
    fold = fullpath + str(i)
    print(fold)
    os.mkdir(fold,mode)
