from os import listdir
import time
#from os.path import isfile, join
import os.path
configpath = '/home/jonathan/.config/updates/'
onlyfiles = [ f for f in listdir(configpath) if os.path.isfile(os.path.join(configpath, f)) ]
for file in onlyfiles:
    print time.ctime(os.path.getctime(configpath+file))
