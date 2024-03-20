import paho.mqtt.client as mqtt
import struct
from opcua import Client


# 当连接到MQTT服务器时被调用
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")

    # client.subscribe("proDis2PC_C0_P2001", 1)  # 订阅CNC状态
    client.subscribe("proDis2PC_C0_P2004", 1)  # 订阅轴编程值
    data = 1
    byteArray = struct.pack('i', data)
    client.publish("mallPC2Dis_C0_cmd", byteArray)

    data2 = 2
    byteArray2 = struct.pack('i', data2)
    client.publish("mallPC2Dis_C0_cmd", byteArray2)


def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT Broker")


# 当接收到从MQTT服务器发来的消息时被调用
def on_message(client, userdata, msg):
    print(f"Topic: {msg.topic}")


    # # 周期数据表
    if msg.topic == "proDis2PC_C0_P2001":
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

    elif msg.topic == "proDis2PC_C0_P2004":
        # 轴编程值
        data = struct.unpack('32d', msg.payload)
        print(f"CNC Axis var: {data}")
        if data is not None:
            CNCVar_x.set_value(data[0])  # 将数据写入到OPC UA服务器的节点
            CNCVar_y.set_value(data[1])  # 将数据写入到OPC UA服务器的节点
            CNCVar_z.set_value(data[2])  # 将数据写入到OPC UA服务器的节点


if __name__ == '__main__':

    # MQTT服务器的地址
    broker = "192.168.162.200"

    # OPC UA服务器的地址
    opcua_url = "opc.tcp://192.168.162.82:4840"

    # 创建一个OPC UA客户端并连接到服务器
    opcua_client = Client(opcua_url)
    opcua_client.connect()

    # 获取OPC UA服务器的节点

    # AxisNumber_node = opcua_client.get_node("ns=2;i=2")

    CNCChannels = opcua_client.get_node("ns=2;i=2")
    AxisNumber = opcua_client.get_node("ns=2;i=3")

    CNCState = opcua_client.get_node("ns=2;i=4")
    CNCMode = opcua_client.get_node("ns=2;i=5")

    CNCVar_x = opcua_client.get_node("ns=2;i=6")
    CNCVar_y = opcua_client.get_node("ns=2;i=7")
    CNCVar_z = opcua_client.get_node("ns=2;i=8")


    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    client.connect(broker, 1883, 60)

    # 开始循环，处理网络事件
    client.loop_start()

    while True: pass
