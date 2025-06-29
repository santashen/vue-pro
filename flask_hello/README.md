# Flask Hello 项目

这是一个最小可运行的 Flask 页面项目，当访问时会显示 "Hello, Flask!" 信息。

## 本地运行

### 使用 conda 环境（推荐）
1. 使用 conda 环境安装依赖：
```bash
/data/miniconda3/envs/light/bin/pip install -r requirements.txt
```

2. 运行应用：
```bash
/data/miniconda3/envs/light/bin/python app.py
```

4. 访问 http://localhost:5000

### 使用系统 Python
1. 安装依赖：
```bash
pip3 install -r requirements.txt
```

2. 运行应用：
```bash
python3 app.py
```

3. 访问 http://localhost:5000

## 生产环境部署

### 手动运行
使用 conda 环境运行：
```bash
/data/miniconda3/envs/light/bin/gunicorn wsgi:app --bind 127.0.0.1:5001
```

或使用系统 Python：
```bash
python3 -m gunicorn wsgi:app --bind 127.0.0.1:5001
```

### 便捷启动脚本
使用提供的启动脚本：
```bash
chmod +x start.sh
./start.sh
```

### systemd 服务管理
1. 复制服务文件：
```bash
sudo cp flask-hello.service /etc/systemd/system/
```

2. 启用并启动服务：
```bash
sudo systemctl daemon-reload
sudo systemctl enable flask-hello.service
sudo systemctl start flask-hello.service
```

3. 检查服务状态：
```bash
sudo systemctl status flask-hello.service
```

### nginx 配置（自动化管理）

#### 方案一：自动化部署（推荐）
项目使用模块化的 nginx 配置管理方案：

1. **toy 目录管理**：配置文件自动部署到 `/www/server/panel/vhost/nginx/toy/` 目录
2. **主配置包含**：需要在 `blog.com.conf` 中添加一行包含语句
3. **自动重载**：部署时自动测试和重载 nginx 配置

#### 使用 nginx 管理脚本
我们提供了 `nginx-toy-manager.sh` 脚本来管理配置：

```bash
# 上传并运行管理脚本
sudo ./nginx-toy-manager.sh
```

选择 "1. 初始化 toy 配置环境" 来自动设置。

#### 手动配置
如果需要手动配置，请在 `blog.com.conf` 的 server 块中添加：
```nginx
include /www/server/panel/vhost/nginx/toy/*.conf;
```

参考 `blog.com.conf.example` 文件查看具体位置。

## 项目结构

- `app.py` - Flask 主应用文件
- `wsgi.py` - WSGI 入口文件
- `requirements.txt` - 项目依赖
- `start.sh` - 便捷启动脚本
- `flask-hello.service` - systemd 服务配置文件
- `nginx-hello.conf` - nginx 代理配置文件（自动部署到 toy 目录）
- `blog.com.conf.example` - 主配置文件修改示例
- `README.md` - 项目说明

## 相关管理文件

- `../nginx-toy-manager.sh` - nginx 配置管理脚本

## 服务管理命令

- 启动服务：`sudo systemctl start flask-hello.service`
- 停止服务：`sudo systemctl stop flask-hello.service`
- 重启服务：`sudo systemctl restart flask-hello.service`
- 查看日志：`sudo journalctl -u flask-hello.service -f`

部署地址：http://windsong.top/hello/ 