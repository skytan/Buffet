import os
import shutil
import subprocess

SHARE_FOLDER = "Z:\\tansky\\edge1000\\sw\\"
COMPRESS_TOOL='C:\\Program Files\\WinRAR\\WinRAR.exe'

def compare(x, y):
    stat_x = os.stat(SHARE_FOLDER + x)
    stat_y = os.stat(SHARE_FOLDER + y)
    if stat_x.st_ctime < stat_y.st_ctime:
        return 1
    elif stat_x.st_ctime > stat_y.st_ctime:
        return -1
    else:
        return 0

iterms = os.listdir(SHARE_FOLDER)
iterms.sort(compare)

#for iterm in iterms:
#    print iterm
print iterms[0]
des = SHARE_FOLDER + iterms[0]
#shutil.copy( des, os.getcwd() )

#command = '"'+COMPRESS_TOOL+'"'+' a -mx9 -t7z '+temp_file+' '+source_file
command = '"'+COMPRESS_TOOL+'"'+' e -o '+des + ' -y'
print command
ps = subprocess.Popen( command )
if ps.wait() != 0:
	exit(1)

#os.remove(des)



