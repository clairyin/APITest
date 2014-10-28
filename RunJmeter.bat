set WORKSPACE=%1
set times=%2

set TEST_RESULT_PATH=%WORKSPACE%\TestResults

echo Clean Environment.         
cmd /c rd /S /Q %TEST_RESULT_PATH%\                      
cmd /c mkdir %TEST_RESULT_PATH%

echo START TEST SUITE 
cd %TEST_RESULT_PATH%
D: 


for /l %%a in (1,1,%times%) do (
cmd /c jmeter -n -t %WORKSPACE%\anjuke.jmx -l %WORKSPACE%\TestResults\anjuke.jtl -L jmeter.util=DEBUG
)

