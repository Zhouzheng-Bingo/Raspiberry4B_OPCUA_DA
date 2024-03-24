import os
import re

from opcua import Client
import time

global file_name

if __name__ == '__main__':

    opcua_url = "opc.tcp://localhost:48020/"
    opcua_client = Client(opcua_url)

    try:
        opcua_client.connect()

        # 这些节点是存在的，并且能正确获取值
        current_line_node = opcua_client.get_node("ns=2;i=8465")
        program_file_name_node = opcua_client.get_node("ns=2;i=8467")
        Line = opcua_client.get_node("ns=2;i=9010")  # XXXX 替换为实际节点ID

        gcode_dir = "GCode"

        while True:
            # 读取当前行号和程序名
            current_line = current_line_node.get_value()
            program_file_name = program_file_name_node.get_value()

            # 使用正则表达式提取文件名
            match1 = re.search(r'[^\\/]+$', program_file_name)
            if match1:
                program_file_name = match1.group()
                print(program_file_name)
            # else:
            #     print("文件名未找到----")


            # 构造文件路径
            file_path = os.path.join(gcode_dir, program_file_name)

            try:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    if 1 <= current_line <= len(lines):
                        # 获取当前行的G代码并去除空白符
                        current_gcode = lines[current_line - 1].strip()
                        # 将当前行的G代码写入OPC UA节点
                        Line.set_value(current_gcode)
                        print(f"Updated GCode to OPC UA: {current_gcode}")
                    else:
                        print(f"Current line {current_line} is out of range for the file.")
            except FileNotFoundError:
                print(f"文件 {program_file_name} 未找到。")
            except Exception as e:
                print(f"读取文件时发生错误：{e}")

            # 设置轮询间隔
            time.sleep(1)

    finally:
        opcua_client.disconnect()
