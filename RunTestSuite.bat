set WORKSPACE=%1
set times=%2

set TEST_RESULT_PATH=%WORKSPACE%\TestResults

echo Clean Environment.                   
cmd /c rd /S /Q %TEST_RESULT_PATH%\                      
cmd /c mkdir %TEST_RESULT_PATH%

echo START TEST SUITE 
cd %TEST_RESULT_PATH%
D:  

cmd /c copy %WORKSPACE%\template.html %TEST_RESULT_PATH%\results.html
cmd /c copy %WORKSPACE%\summary.html %TEST_RESULT_PATH%\summary.html
cmd /c copy %WORKSPACE%\scene.html %TEST_RESULT_PATH%\sceresults.html



for /l %%a in (1,1,%times%) do (
cmd /c jmeter -n -t %WORKSPACE%\anjuke.jmx -l %WORKSPACE%\TestResults\anjuke.jtl -L jmeter.util=DEBUG
)

for /l %%a in (1,1,%times%) do (
cmd /c jmeter -n -t %WORKSPACE%\haozu.jmx -l %WORKSPACE%\TestResults\haozu.jtl -L jmeter.util=DEBUG
)

for /l %%a in (1,1,%times%) do (
cmd /c jmeter -n -t %WORKSPACE%\aifang.jmx -l %WORKSPACE%\TestResults\aifang.jtl -L jmeter.util=DEBUG
)

for /l %%a in (1,1,%times%) do (
cmd /c jmeter -n -t %WORKSPACE%\jingjiren.jmx -l %WORKSPACE%\TestResults\jingjiren.jtl -L jmeter.util=DEBUG
)

for /l %%a in (1,1,%times%) do (
cmd /c jmeter -n -t %WORKSPACE%\weiliao.jmx -l %WORKSPACE%\TestResults\weiliao.jtl -L jmeter.util=DEBUG
)

for /l %%a in (1,1,%times%) do (
cmd /c jmeter -n -t %WORKSPACE%\weiliao_common.jmx -l %WORKSPACE%\TestResults\weiliao_common.jtl -L jmeter.util=DEBUG
)

ping -n 5 127.1 >nul 2>nul

cmd /c %WORKSPACE%\GenLog.py %TEST_RESULT_PATH%\anjuke.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html %WORKSPACE%\anjuke.jmx %times%
cmd /c %WORKSPACE%\GenLog.py %TEST_RESULT_PATH%\haozu.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html %WORKSPACE%\haozu.jmx %times%
cmd /c %WORKSPACE%\GenLog.py %TEST_RESULT_PATH%\aifang.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html %WORKSPACE%\aifang.jmx %times%
cmd /c %WORKSPACE%\GenLog.py %TEST_RESULT_PATH%\jingjiren.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html %WORKSPACE%\jingjiren.jmx %times%
cmd /c %WORKSPACE%\GenLog.py %TEST_RESULT_PATH%\weiliao_common.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html %WORKSPACE%\weiliao_common.jmx %times%

cmd /c %WORKSPACE%\SceneAPI.py %TEST_RESULT_PATH%\weiliao.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\sceresults.html AccountMessageSendAndGet 2
cmd /c %WORKSPACE%\SceneAPI.py %TEST_RESULT_PATH%\weiliao.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\sceresults.html AccountMsgBlackList 7
cmd /c %WORKSPACE%\SceneAPI.py %TEST_RESULT_PATH%\weiliao.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\sceresults.html ReadMessages 4
cmd /c %WORKSPACE%\SceneAPI.py %TEST_RESULT_PATH%\weiliao.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\sceresults.html ReceiveMessages 5
cmd /c %WORKSPACE%\SceneAPI.py %TEST_RESULT_PATH%\weiliao.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\sceresults.html BrokerSwitchStatus 4
cmd /c %WORKSPACE%\SceneAPI.py %TEST_RESULT_PATH%\weiliao.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\sceresults.html AppMsgBlackList 4
cmd /c %WORKSPACE%\SceneAPI.py %TEST_RESULT_PATH%\weiliao.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\sceresults.html AppMessageSendAndGet 2



ping -n 10 127.1 >nul 2>nul