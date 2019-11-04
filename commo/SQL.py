import pymysql

class UseSQL:
    def __init__(self):
        self.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='mysql',
            charset='utf8')
        self.cur = self.db.cursor(cursor= pymysql.cursors.DictCursor)

    def selectDB(self, sql):
        self.cur.execute(sql)
        res = self.cur.fetchone()
        return res

if __name__ == '__main__':
    op = UseSQL().selectDB("select user from user")
    print(type(op))
    print(op)