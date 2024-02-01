from opcua import Server
import time
from opcua import ua

server = Server()

url = "opc.tcp://192.168.162.20:4840"
server.set_endpoint(url)

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

# 测试用
# AxisNumber = Param.add_variable(addspace, "AxisNumber", 0)
# AxisNumber.set_writable()

# 创建变量并设置NodeID以及数据类型
CNCChannels = Param.add_variable(addspace, "CNCChannels", 0)
CNCChannels.set_writable()

AxisNumber = Param.add_variable(addspace, "AxisNumber", 0)
AxisNumber.set_writable()

# AxisName = Param.add_variable(addspace, "AxisName", [])
# AxisName.set_array_dimensions([10])
# AxisName.set_data_type(ua.NodeId(ua.ObjectIds.String))
# AxisName.set_writable()
#
#
# CartAxis = Param.add_variable(addspace, "CartAxis", [])
# CartAxis.set_data_value(ua.DataValue(ua.Variant([], ua.VariantType.Float)))
# CartAxis.set_array_dimensions([10])
# CartAxis.set_writable()
#

CNCState = Param.add_variable(addspace, "CNCState", 0)
CNCState.set_writable()

CNCMode = Param.add_variable(addspace, "CNCMode", 0)
CNCMode.set_writable()

#
# CNCActValue = Param.add_variable(addspace, "CNCActValue", [0.0] * 32)
# CNCActValue.set_writable()
#
# CNCVar = Param.add_variable(addspace, "CNCVar", [])
# CNCVar.set_data_value(ua.DataValue(ua.Variant([], ua.VariantType.Float)))
# CNCVar.set_array_dimensions([10])
# CNCVar.set_writable()

#x, y, z编程值
CNCVar_x = Param.add_variable(addspace, "x_program_value", 0)
CNCVar_x.set_writable()

CNCVar_y = Param.add_variable(addspace, "y_program_value", 0)
CNCVar_y.set_writable()

CNCVar_z = Param.add_variable(addspace, "z_program_value", 0)
CNCVar_z.set_writable()

#
# PLCInX = Param.add_variable(addspace, "PLCInX", [])
# PLCInX.set_data_value(ua.DataValue(ua.Variant([], ua.VariantType.Float)))
# PLCInX.set_array_dimensions([5])
# PLCInX.set_writable()
#
# PLCOutY = Param.add_variable(addspace, "PLCOutY", [])
# PLCOutY.set_data_value(ua.DataValue(ua.Variant([], ua.VariantType.Float)))
# PLCOutY.set_array_dimensions([5])
# PLCOutY.set_writable()
#
# PLCMidR = Param.add_variable(addspace, "PLCMidR", 0)
# PLCMidR.set_data_value(ua.DataValue(ua.Variant(0, ua.VariantType.Int32)))
# PLCMidR.set_writable()
#
# CNCTeachState = Param.add_variable(addspace, "CNCTeachState", 0)
# CNCTeachState.set_data_value(ua.DataValue(ua.Variant(0, ua.VariantType.Int32)))
# CNCTeachState.set_writable()
#
# CNCLoadProgram = Param.add_variable(addspace, "CNCLoadProgram", 0)
# CNCLoadProgram.set_data_value(ua.DataValue(ua.Variant(0, ua.VariantType.Int32)))
# CNCLoadProgram.set_writable()
#
# CNCLine = Param.add_variable(addspace, "CNCLine", 0)
# CNCLine.set_data_value(ua.DataValue(ua.Variant(0, ua.VariantType.Int32)))
# CNCLine.set_writable()
#
# CNCAlarm = Param.add_variable(addspace, "CNCAlarm", [])
# CNCAlarm.set_data_value(ua.DataValue(ua.Variant([], ua.VariantType.String)))
# CNCAlarm.set_array_dimensions([5])
# CNCAlarm.set_writable()
#
# CNCCycle = Param.add_variable(addspace, "CNCCycle", 0)
# CNCCycle.set_data_value(ua.DataValue(ua.Variant(0, ua.VariantType.Int32)))
# CNCCycle.set_writable()
#
# CNCIsSingle = Param.add_variable(addspace, "CNCIsSingle", 0)
# CNCIsSingle.set_data_value(ua.DataValue(ua.Variant(False, ua.VariantType.Boolean)))
# CNCIsSingle.set_writable()

server.start()

print(f"Server started at {url}")

while True:
    # 在此处可以设置不同变量的值，例如：CNCChannels.set_value("New Value")
    time.sleep(1)
