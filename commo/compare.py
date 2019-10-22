# coding:utf-8:


class Compare:
    def is_contain(self, str_one, str_two):
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag



counter = 1
def doLotsOfStuff():
    global counter
    for i in (1, 2, 3):
        counter += 1
doLotsOfStuff()
print (counter)