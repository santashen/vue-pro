#!/bin/bash

# 个人信息管理系统启动脚本

echo "正在启动个人信息管理系统..."

# 激活虚拟环境（如果需要）
export PATH="/data/miniconda3/envs/light/bin:$PATH"

# 设置环境变量
export FLASK_APP=wsgi.py
export FLASK_ENV=production

# 安装依赖
pip install -r requirements.txt

# 运行Gunicorn
gunicorn --bind 127.0.0.1:5002 --workers 2 --timeout 60 wsgi:app 