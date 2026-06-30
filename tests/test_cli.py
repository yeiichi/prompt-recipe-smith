import builtins
import sys

from prompt_recipe_smith import cli
from prompt_recipe_smith.cli import main


def test_cli_asks_layered_questions_by_default(
    monkeypatch,
    capsys,
) -> None:
    answers = iter(
        (
            "議題を整理する",
            "新任マネージャー向け",
            "日本語で簡潔に",
        )
    )
    prompts: list[str] = []

    def fake_input(prompt: str = "") -> str:
        prompts.append(prompt)
        return next(answers)

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "prompt-recipe-smith",
            "ワークショップを",
            "計画したい",
        ],
    )
    monkeypatch.setattr(builtins, "input", fake_input)

    main()

    captured = capsys.readouterr()

    assert len(prompts) == 3
    assert "Create a strong prompt for a chat agent." in captured.out
    assert "ワークショップを 計画したい" in captured.out
    assert "Detected focus: planning" in captured.out
    assert "議題を整理する" in captured.out
    assert "新任マネージャー向け" in captured.out
    assert "日本語で簡潔に" in captured.out


def test_cli_configures_text_stream_as_utf8() -> None:
    class FakeStream:
        encoding: str | None = None
        errors: str | None = None

        def reconfigure(self, *, encoding: str, errors: str) -> None:
            self.encoding = encoding
            self.errors = errors

    stream = FakeStream()

    cli._configure_text_stream(stream)  # type: ignore[arg-type]

    assert stream.encoding == "utf-8"
    assert stream.errors == "replace"
