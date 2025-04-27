# SDKMAN! MCP Server

一个用于与SDKMAN交互的Model Context Protocol (MCP) 服务器，支持通过Claude和其他LLM管理软件开发工具包(SDK)。

## 功能特点

* SDK管理（安装、卸载、列表、更新等）
* 交互式SDK版本选择
* 环境配置和管理
* 系统监控与信息检索
* 与SDKMAN CLI的完全集成
* 支持全部SDKMAN命令

## 前提条件

* Python ≥ 3.11
* 已安装的SDKMAN实例
* Claude Desktop或其他支持MCP的LLM界面

## 安装

### 使用pip安装

```bash
pip install sdkman-mcp
```

### 从源码安装

```bash
git clone https://github.com/your-username/sdkman-mcp.git
cd sdkman-mcp
pip install -e .
```

## 使用方法

### 在Claude Desktop中使用

要在Claude Desktop中使用此MCP服务器，需要编辑Claude配置文件：

* MacOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
* Windows: `%APPDATA%/Claude/claude_desktop_config.json`

添加以下配置：

```json
{
  "mcpServers": {
    "sdkman": {
      "command": "python",
      "args": ["-m", "sdkman_mcp"],
      "env": {
        "SDKMAN_DIR": "/Users/ocean/.sdkman"  // 可选，默认使用~/.sdkman
      },
      "alwaysAllow": [
        "sdk_list_all",
        "sdk_current_all",
        "sdk_get_version"
      ]
    }
  }
}
```

### 可用工具

SDKMAN MCP服务器提供以下工具：

* `sdk_list_all` - 列出所有可用的SDK候选项
* `sdk_list_versions` - 列出特定SDK候选项的所有可用版本
* `sdk_current_all` - 显示所有已安装SDK的当前版本
* `sdk_current_version` - 显示特定SDK候选项的当前版本
* `sdk_install_version` - 安装特定版本的SDK候选项
* `sdk_uninstall_version` - 卸载特定版本的SDK候选项
* `sdk_use_version` - 在当前shell中使用特定版本的SDK候选项
* `sdk_set_default` - 设置SDK候选项的默认版本
* `sdk_get_home` - 获取特定版本SDK候选项的主目录
* `sdk_manage_env` - 管理当前目录的.sdkmanrc文件
* `sdk_check_upgrade` - 检查可用升级或升级特定候选项
* `sdk_get_version` - 显示SDKMAN版本
* `sdk_set_offline` - 启用或禁用离线模式
* `sdk_self_update` - 更新SDKMAN本身
* `sdk_update_candidates` - 更新SDKMAN候选项
* `sdk_flush_state` - 刷新SDKMAN本地状态
* `sdk_get_help` - 获取关于SDKMAN或特定命令的帮助
* `sdk_edit_config` - 编辑SDKMAN配置

### 可用资源

* `sdkman://version` - SDKMAN版本信息
* `sdkman://current` - 当前活跃的SDK信息
* `sdkman://candidates/{candidate}` - 特定候选项的可用版本

## 开发

要设置开发环境：

```bash
git clone https://github.com/your-username/sdkman-mcp.git
cd sdkman-mcp
pip install -e ".[dev]"
```

### 使用MCP Inspector测试

```bash
npx @modelcontextprotocol/inspector python -m sdkman_mcp
```

## 故障排除

* 确保SDKMAN已正确安装（`~/.sdkman/bin/sdkman-init.sh`可执行）
* 检查环境变量`SDKMAN_DIR`指向正确的SDKMAN安装目录
* 在MacOS上，您可能需要给予终端"完全磁盘访问权限"

## 许可证

Apache License 2.0 