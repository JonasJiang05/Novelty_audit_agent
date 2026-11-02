import os, datetime, sys
from agent import agent
from config import CLAIM

PROMPT = f"审这条 claim：'{CLAIM}'。用 search_arxiv 检索 DRO/redundant constraints 相关文献，按协议输出。"

def run():
    result = agent.invoke({"messages": [("user", PROMPT)]})
    output = result["messages"][-1].content
    print(output)
    os.makedirs("output", exist_ok=True)
    with open(f"output/demo_{datetime.date.today()}.md", "w", encoding="utf-8") as f:
        f.write(output)

def run_streaming():
    for chunk in agent.stream({"messages": [("user", PROMPT)]}, stream_mode="updates"):
        print(chunk)

if __name__ == "__main__":
    run_streaming() if "--stream" in sys.argv else run()
