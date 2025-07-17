# Flask Heat Calculator

水的加热功率计算器，基于 Flask 开发的 Web 应用。

## 功能特性

- 支持多种流量单位（m³/h、L/min、kg/h）
- 精确计算水的比热容（考虑温度变化）
- 实时计算加热功率（kJ/h、kW、W）
- 响应式 Web 界面
- 数据输入验证

## 部署说明

### 生产环境部署

项目已配置自动部署，当代码推送到 main 分支时会自动部署到 VPS。

**访问地址：** `/toy/heat/`

**端口配置：** 5003

**服务管理：**
```bash
# 启动服务
sudo systemctl start flask-heat.service

# 停止服务
sudo systemctl stop flask-heat.service

# 重启服务
sudo systemctl restart flask-heat.service

# 查看服务状态
sudo systemctl status flask-heat.service
```

### 本地开发

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行应用：
```bash
python app.py
```

或使用启动脚本：
```bash
./start.sh
```

## 技术栈

- Flask 3.0.0
- NumPy（数值计算）
- Gunicorn（WSGI 服务器）
- Nginx（反向代理）
- Systemd（服务管理）

## 文件结构

```
flask_heat_calculator/
├── app.py                 # 主应用文件
├── wsgi.py                # WSGI 入口点
├── requirements.txt       # Python 依赖
├── start.sh              # 启动脚本
├── flask-heat.service    # Systemd 服务文件
├── nginx-heat.conf       # Nginx 配置文件
├── water_heat_calculator.py  # 核心计算逻辑
├── templates/
│   └── index.html        # 前端模板
└── README.md            # 说明文档
```

## API 端点

- `GET /` - 主页面
- `POST /calculate` - 计算加热功率

## 计算公式

比热容计算公式（考虑温度变化）：
```
c = 4.214 - 2.286e-3 * T + 4.991e-5 * T² - 4.519e-7 * T³
```

加热功率计算公式：
```
Q = m × c × ΔT
```

其中：
- Q: 加热功率 (kJ/h)
- m: 质量流量 (kg/h)
- c: 比热容 (kJ/kg·°C)
- ΔT: 温度差 (°C) 