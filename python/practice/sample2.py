from ctypes import *
import struct
import os
import shutil
import threading
import hashlib
import time
import datetime
import string
import subprocess
import ConfigParser
import getpass
import sys

def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
		return os.path.dirname(path)

#exec a system cmd
#a = 'C:\\"Program Files"\\Tencent\\QQ\\QQProtect\\Bin\\QQProtect.exe'
#cmd = '"' + a + '"'
#print cmd
#os.system(a)

#define global variables
USER_NAME = getpass.getuser()
COMPRESS_TEMP_DIR = 'E:\\Users\\'+USER_NAME+'\\compress_temp'
COMPRESS_TOOL='C:\\Program Files\\7-Zip\\7z.exe'
SHARE_FOLDER = "F:\\"

#read configure file
#home_dir = os.getcwd()
#home_dir = os.path.split(os.path.realpath(__file__))[0]
home_dir = cur_file_dir()
print home_dir
config_file = os.path.join(home_dir, "file_transfer.conf")
cf = ConfigParser.ConfigParser()
if not os.path.exists(config_file):
	cf.add_section("dir_config")
	cf.set("dir_config", "COMPRESS_TEMP_DIR", COMPRESS_TEMP_DIR)
	cf.set("dir_config", "SHARE_FOLDER", SHARE_FOLDER)
	cf.set("dir_config", "COMPRESS_TOOL", COMPRESS_TOOL)
	fp = open(config_file, "w")
	cf.write(fp)
	fp.close()
else:
	cf.read(config_file)
	COMPRESS_TEMP_DIR = cf.get("dir_config", "COMPRESS_TEMP_DIR")
	SHARE_FOLDER = cf.get("dir_config", "SHARE_FOLDER")
	COMPRESS_TOOL = cf.get("dir_config", "COMPRESS_TOOL")

#compress a source file
if not os.path.exists( COMPRESS_TEMP_DIR ):
	os.makedirs( COMPRESS_TEMP_DIR )
	
if not os.path.exists( SHARE_FOLDER ):
	os.makedirs( SHARE_FOLDER )
	
time_name = time.strftime( "%Y-%m-%d_%H-%M-%S", time.localtime(time.time()) )
if len(sys.argv) > 1:
	source_file = sys.argv[1]
else:
	source_file = raw_input("Please input file:")
dest_file = os.path.join( COMPRESS_TEMP_DIR, time_name )+'.7z'

command = '"'+COMPRESS_TOOL+'"'+' a -mx9 -t7z '+dest_file+' '+source_file
print command
ps = subprocess.Popen( command )
if ps.wait() != 0:
	exit(1)

#copy file to destination
shutil.copy( dest_file, SHARE_FOLDER )

#dest_file = "file.7z" dest_file
#command = '"C:\\Program Files\\7-Zip\\7z." a -mx9 -t7z file.7z write.py'
#os.system(command)

'''
#pack data
print struct.pack("<f", 238.3).encode("hex")

print struct.unpack("!f", '41973333'.decode('hex'))[0]

def convert(s):
    i = int(s,16)
    cp = pointer(c_int(i))
    fp = cast( cp, POINTER(c_float))
    return fp.contents.value

if __name__ == " __main__ ":
    convert(s)

#raw_input
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

ending = [ 'st', 'nd', 'rd' ]+ 17 * [ 'th' ] + [ 'st', 'nd', 'rd' ] + 7*['th'] + ['st']

year = raw_input('year:')
month = raw_input('month(1-12):')
day = raw_input('day(1-30):')

month_number = int(month)
day_number =int(day)


month_name = months[ month_number -1 ]
 

ordinal = day + ending[ day_number - 1 ]

print month_name + ' '+ ordinal + ', ' + year
'''


'''
#class defination
class peo:
    def __init__(self,name,age,sex):
        self.Name = name
        self.Age  = age
        self.Sex  = sex
    def speak(self):
        print "my name " + self.Name
    def __str__(self):
        msg = 'my name is: ' + self.Name + 'my age: ' + self.Age
        return msg
    
if __name__ == '__main__':
    peo('shanghai', '23', 'man')
'''

'''
import thread

def hello():
    for i in xrange(5):
        h_ok.acquire()
        print "hello"
        w_or.release()

def world():
    for i in xrange(5):
        w_ok.acquire()
        print "world"
        h_ok.release()

h_ok = thread.allocate_lock()
w_ok = thread.allocate_lock()

w_ok.acquire()

thread.start_new_thread(hello,())
thread.start_new_thread(world,())

raw_input("finish")
'''
