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
    }
