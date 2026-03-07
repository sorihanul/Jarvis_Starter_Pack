@echo off
setlocal
if "%~1"=="" (
  echo Usage: run_ivk2_dual_profile.bat ROOT_PATH [HOT_DAYS]
  exit /b 1
)
set "SCRIPT_DIR=%~dp0"
set "PY_SCRIPT=%SCRIPT_DIR%ivk2_improved.py"
set "DATA_DIR=%SCRIPT_DIR%data"
set "HOT_DB=%DATA_DIR%\hot.sqlite"
set "COLD_DB=%DATA_DIR%\cold.sqlite"
set "ROOT=%~1"
set "HOT_DAYS=%~2"
if "%HOT_DAYS%"=="" set HOT_DAYS=30
if not exist "%DATA_DIR%" mkdir "%DATA_DIR%"

python "%PY_SCRIPT%" build "%ROOT%" --db "%HOT_DB%" --mtime-days-max %HOT_DAYS%
python "%PY_SCRIPT%" build "%ROOT%" --db "%COLD_DB%" --mtime-days-min %HOT_DAYS%

echo Done. hot/cold indexes built.
endlocal
