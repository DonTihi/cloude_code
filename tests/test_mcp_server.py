import asyncio
import runpy
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from mcp_server import server

SERVER_PATH = Path(__file__).resolve().parents[1] / "mcp_server" / "server.py"


def test_server_registers_expected_tools():
    tools = asyncio.run(server.mcp.list_tools())

    assert {tool.name for tool in tools} == {"get_project_context", "get_demo_request"}


def test_get_project_context_describes_project():
    context = server.get_project_context()

    assert context["project"] == "Claude Code Agent Demo"
    assert context["framework"] == "Flask"
    assert context["test_framework"] == "pytest"
    assert all(isinstance(value, str) and value for value in context.values())


def test_get_demo_request_mentions_button_and_tests():
    request = server.get_demo_request()

    assert "Calculate button" in request
    assert "run the tests" in request


def test_running_server_script_starts_mcp(monkeypatch):
    calls = []
    monkeypatch.setattr(FastMCP, "run", lambda self, *args, **kwargs: calls.append(self))

    runpy.run_path(str(SERVER_PATH), run_name="__main__")

    assert len(calls) == 1
    assert calls[0].name == "claude-agent-demo"
