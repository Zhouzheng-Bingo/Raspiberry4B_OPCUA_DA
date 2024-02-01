import paho.mqtt.client as mqtt
import struct
from opcua import Client

# MQTT服务器的地址
broker = "192.168.162.200"

# OPC UA服务器的地址
opcua_url = "opc.tcp://192.168.162.20:4840"

# 创建一个OPC UA客户端并连接到服务器
opcua_client = Client(opcua_url)
opcua_client.connect()

# 获取OPC UA服务器的节点

# AxisNumber_node = opcua_client.get_node("ns=2;i=2")

CNCChannels = opcua_client.get_node("ns=2;i=2")
AxisNumber = opcua_client.get_node("ns=2;i=3")
# AxisName = opcua_client.get_node("ns=2;i=4")
# CartAxis = opcua_client.get_node("ns=2;i=5")
CNCState = opcua_client.get_node("ns=2;i=4")
CNCMode = opcua_client.get_node("ns=2;i=5")
# CNCActValue = opcua_client.get_node("ns=2;i=5")
CNCVar_x = opcua_client.get_node("ns=2;i=6")
CNCVar_y = opcua_client.get_node("ns=2;i=7")
CNCVar_z = opcua_client.get_node("ns=2;i=8")
# PLCInX = opcua_client.get_node("ns=2;i=10")
# PLCOutY = opcua_client.get_node("ns=2;i=11")
# PLCMidR = opcua_client.get_node("ns=2;i=12")
# CNCTeachState = opcua_client.get_node("ns=2;i=13")
# CNCLoadProgram = opcua_client.get_node("ns=2;i=14")
# CNCLine = opcua_client.get_node("ns=2;i=15")
# CNCAlarm = opcua_client.get_node("ns=2;i=16")
# CNCCycle = opcua_client.get_node("ns=2;i=17")
# CNCIsSingle = opcua_client.get_node("ns=2;i=18")

# 当连接到MQTT服务器时被调用
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")

    # 测试用
    # client.subscribe("mallDis2PC_C0_P1002", 1)  # 订阅轴数

    client.subscribe("mallDis2PC_C1_P1001",1)  # 订阅通道数
    client.subscribe("mallDis2PC_C0_P1002",1)  # 订阅轴数
    # client.subscribe("mallDis2PC_C0_P1003",1)  # 订阅轴名
    # client.subscribe("mallDis2PC_C0_P1004",1)  # 订阅笛卡尔轴
    #
    client.subscribe("proDis2PC_C0_P2001",1)  # 订阅CNC状态
    client.subscribe("proDis2PC_C0_P2002",1)  # 订阅模式
    # client.subscribe("proDis2PC_C0_P2003",1)  # 订阅机床位置实际值
    client.subscribe("proDis2PC_C0_P2004",1)  # 订阅轴编程值
    # client.subscribe("proDis2PC_C0_P2005",1)  # 订阅PLC输入点X
    # client.subscribe("proDis2PC_C0_P2006",1)  # 订阅PLC输出点Y
    # client.subscribe("proDis2PC_C0_P2007",1)  # 订阅PLC中间变量R
    # client.subscribe("proDis2PC_C0_P2008",1)  # 订阅CNC示教状态
    # client.subscribe("proDis2PC_C0_P2009",1)  # 订阅CNC当前加载程序
    # client.subscribe("programLine2PC_C0_cmd",1)  # 订阅CNC当前运行行号
    # client.subscribe("cncAlarm2PC_C0_cmd",1)  # 订阅CNC报警信息
    # client.subscribe("ProDis2PC_C0_cmd",1)  # 订阅CNC运行周期数
    # client.subscribe("proDis2PC_C0_P2010",1)  # 订阅CNC是否处于单步运行模式

    data = 1
    byteArray = struct.pack('i',data)
    client.publish("mallPC2Dis_C0_cmd", byteArray)

    data2 = 2
    byteArray2 = struct.pack('i',data2)
    client.publish("mallPC2Dis_C0_cmd", byteArray2)

def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT Broker")

