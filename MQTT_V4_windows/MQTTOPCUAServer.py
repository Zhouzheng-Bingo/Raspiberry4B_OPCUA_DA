from opcua import Server, ua
import time
import os

if __name__ == '__main__':

    server = Server()

    url = "opc.tcp://localhost:48020/"
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
    xaxismachinetoolcoordinateactualvalue = Param.add_variable(ua.NodeId(8472, addspace), "xaxismachinetoolcoordinateactualvalue", 0.0)
    xaxismachinetoolcoordinateactualvalue.set_writable()

    yaxismachinetoolcoordinateactualvalue = Param.add_variable(ua.NodeId(8473, addspace), "yaxismachinetoolcoordinateactualvalue", 0.0)
    yaxismachinetoolcoordinateactualvalue.set_writable()

    zaxismachinetoolcoordinateactualvalue = Param.add_variable(ua.NodeId(8474, addspace), "zaxismachinetoolcoordinateactualvalue", 0.0)
    zaxismachinetoolcoordinateactualvalue.set_writable()

    aaxismachinetoolcoordinateactualvalue = Param.add_variable(ua.NodeId(8475, addspace), "aaxismachinetoolcoordinateactualvalue", 0.0)
    aaxismachinetoolcoordinateactualvalue.set_writable()

    baxismachinetoolcoordinateactualvalue = Param.add_variable(ua.NodeId(1005, addspace), "baxismachinetoolcoordinateactualvalue", 0.0)
    baxismachinetoolcoordinateactualvalue.set_writable()

    caxismachinetoolcoordinateactualvalue = Param.add_variable(ua.NodeId(8476, addspace), "caxismachinetoolcoordinateactualvalue", 0.0)
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

    # Read 当前行号
    CurrentLine = Param.add_variable(ua.NodeId(8465, addspace), "CurrentLine", 0)
    CurrentLine.set_writable()



    #预读21行G代码

    # LineBefore10 = Param.add_variable(ua.NodeId(9000, addspace), "(n-10)th G code", "", ua.VariantType.String)
    # LineBefore10.set_writable()
    #
    # LineBefore9 = Param.add_variable(ua.NodeId(9001, addspace), "(n-9)th G code", "", ua.VariantType.String)
    # LineBefore9.set_writable()
    #
    # LineBefore8 = Param.add_variable(ua.NodeId(9002, addspace), "(n-8)th G code", "", ua.VariantType.String)
    # LineBefore8.set_writable()
    #
    # LineBefore7 = Param.add_variable(ua.NodeId(9003, addspace), "(n-7)th G code", "", ua.VariantType.String)
    # LineBefore7.set_writable()
    #
    # LineBefore6 = Param.add_variable(ua.NodeId(9004, addspace), "(n-6)th G code", "", ua.VariantType.String)
    # LineBefore6.set_writable()
    #
    # LineBefore5 = Param.add_variable(ua.NodeId(9005, addspace), "(n-5)th G code", "", ua.VariantType.String)
    # LineBefore5.set_writable()
    #
    # LineBefore4 = Param.add_variable(ua.NodeId(9006, addspace), "(n-4)th G code", "", ua.VariantType.String)
    # LineBefore4.set_writable()
    #
    # LineBefore3 = Param.add_variable(ua.NodeId(9007, addspace), "(n-3)th G code", "", ua.VariantType.String)
    # LineBefore3.set_writable()
    #
    LineBefore2 = Param.add_variable(ua.NodeId(9000, addspace), "(n-2)th G code", "", ua.VariantType.String)
    LineBefore2.set_writable()

    LineBefore1 = Param.add_variable(ua.NodeId(9001, addspace), "(n-1)th G code", "", ua.VariantType.String)
    LineBefore1.set_writable()

    Line = Param.add_variable(ua.NodeId(9002, addspace), "(n)th G code", "", ua.VariantType.String)
    Line.set_writable()

    LineAfter1 = Param.add_variable(ua.NodeId(9003, addspace), "(n+1)th G code", "", ua.VariantType.String)
    LineAfter1.set_writable()

    LineAfter2 = Param.add_variable(ua.NodeId(9004, addspace), "(n+2)th G code", "", ua.VariantType.String)
    LineAfter2.set_writable()

    LineAfter3 = Param.add_variable(ua.NodeId(9005, addspace), "(n+3)th G code", "", ua.VariantType.String)
    LineAfter3.set_writable()

    LineAfter4 = Param.add_variable(ua.NodeId(9006, addspace), "(n+4)th G code", "", ua.VariantType.String)
    LineAfter4.set_writable()

    LineAfter5 = Param.add_variable(ua.NodeId(9007, addspace), "(n+5)th G code", "", ua.VariantType.String)
    LineAfter5.set_writable()

    LineAfter6 = Param.add_variable(ua.NodeId(9008, addspace), "(n+6)th G code", "", ua.VariantType.String)
    LineAfter6.set_writable()

    LineAfter7 = Param.add_variable(ua.NodeId(9009, addspace), "(n+7)th G code", "", ua.VariantType.String)
    LineAfter7.set_writable()

    LineAfter8 = Param.add_variable(ua.NodeId(9010, addspace), "(n+8)th G code", "", ua.VariantType.String)
    LineAfter8.set_writable()

    LineAfter9 = Param.add_variable(ua.NodeId(9011, addspace), "(n+9)th G code", "", ua.VariantType.String)
    LineAfter9.set_writable()

    LineAfter10 = Param.add_variable(ua.NodeId(9012, addspace), "(n+10)th G code", "", ua.VariantType.String)
    LineAfter10.set_writable()

    LineAfter11 = Param.add_variable(ua.NodeId(9013, addspace), "(n+11)th G code", "", ua.VariantType.String)
    LineAfter11.set_writable()

    LineAfter12 = Param.add_variable(ua.NodeId(9014, addspace), "(n+12)th G code", "", ua.VariantType.String)
    LineAfter12.set_writable()

    LineAfter13 = Param.add_variable(ua.NodeId(9015, addspace), "(n+13)th G code", "", ua.VariantType.String)
    LineAfter13.set_writable()

    LineAfter14 = Param.add_variable(ua.NodeId(9016, addspace), "(n+14)th G code", "", ua.VariantType.String)
    LineAfter14.set_writable()

    LineAfter15 = Param.add_variable(ua.NodeId(9017, addspace), "(n+15)th G code", "", ua.VariantType.String)
    LineAfter15.set_writable()

    LineAfter16 = Param.add_variable(ua.NodeId(9018, addspace), "(n+16)th G code", "", ua.VariantType.String)
    LineAfter16.set_writable()

    LineAfter17 = Param.add_variable(ua.NodeId(9019, addspace), "(n+17)th G code", "", ua.VariantType.String)
    LineAfter17.set_writable()

    LineAfter18 = Param.add_variable(ua.NodeId(9020, addspace), "(n+18)th G code", "", ua.VariantType.String)
    LineAfter18.set_writable()

    # Read 是否单步执行
    IsSingleStepExecutionMode = Param.add_variable(ua.NodeId(8466, addspace), "IsSingleStepExecutionMode", 0)
    IsSingleStepExecutionMode.set_writable()

    # 创建程序名节点
    ProgramFileName = Param.add_variable(ua.NodeId(8467, addspace), "ProgramFileName", "", ua.VariantType.String)
    ProgramFileName.set_writable()

    # Read x_电压(x方向振动)
    x_voltage = Param.add_variable(ua.NodeId(1021, addspace), "x_voltage", 0.0)
    x_voltage.set_writable()

    # Read y_电压(y方向振动)
    y_voltage = Param.add_variable(ua.NodeId(1022, addspace), "y_voltage", 0.0)
    y_voltage.set_writable()

    # Read z_电压(z方向振动)
    z_voltage = Param.add_variable(ua.NodeId(1023, addspace), "z_voltage", 0.0)
    z_voltage.set_writable()

    # Read 当前急停状态
    CurrentEmergencyStopStatus = Param.add_variable(ua.NodeId(8468, addspace), "CurrentEmergencyStopStatus", 0)
    CurrentEmergencyStopStatus.set_writable()

    # Read 当前进给倍率
    CurrentFeedRateRatio = Param.add_variable(ua.NodeId(8469, addspace), "CurrentFeedRateRatio", 0.0)
    CurrentFeedRateRatio.set_writable()

    # Read 当前快速进给
    CurrentRapidFeed = Param.add_variable(ua.NodeId(8470, addspace), "CurrentRapidFeed", 0.0)
    CurrentRapidFeed.set_writable()

    # Read 当前主轴倍率
    CurrentSpindleSpeedRatio = Param.add_variable(ua.NodeId(8471, addspace), "CurrentSpindleSpeedRatio", 0.0)
    CurrentSpindleSpeedRatio.set_writable()

    server.start()

    print(f"Server started at {url}")

    while True:
        # 在此处可以设置不同变量的值，例如：CNCChannels.set_value("New Value")
        time.sleep(1)
