#coding:utf-8
import unittest
from pprint import pprint
from Imoocdemo.demo import RunMain
import HTMLTestRunner


class TestMethod(unittest.TestCase):
    # 类方法，类执行前的方法
    @classmethod
    def setUpClass(cls):
        print("类方法只执行一次——setup")

    @classmethod
    def tearDownClass(cls):
        print("类方法只执行一次——teardown")
    # 每次方法之前之前
    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = "https://testapi.51nbapi.com/mfabric/cspadve/adve/h5/queryMultipleBannerList.json"
        data = {
            'channelCode': 'WECHAT_PLATFORM',
            'multipleBannerSceneCodeList': 'CARD_SUPERMARKET_INDEX_FLOAT'
        }
        res1 = self.run.runmain("GET", url, data)
        globals()["userid"]=1000
        self.assertEqual(res1["result"]["status"], "success", "测试失败")
        print('----------第一条用例---------')

    # # 每次方法之后执行
    # def tearDown(self):
    #     print("test---->teardown")
    @unittest.skip('test_02')
    def test_02(self):
        print(userid)
        url = "https://testapi.51nbapi.com/mfabric/cspadve/adve/h5/queryMultipleBannerList.json"
        data = {
            'channelCode': '',
            'multipleBannerSceneCodeList': 'CARD_SUPERMARKET_INDEX_FLOAT'
        }
        res2 = self.run.runmain("GET", url, data)
        pprint(res2)


if __name__ == "__main__":
    # 设置用例路径，捞取用例
    casepath = 'E:\\PY\\Imooc\\Imoocdemo'
    suit = unittest.defaultTestLoader.discover(casepath, 'unittest*.py') #输入要运行的文件名称
    # 设置报告生成路径，生成报告
    filepath = "../report/htmlreport.html"
    fp = open(filepath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(fp, title="this is title")
    runner.run(suit)