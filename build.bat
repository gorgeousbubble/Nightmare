:: Nightmare Project - Build(Python)
:: Copyright(C) 2019, Team Gorgeous Bubble, All Rights Reserved.
@echo off

:: Build Python target(Debug/Release)
set "build_target=Release"

:: Get the module dir name
set dirName =
goto getDirName

:: Get the absolute dir path
set absPath =
goto getAbsPath

:: Delete image process
taskkill /f /fi "IMAGENAME eq %dirName%.exe" > nul

for /f "skip=3 tokens=4" %%i in ('sc query AeLookupSvc') do set "zt=%%i"
if /i "%zt%"=="RUNNING" ( echo . ) else ( net start "AeLookupSvc" )

for /f "skip=3 tokens=4" %%i in ('sc query PcaSvc') do set "zt=%%i"
if /i "%zt%"=="RUNNING" ( echo . ) else ( net start "PcaSvc" )

:: Delete old compile file
if exist %dirName%.exe ( del %dirName%.exe ) > nul

:: Get dir name function
:getDirName
    set "lj=%~p0"
    set "lj=%lj:\= %"
    for %%a in (%lj%) do set wjj=%%a
    set dirName=%wjj%

:: Get absolute dir path
:getAbsPath
    set absPath=%~dp0

:: Build Python App
:build_python_app:
    echo build python app:
    echo .

    :: build target select
    if "%build_target%"=="Debug" ( goto build_debug ) else ( goto build_release )

:build_debug:
    :: Build Python(With debug information)
    echo [Build Debug]
    echo pyinstaller -n Nightmare -d -F main.py
    pyinstaller -n Nightmare -d all -F main.py
    echo.
    echo.

    :: Build Pause & Exit
    pause
    exit

:build_release:
    :: Build Python(Without debug information)
    echo [Build Release]
    echo pyinstaller -n Nightmare -F main.py
    pyinstaller -n Nightmare -F main.py
    echo.
    echo.

    :: Build Pause & Exit
    pause
    exit