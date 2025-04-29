# SDKMAN 交互式命令行工具

一个用于SDKMAN（软件开发工具包管理器）的交互式命令行界面，使浏览、筛选和安装SDK变得更加容易。

## 功能特点

- 格式化显示的交互式版本选择
- 通过关键词过滤版本（例如，通过"21"筛选Java 21）
- 支持所有SDKMAN候选软件（Java、Kotlin、Gradle等）
- 全面的命令行界面
- 用户友好的版本信息显示

## 前提条件

- Python 3.6+
- 已安装并配置SDKMAN
- Bash shell环境

## 安装

克隆此仓库：

```bash
git clone https://github.com/yourusername/sdkman-mcp.git
cd sdkman-mcp
```

## 使用方法

### 作为Python模块使用

```python
from src.sdkman_mcp.sdk_commands import sdk_interactive_install

# 通过交互式选择安装Java
result = sdk_interactive_install("java")

# 安装Java 21.x（带过滤）
result = sdk_interactive_install("java", "21")
```

### 命令行界面

本工具提供了即用型脚本：

#### 通用SDK安装器

安装任何SDKMAN候选软件：

```bash
python examples/install_sdk.py java       # 安装任意Java版本
python examples/install_sdk.py java 21    # 安装Java 21.x版本
python examples/install_sdk.py kotlin     # 安装Kotlin
python examples/install_sdk.py gradle 8   # 安装Gradle 8.x版本
```

#### JDK专用安装器

```bash
python examples/install_jdk.py           # 安装任意JDK版本
python examples/install_jdk.py 21        # 安装JDK 21.x版本
```

### 主命令行界面

该模块也可以直接运行：

```bash
python -m src.sdkman_mcp.sdk_commands install java --version 21
python -m src.sdkman_mcp.sdk_commands list java
python -m src.sdkman_mcp.sdk_commands current
```

## 与AI助手集成（MCP集成）

SDKMAN交互式命令行工具可以与支持模型上下文协议（Model Context Protocol, MCP）的AI助手集成，让您能够通过与AI的对话直接管理SDK。

### 与Claude Desktop集成

要在Claude Desktop中使用此工具，编辑Claude配置文件：

* MacOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
* Windows: `%APPDATA%/Claude/claude_desktop_config.json`

添加以下配置：

```json
{
  "mcpServers": {
    "sdkman": {
      "command": "python",
      "args": ["-m", "src.sdkman_mcp.sdk_commands"],
      "env": {
        "SDKMAN_DIR": "~/.sdkman"  // 可选，默认为~/.sdkman
      },
      "alwaysAllow": [
        "list",
        "current"
      ]
    }
  }
}
```

### 与其他支持MCP的AI助手集成

对于其他支持MCP的AI助手：

1. 配置助手使用此模块作为MCP服务器
2. 提供模块路径：`src.sdkman_mcp.sdk_commands`
3. 确保环境能够访问您的SDKMAN安装

### 可用的MCP命令

集成到MCP后，您可以使用自然语言与SDKMAN交互：

* "列出可用的Java版本"
* "安装Java 21"
* "显示我当前安装的所有SDK"
* "将Gradle更新到最新版本"
* "将Java 17设置为默认版本"

AI助手将解释这些命令并使用适当的SDKMAN函数来执行它们。

## 输出示例

运行交互式安装器时，您将看到格式化的可用版本列表：

```
=========================================================================
可用的 java 版本 (符合条件: '21') - 12个结果
=========================================================================
序号   供应商       | 使用 | 版本      | 分发      | 状态        | 标识符
------ ------------ | ---- | ---------- | --------- | ----------- | -------------------------
1      Correto      |      | 21.0.7     | amzn      |             | 21.0.7-amzn
2      Correto      |      | 21.0.6     | amzn      |             | 21.0.6-amzn
3      GraalVM CE   |      | 21.0.2     | graalce   |             | 21.0.2-graalce
4      GraalVM Oracle|     | 21.0.7     | graal     |             | 21.0.7-graal
5      GraalVM Oracle|     | 21.0.6     | graal     |             | 21.0.6-graal
6      Java.net     |      | 21.0.2     | open      |             | 21.0.2-open
7      Liberica     |      | 21.0.7.fx  | librca    |             | 21.0.7.fx-librca
8      Liberica     |      | 21.0.7     | librca    |             | 21.0.7-librca
9      Liberica     |      | 21.0.6.fx  | librca    |             | 21.0.6.fx-librca
10     Liberica     |      | 21.0.6     | librca    |             | 21.0.6-librca

说明: 使用列中的 >>> 表示当前默认版本

请选择要安装的版本序号 (或输入 'q' 退出): 
```

## API参考

该模块提供了以下函数：

- `sdk_interactive_install(candidate, search_version=None)`: 交互式安装
- `parse_sdk_versions(output, search_version=None)`: 解析SDK版本列表
- 其他标准SDKMAN函数（列表、安装、当前等）

## 工作原理

该工具通过以下方式为SDKMAN提供增强界面：

1. 通过shell执行SDKMAN命令
2. 解析和格式化输出
3. 提供交互式选择界面
4. 使用适当的确认步骤处理安装

## 故障排除

常见问题和解决方案：

- **找不到SDKMAN**：确保SDKMAN正确安装在`~/.sdkman`目录下，或设置`SDKMAN_DIR`环境变量
- **权限被拒绝**：检查SDKMAN脚本是否具有执行权限
- **命令未找到**：确保系统上可用bash（运行SDKMAN命令所需）
- **MCP集成问题**：检查AI助手是否具有执行命令的适当权限

## 贡献

欢迎贡献！请随时提交Pull Request。

## 许可证

本项目使用MIT许可证 - 详见LICENSE文件。

## 致谢

- [SDKMAN](https://sdkman.io/) - 软件开发工具包管理器
- 本项目的所有贡献者 