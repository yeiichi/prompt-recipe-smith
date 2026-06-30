from prompt_recipe_smith import PromptBranch, PromptBuilder, PromptRecipe, PromptTemplate


def test_builder_outputs_default_prompt_when_no_branch_matches() -> None:
    recipe = PromptRecipe(
        name="basic",
        description="A basic recipe.",
        final_template=PromptTemplate("Improve this idea: {user_input}"),
    )

    result = PromptBuilder().build(recipe, "make dinner easier")

    assert result.prompt == "Improve this idea: make dinner easier"
    assert result.selected_branch is None
    assert result.provider == "chatgpt"


def test_builder_selects_first_matching_branch() -> None:
    recipe = PromptRecipe(
        name="branched",
        description="A branched recipe.",
        final_template=PromptTemplate("Default: {user_input}"),
        branches=(
            PromptBranch(
                name="writing",
                description="Writing branch.",
                keyword="write",
                template=PromptTemplate("Write with care: {user_input}"),
            ),
        ),
    )

    result = PromptBuilder().build(recipe, "write a note")

    assert result.prompt == "Write with care: write a note"
    assert result.selected_branch == "writing"
