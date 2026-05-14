@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
set "PY_SCRIPT=%SCRIPT_DIR%ivk2_improved.py"
set "DATA_DIR=%SCRIPT_DIR%data"
set "DEFAULT_DB=%DATA_DIR%\index.sqlite"
set "PY_CMD="

if not exist "%DATA_DIR%" mkdir "%DATA_DIR%"

where python >nul 2>nul
if not errorlevel 1 set "PY_CMD=python"
if not defined PY_CMD (
  py -3 -c "import sys" >nul 2>nul
  if not errorlevel 1 set "PY_CMD=py -3"
)

if not defined PY_CMD (
  echo Python 3 is required. Install Python or enable the py launcher.
  exit /b 1
)

if "%~1"=="" (
  echo Usage:
  echo   run_ivk2.bat build ROOT_PATH
  echo   run_ivk2.bat query "question"
  echo   run_ivk2.bat stats
  echo   run_ivk2.bat vacuum
  echo.
  echo Default DB:
  echo   %DEFAULT_DB%
  exit /b 1
)

if /I "%~1"=="build" (
  if "%~2"=="" (
    echo build requires ROOT_PATH
    exit /b 1
  )
  %PY_CMD% "%PY_SCRIPT%" build "%~2" --db "%DEFAULT_DB%"
  exit /b %ERRORLEVEL%
)

if /I "%~1"=="query" (
  if "%~2"=="" (
    echo query requires a search string
    exit /b 1
  )
  %PY_CMD% "%PY_SCRIPT%" query "%~2" --db "%DEFAULT_DB%" -k 10
  exit /b %ERRORLEVEL%
)

if /I "%~1"=="stats" (
  %PY_CMD% "%PY_SCRIPT%" stats --db "%DEFAULT_DB%"
  exit /b %ERRORLEVEL%
)

if /I "%~1"=="vacuum" (
  %PY_CMD% "%PY_SCRIPT%" vacuum --db "%DEFAULT_DB%"
  exit /b %ERRORLEVEL%
)

%PY_CMD% "%PY_SCRIPT%" %*
endlocal
