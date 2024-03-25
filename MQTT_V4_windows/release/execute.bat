@echo off
echo Starting MQTTOPCUAServer.exe...
start MQTTOPCUAServer.exe
timeout /t 5 /nobreak
echo Starting MQTTOPCUAClient.exe...
start MQTTOPCUAClient.exe
timeout /t 5 /nobreak
echo Starting OPCUAClientGCode.exe...
start OPCUAClientGCode.exe
timeout /t 5 /nobreak
echo All programs have been started.
