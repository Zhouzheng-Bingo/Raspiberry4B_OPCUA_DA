from pymodbus.client.sync import ModbusTcpClient
import struct

# Connection details for Modbus
HOST = '192.168.162.200'
PORT = 502

# Create a connection to the Modbus server
client = ModbusTcpClient(HOST, port=PORT)

# Connect to the server
if not client.connect():
    print("Unable to connect to the Modbus server!")
else:
    print("Connected successfully")


# Read data from Modbus
data = {}

# Read 剩余量（轴1-9偏移+4）
response = client.read_input_registers(572, count=2)
if response.isError():
    print("Error reading 剩余量（轴1-9偏移+4）")
else:
    # Swap the byte order
    int_value = (response.registers[1] << 16) + response.registers[0]
    # Convert the 32-bit integer into a float
    float_value = struct.unpack('!f', struct.pack('!I', int_value))[0]

    data["剩余量（轴1-9偏移+4）"] = float_value
    print(f"剩余量（轴1-9偏移+4）: {float_value}")

# Read 主轴编程位置
response = client.read_input_registers(1508, count=2)
if response.isError():
    print("Error reading 主轴编程位置")
else:
    # Swap the byte order
    int_value = (response.registers[1] << 16) + response.registers[0]
    # Convert the 32-bit integer into a float
    float_value = struct.unpack('!f', struct.pack('!I', int_value))[0]

    data["主轴编程位置"] = float_value
    print(f"主轴编程位置: {float_value}")

# Read 主轴速度实际值
response = client.read_input_registers(1524, count=2)
if response.isError():
    print("Error reading 主轴速度实际值")
else:
    # Swap the byte order
    int_value = (response.registers[1] << 16) + response.registers[0]
    # Convert the 32-bit integer into a float
    float_value = struct.unpack('!f', struct.pack('!I', int_value))[0]

    data["主轴速度实际值"] = float_value
    print(f"主轴速度实际值: {float_value}")

# Read 主轴修调
response = client.read_holding_registers(3, count=1)
if response.isError():
    print("Error reading 主轴修调")
else:
    data["主轴修调"] = response.registers[0]
    print(f"主轴修调: {response.registers[0]}")

# Read 轴实际速度
response = client.read_input_registers(400, count=2)
if response.isError():
    print("Error reading 轴实际速度")
else:
    # Swap the byte order
    int_value = (response.registers[1] << 16) + response.registers[0]
    # Convert the 32-bit integer into a float
    float_value = struct.unpack('!f', struct.pack('!I', int_value))[0]

    data["轴实际速度"] = float_value
    print(f"轴实际速度: {float_value}")

# Read 轴进给实际倍率
response = client.read_input_registers(404, count=2)
if response.isError():
    print("Error reading 轴进给实际倍率")
else:
    # Swap the byte order
    int_value = (response.registers[1] << 16) + response.registers[0]
    # Convert the 32-bit integer into a float
    float_value = struct.unpack('!f', struct.pack('!I', int_value))[0]

    data["轴进给实际倍率"] = float_value
    print(f"轴进给实际倍率: {float_value}")

# Read 绝对坐标编程值 for 轴1 to 轴9
for i in range(554, 572, 2):
    key = f"绝对坐标编程值（通道轴{i // 2 + 1}）"
    response = client.read_input_registers(i, count=2)
    if response.isError():
        print(f"Error reading {key}")
    else:
        # Swap the byte order
        int_value = (response.registers[1] << 16) + response.registers[0]
        # Convert the 32-bit integer into a float
        float_value = struct.unpack('!f', struct.pack('!I', int_value))[0]

        data[key] = float_value
        print(f"{key}: {float_value}")

# Read 工作模式
response = client.read_input_registers(0, count=2)
if response.isError():
    print("Error reading 工作模式")
else:
    work_mode_value = response.registers[0]
    work_mode_mapping = {
        0: "自动",
        1: "单步",
        2: "MDI",
        3: "手动",
        4: "手轮",
        5: "回零",
        6: "增量"
    }
    work_mode_str = work_mode_mapping.get(work_mode_value, "Unknown")
    data["工作模式"] = work_mode_str
    print(f"工作模式: {work_mode_str}")

# Read 工作状态
response = client.read_input_registers(1, count=1)
if response.isError():
    print("Error reading 工作状态")
else:
    work_status_value = response.registers[0]
    work_status_mapping = {
        1: "就绪",
        2: "运行",
        3: "暂停"
    }
    work_status_str = work_status_mapping.get(work_status_value, "Unknown")
    data["工作状态"] = work_status_str
    print(f"工作状态: {work_status_str}")



# Close the connection to Modbus
client.close()
