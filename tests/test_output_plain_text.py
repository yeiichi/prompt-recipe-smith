from prompt_recipe_smith.models import PromptResult
from prompt_recipe_smith.output import to_plain_text


def test_plain_text_output_returns_prompt() -> None:
    result = PromptResult(
        prompt="A useful prompt.",
        recipe_name="recipe",
        user_input="rough idea",
    )

    assert to_plain_text(result) == "A useful prompt."
