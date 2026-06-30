# prompt-recipe-smith

[![PyPI](https://img.shields.io/pypi/v/prompt-recipe-smith.svg)](https://pypi.org/project/prompt-recipe-smith/)
[![GitHub](https://img.shields.io/badge/GitHub-yeiichi%2Fprompt--recipe--smith-181717?logo=github)](https://github.com/yeiichi/prompt-recipe-smith)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yeiichi/prompt-recipe-smith/blob/main/examples/prompt_recipe_smith_colab_demo.ipynb)
[![Python](https://img.shields.io/pypi/pyversions/prompt-recipe-smith.svg)](https://pypi.org/project/prompt-recipe-smith/)
[![Tests](https://img.shields.io/badge/tests-pytest%20passing-brightgreen.svg)](https://github.com/yeiichi/prompt-recipe-smith)

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

The command-line app asks three clarification questions, then prints the final
prompt for the chat agent:

```bash
prompt-recipe-smith I want to plan a small workshop
```

## One-shot Builder

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

## Layered Questions

Use `PromptSessionRunner` when you want the same three-question flow in Python:

The built-in clarification questions are written in English, but users can
answer them in any language. The CLI, API, and JSON output preserve Unicode
text such as Japanese, Chinese, French, and Arabic.

```python
from prompt_recipe_smith import PromptBuilder
from prompt_recipe_smith.recipes import clarify_idea_recipe
from prompt_recipe_smith.session import PromptSessionRunner

runner = PromptSessionRunner(
    recipe=clarify_idea_recipe(),
    builder=PromptBuilder(),
)
session = runner.start("I want to plan a small workshop")

session = runner.answer(session, "A one-day facilitation agenda")
session = runner.answer(session, "First-time team leads")
session = runner.answer(session, "Keep it practical and under six hours")

result = runner.finish(session)
print(result.prompt)
```

## Keyword Matching

Branch keywords are internal hints used to select a simple recipe path such as
writing, learning, or planning. The built-in keyword data is defined in
`src/prompt_recipe_smith/recipes/builtin.py`, and the matching logic is handled
by `src/prompt_recipe_smith/models.py`.

## Notebook Demo

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yeiichi/prompt-recipe-smith/blob/main/examples/prompt_recipe_smith_colab_demo.ipynb)

A Google Colab-friendly demo notebook is available at
`examples/prompt_recipe_smith_colab_demo.ipynb`. It shows installation, one-shot
prompt building, the three-question layered flow, multilingual answers, and JSON
output.

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
  "provider": "chatgpt",
  "answers": {}
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

## Documentation CI

GitHub Actions builds the Sphinx docs when documentation-related files change.
On pushes to `main`, a successful docs build triggers a Read the Docs webhook.

Configure these repository secrets before relying on the RTD trigger:

- `RTD_WEBHOOK_URL`: the Read the Docs generic incoming webhook URL.
- `RTD_WEBHOOK_TOKEN`: the token shown for that RTD webhook integration.

## Scope

The first version supports plain text and JSON output. JSONL, Gemini,
Anthropic, and Django integrations are future extension targets. The provider
layer does not call external APIs.
