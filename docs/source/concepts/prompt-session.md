# PromptSession

A `PromptSession` represents one prompt-building interaction.

It stores the recipe name, the user's rough input, the selected branch, the
answers collected so far, the next clarification question, and whether the
session is complete.

The built-in session flow asks three clarification questions in English. Users
can answer those questions in any language; their answers are carried into the
final prompt unchanged.
