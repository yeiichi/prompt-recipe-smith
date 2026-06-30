from __future__ import annotations

import argparse

from prompt_recipe_smith.builder import PromptBuilder
from prompt_recipe_smith.output import to_plain_text
from prompt_recipe_smith.recipes import clarify_idea_recipe


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="prompt-recipe-smith",
        description="Build effective chat prompts from vague ideas.",
    )
    parser.add_argument(
        "idea",
        nargs="?",
        help="A rough idea to turn into a clearer prompt.",
    )
    args = parser.parse_args()

    if args.idea is None:
        parser.print_help()
        return

    result = PromptBuilder().build(clarify_idea_recipe(), args.idea)
    print(to_plain_text(result))
