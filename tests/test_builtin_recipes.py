from prompt_recipe_smith import PromptBuilder
from prompt_recipe_smith.recipes import clarify_idea_recipe


def test_builtin_recipe_builds_prompt() -> None:
    recipe = clarify_idea_recipe()
    result = PromptBuilder().build(recipe, "I want to learn about passwords")

    assert recipe.name == "clarify-idea"
    assert result.selected_branch == "learning"
    assert "beginner-friendly prompt" in result.prompt


def test_builtin_recipe_selects_japanese_planning_input() -> None:
    recipe = clarify_idea_recipe()
    result = PromptBuilder().build(recipe, "ワークショップを計画したい")

    assert result.selected_branch == "planning"
    assert "ワークショップを計画したい" in result.prompt
