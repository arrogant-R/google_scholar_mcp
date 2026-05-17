# Google Scholar MCP Server & Skill

🔍 让 AI 助手通过 MCP 协议或 OpenClaw Skill 搜索和访问 Google Scholar 学术论文。

本项目提供两种使用方式：

| 方式 | 适用场景 | 协议 |
|------|----------|------|
| **MCP Server** | Claude Desktop / Cursor / VS Code / Cline 等支持 MCP 的客户端 | Model Context Protocol (stdio) |
| **OpenClaw Skill** | OpenClaw / QClaw 平台的 Agent 技能包 | OpenClaw Skill 协议 |

---

## ✨ 核心功能

- 🔎 **论文搜索**：支持关键词搜索、作者筛选、年份范围筛选
- 📄 **完整摘要**：提供精确标题和作者时可获取完整摘要内容
- 🛡️ **验证码处理**：优化了 scholarly 库的 CAPTCHA 验证码处理机制，遇到验证码时自动弹出浏览器窗口供手动验证
- 📚 **BibTeX 支持**：可获取论文的 BibTeX 引用格式
- 🚀 **高效检索**：快速获取论文元数据

---

## 📦 方式一：MCP Server

### MCP 工具

#### search_google_scholar

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

### 使用示例

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

### 🐍 作为 Python 包直接调用

```python
from google_scholar_mcp import search_google_scholar

results = search_google_scholar(
    "attention is all you need",
    author="Vaswani",
    year_low=2017,
    year_high=2018,
    num_results=2
)
print(results)
```

### 安装

#### 从 PyPI 安装

```bash
uv tool install google_scholar_mcp
```

#### 从 GitHub 安装

```bash
uv tool install git+https://github.com/arrogant-R/google_scholar_mcp.git
```

#### 本地安装 + 开发模式

```bash
git clone https://github.com/arrogant-R/google_scholar_mcp.git
cd Google-Scholar-MCP-Server

# 使用 uv（推荐）
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -e .

# 或使用 pip
pip install -r requirements.txt
```

#### 本地直接安装

```bash
pip install google_scholar_mcp
# 或
uv add google_scholar_mcp
```

启动服务（方式3/4）：

```bash
# 作为模块运行
python -m google_scholar_mcp

# 直接运行
google-scholar-mcp
```

### ⚙️ 配置 MCP 客户端

#### 使用 uv（从 uv tool 安装后）

```json
{
  "mcpServers": {
    "google-scholar": {
      "command": "uv",
      "args": ["tool", "run", "google_scholar_mcp"]
    }
  }
}
```

#### 本地开发模式（uv）

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

#### 使用本地 Python

```json
{
  "mcpServers": {
    "google-scholar": {
      "command": "/path/to/python",
      "args": ["-m", "google_scholar_mcp"]
    }
  }
}
```

### VS Code (GitHub Copilot)

```json
{
  "servers": {
    "google_scholar": {
      "type": "stdio",
      "command": "uv",
      "args": ["tool", "run", "google_scholar_mcp"]
    }
  }
}
```

### Claude Desktop

```json
{
  "mcpServers": {
    "google-scholar": {
      "command": "uv",
      "args": ["tool", "run", "google_scholar_mcp"]
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
      "args": ["-m", "google_scholar_mcp"]
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
    "args": ["tool", "run", "google-scholar-mcp"]
  }
}
```

### Cline

```json
{
  "mcpServers": {
    "google-scholar": {
      "command": "uv",
      "args": ["tool", "run", "google-scholar-mcp"]
    }
  }
}
```

---

## 🧩 方式二：OpenClaw Skill

Skill 版本将搜索功能封装为 OpenClaw 技能包，Agent 可直接通过命令行脚本调用搜索能力，无需启动 MCP 服务器进程。

### 安装

#### 方式一：对话安装

直接对 Agent 说：

> 「从 GitHub 仓库 `arrogant-R/google_scholar_mcp` 安装 google-scholar-search 技能」

Agent 会自动从仓库的 `skill/google-scholar-search/` 目录下载并安装。

#### 方式二：手动安装

**Step 1：安装 CLI 工具**

Skill 依赖 `google-scholar` 命令，需要先安装：

```bash
# Via uv (recommended)
uv tool install google_scholar_mcp

# Via pip
pip install google_scholar_mcp
```

**Step 2：复制 Skill 文件**

