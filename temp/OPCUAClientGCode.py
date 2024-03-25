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
        # 获取所有的前后行的OPC UA节点
        lines_before = [opcua_client.get_node(f"ns=2;i={9000 + i}") for i in range(10)]
        lines_after = [opcua_client.get_node(f"ns=2;i={9011 + i}") for i in range(10)]

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

            # 构造文件路径
            file_path = os.path.join(gcode_dir, program_file_name)

            try:
                with open(file_path, 'r') as file:
                    lines = file.readlines()

                    # 更新前10行
                    for i in range(1, 11):
                        line_num = current_line - i
                        line_content = lines[line_num - 1].strip() if 1 <= line_num else ""
                        lines_before[10 - i].set_value(line_content)

                    # 更新当前行的G代码
                    current_gcode = lines[current_line - 1].strip() if 1 <= current_line <= len(lines) else ""
                    Line.set_value(current_gcode)
                    print(f"Updated GCode to OPC UA: {current_gcode}")

                    # 更新后10行
                    for i in range(1, 11):
                        line_num = current_line + i
                        line_content = lines[line_num - 1].strip() if line_num <= len(lines) else ""
                        lines_after[i - 1].set_value(line_content)

                    # # 更新前10行
                    # for i in range(10):
                    #     line_num = current_line - 10 + i
                    #     line_content = lines[line_num].strip() if 1 <= line_num < current_line else ""
                    #     lines_before[i].set_value(line_content)
                    #
                    # # 更新后10行
                    # for i in range(10):
                    #     line_num = current_line + i
                    #     line_content = lines[line_num].strip() if current_line < line_num <= len(lines) else ""
                    #     lines_after[i].set_value(line_content)
                    #
                    # if 1 <= current_line <= len(lines):
                    #     # 获取当前行的G代码并去除空白符
                    #     current_gcode = lines[current_line - 1].strip()
                    #     # 将当前行的G代码写入OPC UA节点
                    #     Line.set_value(current_gcode)
                    #     print(f"Updated GCode to OPC UA: {current_gcode}")
                    # else:
                    #     print(f"Current line {current_line} is out of range for the file.")
            except FileNotFoundError:
                print(f"文件 {program_file_name} 未找到。")
            except Exception as e:
                print(f"读取文件时发生错误：{e}")

            # 设置轮询间隔
            time.sleep(1)

    finally:
        opcua_client.disconnect()
