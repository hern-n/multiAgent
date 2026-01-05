import requests
from typing import Iterator, Optional


def ask_agent(question: str, url: str = "http://127.0.0.1:5000/agents", timeout: Optional[float] = 30.0) -> str:
    """Send `question` to the API and return the full response text.

    Defaults to posting to http://127.0.0.1:5000/agents. Raises for HTTP errors.
    """
    resp = requests.post(url, json={"question": question}, stream=True, timeout=timeout)
    resp.raise_for_status()

    parts = []
    # read streamed content as text
    for chunk in resp.iter_content(chunk_size=None, decode_unicode=True):
        if chunk:
            parts.append(chunk)

    return "".join(parts)


def ask_agent_stream(question: str, url: str = "http://127.0.0.1:5000/agents", timeout: Optional[float] = 30.0) -> Iterator[str]:
    """POST and yield response chunks as they arrive (text chunks)."""
    resp = requests.post(url, json={"question": question}, stream=True, timeout=timeout)
    resp.raise_for_status()

    for chunk in resp.iter_content(chunk_size=None, decode_unicode=True):
        if chunk:
            yield chunk


if __name__ == "__main__":

    q = "Primero dime que modelo eres, y depues: Puesdes hacerme Fibonnacci en python" 
    
    for chunk in ask_agent_stream(q):
        print(chunk, end="")
    print("\n")
