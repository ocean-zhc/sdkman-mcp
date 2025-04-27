"""
SDK Command Executor Module

This module provides functions to execute various SDKMAN commands through subprocess.
"""

import subprocess
import logging
import json
import os
from typing import Dict, List, Optional, Any, Union, Tuple

logger = logging.getLogger(__name__)

# SDKMAN initialization similar to shell config:
# export SDKMAN_DIR="$HOME/.sdkman"
# [[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"
SDKMAN_DIR = os.environ.get("SDKMAN_DIR", os.path.expanduser("~/.sdkman"))
SDK_INIT_PATH = os.path.join(SDKMAN_DIR, "bin/sdkman-init.sh")
SDK_COMMAND = SDK_INIT_PATH

# 检查SDKMAN初始化脚本是否存在
if not os.path.isfile(os.path.expanduser(SDK_COMMAND)):
    logger.warning(f"SDKMAN initialization script not found at {SDK_COMMAND}")

def _run_command(cmd: List[str]) -> Tuple[int, str, str]:
    """Run a command and return stdout, stderr and exit code."""
    try:
        # 构建一个shell命令，先source初始化脚本，然后执行SDK命令
        shell_cmd = f"source {SDK_COMMAND} && sdk {' '.join(cmd)}"
        logger.debug(f"Running shell command: {shell_cmd}")
        
        process = subprocess.Popen(
            shell_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True,
            executable="/bin/bash"  # 确保使用bash执行命令
        )
        stdout, stderr = process.communicate()
        return process.returncode, stdout, stderr
    except Exception as e:
        logger.error(f"Error running command {cmd}: {str(e)}")
        return 1, "", str(e)

def sdk_list() -> Dict[str, Any]:
    """List all available candidates in SDKMAN."""
    returncode, stdout, stderr = _run_command(["list"])
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or "Failed to list candidates"
        }
    
    return {
        "success": True,
        "data": stdout
    }

def sdk_list_candidate(candidate: str) -> Dict[str, Any]:
    """List versions of a specific candidate."""
    returncode, stdout, stderr = _run_command(["list", candidate])
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or f"Failed to list versions for {candidate}"
        }
    
    return {
        "success": True,
        "data": stdout
    }

def sdk_current() -> Dict[str, Any]:
    """Show the current version of all installed candidates."""
    returncode, stdout, stderr = _run_command(["current"])
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or "Failed to get current versions"
        }
    
    return {
        "success": True,
        "data": stdout
    }

def sdk_current_candidate(candidate: str) -> Dict[str, Any]:
    """Show the current version of a specific candidate."""
    returncode, stdout, stderr = _run_command(["current", candidate])
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or f"Failed to get current version of {candidate}"
        }
    
    return {
        "success": True,
        "data": stdout
    }

def sdk_install(candidate: str, version: Optional[str] = None, path: Optional[str] = None) -> Dict[str, Any]:
    """Install a candidate with the specified version or from a specific path."""
    cmd = ["install", candidate]
    if version:
        cmd.append(version)
    if path:
        cmd.append(path)
    
    returncode, stdout, stderr = _run_command(cmd)
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or f"Failed to install {candidate}"
        }
    
    return {
        "success": True,
        "data": stdout
    }

def sdk_uninstall(candidate: str, version: str) -> Dict[str, Any]:
    """Uninstall a candidate with the specified version."""
    returncode, stdout, stderr = _run_command(["uninstall", candidate, version])
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or f"Failed to uninstall {candidate} {version}"
        }
    
    return {
        "success": True,
        "data": stdout
    }

def sdk_use(candidate: str, version: str) -> Dict[str, Any]:
    """Use a specific version of a candidate in the current shell."""
    returncode, stdout, stderr = _run_command(["use", candidate, version])
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or f"Failed to use {candidate} {version}"
        }
    
    return {
        "success": True,
        "data": stdout
    }

def sdk_default(candidate: str, version: str) -> Dict[str, Any]:
    """Set the default version of a candidate."""
    returncode, stdout, stderr = _run_command(["default", candidate, version])
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or f"Failed to set {candidate} {version} as default"
        }
    
    return {
        "success": True,
        "data": stdout
    }

def sdk_home(candidate: str, version: str) -> Dict[str, Any]:
    """Get the home directory of a specific version of a candidate."""
    returncode, stdout, stderr = _run_command(["home", candidate, version])
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or f"Failed to get home directory of {candidate} {version}"
        }
    
    return {
        "success": True,
        "data": stdout.strip()  # Remove trailing newline
    }

def sdk_env(action: Optional[str] = None) -> Dict[str, Any]:
    """Manage the .sdkmanrc file. Action can be 'init', 'install', or 'clear'."""
    cmd = ["env"]
    if action:
        cmd.append(action)
    
    returncode, stdout, stderr = _run_command(cmd)
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or f"Failed to execute env {action or ''}"
        }
    
    return {
        "success": True,
        "data": stdout
    }

