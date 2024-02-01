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

# 创建变量并设置NodeID以及数据类型

# Read 剩余量（轴1-9偏移+4）
axisresidual = Param.add_variable(addspace, "axisresidual", 0.0)
axisresidual.set_writable()

# Read 主轴编程位置
spindleprogrammingpos = Param.add_variable(addspace, "spindleprogrammingspeed", 0.0)
spindleprogrammingpos.set_writable()

# Read 主轴速度实际值
actualspindlevelocity = Param.add_variable(addspace, "actualspindlevelocity", 0.0)
actualspindlevelocity.set_writable()

# Read 主轴修调
spindletrimmingvalue = Param.add_variable(addspace, "spindletrimmingvalue", 0)
spindletrimmingvalue.set_writable()

# Read 轴实际速度
axisactualvalue = Param.add_variable(addspace, "axisactualvalue", 0.0)
axisactualvalue.set_writable()

# Read 轴进给实际倍率
actualfeedrate = Param.add_variable(addspace, "actualfeedrate", 0.0)
actualfeedrate.set_writable()

# Read 绝对坐标编程值 for 轴1 to 轴9
xaxismachinetoolcoordinatetheoryvalue = Param.add_variable(addspace, "xaxismachinetoolcoordinatetheoryvalue", 0.0)
xaxismachinetoolcoordinatetheoryvalue.set_writable()

yaxismachinetoolcoordinatetheoryvalue = Param.add_variable(addspace, "yaxismachinetoolcoordinatetheoryvalue", 0.0)
yaxismachinetoolcoordinatetheoryvalue.set_writable()

zaxismachinetoolcoordinatetheoryvalue = Param.add_variable(addspace, "zaxismachinetoolcoordinatetheoryvalue", 0.0)
zaxismachinetoolcoordinatetheoryvalue.set_writable()

aaxismachinetoolcoordinatetheoryvalue = Param.add_variable(addspace, "aaxismachinetoolcoordinatetheoryvalue", 0.0)
aaxismachinetoolcoordinatetheoryvalue.set_writable()

baxismachinetoolcoordinatetheoryvalue = Param.add_variable(addspace, "baxismachinetoolcoordinatetheoryvalue", 0.0)
baxismachinetoolcoordinatetheoryvalue.set_writable()

caxismachinetoolcoordinatetheoryvalue = Param.add_variable(addspace, "caxismachinetoolcoordinatetheoryvalue", 0.0)
caxismachinetoolcoordinatetheoryvalue.set_writable()

uaxismachinetoolcoordinatetheoryvalue = Param.add_variable(addspace, "uaxismachinetoolcoordinatetheoryvalue", 0.0)
uaxismachinetoolcoordinatetheoryvalue.set_writable()

vaxismachinetoolcoordinatetheoryvalue = Param.add_variable(addspace, "vaxismachinetoolcoordinatetheoryvalue", 0.0)
vaxismachinetoolcoordinatetheoryvalue.set_writable()

waxismachinetoolcoordinatetheoryvalue = Param.add_variable(addspace, "waxismachinetoolcoordinatetheoryvalue", 0.0)
waxismachinetoolcoordinatetheoryvalue.set_writable()

# Read 工作模式
CNCMode = Param.add_variable(addspace, "CNCMode", 0)
CNCMode.set_writable()

# Read 工作状态
CNCState = Param.add_variable(addspace, "CNCState", 0)
CNCState.set_writable()

# Read x_电压(x方向振动)
x_voltage = Param.add_variable(addspace, "x_voltage", 0.0)
x_voltage.set_writable()

# Read y_电压(y方向振动)
y_voltage = Param.add_variable(addspace, "y_voltage", 0.0)
y_voltage.set_writable()

# Read z_电压(z方向振动)
z_voltage = Param.add_variable(addspace, "z_voltage", 0.0)
z_voltage.set_writable()

server.start()

print(f"Server started at {url}")

while True:
    # 在此处可以设置不同变量的值，例如：CNCChannels.set_value("New Value")
    time.sleep(1)
