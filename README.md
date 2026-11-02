# Novelty_audit_agent
Agents for literature novelty audition based on deep agent harness

一个基于 DeepSeek + LangChain DeepAgents 的**文献创新度审查 agent**：
给定一条"贡献声明（claim）"，自动检索 arXiv，判断该 claim 是否已被现有文献覆盖，
并诚实标注"needs_human（需人工核验）"。

## 依赖
- Python 3.12
- uv（推荐）或 pip

## 安装
1. 克隆/拷贝本项目；
2. 创建虚拟环境并装依赖：
   ```bash
   uv venv && uv pip install deepagents langchain-openai python-dotenv
