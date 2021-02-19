@echo off
set /a a=0
taskkill /f /im bilifans_num.exe
:a
TIMEOUT /T 600 /NOBREAK
set a=0
taskkill /f /im bilifans_num.exe
del *.txt
goto a