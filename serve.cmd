@echo off
REM Serve this folder over http://localhost:8000 and open the map.
REM Double-clicking index.html also works, but serving is the "real" way:
REM it lets the pages read locations.json directly instead of the bundled copy.
cd /d "%~dp0"
start "" http://localhost:8000/index.html
python -m http.server 8000
