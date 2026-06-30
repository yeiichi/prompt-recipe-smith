from prompt_recipe_smith import PromptBuilder
from prompt_recipe_smith.output import to_plain_text
from prompt_recipe_smith.recipes import clarify_idea_recipe
from prompt_recipe_smith.session import PromptSessionRunner


def main() -> None:
    recipe = clarify_idea_recipe()
    runner = PromptSessionRunner(recipe=recipe, builder=PromptBuilder())
    session = runner.start("I want to plan a small workshop")

    while not session.complete and session.next_question is not None:
        answer = input(f"{session.next_question.text}\n> ")
        session = runner.answer(session, answer)

    result = runner.finish(session)
    print(to_plain_text(result))


if __name__ == "__main__":
    main()
