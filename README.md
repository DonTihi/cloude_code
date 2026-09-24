# Claude Code Agent Demo

A tiny Flask application designed for a live demonstration of agentic software development with Claude Code.

## What the demo shows

1. Claude Code receives a normal development request.
2. It explores the repository instead of being given the exact file.
3. It uses project instructions from `CLAUDE.md`.
4. It can use a local MCP server for project-specific context.
5. It edits the code.
6. It runs the existing tests.
7. It reviews the Git diff.
8. It commits the change.

## Demo request

> Change the Calculate button from blue to red. Keep the existing behavior unchanged. Add or update tests if necessary, run the tests, and commit the change.

## Run the application

Create a virtual environment and install dependencies:

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run the app:

```powershell
python -m app
```

Open http://127.0.0.1:5000 in a browser.

## Project layout

```text
app/
  __init__.py        application factory (create_app)
  __main__.py        entry point for `python -m app`
  calculator.py      input parsing and arithmetic
  routes.py          Flask routes
  templates/         HTML templates
  static/            CSS
tests/               pytest tests (fixtures in conftest.py)
mcp_server/          local MCP server for project context
```

## Run tests

```powershell
pytest
```

## MCP

The project includes a local MCP server in `mcp_server/server.py`. Claude Code can launch it over stdio using the project `.mcp.json` configuration.

Check the server:

```powershell
claude mcp list
```

Inside Claude Code, use `/mcp` to inspect the connection and available tools.

## Git

The demo should end with a normal Git commit containing the UI change.
