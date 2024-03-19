from opcua import Client
from opcua import ua

class SubHandler(object):
    """
    订阅处理器类用于处理服务器发送的数据变更通知。
    """

    def datachange_notification(self, node, val, data):
        print(f"Value changed for {node}: {val}")

    def event_notification(self, event):
        print(f"Event received: {event}")


if __name__ == "__main__":
    # 连接到服务器
    url = 'opc.tcp://localhost:4840/freeopcua/server/'  # 根据实际情况调整URL
    client = Client(url)

    try:
        client.connect()
        print("Client connected to the OPC UA server.")

        # 创建一个订阅对象
        handler = SubHandler()
        subscription = client.create_subscription(1000, handler)  # 1000ms更新一次

        # 获取想要订阅的节点
        node_id = "ns=100;i=2"  # 根据实际的命名空间索引和NodeID调整
        node = client.get_node(node_id)

        # 添加订阅
        subscription.subscribe_data_change(node)

        print(f"Subscribed to {node_id}, waiting for changes...")

        # 使主线程保持运行，以便持续接收变更通知
        try:
            while True:
                pass
        finally:
            # 如果中断（如通过Ctrl+C），则删除订阅并断开连接
            subscription.delete()
            client.disconnect()
            print("Client disconnected.")

    except Exception as e:
        print(f"Error: {e}")
        client.disconnect()
