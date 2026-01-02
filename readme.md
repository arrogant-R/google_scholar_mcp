# Google Scholar MCP Server

🔍 让 AI 助手通过 MCP 协议搜索和访问 Google Scholar 学术论文。

Google Scholar MCP Server 是一个基于 Model Context Protocol (MCP) 的服务器，为 AI 助手提供搜索 Google Scholar 学术论文的能力。

## ✨ 核心功能

- 🔎 **论文搜索**：支持关键词搜索、作者筛选、年份范围筛选
- 📄 **完整摘要**：搜索单篇论文时可获取完整摘要内容
- 🛡️ **验证码处理**：优化了 scholarly 库的 CAPTCHA 验证码处理机制，遇到验证码时自动弹出浏览器窗口供手动验证
- 📚 **BibTeX 支持**：可获取论文的 BibTeX 引用格式
- 🚀 **高效检索**：快速获取论文元数据
---
## 🛠️ MCP 工具

### search_google_scholar

搜索 Google Scholar 上的学术文章。

**参数：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `query` | string | ✅ | 搜索关键词（论文标题、主题或关键词） |
| `author` | string | ❌ | 作者名称筛选 |
| `year_low` | int | ❌ | 起始年份 |
| `year_high` | int | ❌ | 结束年份 |
| `num_results` | int | ❌ | 返回结果数量（默认: 5） |

**返回结果：**

```json
{
  "bib": {
    "title": "论文标题",
    "author": "作者",
    "pub_year": "发表年份",
    "venue": "发表期刊/会议",
    "abstract": "摘要"
  },
  "pub_url": "论文链接",
  "num_citations": "被引用次数",
  "citedby_url": "引用链接",
  "eprint_url": "PDF 链接"
}
```
### 📚 使用示例

#### 🤖 mcp客户端调用

**关键词搜索：**

```python
result = await mcp.use_tool("search_google_scholar", {
    "query": "deep learning",
    "num_results": 5
})
```

**带作者筛选：**

```python
result = await mcp.use_tool("search_google_scholar", {
    "query": "convolutional neural networks",
    "author": "Yann LeCun",
    "num_results": 3
})
```

**带年份范围：**

```python
result = await mcp.use_tool("search_google_scholar", {
    "query": "transformer",
    "year_low": 2020,
    "year_high": 2024,
    "num_results": 5
})
```

**组合搜索：**

```python
result = await mcp.use_tool("search_google_scholar", {
    "query": "neural networks",
    "author": "Geoffrey Hinton",
    "year_low": 2015,
    "year_high": 2023,
    "num_results": 10
})
```
#### 🐍 作为 Python 包直接调用

你可以直接在 Python/Jupyter 中导入并调用：

```python
from google_scholar_mcp import search_google_scholar
results = search_google_scholar("attention is all you need", 
                                  author="Vaswani",
                                  year_low=2017, 
                                  year_high=2018, 
                                  num_results=2  )
print(results)
```
## 🚀 快速开始

### 方式一：从 PyPI 安装
```bash
uv tool install google_scholar_mcp
```

### 方式二：从 GitHub 安装

```bash
uv tool install git+https://github.com/arrogant-R/google_scholar_mcp.git
```

### 方式三：本地安装 + 开发模式

1. 克隆仓库：

```bash
git clone https://github.com/arrogant-R/google_scholar_mcp.git
cd Google-Scholar-MCP-Server
```

2. 创建虚拟环境并安装依赖：

```bash
# 使用 uv（推荐）
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -e .

# 或使用 pip
pip install -r requirements.txt
```



### 方式四：本地直接安装
```bash
# pip 直接安装
pip install google_scholar_mcp

# 或
uv add google_scholar_mcp
```

启动服务：(方式3/4)

```bash
# 作为模块运行
python -m google_scholar_mcp

# 直接运行
google-scholar-mcp
```


## ⚙️ 配置 MCP 客户端

### 方式一：使用 uv（从 uv tool 安装后）

