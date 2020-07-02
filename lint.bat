:: Nightmare Project - Lint(Python)
:: Copyright(C) 2020, Team Gorgeous Bubble, All Rights Reserved.
@echo off

:: Set Python(python/python3)
set "python=python"

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

:: Python Lint files
:python_lint_files:
    echo python lint start:
    echo.
    echo.

    :: python lint cmds
    echo python lint cmds:
    %python% -m pylint %absPath%cmds
    echo.
    echo.

    :: python lint console
    echo python lint console:
    %python% -m pylint %absPath%console
    echo.
    echo.

    :: python lint const
    echo python lint const:
    %python% -m pylint %absPath%const
    echo.
    echo.

    :: python lint dbs
    echo python lint dbs:
    %python% -m pylint %absPath%dbs
    echo.
    echo.

    :: python lint console
    echo python lint console:
    %python% -m pylint %absPath%console
    echo.
    echo.

    :: python lint exec
    echo python lint exec:
    %python% -m pylint %absPath%exec
    echo.
    echo.

    :: python lint hash
    echo python lint hash:
    %python% -m pylint %absPath%hash
    echo.
    echo.

    :: python lint logs
    echo python lint logs:
    %python% -m pylint %absPath%logs
    echo.
    echo.

    :: python lint nets
    echo python lint nets:
    %python% -m pylint %absPath%nets
    echo.
    echo.

    :: python lint finished
    echo python lint finished.
    echo.
    echo.
