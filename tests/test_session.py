from prompt_recipe_smith import PromptBuilder
from prompt_recipe_smith.recipes import clarify_idea_recipe
from prompt_recipe_smith.session import PromptSessionRunner


def test_session_runner_asks_three_questions_then_finishes() -> None:
    runner = PromptSessionRunner(
        recipe=clarify_idea_recipe(),
        builder=PromptBuilder(),
    )

    session = runner.start("I want to plan a small workshop")

    assert session.selected_branch == "planning"
    assert session.next_question is not None
    assert session.next_question.key == "outcome"

    session = runner.answer(session, "A one-day facilitation agenda")
    assert session.next_question is not None
    assert session.next_question.key == "context"

    session = runner.answer(session, "First-time team leads")
    assert session.next_question is not None
    assert session.next_question.key == "constraints"

    session = runner.answer(session, "Keep it practical and under six hours")
    assert session.complete is True
    assert session.next_question is None

    result = runner.finish(session)

    assert result.selected_branch == "planning"
    assert "A one-day facilitation agenda" in result.prompt
    assert "First-time team leads" in result.prompt
    assert "Keep it practical and under six hours" in result.prompt
