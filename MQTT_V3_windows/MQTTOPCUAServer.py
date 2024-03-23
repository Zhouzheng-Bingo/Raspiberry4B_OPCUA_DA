from opcua import Server, ua
import time


if __name__ == '__main__':

    server = Server()

    url = "opc.tcp://192.168.162.82:4840"
    server.set_endpoint(url)

    name = "OPCUA_SIMULATION_SERVER"
    addspace = server.register_namespace(name)

    node = server.get_objects_node()

    Param = node.add_object(addspace, "Parameters")

    # 创建变量并设置NodeID以及数据类型

    # Read 剩余量（轴1-9偏移+4）
    axisresidual = Param.add_variable(ua.NodeId(1024, addspace), "axisresidual", 0.0)
    axisresidual.set_writable()

    # Read 主轴编程位置
    spindleprogrammingpos = Param.add_variable(ua.NodeId(1025, addspace), "spindleprogrammingspeed", 0.0)
    spindleprogrammingpos.set_writable()

    # Read 主轴速度实际值
    actualspindlevelocity = Param.add_variable(ua.NodeId(1026, addspace), "actualspindlevelocity", 0.0)
    actualspindlevelocity.set_writable()

    # Read 主轴修调
    spindletrimmingvalue = Param.add_variable(ua.NodeId(1027, addspace), "spindletrimmingvalue", 0)
    spindletrimmingvalue.set_writable()

    # Read 轴实际速度
    axisactualvalue = Param.add_variable(ua.NodeId(1028, addspace), "axisactualvalue", 0.0)
    axisactualvalue.set_writable()

    # Read 轴进给实际倍率
    actualfeedrate = Param.add_variable(ua.NodeId(8494, addspace), "actualfeedrate", 0.0)
    actualfeedrate.set_writable()

    # Read 实际坐标编程值 for 轴1 to 轴9
    xaxismachinetoolcoordinateactualvalue = Param.add_variable(ua.NodeId(1001, addspace), "xaxismachinetoolcoordinateactualvalue", 0.0)
    xaxismachinetoolcoordinateactualvalue.set_writable()

    yaxismachinetoolcoordinateactualvalue = Param.add_variable(ua.NodeId(1002, addspace), "yaxismachinetoolcoordinateactualvalue", 0.0)
    yaxismachinetoolcoordinateactualvalue.set_writable()

    zaxismachinetoolcoordinateactualvalue = Param.add_variable(ua.NodeId(1003, addspace), "zaxismachinetoolcoordinateactualvalue", 0.0)
    zaxismachinetoolcoordinateactualvalue.set_writable()

    aaxismachinetoolcoordinateactualvalue = Param.add_variable(ua.NodeId(1004, addspace), "aaxismachinetoolcoordinateactualvalue", 0.0)
    aaxismachinetoolcoordinateactualvalue.set_writable()

    baxismachinetoolcoordinateactualvalue = Param.add_variable(ua.NodeId(1005, addspace), "baxismachinetoolcoordinateactualvalue", 0.0)
    baxismachinetoolcoordinateactualvalue.set_writable()

    caxismachinetoolcoordinateactualvalue = Param.add_variable(ua.NodeId(1006, addspace), "caxismachinetoolcoordinateactualvalue", 0.0)
    caxismachinetoolcoordinateactualvalue.set_writable()

    uaxismachinetoolcoordinateactualvalue = Param.add_variable(ua.NodeId(1007, addspace), "uaxismachinetoolcoordinateactualvalue", 0.0)
    uaxismachinetoolcoordinateactualvalue.set_writable()

    vaxismachinetoolcoordinateactualvalue = Param.add_variable(ua.NodeId(1008, addspace), "vaxismachinetoolcoordinateactualvalue", 0.0)
    vaxismachinetoolcoordinateactualvalue.set_writable()

    waxismachinetoolcoordinateactualvalue = Param.add_variable(ua.NodeId(1009, addspace), "waxismachinetoolcoordinateactualvalue", 0.0)
    waxismachinetoolcoordinateactualvalue.set_writable()

    # Read 绝对坐标编程值 for 轴1 to 轴9
    xaxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(8460, addspace), "xaxismachinetoolcoordinatetheoryvalue", 0.0)
    xaxismachinetoolcoordinatetheoryvalue.set_writable()

    yaxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(8461, addspace), "yaxismachinetoolcoordinatetheoryvalue", 0.0)
    yaxismachinetoolcoordinatetheoryvalue.set_writable()

    zaxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(8462, addspace), "zaxismachinetoolcoordinatetheoryvalue", 0.0)
    zaxismachinetoolcoordinatetheoryvalue.set_writable()

    aaxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(8463, addspace), "aaxismachinetoolcoordinatetheoryvalue", 0.0)
    aaxismachinetoolcoordinatetheoryvalue.set_writable()

    baxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(8001, addspace), "baxismachinetoolcoordinatetheoryvalue", 0.0)
    baxismachinetoolcoordinatetheoryvalue.set_writable()

    caxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(8464, addspace), "caxismachinetoolcoordinatetheoryvalue", 0.0)
    caxismachinetoolcoordinatetheoryvalue.set_writable()

    uaxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(8002, addspace), "uaxismachinetoolcoordinatetheoryvalue", 0.0)
    uaxismachinetoolcoordinatetheoryvalue.set_writable()

    vaxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(8003, addspace), "vaxismachinetoolcoordinatetheoryvalue", 0.0)
    vaxismachinetoolcoordinatetheoryvalue.set_writable()

    waxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(8004, addspace), "waxismachinetoolcoordinatetheoryvalue", 0.0)
    waxismachinetoolcoordinatetheoryvalue.set_writable()

    # Read 工作模式
    CNCMode = Param.add_variable(ua.NodeId(1019, addspace), "CNCMode", 0)
    CNCMode.set_writable()

    # Read 工作状态
    CNCState = Param.add_variable(ua.NodeId(1020, addspace), "CNCState", 0)
    CNCState.set_writable()

    # Read x_电压(x方向振动)
    x_voltage = Param.add_variable(ua.NodeId(1021, addspace), "x_voltage", 0.0)
    x_voltage.set_writable()

    # Read y_电压(y方向振动)
    y_voltage = Param.add_variable(ua.NodeId(1022, addspace), "y_voltage", 0.0)
    y_voltage.set_writable()

    # Read z_电压(z方向振动)
    z_voltage = Param.add_variable(ua.NodeId(1023, addspace), "z_voltage", 0.0)
    z_voltage.set_writable()

    server.start()

    print(f"Server started at {url}")

    while True:
        # 在此处可以设置不同变量的值，例如：CNCChannels.set_value("New Value")
        time.sleep(1)
