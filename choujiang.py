import tornado.ioloop
import tornado.web
import random


def get_num(ns):  # 判断获取str是否为空，为空返回0
    if ns == "":
        return 0
    else:
        return int(ns)


def random_cj(fir, sec, thi, li):  # 抽奖函数
    li = list(set(li))  # 去重
    fl = random.sample(li, fir)
    for i in fl:
        li.remove(i)
    sl = random.sample(li, sec)
    for i in sl:
        li.remove(i)
    tl = random.sample(li, thi)
    print(fl, sl, tl)
    return fl, sl, tl


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("web.html")

    def post(self):
        firNum = get_num(self.get_argument("firNum"))  # 一等奖数量
        secNum = get_num(self.get_argument("secNum"))  # 二等奖数量
        thiNum = get_num(self.get_argument("thiNum"))  # 三等奖数量
        memlist = self.get_argument("md").split("\r\n")
        # print(memlist)
        fl, sl, tl = random_cj(firNum, secNum, thiNum, memlist)
        self.render("result.html", fi_num=",".join(list(fl)),
                    se_num=",".join(list(sl)), th_num=",".join(list(tl)))


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
