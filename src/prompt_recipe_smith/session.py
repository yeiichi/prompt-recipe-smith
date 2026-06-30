from __future__ import annotations

from dataclasses import dataclass

from prompt_recipe_smith.builder import PromptBuilder
from prompt_recipe_smith.models import PromptRecipe, PromptResult, PromptSession


@dataclass
class PromptSessionRunner:
    """Runs one prompt-building session."""

    recipe: PromptRecipe
    builder: PromptBuilder

    def run(self, user_input: str) -> PromptResult:
        return self.builder.build(self.recipe, user_input)

    def session_for(self, result: PromptResult) -> PromptSession:
        return PromptSession(
            recipe_name=result.recipe_name,
            user_input=result.user_input,
            selected_branch=result.selected_branch,
        )
