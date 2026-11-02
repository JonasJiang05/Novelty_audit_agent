import json
import urllib.request, urllib.parse
import xml.etree.ElementTree as ET
from langchain_core.tools import tool

@tool
def search_arxiv(query: str, max_results: int = 10) -> str:
    """在 arXiv 搜索论文。
    换平台：只改本函数体，保持返回 JSON 的字段不变
    （title / authors / arxiv / abstract），agent 无需改动。"""
    data = urllib.request.urlopen(url, timeout=30).read().decode("utf-8")
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(data)
    papers = []
    for e in root.findall("atom:entry", ns):
        papers.append({
            "title": " ".join((e.find("atom:title", ns).text or "").split()),
            "authors": [a.find("atom:name", ns).text for a in e.findall("atom:author", ns)],
            "arxiv": (e.find("atom:id", ns).text or "").split("/abs/")[-1],
            "abstract": " ".join((e.find("atom:summary", ns).text or "").split())[:300],
        })
    return json.dumps(papers, ensure_ascii=False, indent=2)
