#coding:utf-8
from commo.get_data import GetData
from commo.runmethod import RunMethod
from pprint import pprint
import urllib3
from commo.compare import Compare
import json

urllib3.disable_warnings()


class RunCase:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.compare = Compare()


    def go_on_run(self):
        row_count = self.data.get_caselines()
        for i in range(1, row_count):
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_json(i)
            header = self.data.get_is_header(i)
            expect = self.data.get_expect(i)
            if is_run:
                res = self.run_method.run_main(method, url, data, header)
                print(type(res))
                if self.compare.is_contain(expect, res):
                    print("测试通过")
                else:
                    print("测试失败")
                # return res
                pprint(res)



if __name__ == "__main__":
    run =RunCase().go_on_run()
    # pprint(run)
