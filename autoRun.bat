@echo off
mode con: cols=81
cd /d ".\program"
"..\python\App\python.exe" ".\main.py"
pause