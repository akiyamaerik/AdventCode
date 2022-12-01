@echo off
setlocal

rem change directory to dir of this .bat file, needed when runing as admin
cd %~dp0
call repo_setup.bat
set CHERE_INVOKING=1
set PATH=C:\Devtools\Install\Cygwin\3.3.2\bin;%PATH%
echo Checking tool installations
echo Launching bash from Cygwin 3.3.2
bash --login -i
