import runpy

from flask import Flask


def test_python_m_app_runs_development_server(monkeypatch):
    calls = []
    monkeypatch.setattr(Flask, "run", lambda self, **kwargs: calls.append((self, kwargs)))

    runpy.run_module("app", run_name="__main__")

    assert len(calls) == 1
    app, kwargs = calls[0]
    assert isinstance(app, Flask)
    assert kwargs == {"debug": True}


def test_importing_entrypoint_does_not_start_server(monkeypatch):
    calls = []
    monkeypatch.setattr(Flask, "run", lambda self, **kwargs: calls.append(kwargs))

    runpy.run_module("app.__main__", run_name="app.__main__")

    assert calls == []
