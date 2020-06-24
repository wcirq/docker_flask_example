# -*- coding: utf-8 -*- 
# @Time 2020/6/24 14:50
# @Author wcy
# 这里导入的app就是__init__.py文件中初始化的Flask实例
from my_app import app
import os

# 定义相关处理函数
@app.route("/")
def index():

    # Use os.getenv("key") to get environment variables
    # 此处获取环境变量
    # 相关环境变量配置后面会说
    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"Hello from {app_name} running in a Docker container behind Nginx!"

    return "Hello from Flask"