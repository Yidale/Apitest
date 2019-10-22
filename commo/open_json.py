#coding:utf-8
import json
# fp = open("../Testdata/case_data.json")
# # json文件里数据必须双引号，否则转换可能出错
# data = json.load(fp)
# print(type(data["xnapi"]))


class OperationJson:
    def __init__(self):
        self.data = self.read_json()


    # 获取json
    def read_json(self):
        with open("../Testdata/case_data.json") as fp:
            data = json.load(fp)
            return data

    # 获取json数据
    def get_data(self, key=None):
        data = self.data[key]
        return data

if __name__ == "__main__":
    aa = OperationJson().get_data("account")
    print(aa)