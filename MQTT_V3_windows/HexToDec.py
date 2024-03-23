
if __name__ == '__main__':

    # 将提供的十六进制数据转换为十进制数据
    hex_data = """
    c610 42a8 5157 3e40 2f36 97c8 8f2a 23c0 5b0a 4633 887d 5840 fa29 0181 6ea7 52c0 1d41 a2e9 bd66 7140 00a0 0000 9422 b62a ffff ffff ffff ff7f 0a00 0000 ffff ffff ffff ff7f 0a00 0000 0000 0000 ffff ffff ffff ff7f 401f 867e ffff ffff 782d b62a 0000 0000 3300 0000 a91d 867e 0000 0000 0a00 0000 b401 b62a 001d 867e b8f9 da2b 0700 0000 0000 0000 0000 0000 a81d 867e cccc cccc cccc cc0c 0a00 0000 0000 0000 00c0 472c 581d 867e 0000 0000 00c0 472c 0a00 0000 e884 bb2a 00c0 472c 2100 0000 0500 0000 0a00 0000 b81f 867e 40cd 1b01 1800 0000 48d2 472c 48cd 1b01 2800 0000 48d2 472c a0a3 7800 1800 0000 8c16 3c2c 2800 0000 0000 0000 c084 bb2a 48cd 1b01
    """

    # 移除空格和换行符，以便进行转换
    clean_hex_data = hex_data.replace(" ", "").replace("\n", "")

    # 分割字符串为16进制数的列表
    hex_list = [clean_hex_data[i:i+2] for i in range(0, len(clean_hex_data), 2)]

    # 将16进制数转换为10进制数
    dec_list = [int(h, 16) for h in hex_list]

    print(dec_list)
