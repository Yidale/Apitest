import requests
import json
from pprint import pprint


class RunMain:
    #
    # def __init__(self, method, url, data=None):
    #     self.res = self.runmain(method, url, data)

    def send_post(self, url, data):
        res = requests.post(url=url, data=data, verify=False).json()
        # return json.dumps(res, indent=2, sort_keys=True)
        return res

    def send_get(self, url, data=None):
        res = requests.get(url=url, params=data, verify=False).json()
        return res


    def runmain(self, method, url, data =None):
        res = None
        if method == "GET":
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == "__main__":
    url = "https://testapi.51nbapi.com/mfabric/cspadve/adve/h5/queryMultipleBannerList.json"
    data = {
        'channelCode': 'WECHAT_PLATFORM',
        'multipleBannerSceneCodeList': 'CARD_SUPERMARKET_INDEX_FLOAT'
    }
    aa = RunMain().runmain("GET",url,data)
    pprint(aa)