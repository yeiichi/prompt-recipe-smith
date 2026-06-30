from __future__ import annotations

import argparse
import sys
from typing import TextIO

from prompt_recipe_smith.builder import PromptBuilder
from prompt_recipe_smith.output import to_plain_text
from prompt_recipe_smith.recipes import clarify_idea_recipe
from prompt_recipe_smith.session import PromptSessionRunner


def main() -> None:
    _configure_text_streams()

    parser = argparse.ArgumentParser(
        prog="prompt-recipe-smith",
        description="Build effective chat prompts from vague ideas.",
    )
    parser.add_argument(
        "idea",
        nargs="*",
        help="A rough idea to turn into a clearer prompt.",
    )
    args = parser.parse_args()

    if not args.idea:
        parser.print_help()
        return

    idea = " ".join(args.idea)

    recipe = clarify_idea_recipe()
    builder = PromptBuilder()
    runner = PromptSessionRunner(recipe=recipe, builder=builder)
    session = runner.start(idea)
    while not session.complete and session.next_question is not None:
        answer = input(f"{session.next_question.text}\n> ")
        session = runner.answer(session, answer)
    result = runner.finish(session)

    print(to_plain_text(result))


def _configure_text_streams() -> None:
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        _configure_text_stream(stream)


def _configure_text_stream(stream: TextIO) -> None:
    reconfigure = getattr(stream, "reconfigure", None)
    if reconfigure is None:
        return
    reconfigure(encoding="utf-8", errors="replace")
