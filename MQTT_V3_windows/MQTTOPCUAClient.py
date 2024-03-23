import paho.mqtt.client as mqtt
import struct
from opcua import Client
import threading
import time

# 设置固定频率接收消息的时间间隔（秒）
PROCESS_INTERVAL = 0.0005
# 上一次处理消息的时间戳
last_process_time = time.time() - PROCESS_INTERVAL


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe("mallDis2PC_C1_P1001", 0)
    client.subscribe("mallDis2PC_C0_P1002", 0)
    client.subscribe("proDis2PC_C0_P2001", 0)
    client.subscribe("proDis2PC_C0_P2002", 0)
    client.subscribe("proDis2PC_C0_P2003", 0)
    client.subscribe("proDis2PC_C0_P2004", 0)
    client.subscribe("programLine2PC_C0_cmd", 0)
    client.subscribe("proDis2PC_C0_P2010", 0)
    client.subscribe("proDis2PC_C0_P2009", 0)

def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT Broker")


def process_message(msg):
    # 解析不同主题的消息并更新OPC UA节点
    # if msg.topic == "mallDis2PC_C1_P1001":
    #     data = struct.unpack('i', msg.payload)[0]
    #     CNCChannels.set_value(data)
    #     print(f"Updated CNC Channels: {data}")
    # elif msg.topic == "mallDis2PC_C0_P1002":
    #     data = struct.unpack('i', msg.payload)[0]
    #     AxisNumber.set_value(data)
    #     print(f"Updated Axis Number: {data}")
    if msg.topic == "proDis2PC_C0_P2001":
        data = struct.unpack('i', msg.payload)[0]
        CNCState.set_value(data)
        print(f"Updated CNC State: {data}")
    elif msg.topic == "proDis2PC_C0_P2002":
        data = struct.unpack('i', msg.payload)[0]
        CNCMode.set_value(data)
        print(f"Updated CNC Mode: {data}")
    elif msg.topic == "proDis2PC_C0_P2003":
        data = struct.unpack('32d', msg.payload)
        CNCVarAct_x.set_value(data[0])
        CNCVarAct_y.set_value(data[1])
        CNCVarAct_z.set_value(data[2])
        CNCVarAct_a.set_value(data[3])
        CNCVarAct_c.set_value(data[4])
        print(f"Updated CNC Axis Vars: X={data[0]}, Y={data[1]}, Z={data[2]}")
    elif msg.topic == "proDis2PC_C0_P2004":
        data = struct.unpack('32d', msg.payload)
        CNCVar_x.set_value(data[0])
        CNCVar_y.set_value(data[1])
        CNCVar_z.set_value(data[2])
        CNCVar_a.set_value(data[3])
        CNCVar_c.set_value(data[4])
        print(f"Updated CNC Axis Vars: X={data[0]}, Y={data[1]}, Z={data[2]}")
    elif msg.topic == "programLine2PC_C0_cmd":
        data = struct.unpack('i', msg.payload)[0]
        CurrrentLine.set_value(data)
        print(f"Updated CNC CurrentLine: {data}")
    elif msg.topic == "proDis2PC_C0_P2010":
        data = struct.unpack('i', msg.payload)[0]
        IsSingleStepExecutionMode.set_value(data)
        print(f"Updated CNC IsSingleStepExecutionMode: {data}")
    elif msg.topic == "proDis2PC_C0_P2009":
        if msg.topic == "proDis2PC_C0_P2009":
            # 解析长度为128的字符串
            data = struct.unpack('128s', msg.payload)[0]

            # 解码字符串，使用UTF-8编码，替换无法解码的字符，并去除尾随的空字符
            fileName = data.decode('utf-8', errors='replace').rstrip('\x00')

            # 使用正则表达式提取有效的程序名部分
            import re
            match = re.search(r'\A[ -~]+', fileName)
            if match:
                clean_filename = match.group()
                print(f"Clean Program file name: {clean_filename}")
            else:
                print("No valid program file name found.")
                clean_filename = ""  # 使用空字符串，因为没有找到有效的文件名

            # 将解析出的文件名写入到OPC UA节点
            try:
                # 假设 ProgramFileName 是您已经创建的 OPC UA 节点对象
                ProgramFileName.set_value(clean_filename)
                print(f"ProgramFileName set to {clean_filename} in OPC UA server.")
            except Exception as e:
                print(f"Failed to write ProgramFileName to OPC UA server: {e}")


def on_message(client, userdata, msg):
    global last_process_time
    current_time = time.time()

    if current_time - last_process_time >= PROCESS_INTERVAL:
        last_process_time = current_time
        threading.Thread(target=process_message, args=(msg,)).start()
    else:
        print(f"Message from topic: {msg.topic} dropped due to high frequency.")


if __name__ == '__main__':
    broker = "192.168.162.201"
    opcua_url = "opc.tcp://localhost:48020/"

    # 创建MQTT客户端并连接
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.connect(broker, 1883, 60)

    # 创建OPC UA客户端并连接
    opcua_client = Client(opcua_url)
    opcua_client.connect()

    # 获取并设置OPC UA节点
    # CNCChannels = opcua_client.get_node("ns=2;i=2")
    # AxisNumber = opcua_client.get_node("ns=2;i=3")
    CNCState = opcua_client.get_node("ns=2;i=1020")
    CNCMode = opcua_client.get_node("ns=2;i=1019")
    CNCVar_x = opcua_client.get_node("ns=2;i=8460")
    CNCVar_y = opcua_client.get_node("ns=2;i=8461")
    CNCVar_z = opcua_client.get_node("ns=2;i=8462")
    CNCVar_a = opcua_client.get_node("ns=2;i=8463")
    CNCVar_c = opcua_client.get_node("ns=2;i=8464")
    CNCVarAct_x = opcua_client.get_node("ns=2;i=8472")
    CNCVarAct_y = opcua_client.get_node("ns=2;i=8473")
    CNCVarAct_z = opcua_client.get_node("ns=2;i=8474")
    CNCVarAct_a = opcua_client.get_node("ns=2;i=8475")
    CNCVarAct_c = opcua_client.get_node("ns=2;i=8476")

    # CNC当前运行行号
    CurrrentLine = opcua_client.get_node("ns=2;i=8465")
    # 是否单步执行
    IsSingleStepExecutionMode = opcua_client.get_node("ns=2;i=8466")
    # 程序名
    ProgramFileName = opcua_client.get_node("ns=2;i=8467")

    # 开始MQTT客户端循环
    client.loop_start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program stopped manually")
        client.loop_stop()
        opcua_client.disconnect()
