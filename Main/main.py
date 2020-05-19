from Main.read_file import *
from steps.steps import *
import re

def get_test_data(file_test,file_steps):
    test_datas = read_data(file_test)
    print(test_datas)
    steps = read_steps(file_steps)
    print(steps)
    command = None
    flag = True
    for test_data in test_datas:
        test_data = eval(test_data)
        for step in steps:
            if "{{" in step:
                # 获取key
                key = re.search(r"{{(.*?)}}", step).group(1)
                # 获取到key，把测试步骤进行再次拼接，把测试数据放进去
                step = re.sub(r"{{%s}}" % key, test_data[key], step)
            if step.count("||") == 0:
                command = step + "()"
            elif step.count("||") == 1:
                funcname, value = step.split("||")
                command = "%s(%s)" % (funcname, value)
                xpath_exc = None
            elif step.count("||") == 2:
                funcname, xpath_exc, value = step.split("||")
                command = "%s(%s,%s)" % (funcname, xpath_exc, value)
            else:
                print("数据读取异常，请检查！")
            try:
                eval(command)
            except Exception as e:
                print("每个测试步骤执行失败,原因是:%s" % e)
                flag = False
            else:
                print("每个测试步骤执行成功！")
        if flag == False:
            print("所有测试步骤执行失败！")
        else:
            print("所有测试步骤执行成功！")