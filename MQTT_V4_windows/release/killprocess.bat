@echo off
echo Closing OPCUAClientGCode.exe...
taskkill /im OPCUAClientGCode.exe /f
timeout /t 5 /nobreak
echo Closing MQTTOPCUAClient.exe...
taskkill /im MQTTOPCUAClient.exe /f
timeout /t 5 /nobreak
echo Closing MQTTOPCUAServer.exe...
taskkill /im MQTTOPCUAServer.exe /f
timeout /t 5 /nobreak
echo All specified processes have been closed.

