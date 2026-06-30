from prompt_recipe_smith import (
    PromptBranch,
    PromptBuilder,
    PromptQuestion,
    PromptRecipe,
    PromptTemplate,
)


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


def test_builder_selects_branch_with_multibyte_keyword() -> None:
    recipe = PromptRecipe(
        name="branched",
        description="A branched recipe.",
        final_template=PromptTemplate("Default: {user_input}"),
        branches=(
            PromptBranch(
                name="planning",
                description="Planning branch.",
                keywords=("計画",),
                template=PromptTemplate("Plan with care: {user_input}"),
            ),
        ),
    )

    result = PromptBuilder().build(recipe, "ワークショップを計画したい")

    assert result.prompt == "Plan with care: ワークショップを計画したい"
    assert result.selected_branch == "planning"


def test_builder_outputs_layered_prompt_with_answers() -> None:
    recipe = PromptRecipe(
        name="layered",
        description="A layered recipe.",
        final_template=PromptTemplate("Default: {user_input}"),
        questions=(
            PromptQuestion("goal", "What is the goal?"),
            PromptQuestion("audience", "Who is it for?"),
        ),
        layered_final_template=PromptTemplate(
            "Idea: {user_input}\n"
            "Goal: {answer_goal}\n"
            "Audience: {answer_audience}\n"
            "{clarifications}"
        ),
    )

    result = PromptBuilder().build_layered(
        recipe,
        "plan a workshop",
        {"goal": "Create an agenda", "audience": "new managers"},
    )

    assert "Goal: Create an agenda" in result.prompt
    assert "Audience: new managers" in result.prompt
    assert "- What is the goal?: Create an agenda" in result.prompt
    assert result.answers == (
        ("goal", "Create an agenda"),
        ("audience", "new managers"),
    )
