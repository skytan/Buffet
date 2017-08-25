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

#----------------------------exec a system cmd------------------------------
#a = 'C:\\"Program Files"\\Tencent\\QQ\\QQProtect\\Bin\\QQProtect.exe'
#cmd = '"' + a + '"'
#print cmd
#os.system(a)

#-----------------------------define global variables------------------------
USER_NAME = getpass.getuser()
COMPRESS_TEMP_DIR = 'D:\\User\\TanSky\Compress_temp'
COMPRESS_TOOL='C:\\Program Files\\7-Zip\\7z.exe'
SHARE_FOLDER = "\\\\c3-se-terminal3\\Shared_Folder\\Marine\\Superman\\Sky"

#------------------------------read configure file----------------------------
#home_dir = os.getcwd()
#home_dir = os.path.split(os.path.realpath(__file__))[0]
'''
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

if not os.path.exists( COMPRESS_TEMP_DIR ):
	os.makedirs( COMPRESS_TEMP_DIR )
	
if not os.path.exists( SHARE_FOLDER ):
	os.makedirs( SHARE_FOLDER )
	
time_name = time.strftime( "%Y-%m-%d_%H-%M-%S", time.localtime(time.time()) )
'''

#------------------------read the source file path-------------------------------
atrr = len(sys.argv)
print atrr
if atrr > 2:
	source_file = sys.argv[1]
	dst_file_name = sys.argv[2]
elif atrr > 1:
    source_file = sys.argv[1]
    dst_file_name = ""
else:
	source_file = raw_input("Please input correct format:")
if not os.path.exists(source_file):
	print "File not exist...."
	exit(1)

#------------------------create the temp zip file path----------------------------
#file_name = os.path.splitext(os.path.basename(source_file))
#dst_file_name = file_name[0]+ '-' + time_name +'.7z'
#temp_file = os.path.join( COMPRESS_TEMP_DIR, dst_file_name )
#temp_file = os.path.join( SHARE_FOLDER, dst_file_name )
file_name = os.path.splitext(os.path.basename(source_file))
if(dst_file_name ==""):
    dst_file_name = file_name[0] +'.zip'
temp_file = "deliverables.zip"
print dst_file_name

#------------------------run the zip commond--------------------------------------
command = '"'+COMPRESS_TOOL+'"'+' a -mx9 -tzip '+temp_file+' '+source_file
#command = '"'+COMPRESS_TOOL+'"'+' a -mx9 -t7z -ao '+temp_file+' '+source_file + ' -y'
print command
ps = subprocess.Popen( command )
if ps.wait() == 0:
    command1 = '"'+COMPRESS_TOOL+'"'+' a -mx9 -tzip '+dst_file_name+' '+temp_file
    print command1
    ps1 = subprocess.Popen( command1 )
    if ps1.wait() != 0:
        os.remove(temp_file)
        exit(1)

#-----------------------copy file to destination-----------------------------------
#shutil.move( temp_file, os.path.join( SHARE_FOLDER, dst_file_name) )
#shutil.copy( temp_file, SHARE_FOLDER )
#os.remove(temp_file)
