from __future__ import annotations

from prompt_recipe_smith.models import PromptResult


def to_plain_text(result: PromptResult) -> str:
    return result.prompt
