#!/usr/bin/python
# -*- encoding: utf-8 -*-
import random

wl = {(1, 1): "平手", (1, 2): "你赢了", (1, 3): "你输了", (2, 1): "你输了", (2, 2): "平手", (2, 3): "你赢了", (3, 1): "你赢了",
      (3, 2): "你输了", (3, 3): "平手"}
computer = random.randint(1, 3)

print '''1，石头
2，剪刀
3，布
'''
human = int(raw_input("请输入你的选择："))
print computer
print wl[(computer, human)]
