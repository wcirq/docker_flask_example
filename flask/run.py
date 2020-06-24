# -*- coding: utf-8 -*- 
# @Time 2020/6/24 14:51
# @Author wcy
# 在执行该语句之前，会执行__init__.py，实例化Flask实例，导入自己的相关应用
from my_app import app

if __name__ == "__main__":
    app.run()