# 使用说明
 
 - 执行 
```shell script
 python3 -m pip install uwsgi
 ln -s /usr/local/python3.6/bin/uwsgi  /usr/bin/
```
 - 安装docker-compose
 ```shell script
# 下载docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
# 添加可执行权限(这里不懂可以看一下菜鸟教程-linux教程-文件权限)
sudo chmod +x /usr/local/bin/docker-compose
# 查看docker-compose版本
docker-compose --version
```

 - 在docker-compose.yml所在目录执行该命令， 生成镜像文件
```shell script
docker-compose build
```

 - 启动容器
```shell script
docker-compose up
```

 - 列出正在运行的镜像
```shell script
docker-compose images
```

 - 列出正在运行的容器
```shell script
docker-compose ps
```

 - 停止服务
```shell script
docker-compose ps
```