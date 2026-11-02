from deepagents import create_deep_agent
from config import model
from protocol import AUDIT_PROTOCOL
from tools import search_arxiv

agent = create_deep_agent(
    model=model,
    tools=[search_arxiv],
    system_prompt=AUDIT_PROTOCOL,
)
