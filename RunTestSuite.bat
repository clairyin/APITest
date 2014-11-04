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

for /l %%a in (1,1,%times%) do (
cmd /c jmeter -n -t %WORKSPACE%\wechat.jmx -l %WORKSPACE%\TestResults\wechat.jtl -L jmeter.util=DEBUG
)

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

ping -n 5 127.1 >nul 2>nul
cmd /c %WORKSPACE%\GenLog.py %TEST_RESULT_PATH%\wechat.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html %times%
cmd /c %WORKSPACE%\GenLog.py %TEST_RESULT_PATH%\anjuke.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html %times%
cmd /c %WORKSPACE%\GenLog.py %TEST_RESULT_PATH%\haozu.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html %times%
cmd /c %WORKSPACE%\GenLog.py %TEST_RESULT_PATH%\aifang.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html %times%
cmd /c %WORKSPACE%\GenLog.py %TEST_RESULT_PATH%\jingjiren.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html %times%
cmd /c %WORKSPACE%\GenLog.py %TEST_RESULT_PATH%\weiliao.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html %times%
cmd /c %WORKSPACE%\SceneAPI.py %TEST_RESULT_PATH%\weiliao.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html AccountMessageSendAndGet 2
cmd /c %WORKSPACE%\SceneAPI.py %TEST_RESULT_PATH%\weiliao.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html AccountMsgBlackList 7
cmd /c %WORKSPACE%\SceneAPI.py %TEST_RESULT_PATH%\weiliao.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html ReadMessages 4
cmd /c %WORKSPACE%\SceneAPI.py %TEST_RESULT_PATH%\weiliao.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html ReceiveMessages 5
cmd /c %WORKSPACE%\SceneAPI.py %TEST_RESULT_PATH%\weiliao.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html BrokerSwitchStatus 4
cmd /c %WORKSPACE%\SceneAPI.py %TEST_RESULT_PATH%\weiliao.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html AppMsgBlackList 4
cmd /c %WORKSPACE%\SceneAPI.py %TEST_RESULT_PATH%\weiliao.jtl %TEST_RESULT_PATH%\summary.html %TEST_RESULT_PATH%\results.html AppMessageSendAndGet 2



ping -n 10 127.1 >nul 2>nul