# 当接收到从MQTT服务器发来的消息时被调用
def on_message(client, userdata, msg):
    print(f"Topic: {msg.topic}")

    # 非周期数据表

    # 测试用
    # if msg.topic == "mallDis2PC_C0_P1002":
    #     # 轴数
    #     data = struct.unpack('i', msg.payload)[0]
    #     print(f"Axis number: {data}")
    #     if data is not None:
    #         AxisNumber_node.set_value(data)  # 将数据写入到OPC UA服务器的节点

    if msg.topic == "mallDis2PC_C1_P1001":
        # CNC通道数
        data = struct.unpack('i', msg.payload)[0]
        print(f"CNC Channels: {data}")
        if data is not None:
            CNCChannels.set_value(data)  # 将数据写入到OPC UA服务器的节点
    elif msg.topic == "mallDis2PC_C0_P1002":
        # 轴数
        data = struct.unpack('i', msg.payload)[0]
        print(f"Axis number: {data}")
        if data is not None:
            AxisNumber.set_value(data)  # 将数据写入到OPC UA服务器的节点
    # elif msg.topic == "mallDis2PC_Cx_P1003":
    #     # 轴名
    #     data = struct.unpack('s', msg.payload)[0]
    #     print(f"Axis Nmae: {data}")
    #     if data is not None:
    #         AxisName_node.set_value(data)  # 将数据写入到OPC UA服务器的节点
    # elif msg.topic == "mallDis2PC_Cx_P1004":
    #     # 笛卡尔轴
    #     data = struct.unpack('i', msg.payload)[0]
    #     print(f"Cartesian Axis: {data}")
    #     if data is not None:
    #         CartAxis_node.set_value(data)  # 将数据写入到OPC UA服务器的节点
    #
    # # 周期数据表
    elif msg.topic == "proDis2PC_C0_P2001":
        # CNC状态
        data2 = struct.unpack('i', msg.payload)[0]
        print(f"CNC State: {data2}")
        if data2 is not None:
            CNCState.set_value(data2)  # 将数据写入到OPC UA服务器的节点
    elif msg.topic == "proDis2PC_C0_P2002":
        # CNC模式
        data2 = struct.unpack('i', msg.payload)[0]
        print(f"CNC mode: {data2}")
        if data2 is not None:
            CNCMode.set_value(data2)  # 将数据写入到OPC UA服务器的节点
    # elif msg.topic == "proDis2PC_C0_P2003":
    #     # 机床位置实际值
    #     data2 = struct.unpack('32d', msg.payload)
    #     print(f"CNC Actual Value: {data2}")
    #     if data2 is not None:
    #         CNCActValue.set_value(list(data2))  # 将数据写入到OPC UA服务器的节点
    elif msg.topic == "proDis2PC_C0_P2004":
        # 轴编程值
        data = struct.unpack('32d', msg.payload)
        print(f"CNC Axis var: {data}")
        if data is not None:
            CNCVar_x.set_value(data[0])  # 将数据写入到OPC UA服务器的节点
            CNCVar_y.set_value(data[1])  # 将数据写入到OPC UA服务器的节点
            CNCVar_z.set_value(data[2])  # 将数据写入到OPC UA服务器的节点

    # elif msg.topic == "proDis2PC_C0_P2005":
    #     # PLC输入点X
    #     data2 = struct.unpack('i', msg.payload)[0]
    #     print(f"PLC Input X: {data}")
    #     if data is not None:
    #         PLCInX_node.set_value(data)  # 将数据写入到OPC UA服务器的节点
    # elif msg.topic == "proDis2PC_C0_P2006":
    #     # PLC输出点Y
    #     data2 = struct.unpack('i', msg.payload)[0]
    #     print(f"PLC Output Y: {data}")
    #     if data is not None:
    #         PLCOutY_node.set_value(data)  # 将数据写入到OPC UA服务器的节点
    # elif msg.topic == "proDis2PC_C0_P2007":
    #     # PLC中间变量R
    #     data2 = struct.unpack('i', msg.payload)[0]
    #     print(f"PLC Middle Value R: {data}")
    #     if data is not None:
    #         PLCMidR_node.set_value(data)  # 将数据写入到OPC UA服务器的节点
    # elif msg.topic == "proDis2PC_C0_P2008":
    #     # CNC示教状态
    #     data2 = struct.unpack('i', msg.payload)[0]
    #     print(f"CNC Teach State: {data}")
    #     if data is not None:
    #         CNCTeachState_node.set_value(data)  # 将数据写入到OPC UA服务器的节点
    # elif msg.topic == "proDis2PC_Cx_P2009":
    #     # CNC当前加载程序
    #     data2 = struct.unpack('s', msg.payload)[0]
    #     print(f"CNC Load Progress: {data}")
    #     if data is not None:
    #         CNCLoadProgresse_node.set_value(data)  # 将数据写入到OPC UA服务器的节点
    # elif msg.topic == "programLine2PC_Cx_cmd":
    #     # CNC当前运行行号
    #     data2 = struct.unpack('i', msg.payload)[0]
    #     print(f"CNC Line: {data}")
    #     if data is not None:
    #         CNCLine_node.set_value(data)  # 将数据写入到OPC UA服务器的节点
    # elif msg.topic == "cncAlarm2PC_C0_cmd":
    #     # CNC报警信息
    #     data2 = struct.unpack('s', msg.payload)[0]
    #     print(f"CNC Alarm: {data}")
    #     if data is not None:
    #         CNCAlarm_node.set_value(data)  # 将数据写入到OPC UA服务器的节点
    # elif msg.topic == "ProDis2PC_Cx_cmd":
    #     # CNC运行周期数
    #     data2 = struct.unpack('i', msg.payload)[0]
    #     print(f"CNC Cycle: {data}")
    #     if data is not None:
    #         CNCCycle_node.set_value(data)  # 将数据写入到OPC UA服务器的节点
    # elif msg.topic == "proDis2PC_Cx_P2010":
    #     # CNC是否处于单步运行模式
    #     data2 = struct.unpack('i', msg.payload)[0]
    #     print(f"CNC Is Single Mode: {data}")
    #     if data is not None:
    #         CNCIsSingle_node.set_value(data)  # 将数据写入到OPC UA服务器的节点


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

client.connect(broker, 1883, 60)

# 开始循环，处理网络事件
client.loop_start()

while True:pass
