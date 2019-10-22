#coding:utf-8
import xlrd
# 确定Excel位置并打开
# Excelpath ='../Testdata/excel_case.xlsx'
# data = xlrd.open_workbook(Excelpath)
# 选择Excel第一页sheet
# tables = data.sheets()[0]
# 打印Excel行数
# print(tables.nrows)
# 打印Excel第二行，第三列内容
# print(tables.cell_value(1,2))

class OperationExcel:
    def __init__(self, exc_path=None, sheet_id=0):
        if exc_path:
            self.exc_path = exc_path
            self.sheet_id = sheet_id
        else:
            self.exc_path = '../Testdata/excel_case.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheet内容
    def get_data(self):
        data = xlrd.open_workbook(self.exc_path)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 打印行数
    def get_lines(self):
        tab = self.data
        return tab.nrows

    # 选择某个单元
    def get_value(self, hang, lie):
        tab = self.data
        return tab.cell_value(hang, lie)


if __name__ == "__main__":
    aa = OperationExcel()
    print(aa.get_value(1, 2))