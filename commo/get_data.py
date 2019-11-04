#coding:utf-8
from commo.open_excel import OperationExcel
from commo.open_json import OperationJson
from constant import constant_var


class GetData:
    def __init__(self):
        self.op_excel = OperationExcel()

    # 获取Excel行数，也就是case个数
    def get_caselines(self):
        return self.op_excel.get_lines()


    # 获取是否运行
    def get_is_run(self, hang):
        lie = constant_var.get_run()
        run_model = self.op_excel.get_value(hang, lie)
        if run_model == "yes":
            return True
        else:
            return False


    # 是否携带请求头
    def get_is_header(self, hang):
        lie = constant_var.get_header()
        header = self.op_excel.get_value(hang, lie)
        if header == "yes":
            return constant_var.head_value()
        else:
            return None


    # 获取请求方式
    def get_request_method(self, hang):
        lie = constant_var.get_request_way()
        method = self.op_excel.get_value(hang, lie)
        return method


    # 获取URL
    def get_request_url(self, hang):
        lie = constant_var.get_url()
        url = self.op_excel.get_value(hang, lie)
        return url


    # 获取请求数据
    def get_request_data(self, hang):
        lie = constant_var.request_val()
        data = self.op_excel.get_value(hang, lie)
        if data == ' ':
            return None
        else:
            return data


    # 通过关键字获得json里的数据
    def get_data_json(self, hang):
        op_json = OperationJson()
        requset_data = op_json.get_data(self.get_request_data(hang))
        return requset_data


    # 获取预期结果
    def get_expect(self, hang):
        lie = constant_var.expect()
        exp = self.op_excel.get_value(hang, lie)
        if exp == "":
            return None
        else:
            return exp


    def weite_result(self, hang, value):
        lie = constant_var.result()
        self.op_excel.wite_value(hang, lie, value)

