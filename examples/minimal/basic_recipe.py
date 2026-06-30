from prompt_recipe_smith import PromptBuilder
from prompt_recipe_smith.output import to_plain_text
from prompt_recipe_smith.recipes import clarify_idea_recipe


def main() -> None:
    recipe = clarify_idea_recipe()
    result = PromptBuilder().build(recipe, "I want to plan a small workshop")
    print(to_plain_text(result))


if __name__ == "__main__":
    main()
