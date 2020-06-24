# -*- coding: utf-8 -*- 
# @Time 2020/6/24 14:50
# @Author wcy
from flask import Flask

# 实例化一个web应用
app = Flask(__name__)

# 导入views及其他相关模块
from my_app import views