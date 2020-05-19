import os


def read_steps(file_path):
    # 判断文件是否存在
    if not (os.path.exists(file_path)):
        print("测试步骤文件不存在，请检查")
        exit()
    print("开始读取测试步骤内容")
    with open(file_path, encoding="utf-8") as pf:
        test_steps = []
        for line in pf:
            test_steps.append(line.strip())
    print("返回数据列表")
    return test_steps

def read_data(file_path):
    if not os.path.exists(file_path):
        print("测试文件不存在，请重新检查！")
        exit()
    print("开始读取测试数据文件内容")
    with open(file_path, encoding='utf-8') as fp:
        datalist = []
        for line in fp:
            datalist.append(line.strip())
    return datalist

