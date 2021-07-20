# @Project: SCB22
# @Auth ： 柠檬班-土豆
# @Time ： 2021/7/16 15:16
# @E-mail ：121313927@qq.com
# @Company：湖南省零檬信息技术有限公司
# @Site: http://www.lemonban.com
# @Forum: http://testingpai.com


from api.common.method import read_case,api_fun,write_result

# 完整的接口自动化测试
def execute_fun(filename,sheetname):
    cases = read_case(filename,sheetname)   # 定义变量，接收获取测试用例数据
    for case in cases:
        case_id = case['case_id']   # 获取用例id
        url = case['url']    # 获取url
        data = eval(case['data'])  # 获取data
        expect = eval(case['expect']) # 获取期望

        # 获取期望code、msg
        expect_code = expect['code']
        expect_msg = expect['msg']
        print("预期结果：code为{}，msg为{}".format(expect_code,expect_msg))

        # 调用接口
        real_result =  api_fun(url=url,data=data)
        # 获取实际的code，msg
        real_code = real_result['code']
        real_msg = real_result['msg']
        print("实际结果：code为{}，msg为{}".format(real_code,real_msg))

        # 断言
        if expect_code==real_code and expect_msg== real_msg:
            print("第{}条测试用例执行通过！".format(case_id))
            final_re = 'Passed'
        else:
            print("第{}条测试用例执行不通过！".format(case_id))
            final_re = 'Failed'
        print("*"*20)

        # 写入最终的测试结果到excel
        write_result(filename,sheetname,case_id+1,8,final_re)


# 调用excute_fun 对login接口自动化测试
execute_fun("D:\Pycharm_workspace\SCB22\\api\\test_data\\testcase_api_wuye.xlsx", "login")  # 代码分层结构，测试用例xlsx获取写绝对路径