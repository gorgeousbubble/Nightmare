:: Nightmare Project - Clean(Python)
:: Copyright(C) 2019, Team Gorgeous Bubble, All Rights Reserved.
@echo off

:: Get the module dir name
set dirName =
goto getDirName

:: Get the absolute dir path
set absPath =
goto getAbsPath

:: Get dir name function
:getDirName
    set "lj=%~p0"
    set "lj=%lj:\= %"
    for %%a in (%lj%) do set wjj=%%a
    set dirName=%wjj%

:: Get absolute dir path
:getAbsPath
    set absPath=%~dp0

:: Clean Python App
:clean_python_app:
    echo clean python app:
    echo.
    echo.

    :: clean build folder
    echo clean build folder:
    rd /s /q %absPath%build
    echo.
    echo.

    :: clean dist folder
    echo clean dist folder:
    rd /s /q %absPath%dist
    echo.
    echo.

    :: clean log folder
    echo clean log folder:
    rd /s /q %absPath%log
    echo.
    echo.

    :: clean cache folder
    echo clean cache folder:
    rd /s /q %absPath%__pycache__
    echo.
    echo.

    :: clean spec file
    echo clean spec file:
    del %absPath%Nightmare.spec
    echo.
    echo.

    :: clean sub cache folder
    echo clean all sub cache folder:
    for /f "delims=" %%i in ('dir /ad/s/b cmds console const dbs logs nets') do echo rd /s /q %%i & (rd /s /q %%i)
    echo.
    echo.

    :: clean finished
    echo clean success.
    echo.
    echo.
