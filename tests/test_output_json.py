import json

from prompt_recipe_smith.models import PromptResult
from prompt_recipe_smith.output import to_json


def test_json_output_serializes_result() -> None:
    result = PromptResult(
        prompt="A useful prompt.",
        recipe_name="recipe",
        user_input="rough idea",
        selected_branch="branch",
        steps=("one", "two"),
    )

    payload = json.loads(to_json(result))

    assert payload == {
        "prompt": "A useful prompt.",
        "recipe_name": "recipe",
        "user_input": "rough idea",
        "selected_branch": "branch",
        "steps": ["one", "two"],
        "provider": "chatgpt",
        "answers": {},
    }


def test_json_output_preserves_multibyte_text() -> None:
    result = PromptResult(
        prompt="ワークショップを計画したい",
        recipe_name="recipe",
        user_input="議題を整理する",
    )

    payload = to_json(result)

    assert "ワークショップを計画したい" in payload
    assert "\\u30ef" not in payload
