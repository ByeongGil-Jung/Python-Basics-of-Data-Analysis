"""
 Created by IntelliJ IDEA.
 Project: source
 ===========================================
 User: ByeongGil Jung
 Date: 2018-07-08
 Time: 오후 5:47
"""


class DtoPC(object):

    def __init__(self, model, speed, ram, hd, cd, price):
        self.model = model
        self.speed = speed
        self.ram = ram
        self.hd = hd
        self.cd = cd
        self.price = price

    def __str__(self):
        return "{}".format(self.model)
