# My Travel 旅行地图项目

## 项目简介

这是一个静态HTML项目，使用Leaflet.js地图库展示个人旅行足迹。项目包含一个互动地图，标记了作者访问过的各个城市，并附有相应的旅行回忆和评论。

## 项目特点

- 📍 **互动地图**：基于OpenStreetMap的地图展示
- 🐧 **自定义标记**：使用可爱的企鹅图标作为地点标记
- 💬 **旅行回忆**：每个地点都包含个人的旅行感受和回忆
- 📱 **响应式设计**：使用Bootstrap框架，支持移动端访问
- 🎨 **美观界面**：渐变背景和现代化UI设计

## 文件结构

```
my_travel/
├── app.html           # 主页面文件
├── penguin.png        # 地图标记图标
├── places.json        # 地点数据文件
├── nginx-travel.conf  # Nginx配置文件
└── README.md         # 项目说明文件
```

## 技术栈

- **前端**：HTML5, CSS3, JavaScript
- **地图库**：Leaflet.js
- **UI框架**：Bootstrap 5.3.3
- **地图服务**：OpenStreetMap
- **Web服务器**：Nginx（静态文件服务）

## 部署说明

### 自动部署

项目通过GitHub Actions自动部署到VPS服务器：

1. 代码推送到main分支后，自动触发部署流程
2. 静态文件上传到服务器 `/www/wwwroot/hexo/travel/` 目录
3. Nginx配置文件自动复制到 `/www/server/panel/vhost/nginx/toy/` 目录
4. Nginx服务自动重新加载配置

### 手动部署

如果需要手动部署：

```bash
# 1. 上传文件到服务器
scp -r my_travel/* user@server:/www/wwwroot/hexo/travel/

# 2. 复制nginx配置
sudo cp /www/wwwroot/hexo/travel/nginx-travel.conf /www/server/panel/vhost/nginx/toy/

# 3. 测试nginx配置
sudo nginx -t

# 4. 重新加载nginx
sudo systemctl reload nginx
```

## 访问方式

部署完成后，可以通过以下URL访问：

```
https://your-domain.com/toy/travel/
```

## 配置说明

### Nginx配置特点

- **静态文件服务**：直接serve HTML、CSS、JS、图片等静态文件
- **缓存优化**：对不同类型的文件设置不同的缓存策略
- **安全头**：添加了基本的安全响应头
- **MIME类型**：为JSON文件设置正确的Content-Type

### 数据格式

`places.json` 文件格式：

```json
[
  {
    "name": "城市名称",
    "lat": 纬度,
    "lon": 经度,
    "comment": "旅行回忆和评论"
  }
]
```

## 维护说明

### 添加新地点

编辑 `places.json` 文件，添加新的地点对象：

```json
{
  "name": "新城市",
  "lat": 新纬度,
  "lon": 新经度,
  "comment": "新的旅行体验"
}
```

### 自定义样式

可以修改 `app.html` 中的CSS样式来调整页面外观。

### 更换地图标记

替换 `penguin.png` 文件可以更换地图标记图标，建议使用32x32像素的PNG图片。

## 注意事项

1. 由于使用的是静态文件，无需数据库或后端服务
2. 地点数据存储在JSON文件中，修改后需要重新部署
3. 确保服务器有足够的带宽处理地图加载请求
4. 如果需要添加大量地点，建议考虑性能优化

## 许可证

本项目为个人使用项目，地图数据来源于OpenStreetMap。 