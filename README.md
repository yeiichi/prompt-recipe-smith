# prompt-recipe-smith

`prompt-recipe-smith` is a small Python package for building effective chat prompts
from vague user ideas.

It is designed for people who may not know AI, software, or prompt engineering
terms. The package helps turn a rough thought into a clearer prompt by applying
a reusable prompt-building procedure.

## PromptTemplate vs PromptRecipe

A `PromptTemplate` is a fixed prompt form with variables:

```python
from prompt_recipe_smith import PromptTemplate

template = PromptTemplate("Explain {topic} for a beginner.")
print(template.render({"topic": "email security"}))
```

A `PromptRecipe` is more than a template. It can include steps, defaults,
examples, clarification ideas, and up to three simple branches. A
`PromptBuilder` applies the recipe to a user's rough input and returns a
`PromptResult`.

## Installation

Install from PyPI:

```bash
uv add prompt-recipe-smith
```

## Minimal Example

```python
from prompt_recipe_smith import PromptBuilder
from prompt_recipe_smith.output import to_json, to_plain_text
from prompt_recipe_smith.recipes import clarify_idea_recipe

recipe = clarify_idea_recipe()
result = PromptBuilder().build(recipe, "I want to write a polite follow-up email")

print(to_plain_text(result))
print(to_json(result))
```

## Plain Text Output

```text
Help me turn this writing idea into a clear request:
I want to write a polite follow-up email

Ask up to three plain-language clarification questions, then draft an improved prompt.
```

## JSON Output

```json
{
  "prompt": "Help me turn this writing idea into a clear request:\nI want to write a polite follow-up email\n\nAsk up to three plain-language clarification questions, then draft an improved prompt.",
  "recipe_name": "clarify-idea",
  "user_input": "I want to write a polite follow-up email",
  "selected_branch": "writing",
  "steps": [
    "Restate the user's rough idea.",
    "Ask for the missing context only if it matters.",
    "Produce a practical prompt the user can paste into chat."
  ],
  "provider": "chatgpt"
}
```

## Development

```bash
uv sync
uv run pytest
uv run ruff check .
uv run mypy src
uv build
```

## Scope

The first version supports plain text and JSON output. JSONL, Gemini,
Anthropic, and Django integrations are future extension targets. The provider
layer does not call external APIs.
