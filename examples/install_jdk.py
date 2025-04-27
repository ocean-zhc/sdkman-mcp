#!/usr/bin/env python3
"""
示例脚本：交互式安装JDK

用法：
    python install_jdk.py [版本号]

示例：
    python install_jdk.py          # 显示所有JDK版本供选择
    python install_jdk.py 21       # 仅显示包含"21"的JDK版本
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.sdkman_mcp.sdk_commands import sdk_interactive_install

def main():
    """主入口函数"""
    # 获取命令行参数
    version = None
    if len(sys.argv) > 1:
        version = sys.argv[1]
    
    print("=== SDKMAN交互式JDK安装 ===")
    
    # 调用交互式安装函数
    result = sdk_interactive_install("java", version)
    
    # 处理结果
    if result["success"]:
        print("JDK安装成功！")
    else:
        print(f"安装失败: {result['error']}")
        sys.exit(1)

if __name__ == "__main__":
    main() 