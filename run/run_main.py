from Main.main import *

def search_test(file_test,file_step):
    get_test_data(file_test,file_step)

def login_test(file_test,file_step):
    get_test_data(file_test,file_step)


search_test("../data/data.txt","../data/test_data.txt")
login_test("../data/logi_data.txt","../data/login_step.txt")