```json
{
  "mcpServers": {
    "google-scholar": {
      "command": "uv",
      "args": [
        "tool",
        "run",
        "google_scholar_mcp"
      ]
    }
  }
}
```

### 方式二：本地开发模式（uv）

```json
{
  "mcpServers": {
    "google-scholar": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/Google-Scholar-MCP-Server",
        "run",
        "google_scholar_mcp"
      ]
    }
  }
}
```

### 方式三：使用本地 Python

```json
{
  "mcpServers": {
    "google-scholar": {
      "command": "/path/to/python", // 替换为你的安装环境下的Python解释器
      "args": [
        "-m",
        "google_scholar_mcp"
      ]
    }
  }
}
```
---

### VS Code (GitHub Copilot)

在 VS Code 的 `mcp.json` 配置文件中添加：

**使用 uv：**

```json
{
  "servers": {
    "google_scholar": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "tool",
        "run",
        "google_scholar_mcp"
      ]
    }
  }
}
```


### Claude Desktop

使用 uv（推荐）：

```json
{
  "mcpServers": {
    "google-scholar": {
      "command": "uv",
      "args": [
        "tool",
        "run",
        "google_scholar_mcp"
      ]
    }
  }
}
```

或使用 Python：

**Mac OS:**

```json
{
  "mcpServers": {
    "google-scholar": {
      "command": "python",
      "args": ["-m", "google_scholar_mcp"]
    }
  }
}
```

**Windows:**

```json
{
  "mcpServers": {
    "google-scholar": {
      "command": "C:\\Users\\YOUR\\PATH\\python.exe",
      "args": [
        "-m",
        "google_scholar_mcp"
      ]
    }
  }
}
```

### Cursor

在 Settings → Cursor Settings → MCP → Add new server 中添加：

```json
{
  "google-scholar": {
    "command": "uv",
    "args": [
      "tool",
      "run",
      "google-scholar-mcp"
    ]
  }
}
```

### Cline

```json
{
  "mcpServers": {
    "google-scholar": {
      "command": "uv",
      "args": [
        "tool",
        "run",
        "google-scholar-mcp"
      ]
    }
  }
}
```





## 优化

### 🛡️ CAPTCHA 验证码处理

本项目对 scholarly 库进行了优化，解决了遇到 Google Scholar 验证码时程序卡住的问题：

1. **自动检测验证码**：当检测到验证码时，自动弹出浏览器窗口
2. **手动验证**：在弹出的浏览器中手动完成验证
3. **Cookie 同步**：验证完成后后续请求使用自动同步的 Cookie，避免频繁触发验证
4. **Cookie 持久化**：将 Cookie 保存到本地文件，下次启动时自动加载，减少验证码出现频率

> ⚠️ 如果遇到验证码，请在弹出的浏览器窗口中手动完成验证，程序会自动等待并继续执行。

### 📄 完整摘要获取

当进行query比较完整且精确时，系统会自动获取论文的完整 abstract，而不仅仅是截断的摘要片段。这对于需要详细了解单篇论文内容的场景非常有用。

## 📁 项目结构

```
Google-Scholar-MCP-Server/
├── src/
│   └── google_scholar_mcp/
│       ├── __init__.py         # 包入口
│       ├── __main__.py         # 主入口
│       ├── server.py           # MCP 服务器实现
│       ├── search.py           # 搜索逻辑
│       └── scholarly/          # 修改版 scholarly 库
│           ├── _navigator.py
│           ├── _proxy_generator.py
│           ├── _scholarly.py
│           └── ...
├── requirements.txt            # 依赖列表
└── pyproject.toml              # 项目配置（支持 uv/pip 安装）
```

## 🔧 依赖

- Python 3.10+
- mcp
- requests
- beautifulsoup4
- selenium
- httpx
- fake_useragent
- 等（详见 requirements.txt）

## 🤝 贡献

欢迎提交 Pull Request 和 Issue！

## 📄 许可证

本项目采用 MIT 许可证。

## ⚠️ 免责声明

本工具仅供学术研究使用。请遵守 Google Scholar 的服务条款，合理使用本工具。
