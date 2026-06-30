from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from prompt_recipe_smith.exceptions import TooManyBranchesError

MAX_BRANCHES = 3


@dataclass(frozen=True)
class PromptTemplate:
    """A fixed prompt form with named variables."""

    template: str

    def render(self, variables: dict[str, Any]) -> str:
        return self.template.format_map(_SafeFormatDict(variables))


@dataclass(frozen=True)
class PromptBranch:
    """One simple conditional path in a prompt recipe."""

    name: str
    description: str
    keyword: str | None = None
    template: PromptTemplate | None = None

    def matches(self, user_input: str) -> bool:
        if self.keyword is None:
            return False
        return self.keyword.casefold() in user_input.casefold()


@dataclass(frozen=True)
class PromptRecipe:
    """A reusable conditional prompt-building procedure."""

    name: str
    description: str
    final_template: PromptTemplate
    steps: tuple[str, ...] = ()
    branches: tuple[PromptBranch, ...] = ()
    examples: tuple[str, ...] = ()
    defaults: dict[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if len(self.branches) > MAX_BRANCHES:
            msg = f"PromptRecipe supports up to {MAX_BRANCHES} branches."
            raise TooManyBranchesError(msg)


@dataclass(frozen=True)
class PromptSession:
    """One prompt-building interaction."""

    recipe_name: str
    user_input: str
    selected_branch: str | None = None


@dataclass(frozen=True)
class PromptResult:
    """The result of applying a recipe to user input."""

    prompt: str
    recipe_name: str
    user_input: str
    selected_branch: str | None = None
    steps: tuple[str, ...] = ()
    provider: str = "chatgpt"

    def to_dict(self) -> dict[str, str | list[str] | None]:
        return {
            "prompt": self.prompt,
            "recipe_name": self.recipe_name,
            "user_input": self.user_input,
            "selected_branch": self.selected_branch,
            "steps": list(self.steps),
            "provider": self.provider,
        }


class _SafeFormatDict(dict[str, Any]):
    def __missing__(self, key: str) -> str:
        return "{" + key + "}"
