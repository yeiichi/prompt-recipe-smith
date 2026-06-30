# PromptBuilder

`PromptBuilder` is the engine that applies a `PromptRecipe`.

It selects a simple branch when one matches the user's input, renders the chosen
template, applies provider-oriented formatting, and returns a `PromptResult`.
