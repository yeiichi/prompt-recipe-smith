# PromptBuilder

`PromptBuilder` is the engine that applies a `PromptRecipe`.

It selects a simple branch when one matches the user's input, renders the chosen
template, applies provider-oriented formatting, and returns a `PromptResult`.

Branch matching is handled by ``PromptBranch.matches()`` in
``src/prompt_recipe_smith/models.py``. The built-in keyword values used by the
default recipe are defined in
``src/prompt_recipe_smith/recipes/builtin.py``.
