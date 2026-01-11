cd /d %~dp0
call .venv\Scripts\activate.bat
pytest -v -s testCases/test_addCustomer.py --browser chrome
REM pytest -s -v -m "sanity" --html=./Reports/report.html testCases/test_addCustomer.py
REM pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome