@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
set "PY_SCRIPT=%SCRIPT_DIR%ivk2_improved.py"
set "DATA_DIR=%SCRIPT_DIR%data"
set "DEFAULT_DB=%DATA_DIR%\index.sqlite"

if not exist "%DATA_DIR%" mkdir "%DATA_DIR%"

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
  python "%PY_SCRIPT%" build "%~2" --db "%DEFAULT_DB%"
  exit /b %ERRORLEVEL%
)

if /I "%~1"=="query" (
  if "%~2"=="" (
    echo query requires a search string
    exit /b 1
  )
  python "%PY_SCRIPT%" query "%~2" --db "%DEFAULT_DB%" -k 10
  exit /b %ERRORLEVEL%
)

if /I "%~1"=="stats" (
  python "%PY_SCRIPT%" stats --db "%DEFAULT_DB%"
  exit /b %ERRORLEVEL%
)

if /I "%~1"=="vacuum" (
  python "%PY_SCRIPT%" vacuum --db "%DEFAULT_DB%"
  exit /b %ERRORLEVEL%
)

python "%PY_SCRIPT%" %*
endlocal
