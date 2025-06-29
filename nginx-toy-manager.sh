#!/bin/bash

# Nginx Toy 配置管理脚本
# 用于管理 /www/server/panel/vhost/nginx/toy/ 目录下的配置文件

NGINX_TOY_DIR="/www/server/panel/vhost/nginx/toy"
MAIN_CONF="/www/server/panel/vhost/nginx/blog.com.conf"
INCLUDE_LINE="include /www/server/panel/vhost/nginx/toy/*.conf;"

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Nginx Toy 配置管理器 ===${NC}"

# 检查是否以 root 权限运行
if [[ $EUID -ne 0 ]]; then
   echo -e "${RED}此脚本需要 root 权限运行${NC}"
   echo "请使用: sudo $0"
   exit 1
fi

# 创建 toy 目录
create_toy_dir() {
    echo -e "${YELLOW}创建 toy 配置目录...${NC}"
    mkdir -p "$NGINX_TOY_DIR"
    echo -e "${GREEN}✓ 目录已创建: $NGINX_TOY_DIR${NC}"
}

# 检查主配置文件
check_main_config() {
    echo -e "${YELLOW}检查主配置文件...${NC}"
    if grep -q "$INCLUDE_LINE" "$MAIN_CONF"; then
        echo -e "${GREEN}✓ 主配置已包含 toy 目录${NC}"
        return 0
    else
        echo -e "${RED}✗ 主配置未包含 toy 目录${NC}"
        echo -e "${YELLOW}需要在 $MAIN_CONF 中添加：${NC}"
        echo "  $INCLUDE_LINE"
        return 1
    fi
}

# 添加 include 到主配置
add_include_to_main() {
    echo -e "${YELLOW}添加 include 到主配置文件...${NC}"
    
    # 备份原文件
    cp "$MAIN_CONF" "$MAIN_CONF.backup.$(date +%Y%m%d_%H%M%S)"
    echo -e "${GREEN}✓ 已备份原配置文件${NC}"
    
    # 在 SSL 配置后添加 include
    sed -i '/^[[:space:]]*#SSL-END/a\\n    # === TOY PROJECTS CONFIG ===\n    include /www/server/panel/vhost/nginx/toy/*.conf;\n    # === TOY PROJECTS END ===' "$MAIN_CONF"
    
    echo -e "${GREEN}✓ 已添加 include 配置${NC}"
}

# 列出所有 toy 配置
list_configs() {
    echo -e "${YELLOW}toy 目录下的配置文件：${NC}"
    if ls "$NGINX_TOY_DIR"/*.conf 2>/dev/null; then
        echo -e "${GREEN}找到以上配置文件${NC}"
    else
        echo -e "${YELLOW}暂无配置文件${NC}"
    fi
}

# 测试 nginx 配置
test_nginx() {
    echo -e "${YELLOW}测试 nginx 配置...${NC}"
    if nginx -t; then
        echo -e "${GREEN}✓ nginx 配置测试通过${NC}"
        return 0
    else
        echo -e "${RED}✗ nginx 配置测试失败${NC}"
        return 1
    fi
}

# 重新加载 nginx
reload_nginx() {
    echo -e "${YELLOW}重新加载 nginx...${NC}"
    if systemctl reload nginx; then
        echo -e "${GREEN}✓ nginx 已重新加载${NC}"
    else
        echo -e "${RED}✗ nginx 重新加载失败${NC}"
    fi
}

# 主菜单
show_menu() {
    echo ""
    echo "请选择操作："
    echo "1. 初始化 toy 配置环境"
    echo "2. 检查配置状态"
    echo "3. 列出 toy 配置文件"
    echo "4. 测试 nginx 配置"
    echo "5. 重新加载 nginx"
    echo "6. 退出"
    echo ""
}

# 初始化环境
init_environment() {
    echo -e "${GREEN}=== 初始化 toy 配置环境 ===${NC}"
    create_toy_dir
    
    if ! check_main_config; then
        read -p "是否自动添加 include 配置到主文件？(y/n): " answer
        if [[ $answer == "y" || $answer == "Y" ]]; then
            add_include_to_main
        else
            echo -e "${YELLOW}请手动添加以下行到 $MAIN_CONF 的 server 块中：${NC}"
            echo "  $INCLUDE_LINE"
        fi
    fi
    
    if test_nginx; then
        reload_nginx
    fi
}

# 主循环
while true; do
    show_menu
    read -p "请输入选项 (1-6): " choice
    
    case $choice in
        1)
            init_environment
            ;;
        2)
            create_toy_dir
            check_main_config
            ;;
        3)
            list_configs
            ;;
        4)
            test_nginx
            ;;
        5)
            if test_nginx; then
                reload_nginx
            fi
            ;;
        6)
            echo -e "${GREEN}再见！${NC}"
            exit 0
            ;;
        *)
            echo -e "${RED}无效选项，请重新选择${NC}"
            ;;
    esac
    
    echo ""
    read -p "按 Enter 继续..."
done 