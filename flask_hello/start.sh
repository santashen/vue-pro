#!/bin/bash

# Flask Hello 启动脚本

echo "正在启动 Flask Hello 应用..."

# 设置 conda 环境路径
CONDA_PATH="/data/miniconda3"
PYTHON_PATH="/data/miniconda3/envs/light/bin/python"

# 检查 conda 环境是否存在
if [[ -f "$PYTHON_PATH" ]]; then
    echo "使用 conda 环境: $PYTHON_PATH"
    export PATH="/data/miniconda3/envs/light/bin:$PATH"
    /data/miniconda3/envs/light/bin/gunicorn wsgi:app --bind 127.0.0.1:5001
else
    echo "警告：conda 环境不存在，尝试使用系统 Python"
    python3 -m gunicorn wsgi:app --bind 127.0.0.1:5001
fi 