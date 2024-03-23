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

    # 为每个变量手动指定并添加NodeID
    axisresidual = Param.add_variable(ua.NodeId(1001, addspace), "axisresidual", 0.0)
    axisresidual.set_writable()

    spindleprogrammingpos = Param.add_variable(ua.NodeId(1002, addspace), "spindleprogrammingspeed", 0.0)
    spindleprogrammingpos.set_writable()

    actualspindlevelocity = Param.add_variable(ua.NodeId(1003, addspace), "actualspindlevelocity", 0.0)
    actualspindlevelocity.set_writable()

    spindletrimmingvalue = Param.add_variable(ua.NodeId(1004, addspace), "spindletrimmingvalue", 0)
    spindletrimmingvalue.set_writable()

    axisactualvalue = Param.add_variable(ua.NodeId(1005, addspace), "axisactualvalue", 0.0)
    axisactualvalue.set_writable()

    actualfeedrate = Param.add_variable(ua.NodeId(1006, addspace), "actualfeedrate", 0.0)
    actualfeedrate.set_writable()

    xaxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(1007, addspace), "xaxismachinetoolcoordinatetheoryvalue", 0.0)
    xaxismachinetoolcoordinatetheoryvalue.set_writable()

    yaxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(1008, addspace), "yaxismachinetoolcoordinatetheoryvalue", 0.0)
    yaxismachinetoolcoordinatetheoryvalue.set_writable()

    zaxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(1009, addspace), "zaxismachinetoolcoordinatetheoryvalue", 0.0)
    zaxismachinetoolcoordinatetheoryvalue.set_writable()

    aaxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(1010, addspace), "aaxismachinetoolcoordinatetheoryvalue", 0.0)
    aaxismachinetoolcoordinatetheoryvalue.set_writable()

    baxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(1011, addspace), "baxismachinetoolcoordinatetheoryvalue", 0.0)
    baxismachinetoolcoordinatetheoryvalue.set_writable()

    caxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(1012, addspace), "caxismachinetoolcoordinatetheoryvalue", 0.0)
    caxismachinetoolcoordinatetheoryvalue.set_writable()

    uaxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(1013, addspace), "uaxismachinetoolcoordinatetheoryvalue", 0.0)
    uaxismachinetoolcoordinatetheoryvalue.set_writable()

    vaxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(1014, addspace), "vaxismachinetoolcoordinatetheoryvalue", 0.0)
    vaxismachinetoolcoordinatetheoryvalue.set_writable()

    waxismachinetoolcoordinatetheoryvalue = Param.add_variable(ua.NodeId(1015, addspace), "waxismachinetoolcoordinatetheoryvalue", 0.0)
    waxismachinetoolcoordinatetheoryvalue.set_writable()

    CNCMode = Param.add_variable(ua.NodeId(1016, addspace), "CNCMode", 0)
    CNCMode.set_writable()

    CNCState = Param.add_variable(ua.NodeId(1017, addspace), "CNCState", 0)
    CNCState.set_writable()

    x_voltage = Param.add_variable(ua.NodeId(1018, addspace), "x_voltage", 0.0)
    x_voltage.set_writable()

    y_voltage = Param.add_variable(ua.NodeId(1019, addspace), "y_voltage", 0.0)
    y_voltage.set_writable()

    z_voltage = Param.add_variable(ua.NodeId(1020, addspace), "z_voltage", 0.0)
    z_voltage.set_writable()

    server.start()
    print(f"Server started at {url}")

    try:
        while True:
            time.sleep(1)
            # 在此处可以设置不同变量的值，例如：axisresidual.set_value(新的值)
    except KeyboardInterrupt:
        print("Server is shutting down.")
        server.stop()

