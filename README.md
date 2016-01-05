# 张馨允毕业设计之环境部署

本项目基于 [Fabric](http://www.fabfile.org/) 实现了 *zhangxinyun-flask* 服务的远程部署

## 依赖

* fabric

## 配置说明

//TODO

## 任务说明

### fab init

执行初始化环境操作：

1. 安装 Python 包管理器 *pip*

2. 安装 Python 虚拟环境 *virtualenv*

3. 安装 Git

### fab install

执行安装操作：

1. 下载工程源代码

2. 创建 Python 虚拟环境

3. 安装依赖库

### fab clean

执行清理操作

### fab runserver

执行启动服务操作