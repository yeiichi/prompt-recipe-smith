# PromptRecipe

A `PromptRecipe` is a reusable conditional prompt-building procedure.

It can contain metadata, steps, examples, defaults, up to three branches, and
up to three layered clarification questions. It is useful when the user starts
from a vague idea and needs help shaping a better request.

The built-in recipe asks its clarification questions in English, but users can
answer in any language. The CLI, API, and JSON output preserve Unicode text
such as Japanese, Chinese, French, and Arabic.

Branch keywords are internal hints used to select a simple recipe path such as
writing, learning, or planning. The built-in keyword data is defined in
``src/prompt_recipe_smith/recipes/builtin.py``.