将本仓库 `skill/google-scholar-search` 目录复制到 `~/.qclaw/skills/`：

```powershell
# Windows
Copy-Item -Recurse "./skill/google-scholar-search" "$env:USERPROFILE\.qclaw\skills\google-scholar-search"

# macOS/Linux
cp -r ./skill/google-scholar-search ~/.qclaw/skills/
```

### 使用方法

Skill 安装后，Agent 会在用户提及学术论文搜索、Google Scholar、文献检索等场景时自动触发。

Skill 内部调用 `google-scholar` CLI 命令（由 `google_scholar_mcp` 包提供），用法如下：

#### 搜索论文

```bash
# 基本搜索
google-scholar search "deep learning" --num-results 5

# 带作者筛选
google-scholar search "convolutional neural networks" --author "Yann LeCun"

# 带年份范围
google-scholar search "transformer" --year-low 2020 --year-high 2024

# 组合搜索
google-scholar search "neural networks" --author "Geoffrey Hinton" --year-low 2015 --year-high 2023 --num-results 10
```

#### 获取 BibTeX 引用

```bash
google-scholar bibtex "attention is all you need"
```

#### 快速搜索（不填充详细信息）

```bash
google-scholar search "large language model" --no-fill --num-results 10
```

### CLI 参数

#### search 命令

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `query` | str | 必填 | 搜索关键词（论文标题、主题或关键词） |
| `--author` | str | None | 作者名称筛选 |
| `--year-low` | int | None | 起始年份 |
| `--year-high` | int | None | 结束年份 |
| `--num-results` | int | 5 | 返回结果数量 |
| `--no-fill` | flag | off | 跳过详细信息填充（更快但数据较少） |

#### bibtex 命令

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `query` | str | 必填 | 搜索查询（论文标题） |
| `--num-results` | int | 1 | 返回条目数量 |

### 安装 CLI 工具

`google-scholar` 命令由 `google_scholar_mcp` 包提供，安装方式：

```bash
# Via uv (recommended)
uv tool install google_scholar_mcp

# Via pip
pip install google_scholar_mcp
```

安装后即可在任意目录直接使用 `google-scholar` 命令。

---

## 🛡️ 优化特性

### CAPTCHA 验证码处理

本项目对 scholarly 库进行了优化，解决了遇到 Google Scholar 验证码时程序卡住的问题：

1. **自动检测验证码**：当检测到验证码时，自动弹出浏览器窗口
2. **手动验证**：在弹出的浏览器中手动完成验证
3. **Cookie 同步**：验证完成后后续请求使用自动同步的 Cookie，避免频繁触发验证
4. **Cookie 持久化**：将 Cookie 保存到本地文件，下次启动时自动加载，减少验证码出现频率

> ⚠️ 如果遇到验证码，请在弹出的浏览器窗口中手动完成验证，程序会自动等待并继续执行。

### 📄 完整摘要获取

当 query 比较完整且精确时，系统会自动获取论文的完整 abstract，而不仅仅是截断的摘要片段。这对于需要详细了解单篇论文内容的场景非常有用。

---

## 📁 项目结构

```
Google-Scholar-MCP-Server/
├── src/
│   └── google_scholar_mcp/        # MCP Server 核心代码
│       ├── __init__.py            # 包入口
│       ├── __main__.py            # 主入口
│       ├── server.py              # MCP 服务器实现
│       ├── search.py              # 搜索逻辑
│       └── scholarly/             # 修改版 scholarly 库
│           ├── _navigator.py
│           ├── _proxy_generator.py
│           ├── _scholarly.py
│           └── ...
├── skill/
│   └── google-scholar-search/     # OpenClaw Skill 版本
│       └── SKILL.md               # 技能描述与使用指南
├── dist/
│   └── google-scholar-search.skill # 打包好的技能文件
├── requirements.txt               # 依赖列表
└── pyproject.toml                 # 项目配置（支持 uv/pip 安装）
```

---

## 🔧 依赖

- Python 3.10+
- mcp
- requests
- beautifulsoup4
- selenium
- httpx
- fake_useragent
- 等（详见 requirements.txt）

---

## 🤝 贡献

欢迎提交 Pull Request 和 Issue！

## 📄 许可证

本项目采用 MIT 许可证。

## ⚠️ 免责声明

本工具仅供学术研究使用。请遵守 Google Scholar 的服务条款，合理使用本工具。
