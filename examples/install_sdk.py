#!/usr/bin/env python3
"""
通用SDKMAN交互式安装脚本

用法：
    python install_sdk.py <candidate> [版本过滤]

参数：
    candidate: 要安装的候选软件（例如 java, kotlin, gradle, maven 等）
    版本过滤: 可选，用于筛选特定版本号的关键字

示例：
    python install_sdk.py java         # 安装Java
    python install_sdk.py java 21      # 安装包含"21"的Java版本
    python install_sdk.py kotlin       # 安装Kotlin
    python install_sdk.py gradle 8     # 安装Gradle 8.x版本
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.sdkman_mcp.sdk_commands import sdk_interactive_install, sdk_list

def main():
    """主入口函数"""
    # 检查参数
    if len(sys.argv) < 2:
        print("错误: 必须指定要安装的候选软件")
        print(f"用法: {sys.argv[0]} <candidate> [版本过滤]")
        print("\n可用的候选软件:")
        
        # 列出所有可用的候选软件
        result = sdk_list()
        if result["success"]:
            # 提取并显示候选软件列表
            lines = result["data"].split('\n')
            candidates = []
            for line in lines:
                line = line.strip()
                if line and ":" in line and "sdk install" in line:
                    candidate = line.split(":", 1)[0].strip()
                    if candidate:
                        candidates.append(candidate)
            
            if candidates:
                # 每行显示5个候选软件
                for i in range(0, len(candidates), 5):
                    print("  " + ", ".join(candidates[i:i+5]))
        
        sys.exit(1)
    
    # 获取参数
    candidate = sys.argv[1]
    version = None
    if len(sys.argv) > 2:
        version = sys.argv[2]
    
    print(f"=== SDKMAN交互式安装: {candidate} ===")
    if version:
        print(f"筛选版本关键字: {version}")
    
    # 调用交互式安装函数
    result = sdk_interactive_install(candidate, version)
    
    # 处理结果
    if result["success"]:
        print(f"{candidate} 安装成功！")
    else:
        print(f"安装失败: {result['error']}")
        sys.exit(1)

if __name__ == "__main__":
    main() 