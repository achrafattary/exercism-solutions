@echo off
set /p UserInputPath=what is the commit



git add .
git commit -m %UserInputPath%
git push