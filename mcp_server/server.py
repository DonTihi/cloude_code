from mcp.server.fastmcp import FastMCP

mcp = FastMCP("claude-agent-demo")


@mcp.tool()
def get_project_context() -> dict[str, str]:
    """Return project-specific context and engineering rules for the demo."""
    return {
        "project": "Claude Code Agent Demo",
        "language": "Python",
        "framework": "Flask",
        "test_framework": "pytest",
        "rule": "UI changes must not change application behavior.",
        "verification": "Run pytest after code changes and inspect git diff before committing.",
    }


@mcp.tool()
def get_demo_request() -> str:
    """Return the request used for the live agentic-development demonstration."""
    return (
        "Change the Calculate button from blue to red. "
        "Keep the existing behavior unchanged. "
        "Add or update tests if necessary, run the tests, "
        "and commit the change."
    )


if __name__ == "__main__":
    mcp.run()
