import pytest

from prompt_recipe_smith import (
    PromptBranch,
    PromptRecipe,
    PromptTemplate,
    TooManyBranchesError,
)


def test_template_rendering_replaces_known_variables() -> None:
    template = PromptTemplate("Explain {topic} for {audience}.")

    assert template.render({"topic": "AI", "audience": "beginners"}) == (
        "Explain AI for beginners."
    )


def test_template_rendering_keeps_unknown_variables() -> None:
    template = PromptTemplate("Explain {topic} with {missing}.")

    assert template.render({"topic": "AI"}) == "Explain AI with {missing}."


def test_recipe_creation_accepts_three_branches() -> None:
    recipe = PromptRecipe(
        name="three",
        description="Three branches are supported.",
        final_template=PromptTemplate("{user_input}"),
        branches=(
            PromptBranch("a", "A", "a"),
            PromptBranch("b", "B", "b"),
            PromptBranch("c", "C", "c"),
        ),
    )

    assert len(recipe.branches) == 3


def test_recipe_creation_rejects_more_than_three_branches() -> None:
    with pytest.raises(TooManyBranchesError, match="up to 3 branches"):
        PromptRecipe(
            name="four",
            description="Four branches are not supported.",
            final_template=PromptTemplate("{user_input}"),
            branches=(
                PromptBranch("a", "A", "a"),
                PromptBranch("b", "B", "b"),
                PromptBranch("c", "C", "c"),
                PromptBranch("d", "D", "d"),
            ),
        )
