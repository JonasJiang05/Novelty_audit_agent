import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com/v1",
)

CLAIM = ("多通道分布鲁棒优化中，两个风险通道的决策非冗余性"
         "可在求解前由原始输入识别（存在 Δr>0 的求解前充分条件）")
