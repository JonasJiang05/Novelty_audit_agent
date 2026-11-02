import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

# ===== 接口①：换 LLM 模型 =====
model = ChatOpenAI(
    model="deepseek-chat",                     # ← 改这里换模型名
    api_key=os.environ["DEEPSEEK_API_KEY"],    # ← 改这里换 key
    base_url="https://api.deepseek.com/v1",    # ← 改这里换服务商
)

# ===== 接口②：修改待审的 claim =====
CLAIM = ("多通道分布鲁棒优化中，两个风险通道的决策非冗余性"
         "可在求解前由原始输入识别（存在 Δr>0 的求解前充分条件）")

# ===== 接口③：可以加已知文献起点/依赖 =====
KNOWN_LITERATURE = [
    {"arxiv": "2105.00760", "note": "Zhen–Kuhn–Wiesemann 统一对偶框架"},
    {"arxiv": "1306.3437", "note": "Mehrotra–Papp cutting surface"},
    # ← 在这里加你已知的文献，agent 会优先对照这些
]