def sdk_upgrade(candidate: Optional[str] = None) -> Dict[str, Any]:
    """Check available upgrades or upgrade a specific candidate."""
    cmd = ["upgrade"]
    if candidate:
        cmd.append(candidate)
    
    returncode, stdout, stderr = _run_command(cmd)
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or f"Failed to upgrade {candidate or 'all candidates'}"
        }
    
    return {
        "success": True,
        "data": stdout
    }

def sdk_version() -> Dict[str, Any]:
    """Display the SDKMAN version."""
    returncode, stdout, stderr = _run_command(["version"])
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or "Failed to get SDKMAN version"
        }
    
    return {
        "success": True,
        "data": stdout
    }

def sdk_offline(mode: str) -> Dict[str, Any]:
    """Enable or disable offline mode."""
    if mode not in ["enable", "disable"]:
        return {
            "success": False,
            "error": "Mode must be 'enable' or 'disable'"
        }
    
    returncode, stdout, stderr = _run_command(["offline", mode])
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or f"Failed to {mode} offline mode"
        }
    
    return {
        "success": True,
        "data": stdout
    }

def sdk_selfupdate(force: bool = False) -> Dict[str, Any]:
    """Update SDKMAN itself."""
    cmd = ["selfupdate"]
    if force:
        cmd.append("force")
    
    returncode, stdout, stderr = _run_command(cmd)
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or "Failed to update SDKMAN"
        }
    
    return {
        "success": True,
        "data": stdout
    }

def sdk_update() -> Dict[str, Any]:
    """Update SDKMAN candidates."""
    returncode, stdout, stderr = _run_command(["update"])
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or "Failed to update SDKMAN candidates"
        }
    
    return {
        "success": True,
        "data": stdout
    }

def sdk_flush(mode: Optional[str] = None) -> Dict[str, Any]:
    """Flush SDKMAN local state. Mode can be 'tmp', 'metadata', or 'version'."""
    cmd = ["flush"]
    if mode:
        if mode not in ["tmp", "metadata", "version"]:
            return {
                "success": False,
                "error": "Mode must be 'tmp', 'metadata', or 'version'"
            }
        cmd.append(mode)
    
    returncode, stdout, stderr = _run_command(cmd)
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or f"Failed to flush {mode or 'all'}"
        }
    
    return {
        "success": True,
        "data": stdout
    }

def sdk_help(command: Optional[str] = None) -> Dict[str, Any]:
    """Get help about SDKMAN or a specific command."""
    cmd = ["help"]
    if command:
        cmd.append(command)
    
    returncode, stdout, stderr = _run_command(cmd)
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or f"Failed to get help for {command or 'SDKMAN'}"
        }
    
    return {
        "success": True,
        "data": stdout
    }

def sdk_config() -> Dict[str, Any]:
    """Edit the SDKMAN configuration."""
    returncode, stdout, stderr = _run_command(["config"])
    
    if returncode != 0:
        return {
            "success": False,
            "error": stderr or "Failed to edit SDKMAN configuration"
        }
    
    return {
        "success": True,
        "data": stdout
    }

def parse_sdk_versions(output: str, search_version: Optional[str] = None) -> List[Dict[str, str]]:
    """
    解析SDK版本列表输出，转换成结构化数据
    
    Args:
        output: sdk list <candidate> 命令的输出
        search_version: 可选的版本搜索字符串 (例如 "21")
    
    Returns:
        包含版本信息的字典列表
    """
    versions = []
    lines = output.split('\n')
    vendor = None
    in_version_section = False
    
    for line in lines:
        line = line.strip()
        
        # 跳过空行和非数据行
        if not line:
            continue
            
        # 检查是否是分隔符行
        if line.startswith('==') or line.startswith('--'):
            if "Version" in line and "Vendor" in line:
                in_version_section = True
            continue
            
        # 如果尚未进入版本区域，检查是否是版本表头
        if not in_version_section and "Vendor" in line and "Version" in line:
            in_version_section = True
            continue
            
        # 如果已进入版本区域
        if in_version_section:
            # 检查是否是新的供应商部分（没有 | 符号的行）
            if '|' not in line:
                vendor = line.strip()
                continue
                
            # 处理版本行
            if '|' in line:
                parts = [part.strip() for part in line.split('|')]
                # 确保行包含足够的字段
                if len(parts) >= 6:
                    # 确定是否是当前使用的版本
                    use_indicator = ">>>" in parts[1]
                    
                    # 提取版本信息
                    version_info = {
                        "vendor": vendor or "",
                        "use": use_indicator,
                        "version": parts[2],
                        "dist": parts[3],
                        "status": parts[4],
                        "identifier": parts[5]
                    }
                    
                    # 如果指定了搜索版本，检查版本号是否匹配
                    if search_version:
                        if search_version in version_info["version"]:
                            versions.append(version_info)
                    else:
                        versions.append(version_info)
    
    return versions

