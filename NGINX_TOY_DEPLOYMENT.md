# Nginx Toy 项目自动化部署方案

## 概述

这是一个模块化的 nginx 配置管理方案，用于自动化部署多个小项目的 nginx 配置。

## 架构设计

```
/www/server/panel/vhost/nginx/
├── blog.com.conf              # 主配置文件
└── toy/                       # toy 项目配置目录
    ├── nginx-hello.conf       # Flask Hello 项目配置
    └── [其他项目配置文件]      # 未来的其他项目配置
```

## 工作原理

1. **模块化配置**：每个项目都有独立的 nginx 配置文件
2. **统一管理**：所有项目配置文件放在 `toy/` 目录下
3. **自动包含**：主配置文件通过 `include` 语句包含所有 toy 配置
4. **自动部署**：GitHub Actions 自动复制配置文件并重载 nginx

## 部署流程

### 首次设置

1. **运行管理脚本**：
   ```bash
   sudo ./nginx-toy-manager.sh
   ```
   选择 "1. 初始化 toy 配置环境"

2. **或者手动配置**：
   - 创建目录：`sudo mkdir -p /www/server/panel/vhost/nginx/toy`
   - 在 `blog.com.conf` 中添加：`include /www/server/panel/vhost/nginx/toy/*.conf;`

### 自动部署

每次 push 到 main 分支时，GitHub Actions 会自动：

1. 部署 Vue 项目到 `/www/wwwroot/hexo/toy/`
2. 部署 Flask 项目到 `/www/wwwroot/hexo/hello/`
3. 安装 Python 依赖
4. 配置 systemd 服务
5. 复制 nginx 配置到 toy 目录
6. 测试并重载 nginx 配置

## 添加新项目

要添加新的项目，只需要：

1. 在项目中创建对应的 nginx 配置文件
2. 在 GitHub Actions 中添加复制步骤
3. push 代码，自动部署

## 管理命令

使用 `nginx-toy-manager.sh` 脚本：

- `1` - 初始化环境
- `2` - 检查配置状态  
- `3` - 列出配置文件
- `4` - 测试 nginx 配置
- `5` - 重新加载 nginx

## 优势

✅ **模块化管理**：每个项目独立配置，互不影响  
✅ **自动化部署**：无需手动操作 nginx 配置  
✅ **安全可靠**：自动备份和配置测试  
✅ **易于维护**：统一的管理工具和清晰的目录结构  
✅ **可扩展性**：轻松添加新项目配置

## 注意事项

- 确保主配置文件中包含了 `include /www/server/panel/vhost/nginx/toy/*.conf;`
- 新增配置后建议使用管理脚本测试配置
- 配置文件会自动备份，安全可靠 