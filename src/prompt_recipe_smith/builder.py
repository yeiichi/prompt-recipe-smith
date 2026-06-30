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

    def build_layered(
        self,
        recipe: PromptRecipe,
        user_input: str,
        answers: dict[str, str],
        variables: dict[str, Any] | None = None,
    ) -> PromptResult:
        selected_branch = self._select_branch(recipe, user_input)
        template = recipe.layered_final_template or recipe.final_template
        answer_items = tuple(
            (question.key, answers.get(question.key, ""))
            for question in recipe.questions
        )
        answer_variables = {
            f"answer_{key}": answer for key, answer in answer_items
        }

        render_variables: dict[str, Any] = {
            **recipe.defaults,
            **(variables or {}),
            **answer_variables,
            "user_input": user_input,
            "recipe_name": recipe.name,
            "branch_name": selected_branch.name if selected_branch else "",
            "clarifications": self._format_answers(recipe, answer_items),
        }
        prompt = self.provider.adapt(template.render(render_variables))

        return PromptResult(
            prompt=prompt,
            recipe_name=recipe.name,
            user_input=user_input,
            selected_branch=selected_branch.name if selected_branch else None,
            steps=recipe.steps,
            provider=self.provider.name,
            answers=answer_items,
        )

    def _select_branch(
        self, recipe: PromptRecipe, user_input: str
    ) -> PromptBranch | None:
        for branch in recipe.branches:
            if branch.matches(user_input):
                return branch
        return None

    def _format_answers(
        self,
        recipe: PromptRecipe,
        answer_items: tuple[tuple[str, str], ...],
    ) -> str:
        question_text_by_key = {
            question.key: question.text for question in recipe.questions
        }
        lines = []
        for key, answer in answer_items:
            question_text = question_text_by_key.get(key, key)
            lines.append(f"- {question_text}: {answer}")
        return "\n".join(lines)
