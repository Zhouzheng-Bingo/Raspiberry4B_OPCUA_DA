from opcua import Server, ua
import time

if __name__ == '__main__':

    server = Server()
    url = "opc.tcp://localhost:4840/freeopcua/server/"
    server.set_endpoint(url)

    # 注册命名空间
    namespace_index = server.register_namespace("OPCUA_SIMULATION_SERVER")

    # 获取Objects节点，这是所有自定义节点的父节点
    objects_node = server.get_objects_node()

    # 使用UA_NODEID_NUMERIC创建一个具体NodeID的变量
    node_id = ua.NodeId(2, 100)  # 第一个参数是节点的数值ID，第二个参数是命名空间的索引
    # var = ua.Variant("Hello World!", ua.VariantType.String)

    # 创建一个新的变量节点，指定NodeID，名称和初始值
    my_var = objects_node.add_variable(node_id, "axisresidual", 10.0)
    my_var.set_writable()  # 使变量可写

    server.start()

    print("Server started at {}".format(url))
