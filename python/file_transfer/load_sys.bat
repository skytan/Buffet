@ECHO OFF
rem "C:\\Program Files\\7-Zip\\7z.exe" a -mx9 -t7z file.7z write.py
rem "C:\\Program Files\\7-Zip\\7z.exe" x -o%~dp0 sys.7z -y
::"C:\\Program Files\\WinRAR\\WinRAR.exe" e -o sys.7z
python load_sys.py
::if %errorlevel%==1 exit
xrgn_usb.exe /r12 LDR.bin
xrgn_usb.exe /r14 SYS.bin
timeout /t 5
@ECHO ON