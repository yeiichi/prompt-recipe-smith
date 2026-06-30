from __future__ import annotations

from typing import Any

from prompt_recipe_smith.models import PromptBranch, PromptRecipe, PromptResult
from prompt_recipe_smith.providers import ChatGPTProvider, PromptProvider


class PromptBuilder:
    """Engine that applies prompt recipes."""

    def __init__(self, provider: PromptProvider | None = None) -> None:
        self.provider = provider or ChatGPTProvider()

    def build(
        self,
        recipe: PromptRecipe,
        user_input: str,
        variables: dict[str, Any] | None = None,
    ) -> PromptResult:
        selected_branch = self._select_branch(recipe, user_input)
        template = selected_branch.template if selected_branch else None
        template = template or recipe.final_template

        render_variables: dict[str, Any] = {
            **recipe.defaults,
            **(variables or {}),
            "user_input": user_input,
            "recipe_name": recipe.name,
            "branch_name": selected_branch.name if selected_branch else "",
        }
        prompt = self.provider.adapt(template.render(render_variables))

        return PromptResult(
            prompt=prompt,
            recipe_name=recipe.name,
            user_input=user_input,
            selected_branch=selected_branch.name if selected_branch else None,
            steps=recipe.steps,
            provider=self.provider.name,
        )

    def _select_branch(
        self, recipe: PromptRecipe, user_input: str
    ) -> PromptBranch | None:
        for branch in recipe.branches:
            if branch.matches(user_input):
                return branch
        return None
