# coding:utf-8
import requests
import json

requests.adapters.DEFAULT_RETRIES = 5
s = requests.session
s.keep_alive=False


class RunMethod:
    def post_main(self, url, data, header=None):
        if header is not None:
            res = requests.post(url=url, data=data, header=header, verify=False).json()
        else:
            res = requests.post(url=url, data=data, verify=False).json()
        return res



    def get_main(self, url, params=None, header=None):
        if header is not None:
            res = requests.get(url=url, params=params, header=header, verify=False).json()
        else:
            res = requests.get(url=url, params=params, verify=False).json()
        return res



    def run_main(self, method, url, data=None, header=None):
        if method == "GET":
            res = self.get_main(url, data, header)
        else:
            res = self.post_main(url, data, header)
        return json.dumps(res)
