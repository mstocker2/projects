import os
import shutil

backupfile = input("Enter Backup File Name (YYYY-MM): ")
parent_dir = "/home/michael/Documents/GitHub/projects/pds/practice/"

path = os.path.join(parent_dir, backupfile)
os.mkdir(path)
print("Directory '% s' created" % path)

files = ['test.txt','test2.txt']
for f in files:
	shutil.copy(f, path)