def sdk_interactive_install(candidate: str, search_version: Optional[str] = None) -> Dict[str, Any]:
    """
    交互式安装指定候选软件的特定版本
    
    Args:
        candidate: 要安装的候选软件 (例如 "java")
        search_version: 可选的版本搜索字符串 (例如 "21")
        
    Returns:
        安装结果字典
    """
    # 获取可用版本列表
    list_result = sdk_list_candidate(candidate)
    if not list_result["success"]:
        return list_result
    
    # 解析版本列表
    versions = parse_sdk_versions(list_result["data"], search_version)
    if not versions:
        return {
            "success": False,
            "error": f"未找到 {candidate} 的版本" + (f" (包含 '{search_version}')" if search_version else "")
        }
    
    # 显示可用的版本列表
    print(f"\n{'='*75}")
    print(f"可用的 {candidate} 版本" + (f" (符合条件: '{search_version}')" if search_version else "") + f" - {len(versions)}个结果")
    print(f"{'='*75}")
    print(f"{'序号':<6} {'供应商':<12} {'|'} {'使用':<4} {'|'} {'版本':<10} {'|'} {'分发':<10} {'|'} {'状态':<12} {'|'} {'标识符'}")
    print(f"{'-'*6} {'-'*12} {'|'} {'-'*4} {'|'} {'-'*10} {'|'} {'-'*10} {'|'} {'-'*12} {'|'} {'-'*25}")
    
    for i, ver in enumerate(versions, 1):
        use_mark = ">>>" if ver["use"] else ""
        status = ver["status"] if ver["status"] else ""
        print(f"{i:<6} {ver['vendor']:<12} {'|'} {use_mark:<4} {'|'} {ver['version']:<10} {'|'} {ver['dist']:<10} {'|'} {status:<12} {'|'} {ver['identifier']}")
    
    print(f"\n说明: 使用列中的 >>> 表示当前默认版本")
    
    # 提示用户选择
    while True:
        try:
            choice = input("\n请选择要安装的版本序号 (或输入 'q' 退出): ")
            if choice.lower() in ['q', 'quit', 'exit']:
                return {
                    "success": False,
                    "error": "用户取消安装"
                }
            
            idx = int(choice) - 1
            if 0 <= idx < len(versions):
                selected = versions[idx]
                identifier = selected['identifier']
                
                print(f"\n您选择了: {selected['vendor']} {selected['version']} ({identifier})")
                confirm = input("确认安装? (y/n): ")
                if confirm.lower() in ['y', 'yes', '是']:
                    print(f"\n正在安装 {candidate} {identifier}，请稍候...\n")
                    result = sdk_install(candidate, identifier)
                    
                    if result["success"]:
                        print(f"\n安装成功! 通过以下命令使用该版本:")
                        print(f"  sdk use {candidate} {identifier}")
                        
                    return result
                else:
                    print("取消安装操作")
            else:
                print(f"无效的选择，请输入 1 到 {len(versions)} 之间的数字")
        except ValueError:
            print("请输入有效的数字")
        except KeyboardInterrupt:
            print("\n操作被用户中断")
            return {
                "success": False,
                "error": "用户中断操作"
            }

def main():
    """主函数入口，允许从命令行直接使用交互式安装功能"""
    import argparse
    import sys
    
    parser = argparse.ArgumentParser(description='SDKMAN交互式工具')
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # 安装命令
    install_parser = subparsers.add_parser('install', help='交互式安装SDK')
    install_parser.add_argument('candidate', help='要安装的候选软件 (例如 java, kotlin, gradle)')
    install_parser.add_argument('--version', '-v', help='要筛选的版本 (例如 21)')
    
    # 列出命令
    list_parser = subparsers.add_parser('list', help='列出可用的SDK')
    list_parser.add_argument('candidate', nargs='?', help='要列出版本的候选软件 (例如 java)')
    
    # 当前版本命令
    current_parser = subparsers.add_parser('current', help='显示当前使用的SDK版本')
    current_parser.add_argument('candidate', nargs='?', help='要显示当前版本的候选软件')
    
    # 解析参数
    args = parser.parse_args()
    
    # 如果没有指定命令，显示帮助
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # 执行相应的命令
    if args.command == 'install':
        result = sdk_interactive_install(args.candidate, args.version)
        if not result["success"]:
            print(f"错误: {result['error']}")
            sys.exit(1)
    
    elif args.command == 'list':
        if args.candidate:
            result = sdk_list_candidate(args.candidate)
            if result["success"]:
                print(result["data"])
            else:
                print(f"错误: {result['error']}")
                sys.exit(1)
        else:
            result = sdk_list()
            if result["success"]:
                print(result["data"])
            else:
                print(f"错误: {result['error']}")
                sys.exit(1)
    
    elif args.command == 'current':
        if args.candidate:
            result = sdk_current_candidate(args.candidate)
        else:
            result = sdk_current()
            
        if result["success"]:
            print(result["data"])
        else:
            print(f"错误: {result['error']}")
            sys.exit(1)

if __name__ == "__main__":
    main() 