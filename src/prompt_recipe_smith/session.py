from __future__ import annotations

from dataclasses import dataclass

from prompt_recipe_smith.builder import PromptBuilder
from prompt_recipe_smith.models import (
    PromptQuestion,
    PromptRecipe,
    PromptResult,
    PromptSession,
)


@dataclass
class PromptSessionRunner:
    """Runs one prompt-building session."""

    recipe: PromptRecipe
    builder: PromptBuilder

    def run(self, user_input: str) -> PromptResult:
        return self.builder.build(self.recipe, user_input)

    def start(self, user_input: str) -> PromptSession:
        selected_branch = self.builder._select_branch(self.recipe, user_input)
        return PromptSession(
            recipe_name=self.recipe.name,
            user_input=user_input,
            selected_branch=selected_branch.name if selected_branch else None,
            next_question=self._question_at(0),
            complete=len(self.recipe.questions) == 0,
        )

    def answer(self, session: PromptSession, answer: str) -> PromptSession:
        if session.complete:
            return session

        next_question = session.next_question
        if next_question is None:
            return PromptSession(
                recipe_name=session.recipe_name,
                user_input=session.user_input,
                selected_branch=session.selected_branch,
                answers=session.answers,
                complete=True,
            )

        answers = (*session.answers, (next_question.key, answer))
        return PromptSession(
            recipe_name=session.recipe_name,
            user_input=session.user_input,
            selected_branch=session.selected_branch,
            answers=answers,
            next_question=self._question_at(len(answers)),
            complete=len(answers) >= len(self.recipe.questions),
        )

    def finish(self, session: PromptSession) -> PromptResult:
        return self.builder.build_layered(
            self.recipe,
            session.user_input,
            dict(session.answers),
        )

    def session_for(self, result: PromptResult) -> PromptSession:
        return PromptSession(
            recipe_name=result.recipe_name,
            user_input=result.user_input,
            selected_branch=result.selected_branch,
            answers=result.answers,
            complete=True,
        )

    def _question_at(self, index: int) -> PromptQuestion | None:
        if index >= len(self.recipe.questions):
            return None
        return self.recipe.questions[index]
