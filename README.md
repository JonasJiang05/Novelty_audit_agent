# Novelty_audit_agent
Agents for literature novelty audition based on deep agent harness and Deepseek API

一个基于 DeepSeek + LangChain DeepAgents 的**文献创新度审查 agent**：
给定一条"贡献声明（claim）"，自动检索 arXiv，判断该 claim 是否已被现有文献覆盖，
并诚实标注"needs_human（需人工核验）"。

## 依赖
- Python 3.12
- uv（推荐）或 pip

## 文件结构与依赖
config.py / protocol.py / tools.py（无依赖，叶子）
        ↓
agent.py（组装三者）
        ↓
main.py（唯一入口）

只跑 python main.py，其余文件都是被 import，不直接运行。

## 报错排查参考
| 报错 | 含义（先验） | 下一步验证 |
|---|---|---|
| KeyError: 'DEEPSEEK_API_KEY' | .env 没配或没加载 | 检查 .env 是否有该行 |
| ModuleNotFoundError: deepagents | 依赖没装 | uv pip install deepagents langchain-openai python-dotenv |
| 429 Too Many Requests | arXiv 限流 | 等几秒重试；别让 agent 空转 |
| timeout | 网络不稳 | 检查网络，重试 |

## 个性化接口清单
| 想改什么 | 文件 | 位置 |
|---|---|---|
| 审哪条 claim | config.py | CLAIM |
| 已知文献起点 | config.py | KNOWN_LITERATURE |
| 换 LLM 模型 | config.py | model |
| 换搜索平台 | tools.py | search_arxiv 函数体 |

**换平台原则**：search_arxiv 的输出字段（title/authors/arxiv/abstract）是"稳定接口"，
只要换平台后仍返回这些字段，agent、协议、入口都不需要改。

涉及的课程链接：https://datawhalechina.github.io/deepagents-in-action/

## 安装
1. 克隆/拷贝本项目；
2. 创建虚拟环境并装依赖：
   ```bash
   uv venv && uv pip install deepagents langchain-openai python-dotenv
