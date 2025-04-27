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

## 贡献

欢迎贡献！请随时提交Pull Request。

## 许可证

本项目使用MIT许可证 - 详见LICENSE文件。

## 致谢

- [SDKMAN](https://sdkman.io/) - 软件开发工具包管理器
- 本项目的所有贡献者 