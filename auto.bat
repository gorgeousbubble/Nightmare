:: Nightmare Project - Git Auto Push(Github)
:: Copyright(C) 2019, Team Gorgeous Bubble, All Rights Reserved.
@echo off

:: Git Automatic Push to Remote Branch(Github)<default>
git pull origin master
git add .
git commit -m "Automatic Push to Remote Branch."
git push origin master